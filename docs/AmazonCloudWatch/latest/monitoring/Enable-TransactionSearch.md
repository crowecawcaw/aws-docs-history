# Enable transaction search

You can enable [Transaction Search](CloudWatch-Transaction-Search.md "CloudWatch-Transaction-Search.md") through the console or by using an
API. Transaction search is configured for the entire account and switches all spans
ingestion through X-Ray into cost effective collection mode using [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). By default you will also index
1% of ingested spans for free as trace summary for analysis, which is typically sufficient given you already have full end-to-end
trace visibility on all ingested spans through Transaction Search.

## Prerequisites

Before you can enable Transaction Search, you must create a role with the following
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TransactionSearchXRayPermissions",
 "Effect": "Allow",
 "Action": [
 "xray:GetTraceSegmentDestination",
 "xray:UpdateTraceSegmentDestination",
 "xray:GetIndexingRules",
 "xray:UpdateIndexingRule"
 ],
 "Resource": "*"
 },
 {
 "Sid": "TransactionSearchLogGroupPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutRetentionPolicy"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/application-signals/data:*",
 "arn:aws:logs:*:*:log-group:aws/spans:*"
 ]
 },
 {
 "Sid": "TransactionSearchLogsPermissions",
 "Effect": "Allow",
 "Action": [
 "logs:PutResourcePolicy",
 "logs:DescribeResourcePolicies"
 ],
 "Resource": "*"
 },
 {
 "Sid": "TransactionSearchApplicationSignalsPermissions",
 "Effect": "Allow",
 "Action": [
 "application-signals:StartDiscovery"
 ],
 "Resource": "*"
 },
 {
 "Sid": "CloudWatchApplicationSignalsCreateServiceLinkedRolePermissions",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/application-signals.cloudwatch.amazonaws.com/AWSServiceRoleForCloudWatchApplicationSignals",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "application-signals.cloudwatch.amazonaws.com"
 }
 }
 },
 {
 "Sid": "CloudWatchApplicationSignalsGetRolePermissions",
 "Effect": "Allow",
 "Action": "iam:GetRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/application-signals.cloudwatch.amazonaws.com/AWSServiceRoleForCloudWatchApplicationSignals"
 },
 {
 "Sid": "CloudWatchApplicationSignalsCloudTrailPermissions",
 "Effect": "Allow",
 "Action": [
 "cloudtrail:CreateServiceLinkedChannel"
 ],
 "Resource": "arn:aws:cloudtrail:*:*:channel/aws-service-channel/application-signals/*"
 }
 ]
}`

```

###### Note

To use Transaction Search and other CloudWatch features, add the [CloudWatchReadOnlyAccess policy](../../../aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/CloudWatchReadOnlyAccess.md") to your role. For information about how
to create a role, see [IAM role creation](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md").

## Enabling Transaction Search in the console

The following procedure describes how to enable Transaction Search in the
console.

###### To enable Transaction Search in the CloudWatch console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. From the navigation pane, under **Application Signals**,
   choose **Transaction Search**.
3. Choose **Enable Transaction Search**.
4. Select the box to ingest spans as structured logs, and enter a percentage
   of spans to be indexed. You can index spans at 1% for free and change the
   percentage later based on your requirements.

## Enabling Transaction Search using an API

The following procedure describes how to enable Transaction Search using an API.

### Step 1. Create a policy that grants access to ingest spans in CloudWatch Logs

When using the AWS CLI or SDK to enable Transaction Search, you must configure
permissions using a resource-based policy with [`PutResourcePolicy`](../../../xray/latest/api/API_PutResourcePolicy.md "../../../xray/latest/api/API_PutResourcePolicy.md").

###### Example policy

The following example policy allows X-Ray to send traces to CloudWatch Logs

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TransactionSearchXRayAccess",
 "Effect": "Allow",
 "Principal": {
 "Service": "xray.amazonaws.com"
 },
 "Action": "logs:PutLogEvents",
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:aws/spans:*",
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/application-signals/data:*"
 ],
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:xray:`us-east-1`:`123456789012`:*"
 },
 "StringEquals": {
 "aws:SourceAccount": "`123456789012`"
 }
 }
 }
 ]
}`

```

###### Example command

The following example shows how to format your AWS CLI command with
`PutResourcePolicy`.

```
aws logs put-resource-policy --policy-name MyResourcePolicy --policy-document '{ "Version": "2012-10-17",		 	 	  "Statement": [ { "Sid": "TransactionSearchXRayAccess", "Effect": "Allow", "Principal": { "Service": "xray.amazonaws.com" }, "Action": "logs:PutLogEvents", "Resource": [ "arn:partition:logs:region:account-id:log-group:aws/spans:*", "arn:partition:logs:region:account-id:log-group:/aws/application-signals/data:*" ], "Condition": { "ArnLike": { "aws:SourceArn": "arn:partition:xray:region:account-id:*" }, "StringEquals": { "aws:SourceAccount": "account-id" } } } ]}'
```

### Step 2. Configure the destination of trace segments

Configure the ingestion of spans with [`UpdateTraceSegmentDestination`](../../../xray/latest/api/API_UpdateTraceSegmentDestination.md "../../../xray/latest/api/API_UpdateTraceSegmentDestination.md").

###### Example command

The following example shows how to format your AWS CLI command with
`UpdateTraceSegmentDestination`.

```
aws xray update-trace-segment-destination --destination CloudWatchLogs
```

### Step 3. Configure the amount of spans to index

Configure your desired sampling percentage with [`UpdateIndexingRule`](../../../xray/latest/api/API_UpdateIndexingRule.md "../../../xray/latest/api/API_UpdateIndexingRule.md")

###### Example command

The following example shows how to format your AWS CLI command with
`UpdateIndexingRule`.

```
aws xray update-indexing-rule --name "Default" --rule '{"Probabilistic": {"DesiredSamplingPercentage": number}}'
```

###### Note

After you enable Transaction Search, it can take ten minutes for spans to
become available for search and analysis.

### Step 4. Verify spans are available for search and analysis

To verify spans are available for search and analysis, use [`GetTraceSegmentDestination`](../../../xray/latest/api/API_GetTraceSegmentDestination.md "../../../xray/latest/api/API_GetTraceSegmentDestination.md").

###### Example commands

The following example shows how to format your AWS CLI command with
`GetTraceSegmentDestination`.

```
aws xray get-trace-segment-destination
```

###### Example response

The following example shows the response you can expect when Transaction
Search is active.

```
{
    "Destination": "CloudWatchLogs",
    "Status": "ACTIVE"
}
```
