# IVS Chat Client Messaging SDK:

JavaScript Tutorial Part 2: Messages and Events

This second (and last) part of the tutorial is broken up into several sections:

1. [Subscribe to Chat Message Events](#chat-js-messages-events-subscribe "#chat-js-messages-events-subscribe")
2. [Show Received Messages](#chat-js-messages-events-show "#chat-js-messages-events-show")
   1. [Creating a Message Component](#chat-js-messages-create-component "#chat-js-messages-create-component")
   2. [Recognizing Messages Sent by the Current
      User](#chat-js-messages-recognize "#chat-js-messages-recognize")
   3. [Creating a Message List
      Component](#chat-js-messages-create-list-component "#chat-js-messages-create-list-component")
   4. [Rendering a List of Chat Messages](#chat-js-messages-render-list "#chat-js-messages-render-list")

3. [Perform Actions in a Chat Room](#chat-js-messages-events-room-actions "#chat-js-messages-events-room-actions")
   1. [Sending a Message](#chat-js-room-actions-sending-message "#chat-js-room-actions-sending-message")
   2. [Deleting a Message](#chat-js-room-actions-deleting-message "#chat-js-room-actions-deleting-message")

4. [Next Steps](#chat-js-messages-events-next-steps "#chat-js-messages-events-next-steps")
   **Note**: In some cases, code examples for JavaScript and
   TypeScript are identical, so they are combined.

For full SDK documentation, start with
[Amazon IVS Chat Client Messaging SDK](chat-sdk.md "chat-sdk.md") (here in
the _Amazon IVS Chat User Guide_) and the [Chat Client Messaging:
SDK for JavaScript Reference](https://aws.github.io/amazon-ivs-chat-messaging-sdk-js/latest/ "https://aws.github.io/amazon-ivs-chat-messaging-sdk-js/latest/") (on GitHub).

## Prerequisite

Be sure you have completed Part 1 of this tutorial, [Chat Rooms](chat-sdk-js-tutorial-chat-rooms.md "chat-sdk-js-tutorial-chat-rooms.md").

## Subscribe to Chat Message Events

The `ChatRoom` instance uses events to communicate when events occur in a chat
room. To start implementing the chat experience, you need to show your users when others send
a message in the room to which they're connected.

Here, you subscribe to chat message events. Later, we’ll show you how to update a message
list you create, which updates with every message/event.

In your `App`, inside the `useEffect` hook, subscribe to all message
events:

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

export default function App() {
  const [messages, setMessages] = useState([]);

  //...
}
```

Next, in the `message` listener function, append `message` to the
`messages` array:

```
// App.jsx / App.tsx

// ...

const unsubscribeOnMessageReceived = room.addListener('message', (message) => {
  setMessages((msgs) => [...msgs, message]);
});

// ...
```

Below we step through the tasks to show received messages:

1. [Creating a Message Component](#chat-js-messages-create-component "#chat-js-messages-create-component")
2. [Recognizing Messages Sent by the Current
   User](#chat-js-messages-recognize "#chat-js-messages-recognize")
3. [Creating a Message List
   Component](#chat-js-messages-create-list-component "#chat-js-messages-create-list-component")
4. [Rendering a List of Chat Messages](#chat-js-messages-render-list "#chat-js-messages-render-list")

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

import * as React from 'react';
import { ChatMessage } from 'amazon-ivs-chat-messaging';

type Props = {
  message: ChatMessage;
}

export const Message = ({ message }: Props) => {
  return (
    <div style={{ backgroundColor: 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
    </div>
  );
};
```

JavaScript

```
// Message.jsx

import * as React from 'react';

export const Message = ({ message }) => {
  return (
    <div style={{ backgroundColor: 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
    </div>
  );
};
```

Tip: Use this component to store different properties that you want to render in your
message rows; for example, avatar URLs, user names, and timestamps of when the message was
sent.

### Recognizing Messages Sent by the Current

User

To recognize the message sent by the current user, we modify the code and create a React
context for storing the `userId` of the current user.

Create a new file in the `src` directory and name it
`UserContext`:

TypeScript

```
// UserContext.tsx

import React, { ReactNode, useState, useContext, createContext } from 'react';

type UserContextType = {
  userId: string;
  setUserId: (userId: string) => void;
};

const UserContext = createContext<UserContextType | undefined>(undefined);

export const useUserContext = () => {
  const context = useContext(UserContext);

  if (context === undefined) {
    throw new Error('useUserContext must be within UserProvider');
  }

  return context;
};

type UserProviderType = {
  children: ReactNode;
}

export const UserProvider = ({ children }: UserProviderType) => {
  const [userId, setUserId] = useState('Mike');

  return <UserContext.Provider value={{ userId, setUserId }}>{children}</UserContext.Provider>;
};
```

JavaScript

```
// UserContext.jsx

import React, { useState, useContext, createContext } from 'react';

const UserContext = createContext(undefined);

export const useUserContext = () => {
  const context = useContext(UserContext);

  if (context === undefined) {
    throw new Error('useUserContext must be within UserProvider');
  }

  return context;
};

export const UserProvider = ({ children }) => {
  const [userId, setUserId] = useState('Mike');

  return <UserContext.Provider value={{ userId, setUserId }}>{children}</UserContext.Provider>;
};
```

Note: Here we used the `useState` hook to store the `userId`
value. In the future you can use `setUserId` to change user context or for login
purposes.

Next, replace `userId` in the first parameter passed to
`tokenProvider`, using the previously created context:

```
// App.jsx / App.tsx

// ...

import { useUserContext } from './UserContext';

// ...


export default function App() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const { userId } = useUserContext();
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

import * as React from 'react';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

type Props = {
  message: ChatMessage;
}

export const Message = ({ message }: Props) => {
  const { userId } = useUserContext();

  const isMine = message.sender.userId === userId;

  return (
    <div style={{ backgroundColor: isMine ? 'lightblue' : 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
    </div>
  );
};
```

JavaScript

```
// Message.jsx

import * as React from 'react';
import { useUserContext } from './UserContext';

export const Message = ({ message }) => {
  const { userId } = useUserContext();

  const isMine = message.sender.userId === userId;

  return (
    <div style={{ backgroundColor: isMine ? 'lightblue' : 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
    </div>
  );
};
```

### Creating a Message List

Component

The `MessageList` component is responsible for displaying a chat room's
conversation over time. The `MessageList` file is the container that holds all
our messages. `Message` is one row in `MessageList`.

Create a new file in the `src` directory and name it
`MessageList`. Define `Props` with `messages` of type
`ChatMessage` array. Inside the body, map our `messages` property
and pass `Props` to your `Message` component.

TypeScript

```
// MessageList.tsx

import React from 'react';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { Message } from './Message';

interface Props {
  messages: ChatMessage[];
}

export const MessageList = ({ messages }: Props) => {
  return (
    <div>
      {messages.map((message) => (
        <Message key={message.id} message={message}/>
      ))}
    </div>
  );
};
```

JavaScript

```
// MessageList.jsx

import React from 'react';
import { Message } from './Message';

export const MessageList = ({ messages }) => {
  return (
    <div>
      {messages.map((message) => (
        <Message key={message.id} message={message} />
      ))}
    </div>
  );
};
```

### Rendering a List of Chat Messages

Now bring your new `MessageList` into your main `App`
component:

```
// App.jsx / App.tsx

import { MessageList } from './MessageList';
// ...

return (
  <div style={{ display: 'flex', flexDirection: 'column', padding: 10 }}>
    <h4>Connection State: {connectionState}</h4>
    <MessageList messages={messages} />
    <div style={{ flexDirection: 'row', display: 'flex', width: '100%', backgroundColor: 'red' }}>
      <MessageInput value={messageToSend} onValueChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onPress={onMessageSend} />
    </div>
  </div>
);

// ...
```

All the puzzle pieces are now in place for your `App` to start rendering
messages received by your chat room. Continue below to see how to perform actions in a chat
room that leverage the components you have created.

## Perform Actions in a Chat Room

Sending messages and performing moderator actions within a chat room are some of the
primary ways you interact with a chat room. Here you will learn how to use various
`ChatRequest` objects to perform common actions in Chatterbox, such as sending a
message, deleting a message, and disconnecting other users.

All actions in a chat room follow a common pattern: for every action you perform in a chat
room, there is a corresponding request object. For each request there is a corresponding
response object that you receive on request confirmation.

As long as your users are granted the correct permissions when you create a chat token,
they can successfully perform the corresponding action(s) using the request objects to see
what requests you can perform in a chat room.

Below, we explain how to [send a
message](#chat-js-room-actions-sending-message "#chat-js-room-actions-sending-message") and [delete a
message](#chat-js-room-actions-deleting-message "#chat-js-room-actions-deleting-message").

### Sending a Message

The `SendMessageRequest` class enables sending messages in a chat room. Here,
you modify your `App` to send a message request using the component you created
in [Create a Message Input](chat-sdk-js-tutorial-chat-rooms.md#chat-js-rooms-message-input "chat-sdk-js-tutorial-chat-rooms.md#chat-js-rooms-message-input") (in Part 1 of
this tutorial).

To start, define a new boolean property named `isSending` with the
`useState` hook. Use this new property to toggle the disabled state of your
`button` HTML element, using the `isSendDisabled` constant. In the
event handler for your `SendButton`, clear the value for
`messageToSend` and set `isSending` to true.

_Since you will be making an API call from this button, adding
the `isSending` boolean helps prevent multiple API calls from occuring at the
same time, by disabling user interactions on your `SendButton` until the
request is complete._

```
// App.jsx / App.tsx

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

TypeScript

```
// App.tsx

// ...
import { ChatMessage, ChatRoom, ConnectionState, SendMessageRequest } from 'amazon-ivs-chat-messaging'
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

JavaScript

```
// App.jsx

// ...
import { ChatRoom, SendMessageRequest } from 'amazon-ivs-chat-messaging'
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
`MessageInput` and tapping your `SendButton`. You should see your
sent message rendered within the `MessageList` that you created earlier.

### Deleting a Message

To delete a message from a chat room, you need to have the proper capability.
Capabilities are granted during the initialization of the chat token that you use when
authenticating to a chat room. For the purposes of this section, the `ServerApp`
from [Set Up a Local Authentication/Authorization
Server](chat-sdk-js-tutorial-chat-rooms.md#chat-js-rooms-auth-server "chat-sdk-js-tutorial-chat-rooms.md#chat-js-rooms-auth-server") (in Part 1 of this tutorial) lets you specify moderator capabilities. This
is done in your app using the `tokenProvider` object that you created in [Build a Token Provider](chat-sdk-js-tutorial-chat-rooms.md#chat-js-rooms-token-provider "chat-sdk-js-tutorial-chat-rooms.md#chat-js-rooms-token-provider") (also in Part
1).

Here you modify your `Message` by adding a function to delete the
message.

First, open the `App.tsx` and add the `DELETE_MESSAGE` capability.
(`capabilities` is the second parameter of your `tokenProvider`
function.)

Note: This is how your `ServerApp` informs the IVS Chat APIs that the user
being associated with the resulting chat token can delete messages in a chat room. In a
real-world situation you probably will have more complex backend logic to manage user
capabilities in your server app's infrastructure.

TypeScript

```
// App.tsx

// ...

const [room] = useState( () =>
    new ChatRoom({
      regionOrUrl: process.env.REGION as string,
      tokenProvider: () => tokenProvider(userId, ['SEND_MESSAGE', 'DELETE_MESSAGE']),
    }),
);

// ...
```

JavaScript

```
// App.jsx

// ...

const [room] = useState( () =>
  new ChatRoom({
    regionOrUrl: process.env.REGION,
    tokenProvider: () => tokenProvider(userId, ['SEND_MESSAGE', 'DELETE_MESSAGE']),
  }),
);

// ...
```

In the next steps, you update your `Message` to display a delete
button.

Open `Message` and define a new boolean state named `isDeleting`
using the `useState` hook with an initial value of `false`. Using this
state, update the contents of your `Button` to be different depending on the
current state of `isDeleting`. Disable your button when `isDeleting`
is true; this prevents you from attempting to make two delete message requests at the same
time.

TypeScript

```
// Message.tsx

import React, { useState } from 'react';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

type Props = {
  message: ChatMessage;
}

export const Message = ({ message }: Props) => {
  const { userId } = useUserContext();
  const [isDeleting, setIsDeleting] = useState(false);

  const isMine = message.sender.userId === userId;

  return (
    <div style={{ backgroundColor: isMine ? 'lightblue' : 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
      <button disabled={isDeleting}>Delete</button>
    </div>
  );
};
```

JavaScript

```
// Message.jsx

import React from 'react';
import { useUserContext } from './UserContext';

export const Message = ({ message }) => {
  const { userId } = useUserContext();
  const [isDeleting, setIsDeleting] = useState(false);

  return (
    <div style={{ backgroundColor: isMine ? 'lightblue' : 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
      <button disabled={isDeleting}>Delete</button>
    </div>
  );
};
```

Define a new function called `onDelete` that accepts a string as one of its
parameters and returns `Promise`. In the body of your `Button`‘s
action closure, use `setIsDeleting` to toggle your `isDeleting`
boolean before and after a call to `onDelete`. For the string parameter, pass in
your component message ID.

TypeScript

```
// Message.tsx

import React, { useState } from 'react';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { useUserContext } from './UserContext';

export type Props = {
  message: ChatMessage;
  onDelete(id: string): Promise<void>;
};

export const Message = ({ message onDelete }: Props) => {
  const { userId } = useUserContext();
  const [isDeleting, setIsDeleting] = useState(false);
  const isMine = message.sender.userId === userId;
  const handleDelete = async () => {
    setIsDeleting(true);
    try {
      await onDelete(message.id);
    } catch (e) {
      console.log(e);
      // handle chat error here...
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <div style={{ backgroundColor: isMine ? 'lightblue' : 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{content}</p>
      <button onClick={handleDelete} disabled={isDeleting}>
        Delete
      </button>
    </div>
  );
};
```

JavaScript

```
// Message.jsx

import React, { useState } from 'react';
import { useUserContext } from './UserContext';

export const Message = ({ message, onDelete }) => {
  const { userId } = useUserContext();
  const [isDeleting, setIsDeleting] = useState(false);
  const isMine = message.sender.userId === userId;
  const handleDelete = async () => {
    setIsDeleting(true);
    try {
      await onDelete(message.id);
    } catch (e) {
      console.log(e);
      // handle the exceptions here...
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <div style={{ backgroundColor: 'silver', padding: 6, borderRadius: 10, margin: 10 }}>
      <p>{message.content}</p>
      <button onClick={handleDelete} disabled={isDeleting}>
        Delete
      </button>
    </div>
  );
};
```

Next, you update your `MessageList` to reflect the latest changes to your
`Message` component.

Open `MessageList` and define a new function called `onDelete`
that accepts a string as a parameter and returns `Promise`. Update your
`Message` and pass it through the properties of `Message`. The
string parameter in your new closure will be the ID of the message that you want to delete,
which gets passed from your `Message`.

TypeScript

```
// MessageList.tsx

import * as React from 'react';
import { ChatMessage } from 'amazon-ivs-chat-messaging';
import { Message } from './Message';

interface Props {
  messages: ChatMessage[];
  onDelete(id: string): Promise<void>;
}

export const MessageList = ({ messages, onDelete }: Props) => {
  return (
    <>
      {messages.map((message) => (
        <Message key={message.id} onDelete={onDelete} content={message.content} id={message.id} />
      ))}
    </>
  );
};
```

JavaScript

```
// MessageList.jsx

import * as React from 'react';
import { Message } from './Message';

export const MessageList = ({ messages, onDelete }) => {
  return (
    <>
      {messages.map((message) => (
        <Message key={message.id} onDelete={onDelete} content={message.content} id={message.id} />
      ))}
    </>
  );
};
```

Next, you update your `App` to reflect the latest changes to your
`MessageList`.

In `App`, define a function named `onDeleteMessage` and pass it to
the `MessageList onDelete` property:

TypeScript

```
// App.tsx

// ...

const onDeleteMessage = async (id: string) => {};

return (
  <div style={{ display: 'flex', flexDirection: 'column', padding: 10 }}>
    <h4>Connection State: {connectionState}</h4>
    <MessageList onDelete={onDeleteMessage} messages={messages} />
    <div style={{ flexDirection: 'row', display: 'flex', width: '100%' }}>
      <MessageInput value={messageToSend} onMessageChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onSendPress={onMessageSend} />
    </div>
  </div>
);

// ...
```

JavaScript

```
// App.jsx

// ...

const onDeleteMessage = async (id) => {};

return (
  <div style={{ display: 'flex', flexDirection: 'column', padding: 10 }}>
    <h4>Connection State: {connectionState}</h4>
    <MessageList onDelete={onDeleteMessage} messages={messages} />
    <div style={{ flexDirection: 'row', display: 'flex', width: '100%' }}>
      <MessageInput value={messageToSend} onMessageChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onSendPress={onMessageSend} />
    </div>
  </div>
);

// ...
```

Prepare a request by creating a new instance of `DeleteMessageRequest`,
passing the relevant message ID to the constructor parameter, and call
`deleteMessage` that accepts the prepared request above:

TypeScript

```
// App.tsx

// ...

const onDeleteMessage = async (id: string) => {
  const request = new DeleteMessageRequest(id);
  await room.deleteMessage(request);
};

// ...
```

JavaScript

```
// App.jsx

// ...

const onDeleteMessage = async (id) => {
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

```
// App.jsx / App.tsx

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
