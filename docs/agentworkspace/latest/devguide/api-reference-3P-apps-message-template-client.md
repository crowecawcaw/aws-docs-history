# Amazon Connect Agent Workspace Message Template API

The Amazon Connect SDK provides a `MessageTemplateClient` which serves as an interface that
you can use to make requests to search and get content from your Amazon Connect Message
Template Knowledge Base.

The `MessageTemplateClient` accepts an optional constructor argument, `ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};
```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually
configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

import { MessageTemplateClient } from "@amazon-connect/message-template";

const messageTemplateClient = new MessageTemplateClient({ provider });
```

###### Note

You must first instantiate the [AmazonConnectApp](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which initializes the default AmazonConnectProvider and returns `{ provider }` . This is the recommended option.

Alternatively, providing a constructor argument:

```

import { MessageTemplateClient } from "@amazon-connect/message-template";

const messageTemplateClient = new MessageTemplateClient({
    context: sampleContext,
    provider: sampleProvider
});
```

###### Note

Third-party applications must be configured with \* permission in order to utilize the MessageTemplateClient APIs.

The following sections describe API calls for working with the MessageTemplate
API.

###### Contents

- [getContent()](3P-apps-message-template-requests-getcontent.md "3P-apps-message-template-requests-getcontent.md")
- [isEnabled()](3P-apps-message-template-requests-isenabled.md "3P-apps-message-template-requests-isenabled.md")
- [searchMessageTemplates()](3P-apps-message-template-requests-searchmessagetemplates.md "3P-apps-message-template-requests-searchmessagetemplates.md")
