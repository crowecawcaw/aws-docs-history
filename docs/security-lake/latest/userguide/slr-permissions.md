# Service-linked role (SLR) permissions for Security Lake

Security Lake uses the service-linked role named
`AWSServiceRoleForSecurityLake`. This service-linked role trusts the
`securitylake.amazonaws.com` service to assume the role. For more
information about, AWS managed policies for Amazon Security Lake, see [AWS manage policies for Amazon Security Lake](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

The permissions policy for the role, which is an AWS managed policy named `SecurityLakeServiceLinkedRole`, allows Security Lake to create and operate
the security data lake. It also allows Security Lake to perform tasks such as the following on the specified resources:

- Use AWS Organizations actions to retrieve information about associated accounts
- Use Amazon Elastic Compute Cloud (Amazon EC2) to retrieve information about Amazon VPC Flow Logs
- Use AWS CloudTrail actions to retrieve information about the service-linked role
- Use AWS WAF actions to collect AWS WAF logs, when it is enabled as a log source in
  Security Lake
- Use `LogDelivery` action to create or delete an AWS WAF log delivery
  subscription.
  To review the permissions for this policy, see [SecurityLakeServiceLinkedRole](../../../aws-managed-policy/latest/reference/SecurityLakeServiceLinkedRole.md "../../../aws-managed-policy/latest/reference/SecurityLakeServiceLinkedRole.md") in the _AWS Managed Policy
  Reference Guide_.

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the Security Lake service-linked role

You don't need to manually create the `AWSServiceRoleForSecurityLake`
service-linked role for Security Lake. When you enable Security Lake for your AWS account, Security Lake
automatically creates the service-linked role for you.

## Editing the Security Lake service-linked role

Security Lake doesn't allow you to edit the `AWSServiceRoleForSecurityLake`
service-linked role. After a service-linked role is created, you can't change the name
of the role because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the Security Lake service-linked role

You cannot delete the service-linked role from Security Lake. Instead, you may delete the service-linked role from the IAM
console, API, or AWS CLI. For more information, see
[Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

Before you can delete the service-linked role, you must first confirm that the role has no active sessions and remove any
resources that `AWSServiceRoleForSecurityLake` is using.

###### Note

If Security Lake is using the `AWSServiceRoleForSecurityLake` role when you try to
delete the resources, the deletion might fail. If that happens, wait a few minutes
and then try the operation again.

If you delete the `AWSServiceRoleForSecurityLake` service-linked role and need to
create it again, you can create it again by enabling Security Lake for your account. When you
enable Security Lake again, Security Lake automatically creates the service-linked role again for you.

## Supported AWS Regions for the Security Lake service-linked role

Security Lake supports using the `AWSServiceRoleForSecurityLake` service-linked role
in all the AWS Regions where Security Lake is available. For a list of Regions where Security Lake is
currently available, see [Security Lake Regions and endpoints](supported-regions.md "supported-regions.md").
