**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint campaigns

A _campaign_ is a messaging initiative that engages a specific audience
[segment](segments.md "segments.md"). A campaign sends tailored messages according to
a schedule that you define. You can use the console to create a campaign that sends messages
through any single channel that is supported by Amazon Pinpoint: mobile push, in-app, email, SMS, or
custom channels.

For example, to help increase engagement between your mobile app and its users, you could
use Amazon Pinpoint to create and manage push notification campaigns that reach out to users of that
app. Your campaign might invite users back to your app who haven't run it recently or offer
special promotions to users who haven't purchased recently.

Your campaign can send a message to all users in a segment, or you can allocate a holdout,
which is a percentage of users who receive no messages. The segment can be one that you
created on the **Segments** page or one that you define while you create
the campaign.

You can set the campaign's schedule to send the message once or at a recurring frequency,
such as once per week. You can also set up your campaign to send messages when specific
events occur. For example, you can send a campaign when a user creates a new account, or
when a customer adds an item to their shopping cart, but doesn't complete their purchase. To
prevent users from receiving your messages at inconvenient times, you can also configure
your campaigns so that they don't send messages during specific quiet hours.

To experiment with alternative campaign strategies, set up your campaign as an _A/B test_. An _A/B test_
includes two or more treatments of the message or schedule. Treatments are variations of
your message or schedule. As your users respond to the campaign, you can view campaign
analytics to compare the effectiveness of each treatment.

If you want to send a one-time message without engaging a user segment or defining a
schedule, you can [send a direct message](messages.md "messages.md") instead of creating
a campaign.

###### Topics

- [Create a campaign](campaigns-begin.md "campaigns-begin.md")
- [Specify the audience for the campaign](campaigns-segment.md "campaigns-segment.md")
- [Configure the message](campaigns-message.md "campaigns-message.md")
- [Schedule the campaign](campaigns-schedule.md "campaigns-schedule.md")
- [Review and launch the campaign](campaigns-review.md "campaigns-review.md")
- [Managing campaigns](campaigns-managing.md "campaigns-managing.md")
- [Troubleshooting campaigns](campaigns-troubleshooting.md "campaigns-troubleshooting.md")
