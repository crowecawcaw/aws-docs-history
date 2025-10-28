**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Create Amazon Pinpoint campaigns programmatically

To help increase engagement between your app and its users, use Amazon Pinpoint to create and
manage push notification campaigns that reach out to particular segments of
users.

For example, your campaign might invite users back to your app who haven’t run it
recently or offer special promotions to users who haven’t purchased recently.

A campaign sends a tailored message to a user segment that you specify. The campaign
can send the message to all users in the segment, or you can allocate a holdout,
which is a percentage of users who receive no messages.

You can set the campaign schedule to send the message once or at a recurring
frequency, such as once a week. To prevent users from receiving the message at
inconvenient times, the schedule can include a quiet time during which no messages
are sent.

To experiment with alternative campaign strategies, set up your campaign as an A/B
test. An A/B test includes two or more treatments of the message or schedule.
Treatments are variations of your message or schedule. As your users respond to the
campaign, you can view campaign analytics to compare the effectiveness of each
treatment.

For more information, see [Campaigns](../apireference/apps-application-id-campaigns.md "../apireference/apps-application-id-campaigns.md") in the _Amazon Pinpoint REST API Guide_ or [Campaigns](../userguide/campaigns.md "../userguide/campaigns.md") in the _Amazon Pinpoint User Guide_ .
