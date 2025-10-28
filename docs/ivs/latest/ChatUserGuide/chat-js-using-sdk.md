# Using the IVS Chat Client Messaging JavaScript SDK

This document takes you through the steps involved in using the Amazon IVS chat client messaging
JavaScript SDK.

## Initialize a Chat Room

Instance

Create an instance of the `ChatRoom` class. This requires passing
`regionOrUrl` (the AWS region where your chat room is hosted) and
`tokenProvider` (the token-fetching method will be created in the
next step):

```
const room = new ChatRoom({
  regionOrUrl: 'us-west-2',
  tokenProvider: tokenProvider,
});
```

## Token Provider Function

Create an asynchronous token-provider function that fetches a chat token
from your backend:

```
type ChatTokenProvider = () => Promise<ChatToken>;
```

The function should accept no parameters and return a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise") containing a chat
token object:

```
type ChatToken = {
  token: string;
  sessionExpirationTime?: Date;
  tokenExpirationTime?: Date;
}
```

This function is needed to [initialize the
ChatRoom object](#chat-js-initialize-room "#chat-js-initialize-room"). Below, fill in the `<token>` and
`<date-time>` fields with values received from your
backend:

```
// You will need to fetch a fresh token each time this method is called by
// the IVS Chat Messaging SDK, since each token is only accepted once.
function tokenProvider(): Promise<ChatToken> {
  // Call your backend to fetch chat token from IVS Chat endpoint:
  // e.g. const token = await appBackend.getChatToken()
  return {
    token: "<token>",
    sessionExpirationTime: new Date("<date-time>"),
    tokenExpirationTime: new Date("<date-time>")
  }
}
```

Remember to pass the `tokenProvider` to the ChatRoom
constructor. ChatRoom refreshes the token when the connection is interrupted or
session expires. Do not use the `tokenProvider` to store a token
anywhere; the ChatRoom handles it for you.

## Receive Events

Next, subscribe to chat-room events to receive lifecycle events, as well as messages and events delivered in the chat room:

```
/**
* Called when room is establishing the initial connection or reestablishing
* connection after socket failure/token expiration/etc
*/
const unsubscribeOnConnecting = room.addListener('connecting', () => { });

/** Called when connection has been established. */
const unsubscribeOnConnected = room.addListener('connect', () => { });

/** Called when a room has been disconnected. */
const unsubscribeOnDisconnected = room.addListener('disconnect', () => { });

/** Called when a chat message has been received. */
const unsubscribeOnMessageReceived = room.addListener('message', (message) => {
 /* Example message:
  * {
  *   id: "5OPsDdX18qcJ",
  *   sender: { userId: "user1" },
  *   content: "hello world",
  *   sendTime: new Date("2022-10-11T12:46:41.723Z"),
  *   requestId: "d1b511d8-d5ed-4346-b43f-49197c6e61de"
  * }
  */
});

/** Called when a chat event has been received. */
const unsubscribeOnEventReceived = room.addListener('event', (event) => {
 /* Example event:
  * {
  *   id: "5OPsDdX18qcJ",
  *   eventName: "customEvent,
  *   sendTime: new Date("2022-10-11T12:46:41.723Z"),
  *   requestId: "d1b511d8-d5ed-4346-b43f-49197c6e61de",
  *   attributes: { "Custom Attribute": "Custom Attribute Value" }
  * }
  */
});

/** Called when `aws:DELETE_MESSAGE` system event has been received. */
const unsubscribeOnMessageDelete = room.addListener('messageDelete', (deleteMessageEvent) => {
 /* Example delete message event:
  * {
  *   id: "AYk6xKitV4On",
  *   messageId: "R1BLTDN84zEO",
  *   reason: "Spam",
  *   sendTime: new Date("2022-10-11T12:56:41.113Z"),
  *   requestId: "b379050a-2324-497b-9604-575cb5a9c5cd",
  *   attributes: { MessageID: "R1BLTDN84zEO", Reason: "Spam" }
  * }
  */
});

/** Called when `aws:DISCONNECT_USER` system event has been received. */
const unsubscribeOnUserDisconnect = room.addListener('userDisconnect', (disconnectUserEvent) => {
 /* Example event payload:
  * {
  *   id: "AYk6xKitV4On",
  *   userId": "R1BLTDN84zEO",
  *   reason": "Spam",
  *   sendTime": new Date("2022-10-11T12:56:41.113Z"),
  *   requestId": "b379050a-2324-497b-9604-575cb5a9c5cd",
  *   attributes": { UserId: "R1BLTDN84zEO", Reason: "Spam" }
  * }
  */
});
```

## Connect to the Chat Room

The last step of basic initialization is connecting to the chat room by
establishing a WebSocket connection. To do this, simply call the
`connect()` method within the room instance:

```
room.connect();
```

The SDK will try to establish a connection to the chat room encoded in the chat token received from your server.

After you call `connect()`, the room will transition to the
`connecting` state and emit
a `connecting` event. When the room successfully connects, it transitions
to the `connected` state and emits a `connect` event.

A connection failure might happen due to issues when fetching the token or when
connecting to WebSocket. In this case, the room tries to reconnect automatically up
to the number of times indicated by the `maxReconnectAttempts`
constructor parameter. During the reconnection attempts, the room is in the
`connecting` state and does not emit additional events. After exhausting
the reconnect attempts, the room transitions to the `disconnected` state
and emits a `disconnect` event (with a relevant disconnect reason). In
the `disconnected` state, the room no longer tries to connect; you must
call `connect()` again to trigger the connection process.

## Perform Actions in a Chat Room

The Amazon IVS Chat Messaging SDK provides user actions for sending messages,
deleting messages, and disconnecting other users. These are available on the
`ChatRoom` instance. They return a `Promise` object which allows you to receive request confirmation or rejection.

### Sending a

Message

For this request, you must have a `SEND_MESSAGE` capacity
encoded in your chat token.

To trigger a send-message request:

```
const request = new SendMessageRequest('Test Echo');
room.sendMessage(request);
```

To get a confirmation or rejection of the request, `await` the
returned promise or use the `then()` method:

```
try {
  const message = await room.sendMessage(request);
  // Message was successfully sent to chat room
} catch (error) {
  // Message request was rejected. Inspect the `error` parameter for details.
}
```

### Deleting a

Message

For this request, you must have a `DELETE_MESSAGE` capacity encoded in your
chat token.

To delete a message for moderation purposes, call the
`deleteMessage()` method:

```
const request = new DeleteMessageRequest(messageId, 'Reason for deletion');
room.deleteMessage(request);
```

To get a confirmation or rejection of the request, `await` the
returned promise or use the `then()` method:

```
try {
  const deleteMessageEvent = await room.deleteMessage(request);
  // Message was successfully deleted from chat room
} catch (error) {
  // Delete message request was rejected. Inspect the `error` parameter for details.
}
```

### Disconnecting

Another User

For this request, you must have a `DISCONNECT_USER` capacity
encoded in your chat token.

To disconnect another user for moderation purposes, call the `disconnectUser()` method:

```
const request = new DisconnectUserRequest(userId, 'Reason for disconnecting user');
room.disconnectUser(request);
```

To get a confirmation or rejection of the request, `await` the
returned promise or use the `then()` method:

```
try {
  const disconnectUserEvent = await room.disconnectUser(request);
  // User was successfully disconnected from the chat room
} catch (error) {
  // Disconnect user request was rejected. Inspect the `error` parameter for details.
}
```

## Disconnect from a Chat Room

To close your connection to the chat room, call the `disconnect()`
method on the `room` instance:

```
room.disconnect();
```

Calling this method causes the room to close the underlying WebSocket in an
orderly manner. The room instance transitions to a `disconnected` state
and emits a disconnect event, with the `disconnect` reason set to `"clientDisconnect"`.
