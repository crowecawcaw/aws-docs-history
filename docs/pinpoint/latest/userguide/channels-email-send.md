**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Sending email in Amazon Pinpoint

Before you can use Amazon Pinpoint to send an email, complete the procedures in [Setting up the Amazon Pinpoint email channel](channels-email-setup.md "channels-email-setup.md").

There are several types of email that you can send using Amazon Pinpoint: campaign-based email,
journey-based email, and transactional email. _Campaign-based emails_ are
messages that are sent either one time or on a recurring schedule, and that target customers
based on their attributes. _Journey-based emails_ are
messages that are sent when participants in a journey arrive at an email activity as part of
a larger workflow. _Transactional emails_ are sent one time only, and are
typically sent in response to another action occurring. For example, you can use
transactional messages to send an email when a customer chooses the "Forgot my password"
link in your app, or to send a confirmation when a customer places an order on your
site.

In Amazon Pinpoint, you typically use the web-based management console to send campaign-based emails
and journey-based emails, whereas transactional emails are usually sent from applications
that use an AWS SDK or call the Amazon Pinpoint API directly.

When you send a campaign-based email, you first create a [segment](segments-building.md "segments-building.md"). A segment is a group of recipients for the campaign. Next, you create a
campaign. In Amazon Pinpoint, a campaign consists of one or more target segments, a message, and a
delivery schedule for that message. To learn about creating campaigns, see [Amazon Pinpoint campaigns](campaigns.md "campaigns.md").

When you send a journey-based email, you also start by creating a [segment](segments-building.md "segments-building.md"). A segment is a group of participants in the
journey. Next, you create an email template for each message that you want activities in the
journey to send. Then, you create the journey. To learn about creating journeys, see [Amazon Pinpoint journeys](journeys.md "journeys.md").

To send a transactional email, you can use the `SendMessage` operation of the
Amazon Pinpoint API. To learn more about using the Amazon Pinpoint API, see the [Amazon Pinpoint API Reference](../apireference.md "../apireference.md"). For code
examples that show how to send email using various AWS SDKs, see [Send transactional email messages](../developerguide/send-messages-email.md "../developerguide/send-messages-email.md") in
the _Amazon Pinpoint Developer Guide_.
