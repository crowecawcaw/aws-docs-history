# Using service-linked roles for Macie

Amazon Macie uses an AWS Identity and Access Management (IAM) [service-linked role](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") named
`AWSServiceRoleForAmazonMacie`. This service-linked role is an IAM role
that's linked directly to Macie. It's predefined by Macie and it includes all the
permissions that Macie requires to call other AWS services and monitor AWS resources on
your behalf. Macie uses this service-linked role in all the AWS Regions where Macie is
available.

A service-linked role makes setting up Macie easier because you don't have to manually add
the necessary permissions. Macie defines the permissions of this service-linked role, and
unless defined otherwise, only Macie can assume the role. The defined permissions include the
trust policy and the permissions policy, and that permissions policy can't be attached to any
other IAM entity.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column.
Choose a **Yes** with a link to review the service-linked role
documentation for that service.

###### Topics

- [Service-linked role permissions for Macie](#slr-permissions "#slr-permissions")
- [Creating the Macie service-linked role](#create-slr "#create-slr")
- [Editing the Macie service-linked role](#edit-slr "#edit-slr")
- [Deleting the Macie service-linked role](#delete-slr "#delete-slr")
- [Supported AWS Regions](#slr-regions "#slr-regions")

## Service-linked role permissions for Macie

Amazon Macie uses the service-linked role named
`AWSServiceRoleForAmazonMacie`. This service-linked role trusts the
`macie.amazonaws.com` service to assume the role.

The permissions policy for the role, which is named
`AmazonMacieServiceRolePolicy`, allows Macie to perform tasks such as the
following on the specified resources:

- Use Amazon S3 actions to retrieve information about S3 buckets and objects.
- Use Amazon S3 actions to retrieve S3 objects.
- Use AWS Organizations actions to retrieve information about associated accounts.
- Use Amazon CloudWatch Logs actions to log events for sensitive data discovery jobs.

To review the permissions for this policy, see [AmazonMacieServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonMacieServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonMacieServiceRolePolicy.md") in the _AWS Managed
Policy Reference Guide_.

For details about updates to this policy, see [Updates to AWS managed policies for
Macie](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates"). For automatic alerts about changes
to this policy, subscribe to the RSS feed on the [Macie
document history](doc-history.md "doc-history.md") page.

You must configure permissions for an IAM entity (such as a user or role) to allow
the entity to create, edit, or delete a service-linked role. For more information, see
[Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the service-linked role for Macie

You don't need to manually create the `AWSServiceRoleForAmazonMacie`
service-linked role for Amazon Macie. When you enable Macie for your AWS account, Macie
automatically creates the service-linked role for you.

If you delete the Macie service-linked role and then need to create it again, you can use
the same process to re-create the role in your account. When you enable Macie again, Macie
creates the service-linked role again for you.

## Editing the service-linked role for Macie

Amazon Macie doesn't allow you to edit the `AWSServiceRoleForAmazonMacie`
service-linked role. After a service-linked role is created, you can't change the name
of the role because various entities might reference the role. However, you can edit the
description of the role by using IAM. For more information, see [Updating a
service-linked role](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md") in the _IAM User Guide_.

## Deleting the service-linked role for Macie

You can delete a service-linked role only after you delete its related resources. This
protects your resources because you can't inadvertently remove permission to access the
resources.

If you no longer need to use Amazon Macie, we recommend that you manually delete the
`AWSServiceRoleForAmazonMacie` service-linked role. When you disable
Macie, Macie doesn't delete the role for you.

Before you delete the role, you must disable Macie in each AWS Region where you
enabled it. You must also manually clean up the resources for the role. To delete the role,
you can use the IAM console, the AWS CLI, or the AWS API. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#id_roles_manage_delete_slr") in the
_IAM User Guide_.

###### Note

If Macie is using the `AWSServiceRoleForAmazonMacie` role when you try to
delete the resources, the deletion might fail. If that happens, wait a few minutes
and then try the operation again.

If you delete the `AWSServiceRoleForAmazonMacie` service-linked role and need to
create it again, you can create it again by enabling Macie for your account. When you
enable Macie again, Macie creates the service-linked role again for you.

## Supported AWS Regions for the Macie service-linked

role

Amazon Macie supports using the `AWSServiceRoleForAmazonMacie` service-linked role
in all the AWS Regions where Macie is available. For a list of Regions where Macie is
currently available, see [Amazon Macie endpoints and
quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the _AWS General Reference_.
