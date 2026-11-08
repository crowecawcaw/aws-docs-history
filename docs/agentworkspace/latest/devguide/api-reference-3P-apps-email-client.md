

# Connect Customer SDK Email API
<a name="api-reference-3P-apps-email-client"></a>

The Connect Customer SDK provides an `EmailClient` which serves as an interface that your app can use to subscribe to email contact events and make email contact requests.

The `EmailClient` constructor accepts a `ConnectClientConfig` argument, which is defined as:

```
export type ConnectClientConfig =
    | AmazonConnectProvider
    | { context: ModuleContext; provider?: AmazonConnectProvider }
    | { provider: AmazonConnectProvider };
```

Pass the `provider` that `AmazonConnectApp.init` returns directly to the constructor:

```
import { EmailClient } from "@amazon-connect/email";

const emailClient = new EmailClient(provider);
```

**Note**  
You must first instantiate the [ AmazonConnectApp](getting-started-initialize-sdk.md), which initializes the default AmazonConnectProvider and returns `{ provider }`.

**Note**  
All `EmailClient` operations require the `*` permission.  
The contact scope of the application instance applies only to `getEmailData()` and `sendEmail()`. Both require an instance that is scoped to the contact that you pass in `contactId`, or an instance without a contact scope. `createDraftEmail()`, `getEmailThread()`, and `listFromEmailAddresses()` are not restricted by the contact scope of the instance. For details about contact scope, see [Connect Customer SDK Contact API](api-reference-3P-apps-contact-client.md).

The following sections describe API calls for working with the Email API.

**Topics**
+ [onAcceptedEmail()](3P-apps-email-requests-acceptedemail-subscribing.md)
+ [offAcceptedEmail()](3P-apps-email-requests-acceptedemail-unsubscribing.md)
+ [createDraftEmail()](3P-apps-email-requests-createdraftemail.md)
+ [onDraftEmailCreated()](3P-apps-email-requests-draftemailcreated-subscribing.md)
+ [offDraftEmailCreated()](3P-apps-email-requests-draftemailcreated-unsubscribing.md)
+ [getEmailData()](3P-apps-email-requests-getemaildata.md)
+ [getEmailThread()](3P-apps-email-requests-getemailthread.md)
+ [listFromEmailAddresses()](3P-apps-email-requests-listfromemailaddresses.md)
+ [sendEmail()](3P-apps-email-requests-sendemail.md)