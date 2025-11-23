# Granting AWS Managed Microsoft AD users and groups access to AWS

resources with IAM roles

AWS Directory Service provides the ability to give your AWS Managed Microsoft AD users and groups access to AWS
services and resources, such as access to the Amazon EC2 console. Similar to granting IAM users
access to manage directories as described in [Identity-based
policies (IAM policies)](IAM_Auth_Access_Overview.md#IAM_Auth_Access_ManagingAccess_IdentityBased "IAM_Auth_Access_Overview.md#IAM_Auth_Access_ManagingAccess_IdentityBased"), in order for users in
your directory to have access to other AWS resources, such as Amazon EC2 you must assign IAM
roles and policies to those users and groups. For more information, see [IAM roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") in the
_IAM User Guide_.

For information about how to grant users access to the AWS Management Console, see [Enabling AWS Management Console access with AWS Managed Microsoft AD
credentials](ms_ad_management_console_access.md "ms_ad_management_console_access.md").

###### Topics

- [Creating a new IAM role](create_role.md "create_role.md")
- [Editing the trust relationship for an existing IAM
  role](edit_trust.md "edit_trust.md")
- [Assigning users or groups to an existing IAM
  role](assign_role.md "assign_role.md")
- [Viewing users and groups assigned to a role](view_role_details.md "view_role_details.md")
- [Removing a user or group from an IAM role](remove_role_users.md "remove_role_users.md")
- [Using AWS managed policies with Directory Service](ms_ad_managed_policies.md "ms_ad_managed_policies.md")
