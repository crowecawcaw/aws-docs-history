# Using service-linked roles for

CloudWatch

Amazon CloudWatch uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to CloudWatch. Service-linked roles are predefined by
CloudWatch and include all the permissions that the service requires to call other
AWS services on your behalf.

One service-linked role in CloudWatch makes setting up CloudWatch alarms that can terminate, stop,
or reboot an Amazon EC2 instance without requiring you to manually add the necessary
permissions. Another service-linked role enables a monitoring account to access CloudWatch
data from other accounts that you specify, to build cross-account cross-Region
dashboards.

CloudWatch defines the permissions of these service-linked roles, and unless
defined otherwise, only CloudWatch can assume the role. The defined permissions
include the trust policy and the permissions policy, and that permissions policy cannot
be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This
restriction protects your CloudWatch resources because you can't inadvertently remove
permissions to access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column.
Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions

for CloudWatch alarms EC2 actions

CloudWatch uses the service-linked role named **AWSServiceRoleForCloudWatchEvents**
– CloudWatch uses this service-linked role to perform Amazon EC2 alarm actions.

The AWSServiceRoleForCloudWatchEvents service-linked role trusts the CloudWatch Events service to assume the role.
CloudWatch Events invokes the terminate, stop, or reboot instance actions when called upon by
the alarm.

The AWSServiceRoleForCloudWatchEvents service-linked role permissions policy allows CloudWatch Events to complete the
following actions on Amazon EC2 instances:

