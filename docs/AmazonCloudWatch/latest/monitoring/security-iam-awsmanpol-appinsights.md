# AWS managed policies for

Amazon CloudWatch Application Insights

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

## AWS managed policy: CloudWatchApplicationInsightsFullAccess

You can attach the `CloudWatchApplicationInsightsFullAccess` policy to your
IAM identities.

This policy grants administrative permissions that allow full access to Application Insights
functionality.

**Permissions details**

This policy includes the following permissions.

- `applicationinsights` – Allows full access to Application Insights
  functionality.
- `iam` – Allows Application Insights to create the service-linked role,
  AWSServiceRoleForApplicationInsights. This is required so that Application Insights can
  perform operations such as analyze the resource groups of a customer, create
  CloudFormation stacks to create alarms on metrics, and configure the CloudWatch
  Agent on EC2 instances. For more information, see [Using service-linked roles for
  CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "applicationinsights:*",
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DescribeInstances",
 "ec2:DescribeVolumes",
 "rds:DescribeDBInstances",
 "rds:DescribeDBClusters",
 "sqs:ListQueues",
 "elasticloadbalancing:DescribeLoadBalancers",
 "elasticloadbalancing:DescribeTargetGroups",
 "elasticloadbalancing:DescribeTargetHealth",
 "autoscaling:DescribeAutoScalingGroups",
 "lambda:ListFunctions",
 "dynamodb:ListTables",
 "s3:ListAllMyBuckets",
 "sns:ListTopics",
 "states:ListStateMachines",
 "apigateway:GET",
 "ecs:ListClusters",
 "ecs:DescribeTaskDefinition",
 "ecs:ListServices",
 "ecs:ListTasks",
 "eks:ListClusters",
 "eks:ListNodegroups",
 "fsx:DescribeFileSystems",
 "logs:DescribeLogGroups",
 "elasticfilesystem:DescribeFileSystems"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/application-insights.amazonaws.com/AWSServiceRoleForApplicationInsights"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "application-insights.amazonaws.com"
 }
 }
 }
 ]
}`

```

## AWS managed policy: CloudWatchApplicationInsightsReadOnlyAccess

You can attach the `CloudWatchApplicationInsightsReadOnlyAccess` policy to
your IAM identities.

This policy grants administrative permissions that allow read-only access to all
Application Insights functionality.

**Permissions details**

This policy includes the following permissions.

- `applicationinsights` – Allows read-only access to Application Insights
  functionality.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "applicationinsights:Describe*",
 "applicationinsights:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: CloudwatchApplicationInsightsServiceLinkedRolePolicy

