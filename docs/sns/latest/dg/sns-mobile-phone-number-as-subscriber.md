# Mobile text messaging with

Amazon SNS

###### Important

The Amazon SNS SMS Developer Guide has been updated. Amazon SNS has integrated with [AWS End User Messaging SMS](../../../sms-voice/latest/userguide/what-is-service.md "../../../sms-voice/latest/userguide/what-is-service.md") for the delivery of SMS messages. This guide contains the latest
information on how to create, configure, and manage your Amazon SNS SMS messages.

Amazon SNS mobile text messaging (SMS) is designed to facilitate message delivery to various
platforms, such as web, mobile, and business applications that support SMS. Users can send
messages to one or multiple phone numbers by subscribing them to a topic, simplifying the
distribution process.

Amazon SNS messages are delivered by AWS End User Messaging SMS, which ensures reliable message transmission.
Within Amazon SNS APIs, you can set various properties such as message types (promotional or
transactional), [monthly spending limits](sms_preferences.md#sms_preferences_console "sms_preferences.md#sms_preferences_console"),
[opt-out lists](sms_manage.md#sms_manage_optout "sms_manage.md#sms_manage_optout"), and [message delivery optimization](sms_preferences.md#sms_preferences_console "sms_preferences.md#sms_preferences_console").

AWS End User Messaging SMS handles the transmission of messages to the destination phone number through its
global SMS supply network. It manages the routing, delivery status, and any required
compliance with regional regulations. To access additional SMS features such as granular
permissions, phone pools, configurations sets, SMS simulator, and country rule, see the
[AWS End User Messaging SMS User Guide](../../../sms-voice/latest/userguide/configurations.md "../../../sms-voice/latest/userguide/configurations.md").

![An illustration of how Amazon SNS integrates with AWS End User Messaging SMS to deliver mobile text messages reliably. Messages can be sent directly to individual recipients or distributed to groups through Amazon SNS topics. AWS End User Messaging SMS handles message routing, delivery, and compliance across its global network, ensuring scalability and reliability. This setup also allows for configuring message preferences, managing spending limits, and tracking delivery status to optimize AWS SMS messaging.](images/sns-sms-end-user-messaging.png)
The following key features help you send Amazon SNS SMS messages that are scalable and easily
extensible:

**[Customize message
preferences](sms_preferences.md "sms_preferences.md")**

Customize SMS deliveries for your AWS account by setting up SMS preferences
based on your budget and use case. For example, you can choose whether your
messages prioritize cost efficiency or reliable delivery.

**[Set
spending quotas](channels-sms-awssupport-spend-threshold.md "channels-sms-awssupport-spend-threshold.md")**

Tailor your SMS deliveries by specifying spending quotas or for individual
message deliveries and monthly spending quotas for your AWS account. Where
required by local laws and regulations (such as the US and Canada), SMS
recipients can [opt-out](sms_manage.md#sms_manage_optout "sms_manage.md#sms_manage_optout"), which means
that they choose to stop receiving SMS messages from your AWS account. After a
recipient opts-out of receiving messages, you can, with limitations, opt-in the
phone number again so that you can resume sending messages.

**[Send SMS
messages globally](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md")**

Amazon SNS supports SMS messaging in multiple regions, allowing you to send
messages to over 240 countries and regions.

## How does Amazon SNS deliver my SMS

messages?

When you request Amazon SNS to send SMS on your behalf, the messages are dispatched using
AWS End User Messaging SMS. The integration between Amazon SNS and AWS End User Messaging SMS offers the following
benefits:

**[IAM policies](sns-mobile-phone-number-getting-started.md#sns-mobile-phone-number-prerequisites "sns-mobile-phone-number-getting-started.md#sns-mobile-phone-number-prerequisites")**

You can leverage IAM and resource policies to control and distribute
access to your SMS resources across other AWS services and
regions.

**[AWS End User Messaging SMS
configurations](../../../sms-voice/latest/userguide/configurations.md "../../../sms-voice/latest/userguide/configurations.md")**

All origination ID related configurations (creation, configuration
updating, provisioning new origination IDs, changing registration templates)
use AWS End User Messaging SMS.

**[AWS End User Messaging SMS
billing](https://aws.amazon.com/sns/sms-pricing/ "https://aws.amazon.com/sns/sms-pricing/")**

All SMS billing is done though AWS End User Messaging SMS. You can consolidate your AWS spend for your SMS workloads, while procuring and managing
your SMS resources in one central location.
