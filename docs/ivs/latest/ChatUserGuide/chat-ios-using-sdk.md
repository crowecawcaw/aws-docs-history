# Using the IVS Chat Client Messaging iOS SDK

This document takes you through the steps involved in using the Amazon IVS chat client
messaging iOS SDK.

## Connect to a Chat Room

Before starting, you should be familiar with [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md"). Also see the example apps for
[Web](https://github.com/aws-samples/amazon-ivs-chat-web-demo "https://github.com/aws-samples/amazon-ivs-chat-web-demo"), [Android](https://github.com/aws-samples/amazon-ivs-chat-for-android-demo "https://github.com/aws-samples/amazon-ivs-chat-for-android-demo"), and [iOS](https://github.com/aws-samples/amazon-ivs-chat-for-ios-demo "https://github.com/aws-samples/amazon-ivs-chat-for-ios-demo").

To connect to a chat room, your app needs some way of retrieving a chat token
provided by your backend. Your application probably will retrieve a chat token using
a network request to your backend.

To communicate this fetched chat token with the SDK, the SDK’s
`ChatRoom` model requires you to provide either an `async`
function or an instance of an object conforming to the provided
`ChatTokenProvider` protocol at the point of initialization. The
value returned by either of these methods needs to be an instance of the SDK’s
`ChatToken` model.

**Note:** You populate instances of the
`ChatToken` model using data retrieved from your backend. The fields
required to initialize a `ChatToken` instance are the same as the fields
in the [CreateChatToken](../ChatAPIReference/API_CreateChatToken.md "../ChatAPIReference/API_CreateChatToken.md") response. For more information on initializing
instances of the `ChatToken` model, see [Create an instance of ChatToken](#chat-ios-create-chattoken "#chat-ios-create-chattoken").
Remember, _your backend_ is responsible for
providing the data in the `CreateChatToken` response to your app. How you
decide to communicate with your backend to generate chat tokens is up to your app
and its infrastructure.

After choosing your strategy to provide a `ChatToken` to the SDK, call
`.connect()` after successfully initializing a `ChatRoom`
instance with your token provider and the _AWS
region_ that your backend used to create the chat room you are trying
to connect to. Note that `.connect()` is a throwing async
function:

```
import AmazonIVSChatMessaging

let room = ChatRoom(
   awsRegion: <region-your-backend-created-the-chat-room-in>,
   tokenProvider: <your-chosen-token-provider-strategy>
)
try await room.connect()
```

### Conforming to the

ChatTokenProvider Protocol

For the `tokenProvider` parameter in the initializer for
`ChatRoom`, you can provide an instance of
`ChatTokenProvider`. Here is an example of an object conforming
to `ChatTokenProvider`:

```
import AmazonIVSChatMessaging

// This object should exist somewhere in your app
class ChatService: ChatTokenProvider {
   func getChatToken() async throws -> ChatToken {
      let request = YourApp.getTokenURLRequest
      let data = try await URLSession.shared.data(for: request).0
      ...
      return ChatToken(
         token: String(data: data, using: .utf8)!,
         tokenExpirationTime: ..., // this is optional
         sessionExpirationTime: ... // this is optional
      )
   }
}
```

You can then take an instance of this conforming object and pass it into the
initializer for `ChatRoom`:

```
// This should be the same AWS Region that you used to create
// your Chat Room in the Control Plane
let awsRegion = "us-west-2"
let service = ChatService()
let room = ChatRoom(
   awsRegion: awsRegion,
   tokenProvider: service
)
try await room.connect()
```

### Providing an async

Function in Swift

Suppose you already have a manager that you use to manage your application's
network requests. It might look like this:

```
import AmazonIVSChatMessaging

class EndpointManager {
   func getAccounts() async -> AppUser {...}
   func signIn(user: AppUser) async {...}
   ...
}
```

You could just add another function in your manager to retrieve a
`ChatToken` from your backend:

```
import AmazonIVSChatMessaging

class EndpointManager {
   ...
   func retrieveChatToken() async -> ChatToken {...}
}
```

Then, use the reference to that function in Swift when initializing a
`ChatRoom`:

```
import AmazonIVSChatMessaging

let endpointManager: EndpointManager
let room = ChatRoom(
   awsRegion: endpointManager.awsRegion,
   tokenProvider: endpointManager.retrieveChatToken
)
try await room.connect()
```

## Create an Instance of ChatToken

You can easily create an instance of `ChatToken` using the initializer
provided in the SDK. See the documentation in `Token.swift` to learn more
about the properties on `ChatToken`.

```
import AmazonIVSChatMessaging

let chatToken = ChatToken(
   token: <token-string-retrieved-from-your-backend>,
   tokenExpirationTime: nil, // this is optional
   sessionExpirationTime: nil // this is optional
)
```

### Using Decodable

If, while interfacing with the IVS Chat API, your backend decides to simply
forward the [CreateChatToken](../ChatAPIReference/API_CreateChatToken.md "../ChatAPIReference/API_CreateChatToken.md") response to your frontend application, you can take
advantage of `ChatToken` 's conformance to Swift's
`Decodable` protocol. However, there is a catch.

The `CreateChatToken` response payload uses strings for dates that
are formatted using the [ISO
8601 standard for internet timestamps](https://en.wikipedia.org/wiki/ISO_8601 "https://en.wikipedia.org/wiki/ISO_8601"). Normally in Swift, [you would provide](https://www.hackingwithswift.com/example-code/language/how-to-use-iso-8601-dates-with-jsondecoder-and-codable "https://www.hackingwithswift.com/example-code/language/how-to-use-iso-8601-dates-with-jsondecoder-and-codable")
`JSONDecoder.DateDecodingStrategy.iso8601` as a value to
`JSONDecoder`’s `.dateDecodingStrategy` property.
However, `CreateChatToken` uses high-precision fractional seconds in
its strings, and this is not supported by
`JSONDecoder.DateDecodingStrategy.iso8601`.

For your convenience, the SDK provides a public extension on
`JSONDecoder.DateDecodingStrategy` with an additional
`.preciseISO8601` strategy that allows you to successfully use
`JSONDecoder` when decoding a instance of
`ChatToken`:

```
import AmazonIVSChatMessaging

// The CreateChatToken data forwarded by your backend
let responseData: Data

let decoder = JSONDecoder()
decoder.dateDecodingStrategy = .preciseISO8601
let token = try decoder.decode(ChatToken.self, from: responseData)
```

## Disconnect from a Chat Room

To manually disconnect from a `ChatRoom` instance to which you
successfully connected, call `room.disconnect()`. By default, chat rooms
automatically call this function when they are deallocated.

```
import AmazonIVSChatMessaging

let room = ChatRoom(...)
try await room.connect()

// Disconnect
room.disconnect()
```

## Receive a Chat Message/Event

To send and receive messages in your chat room, you need to provide an object that
conforms to the `ChatRoomDelegate` protocol, after you successfully
initialize an instance of `ChatRoom` and call
`room.connect()`. Here is a typical example using
`UIViewController`:

```
import AmazonIVSChatMessaging
import Foundation
import UIKit

class ViewController: UIViewController {
   let room: ChatRoom = ChatRoom(
      awsRegion: "us-west-2",
      tokenProvider: EndpointManager.shared
   )

   override func viewDidLoad() {
      super.viewDidLoad()
      Task { try await setUpChatRoom() }
   }

   private func setUpChatRoom() async throws {
      // Set the delegate to start getting notifications for room events
      room.delegate = self
      try await room.connect()
   }
}

extension ViewController: ChatRoomDelegate {
   func room(_ room: ChatRoom, didReceive message: ChatMessage) { ... }
   func room(_ room: ChatRoom, didReceive event: ChatEvent) { ... }
   func room(_ room: ChatRoom, didDelete message: DeletedMessageEvent) { ... }
}
```

## Get Notified when the Connection

Changes

As is to be expected, you cannot perform actions like sending a message in a room
until the room is fully connected. The architecture of the SDK tries to encourage
connecting to a ChatRoom on a background thread through async APIs. In case you want
to build something in your UI that disables something like a send-message button,
the SDK provides two strategies for getting notified when the connection state of a
chat room changes, using `Combine` or `ChatRoomDelegate`.
These are described below.

**Important:** A chat room's connection state also
could change due to things like a dropped network connection. Take this into account
when building your app.

### Using Combine

Every instance of `ChatRoom` comes with its own
`Combine` publisher in the form of the `state`
property:

```
import AmazonIVSChatMessaging
import Combine

var cancellables: Set<AnyCancellable> = []

let room = ChatRoom(...)
room.state.sink { state in
   switch state {
   case .connecting:
      let image = UIImage(named: "antenna.radiowaves.left.and.right")
      sendMessageButton.setImage(image, for: .normal)
      sendMessageButton.isEnabled = false
   case .connected:
      let image = UIImage(named: "paperplane.fill")
      sendMessageButton.setImage(image, for: .normal)
      sendMessageButton.isEnabled = true
   case .disconnected:
      let image = UIImage(named: "antenna.radiowaves.left.and.right.slash")
      sendMessageButton.setImage(image, for: .normal)
      sendMessageButton.isEnabled = false
   }
}.assign(to: &cancellables)

// Connect to `ChatRoom` on a background thread
Task(priority: .background) {
   try await room.connect()
}
```

### Using

ChatRoomDelegate

Alternately, use the optional functions `roomDidConnect(_:)`,
`roomIsConnecting(_:)`, and `roomDidDisconnect(_:)`
within an object that conforms to `ChatRoomDelegate`. Here is an
example using a `UIViewController`:

```
import AmazonIVSChatMessaging
import Foundation
import UIKit

class ViewController: UIViewController {
   let room: ChatRoom = ChatRoom(
      awsRegion: "us-west-2",
      tokenProvider: EndpointManager.shared
   )

   override func viewDidLoad() {
      super.viewDidLoad()
      Task { try await setUpChatRoom() }
   }

   private func setUpChatRoom() async throws {
      // Set the delegate to start getting notifications for room events
      room.delegate = self
      try await room.connect()
   }
}

extension ViewController: ChatRoomDelegate {
   func roomDidConnect(_ room: ChatRoom) {
      print("room is connected!")
   }
   func roomIsConnecting(_ room: ChatRoom) {
      print("room is currently connecting or fetching a token")
   }
   func roomDidDisconnect(_ room: ChatRoom) {
      print("room disconnected!")
   }
}
```

## Perform Actions in a Chat Room

Different users have different capabilities for actions they can perform in a chat
room; e.g., sending a message, deleting a message, or disconnecting a user. To
perform one of these actions, call `perform(request:)` on a connected
`ChatRoom`, passing in an instance of one of the provided
`ChatRequest` objects in the SDK. The supported requests are in
`Request.swift`.

Some actions performed in a chat room require connected users to have specific
capabilities granted to them when your backend application calls
`CreateChatToken`. By design, the SDK cannot discern the capabilities
of a connected user. Hence, while you can try to perform moderator actions in a
connected instance of `ChatRoom`, the control-plane API ultimately
decides whether that action will succeed.

All actions that go through `room.perform(request:)` wait until the
room receives the expected instance of a model (the type of which is associated with
the request object itself) matched to the `requestId` of both the
received model and the request object. If there is an issue with the request,
`ChatRoom` always throws an error in the form of a
`ChatError`. The definition of `ChatError` is in
`Error.swift`.

### Sending a Message

To send a chat message, use an instance of
`SendMessageRequest`:

```
import AmazonIVSChatMessaging

let room = ChatRoom(...)
try await room.connect()
try await room.perform(
   request: SendMessageRequest(
      content: "Release the Kraken!"
   )
)
```

As mentioned above, `room.perform(request:)` returns once a
corresponding `ChatMessage` is received by the `ChatRoom`.
If there is an issue with the request (like exceeding the message character
limit for a room), an instance of `ChatError` is thrown instead. You
can then surface this useful information in your UI:

```
import AmazonIVSChatMessaging

do {
   let message = try await room.perform(
      request: SendMessageRequest(
         content: "Release the Kraken!"
      )
   )
   print(message.id)
} catch let error as ChatError {
   switch error.errorCode {
   case .invalidParameter:
      print("Exceeded the character limit!")
   case .tooManyRequests:
      print("Exceeded message request limit!")
   default:
      break
   }

   print(error.errorMessage)
}
```

### Appending Metadata to a

Message

When [sending a message](#room-action-send-message "#room-action-send-message"), you
can append metadata that will be associated with it.
`SendMessageRequest` has an `attributes` property,
with which you can initialize your request. The data you attach there is
attached to the message when others receive that message in the room.

Here is an example of attaching emote data to a message being sent:

```
import AmazonIVSChatMessaging

let room = ChatRoom(...)
try await room.connect()
try await room.perform(
   request: SendMessageRequest(
      content: "Release the Kraken!",
      attributes: [
         "messageReplyId" : "<other-message-id>",
         "attached-emotes" : "krakenCry,krakenPoggers,krakenCheer"
      ]
   )
)
```

Using `attributes` in a `SendMessageRequest` can be
extremely useful for building complex features in your chat product. For
example, one could build threading functionality using the `[String :
 String]` attributes dictionary in a
`SendMessageRequest`!

The `attributes` payload is very flexible and powerful. Use it to
derive information about your message you would not be able to do otherwise.
Using attributes is much easier than, for instance, parsing the string of a
message to get information about things like emotes.

### Deleting a Message

Deleting a chat message is just like sending one. Use the
`room.perform(request:)` function on `ChatRoom` to
achieve this by creating an instance of
`DeleteMessageRequest`.

To easily access previous instances of received Chat messages, pass in the
value of `message.id` to the initializer of
`DeleteMessageRequest`.

Optionally, provide a reason string to `DeleteMessageRequest` so
you can surface that in your UI.

```
import AmazonIVSChatMessaging

let room = ChatRoom(...)
try await room.connect()
try await room.perform(
   request: DeleteMessageRequest(
      id: "<other-message-id-to-delete>",
      reason: "Abusive chat is not allowed!"
   )
)
```

As this is a moderator action, your user may not actually have the capability
of deleting another user's message. You can use Swift's throwable function
mechanic to surface an error message in your UI when a user tries to delete a
message without the appropriate capability.

When your backend calls `CreateChatToken` for a user, it needs to
pass `"DELETE_MESSAGE"` into the `capabilities` field to
activate that functionality for a connected chat user.

Here is an example of catching a capability error thrown when attempting to
delete a message without the appropriate permissions:

```
import AmazonIVSChatMessaging

do {
   // `deleteEvent` is the same type as the object that gets sent to
   // `ChatRoomDelegate`'s `room(_:didDeleteMessage:)` function
   let deleteEvent = try await room.perform(
      request: DeleteMessageRequest(
         id: "<other-message-id-to-delete>",
         reason: "Abusive chat is not allowed!"
      )
   )
   dataSource.messages[deleteEvent.messageID] = nil
   tableView.reloadData()
} catch let error as ChatError {
   switch error.errorCode {
   case .forbidden:
      print("You cannot delete another user's messages. You need to be a mod to do that!")
   default:
      break
   }

   print(error.errorMessage)
}
```

### Disconnecting Another User

Use `room.perform(request:)` to disconnect another user from a chat
room. Specifically, use an instance of `DisconnectUserRequest`. All
`ChatMessage`s received by a `ChatRoom` have a
`sender` property, which contains the user ID that you need to
properly initialize with an instance of `DisconnectUserRequest`.
Optionally, provide a reason string for the disconnect request.

```
import AmazonIVSChatMessaging

let room = ChatRoom(...)
try await room.connect()

let message: ChatMessage = dataSource.messages["<message-id>"]
let sender: ChatUser = message.sender
let userID: String = sender.userId
let reason: String = "You've been disconnected due to abusive behavior"

try await room.perform(
   request: DisconnectUserRequest(
      id: userID,
      reason: reason
   )
)
```

As this is another example of a moderator action, you may try to disconnect
another user, but you will be unable to do so unless you have the
`DISCONNECT_USER` capability. The capability gets set when your
backend application calls `CreateChatToken` and injects the
`"DISCONNECT_USER"` string into the `capabilities`
field.

If your user does not have the capability to disconnect another user,
`room.perform(request:)` throws an instance of
`ChatError`, just like the other requests. You can inspect the
error's `errorCode` property to determine if the request failed
because of the lack of moderator privileges:

```
import AmazonIVSChatMessaging

do {
   let message: ChatMessage = dataSource.messages["<message-id>"]
   let sender: ChatUser = message.sender
   let userID: String = sender.userId
   let reason: String = "You've been disconnected due to abusive behavior"

   try await room.perform(
      request: DisconnectUserRequest(
         id: userID,
         reason: reason
      )
   )
} catch let error as ChatError {
   switch error.errorCode {
   case .forbidden:
      print("You cannot disconnect another user. You need to be a mod to do that!")
   default:
      break
   }

   print(error.errorMessage)
}
```
