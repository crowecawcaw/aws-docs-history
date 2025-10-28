**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Delete your Amazon Pinpoint project and remove sensitive personal data

Depending on how you use it, Amazon Pinpoint might store certain data that could be considered
personal. For example, an endpoint in Amazon Pinpoint contains contact information for an end user,
such as that person's email address or mobile phone number.

You can use the console or the Amazon Pinpoint API to permanently delete personal data. This topic
includes procedures for deleting various types of data that could be considered
personal.

You can also close your AWS account completely. For more information, see
[Close an AWS account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md") in the AWS Account Management Reference Guide.

## Delete all Amazon Pinpoint project data

It's possible to permanently delete all the data that you've stored for an Amazon Pinpoint
project. You can do this by deleting the project.

###### Warning

If you delete a project, Amazon Pinpoint deletes all project-specific settings and data for
the project. The information can't be recovered.

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
  execution metrics. For mobile and web apps, all event data that wasn’t streamed
  to another AWS service such as Amazon Kinesis, all funnels, and data for application
  usage, revenue, and demographic metrics. Before you delete a project, we
  recommend that you export this data to another location.

You can delete a project by using the Amazon Pinpoint console. To learn more, see [Deleting a
Project](../userguide/settings-general.md#settings-general-delete-project "../userguide/settings-general.md#settings-general-delete-project") in the _Amazon Pinpoint User Guide_. You can
also delete a project programmatically by using the [App](../apireference/apps-application-id.md "../apireference/apps-application-id.md") resource of the Amazon Pinpoint
API.
