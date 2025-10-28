# IVS Chat Client Messaging SDK: React

Native Tutorial Part 1: Chat Rooms

This is the first of a two-part tutorial. You will learn the essentials of working with the
Amazon IVS Chat Client Messaging JavaScript SDK by building a fully functional app using React
Native. We call the app _Chatterbox_.

The intended audience is experienced developers who are new to the Amazon IVS Chat Messaging
SDK. You should be comfortable with the TypeScript or JavaScript programming languages and React
Native library.

For brevity, we’ll refer to the Amazon IVS Chat Client Messaging JavaScript SDK as the Chat
JS SDK.

**Note**: In some cases, code examples for JavaScript and
TypeScript are identical, so they are combined.

This first part of the tutorial is broken up into several sections:

1. [Set Up a Local Authentication/Authorization
   Server](#chat-react-rooms-auth-server "#chat-react-rooms-auth-server")
2. [Create a Chatterbox Project](#chat-react-rooms-chatterbox "#chat-react-rooms-chatterbox")
3. [Connect to a Chat Room](#chat-react-rooms-connect "#chat-react-rooms-connect")
4. [Build a Token Provider](#chat-react-rooms-token-provider "#chat-react-rooms-token-provider")
5. [Observe Connection Updates](#chat-react-rooms-connection-state "#chat-react-rooms-connection-state")
6. [Create a Send Button Component](#chat-react-rooms-send-button "#chat-react-rooms-send-button")
7. [Create a Message Input](#chat-react-rooms-message-input "#chat-react-rooms-message-input")
8. [Next Steps](#chat-react-rooms-next-steps "#chat-react-rooms-next-steps")

## Prerequisites

- Be familiar with TypeScript or JavaScript and the React Native library. If you're
  unfamiliar with React Native, learn the basics in [Intro to React Native](https://reactnative.dev/docs/tutorial "https://reactnative.dev/docs/tutorial").
- Read and understand [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").
- Create an AWS IAM user with the CreateChatToken and CreateRoom capabilities defined in
  an existing IAM policy. (See [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").)
- Ensure that the secret/access keys for this user are stored in an AWS credentials
  file. For instructions, see the [AWS CLI
  User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") (especially [Configuration and credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")).
- Create a chat room and save its ARN. See [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md"). (If
  you don’t save the ARN, you can look it up later with the console or Chat API.)
- Install the Node.js 14+ environment with the NPM or Yarn package manager.

## Set Up a Local Authentication/Authorization

Server

Your backend application is responsible for both creating chat rooms and generating the
chat tokens that are needed for the Chat JS SDK to authenticate and authorize your clients for
your chat rooms. You must use your own backend since you cannot securely store AWS keys in a
mobile app; sophisticated attackers could extract these and gain access to your AWS
account.

See [Create a Chat Token](getting-started-chat-auth.md "getting-started-chat-auth.md") in _Getting Started with Amazon IVS Chat_. As shown in the flowchart
there, your server-side application is responsible for creating a chat token. This means your
app must provide its own means of generating a chat token by requesting one from your
server-side application.

In this section, you will learn the basics of creating a token provider in your backend.
We use the express framework to create a live local server that manages the creation of chat
tokens using your local AWS environment.

Create an empty `npm` project using NPM. Create a directory to hold your
application, and make that your working directory:

```
$ mkdir backend & cd backend
```

Use `npm init` to create a `package.json` file for your
application:

```
$ npm init
```

This command prompts you for several things, including the name and version of your
application. For now, just press **RETURN** to accept the
defaults for most of them, with the following exception:

```
entry point: (index.js)
```

Press **RETURN** to accept the suggested default filename of
`index.js` or enter whatever you want the name of the main file to be.

Now install required dependencies:

```
$ npm install express aws-sdk cors dotenv
```

`aws-sdk` requires configuration-environment variables, which automatically
load from a file named `.env` located in the root directory. To configure it,
create a new file named `.env` and fill in the missing configuration
information:

```
# .env

# The region to send service requests to.
AWS_REGION=us-west-2

# Access keys use an access key ID and secret access key
# that you use to sign programmatic requests to AWS.

# AWS access key ID.
AWS_ACCESS_KEY_ID=...

# AWS secret access key.
AWS_SECRET_ACCESS_KEY=...
```

Now we create an entry-point file in the root directory with the name you entered above in
the `npm init` command. In this case, we use `index.js`, and import all
required packages:

```
// index.js
import express from 'express';
import AWS from 'aws-sdk';
import 'dotenv/config';
import cors from 'cors';
```

Now create a new instance of `express`:

```
const app = express();
const port = 3000;

app.use(express.json());
app.use(cors({ origin: ['http://127.0.0.1:5173'] }));
```

After that you can create your first endpoint POST method for the token provider. Take the
required parameters from the request body (`roomId`, `userId`,
`capabilities`, and `sessionDurationInMinutes`):

```
app.post('/create_chat_token', (req, res) => {
  const { roomIdentifier, userId, capabilities, sessionDurationInMinutes } = req.body || {};
});
```

Add validation of required fields:

```
app.post('/create_chat_token', (req, res) => {
  const { roomIdentifier, userId, capabilities, sessionDurationInMinutes } = req.body || {};

  if (!roomIdentifier || !userId) {
    res.status(400).json({ error: 'Missing parameters: `roomIdentifier`, `userId`' });
    return;
  }
});
```

After preparing the POST method, we integrate `createChatToken` with
`aws-sdk` for the core functionality of authentication/authorization:

```
app.post('/create_chat_token', (req, res) => {
  const { roomIdentifier, userId, capabilities, sessionDurationInMinutes } = req.body || {};

  if (!roomIdentifier || !userId || !capabilities) {
    res.status(400).json({ error: 'Missing parameters: `roomIdentifier`, `userId`, `capabilities`' });
    return;
  }

  ivsChat.createChatToken({ roomIdentifier, userId, capabilities, sessionDurationInMinutes }, (error, data) => {
    if (error) {
      console.log(error);
      res.status(500).send(error.code);
    } else if (data.token) {
      const { token, sessionExpirationTime, tokenExpirationTime } = data;
      console.log(`Retrieved Chat Token: ${JSON.stringify(data, null, 2)}`);

      res.json({ token, sessionExpirationTime, tokenExpirationTime });
    }
  });
});
```

At the end of the file, add a port listener for your `express` app:

```
app.listen(port, () => {
  console.log(`Backend listening on port ${port}`);
});
```

Now you can run the server with the following command from the project's root:

```
$ node index.js
```

**Tip**: This server accepts URL requests at https://localhost:3000.

## Create a Chatterbox Project

First you create the React Native project called `chatterbox`. Run this
command:

```
npx create-expo-app
```

Or create an expo project with a TypeScript template.

```
npx create-expo-app -t expo-template-blank-typescript
```

You can integrate the Chat Client Messaging JS SDK via [Node Package Manager](https://www.npmjs.com/ "https://www.npmjs.com/") or [Yarn Package
Manager](https://yarnpkg.com/ "https://yarnpkg.com/"):

- Npm: `npm install amazon-ivs-chat-messaging`
- Yarn: `yarn add amazon-ivs-chat-messaging`

## Connect to a Chat Room

Here you create a `ChatRoom` and connect to it using asynchronous methods. The
`ChatRoom` class manages your user's connection to the Chat JS SDK. To
successfully connect to a chat room, you must provide an instance of `ChatToken`
within your React application.

Navigate to the `App` file that’s created in the default
`chatterbox` project and delete everything that a functional component returns.
None of the pre-populated code is needed. At this point, our `App` is pretty
empty.

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

import * as React from 'react';
import { Text } from 'react-native';

export default function App() {
  return <Text>Hello!</Text>;
}
```

Create a new `ChatRoom` instance and pass it to state using the
`useState` hook. It requires passing `regionOrUrl` (the AWS region in
which your chat room is hosted) and `tokenProvider` (used for the backend
authentication/authorization flow that is created in subsequent steps).

**Important**: You must use the same AWS region as the one in
which you created the room in [Getting Started
with Amazon IVS Chat](getting-started-chat-create-room.md "getting-started-chat-create-room.md"). The API is an AWS regional service. For a list of supported
regions and Amazon IVS Chat HTTPS service endpoints, see the [Amazon IVS Chat
regions](../../../general/latest/gr/ivs.md#ivs_region "../../../general/latest/gr/ivs.md#ivs_region") page.

**TypeScript/JavaScript**:

```
// App.jsx / App.tsx

import React, { useState } from 'react';
import { Text } from 'react-native';
import { ChatRoom } from 'amazon-ivs-chat-messaging';

export default function App() {
  const [room] = useState(() =>
    new ChatRoom({
      regionOrUrl: process.env.REGION,
      tokenProvider: () => {},
    }),
  );

  return <Text>Hello!</Text>;
}
```

## Build a Token Provider

As the next step, we need to build a parameterless `tokenProvider` function
that is required by the `ChatRoom` constructor. First, we will create a
`fetchChatToken` function that will make a POST request to the backend
application that you set up in [Set Up a Local Authentication/Authorization
Server](#chat-react-rooms-auth-server "#chat-react-rooms-auth-server"). Chat tokens
contain the information needed for the SDK to successfully establish a chat-room connection.
The Chat API uses these tokens as a secure way of validating a user's identity, capabilities
within a chat room, and session duration.

In the Project navigator, create a new TypeScript/JavaScript file named
`fetchChatToken`. Build a fetch request to the `backend` application
and return the `ChatToken` object from the response. Add the request body
properties needed for creating a chat token. Use the rules defined for [Amazon
Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). These properties are documented in the [CreateChatToken](../ChatAPIReference/API_CreateChatToken.md#API_CreateChatToken_RequestBody "../ChatAPIReference/API_CreateChatToken.md#API_CreateChatToken_RequestBody") operation.

**Note**: The URL you're using here is the same URL that your
local server created when you ran the backend application.

TypeScript

```
// fetchChatToken.ts

import { ChatToken } from 'amazon-ivs-chat-messaging';

type UserCapability = 'DELETE_MESSAGE' | 'DISCONNECT_USER' | 'SEND_MESSAGE';

export async function fetchChatToken(
  userId: string,
  capabilities: UserCapability[] = [],
  attributes?: Record<string, string>,
  sessionDurationInMinutes?: number,
): Promise<ChatToken> {
  const response = await fetch(`${process.env.BACKEND_BASE_URL}/create_chat_token`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      userId,
      roomIdentifier: process.env.ROOM_ID,
      capabilities,
      sessionDurationInMinutes,
      attributes
    }),
  });

  const token = await response.json();

  return {
    ...token,
    sessionExpirationTime: new Date(token.sessionExpirationTime),
    tokenExpirationTime: new Date(token.tokenExpirationTime),
  };
}
```

JavaScript

```
// fetchChatToken.js

export async function fetchChatToken(
  userId,
  capabilities = [],
  attributes,
  sessionDurationInMinutes) {
  const response = await fetch(`${process.env.BACKEND_BASE_URL}/create_chat_token`, {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      userId,
      roomIdentifier: process.env.ROOM_ID,
      capabilities,
      sessionDurationInMinutes,
      attributes
    }),
  });

  const token = await response.json();

  return {
    ...token,
    sessionExpirationTime: new Date(token.sessionExpirationTime),
    tokenExpirationTime: new Date(token.tokenExpirationTime),
  };
}
```

## Observe Connection Updates

Reacting to changes in a chat room's connection state are essential parts of making a chat
app. Let’s start with subscribing to relevant events:

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

import React, { useState, useEffect } from 'react';
import { Text } from 'react-native';
import { ChatRoom } from 'amazon-ivs-chat-messaging';
import { fetchChatToken } from './fetchChatToken';

export default function App() {
  const [room] = useState(
    () =>
      new ChatRoom({
        regionOrUrl: process.env.REGION,
        tokenProvider: () => fetchChatToken('Mike', ['SEND_MESSAGE']),
      }),
  );

  useEffect(() => {
    const unsubscribeOnConnecting = room.addListener('connecting', () => {});
    const unsubscribeOnConnected = room.addListener('connect', () => {});
    const unsubscribeOnDisconnected = room.addListener('disconnect', () => {});

    return () => {
      // Clean up subscriptions.
      unsubscribeOnConnecting();
      unsubscribeOnConnected();
      unsubscribeOnDisconnected();
    };
  }, [room]);

  return <Text>Hello!</Text>;
}
```

Next, we need to provide the ability to read the connection state. We use our
`useState` hook to create some local state in `App` and set the
connection state inside each listener.

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

import React, { useState, useEffect } from 'react';
import { Text } from 'react-native';
import { ChatRoom, ConnectionState } from 'amazon-ivs-chat-messaging';
import { fetchChatToken } from './fetchChatToken';

export default function App() {
  const [room] = useState(
    () =>
      new ChatRoom({
        regionOrUrl: process.env.REGION,
        tokenProvider: () => fetchChatToken('Mike', ['SEND_MESSAGE']),
      }),
  );
  const [connectionState, setConnectionState] = useState<ConnectionState>('disconnected');

  useEffect(() => {
    const unsubscribeOnConnecting = room.addListener('connecting', () => {
      setConnectionState('connecting');
    });

    const unsubscribeOnConnected = room.addListener('connect', () => {
      setConnectionState('connected');
    });

    const unsubscribeOnDisconnected = room.addListener('disconnect', () => {
      setConnectionState('disconnected');
    });

    return () => {
      unsubscribeOnConnecting();
      unsubscribeOnConnected();
      unsubscribeOnDisconnected();
    };
  }, [room]);

  return <Text>Hello!</Text>;
}
```

After subscribing to the connection state, display the connection state and connect to the
chat room using the `room.connect` method inside the `useEffect`
hook:

**TypeScript/JavaScript**:

```
// App.tsx / App.jsx

// ...

useEffect(() => {
  const unsubscribeOnConnecting = room.addListener('connecting', () => {
    setConnectionState('connecting');
  });

  const unsubscribeOnConnected = room.addListener('connect', () => {
    setConnectionState('connected');
  });

  const unsubscribeOnDisconnected = room.addListener('disconnect', () => {
    setConnectionState('disconnected');
  });

  room.connect();

  return () => {
    unsubscribeOnConnecting();
    unsubscribeOnConnected();
    unsubscribeOnDisconnected();
  };
}, [room]);

// ...

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
  </SafeAreaView>
);

const styles = StyleSheet.create({
  root: {
    flex: 1,
  }
});

// ...
```

You have successfully implemented a chat-room connection.

## Create a Send Button Component

In this section you create a send button that has a different design for each connection
state. The send button facilitates the sending of messages in a chat room. It also serves as a
visual indicator of whether/when messages can be sent; e.g., in the face of dropped
connections or expired chat sessions.

First, create a new file in the `src` directory of your Chatterbox project and
name it `SendButton`. Then, create a component that will display a button for your
chat application. Export your `SendButton` and import it to `App`. In
the empty `<View></View>`, add `<SendButton />`.

TypeScript

```
// SendButton.tsx

import React from 'react';
import { TouchableOpacity, Text, ActivityIndicator, StyleSheet } from 'react-native';

interface Props {
  onPress?: () => void;
  disabled: boolean;
  loading: boolean;
}

export const SendButton = ({ onPress, disabled, loading }: Props) => {
  return (
    <TouchableOpacity style={styles.root} disabled={disabled} onPress={onPress}>
      {loading ? <Text>Send</Text> : <ActivityIndicator />}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  root: {
    width: 50,
    height: 50,
    borderRadius: 30,
    marginLeft: 10,
    justifyContent: 'center',
    alignContent: 'center',
  }
});

// App.tsx

import { SendButton } from './SendButton';

// ...

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <SendButton />
  </SafeAreaView>
);
```

JavaScript

```
// SendButton.jsx

import React from 'react';
import { TouchableOpacity, Text, ActivityIndicator, StyleSheet } from 'react-native';

export const SendButton = ({ onPress, disabled, loading }) => {
  return (
    <TouchableOpacity style={styles.root} disabled={disabled} onPress={onPress}>
      {loading ? <Text>Send</Text> : <ActivityIndicator />}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  root: {
    width: 50,
    height: 50,
    borderRadius: 30,
    marginLeft: 10,
    justifyContent: 'center',
    alignContent: 'center',
  }
});

// App.jsx

import { SendButton } from './SendButton';

// ...

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <SendButton />
  </SafeAreaView>
);
```

Next, in `App` define a function named `onMessageSend` and pass it
to the `SendButton onPress` property. Define another variable named
`isSendDisabled` (which prevents sending messages when the room is not connected)
and pass it to the `SendButton disabled` property.

**TypeScript/JavaScript**:

```
// App.jsx / App.tsx

// ...

const onMessageSend = () => {};

const isSendDisabled = connectionState !== 'connected';

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <SendButton disabled={isSendDisabled} onPress={onMessageSend} />
  </SafeAreaView>
);

// ...
```

## Create a Message Input

The Chatterbox message bar is the component that you will interact with to send messages
to a chat room. Typically it contains a text input for composing your message and a button to
send your message.

To create a `MessageInput` component, first create a new file in the
`src` directory and name it `MessageInput`. Then, create an input
component that will display an input for your chat application. Export your
`MessageInput` and import it to `App` (above the `<SendButton
 />`).

Create a new state named `messageToSend` using the `useState` hook,
with an empty string as its default value. In the body of your app, pass
`messageToSend` to the `value` of `MessageInput` and pass
the `setMessageToSend` to the `onMessageChange` property:

TypeScript

```
// MessageInput.tsx

import * as React from 'react';

interface Props {
  value?: string;
  onValueChange?: (value: string) => void;
}

export const MessageInput = ({ value, onValueChange }: Props) => {
  return (
    <TextInput style={styles.input} value={value} onChangeText={onValueChange} placeholder="Send a message" />
  );
};

const styles = StyleSheet.create({
  input: {
    fontSize: 20,
    backgroundColor: 'rgb(239,239,240)',
    paddingHorizontal: 18,
    paddingVertical: 15,
    borderRadius: 50,
    flex: 1,
  }
})

// App.tsx

// ...

import { MessageInput } from './MessageInput';

// ...

export default function App() {
  const [messageToSend, setMessageToSend] = useState('');

// ...

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <View style={styles.messageBar}>
      <MessageInput value={messageToSend} onMessageChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onPress={onMessageSend} />
    </View>
  </SafeAreaView>
);

const styles = StyleSheet.create({
  root: {
    flex: 1,
  },
  messageBar: {
    borderTopWidth: StyleSheet.hairlineWidth,
    borderTopColor: 'rgb(160,160,160)',
    flexDirection: 'row',
    padding: 16,
    alignItems: 'center',
    backgroundColor: 'white',
  }
});
```

JavaScript

```
// MessageInput.jsx

import * as React from 'react';

export const MessageInput = ({ value, onValueChange }) => {
  return (
    <TextInput style={styles.input} value={value} onChangeText={onValueChange} placeholder="Send a message" />
  );
};

const styles = StyleSheet.create({
  input: {
    fontSize: 20,
    backgroundColor: 'rgb(239,239,240)',
    paddingHorizontal: 18,
    paddingVertical: 15,
    borderRadius: 50,
    flex: 1,
  }
})

// App.jsx

// ...

import { MessageInput } from './MessageInput';

// ...

export default function App() {
  const [messageToSend, setMessageToSend] = useState('');

// ...

return (
  <SafeAreaView style={styles.root}>
    <Text>Connection State: {connectionState}</Text>
    <View style={styles.messageBar}>
      <MessageInput value={messageToSend} onMessageChange={setMessageToSend} />
      <SendButton disabled={isSendDisabled} onPress={onMessageSend} />
    </View>
  </SafeAreaView>
);

const styles = StyleSheet.create({
  root: {
    flex: 1,
  },
  messageBar: {
    borderTopWidth: StyleSheet.hairlineWidth,
    borderTopColor: 'rgb(160,160,160)',
    flexDirection: 'row',
    padding: 16,
    alignItems: 'center',
    backgroundColor: 'white',
  }
});
```

## Next Steps

Now that you finished building a message bar for Chatterbox, proceed to Part 2 of this
React Native tutorial, [Messages and
Events](chat-sdk-react-tutorial-messages-events.md "chat-sdk-react-tutorial-messages-events.md").
