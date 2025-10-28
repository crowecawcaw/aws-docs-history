# Using the IVS Chat Client Messaging Android SDK

This document takes you through the steps involved in using the Amazon IVS chat client messaging Android SDK.

## Initialize a Chat Room

Instance

Create an instance of the `ChatRoom` class. This requires passing
`regionOrUrl`, which typically is the AWS region in which your chat
room is hosted, and `tokenProvider` which is the token-fetching method
created in the previous step.

```
val room = ChatRoom(
    regionOrUrl = "us-west-2",
    tokenProvider = ::fetchChatToken
)
```

Next, create a listener object that will implement handlers for chat related
events, and assign it to the `room.listener` property:

```
private val roomListener = object : ChatRoomListener {
    override fun onConnecting(room: ChatRoom) {
      // Called when room is establishing the initial connection or reestablishing connection after socket failure/token expiration/etc
    }

    override fun onConnected(room: ChatRoom) {
        // Called when connection has been established
    }

    override fun onDisconnected(room: ChatRoom, reason: DisconnectReason) {
        // Called when a room has been disconnected
    }

    override fun onMessageReceived(room: ChatRoom, message: ChatMessage) {
        // Called when chat message has been received
    }

    override fun onEventReceived(room: ChatRoom, event: ChatEvent) {
        // Called when chat event has been received
    }

    override fun onDeleteMessage(room: ChatRoom, event: DeleteMessageEvent) {
       // Called when DELETE_MESSAGE event has been received
    }
}

val room = ChatRoom(
    region = "us-west-2",
    tokenProvider = ::fetchChatToken
)

room.listener = roomListener // <- add this line

// ...
```

The last step of basic initialization is connecting to the specific room by
establishing a WebSocket connection. To do this, call the `connect()`
method within the room instance. We recommend doing so in the `onResume()` lifecycle method to make sure it keeps a connection if your app resumes from
the background.

```
room.connect()
```

The SDK will try to establish a connection to a chat room encoded in the chat
token received from your server. If it fails, it will try to reconnect the number of
times specified in the room instance.

## Perform Actions in a Chat Room

The `ChatRoom` class has actions for sending and deleting messages and
disconnecting other users. These actions accept an optional callback parameter that
allows you to get request confirmation or rejection notifications.

### Sending a

Message

For this request, you must have the `SEND_MESSAGE` capability
encoded in your chat token.

To trigger a send-message request:

```
val request = SendMessageRequest("Test Echo")
room.sendMessage(request)
```

To get a confirmation/rejection of the request, provide a callback as a second
parameter:

```
room.sendMessage(request, object : SendMessageCallback {
   override fun onConfirmed(request: SendMessageRequest, response: ChatMessage) {
      // Message was successfully sent to the chat room.
   }
   override fun onRejected(request: SendMessageRequest, error: ChatError) {
      // Send-message request was rejected. Inspect the `error` parameter for details.
   }
})
```

### Deleting a

Message

For this request, you must have the DELETE_MESSAGE capability encoded in your
chat token.

To trigger a delete-message request:

```
val request = DeleteMessageRequest(messageId, "Some delete reason")
room.deleteMessage(request)
```

To get a confirmation/rejection of the request, provide a callback as a second
parameter:

```
room.deleteMessage(request, object : DeleteMessageCallback {
   override fun onConfirmed(request: DeleteMessageRequest, response: DeleteMessageEvent) {
      // Message was successfully deleted from the chat room.
   }
   override fun onRejected(request: DeleteMessageRequest, error: ChatError) {
      // Delete-message request was rejected. Inspect the `error` parameter for details.
   }
})
```

### Disconnecting

Another User

For this request, you must have the `DISCONNECT_USER` capability
encoded in your chat token.

To disconnect another user for moderation purposes:

```
val request = DisconnectUserRequest(userId, "Reason for disconnecting user")
room.disconnectUser(request)
```

To get confirmation/rejection of the request, provide a callback as a second
parameter:

```
room.disconnectUser(request, object : DisconnectUserCallback {
   override fun onConfirmed(request: SendMessageRequest, response: ChatMessage) {
      // User was disconnected from the chat room.
   }
   override fun onRejected(request: SendMessageRequest, error: ChatError) {
      // Disconnect-user request was rejected. Inspect the `error` parameter for details.
   }
})
```

## Disconnect from a Chat Room

To close your connection to the chat room, call the `disconnect()`
method on the room instance:

```
room.disconnect()
```

Because the WebSocket connection will stop working after a short time when the
application is in a background state, we recommend that you manually
connect/disconnect when transitioning from/to a background state. To do so, match
the `room.connect()` call in the `onResume()` lifecycle
method, on Android `Activity` or `Fragment`, with a
`room.disconnect()` call in the `onPause()` lifecycle
method.
