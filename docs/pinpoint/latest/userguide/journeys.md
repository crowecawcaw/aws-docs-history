**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint journeys

In Amazon Pinpoint, a _journey_ is a customized, multi-step engagement
experience. When you create a journey, you start by choosing a segment that defines which
customers will participate in the journey. After that, you add the activities that customers
pass through on their journeys. Activities can include sending messages or splitting
customers into groups based on their attributes or behaviors.

There are several different types of journey activities, each with its own specific
purpose. For example, you can add a **Send email** activity to your
journey. When a customer arrives on this type of activity, they receive an email message.
Another type of journey activity is the **Multivariate split** activity.
When customers arrive on this type of activity, they are separated into multiple paths based
on their segment membership or their interactions with previous journey activities. You can
learn more about journey activities in [Take a tour of journeys](journeys-tour.md "journeys-tour.md").

This chapter contains conceptual information about journeys in Amazon Pinpoint. It also contains
information about creating, managing, testing, and publishing your journeys.

###### Topics in this section:

- [Take a tour of journeys](journeys-tour.md "journeys-tour.md")
- [Create a journey](journeys-create.md "journeys-create.md")
- [Set up the journey entry activity](journeys-entry-activity.md "journeys-entry-activity.md")
- [Add activities to the journey](journeys-add-activities.md "journeys-add-activities.md")
- [Review and test a journey](journeys-review-test.md "journeys-review-test.md")
- [Publish a journey](journeys-publish.md "journeys-publish.md")
- [Pause, resume, or stop a journey](journeys-pause-stop.md "journeys-pause-stop.md")
- [View journey metrics](journeys-metrics.md "journeys-metrics.md")
- [Tips and best practices for journeys](journeys-best-practices.md "journeys-best-practices.md")
- [Troubleshooting journeys](journeys-troubleshooting.md "journeys-troubleshooting.md")
