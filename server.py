import eventlet

from config import SOCKETIO_REDIS_URL


if __name__ == '__main__':
    eventlet.monkey_patch(os=True, select=True, socket=True, time=True)

    import socketio
    mgr = socketio.RedisManager(SOCKETIO_REDIS_URL)
    sio = socketio.Server(client_manager=mgr, cors_allowed_origins='*', logger=True, engineio_logger=True)

    from namespace import TestNamespace
    sio.register_namespace(TestNamespace('/'))

    app = socketio.WSGIApp(sio)

    eventlet.wsgi.server(eventlet.listen(('', 7069)), app, max_size=4096)
