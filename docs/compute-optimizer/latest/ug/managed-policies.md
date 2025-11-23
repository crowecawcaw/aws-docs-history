# AWS managed policies for AWS Compute Optimizer

To add permissions to users, groups, and roles, consider using AWS managed policies
rather than to writing your own policies. It takes time and expertise to [create IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the
permissions they need. To get started quickly, you can use AWS managed policies. These
policies cover common use cases and are available in your AWS account. For more
information about AWS managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services don't remove permissions from an AWS managed policy, so policy updates
won't break your existing permissions.

Additionally, Amazon Web Services supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all and resources. When a service launches a new
feature, AWS adds read-only permissions for new operations and resources. For a list and
descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed
  policy: ComputeOptimizerServiceRolePolicy](#security-iam-awsmanpol-ComputeOptimizerServiceRolePolicy "#security-iam-awsmanpol-ComputeOptimizerServiceRolePolicy")
- [AWS managed
  policy: ComputeOptimizerReadOnlyAccess](#security-iam-awsmanpol-ComputeOptimizerReadOnlyAccess "#security-iam-awsmanpol-ComputeOptimizerReadOnlyAccess")
- [AWS managed policy: ComputeOptimizerAutomationServiceRolePolicy](#security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy "#security-iam-awsmanpol-ComputeOptimizerAutomationServiceRolePolicy")
- [Compute Optimizer updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed

policy: ComputeOptimizerServiceRolePolicy

The `ComputeOptimizerServiceRolePolicy` managed policy is attached to a
service-linked role that allows Compute Optimizer to perform actions on your behalf. For more
information, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md "using-service-linked-roles.md").

###### Note

You can't attach `ComputeOptimizerServiceRolePolicy` to your IAM
entities.

**Permissions details**

This policy includes the following permissions.

- `compute-optimizer` – Grants full administrative permissions
  to all resources in Compute Optimizer.
- `organizations` – Allows the management account of an AWS
  organization to opt in member accounts of the organization to Compute Optimizer.
- `cloudwatch` – Grants access to CloudWatch resource metrics for
  the purpose of analyzing them and generating Compute Optimizer resource
  recommendations.
- `autoscaling` – Grants access to EC2 Amazon EC2 Auto Scaling groups and the
  instances in EC2 Amazon EC2 Auto Scaling groups for validation purposes.
- `Ec2` – Grants access to Amazon EC2 instances and volumes.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ComputeOptimizerFullAccess",
 "Effect": "Allow",
 "Action": [
 "compute-optimizer:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AwsOrgsAccess",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CloudWatchAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData",
 "cloudwatch:DescribeAlarms"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AutoScalingAccess",
 "Effect": "Allow",
 "Action": [
 "autoscaling:DescribeAutoScalingInstances",
 "autoscaling:DescribeAutoScalingGroups",
 "autoscaling:DescribePolicies",
 "autoscaling:DescribeScheduledActions"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Ec2Access",
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeVolumes"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ComputeOptimizerFullAccess",
 "Effect": "Allow",
 "Action": [
 "compute-optimizer:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AwsOrgsAccess",
 "Effect": "Allow",
 "Action": [
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListAWSServiceAccessForOrganization"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "CloudWatchAccess",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed

policy: ComputeOptimizerReadOnlyAccess

You can attach the `ComputeOptimizerReadOnlyAccess` policy to your IAM
identities.

This policy grants read-only permissions that allow IAM users to view Compute Optimizer resource
recommendations.

**Permissions details**

This policy includes the following:

- `compute-optimizer` – Grants read-only access to Compute Optimizer
  resource recommendations.
- `ec2` – Grants read-only access to Amazon EC2 instances and Amazon EBS
  volumes.
- `autoscaling` – Grants read-only access to EC2 Amazon EC2 Auto Scaling
  groups.
- `lambda` – Grants read-only access to AWS Lambda functions
  and their configurations.
- `cloudwatch` – Grants read-only access to Amazon CloudWatch metric
  data for resource types that are supported by Compute Optimizer.
- `organizations` – Grants read-only access to member accounts
  of an AWS organization.
- `ecs` – Grants access to Amazon ECS services on Fargate.
- `rds` – Grants read-only access to Amazon RDS instances and
  clusters.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "compute-optimizer:DescribeRecommendationExportJobs",
 "compute-optimizer:GetEnrollmentStatus",
 "compute-optimizer:GetEnrollmentStatusesForOrganization",
 "compute-optimizer:GetRecommendationSummaries",
 "compute-optimizer:GetEC2InstanceRecommendations",
 "compute-optimizer:GetEC2RecommendationProjectedMetrics",
 "compute-optimizer:GetAutoScalingGroupRecommendations",
 "compute-optimizer:GetEBSVolumeRecommendations",
 "compute-optimizer:GetLambdaFunctionRecommendations",
 "compute-optimizer:GetRecommendationPreferences",
 "compute-optimizer:GetEffectiveRecommendationPreferences",
 "compute-optimizer:GetECSServiceRecommendations",
 "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
 "compute-optimizer:GetLicenseRecommendations",
 "compute-optimizer:GetRDSDatabaseRecommendations",
 "compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics",
 "compute-optimizer:GetIdleRecommendations",
 "ec2:DescribeInstances",
 "ec2:DescribeVolumes",
 "ecs:ListServices",
 "ecs:ListClusters",
 "autoscaling:DescribeAutoScalingGroups",
 "autoscaling:DescribeAutoScalingInstances",
 "lambda:ListFunctions",
 "lambda:ListProvisionedConcurrencyConfigs",
 "cloudwatch:GetMetricData",
 "organizations:ListAccounts",
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount",
 "rds:DescribeDBInstances",
 "rds:DescribeDBClusters"
 ],
 "Resource": "*"
 }
 ]
}`

```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "compute-optimizer:DescribeRecommendationExportJobs",
 "compute-optimizer:GetEnrollmentStatus",
 "compute-optimizer:GetEnrollmentStatusesForOrganization",
 "compute-optimizer:GetRecommendationSummaries",
 "compute-optimizer:GetEC2InstanceRecommendations",
 "compute-optimizer:GetEC2RecommendationProjectedMetrics",
 "compute-optimizer:GetAutoScalingGroupRecommendations",
 "compute-optimizer:GetEBSVolumeRecommendations",
 "compute-optimizer:GetLambdaFunctionRecommendations",
 "compute-optimizer:GetECSServiceRecommendations",
 "compute-optimizer:GetECSServiceRecommendationProjectedMetrics",
 "compute-optimizer:GetLicenseRecommendations",
 "ec2:DescribeInstances",
 "ec2:DescribeVolumes",
 "ecs:ListServices",
 "ecs:ListClusters",
 "autoscaling:DescribeAutoScalingGroups",
 "lambda:ListFunctions",
 "lambda:ListProvisionedConcurrencyConfigs",
 "cloudwatch:GetMetricData",
 "organizations:ListAccounts",
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

The following policy statement only grants read-only access to Compute Optimizer for a
management account of an organization to view org-level recommendations. If you're
the delegated administrator and you want to view org-level recommendations, see
[Policies to grant access to Compute Optimizer for a management account of an
organization](security-iam.md#organization-account-access "security-iam.md#organization-account-access").

## AWS managed policy: ComputeOptimizerAutomationServiceRolePolicy

The `ComputeOptimizerAutomationServiceRolePolicy` managed policy is
attached to a service-linked role that allows Compute Optimizer to to implement optimization recommendations by managing AWS resources in your account. .
For more information, see [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md "using-service-linked-roles.md").

###### Note

You can't attach `ComputeOptimizerAutomationServiceRolePolicy` to your
IAM entities.

**Permissions details**

This policy includes the following permissions:

- `ec2:DescribeVolumes`, `ec2:DescribeSnapshots`,
  `ec2:DescribeVolumesModifications` – Grants read-only
  access to view Amazon EBS volumes, snapshots, and volume modification status for
  monitoring and validation purposes.
- `ec2:ModifyVolume`, `ec2:DeleteVolume` – Allows
  modification and deletion of Amazon EBS volumes, but only for resources that do not
  have the `exclude-from-compute-optimizer-automation`tag. This allows you to exclude resources from automated optimization actions.
- `ec2:CreateSnapshot` – Grants permission to create snapshots
  of Amazon EBS volumes for backup purposes before performing optimization
  actions.
- `ec2:CreateVolume` – Allows creation of Amazon EBS volumes from
  snapshots to support rollback operations in case optimization actions need to be
  reverted.
- `ec2:CreateTags` – Grants permission to add tags to Amazon EBS
  resources for tracking automation events and maintaining resource
  metadata.

To view the permissions for this policy, see [ComputeOptimizerAutomationServiceRolePolicy](../../../aws-managed-policy/latest/reference/ComputeOptimizerAutomationServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/ComputeOptimizerAutomationServiceRolePolicy.md") in the in the _AWS
Managed Policy Reference_.

## Compute Optimizer updates to AWS managed

policies

View details about updates to AWS managed policies for Compute Optimizer since this service began
tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed for this guide.

| Change                                                                    | Description                                                                                                                                                                                                                                                              | Date              |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| Added new `ComputeOptimizerAutomationServiceRolePolicy`<br>managed policy | Added a new<br>`ComputeOptimizerAutomationServiceRolePolicy`<br>service-linked role policy.                                                                                                                                                                              | November 19, 2025 |
| Edit to the `ComputeOptimizerServiceRolePolicy` managed<br>policy         | Added the `cloudwatch:DescribeAlarms`,<br>`autoscaling:DescribePolicies`, and<br>`autoscaling:DescribeScheduledActions` actions to the<br>`ComputeOptimizerServiceRolePolicy` managed<br>policy.                                                                         | January 9, 2025   |
| Edit to the `ComputeOptimizerReadOnlyAccess` managed<br>policy            | Added the `compute-optimizer:GetIdleRecommendations`<br>actions to the `ComputeOptimizerReadOnlyAccess` managed<br>policy.                                                                                                                                               | November 20, 2024 |
| Edit to the `ComputeOptimizerReadOnlyAccess` managed<br>policy            | Added the<br>`compute-optimizer:GetRDSDatabaseRecommendations`,<br>`compute-optimizer:GetRDSDatabaseRecommendationProjectedMetrics`,<br>`rds:DescribeDBInstances`, and<br>`rds:DescribeDBClusters` actions to the<br>`ComputeOptimizerReadOnlyAccess` managed<br>policy. | June 20, 2024     |
| Edit to the `ComputeOptimizerReadOnlyAccess` managed<br>policy            | Added the `compute-optimizer:GetLicenseRecommendations`<br>actions to the `ComputeOptimizerReadOnlyAccess` managed<br>policy.                                                                                                                                            | July 26, 2023     |
| Edit to the `ComputeOptimizerReadOnlyAccess` managed<br>policy            | Added the<br>`compute-optimizer:GetECSServiceRecommendations`,<br>`compute-optimizer:GetECSServiceRecommendationProjectedMetrics`,<br>`ecs:ListServices`, and `ecs:ListClusters`<br>actions to the `ComputeOptimizerReadOnlyAccess` managed<br>policy.                   | December 22, 2022 |
| Edit to the `ComputeOptimizerServiceRolePolicy` managed<br>policy         | Added the `ec2:DescribeInstances`,<br>`ec2:DescribeVolumes`, and<br>`organizations:ListDelegatedAdministrators` actions to<br>the `ComputeOptimizerServiceRolePolicy` managed<br>policy.                                                                                 | July 25, 2022     |
| Edit to the `ComputeOptimizerServiceRolePolicy` managed<br>policy         | Added the `autoscaling:DescribeAutoScalingInstances`<br>and `autoscaling:DescribeAutoScalingGroups` actions to<br>the `ComputeOptimizerServiceRolePolicy` managed<br>policy.                                                                                             | November 29, 2021 |
| Edit to the `ComputeOptimizerReadOnlyAccess` managed<br>policy            | Added the<br>`compute-optimizer:GetRecommendationPreferences`,<br>`compute-optimizer:GetEffectiveRecommendationPreferences`,<br>and `autoscaling:DescribeAutoScalingInstances` actions to<br>the `ComputeOptimizerReadOnlyAccess` managed<br>policy.                     | November 29, 2021 |
| Edit to the `ComputeOptimizerReadOnlyAccess` managed<br>policy            | Added the `GetEnrollmentStatusesForOrganization` action<br>to the `ComputeOptimizerReadOnlyAccess` managed<br>policy.                                                                                                                                                    | August 26, 2021   |
| Compute Optimizer started tracking changes                                | Compute Optimizer started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                              | May 18, 2021      |