- `ec2:StopInstances`
- `ec2:TerminateInstances`
- `ec2:RecoverInstances`
- `ec2:DescribeInstanceRecoveryAttribute`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceStatus`

The **AWSServiceRoleForCloudWatchCrossAccount** service-linked
role permissions policy allows CloudWatch to complete the following actions:

- `sts:AssumeRole`

## Service-linked role

permissions for CloudWatch telemetry config

CloudWatch observability admin creates and uses a service-linked role named
**AWSServiceRoleForObservabilityAdmin** – CloudWatch uses this
service-linked role to support resource and telemetry config discovery for AWS
Organizations. The role is created in all member accounts of the
Organization.

The **AWSServiceRoleForObservabilityAdmin** service-linked role
trusts Observability Admin to assume the role. Observability Admin manages AWS
Config Service Linked Configuration Recorders and Service Linked Configuration
Aggregator in your Organizations accounts.

The **AWSServiceRoleForObservabilityAdmin** service-linked role
has a policy, called AWSObservabilityAdminServiceRolePolicy, attached and this
policy grants permission to CloudWatch Observability Admin to complete the following
actions:

- `organizations:ListAccounts`
- `organizations:ListAccountsForParent`
- `organizations:ListChildren`
- `organizations:ListParents`
- `organizations:DescribeOrganization`
- `organizations:DescribeOrganizationalUnit`
- `organizations:EnableAWSServiceAccess`
- `organizations:ListDelegatedAdministrators`
- `config:PutServiceLinkedConfigurationRecorder`
- `config:DeleteServiceLinkedConfigurationRecorder`
- `config:PutConfigurationAggregator`
- `config:DeleteConfigurationAggregator`
- `config:SelectAggregateResourceConfig`
- `iam:CreateServiceLinkedRole`
- `iam:PassRole`

The complete contents of the AWSObservabilityAdminServiceRolePolicy policy are as
follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListChildren",
 "organizations:ListParents",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "config:PutServiceLinkedConfigurationRecorder",
 "config:DeleteServiceLinkedConfigurationRecorder"
 ],
 "Resource": [
 "arn:aws:config:*:*:configuration-recorder/AWSConfigurationRecorderForObservabilityAdmin/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "config:PutConfigurationAggregator",
 "config:DeleteConfigurationAggregator",
 "config:SelectAggregateResourceConfig"
 ],
 "Resource": [
 "arn:aws:config:*:*:config-aggregator/aws-service-config-aggregator/observabilityadmin.amazonaws.com/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "config.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "config.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "config.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "observabilityadmin.amazonaws.com",
 "config.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Service-linked role

permissions for CloudWatch telemetry enablement

The `AWSObservabilityAdminTelemetryEnablementServiceRolePolicy` grants
permissions necessary to enable and manage telemetry configurations for AWS
resources based on telemetry rules.

This policy grants permissions for:

- Basic telemetry operations including describing VPCs, flow logs, log
  groups, and managing EC2 instance monitoring
- Resource tagging operations with the
  `CloudWatchTelemetryRuleManaged` tag for tracking managed
  resources
- Log delivery configuration for services like AWS Bedrock and VPC Flow
  Logs
- Configuration recorder management for telemetry enablement tracking

The policy enforces security boundaries through conditions that:

- Restrict operations to resources within the same account using
  `aws:ResourceAccount`
- Require the `CloudWatchTelemetryRuleManaged` tag for resource
  modifications
- Limit configuration recorder access to those associated with telemetry
  enablement

The complete contents of the
AWSObservabilityAdminTelemetryEnablementServiceRolePolicy are as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccounts",
 "organizations:ListAccountsForParent",
 "organizations:ListChildren",
 "organizations:ListParents",
 "organizations:DescribeOrganization",
 "organizations:DescribeOrganizationalUnit"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "config:PutServiceLinkedConfigurationRecorder",
 "config:DeleteServiceLinkedConfigurationRecorder"
 ],
 "Resource": [
 "arn:aws:config:*:*:configuration-recorder/AWSConfigurationRecorderForObservabilityAdmin/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "config:PutConfigurationAggregator",
 "config:DeleteConfigurationAggregator",
 "config:SelectAggregateResourceConfig"
 ],
 "Resource": [
 "arn:aws:config:*:*:config-aggregator/aws-service-config-aggregator/observabilityadmin.amazonaws.com/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateServiceLinkedRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig"
 ],
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "config.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "config.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:EnableAWSServiceAccess"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "config.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "observabilityadmin.amazonaws.com",
 "config.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## Service-linked role permissions for

CloudWatch Application Signals

CloudWatch Application Signals uses the service-linked role named
**AWSServiceRoleForCloudWatchApplicationSignals** – CloudWatch
uses this service-linked role to collect CloudWatch Logs data, X-Ray trace data, CloudWatch metrics
data, and tagging data from applications that you have enabled for CloudWatch Application
Signals.

The **AWSServiceRoleForCloudWatchApplicationSignals**
service-linked role trusts CloudWatch Application Signals to assume the role. Application
Signals collects the logs, traces, metrics, and tags data from your account.

The **AWSServiceRoleForCloudWatchApplicationSignals** has an
IAM policy attached, and this policy is named
**CloudWatchApplicationSignalsServiceRolePolicy**. This policy
grants permission to CloudWatch Application Signals to collect monitoring and tagging data
from other relevant AWS services. It includes permissions for Application Signals
to complete the following actions:

- `xray` – Retrieve X-Ray traces.
- `logs` – Retrieve the current CloudWatch logs
  information.
- `cloudwatch` – Retrieve the current CloudWatch metric
  information.
- `tags` – Retrieve the current tags.
- `application-signals` – Retrieve information on SLOs and
  their associated time exclusion windows.
- `autoscaling` – Retrieve application tags from Amazon EC2
  Autoscaling group.

The complete contents of
**CloudWatchApplicationSignalsServiceRolePolicy** are as
follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "XRayPermission",
 "Effect": "Allow",
 "Action": [
 "xray:GetServiceGraph"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "CWLogsPermission",
 "Effect": "Allow",
 "Action": [
 "logs:StartQuery",
 "logs:GetQueryResults"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/appsignals/*:*",
 "arn:aws:logs:*:*:log-group:/aws/application-signals/data:*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "CWListMetricsPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:ListMetrics"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "CWGetMetricDataPermission",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:GetMetricData"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "TagsPermission",
 "Effect": "Allow",
 "Action": [
 "tag:GetResources"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "ApplicationSignalsPermission",
 "Effect": "Allow",
 "Action": [
 "application-signals:ListServiceLevelObjectiveExclusionWindows",
 "application-signals:GetServiceLevelObjective"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "EC2AutoScalingPermission",
 "Effect": "Allow",
 "Action": [
 "autoscaling:DescribeAutoScalingGroups"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

## Service-linked role

permissions for CloudWatch alarms Systems Manager OpsCenter actions

CloudWatch uses the service-linked role named
**AWSServiceRoleForCloudWatchAlarms_ActionSSM** – CloudWatch
uses this service-linked role to perform Systems Manager OpsCenter actions when a CloudWatch alarm
goes into ALARM state.

The AWSServiceRoleForCloudWatchAlarms_ActionSSM service-linked role trusts the
CloudWatch service to assume the role. CloudWatch alarms invoke the Systems Manager OpsCenter actions when
called upon by the alarm.

The **AWSServiceRoleForCloudWatchAlarms_ActionSSM**
service-linked role permissions policy allows Systems Manager to complete the following
actions:

- `ssm:CreateOpsItem`

## Service-linked

role permissions for CloudWatch alarms Systems Manager Incident Manager actions

CloudWatch uses the service-linked role named
**AWSServiceRoleForCloudWatchAlarms_ActionSSMIncidents**
– CloudWatch uses this service-linked role to start Incident Manager incidents when
a CloudWatch alarm goes into ALARM state.

The **AWSServiceRoleForCloudWatchAlarms_ActionSSMIncidents**
service-linked role trusts the CloudWatch service to assume the role. CloudWatch alarms invoke
the Systems Manager Incident Manager action when called upon by the alarm.

The **AWSServiceRoleForCloudWatchAlarms_ActionSSMIncidents**
service-linked role permissions policy allows Systems Manager to complete the following
actions:

- `ssm-incidents:StartIncident`

## Service-linked role permissions

for CloudWatch cross-account cross-Region

CloudWatch uses the service-linked role named
**AWSServiceRoleForCloudWatchCrossAccount** – CloudWatch uses
this role to access CloudWatch data in other AWS accounts that you specify. The SLR only
provides the assume role permission to allow the CloudWatch service to assume the role in
the sharing account. It is the sharing role that provides access to data.

The **AWSServiceRoleForCloudWatchCrossAccount** service-linked
role permissions policy allows CloudWatch to complete the following actions:

- `sts:AssumeRole`

The **AWSServiceRoleForCloudWatchCrossAccount** service-linked
role trusts the CloudWatch service to assume the role.

## Service-linked role

permissions for CloudWatch database Performance Insights

CloudWatch uses the service-linked role named
**AWSServiceRoleForCloudWatchMetrics_DbPerfInsights** –
CloudWatch uses this role to retrieve Performance Insights metrics for creating alarms and
snapshotting.

The **AWSServiceRoleForCloudWatchMetrics_DbPerfInsights**
service-linked role has the
`AWSServiceRoleForCloudWatchMetrics_DbPerfInsightsServiceRolePolicy`
IAM policy attached. The contents of that policy are as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "pi:GetResourceMetrics"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "${aws:PrincipalAccount}"
 }
 }
 }
 ]
}`

