
from aiohttp import web
import asyncio

from routes import setupRoutes
from setup import setupDB

loop = asyncio.get_event_loop()
db = loop.run_until_complete(setupDB())
app = web.Application()

app['db'] = db
setupRoutes(app)
web.run_app(app)
