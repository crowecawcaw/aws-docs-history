# IAM role management

Before a user, application, or service can use a role that you created, you must grant
permissions to switch to the role. You can use any policy attached to groups or users to grant
the necessary permissions. This section describes how to grant users permission to use a role.
It also explains how the user can switch to a role from the AWS Management Console, the Tools for Windows PowerShell, the AWS Command Line Interface
(AWS CLI) and the [`AssumeRole`](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md")
API.

###### Important

When you create a role programmatically instead of in the IAM console, you have an
option to add a `Path` of up to 512 characters in addition to the
`RoleName`, which can be up to 64 characters long. However, if you intend to use
a role with the **Switch Role** feature in the AWS Management Console, then the combined
`Path` and `RoleName` cannot exceed 64 characters.

###### Topics

- [View role access](#roles-modify_prerequisites "#roles-modify_prerequisites")
- [Generate a policy based on access
  information](#roles-modify_gen-policy "#roles-modify_gen-policy")
- [Grant a user permissions to switch
  roles](id_roles_use_permissions-to-switch.md "id_roles_use_permissions-to-switch.md")
- [Grant a user permissions to pass a role to an AWS
  service](id_roles_use_passrole.md "id_roles_use_passrole.md")
- [Revoke IAM role temporary security
  credentials](id_roles_use_revoke-sessions.md "id_roles_use_revoke-sessions.md")
- [Update a service-linked role](id_roles_update-service-linked-role.md "id_roles_update-service-linked-role.md")
- [Update a role trust policy](id_roles_update-role-trust-policy.md "id_roles_update-role-trust-policy.md")
- [Update permissions for a role](id_roles_update-role-permissions.md "id_roles_update-role-permissions.md")
- [Update settings for a role](id_roles_update-role-settings.md "id_roles_update-role-settings.md")
- [Delete roles or instance profiles](id_roles_manage_delete.md "id_roles_manage_delete.md")

## View role access

Before you change the permissions for a role, you should review its recent service-level
activity. This is important because you don't want to remove access from a principal (person
or application) who is using it. For more information about viewing last accessed information,
see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Generate a policy based on access

information

You might sometimes grant permissions to an IAM entity (user or role) beyond what they
require. To help you refine the permissions that you grant, you can generate an IAM policy
that is based on the access activity for an entity. IAM Access Analyzer reviews your AWS CloudTrail logs
and generates a policy template that contains the permissions that have been used by the
entity in your specified date range. You can use the template to create a managed policy with
fine-grained permissions and then attach it to the IAM entity. That way, you grant only the
permissions that the user or role needs to interact with AWS resources for your specific use
case. To learn more, see [IAM Access Analyzer policy
generation](access-analyzer-policy-generation.md "access-analyzer-policy-generation.md").
