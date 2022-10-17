import socketio


class TestNamespace(socketio.Namespace):
    def on_connect(self, sid, environ):
        self.enter_room(sid, 'test_room')
