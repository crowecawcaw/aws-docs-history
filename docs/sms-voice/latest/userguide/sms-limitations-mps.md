# What are the Message Parts per Second (MPS)

limits

SMS messages are delivered in 140-byte sections known as _message
parts_. Messages that are very long, or that contain many multi-byte
characters, are split into several message parts. These messages are usually re-assembled on
the recipient's device, appearing as a single long message rather than several small ones.
For more information about SMS character limits, see [SMS character limits](sms-limitations-character.md "sms-limitations-character.md").

For this reason, SMS throughput limits, also referred to as throttling, are measured in
_Message Parts per Second_ (MPS)—that is, the maximum number of
message parts that you can send in a second. Your MPS limit depends on the destination
country of your messages, and the type of phone number, known as the _origination
number_, that you use to send the message. For example, if you use a United
States short code to send messages to recipients in the US, you can send 100 MPS. However,
if you use a US toll-free number to send to US recipients, you are throttled to only send 3
MPS.

MMS message are delivered as a single _message part_ and are not broken
into multiple _message parts_. The maximum media file size can be up to
2MB for gif, jpeg, png, and 600KB in size for all other media file types and can contain up
to 1600 characters, from any character set, in the message body, see [MMS file types, size and character limits](mms-limitations-character.md "mms-limitations-character.md"). If you
are sending SMS messages that have more than 3 _message parts_ you should
consider sending an MMS message instead. For example if you send an SMS message with 481 GSM
03.38 characters then the SMS message will be split into 4 _message
parts_. You are billed for each of those _message parts_.
If you send the 481 GSM 03.38 characters in the MMS message body you are only billed for one
_message parts_. Also only sending 1 MMS _message
part_ instead of 4 SMS _message parts_ will increase your
message throughput. For more information on pricing, see [AWS End User Messaging
Pricing](https://aws.amazon.com/end-user-messaging/pricing/ "https://aws.amazon.com/end-user-messaging/pricing/").

The following sections describe the MPS for various types of origination numbers and for
various countries.

## Short codes

The following table shows general MPS limits for dedicated short codes.

| Geographic area                 | SMS MPS                      | MMS MPS |
| ------------------------------- | ---------------------------- | ------- |
| United States (US)              | 100 MPS                      | 40 MPS  |
| Canada (CA)                     | 100 MPS                      | 40 MPS  |
| All other countries and regions | Varies by country or region. | N/A     |

## Long codes

The following table shows general MPS limits for dedicated long codes.

| Geographic area                 | SMS MPS                                                                                                                                                                                                                                                                                                                                                                                                                                                                | MMS MPS |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| United States (US) (10DLC)      | Default:<br>1 MPS per 10DLC number. Higher limits require a separate MPS increase<br>request and are not automatically increased when you externally vet your<br>company or after your campaign is approved. Final eligible rates are<br>carrier-dependent based on brand score and campaign type. To submit a<br>limit increase for your 10DLC numbers to match 10DLC campaign<br>qualifications, see [Quotas for AWS End User Messaging SMS](quotas.md "quotas.md"). | 1 MPS   |
| Canada (CA)                     | 1 MPS                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 1 MPS   |
| All other countries and regions | 10 MPS                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | N/A     |

## Toll-free numbers

Toll-free numbers are currently only available in the United States. US toll-free
numbers support 3 MPS and require that you register the toll-free number. For more
information about registering a toll-free number, see [US toll-free number registration form](registrations-tfn-register.md "registrations-tfn-register.md").

| Geographic area    | SMS MPS | MMS MPS |
| ------------------ | ------- | ------- |
| United States (US) | 3 MPS   | 3 MPS   |

###### Important

If your throughput requirements exceed 3 MPS, you should use a 10DLC number or a
short code. If you purchase multiple toll-free numbers and attempt to distribute
your throughput across them, the mobile carriers are likely to identify this as
"snowshoeing" and filter all of your messages from their networks. For more
information about "snowshoeing", see [Prohibited message content](best-practices.md#best-practices-sms-message-content "best-practices.md#best-practices-sms-message-content")

## Sender IDs

The following table shows general MPS limits for sender IDs.

| Sender ID type                                                                                              | SMS MPS | MMS MPS |
| ----------------------------------------------------------------------------------------------------------- | ------- | ------- |
| Customer-defined using the AWS End User Messaging SMS API or from the AWS End User Messaging SMS<br>console | 10 MPS  | N/A     |

## Shared routes

The following table shows general MPS limits for shared routes.

| Sender ID type                      | SMS MPS | MMS MPS |
| ----------------------------------- | ------- | ------- |
| Shared routes/customer-owned number | 20 MPS  | N/A     |
