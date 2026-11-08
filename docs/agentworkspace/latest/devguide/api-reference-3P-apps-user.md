

# Connect Customer SDK User API
<a name="api-reference-3P-apps-user"></a>

The `@amazon-connect/user` package of the Connect Customer SDK provides two clients that your app in Connect Customer agent workspace can use to work with the current user:
+ `SettingsClient` reads and changes the user's settings. It provides the `getLanguage`, `setLanguage`, `onLanguageChanged`, `offLanguageChanged`, `setVisualMode`, `onVisualModeChange`, and `offVisualModeChange` operations.
+ `UserClient` returns information about the user and the Connect Customer instance. It provides the `getUserArn`, `getInstanceId`, and `getUserRegion` operations.

To create either client, pass it the `provider` that `AmazonConnectApp.init` returns. For details, see [Initialize the Connect Customer SDK in your application for Connect Customer agent workspace](getting-started-initialize-sdk.md). This is the recommended option.

```
import { AmazonConnectApp } from "@amazon-connect/app";
import { SettingsClient, UserClient } from "@amazon-connect/user";

const { provider } = AmazonConnectApp.init({
  onCreate: async (event) => {
    // Your app is ready.
  },
});

const settingsClient = new SettingsClient(provider);
const userClient = new UserClient(provider);
```

The constructor argument has the type `ConnectClientConfig`, which is defined as follows:

```
type ConnectClientConfig =
  | AmazonConnectProvider
  | { context: ModuleContext; provider?: AmazonConnectProvider }
  | { provider: AmazonConnectProvider };
```

You can also pass the provider inside an object, for example `new SettingsClient({ provider })`.

Always pass a provider when you create a `SettingsClient` or a `UserClient`.

The following sections describe API calls for working with the User API.

**Topics**
+ [getLanguage()](3P-apps-user-requests-getlanguage.md)
+ [onLanguageChanged()](3P-apps-user-events-languagechanged-sub.md)
+ [offLanguageChanged()](3P-apps-user-events-languagechanged-unsub.md)
+ [getUserArn()](3P-apps-user-requests-getuserarn.md)
+ [getInstanceId()](3P-apps-user-requests-getinstanceid.md)
+ [getUserRegion()](3P-apps-user-requests-getuserregion.md)
+ [getNetworkType()](3P-apps-user-requests-getnetworktype.md)
+ [setLanguage()](3P-apps-user-requests-setlanguage.md)
+ [setVisualMode()](3P-apps-user-requests-setvisualmode.md)
+ [onVisualModeChange()](3P-apps-user-events-visualmodechange-sub.md)
+ [offVisualModeChange()](3P-apps-user-events-visualmodechange-unsub.md)