import time

import socketio

from config import SOCKETIO_REDIS_URL

external_sio = socketio.RedisManager(SOCKETIO_REDIS_URL, write_only=True)

if __name__ == '__main__':
    while True:
        print('Emitting to test_room...')
        external_sio.emit('test_event', 'test_data', namespace='/', room='test_room')
        time.sleep(5)
