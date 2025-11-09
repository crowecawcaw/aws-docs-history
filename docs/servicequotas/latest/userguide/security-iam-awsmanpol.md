# AWS managed policies for Service Quotas

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

## AWS managed policy:

ServiceQuotasFullAccess

You can attach `ServiceQuotasFullAccess` to your users, groups, and roles.

This policy grants permissions that allow full administrative control of the Service Quotas service. You can perform all tasks involved in viewing and managing your quotas for AWS services in Service Quotas in the AWS Regions in your account.

**Permissions details**

This policy includes permissions that allow all actions for Service Quotas, including
viewing AWS default values and applied values, requesting a service quota increase,
and viewing current utilization of resources. This policy also includes 18 permissions
that are not part of Service Quotas and can be broadly split into **non-mutating** and **mutating** operations.
Non-mutating operations include permissions from trusted advisors to retrieve applied
quota value and view current utilization of resources. Mutating operations include
permission to create and delete alarms on utilization of resources, and permissions to
create the service-linked role necessary to create a support case on your behalf while
requesting a quota increase.

This policy includes the following non-mutating and mutating operations that are
_not_ part of Service Quotas:

###### Non-mutating operations

- `autoscaling:DescribeAccountLimits` – Allows Service Quotas to
  retrieve applied quota value for AWS Auto Scaling quotas.
- `cloudformation:DescribeAccountLimits` – Allows Service Quotas to
  retrieve applied quota value for AWS CloudFormation quotas.
- `cloudwatch:DescribeAlarmsForMetric` – Allows you to
  retrieve alarms for specified metrics from Service Quotas that were created for
  notifying automatically whenever a specified quota reaches a percentage of the
  maximum or reaches the maximum level.
- `cloudwatch:DescribeAlarms` – Allows you to retrieve alarms
  from Service Quotas that were created for notifying automatically whenever a
  specified quota reaches a percentage of the maximum or reaches the maximum
  level.
- `cloudwatch:GetMetricData` – Allows Service Quotas to view
  current utilization of resources.
- `cloudwatch:GetMetricStatistics` – Allows Service Quotas to view
  current utilization of resources.
- `dynamodb:DescribeLimits` – Allows Service Quotas to retrieve
  applied quota value for DynamoDB quotas.
- `elasticloadbalancing:DescribeAccountLimits` – Allows
  Service Quotas to retrieve applied quota value for Elastic Load Balancing quotas.
- `iam:GetAccountSummary` – Allows Service Quotas to retrieve
  applied quota value for IAM.
- `kinesis:DescribeLimits` – Allows Service Quotas to retrieve
  applied quota value for Amazon Kinesis quotas.
- `organizations:DescribeAccount` and
  `organizations:DescribeOrganization` – Allows Service Quotas to
  create and execute quota templates.
- `rds:DesceibeAccountAttributes` – Allows Service Quotas to
  retrieve applied quota value for Amazon RDS quotas.
- `route53:GetAccountLimit` – Allows Service Quotas to retrieve
  applied quota value for Amazon Route 53 quotas.
- `tag:GetTagKeys` – Allows Service Quotas to get tag keys
  currently in use in the specified AWS Region for the calling account.
- `tag:GetTagValues` – Allows Service Quotas to get tag values for
  the specified key that are used in the specified AWS Region for the calling
  account.

###### Mutating operations

- `cloudwatch:PutMetricAlarm` – Allows Service Quotas to create an
  alarm for notifying you automatically whenever a specified quota reaches a
  percentage of the maximum or the maximum level.
- `cloudwatch:DeleteAlarms` – Allows Service Quotas to delete the
  specified alarm.
