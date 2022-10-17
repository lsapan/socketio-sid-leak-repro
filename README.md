### Socketio SID Leak Repro

#### Description
This is a very minimal repro to demonstrate SID leaking with rooms. There is an emitter that sends out a `test_event` every 5 seconds to the `test_room`. When a client connects, the default namespace automatically adds them to the `test_room`. You can observe that these events are making it to the client in the JavaScript console.

When you close your browser window, you will see that the server is aware of the disconnect:
```
pubsub message: disconnect
```

However, you'll then begin to see messages like:
```
emitter | Emitting to test_room...
server  | pubsub message: emit
server  | Cannot send to sid C4384ZtK0FpbJExOAAAA
emitter | Emitting to test_room...
server  | pubsub message: emit
server  | Cannot send to sid C4384ZtK0FpbJExOAAAA
```

As you can see, SIDs are not being cleaned up from the room after they are disconnected. You can imagine that this list quickly grows out of control as clients connect and disconnect.

#### Usage
Ensure you have a local redis server running.

If you use foreman or overmind, run `foreman start` or `overmind start`, respectively. This will start up the socketio server, as well as the emitter process.

If you don't use either of those, you can also start them separately:
```bash
python server.py
python emitter.py
```

Once the server is running, open up `index.html` in your browser to start the connection, and then close it to observe the leak. You can repeat this as many times as you like to observe the leak growing larger.
