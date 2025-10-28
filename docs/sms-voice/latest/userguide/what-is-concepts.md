# AWS End User Messaging SMS concepts

This section describes key concepts and defines terminology specific to AWS End User Messaging SMS.

###### Configuration set

Configuration sets are sets of rules that are applied when you send a
message. For example, a configuration set can specify a destination for
events related to a message. When SMS events occur (such as delivery or
failure events), they are routed to the destination associated with the
configuration set that you specified when you sent the message.

###### Event destination

An event destination is a location (such as a Amazon CloudWatch Logs Group, a Amazon Data Firehose
stream, or an Amazon Simple Notification Service topic) that SMS and voice events are sent to. To use
event destinations, you first create the destination, and then associate it
with a configuration set. When you send a message, your call to the API can
include a reference to a configuration set.

###### Keywords

A keyword is a specific word or phrase that a customer can send to your
number to elicit a response, such as an informational message, opting-in to receive more messages,
a special offer and other promotional and transactional messages. When your number receives a
message that begins with a keyword, AWS End User Messaging SMS responds with a customizable message.

###### Opt-out list

A list of destination identities that should not have messages sent to
them. Destination identities are automatically added to the opt-out list if
they reply to your origination number with the keyword STOP. If you attempt
to send a message to a destination number that is on an opt-out list, and
the opt-out list is associated with the pool used to send the message, AWS End User Messaging SMS
doesn't attempt to send the message. If you enable the self-managed opt-out feature for a phone number,
then your recipients aren't automatically opted out when they reply to
your messages with the keyword STOP.

###### Originator

An originator refers to either a phone number or sender ID.

###### Origination phone number

See phone number.

###### Originator sender ID

See sender ID. Also called originator ID, an alphanumeric string that identifies the
sender.

###### Phone number

Also called originator number, a numeric string of numbers that identifies the sender.
This can be a long code, short code, toll-free number (TFN), or 10 digit long code
(10DLC). For more information, see [Choosing an origination identity](phone-number-types.md "phone-number-types.md").

###### Phone pool

A collection of phone numbers and sender IDs that share the same settings that you can
use to send messages. When you send messages through a phone pool, it chooses an
appropriate origination identity to send the message as. If an origination identity in
the phone pool fails, the phone pool will fail over to another origination identity if
it is in the same phone pool.

###### Registered phone number

Some countries require you to register your company's identity before you can purchase
phone numbers or sender IDs. They also require a review of the messages that you send to
recipients in their country. Registrations are processed by external third parties, so
the amount of time to process a registration varies by phone number type and country.
After all required registrations are complete, the status of your phone numbers changes
to **Active** and is available for use. For more
information about which countries require registration, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").

###### Simulator phone number

A simulator phone number behaves as an origination phone number and verified destination phone number. Simulator phone numbers do not require registration.

###### Sender ID

Also called originator ID, an alphanumeric string that identifies the sender. For more
information, see [Choosing an origination identity](phone-number-types.md "phone-number-types.md")

###### Verified phone number/Verified destination phone number

See phone number. When your account is in Sandbox you can only send SMS messages to
phone numbers that have gone through the verification process. The phone number receives
an SMS messaging with a verification code. The received code must be entered into the console to complete the process.
