

# Initialize the Connect Customer SDK in your application for Connect Customer agent workspace
<a name="getting-started-initialize-sdk"></a>

Initializing the [Connect Customer SDK](https://github.com/amazon-connect/AmazonConnectSDK) in your app for the Connect Customer agent workspace requires calling `init` on the AmazonConnectApp module. This takes an `onCreate` and `onDestroy` callback, which will be invoked once the app has successfully initialized in the agent workspace and then when the agent workspace is going to destroy the iframe the app is running in. These are two of the lifecycle events that your app can integrate with. See [Application lifecycle events in Connect Customer agent workspace](integrating-with-agent-workspace-lifecycle-events.md) for details on the other app lifecycle events that your app can hook into.

```
import { AmazonConnectApp } from "@amazon-connect/app";

const { provider } = AmazonConnectApp.init({
  onCreate: async (event) => {
    const { instanceId } = event.context;
    console.log('App initialized: ', instanceId);
  },
  onDestroy: async (event) => {
    console.log('App being destroyed');
  },
});
```

**Note**  
Keep the reference to `{ provider }` which is required to create clients to interact with events and requests. 

If you need the provider in a module that does not have the reference, use `AmazonConnectApp.default`. It returns the provider that `AmazonConnectApp.init` created, and it throws an error if `init` has not been called.

The `onCreate` handler is required. If you omit it, the agent workspace closes your application. The `onDestroy` handler is optional. If either handler throws an error or returns a rejected promise, the Connect Customer SDK reports a fatal error and the agent workspace closes your application.

By default, your application has 5000 milliseconds (5 seconds) after it calls `init` to connect to the agent workspace. To change this period, set `workspace.connectionTimeout` to a value in milliseconds, up to a maximum of 60000 (60 seconds). A larger value is reduced to 60000.

```
const { provider } = AmazonConnectApp.init({
  onCreate: async (event) => {
    console.log('App initialized: ', event.context.instanceId);
  },
  workspace: {
    connectionTimeout: 10000, // 10 seconds
  },
});
```

Doing a quick test locally by loading your app directly will produce an error message in the browser dev tools console that the app was unable to establish a connection to the workspace. This will happen when your app is correctly calling ` init` when run outside of the workspace.

```
> App failed to connect to workspace in the allotted time   
```