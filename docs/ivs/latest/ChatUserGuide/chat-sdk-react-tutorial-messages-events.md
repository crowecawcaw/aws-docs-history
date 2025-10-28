# IVS Chat Client Messaging SDK:

React Native Tutorial Part 2: Messages and Events

This second (and last) part of the tutorial is broken up into several sections:

1. [Subscribe to Chat Message
   Events](#chat-react-messages-events-subscribe "#chat-react-messages-events-subscribe")
2. [Show Received Messages](#chat-react-messages-events-show "#chat-react-messages-events-show")
   1. [Creating a Message Component](#chat-react-messages-create-component "#chat-react-messages-create-component")
   2. [Recognizing Messages Sent by the Current
      User](#chat-react-messages-recognize "#chat-react-messages-recognize")
   3. [Rendering a List of Chat Messages](#chat-react-messages-render-list "#chat-react-messages-render-list")

3. [Perform Actions in a Chat
   Room](#chat-react-messages-events-room-actions "#chat-react-messages-events-room-actions")
   1. [Sending a Message](#chat-react-room-actions-sending-message "#chat-react-room-actions-sending-message")
   2. [Deleting a Message](#chat-react-room-actions-deleting-message "#chat-react-room-actions-deleting-message")

4. [Next Steps](#chat-react-messages-events-next-steps "#chat-react-messages-events-next-steps")
   **Note**: In some cases, code examples for JavaScript and
   TypeScript are identical, so they are combined.

## Prerequisite

Be sure you have completed Part 1 of this tutorial, [Chat Rooms](chat-sdk-react-tutorial-chat-rooms.md "chat-sdk-react-tutorial-chat-rooms.md").

## Subscribe to Chat Message

Events

The `ChatRoom` instance uses events to communicate when events occur in a chat
room. To start implementing the chat experience, you need to show your users when others send
a message in the room to which they're connected.

Here, you subscribe to chat message events. Later, we’ll show you how to update a message
list you create, which updates with every message/event.

In your `App`, inside the `useEffect` hook, subscribe to all message
events:

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

useEffect(() => {
  // ...
  const unsubscribeOnMessageReceived = room.addListener('message', (message) => {});

  return () => {
    // ...
    unsubscribeOnMessageReceived();
  };
}, []);
```

## Show Received Messages

Receiving messages is a core part of the chat experience. Using the Chat JS SDK, you can
set up your code to easily receive events from other users connected to a chat room.

Later, we’ll show you how to perform actions in a chat room that leverage the components
you create here.

In your `App`, define a state named `messages` with a
`ChatMessage` array type named `messages`:

TypeScript

```
// App.tsx

// ...

import { ChatRoom, ChatMessage, ConnectionState } from 'amazon-ivs-chat-messaging';

export default function App() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);

  //...
}
```

JavaScript

```
// App.jsx

// ...

import { ChatRoom, ConnectionState } from 'amazon-ivs-chat-messaging';

export default function App() {
  const [messages, setMessages] = useState([]);

  //...
}
```

Next, in the `message` listener function, append `message` to the
`messages` array:

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

// ...

const unsubscribeOnMessageReceived = room.addListener('message', (message) => {
  setMessages((msgs) => [...msgs, message]);
});

// ...
```

Below we step through the tasks to show received messages:

1. [Creating a Message Component](#chat-react-messages-create-component "#chat-react-messages-create-component")
2. [Recognizing Messages Sent by the Current
   User](#chat-react-messages-recognize "#chat-react-messages-recognize")
3. [Rendering a List of Chat Messages](#chat-react-messages-render-list "#chat-react-messages-render-list")

### Creating a Message Component

The `Message` component is responsible for rendering the contents of a
message received by your chat room. In this section, you create a messages component for
rendering individual chat messages in the `App`.

Create a new file in the `src` directory and name it `Message`.
Pass in the `ChatMessage` type for this component, and pass the
`content` string from `ChatMessage` properties to display message
text received from chat-room message listeners. In the Project Navigator, go to
`Message`.

TypeScript

```
// Message.tsx

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { ChatMessage } from 'amazon-ivs-chat-messaging';

type Props = {
  message: ChatMessage;
}

export const Message = ({ message }: Props) => {
  return (
    <View style={styles.root}>
      <Text>{message.sender.userId}</Text>
      <Text style={styles.textContent}>{message.content}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'silver',
    padding: 6,
    borderRadius: 10,
    marginHorizontal: 12,
    marginVertical: 5,
    marginRight: 50,
  },
  textContent: {
    fontSize: 17,
    fontWeight: '500',
    flexShrink: 1,
  },
});
```

JavaScript

```
// Message.jsx

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export const Message = ({ message }) => {
  return (
    <View style={styles.root}>
      <Text>{message.sender.userId}</Text>
      <Text style={styles.textContent}>{message.content}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'silver',
    padding: 6,
    borderRadius: 10,
    marginHorizontal: 12,
    marginVertical: 5,
    marginRight: 50,
  },
  textContent: {
    fontSize: 17,
    fontWeight: '500',
    flexShrink: 1,
  },
});
```

**Tip**: Use this component to store different properties
that you want to render in your message rows; for example, avatar URLs, user names, and
timestamps of when the message was sent.

### Recognizing Messages Sent by the Current

User

To recognize the message sent by the current user, we modify the code and create a React
context for storing the `userId` of the current user.

Create a new file in the `src` directory and name it
`UserContext`:

TypeScript

```
// UserContext.tsx

import React from 'react';

const UserContext = React.createContext<string | undefined>(undefined);

export const useUserContext = () => {
  const context = React.useContext(UserContext);

  if (context === undefined) {
    throw new Error('useUserContext must be within UserProvider');
  }

  return context;
};

export const UserProvider = UserContext.Provider;
```

JavaScript

```
// UserContext.jsx

import React from 'react';

const UserContext = React.createContext(undefined);

export const useUserContext = () => {
  const context = React.useContext(UserContext);

  if (context === undefined) {
    throw new Error('useUserContext must be within UserProvider');
  }

  return context;
};

export const UserProvider = UserContext.Provider;
```

Note: Here we used the `useState` hook to store the `userId`
value. In the future you can use `setUserId` to change user context or for login
purposes.

Next, replace `userId` in the first parameter passed to
`tokenProvider`, using the previously created context. Make sure you add the
`SEND_MESSAGE` capability to your token provider, as specified below; it is
required to send messages.:

TypeScript

```
// App.tsx

// ...

import { useUserContext } from './UserContext';

// ...


export default function App() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const userId = useUserContext();
  const [room] = useState(
    () =>
      new ChatRoom({
        regionOrUrl: process.env.REGION,
        tokenProvider: () => tokenProvider(userId, ['SEND_MESSAGE']),
      }),
  );

  // ...
}
```

JavaScript

```
// App.jsx

// ...

import { useUserContext } from './UserContext';

// ...


export default function App() {
  const [messages, setMessages] = useState([]);
  const userId = useUserContext();
  const [room] = useState(
    () =>
      new ChatRoom({
        regionOrUrl: process.env.REGION,
        tokenProvider: () => tokenProvider(userId, ['SEND_MESSAGE']),
      }),
  );

  // ...
}
```

In your `Message` component, use the `UserContext` created before,
declare the `isMine` variable, match the sender’s `userId` with the
`userId` from the context, and apply different styles of messages for the
current user.

TypeScript

```
// Message.tsx

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

type Props = {
  message: ChatMessage;
}

export const Message = ({ message }: Props) => {
  const userId = useUserContext();

  const isMine = message.sender.userId === userId;

  return (
    <View style={[styles.root, isMine && styles.mine]}>
      {!isMine && <Text>{message.sender.userId}</Text>}
      <Text style={styles.textContent}>{message.content}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'silver',
    padding: 6,
    borderRadius: 10,
    marginHorizontal: 12,
    marginVertical: 5,
    marginRight: 50,
  },
  textContent: {
    fontSize: 17,
    fontWeight: '500',
    flexShrink: 1,
  },
  mine: {
    flexDirection: 'row-reverse',
    backgroundColor: 'lightblue',
  },
});
```

JavaScript

```
// Message.jsx

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

export const Message = ({ message }) => {
  const userId = useUserContext();

  const isMine = message.sender.userId === userId;

  return (
    <View style={[styles.root, isMine && styles.mine]}>
      {!isMine && <Text>{message.sender.userId}</Text>}
      <Text style={styles.textContent}>{message.content}</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'silver',
    padding: 6,
    borderRadius: 10,
    marginHorizontal: 12,
    marginVertical: 5,
    marginRight: 50,
  },
  textContent: {
    fontSize: 17,
    fontWeight: '500',
    flexShrink: 1,
  },
  mine: {
    flexDirection: 'row-reverse',
    backgroundColor: 'lightblue',
  },
});
```

### Rendering a List of Chat Messages

Now list messages using `FlatList` and `Message` component:

TypeScript

```
// App.tsx

// ...

const renderItem = useCallback<ListRenderItem<ChatMessage>>(({ item }) => {
  return (
    <Message key={item.id} message={item} />
  );
}, []);

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <FlatList inverted data={messages} renderItem={renderItem} />
    <View style={styles.messageBar}>
      <MessageInput value={messageToSend} onMessageChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onPress={onMessageSend} />
    </View>
  </SafeAreaView>
);

// ...
```

JavaScript

```
// App.jsx

// ...

const renderItem = useCallback(({ item }) => {
  return (
    <Message key={item.id} message={item} />
  );
}, []);

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <FlatList inverted data={messages} renderItem={renderItem} />
    <View style={styles.messageBar}>
      <MessageInput value={messageToSend} onMessageChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onPress={onMessageSend} />
    </View>
  </SafeAreaView>
);

// ...
```

All the puzzle pieces are now in place for your `App` to start rendering
messages received by your chat room. Continue below to see how to perform actions in a chat
room that leverage the components you have created.

## Perform Actions in a Chat

Room

Sending messages and performing moderator actions are some of the primary ways you
interact with a chat room. Here you will learn how to use various chat request objects to
perform common actions in Chatterbox, such as sending a message, deleting a message, and
disconnecting other users.

All actions in a chat room follow a common pattern: for every action you perform in a chat
room, there is a corresponding request object. For each request there is a corresponding
response object that you receive on request confirmation.

As long as your users are granted the correct capabilities when you create a chat token,
they can successfully perform the corresponding action(s) using the request objects to see
what requests you can perform in a chat room.

Below, we explain how to [send a
message](#chat-react-room-actions-sending-message "#chat-react-room-actions-sending-message") and [delete a
message](#chat-react-room-actions-deleting-message "#chat-react-room-actions-deleting-message").

### Sending a Message

The `SendMessageRequest` class enables sending messages in a chat room. Here,
you modify your `App` to send a message request using the component you created
in [Create a Message Input](chat-sdk-react-tutorial-chat-rooms.md#chat-react-rooms-message-input "chat-sdk-react-tutorial-chat-rooms.md#chat-react-rooms-message-input") (in Part 1
of this tutorial).

To start, define a new boolean property named `isSending` with the
`useState` hook. Use this new property to toggle the disabled state of your
`button` element, using the `isSendDisabled` constant. In the event
handler for your `SendButton`, clear the value for `messageToSend` and
set `isSending` to true.

_Since you will be making an API call from this button, adding
the `isSending` boolean helps prevent multiple API calls from occuring at the
same time, by disabling user interactions on your `SendButton` until the
request is complete._

Note: Sending messages works only if you added the `SEND_MESSAGE` capability
to your token provider, as covered above in [Recognizing Messages Sent by the Current User](#chat-react-messages-recognize "#chat-react-messages-recognize").

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

// ...

const [isSending, setIsSending] = useState(false);

// ...

const onMessageSend = () => {
  setIsSending(true);
  setMessageToSend('');
};

// ...

const isSendDisabled = connectionState !== 'connected' || isSending;

// ...
```

Prepare the request by creating a new `SendMessageRequest` instance, passing
message content to the constructor. After setting the `isSending` and
`messageToSend` states, call the `sendMessage` method, which sends
the request to the chat room. Finally, clear the `isSending` flag on receiving
confirmation or rejection of the request.

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

// ...
import { ChatRoom, ConnectionState, SendMessageRequest } from 'amazon-ivs-chat-messaging'
// ...

const onMessageSend = async () => {
  const request = new SendMessageRequest(messageToSend);
  setIsSending(true);
  setMessageToSend('');

  try {
    const response = await room.sendMessage(request);
  } catch (e) {
    console.log(e);
    // handle the chat error here...
  } finally {
    setIsSending(false);
  }
};

// ...
```

Give Chatterbox a run: try sending a message by drafting one with your
`MessageBar` and tapping your `SendButton`. You should see your sent
message rendered within the `MessageList` that you created earlier.

### Deleting a Message

To delete a message from a chat room, you need to have the proper capability.
Capabilities are granted during the initialization of the chat token that you use when
authenticating to a chat room. For the purposes of this section, the `ServerApp`
from [Set Up a Local
Authentication/Authorization Server](chat-sdk-react-tutorial-chat-rooms.md#chat-react-rooms-auth-server "chat-sdk-react-tutorial-chat-rooms.md#chat-react-rooms-auth-server") (in Part 1 of this tutorial) lets you specify
moderator capabilities. This is done in your app using the `tokenProvider` object
that you created in [Build a Token
Provider](chat-sdk-react-tutorial-chat-rooms.md#chat-react-rooms-token-provider "chat-sdk-react-tutorial-chat-rooms.md#chat-react-rooms-token-provider") (also in Part 1).

Here you modify your `Message` by adding a function to delete the
message.

First, open the `App.tsx` and add the `DELETE_MESSAGE` capability.
(`capabilities` is the second parameter of your `tokenProvider`
function.)

Note: This is how your `ServerApp` informs the IVS Chat APIs that the user
being associated with the resulting chat token can delete messages in a chat room. In a
real-world situation you probably will have more complex backend logic to manage user
capabilities in your server app's infrastructure.

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

// ...

const [room] = useState(() =>
    new ChatRoom({
      regionOrUrl: process.env.REGION,
      tokenProvider: () => tokenProvider(userId, ['SEND_MESSAGE', 'DELETE_MESSAGE']),
    }),
);

// ...
```

In the next steps, you update your `Message` to display a delete
button.

Define a new function called `onDelete` that accepts a string as one of its
parameters and returns `Promise`. For the string parameter, pass in your
component message ID.

TypeScript

```
// Message.tsx

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

export type Props = {
  message: ChatMessage;
  onDelete(id: string): Promise<void>;
};

export const Message = ({ message, onDelete }: Props) => {
  const userId = useUserContext();

  const isMine = message.sender.userId === userId;
  const handleDelete = () => onDelete(message.id);

  return (
    <View style={[styles.root, isMine && styles.mine]}>
      {!isMine && <Text>{message.sender.userId}</Text>}
      <View style={styles.content}>
        <Text style={styles.textContent}>{message.content}</Text>
        <TouchableOpacity onPress={handleDelete}>
          <Text>Delete<Text/>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'silver',
    padding: 6,
    borderRadius: 10,
    marginHorizontal: 12,
    marginVertical: 5,
    marginRight: 50,
  },
  content: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  textContent: {
    fontSize: 17,
    fontWeight: '500',
    flexShrink: 1,
  },
  mine: {
    flexDirection: 'row-reverse',
    backgroundColor: 'lightblue',
  },
});
```

JavaScript

```
// Message.jsx

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

export const Message = ({ message, onDelete }) => {
  const userId = useUserContext();

  const isMine = message.sender.userId === userId;
  const handleDelete = () => onDelete(message.id);

  return (
    <View style={[styles.root, isMine && styles.mine]}>
      {!isMine && <Text>{message.sender.userId}</Text>}
      <View style={styles.content}>
        <Text style={styles.textContent}>{message.content}</Text>
        <TouchableOpacity onPress={handleDelete}>
          <Text>Delete<Text/>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'silver',
    padding: 6,
    borderRadius: 10,
    marginHorizontal: 12,
    marginVertical: 5,
    marginRight: 50,
  },
  content: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  textContent: {
    fontSize: 17,
    fontWeight: '500',
    flexShrink: 1,
  },
  mine: {
    flexDirection: 'row-reverse',
    backgroundColor: 'lightblue',
  },
});
```

Next, you update your `renderItem` to reflect the latest changes to your
`FlatList` component.

In `App`, define a function named `handleDeleteMessage` and pass
it to the `MessageList onDelete` property:

TypeScript

```
// App.tsx

// ...

const handleDeleteMessage = async (id: string) => {};

const renderItem = useCallback<ListRenderItem<ChatMessage>>(({ item }) => {
  return (
    <Message key={item.id} message={item} onDelete={handleDeleteMessage} />
  );
}, [handleDeleteMessage]);

// ...
```

JavaScript

```
// App.jsx

// ...

const handleDeleteMessage = async (id) => {};

const renderItem = useCallback(({ item }) => {
  return (
    <Message key={item.id} message={item} onDelete={handleDeleteMessage} />
  );
}, [handleDeleteMessage]);

// ...
```

Prepare a request by creating a new instance of `DeleteMessageRequest`,
passing the relevant message ID to the constructor parameter, and call
`deleteMessage` that accepts the prepared request above:

TypeScript

```
// App.tsx

// ...

const handleDeleteMessage = async (id: string) => {
  const request = new DeleteMessageRequest(id);
  await room.deleteMessage(request);
};

// ...
```

JavaScript

```
// App.jsx

// ...

const handleDeleteMessage = async (id) => {
  const request = new DeleteMessageRequest(id);
  await room.deleteMessage(request);
};

// ...
```

Next, you update your `messages` state to reflect a new list of messages that
omits the message you just deleted.

In the `useEffect` hook, listen for the `messageDelete` event and
update your `messages` state array by deleting the message with a matching ID to
the `message` parameter.

Note: The `messageDelete` event might be raised for messages being deleted by
the current user or any other user in the room. Handling it in the event handler (instead of
next to the `deleteMessage` request) allows you to unify delete-message
handling.

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

// ...

const unsubscribeOnMessageDeleted = room.addListener('messageDelete', (deleteMessageEvent) => {
  setMessages((prev) => prev.filter((message) => message.id !== deleteMessageEvent.id));
});

return () => {
  // ...

  unsubscribeOnMessageDeleted();
};

// ...
```

You are now able to delete users from a chat room in your chat app.

## Next Steps

As an experiment, try implementing other actions in a room like disconnecting another
user.
