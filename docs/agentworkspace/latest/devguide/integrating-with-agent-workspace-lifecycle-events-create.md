

# The create event in Connect Customer agent workspace
<a name="integrating-with-agent-workspace-lifecycle-events-create"></a>

The create event in the Connect Customer agent workspace results in the ` onCreate` handler passed into the `AmazonConnectApp.init()` to be invoked. ` Init` should be called in an application once it has successfully loaded and is ready to start handling events from the workspace. The create event provides the following properties in `event.context`.
+ **instanceId**: The ID for this instance of the app provided by the workspace.
+ **config**: The application configuration being used by the instance for this app.
+ **parameters**: The parameters that were passed in `AppLaunchOptions.parameters` when the instance was launched, or undefined if none were passed. Each value is a string, number, boolean, or nested parameters object.
+ **launchedBy**: The source that launched the instance. The `type` property is `external` when the instance was launched by a request made through the Connect Customer SDK, such as a `launchApp` call, and `internal` when the agent workspace launched it. When `type` is `external`, the object also includes the `connectionId` of the requester. The `name` property identifies the launching source, or is undefined.
+ **region**: The AWS Region of the Connect Customer instance.
+ **scope**: The scope the application instance was launched with. When the instance is bound to a contact, this is `{ type: "contact", contactId }` and provides the `contactId` of that contact. When the application is launched while the agent is not handling a contact, this is `{ type: "idle" }` and no `contactId` is available. When the instance is running without a contact scope, such as a cross-contact application launched at the top level, `scope` is undefined. Check `scope?.type` before reading `contactId`. For more information, see [Application scoping for Connect Customer applications](getting-started-application-contact-scope.md).