You can't attach CloudwatchApplicationInsightsServiceLinkedRolePolicy to your IAM
entities. This policy is attached to a service-linked role that allows Application Insights to
monitor customer resources. For more information, see [Using service-linked roles for
CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").

## Application Insights updates to AWS

managed policies

View details about updates to AWS managed policies for Application Insights since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Application Insights [Document history](DocumentHistory.md "DocumentHistory.md")
page.

| Change                                                                                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added a new permission. The policy change allows Amazon CloudWatch Application Insights to enable and disable termination protection on CloudFormation stacks to manage SSM resources used to install and configure CloudWatch agents.                                                                                                                                                                                                                                                                                  | July 25, 2024      |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to list CloudFormation stacks. These permissions are required for Amazon CloudWatch Application Insights to analyze and monitor AWS resources nested in the CloudFormation stack.                                                                                                                                                                                                                                                                                                                 | April 24, 2023     |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to get list of Amazon VPC and Route 53 resources. These permissions are required for Amazon CloudWatch Application Insights to automatically set up best practice network monitoring with Amazon CloudWatch.                                                                                                                                                                                                                                                                                      | January 23, 2023   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to get SSM command invocation results. These permissions are required for Amazon CloudWatch Application Insights to automatically detect and monitor workloads running on Amazon EC2 instances.                                                                                                                                                                                                                                                                                                   | December 19, 2022  |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to describe Amazon VPC and Route 53 resources. These permissions are required for Amazon CloudWatch Application Insights to read customer Amazon VPC and Route 53 resource configurations, and to help customers automatically set up best practice network monitoring with Amazon CloudWatch.                                                                                                                                                                                                    | December 19, 2022  |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to describe EFS resources. These permissions are required for Amazon CloudWatch Application Insights to read Amazon EFS customer resource configurations, and to help customers automatically set up best practices for EFS monitoring with CloudWatch.                                                                                                                                                                                                                                           | October 3, 2022    |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to describe the EFS file system. These permissions are required for Amazon CloudWatch Application Insights to create account-based applications by querying all of the supported resources in an account.                                                                                                                                                                                                                                                                                         | October 3, 2022    |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to retrieve information about FSx resources. These permissions are required for Amazon CloudWatch Application Insights to monitor workloads by retrieving sufficient information about the underlying FSx volumes.                                                                                                                                                                                                                                                                                | September 12, 2022 |
| [AWS managed policy: CloudWatchApplicationInsightsFullAccess](#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess "#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess") – Update to an existing policy | Application Insights added a new permission to describe log groups. This permissions is required for Amazon CloudWatch Application Insights to ensure that the correct permissions for monitoring log groups are in an account when creating a new application.                                                                                                                                                                                                                                                                              | January 24, 2022   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to create and delete CloudWatch Log Subscription Filters. These permissions are required for Amazon CloudWatch Application Insights to create Subscription Filters to facilitate log monitoring of resources within configured applications.                                                                                                                                                                                                                                                      | January 24, 2022   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to describe target groups and target health for Elastic Load Balancers. These permissions are required for Amazon CloudWatch Application Insights to create account-based applications by querying all of the supported resources in an account.                                                                                                                                                                                                                                                  | November 4, 2021   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to run the `AmazonCloudWatch-ManageAgent` SSM document on Amazon EC2 instances. This permissions is required for Amazon CloudWatch Application Insights to clean up CloudWatch agent configuration files created by Application Insights.                                                                                                                                                                                                                                                         | September 30, 2021 |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to support account-based application monitoring to onboard and monitor all supported resources in your account. These permissions are required for Amazon CloudWatch Application Insights to query, tag resources, and create groups for these resources. Application Insights added new permissions to support monitoring of SNS topics. These permissions are required for Amazon CloudWatch Application Insights to gather metadata from SNS resources to configure monitoring for SNS topics. | September 15, 2021 |
| [AWS managed policy: CloudWatchApplicationInsightsFullAccess](#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess "#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess") – Update to an existing policy | Application Insights added new permissions to describe and list supported resources. These permissions are required for Amazon CloudWatch Application Insights to create account-based applications by querying all of the supported resources in an account.                                                                                                                                                                                                                                                                                | September 15, 2021 |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to describe FSx resources. These permissions are required for Amazon CloudWatch Application Insights to read customer FSx resource configurations, and to help customers automatically set up best practice FSx monitoring with CloudWatch.                                                                                                                                                                                                                                                       | August 31, 2021    |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to describe and list ECS and EKS service resources. This permission is required for Amazon CloudWatch Application Insights to read customer container resources configuration, and to help customers automatically set up best practice container monitoring with CloudWatch.                                                                                                                                                                                                                     | May 18, 2021       |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md") – Update to an existing policy                                                                  | Application Insights added new permissions to allow OpsCenter to tag OpsItems using the `ssm:AddTagsToResource` action on resources with the `opsitem` resource type. This permission is required by OpsCenter. Amazon CloudWatch Application Insights creates OpsItems so that the customer can resolve problems using [AWS SSM OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md").                                                                                | April 13, 2021     |
| Application Insights started tracking changes                                                                                                                                                                                                           | Application Insights started tracking changes for its AWS managed policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | April 13, 2021     |
