# Using service-linked roles for Amazon SES

Amazon Simple Email Service (SES) uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that
is linked directly to Amazon SES. Service-linked roles are predefined by SES and include
all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up SES easier because you don’t have to
manually add the necessary permissions. SES defines the permissions of its
service-linked roles, and unless defined otherwise, only SES can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your SES resources because you can't inadvertently remove permission to
access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for

Amazon SES

SES uses the service-linked role named **AWSServiceRoleForAmazonSES** –
Allows SES to publish Amazon CloudWatch basic monitoring metrics on behalf of your SES resources.

The AWSServiceRoleForAmazonSES service-linked role trusts the following service to assume the
role:

- `ses.amazonaws.com`

The role permissions policy named AmazonSESServiceRolePolicy is an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") that allows SES to complete the following
actions on the specified resources:

- Action: `cloudwatch:PutMetricData` in the `AWS/SES` CloudWatch
  namespace. This action grants permission for SES to put metric data into
  the CloudWatch `AWS/SES` namespace. For more information about SES
  metrics available in CloudWatch, see [Logging and monitoring in Amazon SES](security-monitoring-overview.md "security-monitoring-overview.md").
- Action: `cloudwatch:PutMetricData` in the
  `AWS/SES/MailManager` CloudWatch namespace. This action grants
  permission for SES to put metric data into the CloudWatch
  `AWS/SES/MailManager` namespace. For more information about
  SES metrics available in CloudWatch, see [Logging and monitoring in Amazon SES](security-monitoring-overview.md "security-monitoring-overview.md").
- Action: `cloudwatch:PutMetricData` in the
  `AWS/SES/Addons` CloudWatch namespace. This action grants permission
  for SES to put metric data into the CloudWatch `AWS/SES/Addons`
  namespace. For more information about SES metrics available in CloudWatch, see
  [Logging and monitoring in Amazon SES](security-monitoring-overview.md "security-monitoring-overview.md").

You must configure permissions to allow your users, groups, or roles to create, edit,
or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Amazon SES

You don't need to manually create a service-linked role. When you create SES
resources in the AWS Management Console, the AWS CLI, or the AWS API, SES
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you create SES
resources, SES creates the service-linked role for you again.

## Editing a service-linked role for

Amazon SES

SES does not allow you to edit the AWSServiceRoleForAmazonSES service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role
using IAM.

## Deleting a service-linked role for

SES

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. However, you must clean up your service-linked
role before you can manually delete it.

### Cleaning Up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first delete
all SES resources.

###### Note

If the SES service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes
and try the operation again.

### Manually delete the service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonSES
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Amazon SES service-linked roles

SES does not support using service-linked roles in every Region where the
service is available. You can use the AWSServiceRoleForAmazonSES role in the following Regions.

| Region name           | Region identity | Support in SES |
| --------------------- | --------------- | -------------- |
| US East (N. Virginia) | us-east-1       | Yes            |
| US East (Ohio)        | us-east-2       | Yes            |
| Asia Pacific (Sydney) | ap-southeast-2  | Yes            |
| Asia Pacific (Tokyo)  | ap-northeast-1  | Yes            |
| Europe (Frankfurt)    | eu-central-1    | Yes            |
| Europe (Ireland)      | eu-west-1       | Yes            |
