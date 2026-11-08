

# The start and stop events in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-lifecycle-events-start-stop"></a>

After the create event completes, the agent workspace moves the application to the running state and sends a start event. When the application is hidden, the agent workspace can move it to the stopped state and send a stop event, and then send another start event when the application is visible again. Use these events to pause and resume work that only matters while the application is visible, such as polling or animations.

Unlike `onCreate` and `onDestroy`, the start and stop handlers are not passed to `AmazonConnectApp.init()`. Register them on the provider at any time after `init`, and remove them with the same handler reference that you registered.
+ `onStart(handler, options?)`: Registers a handler for the start event. If you register the handler after the application is already running, set `options.invokeIfRunning` to `true` to invoke the handler immediately.
+ `onStop(handler)`: Registers a handler for the stop event.
+ `offStart(handler)` and `offStop(handler)`: Remove a handler that you registered.

```
import { AmazonConnectApp, AppStartEvent, AppStopEvent } from "@amazon-connect/app";

const { provider } = AmazonConnectApp.init({
  onCreate: async () => {},
});

const startHandler = async (event: AppStartEvent) => {
  console.log("App is running", event.context.instanceId);
};

const stopHandler = async (event: AppStopEvent) => {
  console.log("App is stopped", event.context.instanceId);
};

provider.onStart(startHandler, { invokeIfRunning: true });
provider.onStop(stopHandler);

// Later, to stop receiving the events.
provider.offStart(startHandler);
provider.offStop(stopHandler);
```

An error thrown by a start or stop handler is logged, and it does not close the application.