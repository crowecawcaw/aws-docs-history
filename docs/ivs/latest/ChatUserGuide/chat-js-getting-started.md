# Getting Started with the IVS Chat Client Messaging JavaScript SDK

Before starting, you should be familiar with [Getting Started with Amazon IVS Chat](getting-started-chat.md "getting-started-chat.md").

## Add the Package

Use either:

```
$ npm install --save amazon-ivs-chat-messaging
```

or:

```
$ yarn add amazon-ivs-chat-messaging
```

## React Native Support

The IVS Chat Client Messaging JavaScript SDK has a `uuid`
dependency which uses the `crypto.getRandomValues` method. Since this
method is not supported in React Native, you need to install the additional polyfill
`react-native-get-random-value` and import it at the top of the
`index.js` file:

```
import 'react-native-get-random-values';
import {AppRegistry} from 'react-native';
import App from './src/App';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
```

## Set Up Your Backend

This integration requires endpoints on your server that talk to the [Amazon IVS Chat
API](../ChatAPIReference/Welcome.md "../ChatAPIReference/Welcome.md"). Use the [official AWS
libraries](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") for access to the Amazon IVS API from your server. These
libraries are
accessible within several languages from the public packages; e.g., [node.js](https://www.npmjs.com/package/aws-sdk "https://www.npmjs.com/package/aws-sdk"), [java](https://github.com/aws/aws-sdk-java "https://github.com/aws/aws-sdk-java"), and [go](https://github.com/aws/aws-sdk-go "https://github.com/aws/aws-sdk-go").

Create a server endpoint that talks to the Amazon IVS Chat API [CreateChatToken](../ChatAPIReference/API_CreateChatToken.md "../ChatAPIReference/API_CreateChatToken.md") operation, to create a chat token for chat users.
