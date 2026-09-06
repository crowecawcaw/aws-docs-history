

# Initialize the Amazon Connect SDK in your application for Connect Customer agent workspace
<a name="getting-started-initialize-sdk"></a>

Initializing the [Amazon Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK) in your app for the Connect Customer agent workspace requires calling `init` on the AmazonConnectApp module. This takes an `onCreate` and `onDestroy` callback, which will be invoked once the app has successfully initialized in the agent workspace and then when the agent workspace is going to destroy the iframe the app is running in. These are two of the lifecycle events that your app can integrate with. See [Application lifecycle events in Connect Customer agent workspace](integrating-with-agent-workspace-lifecycle-events.md) for details on the other app lifecycle events that your app can hook into.

```
import { AmazonConnectApp } from "@amazon-connect/app";

const { provider } = AmazonConnectApp.init({
  onCreate: (event) => {
    const { appInstanceId } = event.context;
    console.log('App initialized: ', appInstanceId);
  },
  onDestroy: (event) => {
    console.log('App being destroyed');
  },
});
```

**Note**  
Keep the reference to `{ provider }` which is required to create clients to interact with events and requests. 

Doing a quick test locally by loading your app directly will produce an error message in the browser dev tools console that the app was unable to establish a connection to the workspace. This will happen when your app is correctly calling ` init` when run outside of the workspace.

```
> App failed to connect to agent workspace in the allotted time   
```