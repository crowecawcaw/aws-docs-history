# Sender IDs in AWS End User Messaging SMS

A sender ID is an alphanumeric name that identifies the sender of an SMS message. When
you send an SMS message using a sender ID, and the recipient is in an area where sender
ID authentication is supported, your sender ID appears on the recipient's device instead
of a phone number. A sender ID provides SMS recipients with more information about the
sender than a phone number or short code provides. For example, a fictitious company Example Corp could use the sender ID `EXAMPLECO`

Sender IDs are supported in many countries and regions around the world. In some
places, if you're a business that sends SMS messages to individual customers, you must
use a sender ID that's pre-registered with a regulatory agency or industry group. For a
complete list of countries and regions that support or require sender IDs, see [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md "phone-numbers-sms-support-by-country.md").

**Advantages**

Sender IDs provide the recipient with more information about the message sender. It's
easier to establish your brand identity by using a sender ID than by using a short or
long code. There's no additional charge for using a sender ID.

**Disadvantages**

Support and requirements for sender ID authentication aren't consistent across all
countries or regions. Several major markets (including Canada, China, and the United
States) don't support sender ID. In some areas, you must have your sender IDs
pre-approved by a regulatory agency before you can use them.

###### Topics

- [Sender ID country capabilities and limitations](#sender-id-limitations "#sender-id-limitations")
- [Registered and dynamic sender IDs](#sender-id-types "#sender-id-types")
- [Considerations for a sender ID](#sender-id-considerations "#sender-id-considerations")
- [Sender ID display name rules](#channels-sms-countries-sender-id "#channels-sms-countries-sender-id")
- [Request a sender ID](sender-id-request.md "sender-id-request.md")
- [Request a sender ID through Support](sender-id-awssupport-open.md "sender-id-awssupport-open.md")
- [Release a sender ID](sender-id-release.md "sender-id-release.md")
- [Manage tags a for sender ID](sender-id-tags-add.md "sender-id-tags-add.md")
- [List shared sender IDs](sender-id-shared.md "sender-id-shared.md")

## Sender ID country capabilities and limitations in AWS End User Messaging SMS

For more information on which countries support sender IDs see the **Supports Sender IDs** column in [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").

For the rules of which sender ID is displayed when you send SMS messages to countries where sender IDs are supported, compared to those where Sender IDs aren't supported, see [Sender ID display name rules](#channels-sms-countries-sender-id "#channels-sms-countries-sender-id").

## What are registered and dynamic sender IDs in AWS End User Messaging SMS

**Registered sender ID** – A registered sender ID is registered with a regulatory agency or industry group. For a complete list of countries and regions that
support or require sender IDs, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").

**Dynamic sender ID** – A dynamic sender ID does not have to be
registered with a regulatory agency or industry group. Registration requirements can change
quickly and it is recommended that you complete any optional registration for dynamic sender
IDs. For a complete list of countries and regions that
support or optionally have sender ID registration, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md").

## Considerations for a sender ID

When you are creating a Sender ID you should consider the following:

- Choose a Sender ID that matches your company branding and SMS service or use case
- Numeric-only Sender IDs are not supported
- AWS End User Messaging SMS sender ID supported characters (some countries might override these):
  - No special characters except for dashes (-)
  - No spaces
  - Valid characters: a-z, A-Z, 0-9
  - Minimum of 3 characters
  - Maximum of 11 characters

- If the country you're sending to requires registration you must submit a registration for each AWS Region you plan on sending from

## Sender ID display name rules in AWS End User Messaging SMS

The following table explains which Sender ID is displayed when you send SMS messages to
countries where Sender IDs are supported,
compared to those where Sender IDs aren't supported.

| If the recipient is located...                                                                                                | And your SMS message...                                                                                                                                                                                            | The message is sent from... |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- |
| In a country or region where Sender ID registration is required                                                               | Specifies a Sender ID that has been registered                                                                                                                                                                     | The Sender ID.              |
| Doesn't specify a Sender ID, or specifies an unregistered sender ID                                                           | AWS End User Messaging SMS attempts to deliver the message with the Sender ID _NOTICE_. The message might not be received by the recipient based on the carrier requirements in the destination country or region. |                             | In a country or region where Sender IDs are supported but Sender ID registration isn't required                                                                                                                                                                                                                                                 | Specifies a Sender ID                                                                                                                                                          | The Sender ID. |
| Doesn't specify a Sender ID, but the account includes a dedicated phone number for the SMS channel in the destination country | The dedicated phone number.                                                                                                                                                                                        |                             | Doesn't specify a Sender ID, and the account doesn't include a dedicated phone number for the SMS channel in the destination country                                                                                                                                                                                                            | <br>• A random long or short code in countries and regions where Sender IDs aren't supported. <br>• The word _NOTICE_ in countries and regions where Sender IDs are supported. |
|                                                                                                                               | In a country or region where Sender IDs aren't supported                                                                                                                                                           | Specifies a Sender ID       | Varies depending on the destination country. In some countries, your message is sent using a random long code. In other countries, your message is sent using a shared short code. In the United States, you can only send messages using dedicated phone numbers. If you don't have a dedicated US phone number, your message isn't delivered. |
| Doesn't specify a Sender ID                                                                                                   | Varies—see above.                                                                                                                                                                                                  |
