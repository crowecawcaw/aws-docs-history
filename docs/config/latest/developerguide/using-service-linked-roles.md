# Using Service-Linked Roles for AWS Config

AWS Config uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Config. Service-linked roles are predefined by AWS Config and include all the
permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Config easier because you don’t have to manually add
the necessary permissions. AWS Config defines the permissions of its service-linked roles, and unless
defined otherwise, only AWS Config can assume its roles. The defined permissions include the trust
policy and the permissions policy, and that permissions policy cannot be attached to any other
IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in
the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-Linked Role Permissions for AWS Config

AWS Config uses the service-linked role named **AwsServiceRoleForConfig** – AWS Config uses
this service-linked role to call other AWS services on your behalf. To view the latest
updates, see [AWS Config updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

The **AwsServiceRoleForConfig** service-linked role trusts the
`config.amazonaws.com` service to assume the role.

The permissions policy for the `AwsServiceRoleForConfig` role contains read-only and
write-only permissions for AWS Config resources and read-only permissions for resources in other
services that AWS Config supports. To view the managed policy for **AwsServiceRoleForConfig**, see [AWS managed policies for AWS Config](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSConfigServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSConfigServiceRolePolicy").

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

To use a service-linked role with AWS Config, you must configure permissions on your Amazon S3 bucket
and Amazon SNS topic. For more information, see [Required Permissions for the
Amazon S3 Bucket When Using Service-Linked Roles](s3-bucket-policy.md#required-permissions-using-servicelinkedrole "s3-bucket-policy.md#required-permissions-using-servicelinkedrole"), [Required
Permissions for the AWS KMS Key When Using Service-Linked Roles (S3 Bucket
Delivery)](s3-kms-key-policy.md#required-permissions-s3-kms-key-using-servicelinkedrole "s3-kms-key-policy.md#required-permissions-s3-kms-key-using-servicelinkedrole"), and [Required
Permissions for the Amazon SNS Topic When Using Service-Linked Roles](sns-topic-policy.md#required-permissions-snstopic-using-servicelinkedrole "sns-topic-policy.md#required-permissions-snstopic-using-servicelinkedrole").

## Creating a Service-Linked Role for AWS Config

In the IAM CLI or the IAM API, create a service-linked role with the
`config.amazonaws.com` service name. For more information, see [Creating a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a Service-Linked Role for AWS Config

AWS Config does not allow you to edit the **AwsServiceRoleForConfig**
service-linked role. After you create a service-linked role, you cannot change the name of the
role because various entities might reference the role. However, you can edit the description
of the role using IAM. For more information, see [Editing a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a Service-Linked Role for AWS Config

If you no longer need to use a feature or service that requires a service-linked role, we
recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the AWS Config service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

**To delete AWS Config resources used by the **AwsServiceRoleForConfig\*\*\*\*

Ensure that you do not have `ConfigurationRecorders` using the service-linked
role. You can use the AWS Config console to stop the configuration recorder. To stop recording,
under **Recording is on**, choose **Turn
off**.

You can delete the `ConfigurationRecorder` using AWS Config API. To delete, use the
`delete-configuration-recorder` command.

```

        $ aws configservice delete-configuration-recorder --configuration-recorder-name `default`

```

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the AwsServiceRoleForConfig
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
