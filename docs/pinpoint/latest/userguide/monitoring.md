**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Monitoring Amazon Pinpoint with Amazon CloudWatch

You can use Amazon CloudWatch to collect, view, and analyze several important metrics related to
your Amazon Pinpoint account and projects. When you configure CloudWatch for Amazon Pinpoint, you gain insight into
the delivery of your Amazon Pinpoint campaigns, and the status of your endpoint registrations and
import jobs. You can also use CloudWatch to create alarms that notify you when certain metrics
exceed values that you define. For example, you can create an alarm that automatically sends
you an email if a certain number of campaign messages fail within a specific time
period.

For information about how to stream events and logs see [Streaming
Amazon Pinpoint events to Kinesis](../developerguide/event-streams.md "../developerguide/event-streams.md") in the [Amazon Pinpoint Developer Guide](../developerguide.md "../developerguide.md").

###### Topics in this chapter:

- [Amazon Pinpoint metrics that are exported to CloudWatch](monitoring-metrics.md "monitoring-metrics.md")
- [View Amazon Pinpoint metrics in CloudWatch](monitoring-view-metrics.md "monitoring-view-metrics.md")
- [Create CloudWatch alarms for Amazon Pinpoint metrics](monitoring-create-alarms.md "monitoring-create-alarms.md")
