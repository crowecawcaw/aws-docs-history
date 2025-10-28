# Using service-linked roles for

managed integrations

Managed integrations for AWS IoT Device Management uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to managed integrations. Service-linked roles are predefined by managed integrations and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up managed integrations easier because you don’t have to
manually add the necessary permissions. Managed integrations for AWS IoT Device Management defines the permissions of its
service-linked roles, and unless defined otherwise, only managed integrations can assume its roles. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This
protects your managed integrations resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles**
column. Choose a **Yes** with a link to view the service-linked
role documentation for that service.

## Service-linked role permissions for managed integrations

Managed integrations for AWS IoT Device Management uses the service-linked role named **AWSServiceRoleForIoTManagedIntegrations** –
Provides managed integrations for AWS IoT Device Management permission to publish logs and metrics on your behalf.

The AWSServiceRoleForIoTManagedIntegrations service-linked role trusts the following services to assume the
role:

- `iotmanagedintegrations.amazonaws.com`

The role permissions policy named AWSIoTManagedIntegrationsServiceRolePolicy allows managed integrations to complete the
following actions on the specified resources:

- Action: `logs:CreateLogGroup, logs:DescribeLogGroups, logs:CreateLogStream, logs:PutLogEvents, logs:DescribeLogStreams, cloudwatch:PutMetricData`
  `on all of your managed integrations resources.`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "CloudWatchLogs",
 "Effect" : "Allow",
 "Action" : [
 "logs:CreateLogGroup",
 "logs:DescribeLogGroups"
 ],
 "Resource" : [
 "arn:aws:logs:*:*:log-group:/aws/iotmanagedintegrations/*"
 ]
 },
 {
 "Sid" : "CloudWatchStreams",
 "Effect" : "Allow",
 "Action" : [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:DescribeLogStreams"
 ],
 "Resource" : [
 "arn:aws:logs:*:*:log-group:/aws/iotmanagedintegrations/*:log-stream:*"
 ]
 },
 {
 "Sid" : "CloudWatchMetrics",
 "Effect" : "Allow",
 "Action" : [
 "cloudwatch:PutMetricData"
 ],
 "Resource" : "*",
 "Condition" : {
 "StringEquals" : {
 "cloudwatch:namespace" : [
 "AWS/IoTManagedIntegrations",
 "AWS/Usage"
 ]
 }
 }
 }
 ]
}`

```

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for managed integrations

You don't need to manually create a service-linked role. When you
cause an event type such as calling the `PutRuntimeLogConfiguration`, `CreateEventLogConfiguration`, or `RegisterCustomEndpoint` API commands in the AWS Management Console, the AWS CLI, or the AWS API, managed integrations creates
the service-linked role for you. For more information on
`PutRuntimeLogConfiguration`, `CreateEventLogConfiguration`, or
`RegisterCustomEndpoint`, see [PutRuntimeLogConfiguration](../APIReference/API_PutRuntimeLogConfiguration.md "../APIReference/API_PutRuntimeLogConfiguration.md"), [CreateEventLogConfiguration](../APIReference/API_CreateEventLogConfiguration.md "../APIReference/API_CreateEventLogConfiguration.md"), or [RegisterCustomEndpoint](../APIReference/API_RegisterCustomEndpoint.md "../APIReference/API_RegisterCustomEndpoint.md").

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you cause an event type such as calling the `PutRuntimeLogConfiguration`, `CreateEventLogConfiguration`, or `RegisterCustomEndpoint` API commands,
managed integrations creates the service-linked role for you again. Alternatively, you can contact
AWS Customer Support via the AWS Support Center Console. For more information on AWS Support
Plans, see [Compare AWS Support
Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/").

You can also use the IAM console to create a service-linked role with the
**IoT ManagedIntegrations - Managed Role** use case. In the AWS CLI or the AWS API, create a
service-linked role with the `iotmanagedintegrations.amazonaws.com` service name. For more
information, see [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you
delete this service-linked role, you can use this same process to create the role
again.

## Editing a service-linked role for managed integrations

managed integrations does not allow you to edit the AWSServiceRoleForIoTManagedIntegrations service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for managed integrations

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If managed integrations is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForIoTManagedIntegrations service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.

## Supported Regions for managed integrations service-linked roles

Managed integrations for AWS IoT Device Management supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/iot-managedintegrations.md "../../../general/latest/gr/iot-managedintegrations.md").
