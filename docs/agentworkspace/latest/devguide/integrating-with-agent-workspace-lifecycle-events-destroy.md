# The

destroy event in Amazon Connect Agent Workspace

The destroy event in Amazon Connect Agent Workspace will trigger the `onDestroy`
callback configured during `AmazonConnectApp.init()`. The application
should use this event to clean up resources and persist data. The workspace will
wait for the application to respond that it has completed clean up for a period
of time.
