# Identity-based policy examples for
 IAM Identity Center

This topic provides examples of IAM policies that you can create to grant users and roles permissions to administer IAM Identity Center. 

###### Important

We recommend that you first review the introductory topics that explain the basic concepts
 and options available for you to manage access to your IAM Identity Center resources. For more information,
 see [Overview of managing access permissions to your
 IAM Identity Center resources](iam-auth-access-overview.md "iam-auth-access-overview.md").

The sections in this topic cover the following:


* [Custom policy examples](#policyexample "#policyexample")
* [Permissions required to use the IAM Identity Center
 console](#requiredpermissionsconsole "#requiredpermissionsconsole")

## Custom policy examples


This section provides examples of common use cases that require a custom IAM policy.
 These example policies are identity-based policies, which do not specify the Principal
 element. This is because with an identity-based policy, you do not specify the principal who
 gets the permission. Instead, you attach the policy to the principal. When you attach an
 identity-based permission policy to an IAM role, the principal identified in the role's
 trust policy gets the permissions. You can create identity-based policies in IAM and attach
 them to users, groups, and/or roles. You can also apply these policies to IAM Identity Center users when you
 create a permission set in IAM Identity Center.


###### Note

Use these examples when you create policies for your environment and make sure to test
 for both positive (“access granted”) and negative (“access denied”) test cases before you
 deploy these policies in your production environment. For more information about testing
 IAM policies, see [Testing
 IAM policies with the IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the
 *IAM User Guide*.


###### Topics

* [Example 1: Allow a user to view IAM Identity Center](#policyexamplesetupenable "#policyexamplesetupenable")
* [Example 2: Allow a user to manage
 permissions to AWS accounts in IAM Identity Center](#policyexamplemanageconnecteddirectory "#policyexamplemanageconnecteddirectory")
* [Example 3: Allow a user to manage
 applications in IAM Identity Center](#policyexamplemanageapplication "#policyexamplemanageapplication")
* [Example 4: Allow a user to manage users and
 groups in your Identity Center directory](#policyexamplemanageusersgroups "#policyexamplemanageusersgroups")

### Example 1: Allow a user to view IAM Identity Center


The following permissions policy grants read-only permissions to a user so they can view
 all the settings and directory information configured in IAM Identity Center. 


###### Note

This policy is provided for example purposes only. In a production environment, we
 recommend that you use the `ViewOnlyAccess` AWS managed policy for
 IAM Identity Center.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "ds:DescribeDirectories",
 "ds:DescribeTrusts",
 "iam:ListPolicies",
 "organizations:DescribeOrganization",
 "organizations:DescribeAccount",
 "organizations:ListParents",
 "organizations:ListChildren",
 "organizations:ListAccounts",
 "organizations:ListRoots",
 "organizations:ListAccountsForParent",
 "organizations:ListDelegatedAdministrators",
 "organizations:ListOrganizationalUnitsForParent",
 "sso:ListManagedPoliciesInPermissionSet",
 "sso:ListPermissionSetsProvisionedToAccount",
 "sso:ListAccountAssignments",
 "sso:ListAccountsForProvisionedPermissionSet",
 "sso:ListPermissionSets",
 "sso:DescribePermissionSet",
 "sso:GetInlinePolicyForPermissionSet",
 "sso-directory:DescribeDirectory",
 "sso-directory:SearchUsers",
 "sso-directory:SearchGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```





### Example 2: Allow a user to manage
 permissions to AWS accounts in IAM Identity Center


The following permissions policy grants permissions to allow a user to create, manage,
 and deploy permission sets for your AWS accounts. 



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso:AttachManagedPolicyToPermissionSet",
 "sso:CreateAccountAssignment",
 "sso:CreatePermissionSet",
 "sso:DeleteAccountAssignment",
 "sso:DeleteInlinePolicyFromPermissionSet",
 "sso:DeletePermissionSet",
 "sso:DetachManagedPolicyFromPermissionSet",
 "sso:ProvisionPermissionSet",
 "sso:PutInlinePolicyToPermissionSet",
 "sso:UpdatePermissionSet"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMListPermissions",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:ListPolicies"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AccessToSSOProvisionedRoles",
 "Effect": "Allow",
 "Action": [
 "iam:AttachRolePolicy",
 "iam:CreateRole",
 "iam:DeleteRole",
 "iam:DeleteRolePolicy",
 "iam:DetachRolePolicy",
 "iam:GetRole",
 "iam:ListAttachedRolePolicies",
 "iam:ListRolePolicies",
 "iam:PutRolePolicy",
 "iam:UpdateRole",
 "iam:UpdateRoleDescription"
 ],
 "Resource": "arn:aws:iam::*:role/aws-reserved/sso.amazonaws.com/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:GetSAMLProvider"
 ],
 "Resource": "arn:aws:iam::*:saml-provider/AWSSSO_*_DO_NOT_DELETE"
 }
 ]
}`

```





###### Note

The additional permissions listed under the `"Sid": "IAMListPermissions"`,
 and `"Sid": "AccessToSSOProvisionedRoles"` sections are required only to enable
 the user to create assignments in the AWS Organizations management account. In certain cases, you
 may also need to add `iam:UpdateSAMLProvider` to these sections.


### Example 3: Allow a user to manage
 applications in IAM Identity Center


The following permissions policy grants permissions to allow a user to view and
 configure applications in IAM Identity Center, including pre-integrated SaaS applications from within the
 IAM Identity Center catalog. 


###### Note

The `sso:AssociateProfile` operation used in the following policy example
 is required for management of user and group assignments to applications. It also allows a
 user to assign users and groups to AWS accounts by using existing permission sets. If a
 user must manage AWS account access within IAM Identity Center, and requires permissions necessary to
 manage permission sets, see [Example 2: Allow a user to manage
 permissions to AWS accounts in IAM Identity Center](#policyexamplemanageconnecteddirectory "#policyexamplemanageconnecteddirectory").


As of October 2020, many of these operations are available only through the AWS
 console. This example policy includes “read” actions such as list, get, and search, which
 are relevant to the error-free operation of the console for this case.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso:AssociateProfile",
 "sso:CreateApplicationInstance",
 "sso:ImportApplicationInstanceServiceProviderMetadata",
 "sso:DeleteApplicationInstance",
 "sso:DeleteProfile",
 "sso:DisassociateProfile",
 "sso:GetApplicationTemplate",
 "sso:UpdateApplicationInstanceServiceProviderConfiguration",
 "sso:UpdateApplicationInstanceDisplayData",
 "sso:DeleteManagedApplicationInstance",
 "sso:UpdateApplicationInstanceStatus",
 "sso:GetManagedApplicationInstance",
 "sso:UpdateManagedApplicationInstanceStatus",
 "sso:CreateManagedApplicationInstance",
 "sso:UpdateApplicationInstanceSecurityConfiguration",
 "sso:UpdateApplicationInstanceResponseConfiguration",
 "sso:GetApplicationInstance",
 "sso:CreateApplicationInstanceCertificate",
 "sso:UpdateApplicationInstanceResponseSchemaConfiguration",
 "sso:UpdateApplicationInstanceActiveCertificate",
 "sso:DeleteApplicationInstanceCertificate",
 "sso:ListApplicationInstanceCertificates",
 "sso:ListApplicationTemplates",
 "sso:ListApplications",
 "sso:ListApplicationInstances",
 "sso:ListDirectoryAssociations",
 "sso:ListProfiles",
 "sso:ListProfileAssociations",
 "sso:ListInstances",
 "sso:GetProfile",
 "sso:GetSSOStatus",
 "sso:GetSsoConfiguration",
 "sso-directory:DescribeDirectory",
 "sso-directory:DescribeUsers",
 "sso-directory:ListMembersInGroup",
 "sso-directory:SearchGroups",
 "sso-directory:SearchUsers"
 ],
 "Resource": "*"
 }
 ]
}`

```





