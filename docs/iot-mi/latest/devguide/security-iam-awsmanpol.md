# AWS managed policies for managed integrations

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy:

AWSIoTManagedIntegrationsFullAccess

You can attach the `AWSIoTManagedIntegrationsFullAccess` policy to your IAM
identities.

This policy grants full access permissions to managed integrations and related services. To view
this policy in the AWS Management Console, see [AWSIoTManagedIntegrationsFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTManagedIntegrationsFullAccess?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTManagedIntegrationsFullAccess?section=permissions").

**Permissions details**

This policy includes the following permissions:

- `iotmanagedintegrations` – Provides full access to managed integrations and
  related services for the IAM users, groups, and roles you add this policy
  to.
- `iam` – Allows the assigned IAM users, groups, and roles to
  create a service-linked role in an AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "iotmanagedintegrations:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/iotmanagedintegrations.amazonaws.com/AWSServiceRoleForIoTManagedIntegrations",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "iotmanagedintegrations.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS

managed policy: AWSIoTManagedIntegrationsRolePolicy

You can attach the `AWSIoTManagedIntegrationsRolePolicy` policy to your
IAM identities.

This policy grants managed integrations permission to publish Amazon CloudWatch logs and metrics on your
behalf.

To view this policy in the AWS Management Console, see [AWSIoTManagedIntegrationsRolePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTManagedIntegrationsRolePolicy?section=permissions "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AWSIoTManagedIntegrationsRolePolicy?section=permissions").

**Permissions details**

This policy includes the following permissions.

- `logs` – Provides ability to create Amazon CloudWatch log groups and
  stream logs to the groups.
- `cloudwatch` – Provides ability to publish Amazon CloudWatch metrics. For
  more information on Amazon CloudWatch metrics, see [Metrics in Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CloudWatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/iotmanagedintegrations/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:PrincipalAccount": "${aws:ResourceAccount}"
 }
 }
 },
 {
 "Sid": "CloudWatchStreams",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/iotmanagedintegrations/*:log-stream:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:PrincipalAccount": "${aws:ResourceAccount}"
 }
 }
 },
 {
 "Sid": "CloudWatchMetrics",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": [
 "AWS/IoTManagedIntegrations",
 "AWS/Usage"
 ]
 }
 }
 }
 ]
}`

```

## Managed integrations updates to AWS managed

policies

View details about updates to AWS managed policies for managed integrations since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the managed integrations Document history page.

| Change                                        | Description                                                                 | Date           |
| --------------------------------------------- | --------------------------------------------------------------------------- | -------------- |
| Managed integrations started tracking changes | Managed integrations started tracking changes for its AWS managed policies. | March 03, 2025 |
