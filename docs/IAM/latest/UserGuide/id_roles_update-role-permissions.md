# Update permissions for a role

Use the following procedures to update a role's permissions policies and permissions
boundaries.

## Prerequisite: View role access

Before you change the permissions for a role, you should review its recent service-level
activity. This is important because you don't want to remove access from a principal (person
or application) who is using it. For more information about viewing last accessed information,
see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Update the permissions

policy for a role

To change the permissions allowed by the role, modify the role's permissions policy
(or policies). You cannot modify the permissions policy for a _[service-linked
role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ in IAM. You might be able to modify the permissions policy
within the service that depends on the role. To check whether a service supports this
feature, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md") and look for the
services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

###### To change the permissions allowed by a role (console)

1.  Open the IAM console at
    [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose
    **Roles**.
3.  Choose the name of the role that you want to modify, and then choose
    the **Permissions** tab.
4.  Do one of the following:

        * To edit an existing customer managed policy, choose the name
         of the policy and then choose **Edit
         policy**.


        ###### Note

        You cannot edit an AWS managed policy. AWS managed
         policies appear with the AWS icon (
        ![Orange cube icon indicating a policy is managed by AWS.](/images/IAM/latest/UserGuide/images/policy_icon.png)
        ). For more information about the
         difference between AWS managed policies and customer
         managed policies, see [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md").
        * To attach an existing managed policy to the role, choose
         **Add permissions** and then choose
         **Attach policies**.
        * To edit an existing inline policy, expand the policy and
         choose **Edit**.
        * To embed a new inline policy, choose **Add
         permissions** and then choose **Create
         inline policy**.
        * To remove an existing policy from the role, select the check
         box next to the policy name and then choose
         **Remove**.

    To change the permissions allowed by the role, modify the role's permissions
    policy (or policies). You cannot modify the permissions policy for a
    _[service-linked
    role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ in IAM. You might be able to modify the permissions
    policy within the service that depends on the role. To check whether a service
    supports this feature, see [AWS services that work with
    IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md") and look for the
    services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role
    documentation for that service.

###### To change the permissions allowed by a role (AWS CLI)

1. (Optional) To view the current permissions associated with a role, run
   the following commands:
   1. [aws iam
      list-role-policies](../../../cli/latest/reference/iam/list-role-policies.md "../../../cli/latest/reference/iam/list-role-policies.md") to list inline policies
   2. [aws iam list-attached-role-policies](../../../cli/latest/reference/iam/list-attached-role-policies.md "../../../cli/latest/reference/iam/list-attached-role-policies.md") to list managed
      policies

2. The command to update permissions for the role differs depending on
   whether you are updating a managed policy or an inline policy.

To update a managed policy, run the following command to create a new
version of the managed policy:

    * [aws
     iam create-policy-version](../../../cli/latest/reference/iam/create-policy-version.md "../../../cli/latest/reference/iam/create-policy-version.md")

To update an inline policy, run the following command:

    * [aws iam
     put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")

To change the permissions allowed by the role, modify the role's permissions
policy (or policies). You cannot modify the permissions policy for a
_[service-linked
role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ in IAM. You might be able to modify the permissions
policy within the service that depends on the role. To check whether a service
supports this feature, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md") and look for the
services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role
documentation for that service.

###### To change the permissions allowed by a role (AWS API)

1. (Optional) To view the current permissions associated with a role,
   call the following operations:
   1. [ListRolePolicies](../APIReference/API_ListRolePolicies.md "../APIReference/API_ListRolePolicies.md") to list inline policies
   2. [ListAttachedRolePolicies](../APIReference/API_ListAttachedRolePolicies.md "../APIReference/API_ListAttachedRolePolicies.md") to list managed
      policies

2. The operation to update permissions for the role differs depending on
   whether you are updating a managed policy or an inline policy.

To update a managed policy, call the following operation to create a
new version of the managed policy:

    * [CreatePolicyVersion](../APIReference/API_CreatePolicyVersion.md "../APIReference/API_CreatePolicyVersion.md")

To update an inline policy, call the following operation:

    * [PutRolePolicy](../APIReference/API_PutRolePolicy.md "../APIReference/API_PutRolePolicy.md")

## Update the permissions

boundary for a role

To change the maximum permissions allowed for a role, modify the role's [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md").

###### To change the policy used to set the permissions boundary for a

role

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Choose the name of the role with the [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md")
   that you want to change.
4. Choose the **Permissions** tab. If necessary, open
   the **Permissions boundary** section and then choose
   **Change boundary**.
5. Select the policy that you want to use for the permissions
   boundary.
6. Choose **Change boundary**.

Your changes don't take effect until the next time someone assumes
this role.

###### To change the managed policy used to set the permissions boundary for a

role (AWS CLI)

1.  (Optional) To view the current [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md") for
    a role, run the following command:
    - [aws iam
      get-role](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md")

2.  To use a different managed policy to update the permissions boundary
    for a role, run the following command:

        * [aws iam put-role-permissions-boundary](../../../cli/latest/reference/iam/put-role-permissions-boundary.md "../../../cli/latest/reference/iam/put-role-permissions-boundary.md")

    A role can have only one managed policy set as a permissions boundary.
    If you change the permissions boundary, you change the maximum
    permissions allowed for a role.

###### To change the managed policy used to set the permissions boundary for a

role (AWS API)

1.  (Optional) To view the current [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md") for
    a role, call the following operation:
    - [GetRole](../APIReference/API_GetRole.md "../APIReference/API_GetRole.md")

2.  To use a different managed policy to update the permissions boundary
    for a role, call the following operation:

        * [PutRolePermissionsBoundary](../APIReference/API_PutRolePermissionsBoundary.md "../APIReference/API_PutRolePermissionsBoundary.md")

    A role can have only one managed policy set as a permissions boundary.
    If you change the permissions boundary, you change the maximum
    permissions allowed for a role.
