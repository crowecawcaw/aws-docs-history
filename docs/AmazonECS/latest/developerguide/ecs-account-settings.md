# Access Amazon ECS features with account settings

You can go into Amazon ECS account settings to opt in or out of specific features. For each
AWS Region, you can opt in to, or opt out of, each account setting at the account-level or
for a specific user or role.

You might want to opt in or out of specific features if any of the following is relevant
to you:

- A user or role can opt in or opt out specific account settings for their
  individual account.
- A user or role can set the default opt-in or opt-out setting for all users on the
  account.
- The root user or a user with administrator privileges can opt in to, or opt out of,
  any specific role or user on the account. If the account setting for the root user is
  changed, it sets the default for all the users and roles that no individual account
  setting was selected for.

###### Note

Federated users assume the account setting of the root user and can't have explicit
account settings set for them separately.

The following account settings are available. You must separately opt-in and opt-out to
each account setting.

| Resource name                                                                 | Learn more                                                                                                    |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `containerInsights`                                                           | [Container Insights](#container-insights-setting "#container-insights-setting")                               |
| `serviceLongArnFormat``taskLongArnFormat`<br>`containerInstanceLongArnFormat` | [Amazon Resource Names (ARNs) and IDs](#ecs-resource-ids "#ecs-resource-ids")                                 |
| `tagResourceAuthorization`                                                    | [Tagging authorization](#tag-resources-setting "#tag-resources-setting")                                      |
| `fargateFIPSMode`                                                             | [AWS Fargate Federal Information Processing Standard<br>(FIPS-140) compliance](#fips-setting "#fips-setting") |
| `fargateTaskRetirementWaitPeriod`                                             | [AWS Fargate task retirement wait<br>time](#fargate-retirement-wait-time "#fargate-retirement-wait-time")     |
| `fargateEventWindows`                                                         | [AWS Fargate task retirements using EC2 event windows](#fargate-event-windows "#fargate-event-windows")       |
| `guardDutyActivate`                                                           | [Runtime Monitoring (Amazon GuardDuty integration)](#guard-duty-integration "#guard-duty-integration")        |
| `dualStackIPv6`                                                               | [Dual stack IPv6 VPC](#dual-stack-setting "#dual-stack-setting")                                              |
| `awsvpcTrunking`                                                              | [Increase Linux container instance network<br>interfaces](#vpc-trunking-setting "#vpc-trunking-setting")      |
| `defaultLogDriverMode`                                                        | [Default log driver mode](#default-log-driver-mode "#default-log-driver-mode")                                |

## Amazon Resource Names (ARNs) and IDs

When Amazon ECS resources are created, each resource is assigned a unique Amazon Resource
Name (ARN) and resource identifier (ID). If you use a command line tool or the Amazon ECS API
to work with Amazon ECS, resource ARNs or IDs are required for certain commands. For example,
if you use the [stop-task](../../../cli/latest/reference/ecs/stop-task.md "../../../cli/latest/reference/ecs/stop-task.md") AWS CLI
command to stop a task, you must specify the task ARN or ID in the command.

Amazon ECS introduced a new format for Amazon Resource Names (ARNs) and resource IDs for
Amazon ECS services, tasks, and container instances. The opt-in status for each resource type
determines the Amazon Resource Name (ARN) format the resource uses. You must opt in to
the new ARN format to use features such as resource tagging for that resource type.

You can opt in to and opt out of the new Amazon Resource Name (ARN) and resource ID
format on a per-Region basis. Currently, any new account created is opted in by
default.

You can opt in or opt out of the new Amazon Resource Name (ARN) and resource ID format
at any time. After you opt in, any new resources that you create use the new
format.

###### Note

A resource ID doesn't change after it's created. Therefore, opting in or out of
the new format doesn't affect your existing resource IDs.

The following sections describe how ARN and resource ID formats are changing. For more
information about the transition to the new formats, see [Amazon Elastic Container Service FAQ](https://aws.amazon.com/ecs/faqs/ "https://aws.amazon.com/ecs/faqs/").

###### Amazon Resource Name (ARN) format

Some resources have a user-friendly name, such as a service named
`production`. In other cases, you must specify a resource using the
Amazon Resource Name (ARN) format. The new ARN format for Amazon ECS tasks, services, and
container instances includes the cluster name. For information about opting in to
the new ARN format, see [Modifying Amazon ECS account
settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md").

The following table shows both the current format and the new format for each resource
type.

| Resource type      | ARN                                                                                                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Container instance | Current:<br>`arn:aws:ecs:`region`:`aws_account_id`:container-instance/`container-instance-id``<br>New:<br>`arn:aws:ecs:`region`:`aws_account_id`:container-instance/`cluster-name`/`container-instance-id`` |
| Amazon ECS service | Current:<br>`arn:aws:ecs:`region`:`aws_account_id`:service/`service-name``<br>New:<br>`arn:aws:ecs:`region`:`aws_account_id`:service/`cluster-name`/`service-name``                                         |
| Amazon ECS task    | Current:<br>`arn:aws:ecs:`region`:`aws_account_id`:task/`task-id``<br>New:<br>`arn:aws:ecs:`region`:`aws_account_id`:task/`cluster-name`/`task-id``                                                         |

###### Resource ID length

A resource ID takes the form of a unique combination of letters and numbers. New
resource ID formats include shorter IDs for Amazon ECS tasks and container instances. The
current resource ID format is 36 characters long. The new IDs are in a 32-character
format that doesn't include any hyphens. For information about opting in to the new
resource ID format, see [Modifying Amazon ECS account
settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md").

The default is `enabled`.

Only resources launched after opting in receive the new ARN and resource ID format.
All existing resources aren't affected. For Amazon ECS services and tasks to transition to
the new ARN and resource ID formats, you must recreate the service or task. To
transition a container instance to the new ARN and resource ID format, the container
instance must be drained and a new container instance must be launched and registered to
the cluster.

###### Note

Tasks launched by an Amazon ECS service can only receive the new ARN and resource ID
format if the service was created on or after November 16, 2018, and the user who
created the service has opted in to the new format for tasks.

## ARN and resource ID format timeline

The timeline for the opt-in and opt-out periods for the new Amazon Resource Name (ARN)
and resource ID format for Amazon ECS resources ended on April 1, 2021. By default, all
accounts are opted in to the new format. All new resources created receive the new
format, and you can no longer opt out.

## Container Insights

On December 2, 2024, AWS released Container Insights with enhanced observability for
Amazon ECS. This version supports enhanced observability for Amazon ECS clusters using Fargate Amazon ECS Managed Instances, and EC2. After you configure Container Insights with enhanced
observability on Amazon ECS, Container Insights auto-collects detailed infrastructure
telemetry from cluster level down to the container level in your environment and
displays your data in dashboards that show you a variety of metrics and dimensions. You
can then use these out-of-the-box dashboards on the Container Insights console to better
understand your container health and performance, and to mitigate issues faster by
identifying anomalies.

We recommend that you use Container Insights with enhanced observability instead of
Container Insights because it provides detailed visibility in your container
environment, reducing the mean time to resolution. For more information, see [Amazon ECS Container Insights with enhanced observability metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-enhanced-observability-metrics-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-enhanced-observability-metrics-ECS.md") in the
_Amazon CloudWatch User Guide_.

The default for the `containerInsights` account setting is
`disabled`.

### Container Insights with

enhanced observability

Use the following command to turn on Container Insights with enhanced
observability.

Set the `containerInsights` account setting to
`enhanced`.

```
aws ecs put-account-setting --name containerInsights --value enhanced
```

Example output

```
{
    "setting": {
        "name": "containerInsights",
        "value": "enhanced",
        "principalArn": "arn:aws:iam::123456789012:johndoe",
         "type": user
    }
}
```

After you set this account setting, all new clusters automatically use Container
Insights with enhanced observability. Use the `update-cluster-settings`
command to add Container Insights with enhanced observability to an existing
cluster, or to upgrade a cluster from Container Insights to Container Insights with
enhanced observability.

```
aws ecs update-cluster-settings --cluster `cluster-name` --settings name=containerInsights,value=enhanced
```

You can also use the console to configure Container Insights with enhanced
observability. For more information, see [Modifying Amazon ECS account
settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md").

### Container Insights

When you set the `containerInsights` account setting to
`enabled`, all new clusters have Container Insights enabled by
default. You can modify existing clusters by using
`update-cluster-settings`.

To use Container Insights, set the `containerInsights` account setting
to `enabled`. Use the following command to turn on Container
Insights.

```
aws ecs put-account-setting --name containerInsights --value enabled
```

Example output

```
{
    "setting": {
        "name": "containerInsights",
        "value": "enabled",
        "principalArn": "arn:aws:iam::123456789012:johndoe",
         "type": user
    }
}
```

When you set the `containerInsights` account setting to
`enabled`, all new clusters have Container Insights enabled by
default. Use the `update-cluster-settings` command to add Container
Insights to an existing cluster.

```
aws ecs update-cluster-settings --cluster `cluster-name` --settings name=containerInsights,value=enabled
```

You can also use the console to configure Container Insights. For more information,
see [Modifying Amazon ECS account
settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md").

## AWS Fargate Federal Information Processing Standard

(FIPS-140) compliance

Fargate supports the Federal Information Processing Standard (FIPS-140) which
specifies the security requirements for cryptographic modules that protect sensitive
information. It is the current United States and Canadian government standard, and is
applicable to systems that are required to be compliant with Federal Information
Security Management Act (FISMA) or Federal Risk and Authorization Management Program
(FedRAMP).

The resource name is `fargateFIPSMode`.

The default is `disabled`.

You must turn on Federal Information Processing Standard (FIPS-140) compliance on
Fargate. For more information, see [AWS Fargate Federal Information Processing Standard
(FIPS-140)](ecs-fips-compliance.md "ecs-fips-compliance.md").

###### Important

The `fargateFIPSMode` account setting can only be changed using either
the Amazon ECS API or the AWS CLI. For more information, see [Modifying Amazon ECS account
settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md").

Run `put-account-setting-default` with the `fargateFIPSMode`
option set to `enabled`. For more information, see, [put-account-setting-default](../../../cli/latest/reference/ecs/put-account-setting-default.md "../../../cli/latest/reference/ecs/put-account-setting-default.md") in the _Amazon Elastic Container Service API Reference_.

- You can use the following command to turn on FIPS-140 compliance.

```
aws ecs put-account-setting-default --name fargateFIPSMode --value enabled
```

Example output

```
{
    "setting": {
        "name": "fargateFIPSMode",
        "value": "enabled",
        "principalArn": "arn:aws:iam::123456789012:root",
         "type": user
    }
}
```

You can run `list-account-settings` to view the current FIPS-140 compliance
status. Use the `effective-settings` option to view the account level
settings.

```
aws ecs list-account-settings --effective-settings
```

## Tagging authorization

Amazon ECS is introducing tagging authorization for resource creation. Users must have
tagging permissions for actions that create the resource, such as
`ecsCreateCluster`. When you create a resource and specify tags for that
resource, AWS performs additional authorization to verify that there are permissions
to create tags. Therefore, you must grant explicit permissions to use the
`ecs:TagResource` action. For more information, see [Grant permission to tag resources on
creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md").

In order to opt in to tagging authorization, run
`put-account-setting-default` with the
`tagResourceAuthorization` option set to `on`. For more
information, see, [put-account-setting-default](../../../cli/latest/reference/ecs/put-account-setting-default.md "../../../cli/latest/reference/ecs/put-account-setting-default.md") in the _Amazon Elastic Container Service API Reference_. You can run `list-account-settings` to view
the current tagging authorization status.

- You can use the following command to enable tagging authorization.

```
aws ecs put-account-setting-default --name tagResourceAuthorization --value on --region `region`
```

Example output

```
{
    "setting": {
        "name": "tagResourceAuthorization",
        "value": "on",
        "principalArn": "arn:aws:iam::123456789012:root",
        "type": user
    }
}
```

After you enable tagging authorization, you must configure the appropriate permissions
to allow users to tag resources on creation. For more information, see [Grant permission to tag resources on
creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md").

You can run `list-account-settings` to view the current tagging
authorization status. Use the `effective-settings` option to view the account
level settings.

```
aws ecs list-account-settings --effective-settings
```

## Tagging authorization timeline

You can confirm whether tagging authorization is active by running
`list-account-settings` to view the `tagResourceAuthorization`
value. When the value is `on`, it means that the tagging authorization is in
use. For more information, see, [list-account-settings](../../../cli/latest/reference/ecs/list-account-settings.md "../../../cli/latest/reference/ecs/list-account-settings.md") in the _Amazon Elastic Container Service API Reference_.

The following are the important dates related to tagging authorization.

- April 18, 2023 – Tagging authorization is introduced. All new and
  existing accounts must opt in to use the feature. You can opt in to start using
  tagging authorization. By opting in, you must grant the appropriate
  permissions.
- February 9, 2024 - March 6, 2024 – All new accounts and non-impacted
  existing accounts have tagging authorization on by default. You can enable or
  disable the `tagResourceAuthorization` account setting to verify your
  IAM policy.

AWS has notified impacted accounts.

To disable the feature, run `put-account-setting-default` with the
`tagResourceAuthorization` option set to `off`.

- March 7, 2024 – If you have enabled tagging authorization, you can no longer
  disable the account setting.

We recommend that you complete your IAM policy testing before this
date.

- March 29, 2024 – All accounts use tagging authorization. The account-level
  setting will no longer be available in the Amazon ECS console or AWS CLI.

## AWS Fargate task retirement wait

time

AWS sends out notifications when you have Fargate tasks running on a platform
version revision marked for retirement. For more information, see [Task retirement and maintenance for AWS Fargate on Amazon ECS](task-maintenance.md "task-maintenance.md") .

AWS is responsible for patching and maintaining the underlying infrastructure for
AWS Fargate. When AWS determines that a security or infrastructure update is needed for
an Amazon ECS task hosted on Fargate, the tasks need to be stopped and new tasks launched
to replace them. You can configure the wait period before tasks are retired for
patching. You have the option to retire the task immediately, to wait 7 calendar days,
or to wait 14 calendar days.

This setting is at the account-level.

You can configure the time that Fargate starts the task retirement.
The default wait period is 7 days. For workloads
that require immediate application of the updates, choose the immediate setting (`0`). If you need more time,
configure the `7`, or `14` day option.

We recommend that you choose a shorter waiting period in order to pick up newer platform versions revisions sooner.

Configure the wait period by running
`put-account-setting-default` or `put-account-setting` as the root user or an administrative user. Use the
`fargateTaskRetirementWaitPeriod` option for the `name` and the `value` option set to one of the following values:

- `0` - AWS sends the notification, and immediately starts to retire the affected tasks.
- `7` - AWS sends the notification, and waits 7 calendar days before starting to retire the affected tasks. This is the default.
- `14` - AWS sends the notification, and waits 14 calendar days before starting to retire the affected tasks.

For more information, see, [put-account-setting-default](../../../cli/latest/reference/ecs/put-account-setting-default.md "../../../cli/latest/reference/ecs/put-account-setting-default.md") and [put-account-setting](../../../cli/latest/reference/ecs/put-account-setting.md "../../../cli/latest/reference/ecs/put-account-setting.md") in the _Amazon Elastic Container Service API Reference_.

You can run the following command to set the wait period to 14 days.

```
aws ecs put-account-setting-default --name fargateTaskRetirementWaitPeriod --value 14
```

Example output

```
{
    "setting": {
        "name": "fargateTaskRetirementWaitPeriod",
        "value": "14",
        "principalArn": "arn:aws:iam::123456789012:root",
        "type: user"
    }
}
```

You can run `list-account-settings` to view the current Fargate task
retirement wait time. Use the `effective-settings` option.

```
aws ecs list-account-settings --effective-settings
```

## AWS Fargate task retirements using EC2 event windows

AWS is responsible for patching and maintaining the underlying infrastructure for AWS Fargate. When
AWS determines that a security or infrastructure update is needed for an Amazon ECS task hosted on Fargate, the
tasks need to be stopped and new tasks launched to replace them. By enabling this account setting AWS Fargate will use
EC2 event windows to determine the time and day when your tasks will be retired. Note that this is a one time enablement for an account.

To enable usage of EC2 event windows for Fargate task retirements, you can use the following CLI command:

```
aws ecs put-account-setting-default --name fargateEventWindows --value enabled
```

This is an account level setting. You can associate EC2 event windows with Fargate tasks at the account,
cluster and service levels using the following instance tags:

- `aws:ecs:serviceArn` : for service tasks
- `aws:ecs:clusterArn` : for tasks belonging to a cluster
- `aws:ecs:fargateTask` : set to true to target all Fargate tasks in the account

To learn more about how [Amazon EC2 event windows](../../../AWSEC2/latest/UserGuide/event-windows.md "../../../AWSEC2/latest/UserGuide/event-windows.md") work for your Amazon ECS tasks running on Fargate, see
[Step 1: Set the task wait time or use Amazon EC2 event windows](prepare-task-retirement.md#prepare-task-retirement-set-time "prepare-task-retirement.md#prepare-task-retirement-set-time")

## Increase Linux container instance network

interfaces

Each Amazon ECS task that uses the `awsvpc` network mode receives its own
elastic network interface (ENI), which is attached to the container
instance that hosts it. There is a default limit to the number of network interfaces
that can be attached to an Amazon EC2 instance, and the primary network interface counts as
one. For example, by default a `c5.large` instance may have up to three ENIs
attached to it. The primary network interface for the instance counts as one, so you can
attach an additional two ENIs to the instance. Because each task using the
`awsvpc` network mode requires an ENI, you can typically
only run two such tasks on this instance type.

Amazon ECS supports launching container instances with increased ENI density
using supported Amazon EC2 instance types. When you use these instance types and turn on the
`awsvpcTrunking` account setting, additional ENIs are available on newly
launched container instances. This configuration allows you to place more tasks on each
container instance.

For example, a `c5.large` instance with `awsvpcTrunking` has an
increased ENI limit of twelve. The container instance will have the
primary network interface and Amazon ECS creates and attaches a "trunk" network interface to
the container instance. So this configuration allows you to launch ten tasks on the
container instance instead of the current two tasks.

## Runtime Monitoring (Amazon GuardDuty integration)

Runtime Monitoring is an intelligent threat detection service that protects workloads running
on Fargate and EC2 container instances by continuously monitoring AWS log and
networking activity to identify malicious or unauthorized behavior.

The `guardDutyActivate` parameter is read-only in Amazon ECS and indicates whether
Runtime Monitoring is turned on or off by your security administrator in your
Amazon ECS account. GuardDuty controls this account setting on your behalf. For more information, see [Protecting Amazon ECS workloads with Runtime Monitoring](ecs-guard-duty-integration.md "ecs-guard-duty-integration.md").

You can run `list-account-settings` to view the current GuardDuty integration
setting.

```
aws ecs list-account-settings
```

Example output

```
{
    "setting": {
        "name": "guardDutyActivate",
        "value": "on",
        "principalArn": "arn:aws:iam::123456789012:doej",
        "type": aws-managed"
    }
}
```

## Dual stack IPv6 VPC

Amazon ECS supports providing tasks with an IPv6 address in addition to the primary private
IPv4 address.

For tasks to receive an IPv6 address, the task must use the `awsvpc`
network mode, must be launched in a VPC configured for dual-stack mode, and the
`dualStackIPv6` account setting must be enabled. For more information
about other requirements, see [Using a VPC in dual-stack
mode](task-networking-awsvpc.md#task-networking-vpc-dual-stack "task-networking-awsvpc.md#task-networking-vpc-dual-stack") for EC2 capacity, [Using a VPC in
dual-stack mode](managed-instances-awsvpc-mode.md#managed-instance-networking-vpc-dual-stack "managed-instances-awsvpc-mode.md#managed-instance-networking-vpc-dual-stack") for Amazon ECS Managed Instances capacity, and [Using a VPC in dual-stack
mode](fargate-task-networking.md#fargate-task-networking-vpc-dual-stack "fargate-task-networking.md#fargate-task-networking-vpc-dual-stack") for Fargate capacity.

###### Important

The `dualStackIPv6` account setting can only be changed using either
the Amazon ECS API or the AWS CLI. For more information, see [Modifying Amazon ECS account
settings](ecs-modifying-longer-id-settings.md "ecs-modifying-longer-id-settings.md").

If you had a running task using the `awsvpc` network mode in an IPv6
enabled subnet between the dates of October 1, 2020 and November 2, 2020, the default
`dualStackIPv6` account setting in the Region that the
task was running in is `disabled`. If that condition isn't met, the default
`dualStackIPv6` setting in the Region is
`enabled`.

The default is `disabled`.

## Default log driver mode

Amazon ECS supports setting a default delivery mode of log messages from a container to the
chosen log driver. The delivery mode affects application stability when the flow of logs
from the container to the log driver is interrupted.

The `defaultLogDriverMode` setting supports two values:
`blocking` and `non-blocking`. For more information about
these delivery modes, see [LogConfiguration](../APIReference/API_LogConfiguration.md "../APIReference/API_LogConfiguration.md") in the _Amazon Elastic Container Service API Reference_.

If you don't specify a delivery mode in your container definition's
`logConfiguration`, the mode you specify using this account setting will
be used as the default.

The default delivery mode is `non-blocking`.

###### Note

On June 25, 2025, Amazon ECS changed the default log driver mode from `blocking` to `non-blocking` to prioritize task availability over logging. To continue using the `blocking` mode after this change, do one of the following:

- Set the `mode` option in your container definition's `logConfiguration` as `blocking`.
- Set the `defaultLogDriverMode` account setting to `blocking`.

To set a default log driver mode to `blocking`, you can run the
following command.

```
aws ecs put-account-setting-default --name defaultLogDriverMode --value "blocking"
```
