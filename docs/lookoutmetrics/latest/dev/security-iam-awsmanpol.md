Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# AWS managed policies for Amazon Lookout for Metrics

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## Managed policy:

AmazonLookoutMetricsReadOnlyAccess

The AmazonLookoutMetricsReadOnlyAccess managed policy grants `read-only`
permissions that allow read-only access to all Lookout for Metrics resources. You can attach this policy to your IAM
entities.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lookoutmetrics:DescribeMetricSet",
 "lookoutmetrics:ListMetricSets",
 "lookoutmetrics:DescribeAnomalyDetector",
 "lookoutmetrics:ListAnomalyDetectors",
 "lookoutmetrics:DescribeAnomalyDetectionExecutions",
 "lookoutmetrics:DescribeAlert",
 "lookoutmetrics:ListAlerts",
 "lookoutmetrics:ListTagsForResource",
 "lookoutmetrics:ListAnomalyGroupSummaries",
 "lookoutmetrics:ListAnomalyGroupTimeSeries",
 "lookoutmetrics:ListAnomalyGroupRelatedMetrics",
 "lookoutmetrics:GetAnomalyGroup",
 "lookoutmetrics:GetDataQualityMetrics",
 "lookoutmetrics:GetSampleData",
 "lookoutmetrics:GetFeedback"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Managed policy: AmazonLookoutMetricsFullAccess

The AmazonLookoutMetricsFullAccess managed policy grants full access to Lookout for Metrics resources, and permission to
assign a service role to a detector. You can attach this policy to your IAM entities. A _service role_ is an IAM role that grants permissions to an AWS service so it can
access resources. Service roles must be created by an administrator

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lookoutmetrics:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*LookoutMetrics*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "lookoutmetrics.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Lookout for Metrics updates to AWS managed policies

View details about updates to AWS managed policies for Lookout for Metrics since this service began tracking these
changes.

| Change                                                                                                                                | Description                                                                                             | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------- |
| [AmazonLookoutMetricsReadOnlyAccess](#security-iam-awsmanpol-ReadOnlyAccess "#security-iam-awsmanpol-ReadOnlyAccess") – Update policy | Lookout for Metrics updated the read-only policy to include `ListAnomalyGroupRelatedMetrics`.           | November 24, 2021 |
| [AmazonLookoutMetricsReadOnlyAccess](#security-iam-awsmanpol-ReadOnlyAccess "#security-iam-awsmanpol-ReadOnlyAccess") – New policy    | Lookout for Metrics added a new policy to allow read-only access for all Lookout for Metrics resources. | May 06, 2021      |
| [AmazonLookoutMetricsFullAccess](#security-iam-awsmanpol-FullAccess "#security-iam-awsmanpol-FullAccess") – New policy                | Lookout for Metrics added a new policy to allow full access to all Lookout for Metrics resources.       | May 06, 2021      |
| Lookout for Metrics started tracking changes                                                                                          | Lookout for Metrics started tracking changes for its AWS managed policies.                              | May 06, 2021      |
