# The

create event in Amazon Connect Agent Workspace

The create event in the Amazon Connect agent workspace results in the `onCreate` handler passed into the `AmazonConnectApp.init()` to
be invoked. `Init` should be called in an application once it has successfully
loaded and is ready to start handling events from the workspace. The create
event provides the _appInstanceId_ and the _appConfig_ .

- **appInstanceId**: The ID for this
  instance of the app provided by the workspace.
- **appConfig**: The application
  configuration being used by the instance for this app.
- **contactScope**: Provides the current `contactId` if the app is opened during an active contact.
