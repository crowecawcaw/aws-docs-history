

# The destroy event in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-lifecycle-events-destroy"></a>

The destroy event in the Connect Customer agent workspace will trigger the ` onDestroy` callback configured during `AmazonConnectApp.init()`. The application should use this event to clean up resources and persist data. The agent workspace waits five seconds for the application to respond that it has completed clean up. If the application has not responded within that period, the agent workspace destroys the instance, and any incomplete clean up does not finish. Persist critical data as it changes, rather than only in the `onDestroy` callback.

Your application can ask the agent workspace to close it by calling `sendCloseAppRequest(message?)` on the provider. The optional `message` describes the reason and is logged by the agent workspace. The agent workspace then destroys the instance and sends the destroy event, so your `onDestroy` callback runs.

```
provider.sendCloseAppRequest("The agent finished the task");
```