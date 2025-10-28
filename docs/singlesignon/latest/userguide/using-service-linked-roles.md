# Using service-linked roles for

IAM Identity Center

AWS IAM Identity Center uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to IAM Identity Center. It is predefined by IAM Identity Center and includes all the
permissions that the service requires to call other AWS services on your behalf. For more
information, see [Understanding service-linked roles in IAM Identity Center](slrconcept.md "slrconcept.md").

A service-linked role makes setting up IAM Identity Center easier because you don’t have to
manually add the necessary permissions. IAM Identity Center defines the permissions of its
service-linked role, and unless defined otherwise, only IAM Identity Center can assume its role. The
defined permissions include the trust policy and the permissions policy, and that permissions
policy cannot be attached to any other IAM entity.

For information about other services that support service-linked roles, see [AWS Services That Work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in
the **Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for IAM Identity Center

IAM Identity Center uses the service-linked role named **AWSServiceRoleForSSO** to grant
IAM Identity Center permissions to manage AWS resources, including IAM roles, policies, and SAML IdP on
your behalf.

The AWSServiceRoleForSSO service-linked role trusts the following services to assume the
role:

- IAM Identity Center (service prefix: `sso`)

The AWSSSOServiceRolePolicy service-linked role permissions policy allows IAM Identity Center to complete the
following on roles on the path “/aws-reserved/sso.amazonaws.com/” and with the name prefix
“AWSReservedSSO\_”:

- `iam:AttachRolePolicy`
- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:DeleteRolePermissionsBoundary`
- `iam:DeleteRolePolicy`
- `iam:DetachRolePolicy`
- `iam:GetRole`
- `iam:ListRolePolicies`
- `iam:PutRolePolicy`
- `iam:PutRolePermissionsBoundary`
- `iam:ListAttachedRolePolicies`

The AWSSSOServiceRolePolicy service-linked role permissions policy allows IAM Identity Center to complete the
following on SAML providers with name prefix as “AWSSSO\_”:

- `iam:CreateSAMLProvider`
- `iam:GetSAMLProvider`
- `iam:UpdateSAMLProvider`
- `iam:DeleteSAMLProvider`

The AWSSSOServiceRolePolicy service-linked role permissions policy allows IAM Identity Center to complete the
following on all organizations:

- `organizations:DescribeAccount`
- `organizations:DescribeOrganization`
- `organizations:ListAccounts`
- `organizations:ListAWSServiceAccessForOrganization`
- `organizations:ListDelegatedAdministrators`

The AWSSSOServiceRolePolicy service-linked role permissions policy allows IAM Identity Center to complete the
following on all IAM roles (\*):

- `iam:listRoles`

The AWSSSOServiceRolePolicy service-linked role permissions policy allows IAM Identity Center to complete the
following on
“arn:aws:iam::\*:role/aws-service-role/sso.amazonaws.com/AWSServiceRoleForSSO”:

- `iam:GetServiceLinkedRoleDeletionStatus`
- `iam:DeleteServiceLinkedRole`

The AWSSSOServiceRolePolicy service-linked role permissions policy allows IAM Identity Center to complete the
following on
“arn:aws:identity-sync:\*:\*:profile/\*”:

- `identity-sync:DeleteSyncProfile`

For more information on updates to the AWSSSOServiceRolePolicy service-linked role permissions policy, see [IAM Identity Center updates to AWS managed
policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"IAMRoleProvisioningActions",
 "Effect":"Allow",
 "Action":[
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:DeleteRolePermissionsBoundary",
 "iam:PutRolePermissionsBoundary",
 "iam:PutRolePolicy",
 "iam:UpdateRole",
 "iam:UpdateRoleDescription",
 "iam:UpdateAssumeRolePolicy"
 ],
 "Resource":[
 "arn:aws:iam::*:role/aws-reserved/sso.amazonaws.com/*"
 ],
 "Condition":{
 "StringNotEquals":{
 "aws:PrincipalOrgMasterAccountId":"${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid":"IAMRoleReadActions",
 "Effect":"Allow",
 "Action":[
 "iam:GetRole",
 "iam:ListRoles"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Sid":"IAMRoleCleanupActions",
 "Effect":"Allow",
 "Action":[
 "iam:DeleteRole",
 "iam:DeleteRolePolicy",
 "iam:DetachRolePolicy",
 "iam:ListRolePolicies",
 "iam:ListAttachedRolePolicies"
 ],
 "Resource":[
 "arn:aws:iam::*:role/aws-reserved/sso.amazonaws.com/*"
 ]
 },
 {
 "Sid":"IAMSLRCleanupActions",
 "Effect":"Allow",
 "Action":[
 "iam:DeleteServiceLinkedRole",
 "iam:GetServiceLinkedRoleDeletionStatus",
 "iam:DeleteRole",
 "iam:GetRole"
 ],
 "Resource":[
 "arn:aws:iam::*:role/aws-service-role/sso.amazonaws.com/AWSServiceRoleForSSO"
 ]
 },
 {
 "Sid": "IAMSAMLProviderCreationAction",
 "Effect": "Allow",
 "Action": [
 "iam:CreateSAMLProvider"
 ],
 "Resource": [
 "arn:aws:iam::*:saml-provider/AWSSSO_*"
 ],
 "Condition": {
 "StringNotEquals": {
 "aws:PrincipalOrgMasterAccountId": "${aws:PrincipalAccount}"
 }
 }
 },
 {
 "Sid": "IAMSAMLProviderUpdateAction",
 "Effect": "Allow",
 "Action": [
 "iam:UpdateSAMLProvider"
 ],
 "Resource": [
 "arn:aws:iam::*:saml-provider/AWSSSO_*"
 ]
 },
 {
 "Sid":"IAMSAMLProviderCleanupActions",
 "Effect":"Allow",
 "Action":[
 "iam:DeleteSAMLProvider",
 "iam:GetSAMLProvider"
 ],
 "Resource":[
 "arn:aws:iam::*:saml-provider/AWSSSO_*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Sid":"AllowUnauthAppForDirectory",
 "Effect":"Allow",
 "Action":[
 "ds:UnauthorizeApplication"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Sid":"AllowDescribeForDirectory",
 "Effect":"Allow",
 "Action":[
 "ds:DescribeDirectories",
 "ds:DescribeTrusts"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Sid":"AllowDescribeAndListOperationsOnIdentitySource",
 "Effect":"Allow",
 "Action":[
 "identitystore:DescribeUser",
 "identitystore:DescribeGroup",
 "identitystore:ListGroups",
 "identitystore:ListUsers"
 ],
 "Resource":[
 "*"
 ]
 },
 {
 "Sid":"AllowDeleteSyncProfile",
 "Effect":"Allow",
 "Action":[
 "identity-sync:DeleteSyncProfile"
 ],
 "Resource":[
 "arn:aws:identity-sync:*:*:profile/*"
 ]
 }
 ]
}`

```

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for IAM Identity Center

You do not need to manually create a service-linked role. Once enabled, IAM Identity Center creates a service-linked role in all accounts within the organization in AWS Organizations. IAM Identity Center also creates the same service-linked role in every account that is subsequently added to your organization. This role allows IAM Identity Center to access each account's resources on your behalf.

###### Notes

- If you are signed in to the AWS Organizations management account, it uses your currently signed-in role
  and not the service-linked role. This prevents the escalation of privileges.
- When IAM Identity Center performs any IAM operations in the AWS Organizations management
  account, all operations happen using the credentials of the IAM principal. This enables
  the logs in CloudTrail to provide visibility of who made all privilege changes in the
  management account.

###### Important

If you were using the IAM Identity Center service before December 7, 2017, when it began
supporting service-linked roles, then IAM Identity Center created the AWSServiceRoleForSSO role in your
account. To learn more, see [A New
Role Appeared in My IAM Account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-link role and then need to create it again, you can use the
same process to recreate the role in your account.

## Editing a service-linked role for IAM Identity Center

IAM Identity Center does not allow you to edit the AWSServiceRoleForSSO service-linked role. After you
create a service-linked role, you cannot change the name of the role because various entities
might reference the role. However, you can edit the description of the role using IAM. For
more information, see [Editing a
service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

## Deleting a service-linked role for IAM Identity Center

You do not need to manually delete the AWSServiceRoleForSSO role. When an AWS account is removed from an AWS organization, IAM Identity Center automatically cleans up the resources and deletes the service-linked role from that AWS account.

You can also use the IAM console, the IAM CLI, or the IAM API to manually delete the
service-linked role. To do this, you must first manually clean up the resources for your
service-linked role and then you can manually delete it.

###### Note

If the IAM Identity Center service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete IAM Identity Center resources used by the AWSServiceRoleForSSO

1. [Remove user and group access to an
   AWS account](howtoremoveaccess.md "howtoremoveaccess.md") for all users
   and groups that have access to the AWS account.
2. [Remove permission sets in
   IAM Identity Center](howtoremovepermissionset.md "howtoremovepermissionset.md")
   that you have associated with the AWS account.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the AWSServiceRoleForSSO
service-linked role. For more information, see [Deleting a
Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
