# Contents of event data

that Amazon SES publishes to Firehose

Amazon SES publishes email sending event records to Amazon Data Firehose in JSON format. When
publishing events to Firehose, Amazon SES follows each JSON record with a newline
character.

You can find example records for all of these notification types in [Examples of event data
that Amazon SES publishes to Firehose](event-publishing-retrieving-firehose-examples.md "event-publishing-retrieving-firehose-examples.md").

###### Topics in this section

- [Top-level JSON object](#event-publishing-retrieving-firehose-contents-top-level-json-object "#event-publishing-retrieving-firehose-contents-top-level-json-object")
- [Mail
  object](#event-publishing-retrieving-firehose-contents-mail-object "#event-publishing-retrieving-firehose-contents-mail-object")
- [Bounce
  object](#event-publishing-retrieving-firehose-contents-bounce-object "#event-publishing-retrieving-firehose-contents-bounce-object")
- [Complaint object](#event-publishing-retrieving-firehose-contents-complaint-object "#event-publishing-retrieving-firehose-contents-complaint-object")
- [Delivery object](#event-publishing-retrieving-firehose-contents-delivery-object "#event-publishing-retrieving-firehose-contents-delivery-object")
- [Send
  object](#event-publishing-retrieving-firehose-contents-send-object "#event-publishing-retrieving-firehose-contents-send-object")
- [Reject
  object](#event-publishing-retrieving-firehose-contents-reject-object "#event-publishing-retrieving-firehose-contents-reject-object")
- [Open
  object](#event-publishing-retrieving-firehose-contents-open-object "#event-publishing-retrieving-firehose-contents-open-object")
- [Click
  object](#event-publishing-retrieving-firehose-contents-click-object "#event-publishing-retrieving-firehose-contents-click-object")
- [Rendering Failure object](#event-publishing-retrieving-firehose-contents-failure-object "#event-publishing-retrieving-firehose-contents-failure-object")
- [DeliveryDelay object](#event-publishing-retrieving-firehose-delivery-delay-object "#event-publishing-retrieving-firehose-delivery-delay-object")
- [Subscription object](#event-publishing-retrieving-firehose-subscription-object "#event-publishing-retrieving-firehose-subscription-object")

## Top-level JSON object

The top-level JSON object in an email sending event record contains the following
fields.

| Field Name      | Description                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `eventType`     | A string that describes the type of event. Possible values:<br>`Bounce`, `Complaint`, `Delivery`,<br>`Send`, `Reject`, `Open`,<br>`Click`, `Rendering Failure`,<br>`DeliveryDelay`, or `Subscription`.<br>If you did not [set up event<br>publishing](monitor-sending-using-event-publishing-setup.md "monitor-sending-using-event-publishing-setup.md") this field is named<br>`notificationType`. |
| `mail`          | A JSON object that contains information about the email that produced the<br>event.                                                                                                                                                                                                                                                                                                                 |
| `bounce`        | This field is only present if `eventType` is<br>`Bounce`. It contains information about the bounce.                                                                                                                                                                                                                                                                                                 |
| `complaint`     | This field is only present if `eventType` is<br>`Complaint`. It contains information about the<br>complaint.                                                                                                                                                                                                                                                                                        |
| `delivery`      | This field is only present if `eventType` is<br>`Delivery`. It contains information about the<br>delivery.                                                                                                                                                                                                                                                                                          |
| `send`          | This field is only present if `eventType` is<br>`Send`.                                                                                                                                                                                                                                                                                                                                             |
| `reject`        | This field is only present if `eventType` is<br>`Reject`. It contains information about the rejection.                                                                                                                                                                                                                                                                                              |
| `open`          | This field is only present if `eventType` is `Open`.<br>It contains information about the open event.                                                                                                                                                                                                                                                                                               |
| `click`         | This field is only present if `eventType` is<br>`Click`. It contains information about the click event.                                                                                                                                                                                                                                                                                             |
| `failure`       | This field is only present if `eventType` is `Rendering<br>Failure`. It contains information about the rendering failure<br>event.                                                                                                                                                                                                                                                                  |
| `deliveryDelay` | This field is only present if `eventType` is<br>`DeliveryDelay`. It contains information about the delayed<br>delivery of an email.                                                                                                                                                                                                                                                                 |
| `subscription`  | This field is only present if `eventType` is<br>`Subscription`. It contains information about the<br>subscription preferences.                                                                                                                                                                                                                                                                      |

## Mail

object

Each email sending event record contains information about the original email in
the `mail` object. The JSON object that contains information about a
`mail` object has the following fields.

| Field Name         | Description                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp`        | The date and time, in ISO8601 format (_YYYY-MM-DDThh:mm:ss.sZ_),<br>when the message was sent.                                                                                                                                                                                                                                                                                                           |
| `messageId`        | A unique ID that Amazon SES assigned to the message. Amazon SES returned this value to you<br>when you sent the message.<br>NoteThis message ID was assigned by Amazon SES. You can find the message ID of the original<br>email in the `headers` and `commonHeaders` fields of the<br>`mail` object.                                                                                                    |
| `source`           | The email address that the message was sent from (the envelope MAIL FROM<br>address).                                                                                                                                                                                                                                                                                                                    |
| `sourceArn`        | The Amazon Resource Name (ARN) of the identity that was used to send the email. In<br>the case of sending authorization, the `sourceArn` is the ARN of the identity<br>that the identity owner authorized the delegate sender to use to send the email. For<br>more information about sending authorization, see [Email authentication<br>methods](sending-authorization.md "sending-authorization.md"). |
| `sendingAccountId` | The AWS account ID of the account that was used to send the email. In the case of<br>sending authorization, the `sendingAccountId` is the delegate sender's<br>account ID.                                                                                                                                                                                                                               |
| `destination`      | A list of email addresses that were recipients of the original mail.                                                                                                                                                                                                                                                                                                                                     |
| `headersTruncated` | A string that specifies whether the headers are truncated in the notification, which<br>occurs if the headers are larger than 10 KB. Possible values are `true` and<br>`false`.                                                                                                                                                                                                                          |
| `headers`          | A list of the email's original headers. Each header in the list has a<br>`name` field and a `value` field.<br>NoteAny message ID within the `headers` field is from the original message<br>that you passed to Amazon SES. The message ID that Amazon SES subsequently assigned to the<br>message is in the `messageId` field of the `mail` object.                                                      |
| `commonHeaders`    | A<br>mapping of the email's original, commonly used headers.<br>NoteAny message ID within the `commonHeaders` field is<br>the message ID that Amazon SES<br>subsequently assigned to the message in the `messageId` field of<br>the `mail` object.                                                                                                                                                       |
| `tags`             | A list of tags associated with the email.                                                                                                                                                                                                                                                                                                                                                                |

## Bounce

object

The JSON object that contains information about a `Bounce` event will
always have the following fields.

| Field Name          | Description                                                                                                                                                                                                                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounceType`        | The type of bounce, as determined by Amazon SES.                                                                                                                                                                                                                                                                     |
| `bounceSubType`     | The subtype of the bounce, as determined by Amazon SES.                                                                                                                                                                                                                                                              |
| `bouncedRecipients` | A list that contains information about the recipients of the original mail that<br>bounced.                                                                                                                                                                                                                          |
| `timestamp`         | The date and time, in ISO8601 format (_YYYY-MM-DDThh:mm:ss.sZ_),<br>when the ISP sent the bounce notification.                                                                                                                                                                                                       |
| `feedbackId`        | A unique ID for the bounce.                                                                                                                                                                                                                                                                                          |
| `reportingMTA`      | The value of the `Reporting-MTA` field from the DSN. This is the value of<br>the Message Transfer Authority (MTA) that attempted to perform the delivery, relay, or<br>gateway operation described in the DSN.<br>NoteThis field only appears if a delivery status notification (DSN) was attached to<br>the bounce. |

### Bounced recipients

A bounce event may pertain to a single recipient or to multiple recipients.
The `bouncedRecipients` field holds a list of objects—one
object per recipient to whom the bounce event pertains—and will always
contain the following field.

| Field Name     | Description                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `emailAddress` | The email address of the recipient. If a DSN is available,<br>this is the value of the `Final-Recipient` field<br>from the DSN. |

Optionally, if a DSN is attached to the bounce, the following fields may also
be present.

| Field Name       | Description                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `action`         | The value of the `Action` field from the DSN.<br>This indicates the action performed by the reporting MTA as<br>a result of its attempt to deliver the message to this<br>recipient.              |
| `status`         | The value of the `Status` field from the DSN.<br>This is the per-recipient transport-independent status code<br>that indicates the delivery status of the message.                                |
| `diagnosticCode` | The status code issued by the reporting MTA. This is the<br>value of the `Diagnostic-Code` field from the<br>DSN. This field may be absent in the DSN (and therefore also<br>absent in the JSON). |

### Bounce types

Each bounce event will be of one of the types shown in the following
table.

The event publishing system only publishes hard bounces and soft bounces that
will no longer be retried by Amazon SES. When you receive bounces marked
`Permanent`, you should remove the corresponding email addresses
from your mailing list; you will not be able to send to them in the future.
`Transient` bounces are sent to you when a message has soft
bounced several times, and Amazon SES has stopped trying to re-deliver it. You may be
able to successfully resend to an address that initially resulted in a
`Transient` bounce in the future.

| bounceType     | bounceSubType              | Description                                                                                                                                                                                                                                                                                              |
| -------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Undetermined` | `Undetermined`             | Amazon SES was unable to determine a specific bounce reason.                                                                                                                                                                                                                                             |
| `Permanent`    | `General`                  | Amazon SES received a general hard bounce. If you receive this type of bounce,<br>you should remove the recipient's email address from your mailing<br>list.                                                                                                                                             |
| `Permanent`    | `NoEmail`                  | Amazon SES received a permanent hard bounce because the target email address<br>does not exist. If you receive this type of bounce, you should remove the<br>recipient's email address from your mailing list.                                                                                           |
| `Permanent`    | `Suppressed`               | Amazon SES has suppressed sending to this address because it has a recent<br>history of bouncing as an invalid address. To override the global<br>suppression list, see [Using the Amazon SES account-level suppression<br>list](sending-email-suppression-list.md "sending-email-suppression-list.md"). |
| `Permanent`    | `OnAccountSuppressionList` | Amazon SES has suppressed sending to this address because it is on the [account-level suppression<br>list](sending-email-suppression-list.md "sending-email-suppression-list.md"). This does not count toward your bounce rate metric.                                                                   |
| `Transient`    | `General`                  | Amazon SES received a general bounce. You may be able to successfully send to<br>this recipient in the future.                                                                                                                                                                                           |
| `Transient`    | `MailboxFull`              | Amazon SES received a mailbox full bounce. You may be able to successfully send<br>to this recipient in the future.                                                                                                                                                                                      |
| `Transient`    | `MessageTooLarge`          | Amazon SES received a message too large bounce. You may be able to successfully<br>send to this recipient if you reduce the size of the message.                                                                                                                                                         |
| `Transient`    | `CustomTimeoutExceeded`    | Amazon SES was not able to successfully deliver the email within the time<br>specified by the email sender. _(The bounce message will specify<br>the reason for any possible delivery attempt failures within the defined<br>TTL.)_                                                                      |
| `Transient`    | `ContentRejected`          | Amazon SES received a content rejected bounce. You may be able to successfully<br>send to this recipient if you change the content of the message.                                                                                                                                                       |
| `Transient`    | `AttachmentRejected`       | Amazon SES received an attachment rejected bounce. You may be able to<br>successfully send to this recipient if you remove or change the<br>attachment.                                                                                                                                                  |

## Complaint object

The JSON object that contains information about a `Complaint` event has
the following fields.

| Field Name             | Description                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `complainedRecipients` | A list that contains information about recipients that may have submitted<br>the complaint.                          |
| `timestamp`            | The date and time, in ISO8601 format<br>(_YYYY-MM-DDThh:mm:ss.sZ_), when the ISP sent the<br>complaint notification. |
| `feedbackId`           | A unique ID for the complaint.                                                                                       |
| `complaintSubType`     | The subtype of the complaint, as determined by Amazon SES.                                                           |

Further, if a feedback report is attached to the complaint, the following fields
may be present.

| Field Name              | Description                                                                                                                                                                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userAgent`             | The value of the `User-Agent` field from the feedback report. This<br>indicates the name and version of the system that generated the report.                                                                         |
| `complaintFeedbackType` | The value of the `Feedback-Type` field from the feedback report received<br>from the ISP. This contains the type of feedback.                                                                                         |
| `arrivalDate`           | The value of the `Arrival-Date` or `Received-Date` field from<br>the feedback report in ISO8601 format (_YYYY-MM-DDThh:mm:ss.sZ_).<br>This field may be absent in the report (and therefore also absent in the JSON). |

### Complained recipients

The `complainedRecipients` field contains a list of recipients that
may have submitted the complaint.

###### Important

Since most ISPs redact the email address of the recipient who submitted
the complaint from their complaint notification, this list contains
information about recipients who might have sent the complaint, based on the
recipients of the original message and the ISP from which we received the
complaint. Amazon SES performs a lookup against the original message to determine
this recipient list.

JSON objects in this list contain the following field.

| Field Name     | Description                         |
| -------------- | ----------------------------------- |
| `emailAddress` | The email address of the recipient. |

### Complaint types

You may see the following complaint types in the
`complaintFeedbackType` field as assigned by the reporting ISP,
according to the [Internet Assigned Numbers Authority website](https://www.iana.org/assignments/marf-parameters/marf-parameters.xml#marf-parameters-2 "https://www.iana.org/assignments/marf-parameters/marf-parameters.xml#marf-parameters-2"):

| Field Name     | Description                                                                                                                                                                              |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `abuse`        | Indicates unsolicited email or some other kind of email abuse.                                                                                                                           |
| `auth-failure` | Email authentication failure report.                                                                                                                                                     |
| `fraud`        | Indicates some kind of fraud or phishing activity.                                                                                                                                       |
| `not-spam`     | Indicates that the entity providing the report does not consider the<br>message to be spam. This may be used to correct a message that was<br>incorrectly tagged or categorized as spam. |
| `other`        | Indicates any other feedback that does not fit into other registered<br>types.                                                                                                           |
| `virus`        | Reports that a virus is found in the originating message.                                                                                                                                |

## Delivery object

The JSON object that contains information about a `Delivery` event will
always have the following fields.

| Field Name             | Description                                                                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `timestamp`            | The date and time when Amazon SES delivered the email to the recipient's mail server, in<br>ISO8601 format (_YYYY-MM-DDThh:mm:ss.sZ_).                                   |
| `processingTimeMillis` | The time in milliseconds between when Amazon SES accepted the request from the sender to<br>when Amazon SES passed the message to the recipient's mail server.           |
| `recipients`           | A list of intended recipients that the delivery event applies to.                                                                                                        |
| `smtpResponse`         | The SMTP response message of the remote ISP that accepted the email from Amazon SES. This<br>message will vary by email, by receiving mail server, and by receiving ISP. |
| `reportingMTA`         | The host name of the Amazon SES mail server that sent the mail.                                                                                                          |
| `remoteMtaIp`          | The IP address of the MTA to which Amazon SES delivered the email.                                                                                                       |

## Send

object

The JSON object that contains information about a `send` event is
always empty.

## Reject

object

The JSON object that contains information about a `Reject` event will
always have the following fields.

| Field Name | Description                                                                                                                                                                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `reason`   | The reason the email was rejected. The only possible value is `Bad<br>content`, which means that Amazon SES detected that the email contained<br>a virus. When a message is rejected, Amazon SES stops processing it, and doesn't<br>attempt to deliver it to the recipient's mail server. |

## Open

object

The JSON object that contains information about a `Open` event will
always contain the following fields.

| Field Name  | Description                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------- |
| `ipAddress` | The recipient's IP address.                                                                     |
| `timestamp` | The date and time when the open event occurred in ISO8601 format<br>(_YYYY-MM-DDThh:mm:ss.sZ_). |
| `userAgent` | The user agent of the device or email client that the recipient used to open the<br>email.      |

## Click

object

The JSON object that contains information about a `Click` event will
always contain the following fields.

| Field Name  | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ipAddress` | The recipient's IP address.                                                                                                                                                                                                                                                                                                                                                              |
| `timestamp` | The date and time when the click event occurred in ISO8601 format<br>(_YYYY-MM-DDThh:mm:ss.sZ_).                                                                                                                                                                                                                                                                                         |
| `userAgent` | The user agent of the client that the recipient used to click a link in<br>the email.                                                                                                                                                                                                                                                                                                    |
| `link`      | The URL of the link that the recipient clicked.                                                                                                                                                                                                                                                                                                                                          |
| `linkTags`  | A list of tags that were added to the link using the `ses:tags`<br>attribute. For more information about adding tags to links in your emails,<br>see [Q5. Can I tag links with unique<br>identifiers?](faqs-metrics.md#sending-metric-faqs-clicks-q5 "faqs-metrics.md#sending-metric-faqs-clicks-q5") in the [Amazon SES email sending metrics FAQs](faqs-metrics.md "faqs-metrics.md"). |

## Rendering Failure object

The JSON object that contains information about a `Rendering Failure`
event has the following fields.

| Field Name     | Description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| `templateName` | The name of the template used to send the email.                         |
| `errorMessage` | A message that provides more information about the rendering<br>failure. |

## DeliveryDelay object

The JSON object that contains information about a `DeliveryDelay` event
has the following fields.

| Field Name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `delayType`         | The type of delay. Possible values are:<br>• **InternalFailure** – An<br>internal Amazon SES issue caused the message to be delayed.<br>• **General** – A generic failure<br>occurred during the SMTP conversation.<br>• **MailboxFull** – The<br>recipient's mailbox is full and is unable to receive additional<br>messages.<br>• **SpamDetected** – The<br>recipient's mail server has detected a large amount of unsolicited<br>email from your account.<br>• **RecipientServerError** – A<br>temporary issue with the recipient's email server is preventing the<br>delivery of the message.<br>• **IPFailure** – The IP address<br>that's sending the message is being blocked or throttled by the<br>recipient's email provider.<br>• **TransientCommunicationFailure**<br>– There was a temporary communication failure during the SMTP<br>conversation with the recipient's email provider.<br>• **BYOIPHostNameLookupUnavailable**<br>– Amazon SES was unable to look up the DNS hostname for your IP<br>addresses. This type of delay only occurs when you use [Bring Your Own IP](dedicated-ip-byo.md "dedicated-ip-byo.md").<br>• **Undetermined** – Amazon SES wasn't<br>able to determine the reason for the delivery delay.<br>• **SendingDeferral** – Amazon SES has<br>deemed it appropriate to internally defer the message. |
| `delayedRecipients` | An object that contains information about the recipient of the<br>email.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `expirationTime`    | The date and time when Amazon SES will stop trying to deliver the message. This<br>value is shown in ISO 8601 format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `reportingMTA`      | The IP address of the Message Transfer Agent (MTA) that reported the<br>delay.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `timestamp`         | The date and time when the delay occurred, shown in ISO 8601<br>format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Delayed recipients

The `delayedRecipients` object contains the following
values.

| Field Name       | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| `emailAddress`   | The email address that resulted in the delivery of the message being<br>delayed. |
| `status`         | The SMTP status code associated with the delivery delay.                         |
| `diagnosticCode` | The diagnostic code provided by the receiving Message Transfer Agent<br>(MTA).   |

## Subscription object

The JSON object that contains information about a `Subscription` event
has the following fields.

| Field Name            | Description                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `contactList`         | The name of the list the contact is on.                                                                                                                                                       |
| `timestamp`           | The date and time, in ISO8601 format<br>_(YYYY-MM-DDThh:mm:ss.sZ)_, when the ISP sent the<br>subscription notification.                                                                       |
| `source`              | The email address that the message was sent from (the envelope MAIL FROM<br>address).                                                                                                         |
| `newTopicPreferences` | A JSON data-structure (map) which specifies the subscription status of all<br>the topics in the contact list indicating the status after a change (contact<br>subscribed or unsubscribed).    |
| `oldTopicPreferences` | A JSON data-structure (map) which specifies the subscription status of all<br>the topics in the contact list indicating the status before the change<br>(contact subscribed or unsubscribed). |

### New/old topic preferences

The `newTopicPreferences` and `oldTopicPreferences`
objects contain the following values.

| Field Name                       | Description                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `unsubscribeAll`                 | Specifies if the contact unsubscribed from all the topics in the contact<br>list.                                                                                                                                                                                                                                                                      |
| `topicSubscriptionStatus`        | Specifies the subscription status<br>of the topic in the `topicName` field indicating whether it is<br>currently subscribed to receive notifications from SES for the<br>specified event type. Possible values are **OptIn**<br>(subscribed) or \*_OptOut_<br>• (unsubscribed) in the<br>`subscriptionStatus` field.                                   |
| `topicDefaultSubscriptionStatus` | Specifies the default subscription<br>status of the topic in the `topicName` field determining whether<br>new topics added to the event destination will be subscribed or unsubscribed<br>by default. Possible values are **OptIn\*<br>• (subscribed by<br>default) or **OptOut\*<br>• (unsubscribed by default) in the<br>`subscriptionStatus` field. |
