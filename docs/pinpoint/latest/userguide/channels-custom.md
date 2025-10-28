**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Custom channels in Amazon Pinpoint

You can extend the capabilities of Amazon Pinpoint by creating custom channels. You can use custom
channels to send messages to your customers through any service that has an
API—including third-party services. For example, you can use custom channels to send
messages through third-party services such as WhatsApp or Facebook Messenger.

###### Note

To communicate over WhatsApp we recommend using [AWS End User Messaging Social](../../../social-messaging/latest/userguide/what-is-service.md "../../../social-messaging/latest/userguide/what-is-service.md") as it provides access to WhatsApp's
messaging capabilities, enabling the creation of branded, interactive content with
images, videos, and buttons. For more information on getting started with AWS End User
Messaging Social, see [Getting started with AWS End User Messaging Social](../../../social-messaging/latest/userguide/getting-started.md "../../../social-messaging/latest/userguide/getting-started.md").

###### Note

Amazon Web Services isn't responsible for any third-party service that you use to send messages
with custom channels. Third-party services might be subject to additional terms. You
should review these terms before you send messages with custom channels.

You can configure your campaigns to send messages through custom channels by using the
Amazon Pinpoint console. For more information, see [Amazon Pinpoint campaigns](campaigns.md "campaigns.md").

## Setting up and managing custom

channels

You can create custom channels by using a webhook, or by calling a service's API
through an AWS Lambda function. For more information about creating custom channel
functions in Lambda, see [Creating custom
channels](../developerguide/channels-custom.md "../developerguide/channels-custom.md") in the _Amazon Pinpoint Developer Guide_.

Unlike other channels in Amazon Pinpoint, you don't have to enable the custom channels feature.
Custom channels are enabled by default in all Amazon Pinpoint projects. You don't have to request
production access to use custom channels.
