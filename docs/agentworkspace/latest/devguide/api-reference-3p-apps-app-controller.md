# Amazon Connect Agent Workspace App Controller

API

The SDK provides an `AppControllerClient` to control applications in the
Amazon Connect agent workspace.

The `AppControllerClient` accepts an optional argument,
`ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using
the **AmazonConnectProvider** set in the global provider scope. You can
also manually configure this using **setGlobalProvider**.

You can instantiate the AppControllerClient as follows:

```

import { AppControllerClient } from "@amazon-connect/app-controller";

const appControllerClient = new AppControllerClient();
```

The following sections describe API calls for working with the App Controller
API.

###### Contents

- [getAppCatalog()](api-reference-3p-apps-app-controller-getappcatalog.md "api-reference-3p-apps-app-controller-getappcatalog.md")
- [getAppConfig()](api-reference-3p-apps-app-controller-getappconfig.md "api-reference-3p-apps-app-controller-getappconfig.md")
- [launchApp()](api-reference-3p-apps-app-controller-launchapp.md "api-reference-3p-apps-app-controller-launchapp.md")
- [getApp()](api-reference-3p-apps-app-controller-getapp.md "api-reference-3p-apps-app-controller-getapp.md")
- [getApps()](api-reference-3p-apps-app-controller-getapps.md "api-reference-3p-apps-app-controller-getapps.md")
- [focusApp()](api-reference-3p-apps-app-controller-focusapp.md "api-reference-3p-apps-app-controller-focusapp.md")
- [closeApp()](api-reference-3p-apps-app-controller-closeapp.md "api-reference-3p-apps-app-controller-closeapp.md")
