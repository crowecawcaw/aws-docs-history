# Amazon Connect Agent Workspace AppController API

The Amazon Connect SDK provides an `AppControllerClient` to control applications in the Amazon Connect
agent workspace.

The `AppControllerClient` accepts an optional argument, `ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually
configure this using **setGlobalProvider**.

You can instantiate the AppControllerClient as follows:

```

import { AppControllerClient } from "@amazon-connect/app-controller";

const appControllerClient = new AppControllerClient({ provider });
```

The following sections describe API calls for working with the App Controller
API.

###### Contents

- [closeApp()](api-reference-3P-apps-app-controller-closeapp.md "api-reference-3P-apps-app-controller-closeapp.md")
- [focusApp()](api-reference-3P-apps-app-controller-focusapp.md "api-reference-3P-apps-app-controller-focusapp.md")
- [getApp()](api-reference-3P-apps-app-controller-getapp.md "api-reference-3P-apps-app-controller-getapp.md")
- [getAppCatalog()](api-reference-3P-apps-app-controller-getappcatalog.md "api-reference-3P-apps-app-controller-getappcatalog.md")
- [getAppConfig()](api-reference-3P-apps-app-controller-getappconfig.md "api-reference-3P-apps-app-controller-getappconfig.md")
- [getApps()](api-reference-3P-apps-app-controller-getapps.md "api-reference-3P-apps-app-controller-getapps.md")
- [launchApp()](api-reference-3P-apps-app-controller-launchapp.md "api-reference-3P-apps-app-controller-launchapp.md")
