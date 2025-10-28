# Amazon Connect Agent Workspace Email API

The SDK provides an `EmailClient` which serves as an interface that your
app can use to subscribe to email contact events and make email contact requests.

The `EmailClient` accepts an optional constructor argument,
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

import { EmailClient } from "@amazon-connect/email";

const emailClient = new EmailClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

Alternatively, providing a constructor argument:

```

import { EmailClient } from "@amazon-connect/email";

const emailClient = new EmailClient({
    context: sampleContext,
    provider: sampleProvider
});

```

The following sections describe API calls for working with the Email API.

###### Contents

- [createDraftEmail()](3p-apps-email-requests-createdraftemail.md "3p-apps-email-requests-createdraftemail.md")
- [getEmailData()](3p-apps-email-requests-getemaildata.md "3p-apps-email-requests-getemaildata.md")
- [getEmailThread()](3p-apps-email-requests-getemailthread.md "3p-apps-email-requests-getemailthread.md")
- [onAcceptedEmail()](3p-apps-email-requests-acceptedemail-subscribing.md "3p-apps-email-requests-acceptedemail-subscribing.md")
- [offAcceptedEmail()](3p-apps-email-requests-acceptedemail-unsubscribing.md "3p-apps-email-requests-acceptedemail-unsubscribing.md")
- [onDraftEmailCreated()](3p-apps-email-requests-draftemailcreated-subscribing.md "3p-apps-email-requests-draftemailcreated-subscribing.md")
- [offDraftEmailCreated()](3p-apps-email-requests-draftemailcreated-unsubscribing.md "3p-apps-email-requests-draftemailcreated-unsubscribing.md")
- [sendEmail()](3p-apps-email-requests-sendemail.md "3p-apps-email-requests-sendemail.md")
