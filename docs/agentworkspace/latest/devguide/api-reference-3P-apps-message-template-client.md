

# Connect Customer SDK Message Template API
<a name="api-reference-3P-apps-message-template-client"></a>

The Connect Customer SDK provides a `MessageTemplateClient` which serves as an interface that you can use to make requests to search and get content from your Connect Customer Message Template Knowledge Base.

The `MessageTemplateClient` constructor accepts a `ConnectClientConfig` argument, which is defined as:

```
export type ConnectClientConfig =
    | AmazonConnectProvider
    | { context: ModuleContext; provider?: AmazonConnectProvider }
    | { provider: AmazonConnectProvider };
```

Pass the `provider` that `AmazonConnectApp.init` returns directly to the constructor:

```
import { MessageTemplateClient } from "@amazon-connect/message-template";

const messageTemplateClient = new MessageTemplateClient(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md), which initializes the default AmazonConnectProvider and returns `{ provider }`.

**Note**  
Third-party applications must be configured with \* permission in order to utilize the MessageTemplateClient APIs.

The following sections describe API calls for working with the MessageTemplate API.

**Topics**
+ [getContent()](3P-apps-message-template-requests-getcontent.md)
+ [isEnabled()](3P-apps-message-template-requests-isenabled.md)
+ [searchMessageTemplates()](3P-apps-message-template-requests-searchmessagetemplates.md)