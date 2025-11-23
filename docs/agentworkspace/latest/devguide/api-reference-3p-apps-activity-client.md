# Amazon Connect Agent Workspace Activity API

The SDK provides a `SessionExpirationWarningClient` which serves as an interface that your app in Amazon Connect Agent Workspace can use to subscribe to events related to session expiration due to inactivity and to signal Amazon Connect that the agent is active.

The `SessionExpirationWarningClient` accepts an optional constructor argument, `ConnectClientConfig` which itself is defined as:

```
export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually configure this using **setGlobalProvider**.

You can instantiate the client as follows:

```
import { SessionExpirationWarningClient } from "@amazon-connect/activity";

const sessionExpirationWarningClient = new SessionExpirationWarningClient();
```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first instantiate the app which will set up the default `AmazonConnectProvider`. This is the recommended option.

Alternatively, you can provide a constructor argument:

```
import { SessionExpirationWarningClient } from "@amazon-connect/activity";

const sessionExpirationWarningClient = new SessionExpirationWarningClient({
    context: sampleContext,
    provider: sampleProvider
});
```

The following sections describe the API calls for working with the SessionExpirationWarning API.

###### Contents

- [sendActivity()](3p-apps-activity-sendactivity.md "3p-apps-activity-sendactivity.md")
- [ExpirationWarning(Subscribing)](3p-apps-activity-onexpirationwarning.md "3p-apps-activity-onexpirationwarning.md")
- [ExpirationWarning(Unsubscribing)](3p-apps-activity-offexpirationwarning.md "3p-apps-activity-offexpirationwarning.md")
- [ExpirationWarningCleared(Subscribing)](3p-apps-activity-onexpirationwarningcleared.md "3p-apps-activity-onexpirationwarningcleared.md")
- [ExpirationWarningCleared(Unsubscribing)](3p-apps-activity-offexpirationwarningcleared.md "3p-apps-activity-offexpirationwarningcleared.md")
- [SessionExtensionError(Subscribing)](3p-apps-activity-onsessionextensionerror.md "3p-apps-activity-onsessionextensionerror.md")
- [SessionExtensionError(Unsubscribing)](3p-apps-activity-offsessionextensionerror.md "3p-apps-activity-offsessionextensionerror.md")
