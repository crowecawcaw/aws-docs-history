# How AWS Config Works

AWS Config provides a detailed view of the configuration of AWS resources in your AWS
account. This includes how the resources are related to one another and how they were
configured in the past so that you can see how the configurations and relationships change
over time.

An AWS _resource_ is an entity you can work with in AWS, such as an
Amazon Elastic Compute Cloud (EC2) instance, an Amazon Elastic Block Store (EBS) volume, a security group, or an Amazon Virtual Private Cloud
(VPC). For a complete list of AWS resources supported by AWS Config, see [Supported Resource Types for AWS Config](resource-config-reference.md "resource-config-reference.md").

![The image depicts a high-level overview of how AWS Config works. It illustrates the flow of information from various AWS resources to AWS Config, which then stores configuration data in an Amazon S3 bucket. The process involves the configuration recorder, AWS Config rules, and the delivery channel. The goal is to track and manage resource configurations within an AWS environment.](images/how-AWSconfig-works-2.png)

## Resource Discovery

When you turn on AWS Config, it first discovers the supported AWS resources that exist in your
account and generates a [configuration
item](config-concepts.md#config-items "config-concepts.md#config-items") for each resource.

AWS Config also generates configuration items when the configuration of a resource changes, and
it maintains historical records of the configuration items of your resources from the time you
start the configuration recorder. By default, AWS Config creates configuration items for every
supported resource in the region. If you don't want AWS Config to create configuration items for all
supported resources, you can specify the resource types that you want it to track.

Before specifying a resource type for AWS Config to track,
check [Resource Coverage by Region Availability](what-is-resource-config-coverage.md "what-is-resource-config-coverage.md")
to see if the resource type is supported in the AWS Region where you are setting up AWS Config.
If a resource type is supported by AWS Config in at least one Region,
you can enable the recording of that resource type in all Regions supported by AWS Config,
even if the specified resource type is not supported the AWS Region where you are setting up AWS Config.

## Resource Tracking

AWS Config keeps track of all changes to your resources by invoking the Describe or the List API
call for each resource in your account. The service uses those same API calls to capture
configuration details for all related resources.

For example, removing an egress rule from a VPC security group causes AWS Config to invoke a
Describe API call on the security group. AWS Config then invokes a Describe API call on all of the
instances associated with the security group. The updated configurations of the security group
(the resource) and of each instance (the related resources) are recorded as configuration items
and delivered in a configuration stream to an Amazon Simple Storage Service (Amazon S3) bucket.

AWS Config also tracks the configuration changes that were not initiated by the API. AWS Config examines
the resource configurations periodically and generates configuration items for the
configurations that have changed.

If you are using AWS Config rules, AWS Config continuously evaluates your AWS resource configurations
for desired settings. Depending on the rule, AWS Config will evaluate your resources either in
response to configuration changes or periodically. Each rule is associated with an AWS Lambda
function, which contains the evaluation logic for the rule. When AWS Config evaluates your resources,
it invokes the rule's AWS Lambda function. The function returns the compliance status of the
evaluated resources. If a resource violates the conditions of a rule, AWS Config flags the resource
and the rule as noncompliant. When the compliance status of a resource changes, AWS Config sends a
notification to your Amazon SNS topic.

## Delivery of Configuration Items

AWS Config can deliver configuration items through one of the following channels:

### Amazon S3 Bucket

AWS Config tracks changes in the configuration of your AWS resources, and it regularly sends
updated configuration details to an Amazon S3 bucket that you specify. For each resource type
that AWS Config records, it sends a _configuration history file_ every six
hours. Each configuration history file contains details about the resources that changed in
that six-hour period. Each file includes resources of one type, such as Amazon EC2 instances or
Amazon EBS volumes. If no configuration changes occur, AWS Config does not send a file.

AWS Config sends a _configuration snapshot_ to your Amazon S3 bucket when you
use the [deliver-config-snapshot](../../../cli/latest/reference/configservice/deliver-config-snapshot.md "../../../cli/latest/reference/configservice/deliver-config-snapshot.md") command with the AWS CLI, or when you use the [DeliverConfigSnapshot](../APIReference/API_DeliverConfigSnapshot.md "../APIReference/API_DeliverConfigSnapshot.md") action with
the AWS Config API. A configuration snapshot contains configuration details for all resources that
AWS Config records in your AWS account. The configuration history file and configuration
snapshot are in JSON format.

###### Note

AWS Config only delivers the configuration history files and configuration snapshots to
the specified S3 bucket; AWS Config doesn't modify the lifecycle policies for objects in the
S3 bucket. You can use lifecycle policies to specify whether you want to delete or archive
objects to Amazon Glacier. For more information, see [Managing Lifecycle Configuration](../../../AmazonS3/latest/userguide/LifecycleConfiguration.md "../../../AmazonS3/latest/userguide/LifecycleConfiguration.md")
in the _Amazon Simple Storage Service User Guide_. You can also see the [Archiving Amazon S3 Data to
Amazon Glacier](https://aws.amazon.com/blogs/aws/archive-s3-to-glacier/ "https://aws.amazon.com/blogs/aws/archive-s3-to-glacier/") blog post.

### Amazon SNS Topic

An Amazon Simple Notification Service (Amazon SNS) topic is a communication channel that Amazon SNS uses to deliver
messages (or _notifications_) to subscribing endpoints such as an email
address or clients. Other types of Amazon SNS notifications include push notification messages to
apps on mobile phones, Short Message Service (SMS) notifications to SMS-enabled mobile
phones and smart phones, and HTTP POST requests. For best results, use Amazon SQS as the
notification endpoint for the SNS topic and then process the information in the notification
programmatically.

AWS Config uses the Amazon SNS topic that you specify to send you notifications. The type of
notification that you are receiving is indicated by the value for the
`messageType` key in the message body, as in the following example:

```
"messageType": "ConfigurationHistoryDeliveryCompleted"
```

The notifications can be any of the following message types.

| **Message type**                               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ComplianceChangeNotification                   | The compliance type of a resource that AWS Config evaluates has changed. The compliance<br>type indicates whether the resource complies with a specific AWS Config rule, and it is<br>represented by the `ComplianceType` key in the message. The message<br>includes `newEvaluationResult` and `oldEvaluationResult` objects<br>for comparison.                                                                                 |
| ConfigRulesEvaluationStarted                   | AWS Config started evaluating your rule against the specified resources.                                                                                                                                                                                                                                                                                                                                                         |
| ConfigurationSnapshotDeliveryStarted           | AWS Config started delivering the configuration snapshot to your Amazon S3 bucket. The name<br>of the Amazon S3 bucket is provided for the `s3Bucket` key in the<br>message.                                                                                                                                                                                                                                                     |
| ConfigurationSnapshotDeliveryCompleted         | AWS Config successfully delivered the configuration snapshot to your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                           |
| ConfigurationSnapshotDeliveryFailed            | AWS Config failed to deliver the configuration snapshot to your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                                |
| ConfigurationHistoryDeliveryCompleted          | AWS Config successfully delivered the configuration history to your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                                            |
| ConfigurationItemChangeNotification            | A resource has been created, deleted, or changed in configuration. This message<br>includes the details of the configuration item that AWS Config creates for this change, and<br>it includes the type of change. These notifications are delivered within minutes of a<br>change and are collectively known as the _configuration<br>stream_.                                                                                   |
| OversizedConfigurationItemChangeNotification   | This message type is delivered when a configuration item change notification<br>exceeded the maximum size allowed by Amazon SNS. The message includes a summary of the<br>configuration item. With the exception of SMS messages, Amazon SNS messages can contain up<br>to 256 KB of text data, including XML, JSON, and unformatted text. You can view the<br>complete notification in the specified Amazon S3 bucket location. |
| OversizedConfigurationItemChangeDeliveryFailed | AWS Config failed to deliver the oversized configuration item change notification to<br>your Amazon S3 bucket.                                                                                                                                                                                                                                                                                                                   |

For example notifications, see [Notifications that AWS Config Sends to an Amazon SNS
topic](notifications-for-AWS-Config.md "notifications-for-AWS-Config.md"). For more information about Amazon SNS, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md").

###### Note

**Why can't I see my latest configuration changes?**

AWS Config usually records configuration changes to your resources right after a change is detected, or at the frequency that you specify.
However, this is on a best effort basis and can take longer at times. If issues persist after sometime, contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") and provide your AWS Config metrics that are supported by Amazon CloudWatch.
For information about these metrics, see [AWS Config Usage and Success Metrics](viewing-the-aws-config-dashboard.md "viewing-the-aws-config-dashboard.md").

## Control Access to AWS Config

AWS Identity and Access Management is a web service that enables Amazon Web Services (AWS) customers to manage users and
user permissions.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
