# Amazon SNS notification contents for Amazon SES

Bounce, complaint, and delivery notifications are published to [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns "https://aws.amazon.com/sns") topics in JavaScript Object Notation
(JSON) format. The top-level JSON object contains a `notificationType` string, a
`mail` object, and either a `bounce` object, a
`complaint` object, or a `delivery` object.

See the following sections for descriptions of the different types of objects:

- [Top-level JSON object](#top-level-json-object "#top-level-json-object")
- [mail object](#mail-object "#mail-object")
- [bounce object](#bounce-object "#bounce-object")
- [complaint object](#complaint-object "#complaint-object")
- [delivery object](#delivery-object "#delivery-object")
  The following are some important notes about the contents of Amazon SNS notifications for
  Amazon SES:

- For a given notification type, you might receive one Amazon SNS notification for
  multiple recipients, or you might receive a single Amazon SNS notification per recipient.
  Your code should be able to parse the Amazon SNS notification and handle both cases;
  SES does not make ordering or batching guarantees for notifications sent
  through Amazon SNS. However, different Amazon SNS notification types (for example, bounces and
  complaints) are not combined into a single notification.
- You might receive multiple types of Amazon SNS notifications for one recipient. For
  example, the receiving mail server might accept the email (triggering a delivery
  notification), but after processing the email, the receiving mail server might
  determine that the email actually results in a bounce (triggering a bounce
  notification). However, these are always separate notifications because they are
  different notification types.
- SES reserves the right to add additional fields to the notifications. As
  such, applications that parse these notifications must be flexible enough to handle
  unknown fields.
- SES overwrites the headers of the message when it sends the email. You can
  retrieve the headers of the original message from the `headers` and
  `commonHeaders` fields of the `mail` object.

## Top-Level JSON object

The top-level JSON object in an SES notification contains the following
fields.

| Field name         | Description                                                                                                                                                                                                                                                                                                                 |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `notificationType` | A string that holds the type of notification represented by the<br>JSON object. Possible values are `Bounce`,<br>`Complaint`, or `Delivery`.<br>If you [set up<br>event publishing](monitor-sending-using-event-publishing-setup.md "monitor-sending-using-event-publishing-setup.md"), this field is named<br>`eventType`. |
| `mail`             | A JSON object that contains information about the original mail to<br>which the notification pertains. For more information, see [Mail object](#mail-object "#mail-object").                                                                                                                                                |
| `bounce`           | This field is present only if the `notificationType` is<br>`Bounce` and contains a JSON object that holds<br>information about the bounce. For more information, see [Bounce object](#bounce-object "#bounce-object").                                                                                                      |
| `complaint`        | This field is present only if the `notificationType` is<br>`Complaint` and contains a JSON object that holds<br>information about the complaint. For more information, see [Complaint object](#complaint-object "#complaint-object").                                                                                       |
| `delivery`         | This field is present only if the `notificationType` is<br>`Delivery` and contains a JSON object that holds<br>information about the delivery. For more information, see [Delivery object](#delivery-object "#delivery-object").                                                                                            |

## Mail object

Each bounce, complaint, or delivery notification contains information about the
original email in the `mail` object. The JSON object that contains
information about a `mail` object has the following fields.

| Field name         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp`        | The time at which the original message was sent (in ISO8601<br>format).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `messageId`        | A unique ID that SES assigned to the message. SES<br>returned this value to you when you sent the message.<br>NoteThis message ID was assigned by SES. You can find the<br>message ID of the original email in the `headers`<br>field of the `mail` object.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `source`           | The email address from which the original message was sent (the<br>envelope MAIL FROM address).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `sourceArn`        | The Amazon Resource Name (ARN) of the identity that was used to<br>send the email. In the case of sending authorization, the<br>`sourceArn` is the ARN of the identity that the<br>identity owner authorized the delegate sender to use to send the<br>email. For more information about sending authorization, see [Email authentication<br>methods](sending-authorization.md "sending-authorization.md").                                                                                                                                                                                                                                                     |
| `sourceIp`         | The originating public IP address of the client that performed the<br>email sending request to SES.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `sendingAccountId` | The AWS account ID of the account that was used to send the<br>email. In the case of sending authorization, the<br>`sendingAccountId` is the delegate sender's account<br>ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `callerIdentity`   | The IAM identity of the SES user who sent the<br>email.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `destination`      | A list of email addresses that were recipients of the original<br>mail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `headersTruncated` | This object is only present if you configured the notification<br>settings to include the headers from the original email.<br>Indicates whether the headers are truncated in the notification.<br>SES truncates the headers in the notification when the<br>headers from the original message are 10 KB or larger in size.<br>Possible values are `true` and `false`.                                                                                                                                                                                                                                                                                           |
| `headers`          | This object is only present if you configured the notification<br>settings to include the headers from the original email.<br>A list of the email's original headers. Each header in the list<br>has a `name` field and a `value` field.<br>NoteAny message ID within the `headers` object is from<br>the original message that you passed to SES. The message<br>ID that SES subsequently assigned to the message is in<br>the `messageId` field of the `mail`<br>object.                                                                                                                                                                                      |
| `commonHeaders`    | This object is only present if you configured the notification<br>settings to include the headers from the original email.<br>Includes information about common email headers from the original<br>email, including the From, To, and Subject fields. Within this<br>object, each header is a key. The From and To fields are represented<br>by arrays that can contain multiple values.<br>NoteFor events, any message ID within the<br>`commonHeaders` field is the message ID that<br>Amazon SES subsequently assigned to the message in the<br>`messageId` field of the mail object.<br>Notifications will contain the message ID of the original<br>email. |

The following is an example of a `mail` object that includes the original
email headers. When this notification type is not configured to include the original
email headers, the `mail` object does not include the
`headersTruncated`, `headers`, and `commonHeaders`
fields.

```
{
   "timestamp":"2018-10-08T14:05:45 +0000",
   "messageId":"000001378603177f-7a5433e7-8edb-42ae-af10-f0181f34d6ee-000000",
   "source":"sender@example.com",
   "sourceArn": "arn:aws:ses:us-east-1:888888888888:identity/example.com",
   "sourceIp": "127.0.3.0",
   "sendingAccountId":"123456789012",
   "destination":[
      "recipient@example.com"
   ],
   "headersTruncated":false,
   "headers":[
      {
         "name":"From",
         "value":"\"Sender Name\" <sender@example.com>"
      },
      {
         "name":"To",
         "value":"\"Recipient Name\" <recipient@example.com>"
      },
      {
         "name":"Message-ID",
         "value":"custom-message-ID"
      },
      {
         "name":"Subject",
         "value":"Hello"
      },
      {
         "name":"Content-Type",
         "value":"text/plain; charset=\"UTF-8\""
      },
      {
         "name":"Content-Transfer-Encoding",
         "value":"base64"
      },
      {
         "name":"Date",
         "value":"Mon, 08 Oct 2018 14:05:45 +0000"
      }
   ],
   "commonHeaders":{
      "from":[
         "Sender Name <sender@example.com>"
      ],
      "date":"Mon, 08 Oct 2018 14:05:45 +0000",
      "to":[
         "Recipient Name <recipient@example.com>"
      ],
      "messageId":" custom-message-ID",
      "subject":"Message sent using SES"
   }
}
```

## Bounce object

The JSON object that contains information about bounces contains the following
fields.

| Field name          | Description                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounceType`        | The type of bounce, as determined by SES. For more<br>information, see [Bounce types](#bounce-types "#bounce-types").                                                                                    |
| `bounceSubType`     | The subtype of the bounce, as determined by SES. For more<br>information, see [Bounce types](#bounce-types "#bounce-types").                                                                             |
| `bouncedRecipients` | A list that contains information about the recipients of the<br>original mail that bounced. For more information, see [Bounced recipients](#bounced-recipients "#bounced-recipients").                   |
| `timestamp`         | The date and time at which the bounce was sent (in ISO8601<br>format). Note that this is the time at which the notification was<br>sent by the ISP, and not the time at which it was received by<br>SES. |
| `feedbackId`        | A unique ID for the bounce.                                                                                                                                                                              |

If SES was able to contact the remote Message Transfer Authority (MTA), the
following field is also present.

| Field name    | Description                                                               |
| ------------- | ------------------------------------------------------------------------- |
| `remoteMtaIp` | The IP address of the MTA to which SES attempted to deliver<br>the email. |

If a delivery status notification (DSN) was attached to the bounce, the following
field is also present.

| Field name     | Description                                                                                                                                                                       |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `reportingMTA` | The value of the `Reporting-MTA` field from the DSN.<br>This is the value of the MTA that attempted to perform the delivery,<br>relay, or gateway operation described in the DSN. |

The following is an example of a `bounce` object.

```
{
   "bounceType":"Permanent",
   "bounceSubType": "General",
   "bouncedRecipients":[
      {
         "status":"5.0.0",
         "action":"failed",
         "diagnosticCode":"smtp; 550 user unknown",
         "emailAddress":"recipient1@example.com"
      },
      {
         "status":"4.0.0",
         "action":"delayed",
         "emailAddress":"recipient2@example.com"
      }
   ],
   "reportingMTA": "example.com",
   "timestamp":"2012-05-25T14:59:38.605Z",
   "feedbackId":"000001378603176d-5a4b5ad9-6f30-4198-a8c3-b1eb0c270a1d-000000",
   "remoteMtaIp":"127.0.2.0"
}

```

### Bounced recipients

A bounce notification may pertain to a single recipient or to multiple recipients.
The `bouncedRecipients` field holds a list of objects—one per recipient
to whom the bounce notification pertains—and always contains the following
field.

| Field name     | Description                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `emailAddress` | The email address of the recipient. If a DSN is available,<br>this is the value of the `Final-Recipient` field from<br>the DSN. |

Optionally, if a DSN is attached to the bounce, the following fields may also be
present.

| Field name       | Description                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `action`         | The value of the `Action` field from the DSN. This<br>indicates the action performed by the Reporting-MTA as a result<br>of its attempt to deliver the message to this recipient.                 |
| `status`         | The value of the `Status` field from the DSN. This<br>is the per-recipient transport-independent status code that<br>indicates the delivery status of the message.                                |
| `diagnosticCode` | The status code issued by the reporting MTA. This is the value<br>of the `Diagnostic-Code` field from the DSN. This<br>field may be absent in the DSN (and therefore also absent in the<br>JSON). |

The following is an example of an object that might be in the
`bouncedRecipients` list.

```
{
    "emailAddress": "recipient@example.com",
    "action": "failed",
    "status": "5.0.0",
    "diagnosticCode": "X-Postfix; unknown user"
}
```

### Bounce types

The bounce object contains a bounce type of `Undetermined`,
`Permanent`
_(hard)_, or `Transient`
_(soft)_. The `Permanent`
_(hard)_ and `Transient`
_(soft)_ bounce types can also contain one of several bounce
subtypes.

When you receive a bounce notification with a bounce type of
`Transient`
_(soft)_, you might be able to send email to that recipient in
the future if the issue that caused the message to bounce is resolved.

When you receive a bounce notification with a bounce type of
`Permanent`
_(hard)_, it's unlikely that you'll be able to send email to that
recipient in the future. For this reason, you should immediately remove the
recipient whose address produced the bounce from your mailing lists.

###### Note

When a _soft bounce_ (a bounce related to a temporary
issue, such as the recipient's inbox being full) occurs, SES attempts to
redeliver the email for a certain period of time. At the end of that period of
time, if SES still can't deliver the email, it stops trying.

SES provides notifications for hard bounces, and for soft bounces that
it stopped trying to deliver. If you want to receive a notification each time a
soft bounce occurs, [enable event publishing](monitor-sending-using-event-publishing-setup.md "monitor-sending-using-event-publishing-setup.md") and configure it to send notifications when
delivery delay events occur.

| bounceType     | bounceSubType              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Undetermined` | `Undetermined`             | The recipient's email provider sent a bounce message. The<br>bounce message didn't contain enough information for SES<br>to determine the reason for the bounce. The bounce email, which<br>was sent to the address in the Return-Path header of the email<br>that resulted in the bounce, might contain additional<br>information about the issue that caused the email to<br>bounce.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `Permanent`    | `General`                  | The recipient's email provider sent a hard bounce message.<br>ImportantWhen you receive this type of bounce notification, you<br>should immediately remove the recipient's email address from<br>your mailing list. Sending messages to addresses that<br>produce hard bounces can have a negative impact on your<br>reputation as a sender. If you continue sending email to<br>addresses that produce hard bounces, we might pause your<br>ability to send additional email. See [Using the Amazon SES account-level suppression<br>list](sending-email-suppression-list.md "sending-email-suppression-list.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `Permanent`    | `NoEmail`                  | It was not possible to retrieve the recipient email address<br>from the bounce message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Permanent`    | `Suppressed`               | The recipient's email address is on the SES suppression<br>list because it has a recent history of producing hard bounces.<br>To override the global suppression list, see [Using the Amazon SES account-level suppression<br>list](sending-email-suppression-list.md "sending-email-suppression-list.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `Permanent`    | `OnAccountSuppressionList` | SES has suppressed sending to this address because<br>it is on the [account-level suppression list](sending-email-suppression-list.md "sending-email-suppression-list.md"). This does not count<br>toward your bounce rate metric.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Permanent`    | `UnsubscribedRecipient`    | This bounce type occurs when the recipient contact has<br>unsubscribed from the topic and a mail is sent to them using<br>[list management options](sending-email-list-management.md#configuring-list-management-list-contacts "sending-email-list-management.md#configuring-list-management-list-contacts"). SES respects the<br>contact preference and doesn't attempt delivery. Also, this<br>bounce doesn't impact sender reputation since the delivery was<br>not attempted, nor is the recipient contact added to a<br>suppression list due to the bounce.<br>TipIt's recommended that you subscribe to<br>UnsubscribedRecipient events to avoid continued sending to<br>to unsubscribed recipients. Consider [Using list management](sending-email-list-management.md "sending-email-list-management.md"). List<br>management should be the source of truth for your subscriber<br>list. From the perspective of SES enforcement, if you<br>continue to send to suppressed or unsubscribed recipients,<br>you'll have the reputation of not adhering to best practices<br>for email sending. |
| `Transient`    | `General`                  | The recipient's email provider sent a general bounce message.<br>You might be able to send a message to the same recipient in the<br>future if the issue that caused the message to bounce is<br>resolved.<br>NoteIf you send an email to a recipient who has an active<br>automatic response rule (such as an "out of the office"<br>message), you might receive this type of notification. Even<br>though the response has a notification type of<br>`Bounce`, SES doesn't count automatic<br>responses when it calculates the bounce rate for your<br>account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Transient`    | `MailboxFull`              | The recipient's email provider sent a bounce message because<br>the recipient's inbox was full. You might be able to send to the<br>same recipient in the future when the mailbox is no longer<br>full.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `Transient`    | `MessageTooLarge`          | The recipient's email provider sent a bounce message because<br>message you sent was too large. You might be able to send a<br>message to the same recipient if you reduce the size of the<br>message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `Transient`    | `ContentRejected`          | The recipient's email provider sent a bounce message because<br>the message you sent contains content that the provider doesn't<br>allow. You might be able to send a message to the same recipient<br>if you change the content of the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Transient`    | `AttachmentRejected`       | The recipient's email provider sent a bounce message because<br>the message contained an unacceptable attachment. For example,<br>some email providers may reject messages with attachments of a<br>certain file type, or messages with very large attachments. You<br>might be able to send a message to the same recipient if you<br>remove or change the content of the attachment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Complaint object

The JSON object that contains information about complaints has the following
fields.

| Field name             | Description                                                                                                                                                                                                                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `complainedRecipients` | A list that contains information about recipients that may have<br>been responsible for the complaint. For more information, see [Complained recipients](#complained-recipients "#complained-recipients").                                                                                                                                 |
| `timestamp`            | The date and time when the ISP sent the complaint notification, in<br>ISO 8601 format. The date and time in this field might not be the<br>same as the date and time when SES received the notification.                                                                                                                                   |
| `feedbackId`           | A unique ID associated with the complaint.                                                                                                                                                                                                                                                                                                 |
| `complaintSubType`     | The value of the `complaintSubType` field can either<br>be null or `OnAccountSuppressionList`. If the value is<br>`OnAccountSuppressionList`, SES accepted the<br>message, but didn't attempt to send it because it was on the [account-level<br>suppression list](sending-email-suppression-list.md "sending-email-suppression-list.md"). |

Further, if a feedback report is attached to the complaint, the following fields may
be present.

| Field name              | Description                                                                                                                                                                                     |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `userAgent`             | The value of the `User-Agent` field from the feedback<br>report. This indicates the name and version of the system that<br>generated the report.                                                |
| `complaintFeedbackType` | The value of the `Feedback-Type` field from the<br>feedback report received from the ISP. This contains the type of<br>feedback.                                                                |
| `arrivalDate`           | The value of the `Arrival-Date` or<br>`Received-Date` field from the feedback report (in<br>ISO8601 format). This field may be absent in the report (and<br>therefore also absent in the JSON). |

The following is an example of a `complaint` object.

```
{
   "userAgent":"ExampleCorp Feedback Loop (V0.01)",
   "complainedRecipients":[
      {
         "emailAddress":"recipient1@example.com"
      }
   ],
   "complaintFeedbackType":"abuse",
   "arrivalDate":"2009-12-03T04:24:21.000-05:00",
   "timestamp":"2012-05-25T14:59:38.623Z",
   "feedbackId":"000001378603177f-18c07c78-fa81-4a58-9dd1-fedc3cb8f49a-000000"
}

```

### Complained recipients

The `complainedRecipients` field contains a list of recipients that may
have submitted the complaint. You should use this information to determine which
recipient submitted the complaint, and then immediately remove that recipient from
your mailing lists.

###### Important

Most ISPs remove the email address of the recipient who submitted the
complaint from their complaint notification. For this reason, this list contains
information about recipients who might have sent the complaint, based on the
recipients of the original message and the ISP from which we received the
complaint. SES performs a lookup against the original message to
determine this recipient list.

JSON objects in this list contain the following field.

| Field name     | Description                         |
| -------------- | ----------------------------------- |
| `emailAddress` | The email address of the recipient. |

The following is an example of a complained recipient object.

```
{ "emailAddress": "recipient1@example.com" }
```

###### Note

Because of this behavior, you can be more certain that you know which email
address complained about your message if you limit your sending to one message
per recipient (rather than sending one message with 30 different email addresses
in the bcc line).

#### Complaint types

You may see the following complaint types in the
`complaintFeedbackType` field as assigned by the reporting ISP,
according to the [Internet Assigned Numbers Authority website](http://www.iana.org/assignments/marf-parameters/marf-parameters.xml#marf-parameters-2 "http://www.iana.org/assignments/marf-parameters/marf-parameters.xml#marf-parameters-2"):

- `abuse`—Indicates unsolicited email or some other
  kind of email abuse.
- `auth-failure`—Email authentication failure
  report.
- `fraud`—Indicates some kind of fraud or phishing
  activity.
- `not-spam`—Indicates that the entity providing the
  report does not consider the message to be spam. This may be used to
  correct a message that was incorrectly tagged or categorized as
  spam.
- `other`—Indicates any other feedback that does not
  fit into other registered types.
- `virus`—Reports that a virus is found in the
  originating message.

## Delivery object

The JSON object that contains information about deliveries always has the following
fields.

| Field name             | Description                                                                                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `timestamp`            | The time SES delivered the email to the recipient's mail<br>server (in ISO8601 format).                                                                           |
| `processingTimeMillis` | The time in milliseconds between when SES accepted the<br>request from the sender to passing the message to the recipient's<br>mail server.                       |
| `recipients`           | A list of the intended recipients of the email to which the<br>delivery notification applies.                                                                     |
| `smtpResponse`         | The SMTP response message of the remote ISP that accepted the<br>email from SES. This message varies by email, by receiving<br>mail server, and by receiving ISP. |
| `reportingMTA`         | The hostname of the SES mail server that sent the<br>mail.                                                                                                        |
| `remoteMtaIp`          | The IP address of the MTA to which SES delivered the<br>email.                                                                                                    |

The following is an example of a `delivery` object.

```
{
   "timestamp":"2014-05-28T22:41:01.184Z",
   "processingTimeMillis":546,
   "recipients":["success@simulator.amazonses.com"],
   "smtpResponse":"250 ok:  Message 64111812 accepted",
   "reportingMTA":"a8-70.smtp-out.amazonses.com",
   "remoteMtaIp":"127.0.2.0"
}

```
