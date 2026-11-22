

AWS Well-Architected Agent is in preview release and is subject to change.

# Service-linked role permissions for AWS Well-Architected Agent Organizations access

AWS Well-Architected Agent uses the service-linked role named ``. AWS WA Agent uses this service-linked role to read your organization structure and delegated administrator information in AWS Organizations when you enable the agent's organization integration. This role exists in the management account only.

The `` service-linked role trusts the following service to assume the role:
+ `agent.wellarchitected.amazonaws.com`

The role permissions policy is the AWS managed policy named `AWSWellArchitectedAgentOrganizationsServiceRolePolicy`. This policy allows AWS WA Agent to access organizational structure and delegated administrator information in AWS Organizations on your behalf. The policy grants read-only list and describe access to your organization structure and delegated administrators. For the full list of actions, see the reference. For more details about this policy, including the full JSON policy document, see [AWSWellArchitectedAgentOrganizationsServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSWellArchitectedAgentOrganizationsServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS WA Agent Organizations access
<a name="using-service-linked-roles-agent-organizations-creating"></a>

You don't need to manually create the `` service-linked role. AWS WA Agent creates the role inline in the management account when you enable the agent's organization integration. This is the same single action that creates the `` resource-scanning role in the management account. For more information about enabling the organization integration, see [Trusted access with AWS Organizations](agent-preferences.md#agent-preferences-trusted-access).

If you delete this service-linked role and then need to create it again, you can use the same process to recreate the role in your account.

## Editing a service-linked role for AWS WA Agent Organizations access
<a name="using-service-linked-roles-agent-organizations-editing"></a>

AWS Well-Architected does not allow you to edit the `` service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS WA Agent Organizations access
<a name="using-service-linked-roles-agent-organizations-deleting"></a>

If you no longer need to use AWS Well-Architected Agent, we recommend that you delete the `` service-linked role.

You delete the `` role the same way you delete any service-linked role, by using the IAM console, the AWS Command Line Interface (AWS CLI), or the IAM API. Unlike the `` resource-scanning role, deleting this role is not gated on disabling trusted access. We recommend that you disable the agent's organization integration before you remove the role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported AWS Regions for AWS WA Agent Organizations access service-linked roles
<a name="using-service-linked-roles-agent-organizations-regions"></a>

AWS Well-Architected supports using the `` service-linked role in the following AWS Regions.