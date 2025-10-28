# Amazon Connect Agent Workspace Quick

Responses API

The SDK provides a `QuickResponsesClient` which serves as an interface that
you can use to make requests to search your Amazon Connect Quick Responses Knowledge
Base.

The `QuickResponsesClient` accepts an optional constructor argument,
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

You can instantiate the agent client as follows:

```

import { QuickResponsesClient } from "@amazon-connect/quick-responses";

const quickResponsesClient = new QuickResponsesClient();
```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

Alternatively, providing a constructor argument:

```

import { QuickResponsesClient } from "@amazon-connect/quick-responses";

const quickResponsesClient = new QuickResponsesClient({
    context: sampleContext,
    provider: sampleProvider
});
```

The following sections describe API calls for working with the QuickResponses
API.

###### Contents

- [isEnabled()](3p-apps-quick-responses-requests-isenabled.md "3p-apps-quick-responses-requests-isenabled.md")
- [searchQuickResponses()](3p-apps-quick-responses-requests-searchquickresponses.md "3p-apps-quick-responses-requests-searchquickresponses.md")
