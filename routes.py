from views import handle, getRequest

def setupRoutes(app):
    app.router.add_get('/', handle)
    app.router.add_get('/{time_stamp}', getRequest)