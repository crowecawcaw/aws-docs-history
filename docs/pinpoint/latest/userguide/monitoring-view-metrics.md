**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# View Amazon Pinpoint metrics in CloudWatch

You can monitor metrics for Amazon Pinpoint by using the Amazon CloudWatch console or the Amazon CloudWatch API. The
following procedure explains how to view the metrics by using the CloudWatch console.

###### To view metrics by using the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. On the **All metrics** tab, choose
   **Pinpoint**.
4. Select the type of metric that you want to view.
5. Select a metric to add it to the chart.
   You can also use CloudWatch to create alarms that send you notifications about changes in these
   metrics. For more information, see [Create CloudWatch alarms for Amazon Pinpoint metrics](monitoring-create-alarms.md "monitoring-create-alarms.md").
