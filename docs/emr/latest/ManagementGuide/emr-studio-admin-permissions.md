# Administrator permissions to create and manage

an EMR Studio

The IAM permissions described on this page permit you to create and manage an
EMR Studio. For detailed information about each required permission, see [Permissions required to manage an
EMR Studio](#emr-studio-admin-permissions-table "#emr-studio-admin-permissions-table").

## Permissions required to manage an

EMR Studio

The following table lists the operations related to creating and managing an
EMR Studio. The table also displays the permissions needed for each operation.

###### Note

You only need IAM Identity Center and Studio `SessionMapping` actions when you
use IAM Identity Center authentication mode.

| Permissions to create and manage an EMR Studio                                 | Operation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Permissions |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Create a Studio                                                                | `<br>"elasticmapreduce:CreateStudio",<br>"sso:CreateApplication",<br>"sso:PutApplicationAuthenticationMethod",<br>"sso:PutApplicationGrant",<br>"sso:PutApplicationAccessScope",<br>"sso:PutApplicationAssignmentConfiguration",<br>"iam:PassRole"<br>`                                                                                                                                                                                                                                                                                                                                                          |
| Describe a Studio                                                              | `<br>"elasticmapreduce:DescribeStudio",<br>"sso:GetManagedApplicationInstance"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| List Studios                                                                   | `<br>"elasticmapreduce:ListStudios"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Delete a Studio                                                                | `<br>"elasticmapreduce:DeleteStudio",<br>"sso:DeleteApplication",<br>"sso:DeleteApplicationAuthenticationMethod",<br>"sso:DeleteApplicationAccessScope",<br>"sso:DeleteApplicationGrant"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **_Additional permissions required when you use IAM Identity Center<br>mode_** |
| Assign users or groups to a Studio                                             | `<br>"elasticmapreduce:CreateStudioSessionMapping",<br>"sso:GetProfile",<br>"sso:ListDirectoryAssociations",<br>"sso:ListProfiles",<br>"sso:AssociateProfile",<br>"sso-directory:SearchUsers",<br>"sso-directory:SearchGroups",<br>"sso-directory:DescribeUser",<br>"sso-directory:DescribeGroup",<br>"sso:ListInstances",<br>"sso:CreateApplicationAssignment",<br>"sso:DescribeInstance",<br>"organizations:DescribeOrganization",<br>"organizations:ListDelegatedAdministrators",<br>"sso:CreateInstance",<br>"sso:DescribeRegisteredRegions",<br>"sso:GetSharedSsoConfiguration",<br>"iam:ListPolicies"<br>` |
| Retrieve Studio assignment details for a specific user or group                | `<br>"sso-directory:SearchUsers",<br>"sso-directory:SearchGroups",<br>"sso-directory:DescribeUser",<br>"sso-directory:DescribeGroup",<br>"sso:DescribeApplication",<br>"elasticmapreduce:GetStudioSessionMapping"<br>`                                                                                                                                                                                                                                                                                                                                                                                           |
| List all users and groups assigned to a Studio                                 | `<br>"elasticmapreduce:ListStudioSessionMappings"<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Update the session policy attached to a user or group assigned to a<br>Studio  | `<br>"sso-directory:SearchUsers",<br>"sso-directory:SearchGroups",<br>"sso-directory:DescribeUser",<br>"sso-directory:DescribeGroup",<br>"sso:DescribeApplication",<br>"sso:DescribeInstance",<br>"elasticmapreduce:UpdateStudioSessionMapping"<br>`                                                                                                                                                                                                                                                                                                                                                             |
| Remove a user or group from a Studio                                           | `<br>"elasticmapreduce:DeleteStudioSessionMapping",<br>"sso-directory:SearchUsers",<br>"sso-directory:SearchGroups",<br>"sso-directory:DescribeUser",<br>"sso-directory:DescribeGroup",<br>"sso:ListDirectoryAssociations",<br>"sso:GetProfile",<br>"sso:DescribeApplication",<br>"sso:DescribeInstance",<br>"sso:ListProfiles",<br>"sso:DisassociateProfile",<br>"sso:DeleteApplicationAssignment",<br>"sso:ListApplicationAssignments"<br>`                                                                                                                                                                    |

###### To create a policy with admin permissions for EMR Studio

1. Follow the instructions in [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") to
   create a policy using one of the following examples. The permissions you need depend on
   your [authentication mode for
   EMR Studio](emr-studio-authentication.md "emr-studio-authentication.md").

Insert your own values for these items:

    * Replace ``<your-resource-ARN>``to specify the Amazon Resource Name (ARN) of the object or objects that
     the statement covers for your use cases.
    * Replace `<region>` with the code of the AWS Region
     where you plan to create the Studio.
    * Replace `<aws-account_id>` with the ID of the AWS
     account for the Studio.
    * Replace `<EMRStudio-Service-Role>` and
     `<EMRStudio-User-Role>` with the names of your [EMR Studio service role](emr-studio-service-role.md "emr-studio-service-role.md") and [EMR Studio user role](emr-studio-user-permissions.md#emr-studio-create-user-role "emr-studio-user-permissions.md#emr-studio-create-user-role").

###### Example policy: Admin permissions when you use IAM authentication mode

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:studio/*"
 ],
 "Action": [
 "elasticmapreduce:CreateStudio",
 "elasticmapreduce:DescribeStudio",
 "elasticmapreduce:DeleteStudio"
 ],
 "Sid": "AllowELASTICMAPREDUCECreatestudio"
 },
 {
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Action": [
 "elasticmapreduce:ListStudios"
 ],
 "Sid": "AllowELASTICMAPREDUCEListstudios"
 },
 {
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iam::123456789012:role/EMRStudioServiceRole"
 ],
 "Action": [
 "iam:PassRole"
 ],
 "Sid": "AllowIAMPassrole"
 }
 ]
}`

```

###### Example policy: Admin permissions when you use IAM Identity Center authentication mode

###### Note

Identity Center and Identity Center directory APIs don't support specifying an ARN in the
resource element of an IAM policy statement. To allow access to IAM Identity Center and IAM Identity Center
Directory, the following permissions specify all resources, "Resource":"\*", for IAM Identity Center
actions. For more information, see [Actions, resources, and condition keys for IAM Identity Center Directory](../../../service-authorization/latest/reference/list_awsssodirectory.md#awsssodirectory-actions-as-permissions "../../../service-authorization/latest/reference/list_awsssodirectory.md#awsssodirectory-actions-as-permissions").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Resource": [
 "arn:aws:elasticmapreduce:*:123456789012:studio/*"
 ],
 "Action": [
 "elasticmapreduce:CreateStudio",
 "elasticmapreduce:DescribeStudio",
 "elasticmapreduce:DeleteStudio",
 "elasticmapreduce:CreateStudioSessionMapping",
 "elasticmapreduce:GetStudioSessionMapping",
 "elasticmapreduce:UpdateStudioSessionMapping",
 "elasticmapreduce:DeleteStudioSessionMapping"
 ],
 "Sid": "AllowELASTICMAPREDUCECreatestudio"
 },
 {
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Action": [
 "elasticmapreduce:ListStudios",
 "elasticmapreduce:ListStudioSessionMappings"
 ],
 "Sid": "AllowELASTICMAPREDUCEListstudios"
 },
 {
 "Effect": "Allow",
 "Resource": [
 "arn:aws:iam::123456789012:role/EMRStudio-SvcRole",
 "arn:aws:iam::123456789012:role/EMRStudio-User-Role"
 ],
 "Action": [
 "iam:PassRole"
 ],
 "Sid": "AllowIAMPassrole"
 },
 {
 "Effect": "Allow",
 "Resource": [
 "*"
 ],
 "Action": [
 "sso:CreateApplication",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant",
 "sso:PutApplicationAccessScope",
 "sso:PutApplicationAssignmentConfiguration",
 "sso:DescribeApplication",
 "sso:DeleteApplication",
 "sso:DeleteApplicationAuthenticationMethod",
 "sso:DeleteApplicationAccessScope",
 "sso:DeleteApplicationGrant",
 "sso:ListInstances",
 "sso:CreateApplicationAssignment",
 "sso:DeleteApplicationAssignment",
 "sso:ListApplicationAssignments",
 "sso:DescribeInstance",
 "sso:AssociateProfile",
 "sso:DisassociateProfile",
 "sso:GetProfile",
 "sso:ListDirectoryAssociations",
 "sso:ListProfiles",
 "sso-directory:SearchUsers",
 "sso-directory:SearchGroups",
 "sso-directory:DescribeUser",
 "sso-directory:DescribeGroup",
 "organizations:DescribeOrganization",
 "organizations:ListDelegatedAdministrators",
 "sso:CreateInstance",
 "sso:DescribeRegisteredRegions",
 "sso:GetSharedSsoConfiguration",
 "iam:ListPolicies"
 ],
 "Sid": "AllowSSOCreateapplication"
 }
 ]
}`

```

2. Attach the policy to your IAM identity (user, role, or group). For instructions, see
   [Adding and removing
   IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").