### Example 4: Allow a user to manage users and
 groups in your Identity Center directory


The following permissions policy grants permissions to allow a user to create, view,
 modify, and delete users and groups in IAM Identity Center. 


In some cases, direct modifications to users and groups in IAM Identity Center are restricted. For
 example, when Active Directory, or an external identity provider with Automatic Provisioning
 enabled, is selected as the identity source.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso-directory:ListGroupsForUser",
 "sso-directory:DisableUser",
 "sso-directory:EnableUser",
 "sso-directory:SearchGroups",
 "sso-directory:DeleteGroup",
 "sso-directory:AddMemberToGroup",
 "sso-directory:DescribeDirectory",
 "sso-directory:UpdateUser",
 "sso-directory:ListMembersInGroup",
 "sso-directory:CreateUser",
 "sso-directory:DescribeGroups",
 "sso-directory:SearchUsers",
 "sso:ListDirectoryAssociations",
 "sso-directory:RemoveMemberFromGroup",
 "sso-directory:DeleteUser",
 "sso-directory:DescribeUsers",
 "sso-directory:UpdateGroup",
 "sso-directory:CreateGroup"
 ],
 "Resource": "*"
 }
 ]
}`

```





## Permissions required to use the IAM Identity Center
 console


For a user to work with the IAM Identity Center console without errors, additional permissions are
 required. If an IAM policy has been created that is more restrictive than the minimum
 required permissions, the console will not function as intended for users with that policy. The
 following example lists the set of permissions that might be needed to ensure error-free
 operation within the IAM Identity Center console.



JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "sso:DescribeAccountAssignmentCreationStatus",
 "sso:DescribeAccountAssignmentDeletionStatus",
 "sso:DescribePermissionSet",
 "sso:DescribePermissionSetProvisioningStatus",
 "sso:DescribeRegisteredRegions",
 "sso:GetApplicationInstance",
 "sso:GetApplicationTemplate",
 "sso:GetInlinePolicyForPermissionSet",
 "sso:GetManagedApplicationInstance",
 "sso:GetMfaDeviceManagementForDirectory",
 "sso:GetPermissionSet",
 "sso:GetProfile",
 "sso:GetSharedSsoConfiguration",
 "sso:GetSsoConfiguration",
 "sso:GetSSOStatus",
 "sso:GetTrust",
 "sso:ListAccountAssignmentCreationStatus",
 "sso:ListAccountAssignmentDeletionStatus",
 "sso:ListAccountAssignments",
 "sso:ListAccountsForProvisionedPermissionSet",
 "sso:ListApplicationInstanceCertificates",
 "sso:ListApplicationInstances",
 "sso:ListApplications",
 "sso:ListApplicationTemplates",
 "sso:ListDirectoryAssociations",
 "sso:ListInstances",
 "sso:ListManagedPoliciesInPermissionSet",
 "sso:ListPermissionSetProvisioningStatus",
 "sso:ListPermissionSets",
 "sso:ListPermissionSetsProvisionedToAccount",
 "sso:ListProfileAssociations",
 "sso:ListProfiles",
 "sso:ListTagsForResource",
 "sso-directory:DescribeDirectory",
 "sso-directory:DescribeGroups",
 "sso-directory:DescribeUsers",
 "sso-directory:ListGroupsForUser",
 "sso-directory:ListMembersInGroup",
 "sso-directory:SearchGroups",
 "sso-directory:SearchUsers"
 ],
 "Resource": "*"
 }
 ]
}`

```
