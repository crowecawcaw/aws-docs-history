

# Connect Customer SDK Quick Responses API

The Connect Customer SDK provides a `QuickResponsesClient` which serves as an interface that you can use to make requests to search your Connect Customer Quick Responses Knowledge Base.

The `QuickResponsesClient` constructor accepts a `ConnectClientConfig` argument, which is defined as:

```typescript
export type ConnectClientConfig =
    | AmazonConnectProvider
    | { context: ModuleContext; provider?: AmazonConnectProvider }
    | { provider: AmazonConnectProvider };
```

Pass the `provider` that `AmazonConnectApp.init` returns directly to the constructor:

```typescript
import { QuickResponsesClient } from "@amazon-connect/quick-responses";

const quickResponsesClient = new QuickResponsesClient(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md), which initializes the default AmazonConnectProvider and returns `{ provider }`.

**Note**  
Third-party applications must be configured with \* permission in order to utilize the QuickResponsesClient APIs.

The following sections describe API calls for working with the QuickResponses API.

**Topics**
+ [isEnabled()](3P-apps-quick-responses-requests-isenabled.md)
+ [searchQuickResponses()](3P-apps-quick-responses-requests-searchquickresponses.md)