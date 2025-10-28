# Using roles for creating and managing CloudTrail organization trails and CloudTrail Lake organization event data stores in CloudTrail

AWS CloudTrail uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to CloudTrail. Service-linked roles are predefined by CloudTrail and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up CloudTrail easier because you don’t have to
manually add the necessary permissions. CloudTrail defines the permissions of its
service-linked roles, and unless defined otherwise, only CloudTrail can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your CloudTrail resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for CloudTrail

CloudTrail uses the service-linked role named **AWSServiceRoleForCloudTrail**
– This service linked role is used for supporting organization trails and organization event data stores.

The AWSServiceRoleForCloudTrail service-linked role trusts the following services to assume the
role:

- `cloudtrail.amazonaws.com`

The role permissions policy named CloudTrailServiceRolePolicy allows CloudTrail to complete
the following actions on the specified resources:

- Actions on all CloudTrail resources:
  - `All`

- Actions on all AWS Organizations resources:
  - `organizations:DescribeAccount`
  - `organizations:DescribeOrganization`
  - `organizations:ListAccounts`
  - `organizations:ListAWSServiceAccessForOrganization`

- Actions on all Organizations resources for the CloudTrail service principal to list the delegated administrators for the organization:
  - `organizations:ListDelegatedAdministrators`

- Actions for [disabling Lake federation](query-disable-federation.md "query-disable-federation.md") on an organization event data store:
  - `glue:DeleteTable`
  - `lakeformation:DeRegisterResource`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

For more information about the managed policy associated with AWSServiceRoleForCloudTrail, see [AWS managed policies for AWS CloudTrail](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Creating a service-linked role for

CloudTrail

You don't need to manually create a service-linked role. When you
create an organization trail or organization event data store, or add a delegated administrator in the CloudTrail console, in the AWS Management Console, the AWS CLI, or the AWS API, CloudTrail
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create an organization trail or organization event data store, or add a delegated administrator in the CloudTrail console,, CloudTrail creates the service-linked role for you again.

## Editing a service-linked role for

CloudTrail

CloudTrail does not allow you to edit the AWSServiceRoleForCloudTrail service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

CloudTrail

You don't need to manually delete the AWSServiceRoleForCloudTrail role. If an AWS account is removed from
an Organizations organization, the AWSServiceRoleForCloudTrail role is automatically removed from that
AWS account. You cannot detach or remove policies from the AWSServiceRoleForCloudTrail
service-linked role in an organization management account without removing the account from the
organization.

You can also use the IAM console, the AWS CLI or the AWS API to manually delete the
service-linked role. To do this, you must first manually clean up the resources for your
service-linked role, and then you can manually delete it.

###### Note

If the CloudTrail service is using the role when you try to delete the resources, then
deletion might fail. If that happens, wait for a few minutes and try the operation
again.

To remove a resource being used by the AWSServiceRoleForCloudTrail role, you can do one of
the following:

- Remove the AWS account from the organization in Organizations.
- Update the trail so that it is no longer an organization trail. For more information,
  see [Updating a trail with the CloudTrail console](cloudtrail-update-a-trail-console.md "cloudtrail-update-a-trail-console.md").
- Update the event data store so that it is no longer an organization event data store. For more information, see
  [Update an event data store with the console](query-event-data-store-update.md "query-event-data-store-update.md").
- Delete the trail. For more information, see
  [Deleting a trail with the CloudTrail console](cloudtrail-delete-trails-console.md "cloudtrail-delete-trails-console.md").
- Delete the event data store. For more information, see
  [Delete an event data store with the console](query-event-data-store-delete.md "query-event-data-store-delete.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
AWSServiceRoleForCloudTrail service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
