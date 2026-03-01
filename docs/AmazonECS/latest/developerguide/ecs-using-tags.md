# Tagging Amazon ECS resources

To help you manage your Amazon ECS resources, you can optionally assign your own metadata to
each resource using _tags_. Each _tag_
consists of a _key_ and an optional _value_.

You can use tags to categorize your Amazon ECS resources in different ways, for example, by
purpose, owner, or environment. This is useful when you have many resources of the same
type. You can quickly identify a specific resource based on the tags that you assigned to
it. For example, you can define a set of tags for your account's Amazon ECS container instances.
This helps you track each instance's owner and stack level.

You can use tags for your Cost and Usage reports. You can use these reports to analyze the
cost and usage of your Amazon ECS resources. For more information, see [Amazon ECS usage reports](usage-reports.md "usage-reports.md").

###### Warning

There are many APIs that return tag keys and their values. Denying access to
`DescribeTags` doesn’t automatically deny access to tags returned by
other APIs. As a best practice, we recommend that you do not include sensitive data in
your tags.

We recommend that you devise a set of tag keys that meets your needs for each resource
type. You can use a consistent set of tag keys for easier management of your resources. You
can search and filter the resources based on the tags you add.

Tags don't have any semantic meaning to Amazon ECS and are interpreted strictly as a string of
characters. You can edit tag keys and values, and you can remove tags from a resource at any
time. You can set the value of a tag to an empty string, but you can't set the value of a
tag to null. If you add a tag that has the same key as an existing tag on that resource, the
new value overwrites the earlier value. When you delete a resource, any tags for the
resource are also deleted.

If you use AWS Identity and Access Management (IAM), you can control which users in your AWS account have
permission to manage tags.

## How resources are tagged

There are multiple ways that Amazon ECS tasks, services, task definitions, and clusters are
tagged:

- A user manually tags a resource by using the AWS Management Console, Amazon ECS API, the
  AWS CLI, or an AWS SDK.
- A user creates a service or runs a standalone task and selects the
  Amazon ECS-managed tags option.

