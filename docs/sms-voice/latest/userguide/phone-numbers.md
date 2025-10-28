# Phone numbers in AWS End User Messaging SMS

A phone number is an identity that your recipients see on their devices when you send them an
SMS or MMS message. There are several types of identities, including long codes (standard phone
numbers that typically have 10 or more digits), 10 digit long codes (10DLC), toll free numbers
(TFN) and short codes (phone numbers that contain between four and seven digits).

Phone numbers are resources that are unique to each AWS Region, so they can't be shared
across AWS Regions. You can grant cross AWS account and AWS Region access to phone numbers.
Dedicated phone numbers are country-specific. You can't request a dedicated phone number for one
country but then use it as an identity for another country.

For example if your use case requires you to send message to the United States and Canada you
should provision origination identities for both of those countries. You do not need to provision
the origination identities in AWS Regions that are local to that country. You could provision
both origination identities in US West (Oregon). As another example if your use case requires
you to send message to the United States and India you might want to provision the origination
identities in AWS Regions that are geographically close to their message destinations to reduce
latency. For more information see the [Amazon Pinpoint Resilient Architecture Guide](../../../pinpoint/latest/archguide/welcome.md "../../../pinpoint/latest/archguide/welcome.md").

There are several guidelines to consider when you're deciding what type of origination
identity to use:

- Sender IDs are a great option for one-way use cases. However, they're not
  available in all countries.
- Short codes are a great option for two-way use cases. If you have to choose
  between using a short code or a long code, you should choose the short
  code.
- In some countries (such as India and Saudi Arabia), long codes can be used to
  receive incoming messages, but can't be used to send outgoing messages. You can
  use these inbound-only long codes to provide your recipients with a way to opt
  out of messages that you send using a Sender ID.
- In some countries, we maintain a pool of shared routes. If you send messages to recipients
  in a particular country, but you don't have a dedicated origination identity in that country, we
  make an effort to deliver your message using one of these shared identities. Shared identities
  are unavailable in some countries, including the United States and China.
- The mobile industry changes rapidly. In many countries, there is a trend toward increased
  regulation of commercial SMS messages. Carriers can, with little or no warning, decide to
  disallow messages sent from shared origination identities. If this happens, we will attempt to
  tell you about these changes with as much advance warning as possible. However, carriers
  generally provide us with little advance notice of these changes. For these reasons, dedicated
  origination identities are always preferred to shared ones.

###### Topics

- [SMS and MMS country capabilities and limitations](phone-numbers-sms-support-by-country.md "phone-numbers-sms-support-by-country.md")
- [Supported countries and regions for voice](phone-numbers-voice-support-by-country.md "phone-numbers-voice-support-by-country.md")
- [Request a phone number](phone-numbers-request.md "phone-numbers-request.md")
- [View a phone number status and capabilities](phone-numbers-status.md "phone-numbers-status.md")
- [Change a phone number's capabilities](phone-numbers-change-capabilitiy.md "phone-numbers-change-capabilitiy.md")
- [Release a phone number](phone-numbers-delete.md "phone-numbers-delete.md")
- [Change a phone number's opt-out list](phone-numbers-manage-opt-out-list.md "phone-numbers-manage-opt-out-list.md")
- [Using deletion protection](phone-numbers-deletion-protection.md "phone-numbers-deletion-protection.md")
- [Manage tags a for phone number](phone-numbers-tags.md "phone-numbers-tags.md")
- [List shared phone numbers](phone-numbers-shared.md "phone-numbers-shared.md")
