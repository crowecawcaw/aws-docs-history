# Origination identities for Amazon SNS SMS

messages

###### Important

The Amazon SNS SMS Developer Guide has been updated. Amazon SNS has integrated with [AWS End User Messaging SMS](../../../sms-voice/latest/userguide/what-is-service.md "../../../sms-voice/latest/userguide/what-is-service.md") for the delivery of SMS messages. This guide contains the latest
information on how to create, configure, and manage your Amazon SNS SMS messages.

Origination identities for SMS messages are identifiers used to represent the sender of an
SMS message. You can identify yourself to your recipients using the following types of
originating identities:

**Origination numbers**

A numeric string that identifies an SMS message sender's phone number. There
are several types of origination numbers, including long codes (standard phone
numbers that typically have 10 or more digits), 10 digit long codes (10DLC),
toll free numbers (TFN) and short codes (phone numbers that contain between four
and seven digits).

Support for origination numbers is not available in countries where local laws
require the use of sender IDs instead of origination numbers. When you send an
SMS message using an origination number, the recipient's device shows the
origination number as the sender's phone number. You can specify different
origination numbers by use case.

For additional information, see [Phone numbers](../../../sms-voice/latest/userguide/phone-numbers.md "../../../sms-voice/latest/userguide/phone-numbers.md") in
the _AWS End User Messaging SMS User Guide_.

###### Tip

To view a list of all existing origination numbers in your AWS account,
in the navigation pane of the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home"), choose **Origination
numbers**.

**Sender IDs**

An alphabetic name that identifies the sender of an SMS message. When you send
an SMS message using a sender ID, and the recipient is in an area where sender
ID authentication is supported, your sender ID appears on the recipient’s
device instead of your phone number. A sender ID provides SMS recipients with
more information about the sender than a phone number, long code, or short code
provides.

Sender IDs are supported in several countries and regions around the world. In
some places, if you're a business that sends SMS messages to individual
customers, you must use a sender ID that's pre-registered with a regulatory
agency or industry group. For a complete list of countries and regions that
support or require sender IDs, see [Supported
countries and regions for SMS messaging with AWS End User Messaging SMS](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") in the
_AWS End User Messaging SMS User Guide_.

There's no additional charge for using sender IDs. However, support and
requirements for sender ID authentication varies by country. Several major
markets (including Canada, China, and the United States) don't support using
sender IDs. Some areas require that companies who send SMS messages to
individual customers must use a sender ID that's pre-registered with a
regulatory agency or industry group.

For additional information, see [Sender IDs](../../../sms-voice/latest/userguide/sender-id.md "../../../sms-voice/latest/userguide/sender-id.md") in the
_AWS End User Messaging SMS User Guide_.
