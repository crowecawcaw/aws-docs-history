# The destroy event in Connect Customer Customer agent workspace

The destroy event in the Connect Customer Customer agent workspace will trigger the `onDestroy` callback configured during `AmazonConnectApp.init()`.
The application should use this event to clean up resources and persist data.
The agent workspace will wait for the application to respond that it has
completed clean up for a period of time.
