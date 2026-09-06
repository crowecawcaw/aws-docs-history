

# The create event in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-lifecycle-events-create"></a>

The create event in the Connect Customer agent workspace results in the ` onCreate` handler passed into the `AmazonConnectApp.init()` to be invoked. ` Init` should be called in an application once it has successfully loaded and is ready to start handling events from the workspace. The create event provides the *appInstanceId* and the * appConfig* .
+ **appInstanceId**: The ID for this instance of the app provided by the workspace.
+ **appConfig**: The application configuration being used by the instance for this app.
+ **contactScope**: Provides the current ` contactId` if the app is opened during an active contact.