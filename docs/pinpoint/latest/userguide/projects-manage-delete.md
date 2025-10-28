**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Deleting a project

If you want to remove a project from Amazon Pinpoint completely, you can delete the project by
using the Amazon Pinpoint console.

###### Warning

If you delete a project, Amazon Pinpoint deletes all project-specific settings, campaigns,
journeys, and other information for the project. The information can't be
recovered.

When you delete a project, Amazon Pinpoint deletes all project-specific settings for the push
notification and two-way SMS messaging channels, and all segments, campaigns, journeys,
and project-specific analytics data that's stored in Amazon Pinpoint, such as the
following:

- Segments – All segment settings and data. For dynamic segments, this
  includes segment groups and filters that you defined. For imported segments,
  this includes endpoints, user IDs, and other data that you imported, and any
  filters that you applied.
- Campaigns – All messages, message treatments and variables, analytics
  data, schedules, and other settings.
- Journeys – All activities, analytics data, schedules, and other
  settings.
- Analytics – Data for all engagement metrics, such as the number of
  messages sent and delivered for campaigns and journeys, and all journey
  execution metrics. For mobile and web apps, all event data that wasn't streamed
  to another AWS service such as Amazon Kinesis, all funnels, and data for application
  usage, revenue, and demographic metrics. Before you delete a project, we
  recommend that you export this data to another location. For more information,
  see [Exporting dashboards](analytics-charts.md#analytics-exporting "analytics-charts.md#analytics-exporting").
  Note that account-level settings and data for your Amazon Pinpoint account and your
  AWS account aren't deleted. This includes:

- Message templates.
- Production access and sending quotas for channels.
- Dedicated phone numbers for sending SMS and voice messages, and for receiving
  SMS messages.
- Verified identities for sending email and SMS messages.
- SMS information such as short codes, long codes, keywords, and registered
  sender IDs for sending SMS messages.
- SMTP credentials and other settings for sending email by using the Amazon Pinpoint SMTP
  interface.
- Configuration settings for connecting to and using machine learning
  models.
  In addition, data that's stored in other AWS services isn't deleted. This includes
  event data that you streamed to other AWS services such as Amazon Kinesis, files that you
  imported from an Amazon Simple Storage Service (Amazon S3) bucket to define a segment, and any Amazon Pinpoint metrics and
  spending alarms that you configured in Amazon CloudWatch.

###### To delete a project

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to delete.
3. In the navigation pane, under **Settings**, choose
   **General settings**.
4. Choose **Delete project**.
5. Enter the name of the project that you want to delete, and then choose
   **Ok**.
