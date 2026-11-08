

# Connect Customer SDK AppController API
<a name="api-reference-3P-apps-app-controller"></a>

The Connect Customer SDK provides an `AppControllerClient` to control applications in the Connect Customer agent workspace.

To create an `AppControllerClient`, pass it the `provider` that `AmazonConnectApp.init` returns. For details, see [Initialize the Connect Customer SDK in your application for Connect Customer agent workspace](getting-started-initialize-sdk.md). This is the recommended option.

```
import { AmazonConnectApp } from "@amazon-connect/app";
import { AppControllerClient } from "@amazon-connect/app-controller";

const { provider } = AmazonConnectApp.init({
  onCreate: async (event) => {
    // Your app is ready.
  },
});

const appControllerClient = new AppControllerClient(provider);
```

The constructor argument has the type `ConnectClientConfig`, which is defined as follows:

```
type ConnectClientConfig =
  | AmazonConnectProvider
  | { context: ModuleContext; provider?: AmazonConnectProvider }
  | { provider: AmazonConnectProvider };
```

You can also pass the provider inside an object, for example `new AppControllerClient({ provider })`.

The following sections describe API calls for working with the App Controller API.

**Topics**
+ [closeApp()](api-reference-3P-apps-app-controller-closeapp.md)
+ [focusApp()](api-reference-3P-apps-app-controller-focusapp.md)
+ [getApp()](api-reference-3P-apps-app-controller-getapp.md)
+ [getAppCatalog()](api-reference-3P-apps-app-controller-getappcatalog.md)
+ [getAppConfig()](api-reference-3P-apps-app-controller-getappconfig.md)
+ [getApps()](api-reference-3P-apps-app-controller-getapps.md)
+ [launchApp()](api-reference-3P-apps-app-controller-launchapp.md)