import pymongo
import json
from bson import json_util
from aiohttp import web

from setup import setupDB


async def handle(request):
    response = {"status": "SUCCESS"}
    return web.Response(text = json.dumps(response), status=200)


async def getRequest(request):
    try:
        timestamp = request.match_info.get('time_stamp')
        timestamp = float(timestamp)
        db = request.app['db']
 
        document = list(db.logger.find({"time_stamp": { "$gt" : timestamp}}).sort("time_stamp"))

        if not document:
            return web.HTTPNotFound(text="No logs found for the timestamp: {!r}".format(timestamp))

        response_obj = json.loads(json_util.dumps(document)) 
        return web.Response(text=json.dumps(response_obj), status=200)    
        
    except: 
        response_obj = {'status': 'failed'}
        web.Response(text=json.dumps(request), status=500)
