import os

SOCKETIO_REDIS_URL = f'redis://{os.environ.get("REDIS_HOST", "localhost")}:6379/1'
