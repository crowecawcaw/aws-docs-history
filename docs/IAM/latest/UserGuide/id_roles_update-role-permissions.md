

# Update permissions for a role
<a name="id_roles_update-role-permissions"></a>

Use the following procedures to update a role's permissions policies and permissions boundaries.

## Prerequisite: View role access
<a name="roles-modify_prerequisites"></a>

Before you change the permissions for a role, you should review its recent service-level activity. This is important because you don't want to remove access from a principal (person or application) who is using it. For more information about viewing last accessed information, see [Refine permissions in AWS using last accessed information](access_policies_last-accessed.md).

## Update the permissions policy for a role
<a name="id_roles_update-role-permissions-policy"></a>

To change the permissions allowed by the role, modify the role's permissions policy (or policies). You cannot modify the permissions policy for a *[service-linked role](id_roles.md#iam-term-service-linked-role)* in IAM. You might be able to modify the permissions policy within the service that depends on the role. To check whether a service supports this feature, see [AWS services that work with IAM](reference_aws-services-that-work-with-iam.md) and look for the services that have **Yes **in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

### Updating a role permissions policy (console)
<a name="id_roles_update-role-permissions-policy-console"></a>

**To change the permissions allowed by a role (console)**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the IAM console, choose **Roles**.

1. Choose the name of the role that you want to modify, and then choose the **Permissions** tab.

1. Do one of the following:
   + To edit an existing customer managed policy, choose the name of the policy and then choose **Edit policy**.
**Note**  
You cannot edit an AWS managed policy. AWS managed policies appear with the AWS icon (![Orange cube icon indicating a policy is managed by AWS.](http://docs.aws.amazon.com/IAM/latest/UserGuide/images/policy_icon.png)). For more information about the difference between AWS managed policies and customer managed policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md). 
   + To attach an existing managed policy to the role, choose **Add permissions** and then choose **Attach policies**.
   + To edit an existing inline policy, expand the policy and choose **Edit**.
   + To embed a new inline policy, choose **Add permissions** and then choose **Create inline policy**. 
   + To remove an existing policy from the role, select the check box next to the policy name and then choose **Remove**.

### Updating a role permissions policy (AWS CLI)
<a name="id_roles_update_permissions-policy-cli"></a>

To change the permissions allowed by the role, modify the role's permissions policy (or policies). You cannot modify the permissions policy for a *[service-linked role](id_roles.md#iam-term-service-linked-role)* in IAM. You might be able to modify the permissions policy within the service that depends on the role. To check whether a service supports this feature, see [AWS services that work with IAM](reference_aws-services-that-work-with-iam.md) and look for the services that have **Yes **in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**To change the permissions allowed by a role (AWS CLI)**

1. (Optional) To view the current permissions associated with a role, run the following commands:

   1. [aws iam list-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-role-policies.html) to list inline policies

   1. [aws iam list-attached-role-policies](https://docs.aws.amazon.com/cli/latest/reference/iam/list-attached-role-policies.html) to list managed policies

1. The command to update permissions for the role differs depending on whether you are updating a managed policy or an inline policy.

   To update a managed policy, run the following command to create a new version of the managed policy:
   + [aws iam create-policy-version](https://docs.aws.amazon.com/cli/latest/reference/iam/create-policy-version.html)

   To update an inline policy, run the following command:
   + [aws iam put-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-policy.html)

### Updating a role permissions policy (AWS API)
<a name="id_roles_update_permissions-policy-api"></a>

To change the permissions allowed by the role, modify the role's permissions policy (or policies). You cannot modify the permissions policy for a *[service-linked role](id_roles.md#iam-term-service-linked-role)* in IAM. You might be able to modify the permissions policy within the service that depends on the role. To check whether a service supports this feature, see [AWS services that work with IAM](reference_aws-services-that-work-with-iam.md) and look for the services that have **Yes **in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

**To change the permissions allowed by a role (AWS API)**

1. (Optional) To view the current permissions associated with a role, call the following operations:

   1. [ListRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRolePolicies.html) to list inline policies

   1. [ListAttachedRolePolicies](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListAttachedRolePolicies.html) to list managed policies

1. The operation to update permissions for the role differs depending on whether you are updating a managed policy or an inline policy.

   To update a managed policy, call the following operation to create a new version of the managed policy:
   + [CreatePolicyVersion](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreatePolicyVersion.html)

   To update an inline policy, call the following operation:
   + [PutRolePolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePolicy.html)

## Update the permissions boundary for a role
<a name="id_roles_update-role-permissions-boundary"></a>

To change the maximum permissions allowed for a role, modify the role's [permissions boundary](access_policies_boundaries.md).

### Updating a role permissions boundary (console)
<a name="id_roles_update-permissions-boundary-console"></a>

**To change the policy used to set the permissions boundary for a role**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Roles**.

1. Choose the name of the role with the [permissions boundary](access_policies_boundaries.md) that you want to change. 

1. Choose the **Permissions** tab. If necessary, open the **Permissions boundary** section and then choose **Change boundary**.

1. Select the policy that you want to use for the permissions boundary.

1. Choose **Change boundary**.

   Your changes don't take effect until the next time someone assumes this role.

### Updating a role permissions boundary (AWS CLI)
<a name="id_roles_update_permissions-boundary-cli"></a>

**To change the managed policy used to set the permissions boundary for a role (AWS CLI)**

1. (Optional) To view the current [permissions boundary](access_policies_boundaries.md) for a role, run the following command: 
   + [aws iam get-role](https://docs.aws.amazon.com/cli/latest/reference/iam/get-role.html)

1. To use a different managed policy to update the permissions boundary for a role, run the following command: 
   + [aws iam put-role-permissions-boundary](https://docs.aws.amazon.com/cli/latest/reference/iam/put-role-permissions-boundary.html)

   A role can have only one managed policy set as a permissions boundary. If you change the permissions boundary, you change the maximum permissions allowed for a role.

### Updating a role permissions boundary (AWS API)
<a name="id_roles_update-permissions-boundary-api"></a>

**To change the managed policy used to set the permissions boundary for a role (AWS API)**

1. (Optional) To view the current [permissions boundary](access_policies_boundaries.md) for a role, call the following operation: 
   + [GetRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetRole.html)

1. To use a different managed policy to update the permissions boundary for a role, call the following operation: 
   + [PutRolePermissionsBoundary](https://docs.aws.amazon.com/IAM/latest/APIReference/API_PutRolePermissionsBoundary.html)

   A role can have only one managed policy set as a permissions boundary. If you change the permissions boundary, you change the maximum permissions allowed for a role.