Amazon ECS automatically tags all newly launched tasks. For more information, see
[Amazon ECS-managed tags](#managed-tags "#managed-tags").

- A user creates a resource using the console. The console automatically tags
  the resources.

These tags are returned in the AWS CLI, and AWS SDK responses and are
displayed in the console. You cannot modify or delete these tags.

For information about the added tags, see the **Tags
automatically added by the console** column in the **Tagging support for Amazon ECS resources** table.

If you specify tags when you create a resource and the tags can't be applied, Amazon ECS
rolls back the creation process. This ensures that resources are either created with
tags or not created at all, and that no resources are left untagged at any time. By
tagging resources while they're being created, you can eliminate the need to run custom
tagging scripts after resource creation.

The following table describes the Amazon ECS resources that support tagging.

| Resource                       | Supports tags                                                                          | Supports tag propagation                                                                                                                                                                                                                                                                         | Tags automatically added by the console                                                                                                                                                                                                     |
| ------------------------------ | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon ECS tasks               | Yes                                                                                    | Yes, from the task definition.                                                                                                                                                                                                                                                                   | _Key_:<br>`aws:ecs:clusterName`<br>_Value_:<br>`cluster-name`                                                                                                                                                                               |
| Amazon ECS services            | Yes                                                                                    | Yes, from either the task definition or the service to the tasks<br>in the service.                                                                                                                                                                                                              | _Key:_<br>`ecs:service:stackId`<br>_Value_<br>`arn:aws:cloudformation:`arn``                                                                                                                                                                |
| Amazon ECS task sets           | Yes                                                                                    | No                                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                         |
| Amazon ECS task definitions    | Yes                                                                                    | No                                                                                                                                                                                                                                                                                               | _Key_:<br>`ecs:taskDefinition:createdFrom`<br>_Value_:<br>`ecs-console-v2`                                                                                                                                                                  |
| Amazon ECS clusters            | Yes                                                                                    | No                                                                                                                                                                                                                                                                                               | _Key_: `aws:cloudformation:logical-id`<br>_Value_: `ECSCluster`<br>_Key_:<br>`aws:cloudformation:stack-id`_Value_:<br>`arn:aws:cloudformation:`arn``*Key*:<br>`aws:cloudformation:stack-name`*Value*:<br>`ECS-Console-V2-Cluster-`EXAMPLE`` |
| Amazon ECS container instances | Yes                                                                                    | Yes, from the Amazon EC2 instance. For more information, see [Adding tags to an Amazon EC2 container instance for Amazon ECS](instance-details-tags.md "instance-details-tags.md").                                                                                                              | N/A                                                                                                                                                                                                                                         |
| Amazon ECS External instances  | Yes                                                                                    | No                                                                                                                                                                                                                                                                                               | N/A                                                                                                                                                                                                                                         |
| Amazon ECS capacity provider   | Yes. You cannot tag the predefined `FARGATE` and<br>`FARGATE_SPOT` capacity providers. | Yes, only from capacity providers for Amazon ECS Managed Instances. You can<br>propagate tags from the capacity provider for Amazon ECS Managed Instances to all<br>resources managed by the provider such as Amazon EC2 instances, launch<br>template, Elastic Network Interfaces, and volumes. | N/A                                                                                                                                                                                                                                         |

## Tagging resources on creation

The following resources support tagging on creation using the Amazon ECS API, AWS CLI, or
AWS SDK:

- Amazon ECS tasks
- Amazon ECS services
- Amazon ECS task definition
- Amazon ECS task sets
- Amazon ECS clusters
- Amazon ECS container instances
- Amazon ECS capacity providers

Amazon ECS has the option to use tagging authorization for resource creation. When the
AWS account is configured for tagging authorization, users must have permissions for
actions that create the resource, such as `ecsCreateCluster`. If you specify
tags in the resource-creating action, AWS performs additional authorization to verify
if users or roles have permissions to create tags. Therefore, you must grant explicit
permissions to use the `ecs:TagResource` action. For more information, see
[Grant permission to tag resources on creation](supported-iam-actions-tagging.md "supported-iam-actions-tagging.md"). For information about how to
configure the option, see [Tagging authorization](ecs-account-settings.md#tag-resources-setting "ecs-account-settings.md#tag-resources-setting").

## Restrictions

The following restrictions apply to tags:

- A maximum of 50 tags can be associated with a resource.
- Tag keys can't be repeated for one resource. Each tag key must be unique, and
  can only have one value.
- Keys can be up to 128 characters long in UTF-8.
- Values can be up to 256 characters long in UTF-8.
- If multiple AWS services and resources use your tagging schema, limit the
  types of characters you use. Some services might have restrictions on allowed
  characters. Generally, allowed characters are letters, numbers, spaces, and the
  following characters: `+`
  `-`
  `=`
  `.`
  `_`
  `:`
  `/`
  `@`.
- Tag keys and values are case sensitive.
- You can't use `aws:`, `AWS:`, or any upper or lowercase
  combination of such as a prefix for either keys or values. These are reserved
  only for AWS use. You can't edit or delete tag keys or values with this
  prefix. Tags with this prefix don't count against your tags-per-resource
  limit.

## Amazon ECS-managed tags

When you use Amazon ECS-managed tags, Amazon ECS automatically tags all newly launched tasks and
any Amazon EBS volumes attached to the tasks with the cluster information and either the
user-added task definition tags or the service tags. The following describes the added
tags:

- Standalone tasks – a tag with a _Key_ as
  `aws:ecs:clusterName` and a _Value_ set to the
  cluster name. All task definition tags that were added by users. An Amazon EBS volume
  attached to a standalone task will receive the tag with a
  _Key_ as `aws:ecs:clusterName` and a
  _Value_ set to the cluster name. For more information
  about Amazon EBS volume tagging, see [Tagging Amazon EBS volumes](specify-ebs-config.md#ebs-volume-tagging "specify-ebs-config.md#ebs-volume-tagging").
- Tasks that are part of a service – a tag with a _Key_
  as `aws:ecs:clusterName` and a _Value_ set to the
  cluster name. A tag with a _Key_ as
  `aws:ecs:serviceName` and a _Value_ set to the
  service name. Tags from one of the following resources:
  - Task definitions – All task definition tags that were added by
    users.
  - Services – All service tags that were added by users.

  An Amazon EBS volume attached to a task that is part of a service will
  receive a tag with a _Key_ as
  `aws:ecs:clusterName` and a _Value_
  set to the cluster name, and a tag with a _Key_ as
  `aws:ecs:serviceName` and a _Value_
  set to the service name. For more information about Amazon EBS volume
  tagging, see [Tagging Amazon EBS volumes](specify-ebs-config.md#ebs-volume-tagging "specify-ebs-config.md#ebs-volume-tagging").

The following options are required for this feature:

- You must opt in to the new Amazon Resource Name (ARN) and resource identifier (ID) formats. For
  more information, see [Amazon Resource Names (ARNs) and IDs](ecs-account-settings.md#ecs-resource-ids "ecs-account-settings.md#ecs-resource-ids").
- When you use the APIs to create a service or run a task, you must set
  `enableECSManagedTags` to `true` for
  `run-task` and `create-service`. For more information,
  see [create-service](../APIReference/API_CreateService.md "../APIReference/API_CreateService.md") and [run-task](../APIReference/API_RunTask.md "../APIReference/API_RunTask.md") in the
  _AWS Command Line Interface API Reference_.
- Amazon ECS uses managed tags to determine when some features are enabled, for
  example cluster Auto Scaling. We recommend that you do not manually modify tags so that
  the Amazon ECS can effectively manage the features.

## Use tags for billing

AWS provides a reporting tool called Cost Explorer that you can use to analyze the
cost and usage of your Amazon ECS resources.

You can use Cost Explorer to view charts of your usage and costs. You can view data
from the last 13 months, and forecast how much you're likely to spend for the next three
months. You can use Cost Explorer to see patterns in how much you spend on AWS
resources over time. For example, you can use it to identify areas that need further
inquiry and see trends that you can use to understand your costs. You also can specify
time ranges for the data, and view time data by day or by month.

You can use Amazon ECS-managed tags or user-added tags for your Cost and Usage Report. For
more information, see [Amazon ECS usage reports](usage-reports.md "usage-reports.md").

To see the cost of your combined resources, you can organize your billing information
based on resources that have the same tag key values. For example, you can tag several
resources with a specific application name, and then organize your billing information
to see the total cost of that application across several services. For more information
about setting up a cost allocation report with tags, see [The Monthly Cost Allocation
Report](../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md "../../../awsaccountbilling/latest/aboutv2/configurecostallocreport.md") in the _AWS Billing User Guide_.

Additionally, you can turn on _Split Cost Allocation Data_ to get task-level CPU and memory usage data
in your Cost and Usage Reports. For more information, see [Task-level Cost and Usage Reports](usage-reports.md#task-cur "usage-reports.md#task-cur").

###### Note

If you've turned on reporting, it can take up to 24 hours before the data for the
current month is available for viewing.
