# AWS managed policies for Amazon CloudWatch Application Insights

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
  Agent on EC2 instances. For more information, see [Using service-linked roles for CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").

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
monitor customer resources. For more information, see [Using service-linked roles for CloudWatch Application Insights](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md").

## Application Insights updates to AWS managed policies

View details about updates to AWS managed policies for Application Insights since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Application Insights [Document history](DocumentHistory.md "DocumentHistory.md")
page.

| Change                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Date               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added a new permission.<br>The policy change allows Amazon CloudWatch Application Insights to enable and disable<br>termination protection on CloudFormation stacks to manage SSM resources used to install and configure CloudWatch agents.                                                                                                                                                                                                                                                                                                       | July 25, 2024      |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to list CloudFormation stacks.<br>These permissions are required for Amazon CloudWatch Application Insights to analyze and<br>monitor AWS resources nested in the CloudFormation stack.                                                                                                                                                                                                                                                                                                                                      | April 24, 2023     |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to get list of Amazon VPC and Route 53 resources.<br>These permissions are required for Amazon CloudWatch Application Insights to automatically<br>set up best practice network monitoring with Amazon CloudWatch.                                                                                                                                                                                                                                                                                                           | January 23, 2023   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to get SSM command invocation<br>results.<br>These permissions are required for Amazon CloudWatch Application Insights to automatically<br>detect and monitor workloads running on Amazon EC2 instances.                                                                                                                                                                                                                                                                                                                     | December 19, 2022  |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to describe Amazon VPC and Route 53<br>resources.<br>These permissions are required for Amazon CloudWatch Application Insights to read customer<br>Amazon VPC and Route 53 resource configurations, and to help customers<br>automatically set up best practice network monitoring with<br>Amazon CloudWatch.                                                                                                                                                                                                                | December 19, 2022  |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to describe EFS resources.<br>These permissions are required for Amazon CloudWatch Application Insights to read Amazon<br>EFS customer resource configurations, and to help customers<br>automatically set up best practices for EFS monitoring with<br>CloudWatch.                                                                                                                                                                                                                                                          | October 3, 2022    |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to describe the EFS file<br>system.<br>These permissions are required for Amazon CloudWatch Application Insights to create<br>account-based applications by querying all of the supported<br>resources in an account.                                                                                                                                                                                                                                                                                                        | October 3, 2022    |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to retrieve information about FSx<br>resources.<br>These permissions are required for Amazon CloudWatch Application Insights to monitor<br>workloads by retrieving sufficient information about the underlying<br>FSx volumes.                                                                                                                                                                                                                                                                                               | September 12, 2022 |
| [AWS managed policy: CloudWatchApplicationInsightsFullAccess](#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess "#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess")<br>– Update to an existing policy | Application Insights added a new permission to describe log groups.<br>This permissions is required for Amazon CloudWatch Application Insights to ensure that the<br>correct permissions for monitoring log groups are in an account when<br>creating a new application.                                                                                                                                                                                                                                                                                                | January 24, 2022   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to create and delete CloudWatch Log<br>Subscription Filters.<br>These permissions are required for Amazon CloudWatch Application Insights to create Subscription Filters to facilitate log monitoring of resources within configured applications.                                                                                                                                                                                                                                                                           | January 24, 2022   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to describe target groups and<br>target health for Elastic Load Balancers.<br>These permissions are required for Amazon CloudWatch Application Insights to create<br>account-based applications by querying all of the supported<br>resources in an account.                                                                                                                                                                                                                                                                 | November 4, 2021   |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to run the<br>`AmazonCloudWatch-ManageAgent` SSM document on Amazon EC2<br>instances.<br>This permissions is required for Amazon CloudWatch Application Insights to clean up<br>CloudWatch agent configuration files created by Application Insights.                                                                                                                                                                                                                                                                        | September 30, 2021 |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to support account-based<br>application monitoring to onboard and monitor all supported<br>resources in your account.<br>These permissions are required for Amazon CloudWatch Application Insights to query, tag<br>resources, and create groups for these resources.<br>Application Insights added new permissions to support monitoring of SNS<br>topics.<br>These permissions are required for Amazon CloudWatch Application Insights to gather<br>metadata from SNS resources to configure monitoring for SNS<br>topics. | September 15, 2021 |
| [AWS managed policy: CloudWatchApplicationInsightsFullAccess](#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess "#security-iam-awsmanpol-appinsights-CloudWatchApplicationInsightsFullAccess")<br>– Update to an existing policy | Application Insights added new permissions to describe and list supported<br>resources.<br>These permissions are required for Amazon CloudWatch Application Insights to create<br>account-based applications by querying all of the supported<br>resources in an account.                                                                                                                                                                                                                                                                                               | September 15, 2021 |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to describe FSx resources.<br>These permissions are required for Amazon CloudWatch Application Insights to read customer<br>FSx resource configurations, and to help customers automatically set<br>up best practice FSx monitoring with CloudWatch.                                                                                                                                                                                                                                                                         | August 31, 2021    |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to describe and list ECS and EKS<br>service resources.<br>This permission is required for Amazon CloudWatch Application Insights to read customer<br>container resources configuration, and to help customers<br>automatically set up best practice container monitoring with<br>CloudWatch.                                                                                                                                                                                                                                 | May 18, 2021       |
| [CloudwatchApplicationInsightsServiceLinkedRolePolicy](CHAP_using-service-linked-roles-appinsights.md "CHAP_using-service-linked-roles-appinsights.md")<br>– Update to an existing policy                                                                  | Application Insights added new permissions to allow OpsCenter to tag OpsItems<br>using the `ssm:AddTagsToResource` action on resources<br>with the `opsitem` resource type.<br>This permission is required by OpsCenter. Amazon CloudWatch Application Insights creates<br>OpsItems so that the customer can resolve problems using [AWS<br>SSM OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md").                                                                                            | April 13, 2021     |
| Application Insights started tracking<br>changes                                                                                                                                                                                                           | Application Insights started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | April 13, 2021     |
