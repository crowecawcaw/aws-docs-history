

# Phone numbers
<a name="nx-features-phone-numbers"></a>

A phone number is an identity that your recipients see on their devices when you send them an SMS or MMS message. There are several types of identities, including long codes (standard phone numbers that typically have 10 or more digits), 10 digit long codes (10DLC), toll free numbers (TFN) and short codes (phone numbers that contain between four and seven digits).

Phone numbers are resources that are unique to each AWS Region, so they can't be shared across AWS Regions. You can grant cross AWS account and AWS Region access to phone numbers. Dedicated phone numbers are country-specific. You can't request a dedicated phone number for one country but then use it as an identity for another country.

For example if your use case requires you to send message to the United States and Canada you should provision origination identities for both of those countries. You do not need to provision the origination identities in AWS Regions that are local to that country. You could provision both origination identities in US West (Oregon). As another example if your use case requires you to send message to the United States and India you might want to provision the origination identities in AWS Regions that are geographically close to their message destinations to reduce latency. For more information see the [Amazon Pinpoint Resilient Architecture Guide](https://docs.aws.amazon.com/pinpoint/latest/archguide/welcome.html).

There are several guidelines to consider when you're deciding what type of origination identity to use:
+ Sender IDs are a great option for one-way use cases. However, they're not available in all countries.
+ Short codes are a great option for two-way use cases. If you have to choose between using a short code or a long code, you should choose the short code.
+ In some countries (such as India and Saudi Arabia), long codes can be used to receive incoming messages, but can't be used to send outgoing messages. You can use these inbound-only long codes to provide your recipients with a way to opt out of messages that you send using a Sender ID.
+ In some countries, we maintain a pool of shared routes. If you send messages to recipients in a particular country, but you don't have a dedicated origination identity in that country, we make an effort to deliver your message using one of these shared identities. Shared identities are unavailable in some countries, including the United States and China.
+ The mobile industry changes rapidly. In many countries, there is a trend toward increased regulation of commercial SMS messages. Carriers can, with little or no warning, decide to disallow messages sent from shared origination identities. If this happens, we will attempt to tell you about these changes with as much advance warning as possible. However, carriers generally provide us with little advance notice of these changes. For these reasons, dedicated origination identities are always preferred to shared ones.

You can add keyword responses to an individual phone number so that AWS End User Messaging replies automatically when a recipient texts a keyword. For more information, see [Keywords](nx-features-keywords.md). To stop sending messages to recipients who have opted out, associate the phone number with an opt-out list. For more information, see [Opt-out lists](nx-features-opt-out-list.md).

**Topics**
+ [Choosing a phone number type](nx-features-phone-numbers-types.md)
+ [Request a phone number](nx-features-phone-numbers-request.md)
+ [View a phone number status and capabilities](nx-features-phone-numbers-status.md)
+ [Change a phone number's capabilities](nx-features-phone-numbers-change-capabilities.md)
+ [Release a phone number](nx-features-phone-numbers-release.md)
+ [Using deletion protection](nx-features-phone-numbers-deletion-protection.md)
+ [Manage tags for a phone number](nx-features-phone-numbers-tags.md)
+ [Shared routes](nx-features-phone-numbers-shared-routes.md)
+ [List shared phone numbers](nx-features-phone-numbers-shared.md)