

# Connect Customer SDK Activity API
<a name="api-reference-3P-apps-activity-client"></a>

The Connect Customer SDK provides a `SessionExpirationWarningClient` which serves as an interface that your app in the Connect Customer agent workspace can use to subscribe to events related to session expiration due to inactivity and to signal the Connect Customer that the agent is active.

The `SessionExpirationWarningClient` constructor requires a `ConnectClientConfig` argument, which is defined as:

```
export type ConnectClientConfig =
    | AmazonConnectProvider
    | { context: ModuleContext; provider?: AmazonConnectProvider }
    | { provider: AmazonConnectProvider };
```

Pass the `provider` that `AmazonConnectApp.init` returns to the constructor. You must provide this argument.

```
import { SessionExpirationWarningClient } from "@amazon-connect/activity";

const sessionExpirationWarningClient = new SessionExpirationWarningClient(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md), which initializes the default AmazonConnectProvider and returns `{ provider }`.

To use the operations and events in the Activity API, you must have the `*` permission.

The following sections describe the API calls for working with the SessionExpirationWarning API.

**Topics**
+ [offExpirationWarning()](3P-apps-activity-offexpirationwarning.md)
+ [offExpirationWarningCleared()](3P-apps-activity-offexpirationwarningcleared.md)
+ [offSessionExtensionError()](3P-apps-activity-offsessionextensionerror.md)
+ [onExpirationWarning()](3P-apps-activity-onexpirationwarning.md)
+ [onExpirationWarningCleared()](3P-apps-activity-onexpirationwarningcleared.md)
+ [onSessionExtensionError()](3P-apps-activity-onsessionextensionerror.md)
+ [sendActivity()](3P-apps-activity-sendactivity.md)