```

The **AWSServiceRoleForCloudWatchMetrics_DbPerfInsights**
service-linked role trusts the CloudWatch service to assume the role.

## Service-linked role

permissions for CloudWatch Logs centralization

CloudWatch uses the service-linked role named
**AWSObservabilityAdminLogsCentralizationServiceRolePolicy**
– CloudWatch Observability Admin uses this role to use telemetry data from other
AWS accounts that you specify to create CloudWatch log groups, log streams, and log
events in your organization's monitoring account. The SLR only provides the assume
role permission to allow the CloudWatch service to assume the role in the monitoring
account.

The **AWSObservabilityAdminLogsCentralizationServiceRolePolicy**
service-linked role permissions policy allows CloudWatch to complete the following
actions:

- `sts:AssumeRole`

`logs:CreateLogGroup`

`logs:CreateLogStream`

`logs:PutLogEvents`

`kms:Encrypt`

`kms:Decrypt`

`kms:GenerateDataKey`

The **AWSObservabilityAdminLogsCentralizationServiceRolePolicy**
service-linked role trusts the
`logs-centralization.observabilityadmin.amazonaws.com` service to
assume the role.

## Creating a service-linked role for

CloudWatch

You do not need to manually create any of these service-linked roles. The first
time you create an alarm in the AWS Management Console, the IAM CLI, or the IAM API,
CloudWatch creates AWSServiceRoleForCloudWatchEvents and
**AWSServiceRoleForCloudWatchAlarms_ActionSSM** for you.

The first time that you enable service and topology discovery, Application Signals
creates **AWSServiceRoleForCloudWatchApplicationSignals** for
you.

When you first enable an account to be a monitoring account for cross-account
cross-Region functionality, CloudWatch creates
**AWSServiceRoleForCloudWatchCrossAccount** for you.

When you first create an alarm that uses the `DB_PERF_INSIGHTS` metric
math function, CloudWatch creates
**AWSServiceRoleForCloudWatchMetrics_DbPerfInsights** for
you.

For more information, see [Creating a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the
_IAM User Guide_.

## Editing a service-linked role for

CloudWatch

CloudWatch does not allow you to edit the
**AWSServiceRoleForCloudWatchEvents**,
**AWSServiceRoleForCloudWatchAlarms_ActionSSM**,
**AWSServiceRoleForCloudWatchCrossAccount**, or
**AWSServiceRoleForCloudWatchMetrics_DbPerfInsights** roles.
After you create these roles, you cannot change their names because various entities
might reference these roles. However, you can edit the description of these roles
using IAM.

### Editing a service-linked

role description (IAM console)

You can use the IAM console to edit the description of a service-linked
role.

###### To edit the description of a service-linked role (console)

1. In the navigation pane of the IAM console, choose
   **Roles**.
2. Choose the name of the role to modify.
3. To the far right of **Role description**, choose
   **Edit**.
4. Type a new description in the box, and choose
   **Save**.

### Editing a service-linked role

description (AWS CLI)

You can use IAM commands from the AWS Command Line Interface to edit the description of a
service-linked role.

###### To change the description of a service-linked role (AWS CLI)

1. (Optional) To view the current description for a role, use the
   following commands:

```
`$` `aws iam get-role --role-name `role-name``
```

Use the role name, not the ARN, to refer to roles with the AWS CLI
commands. For example, if a role has the following ARN:
`arn:aws:iam::123456789012:role/myrole`, you refer to
the role as `myrole`. 2. To update a service-linked role's description, use the following
command:

```
`$` `aws iam update-role-description --role-name `role-name` --description `description``
```

### Editing a service-linked role

description (IAM API)

You can use the IAM API to edit the description of a service-linked
role.

###### To change the description of a service-linked role (API)

1. (Optional) To view the current description for a role, use the
   following command:

[GetRole](../../../IAM/latest/APIReference/API_GetRole.md "../../../IAM/latest/APIReference/API_GetRole.md") 2. To update a role's description, use the following command:

[UpdateRoleDescription](../../../IAM/latest/APIReference/API_UpdateRoleDescription.md "../../../IAM/latest/APIReference/API_UpdateRoleDescription.md")

## Deleting a service-linked role for

CloudWatch

If you no longer have alarms that automatically stop, terminate, or reboot EC2
instances, we recommend that you delete the AWSServiceRoleForCloudWatchEvents
role.

If you not longer have alarms that perform Systems Manager OpsCenter actions, we recommend
that you delete the AWSServiceRoleForCloudWatchAlarms_ActionSSM role.

If you delete all alarms that use the `DB_PERF_INSIGHTS` metric math
function, we recommend that you delete the
**AWSServiceRoleForCloudWatchMetrics_DbPerfInsights**
service-linked role.

That way you don’t have an unused entity that is not actively monitored or
maintained. However, you must clean up your service-linked role before you can
delete it.

### Cleaning up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first
confirm that the role has no active sessions and remove any resources used by
the role.

###### To check whether the service-linked role has an active session in the

IAM console

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. Choose the
   name (not the check box) of the AWSServiceRoleForCloudWatchEvents role.
3. On the **Summary** page for the selected role, choose
   **Access Advisor** and review the recent activity
   for the service-linked role.

###### Note

If you are unsure whether CloudWatch is using the AWSServiceRoleForCloudWatchEvents
role, try to delete the role. If the service is using the role, then
the deletion fails and you can view the Regions where the role is
being used. If the role is being used, then you must wait for the
session to end before you can delete the role. You cannot revoke the
session for a service-linked role.

### Deleting a

service-linked role (IAM console)

You can use the IAM console to delete a service-linked role.

###### To delete a service-linked role (console)

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**. Select the
   check box next to the name of the role you want to delete, not the name
   or row itself.
3. For **Role actions**, choose **Delete
   role**.
4. In the confirmation dialog box, review the service last accessed data,
   which shows when each of the selected roles last accessed an AWS
   service. This helps you to confirm whether the role is currently active.
   To proceed, choose **Yes, Delete**.
5. Watch the IAM console notifications to monitor the progress of the
   service-linked role deletion. Because the IAM service-linked role
   deletion is asynchronous, the deletion task can succeed or fail after
   you submit the role for deletion. If the task fails, choose
   **View details** or **View
   Resources** from the notifications to learn why the
   deletion failed. If the deletion fails because there are resources in
   the service that are being used by the role, then the reason for the
   failure includes a list of resources.

### Deleting a service-linked

role (AWS CLI)

You can use IAM commands from the AWS Command Line Interface to delete a service-linked
role.

###### To delete a service-linked role (AWS CLI)

1. Because a service-linked role cannot be deleted if it is being used or
   has associated resources, you must submit a deletion request. That
   request can be denied if these conditions are not met. You must capture
   the `deletion-task-id` from the response to check the status
   of the deletion task. Type the following command to submit a
   service-linked role deletion request:

```
`$` `aws iam delete-service-linked-role --role-name `service-linked-role-name``
```

2. Type the following command to check the status of the deletion
   task:

```
`$` `aws iam get-service-linked-role-deletion-status --deletion-task-id `deletion-task-id``
```

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or
`FAILED`. If the deletion fails, the call returns the
reason that it failed so that you can troubleshoot.

### Deleting a service-linked

role (IAM API)

You can use the IAM API to delete a service-linked role.

###### To delete a service-linked role (API)

1. To submit a deletion request for a service-linked role, call [DeleteServiceLinkedRole](../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md "../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md"). In the request, specify the role
   name that you want to delete.

Because a service-linked role cannot be deleted if it is being used or
has associated resources, you must submit a deletion request. That
request can be denied if these conditions are not met. You must capture
the `DeletionTaskId` from the response to check the status of
the deletion task. 2. To check the status of the deletion, call [GetServiceLinkedRoleDeletionStatus](../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md "../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md"). In the request, specify
the `DeletionTaskId`.

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or
`FAILED`. If the deletion fails, the call returns the
reason that it failed so that you can troubleshoot.

## CloudWatch updates to AWS service-linked

roles

View details about updates to AWS managed policies for CloudWatch since this service
began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the CloudWatch Document history page.

| Change                                                                                                                                                                                  | Description                                                                                                                                                                                                                                                                                                                                         | Date               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| [AWSObservabilityAdminLogsCentralizationServiceRolePolicy](#service-linked-role-logscentralization "#service-linked-role-logscentralization") – New service-linked role policy.         | Added information about the [AWSObservabilityAdminLogsCentralizationServiceRolePolicy](#service-linked-role-logscentralization "#service-linked-role-logscentralization") that grants CloudWatch the permissions necessary to enable and manage telemetry configurations for AWS resources based on telemetry rules.                                | September 5, 2025  |
| [AWSObservabilityAdminTelemetryEnablementServiceRolePolicy](#service-linked-role-telemetry-enablement "#service-linked-role-telemetry-enablement") – New service-linked role policy.    | Added information about the [AWSObservabilityAdminTelemetryEnablementServiceRolePolicy](#service-linked-role-telemetry-enablement "#service-linked-role-telemetry-enablement") that grants CloudWatch the permissions necessary to enable and manage telemetry configurations for AWS resources based on telemetry rules.                           | July 17, 2025      |
| [AWSServiceRoleForCloudWatchApplicationSignals](#service-linked-role-signals "#service-linked-role-signals") – Update to permissions of service-linked role policy                      | Updated the [CloudWatchApplicationSignalsServiceRolePolicy](using-service-linked-roles.md#service-linked-role-signals "using-service-linked-roles.md#service-linked-role-signals") to exclude time windows from impacting the SLO attainment rate, error budget, and burn rate metrics. CloudWatch can retrieve exclusion windows on behalf of you. | March 13, 2025     |
| [AWSServiceRoleForObservabilityAdmin](#service-linked-role-telemetry-config "#service-linked-role-telemetry-config") – New service-linked role                                          | CloudWatch added this new service-linked role and corresponding managed policy, AWSObservabilityAdminServiceRolePolicy, to support resource and telemetry config discovery for AWS Organizations.                                                                                                                                                   | November 26, 2024  |
| [AWSServiceRoleForCloudWatchApplicationSignals](#service-linked-role-signals "#service-linked-role-signals") – Update to permissions of service-linked role policy                      | CloudWatch add more log groups to the scope of the `logs:StartQuery` and `logs:GetQueryResults` permissions granted by this role.                                                                                                                                                                                                                   | April 24, 2024     |
| [AWSServiceRoleForCloudWatchApplicationSignals](#service-linked-role-signals "#service-linked-role-signals") – New service-linked role                                                  | CloudWatch added this new service-linked role to allow CloudWatch Application Signals to collect CloudWatch Logs data, X-Ray trace data, CloudWatch metrics data, and tagging data from applications that you have enabled for CloudWatch Application Signals.                                                                                      | November 9, 2023   |
| [AWSServiceRoleForCloudWatchMetrics_DbPerfInsights](#service-linked-role-permissions-dbperfinsights "#service-linked-role-permissions-dbperfinsights") – New service-linked role        | CloudWatch added this new service-linked role to allow CloudWatch to fetch Performance Insights metrics for alarming and snapshotting. An IAM policy is attached to this role, and the policy grants permission to CloudWatch to fetch Performance Insights metrics on your behalf.                                                                 | September 13, 2023 |
| [AWSServiceRoleForCloudWatchAlarms_ActionSSMIncidents](#service-linked-role-permissions-incident-manager "#service-linked-role-permissions-incident-manager") – New service-linked role | CloudWatch added a new service-linked role to allow CloudWatch to create incidents in AWS Systems Manager Incident Manager.                                                                                                                                                                                                                         | April 26, 2021     |
| CloudWatch started tracking changes                                                                                                                                                     | CloudWatch started tracking changes for its service-linked roles.                                                                                                                                                                                                                                                                                   | April 26, 2021     |
