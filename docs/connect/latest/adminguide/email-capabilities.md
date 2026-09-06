

# How Connect Customer email works
<a name="email-capabilities"></a>

Connect Customer Email provides built-in capabilities that make it easy for you to prioritize, assign, and automate the resolution of customer service emails, improving customer satisfaction and agent productivity. You can receive and respond to emails sent by customers to your [configured email addresses](create-email-address1.md), or submitted by using web forms on your website or mobile app by using the [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API. 

Connect Customer Email integrates with [Amazon Simple Email Service (SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) to send, receive, and monitor emails for [content marked as spam or containing viruses](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-auth-and-scan), [delivery success rates](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html), and [sender reputation results](https://docs.aws.amazon.com/ses/latest/dg/monitor-sender-reputation.html). 

 This topic explains how Connect Customer Email, along with Amazon SES, work to enable a seamless customer experience.

**Topics**
+ [Receive emails](#email-capabilities-howreceived)
+ [Email contacts](#email-capabilities-howtranslated)
+ [Every email message is a unique email contact](#email-capabilities-howmanaged)
+ [Email threads](#email-capabilities-howthreadsmanaged)
+ [Send email](#email-capabilities-howemailssent)
+ [Handling email loops](#email-capabilities-loops)

## Receive emails
<a name="email-capabilities-howreceived"></a>

There are three main ways that Connect Customer can receive emails: 
+ **Method 1**: By an [email address](create-email-address1.md) defined in Connect Customer (for example, support@{{customer-domain}}.com) using a [verified email domain from Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-domain-proc), such as the email domain provided with your Connect Customer instance (for example, @{{instance-alias}}.email.connect.aws) or a custom verified domain that you own or is provided by your company (for example, @{{customer-domain}}.com). See [Step 3: Use your own custom email domains](enable-email1.md#use-custom-email) in [Enable email for your instance](enable-email1.md) for details about onboarding custom email domains. 
+ **Method 2**: By using a routing rule on your email server (for example, [Microsoft 365 Connectors](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/use-connectors-to-configure-mail-flow/set-up-connectors-to-route-mail), [Google Workspace Mail Routes](https://support.google.com/a/answer/2614757?hl=en&ref_topic=2921034&sjid=9077065025577504786-NC)) to send the incoming email to one of [the SMTP endpoints of Amazon SES](https://docs.aws.amazon.com/general/latest/gr/ses.html) using a verified email domain onboarded to Amazon SES (for example, @{{customer-domain}}.com). 
+ **Method 3**: By using the [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API to start an email contact by using a webform on your website or in your mobile app. This starts inbound email contacts similar to customers sending emails to your email addresses. 

The following diagram illustrates how emails sent from your customers are received by Connect Customer using the [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API for each of the methods mentioned above.

![How a message is sent as a webform or email to the StartEmailContact API.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-ses-diagram.png)


To integrate Methods 1 or 2, you need to verify an email domain on Amazon SES before you can use the email domain in Connect Customer. For instructions, see [Verifying a DKIM domain identity with your DNS provider](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#just-verify-domain-proc). 

To integrate Method 3, you use the [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API. This is the primary API of all integration methods for inbound email contacts. It functions similarly to [StartTaskContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartTaskContact.html). It requires you to do one of the following steps:
+ Include at least one email address from your Connect Customer instance in either the To or CC attributes of the inbound email contact.

—OR—
+ Define an inbound flow from your Connect Customer instance to route the inbound email contact created.

If both are defined, the default behavior prioritizes the inbound flow from your Connect Customer instance to handle the inbound email contact created. If multiple email addresses from your Connect Customer instance are included in the To or CC email address attributes, multiple inbound email contacts will be created in your Connect Customer instance.

## How email messages become email contacts
<a name="email-capabilities-howtranslated"></a>

For general email receiving in Connect Customer, including webform based email, the [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API exposes basic email fields on the request object. This object is used to populate email information and start an email contact in Connect Customer. The following fields are included:
+ A From email address
+ To email address(es)
+  CC email address(es)
+ A subject
+ A plain or HTML message body
+ Attachment(s)

For more information about how the email contact information is populated into the email contact, see the Connect Customer email contact data model .

After the [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API has performed request parameter validation and ensured that at least one To or CC email address is valid and exists in the Connect Customer instance, here's what happens: 

1. A contact ID is generated and returned as part of the API response body.

1. An asynchronous workflow is triggered to perform additional email message processing. 

1. The flow is started. This is the flow that's associated with the email address found in the Connect Customer instance.

As part of this, you need to setup your email message and attachment storage for your Connect Customer instance. 
+ Both email messages and attachments are stored and accessed in your own Amazon SES S3 bucket. 
+ The remaining email contact attributes such as To, CC, Subject, and other attributes are stored on the email contact; see [Data model for Connect Customer contact records](ctr-data-model.md).

The following diagram illustrates the flow of the email message from the customer to Amazon SES and then to Connect Customer. It shows the email message content stored in your S3 bucket, and then getting data from that bucket to display it to the agent. 

![Email message content stored in your S3 bucket.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-concepts-translated.png)


## Every email message is a unique email contact
<a name="email-capabilities-howmanaged"></a>

Connect Customer email differs from voice, chat, and tasks. 
+ Every email message, inbound to or outbound from Connect Customer, is its own unique email contact.
+ Each email contact contains details specific to that email message such as From address, To address(es), CC address(es), subject, relatedContactId, links to email body and attachment(s) storage locations, and other details relevant to the individual email contact.

 However, like other channels in Connect Customer, an email contact has similar initiation methods, such as `INBOUND`, `OUTBOUND`, `TRANSFER`, `API`, `QUEUE_TRANSFER` and `END/DISCONNECT`. It also has similar states, such as `CREATED`, `QUEUED`, `CONNECTING`, `CONNECTED`, `MISSED`, `TRANSFERRED`, `ERROR`, `ENDED/DISCONNECTED`, `REJECTED`. 

For information about how the email contact information is populated into the email contact, see [Data model for Connect Customer contact records](ctr-data-model.md).

## Email threads
<a name="email-capabilities-howthreadsmanaged"></a>

Email threading makes sure that outgoing emails and incoming responses related to a customer inquiry are associated with each other in a chronological and organized fashion. 

To maintain the whole email conversation, Connect Customer links the email contacts together using a few fields on the email contact such as the relatedContactId and a list of email headers that follow conventional email client standards (RFC 5256). 

Most email clients such as Gmail, Apple Mail, and Outlook, support email threading. However, keep in mind that there are some that don't support it. 

If your customer replies to the latest email message in the thread, the thread follows a straightforward pattern as shown in the following image:

![The email thread in a straightforward pattern.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-threading.png)


If the customer replies to an older message in the email thread, an email thread tree is formed. The email thread pattern looks something like the example in the following image:

![The email thread in a tree pattern.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-threading-tree.png)


In both scenarios Connect Customer keeps a record of each of the email messages that are related to a thread. Each email message can be accessed by the email that succeeded it. 

## Send email
<a name="email-capabilities-howemailssent"></a>

All email messages from Connect Customer are sent from Amazon SES directly to your customer. Whether you're using the email domain provided with your Connect Customer instance (for example, @{{instance-alias}}.email.connect.aws) or a custom verified domain (for example, @{{customer}}.com), Amazon SES is authorized by verifying a domain identity to send emails directly to your customers.

The following diagram shows that the [StartOutboundEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundEmailContact.html) API sends email to Amazon SES, and Amazon SES sends it to your customer.

![Email flow from StartOutboundEmailContact API through SES to customer.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-concepts-sent.png)


The [StartOutboundEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundEmailContact.html) API is the primary API of all integration methods for outbound email contacts including agent replies to inbound contact and agent-initiated outbound email contacts.
+ It functions similarly to [StartEmailContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartEmailContact.html) API, however it is the inverse since it is outbound.
+  It requires at least one email address in either the To or CC email address attributes and it requires an outbound whisper flow for handling the outbound contact.

## Handling email loops
<a name="email-capabilities-loops"></a>

Emails can loop back into your Connect Customer instance in two ways. The first is self-addressed messages (where the sender and recipient are the same). The second is automated responses such as bounce notifications and out-of-office replies. Connect Customer automatically blocks self-addressed emails from re-entering your system. However, automated responses can still create loops. To prevent this, add filtering logic to your inbound email flows that detects and discards these messages.

### Emails that loop back to the same address
<a name="email-capabilities-selfaddressed"></a>

**Automatic behavior**  
Connect Customer applies this behavior automatically, and you cannot turn it off. It prevents duplicate emails from creating unwanted contacts in your contact center.

When an agent replies to an email, the reply is sent from the queue's configured email address. If an agent CCs or includes that same address in the To field, the email is delivered back to your Connect Customer instance.

Connect Customer automatically ignores these emails and does not create new inbound contacts. This prevents duplicate contacts and ensures replies or outbound emails are not re-routed back to agents.

### Prevent automated email loops
<a name="email-capabilities-preventloops"></a>

Email loops can occur when you configure automated responses on your Connect Customer instance using the **Send message** block. The automated reply might trigger a bounce (Non-Delivery Report/NDR). It might also reach a mailbox with an out-of-office auto-reply enabled. In either case, your Connect Customer instance ingests that response as a new inbound email. This triggers another automated reply and creates an infinite loop. Connect Customer does not natively detect or suppress NDR or out-of-office messages. For safeguards that apply when you use the **Send message** block in outbound flows, see [Important information about using the Send message block in outbound flows](send-message.md#send-message-outboundflow-important).

To prevent automated email loops, implement the following logic in your inbound email flows, and optionally adjust your Amazon SES notification settings:
+ **Filter automated senders in your inbound email flow** – Place a [Check contact attributes](check-contact-attributes.md) block early in the flow, before any case creation or automated reply logic. Branch on the sender attribute `$.CustomerEndpoint.Address`. Use Contains conditions to match patterns such as `mailer-daemon`, `MAILER-DAEMON`, `postmaster`, `noreply`, `no-reply`, and `bounces+`. String comparisons in the **Check contact attributes** block are case-sensitive, so include both lowercase and uppercase variants of each pattern. On match, end the contact with [Disconnect / hang up](disconnect-hang-up.md) or route it to a supervisor review queue. As a secondary check, inspect `$.SegmentAttributes['connect:EmailSubject']` for bounce subject prefixes such as `Undeliverable:` and `Mail Delivery Failed`.
+ **(Optional) Disable Amazon SES email feedback forwarding** – By default, Amazon SES delivers bounce and complaint notifications as email to the sending address, which is how NDRs enter your support inbox. Disable email feedback forwarding and route notifications to an Amazon Simple Notification Service (Amazon SNS) topic instead. You can disable forwarding only after you configure Amazon SNS topics for both bounces and complaints. For more information, see [Receiving Amazon SES notifications through email](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity-using-notifications-email.html) and [Configuring Amazon SNS notifications for Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/configure-sns-notifications.html).

**Filter on the sender address**  
`$.SystemEndpoint.Address` contains your Connect Customer instance's configured email address – not the sender's email address. Do not use it as a filter condition, because it does not match against incoming sender addresses (including automated email responses).