- `organizations:EnableAWSServiceAccess` – Allows Service Quotas to
  create a [service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in all the accounts in your organization. This
  allows Service Quotas to perform operations on your behalf in your organization and
  its accounts.
- `iam:CreateServicelinkedRole` – Allows Service Quotas to create
  an IAM role that allows Service Quotas to create a support case on your behalf when
  you request a quota increase.

To see the latest version of this AWS managed policy, see [`ServiceQuotasFullAccess`](../../../aws-managed-policy/latest/reference/ServiceQuotasFullAccess.md "../../../aws-managed-policy/latest/reference/ServiceQuotasFullAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

ServiceQuotasReadOnlyAccess

You can attach `ServiceQuotasReadOnlyAccess` to your users, groups, and roles.

This policy grants permissions that allow users to view their AWS default quotas, applied quotas, and view current utilization of resources.

**Permissions details**

This policy includes permissions that allow your to perform the Service Quotas
`Get*`, and `List*` operations to view your AWS default
quotas and applied quotas. You can also view current utilization of resources.

###### Note

This policy does not allow you to request a service quota increase.

This policy includes the following non-mutating operations that are
_not_ part of Service Quotas:

###### Non-mutating operations

- `autoscaling:DescribeAccountLimits` – Allows Service Quotas to
  retrieve applied quota value for AWS Auto Scaling quotas.
- `cloudformation:DescribeAccountLimits` – Allows Service Quotas to
  retrieve applied quota value for AWS CloudFormation quotas.
- `cloudwatch:DescribeAlarmsForMetric` – Allows you to
  retrieve alarms for specified metrics from Service Quotas that were created for
  notifying automatically whenever a specified quota reaches a percentage of the
  maximum or reaches the maximum level.
- `cloudwatch:DescribeAlarms` – Allows you to retrieve alarms
  from Service Quotas that were created for notifying automatically whenever a
  specified quota reaches a percentage of the maximum or reaches the maximum
  level.
- `cloudwatch:GetMetricData` – Allows Service Quotas to view
  current utilization of resources.
- `cloudwatch:GetMetricStatistics` – Allows Service Quotas to view
  current utilization of resources.
- `dynamodb:DescribeLimits` – Allows Service Quotas to retrieve
  applied quota value for DynamoDB quotas.
- `elasticloadbalancing:DescribeAccountLimits` – Allows
  Service Quotas to retrieve applied quota value for Elastic Load Balancing quotas.
- `iam:GetAccountSummary` – Allows Service Quotas to retrieve
  applied quota value for IAM.
- `kinesis:DescribeLimits` – Allows Service Quotas to retrieve
  applied quota value for Amazon Kinesis quotas.
- `organizations:DescribeAccount` and
  `organizations:DescribeOrganization` – Allows Service Quotas to
  create and execute quota templates.
- `rds:DesceibeAccountAttributes` – Allows Service Quotas to
  retrieve applied quota value for Amazon RDS quotas.
- `route53:GetAccountLimit` – Allows Service Quotas to retrieve
  applied quota value for Amazon Route 53 quotas.
- `tag:GetTagKeys` – Allows Service Quotas to get tag keys
  currently in use in the specified AWS Region for the calling account.
- `tag:GetTagValues` – Allows Service Quotas to get tag values for
  the specified key that are used in the specified AWS Region for the calling
  account.
- `notifications:ListChannels` - Allows Service Quotas to list the channels for
  your Automatic Management configuration.
- `notifications:ListEventRules` - Allows Service Quotas to list the event
  rules Automatic Management configuration.
- `notifications:ListNotificationConfigurations` - Allows Service Quotas to
  list the notifications configuration for your Automatic Management configuration.
- `notifications:GetNotificationConfiguration` - Allows Service Quotas to
  retrieve the notification configuration for your Automatic Management
  configuration.
- `notifications:GetEventRule` - Allows Service Quotas to retrieve the event
  rules for your Automatic Management configuration.
- `notifications:ListNotificationHubs` - Allows Service Quotas to list the
  notification hubs for your Automatic Management configuration.
- `notifications-contacts:ListEmailContacts` - Allows Service Quotas to list
  all the email contacts under the AWS account.
- `notifications-contacts:GetEmailContact` - Allows Service Quotas to retrieve
  all the email contacts under the AWS account.
- `chatbot:ListMicrosoftTeamsChannelConfigurations` - Allows Service Quotas to
  list all Amazon Q Developer Microsoft Team channel configurations in an
  AWS account.
- `chatbot:DescribeChimeWebhookConfigurations` - Allows Service Quotas to list
  all Amazon Chime webhook configurations in an AWS account.
- `chatbot:DescribeSlackChannelConfigurations` - Allows Service Quotas to list
  all Slack channel configurations in an AWS account.
- `consoleapp:ListDeviceIdentities` - Allows Service Quotas to list all the
  devices' identities in an AWS account.
- `consoleapp:GetDeviceIdentity` - Allows Service Quotas to retrieve all the
  devices' identities in an AWS account.

To see the latest version of this AWS managed policy, see [`ServiceQuotasReadOnlyAccess`](../../../aws-managed-policy/latest/reference/ServiceQuotasReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ServiceQuotasReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

## AWS managed policy:

ServiceQuotasServiceRolePolicy

This policy is attached to a service-linked role that allows the service to perform
actions on your behalf. You cannot attach this policy to your users, groups, or
roles.

This policy grants permissions that allows Service Quotas to create support cases on your behalf.

**Permissions details**

This policy includes the following operations:

- `support:CreateCase` – Allows Service Quotas to create support
  cases on your behalf when you request a quota increase.
- `support:DescribeCases` – Allows Service Quotas to retrieve the
  details and status of your support case for the quota increase request.
- `support:RresolveCase` – Allows Service Quotas to resolve support
  cases on your behalf.

To see the latest version of this AWS managed policy, see [`ServiceQuotasServiceRolePolicy`](../../../aws-managed-policy/latest/reference/ServiceQuotasServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/ServiceQuotasServiceRolePolicy.md") in the _AWS Managed Policy
Reference Guide_.

## Service Quotas updates to AWS managed

policies

View details about updates to AWS managed policies for Service Quotas since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Service Quotas Document history page.

| Change                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Date            |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| [ServiceQuotasReadOnlyAccess](#security-iam-awsmanpol-POLICYNAME2 "#security-iam-awsmanpol-POLICYNAME2") – Update policy permissions | Service Quotas modified the permissions for `ServiceQuotasReadOnlyAccess` to<br>support [Automatic Management](automatic-management.md "automatic-management.md").<br>`ServiceQuotasReadOnlyAccess` allows the following actions:<br>• `notifications:ListChannels`<br>• `notifications:ListEventRules`<br>• `notifications:ListNotificationConfigurations`<br>• `notifications:GetNotificationConfiguration`<br>• `notifications:GetEventRule`<br>• `notifications:ListNotificationHubs`<br>• `notifications-contacts:ListEmailContacts`<br>• `notifications-contacts:GetEmailContact`<br>• `chatbot:ListMicrosoftTeamsChannelConfigurations`<br>• `chatbot:DescribeChimeWebhookConfigurations`<br>• `chatbot:DescribeSlackChannelConfigurations`<br>• `consoleapp:ListDeviceIdentities`<br>• `consoleapp:GetDeviceIdentity` | October 3, 2025 |
| [ServiceQuotasFullAccess](#security-iam-awsmanpol-POLICYNAME "#security-iam-awsmanpol-POLICYNAME")<br>– New policy                   | Added a new AWS managed policy that allows full administrative control of the Service Quotas service. You can perform all tasks involved in viewing and managing your quotas for AWS services in Service Quotas in the AWS Regions in your account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | May 30, 2024    |
| [ServiceQuotasReadOnlyAccess](#security-iam-awsmanpol-POLICYNAME2 "#security-iam-awsmanpol-POLICYNAME2") – New policy                | Added a new AWS managed policy that allows users to view their AWS default quotas, applied quotas, and view current utilization of resources.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | May 30, 2024    |
| [ServiceQuotasServiceRolePolicy](#security-iam-awsmanpol-POLICYNAME3 "#security-iam-awsmanpol-POLICYNAME3") – New policy             | Added a new AWS managed policy that allows Service Quotas to create support cases on your behalf.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | May 30, 2024    |
| Service Quotas started tracking changes                                                                                              | Service Quotas started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | May 30, 2024    |
