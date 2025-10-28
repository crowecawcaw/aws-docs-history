**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# IAM policies for querying Amazon Pinpoint analytics

data

By using the Amazon Pinpoint API, you can query analytics data for a subset of standard metrics,
also referred to as _key performance indicators (KPIs)_ that apply to
Amazon Pinpoint projects, campaigns, and journeys. These metrics can help you monitor and assess the
performance of projects, campaigns, and journeys.

To manage access to this data, you can create AWS Identity and Access Management (IAM) policies that define
permissions for IAM roles or users who are authorized to access the data. To support
granular control of access to this data, Amazon Pinpoint provides several distinct actions that you
can specify in IAM policies. There is a distinct action for viewing analytics data on the
Amazon Pinpoint console (`mobiletargeting:GetReports`), and there are other actions for
accessing analytics data programmatically by using the Amazon Pinpoint API.

To create IAM policies that manage access to analytics data, you can use the AWS Management Console,
the AWS CLI, or the IAM API. Note that the **Visual editor** tab on the
AWS Management Console doesn’t currently include actions for viewing or querying Amazon Pinpoint analytics data.
However, you can add the necessary actions to IAM policies manually by using the
**JSON** tab on the console.

For example, the following policy allows programmatic access to all the analytics data for
all of your projects, campaigns, and journeys in all AWS Regions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QueryAllAnalytics",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:GetApplicationDateRangeKpi",
 "mobiletargeting:GetCampaignDateRangeKpi",
 "mobiletargeting:GetJourneyDateRangeKpi",
 "mobiletargeting:GetJourneyExecutionMetrics",
 "mobiletargeting:GetJourneyExecutionActivityMetrics"
 ],
 "Resource": [
 "arn:aws:mobiletargeting:*:`111122223333`:apps/*/kpis/*",
 "arn:aws:mobiletargeting:*:`111122223333`:apps/*/campaigns/*/kpis/*",
 "arn:aws:mobiletargeting:*:`111122223333`:apps/*/journeys/*/kpis/*",
 "arn:aws:mobiletargeting:*:`111122223333`:apps/*/journeys/*/execution-metrics",
 "arn:aws:mobiletargeting:*:`111122223333`:apps/*/journeys/*/activities/*/execution-metrics"
 ]
 }
 ]
}`

```

Where `accountId` is your AWS account ID.

However, as a best practice, you should create policies that follow the principle of
_least privilege_. In other words, you should create policies that
include only the permissions that are required to perform a specific task. To support this
practice and implement more granular control, you can restrict programmatic access to the
analytics data for only a particular project in a specific AWS Region, for example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QueryProjectAnalytics",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:GetApplicationDateRangeKpi",
 "mobiletargeting:GetCampaignDateRangeKpi",
 "mobiletargeting:GetJourneyDateRangeKpi",
 "mobiletargeting:GetJourneyExecutionMetrics",
 "mobiletargeting:GetJourneyExecutionActivityMetrics"
 ],
 "Resource": [
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/kpis/*",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/campaigns/*/kpis/*",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/journeys/*/kpis/*",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/journeys/*/execution-metrics",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/journeys/*/activities/*/execution-metrics"
 ]
 }
 ]
}`

```

Where:

- `region` is the name of the AWS Region that hosts the
  project.
- `accountId` is your AWS account ID.
- `projectId` is the identifier for the project that you
  want to provide access to.
  Similarly, the following example policy allows programmatic access to the analytics data
  for only a particular campaign:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QueryCampaignAnalytics",
 "Effect": "Allow",
 "Action": "mobiletargeting:GetCampaignDateRangeKpi",
 "Resource": "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/campaigns/`campaignId`/kpis/*"
 }
 ]
}`

```

Where:

- `region` is the name of the AWS Region that hosts the
  project.
- `accountId` is your AWS account ID.
- `projectId` is the identifier for the project that’s
  associated with the campaign.
- `campaignId` is the identifier for the campaign that you
  want to provide access to.
  And the following example policy allows programmatic access to all the analytics data,
  both engagement and execution data, for a particular journey and the activities that
  comprise that journey:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QueryJourneyAnalytics",
 "Effect": "Allow",
 "Action": [
 "mobiletargeting:GetJourneyDateRangeKpi",
 "mobiletargeting:GetJourneyExecutionMetrics",
 "mobiletargeting:GetJourneyExecutionActivityMetrics"
 ],
 "Resource": [
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/journeys/`journeyId`/kpis/*",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/journeys/`journeyId`/execution-metrics",
 "arn:aws:mobiletargeting:`us-east-1`:`111122223333`:apps/`projectId`/journeys/`journeyId`/activities/*/execution-metrics"
 ]
 }
 ]
}`

```

Where:

- `region` is the name of the AWS Region that hosts the
  project.
- `accountId` is your AWS account ID.
- `projectId` is the identifier for the project that’s
  associated with the journey.
- `journeyId` is the identifier for the journey that you
  want to provide access to.
  For a complete list of Amazon Pinpoint API actions that you can use in IAM policies, see [Amazon Pinpoint actions for IAM policies](permissions-actions.md "permissions-actions.md"). For detailed information about creating and managing
  IAM policies, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").
