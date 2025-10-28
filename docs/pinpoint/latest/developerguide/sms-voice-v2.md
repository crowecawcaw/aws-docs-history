**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Use the AWS End User Messaging SMS and Voice API, version 2

Amazon Pinpoint includes an API—called the SMS and Voice API, version 2—that was designed for
sending SMS and voice messages. While the Amazon Pinpoint API is focused on sending messages through
scheduled and event-driven campaigns and journeys, the SMS and Voice API provides new
features and capabilities for sending SMS and voice messages directly to individual
recipients. You can use SMS and Voice API independently of the Amazon Pinpoint campaign and journey
features, or you can use both at the same time to accommodate different use cases. If you
already use Amazon Pinpoint to send SMS or voice messages, your account is already configured to use
this API.

This API is a good solution for users who have a multi-tenant architecture, such as
Independent Software Vendors (ISVs). This API makes it easier to ensure that event data,
origination phone numbers, and opt-out lists are separated for different tenants.

When you use the SMS and Voice API, we recommend that you set up configuration sets and
event destinations. The SMS and Voice API doesn't automatically emit event data for the
messages that you send. Setting up event destinations ensures that you capture important
event data, such as message delivery and failure events.

Version 2 of this API was preceded by Version 1. If you currently use Version 1 of this
API, it will continue to be available and you can continue to use it. If you
migrate to Version 2, you will gain additional features, such as the ability to create pools
of phone numbers, request new phone numbers programmatically, and enable or disable certain
capabilities of phone numbers.

###### Note

Some tasks can only be completed by using the Amazon Pinpoint console.
For example, [verifying a
phone number to use while your account is in the SMS sandbox](../../../sms-voice/latest/userguide/sandbox.md#channels-sms-verify-number "../../../sms-voice/latest/userguide/sandbox.md#channels-sms-verify-number") and [registering to use 10DLC](../../../sms-voice/latest/userguide/registrations-10dlc.md "../../../sms-voice/latest/userguide/registrations-10dlc.md").

For more information about the Amazon Pinpoint SMS and Voice version 2 API, see the [SMS and Voice, version 2 API
Reference](../apireference_smsvoicev2/Welcome.md "../apireference_smsvoicev2/Welcome.md"). For information about how to create,
configure, and manage your AWS End User Messaging SMS and voice resources, see the [_AWS End User Messaging SMS User Guide_](../../../sms-voice/latest/userguide/what-is-service.md "../../../sms-voice/latest/userguide/what-is-service.md")
