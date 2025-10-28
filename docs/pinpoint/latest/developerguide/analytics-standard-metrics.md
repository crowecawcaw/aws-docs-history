**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Standard metrics that apply to Amazon Pinpoint projects, campaigns, and journeys

You can use Amazon Pinpoint Analytics APIs to query analytics data for a subset of standard metrics
that apply to Amazon Pinpoint projects, campaigns, and journeys. These metrics, also referred to as a
_key performance indicators (KPIs)_, are measurable values that can help you
monitor and assess the performance of projects, campaigns, and journeys.

Amazon Pinpoint provides programmatic access to analytics data for several types of standard
metrics:

- **Application metrics** – These metrics provide insight
  into trends for all the campaigns and transactional messages that are associated with a project,
  also referred to as an _application_. For example, you can use an application
  metric to get a breakdown of the number of messages that were opened by recipients for each
  campaign that's associated with a project.
- **Campaign metrics** – These metrics provide insight
  into the performance of individual campaigns. For example, you can use a campaign metric to
  determine how many endpoints a campaign message was sent to or how many of those messages were
  delivered to endpoints.
- **Journey engagement metrics** – These metrics provide
  insight into the performance of individual journeys. For example, you can use a journey
  engagement metric to get a breakdown of the number of messages that were opened by participants
  in each activity of a journey.
- **Journey execution metrics** – These metrics provide
  insight into participation trends for individual journeys. For example, you can use a journey
  execution metric to determine how many participants started a journey.
- **Journey activity execution metrics** – These metrics
  provide insight into participation trends for individual activities in a journey. For example,
  you can use a journey activity execution metric to determine how many participants started an
  activity and how many participants completed each path in an activity.
  The topics in this section list and describe the individual metrics that you can query for
  each type of metric.

###### Topics

- [Amazon Pinpoint application metrics for campaigns](application-metrics-campaigns.md "application-metrics-campaigns.md")
- [Amazon Pinpoint application metrics for transactional email
  messages](application-metrics-txn-email.md "application-metrics-txn-email.md")
- [Amazon Pinpoint application metrics for transactional SMS
  messages](application-metrics-txn-sms.md "application-metrics-txn-sms.md")
- [Amazon Pinpoint campaign metrics](campaign-metrics.md "campaign-metrics.md")
- [Amazon Pinpoint journey engagement metrics](journey-metrics-engagement-email.md "journey-metrics-engagement-email.md")
- [Amazon Pinpoint journey execution metrics](journey-metrics-execution.md "journey-metrics-execution.md")
- [Amazon Pinpoint journey activity execution metrics](journey-metrics-activity-execution.md "journey-metrics-activity-execution.md")
- [Amazon Pinpoint journey and campaign execution
  metrics](journey-run-metrics-activity-execution.md "journey-run-metrics-activity-execution.md")
