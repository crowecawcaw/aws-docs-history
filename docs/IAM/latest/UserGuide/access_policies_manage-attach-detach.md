# Adding and removing IAM identity

permissions

You use policies to define the permissions for an identity (user, user group, or role). You
can add and remove permissions by attaching and detaching IAM policies for an identity using
the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the AWS API. You can also use policies to set [permissions boundaries](access_policies_boundaries.md "access_policies_boundaries.md") for only entities (users or
roles) that are using the same methods. Permissions boundaries are an advanced AWS feature
that control the maximum permissions that an entity can have.

###### Topics

- [Terminology](#attach-detach-etc-terminology "#attach-detach-etc-terminology")
- [View identity activity](#attach-detach_prerequisites "#attach-detach_prerequisites")
- [Adding IAM identity permissions (console)](#add-policies-console "#add-policies-console")
- [Removing IAM identity permissions
  (console)](#remove-policies-console "#remove-policies-console")
- [Adding IAM policies (AWS CLI)](#add-policy-cli "#add-policy-cli")
- [Removing IAM policies (AWS CLI)](#remove-policy-cli "#remove-policy-cli")
- [Adding IAM policies (AWS API)](#add-policy-api "#add-policy-api")
- [Removing IAM policies (AWS API)](#remove-policy-api "#remove-policy-api")

## Terminology

When you associate permissions policies with identities (IAM users, IAM groups, and IAM roles),
terminology and procedures vary depending on whether you are working with a managed or inline
policy:

- **Attach** – Used with managed policies. You
  attach a managed policy to an identity (a user, user group, or role). Attaching a policy
  applies the permissions in the policy to the identity.
- **Detach** – Used with managed policies. You
  detach a managed policy from an IAM identity (a user, user group, or role). Detaching a
  policy removes its permissions from the identity.
- **Embed** – Used with inline policies. You embed
  an inline policy in an identity (a user, user group, or role). Embedding a policy applies
  the permissions in the policy to the identity. Because an inline policy is stored in the
  identity, it is embedded rather than attached, though the results are similar.

###### Note

You can embed an inline policy for a _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ only in the service that depends on the role.
See the [AWS documentation](../../../index.md "../../../index.md") for your service to
see whether it supports this feature.

- **Delete** – Used with inline policies. You delete
  an inline policy from an IAM identity (a user, user group, or role). Deleting a policy
  removes its permissions from the identity.

###### Note

You can delete an inline policy for a _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ only in the service that depends on the role.
See the [AWS documentation](../../../index.md "../../../index.md") for your service to
see whether it supports this feature.

You can use the console, AWS CLI, or AWS API to perform any of these actions.

### More information

- For more information about the difference between managed and inline policies, see
  [Managed policies and inline policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md").
- For more information about permissions boundaries, see [Permissions boundaries for IAM
  entities](access_policies_boundaries.md "access_policies_boundaries.md").
- For general information about IAM policies, see [Policies and permissions in AWS Identity and Access Management](access_policies.md "access_policies.md").
- For information about validating IAM policies, see [IAM policy validation](access_policies_policy-validator.md "access_policies_policy-validator.md").
- The number and size of IAM resources in an AWS account are limited. For more information, see [IAM and AWS STS quotas](reference_iam-quotas.md "reference_iam-quotas.md").

## View identity activity

Before you change the permissions for an identity (user, user group, or role), you should
review their recent service-level activity. This is important because you don't want to remove
access from a principal (person or application) who is using it. For more information about
viewing last accessed information, see [Refine permissions in AWS using last
accessed information](access_policies_last-accessed.md "access_policies_last-accessed.md").

## Adding IAM identity permissions (console)

You can use the AWS Management Console to add permissions to an identity (user, user group, or role).
To do this, attach managed policies that control permissions, or specify a policy that serves
as a [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md"). You can also
embed an inline policy.

###### To use a managed policy as a permissions policy for an identity (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, select the radio button next to the name of the policy to
   attach. You can use the search box to filter the list of policies.
4. Choose **Actions**, and then choose
   **Attach**.
5. Select one or more identities to attach the policy to. You can use the search box to
   filter the list of principal entities. After selecting the identities, choose
   **Attach policy**.

###### To use a managed policy to set a permissions boundary (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the name of the policy to set. You can use the search
   box to filter the list of policies.
4. On the policy details page, choose the **Entities attached** tab, and
   then, if necessary, open the **Attached as a permissions boundaries**
   section and choose **Set this policy as a permissions boundary**.
5. Select one or more users or roles on which to use the policy for a permissions
   boundary. You can use the search box to filter the list of principal entities. After
   selecting the principals, choose **Set permissions boundary**.

###### To embed an inline policy for a user or role

(console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users** or
   **Roles**.
3. In the list, choose the name of the user or role to embed a policy in.
4. Choose the **Permissions** tab.
5. Choose **Add permissions** and then choose **Create inline
   policy**.

###### Note

You cannot embed an inline policy in a _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_ in IAM. Because the linked service defines
whether you can modify the permissions of the role, you might be able to add additional
policies from the service console, API, or AWS CLI. To view the service-linked role
documentation for a service, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md") and choose
**Yes** in the **Service-Linked Role** column for
your service. 6. Choose from the following methods to view the steps required to create your
policy:

    * [Importing existing managed policies](access_policies_create-console.md#access_policies_create-copy "access_policies_create-console.md#access_policies_create-copy") – You can import a managed
     policy within your account and then edit the policy to customize it to your specific
     requirements. A managed policy can be an AWS managed policy or a customer managed
     policy that you created previously.
    * [Creating policies with the visual
     editor](access_policies_create-console.md#access_policies_create-visual-editor "access_policies_create-console.md#access_policies_create-visual-editor") – You can construct a
     new policy from scratch in the visual editor. If you use the visual editor, you do not
     have to understand JSON syntax.
    * [Creating policies using the JSON
     editor](access_policies_create-console.md#access_policies_create-json-editor "access_policies_create-console.md#access_policies_create-json-editor") – In the
     **JSON** editor option, you can use JSON syntax to create a policy.
     You can type a new JSON policy document or paste an [example policy](access_policies_examples.md "access_policies_examples.md").

7. After you create an inline policy, it is automatically embedded in your user or
   role.

###### To embed an inline policy for a user group (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups**.
3. In the list, choose the name of the user group to embed a policy in.
4. Choose the **Permissions** tab, choose **Add
   permissions**, and then choose **Create inline
   policy**.
5. Do one of the following:
   - Choose the **Visual** option to create the policy. For more
     information, see [Creating policies with the visual
     editor](access_policies_create-console.md#access_policies_create-visual-editor "access_policies_create-console.md#access_policies_create-visual-editor").
   - Choose the **JSON** option to create the policy. For more
     information, see [Creating policies using the JSON
     editor](access_policies_create-console.md#access_policies_create-json-editor "access_policies_create-console.md#access_policies_create-json-editor").

6. When you are satisfied with the policy, choose **Create
   policy**.

###### To change the permissions boundary for one or more entities (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the name of the policy to set. You can use the search
   box to filter the list of policies.
4. On the policy details page, choose the **Entities attached** tab, and
   then, if necessary, open the **Attached as a permissions boundary**
   section. Select the checkbox next to the users or roles whose boundaries you want to
   change and then choose **Change**.
5. Select a new policy to use for a permissions boundary. You can use the search box to
   filter the list of policies. After selecting the policy, choose **Set permissions
   boundary**.

## Removing IAM identity permissions

(console)

You can use the AWS Management Console to remove permissions from an identity (user, user group, or
role). To do this, detach managed policies that control permissions, or remove a policy that
serves as a [permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md"). You can
also delete an inline policy.

###### To detach a managed policy used as a permissions policy (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, select the radio button next to the name of the policy to
   detach. You can use the search box to filter the list of policies.
4. Choose **Actions**, and then choose
   **Detach**.
5. Select the identities to detach the policy from. You can use the search box to filter
   the list of identities. After selecting the identities, choose **Detach
   policy**.

###### To remove a permissions boundary (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.
3. In the list of policies, choose the name of the policy to set. You can use the search
   box to filter the list of policies.
4. On the policy summary page, choose the **Entities attached** tab, and
   then, if necessary, open the **Attached as a permissions boundary**
   section and choose the entities to remove the permissions boundary from. Then choose
   **Remove boundary**.
5. Confirm that you want to remove the boundary and choose **Remove
   boundary**.

###### To delete an inline policy (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **User groups**,
   **Users**, or **Roles**.
3. In the list, choose the name of the user group, user, or role that has the policy you
   want to remove.
4. Choose the **Permissions** tab.
5. Select the checkbox next to the policy and choose **Remove**.
6. Choose **Remove** in the confirmation box.

## Adding IAM policies (AWS CLI)

You can use the AWS CLI to add permissions to an identity (user, user group, or role). To do
this, attach managed policies that control permissions, or specify a policy that serves as a
[permissions boundary](access_policies_boundaries.md "access_policies_boundaries.md"). You can also embed
an inline policy.

###### To use a managed policy as a permissions policy for an entity (AWS CLI)

1. (Optional) To view information about a managed policy, run the following commands:
   - To list managed policies: [aws iam
     list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")
   - To retrieve detailed information about a managed policy: [get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md")

2. To attach a managed policy to an identity (user, user group, or role), use one of the
   following commands:
   - [aws iam
     attach-user-policy](../../../cli/latest/reference/iam/attach-user-policy.md "../../../cli/latest/reference/iam/attach-user-policy.md")
   - [aws iam
     attach-group-policy](../../../cli/latest/reference/iam/attach-group-policy.md "../../../cli/latest/reference/iam/attach-group-policy.md")
   - [aws iam
     attach-role-policy](../../../cli/latest/reference/iam/attach-role-policy.md "../../../cli/latest/reference/iam/attach-role-policy.md")

###### To use a managed policy to set a permissions boundary (AWS CLI)

1. (Optional) To view information about a managed policy, run the following commands:
   - To list managed policies: [aws iam
     list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")
   - To retrieve detailed information about a managed policy: [aws iam get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md")

2. To use a managed policy to set the permissions boundary for an entity (user or role),
   use one of the following commands:
   - [aws iam
     put-user-permissions-boundary](../../../cli/latest/reference/iam/put-user-permissions-boundary.md "../../../cli/latest/reference/iam/put-user-permissions-boundary.md")
   - [aws iam
     put-role-permissions-boundary](../../../cli/latest/reference/iam/put-role-permissions-boundary.md "../../../cli/latest/reference/iam/put-role-permissions-boundary.md")

###### To embed an inline policy (AWS CLI)

To embed an inline policy to an identity (user, user group, or role that is not a
_[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_), use
one of the following commands:

- [aws iam
  put-user-policy](../../../cli/latest/reference/iam/put-user-policy.md "../../../cli/latest/reference/iam/put-user-policy.md")
- [aws iam
  put-group-policy](../../../cli/latest/reference/iam/put-group-policy.md "../../../cli/latest/reference/iam/put-group-policy.md")
- [aws iam
  put-role-policy](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md")

## Removing IAM policies (AWS CLI)

You can use the AWS CLI to detach managed policies that control permissions, or remove a
policy that serves as a [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md"). You can also delete an inline policy.

###### To detach a managed policy used as a permissions policy (AWS CLI)

1. (Optional) To view information about a policy, run the following commands:
   - To list managed policies: [aws iam
     list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")
   - To retrieve detailed information about a managed policy: [aws iam get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md")

2. (Optional) To find out about the relationships between the policies and identities,
   run the following commands:
   - To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy
     is attached:
     - [aws iam
       list-entities-for-policy](../../../cli/latest/reference/iam/list-entities-for-policy.md "../../../cli/latest/reference/iam/list-entities-for-policy.md")

   - To list the managed policies attached to an identity (a user, user group, or
     role), use one of the following commands:
     - [aws iam
       list-attached-user-policies](../../../cli/latest/reference/iam/list-attached-user-policies.md "../../../cli/latest/reference/iam/list-attached-user-policies.md")
     - [aws iam
       list-attached-group-policies](../../../cli/latest/reference/iam/list-attached-group-policies.md "../../../cli/latest/reference/iam/list-attached-group-policies.md")
     - [aws iam
       list-attached-role-policies](../../../cli/latest/reference/iam/list-attached-role-policies.md "../../../cli/latest/reference/iam/list-attached-role-policies.md")

3. To detach a managed policy from an identity (user, user group, or role), use one of
   the following commands:
   - [aws iam
     detach-user-policy](../../../cli/latest/reference/iam/detach-user-policy.md "../../../cli/latest/reference/iam/detach-user-policy.md")
   - [aws iam
     detach-group-policy](../../../cli/latest/reference/iam/detach-group-policy.md "../../../cli/latest/reference/iam/detach-group-policy.md")
   - [aws iam
     detach-role-policy](../../../cli/latest/reference/iam/detach-role-policy.md "../../../cli/latest/reference/iam/detach-role-policy.md")

###### To remove a permissions boundary (AWS CLI)

1. (Optional) To view which managed policy is currently used to set the permissions
   boundary for a user or role, run the following commands:
   - [aws iam get-user](../../../cli/latest/reference/iam/get-user.md "../../../cli/latest/reference/iam/get-user.md")
   - [aws iam get-role](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md")

2. (Optional) To view the users or roles on which a managed policy is used for a
   permissions boundary, run the following command:
   - [aws iam
     list-entities-for-policy](../../../cli/latest/reference/iam/list-entities-for-policy.md "../../../cli/latest/reference/iam/list-entities-for-policy.md")

3. (Optional) To view information about a managed policy, run the following
   commands:
   - To list managed policies: [aws iam
     list-policies](../../../cli/latest/reference/iam/list-policies.md "../../../cli/latest/reference/iam/list-policies.md")
   - To retrieve detailed information about a managed policy: [aws iam get-policy](../../../cli/latest/reference/iam/get-policy.md "../../../cli/latest/reference/iam/get-policy.md")

4. To remove a permissions boundary from a user or role, use one of the following
   commands:
   - [aws iam
     delete-user-permissions-boundary](../../../cli/latest/reference/iam/detach-user-policy.md "../../../cli/latest/reference/iam/detach-user-policy.md")
   - [aws iam
     delete-role-permissions-boundary](../../../cli/latest/reference/iam/delete-role-permissions-boundary.md "../../../cli/latest/reference/iam/delete-role-permissions-boundary.md")

###### To delete an inline policy (AWS CLI)

1. (Optional) To list all inline policies that are attached to an identity (user, user
   group, role), use one of the following commands:
   - [aws iam
     list-user-policies](../../../cli/latest/reference/iam/list-user-policies.md "../../../cli/latest/reference/iam/list-user-policies.md")
   - [aws iam
     list-group-policies](../../../cli/latest/reference/iam/list-group-policies.md "../../../cli/latest/reference/iam/list-group-policies.md")
   - [aws iam
     list-role-policies](../../../cli/latest/reference/iam/list-role-policies.md "../../../cli/latest/reference/iam/list-role-policies.md")

2. (Optional) To retrieve an inline policy document that is embedded in an identity
   (user, user group, or role), use one of the following commands:
   - [aws iam
     get-user-policy](../../../cli/latest/reference/iam/get-user-policy.md "../../../cli/latest/reference/iam/get-user-policy.md")
   - [aws iam
     get-group-policy](../../../cli/latest/reference/iam/get-group-policy.md "../../../cli/latest/reference/iam/get-group-policy.md")
   - [aws iam
     get-role-policy](../../../cli/latest/reference/iam/get-role-policy.md "../../../cli/latest/reference/iam/get-role-policy.md")

3. To delete an inline policy from an identity (user, user group, or role that is not a
   _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_),
   use one of the following commands:
   - [aws iam
     delete-user-policy](../../../cli/latest/reference/iam/delete-user-policy.md "../../../cli/latest/reference/iam/delete-user-policy.md")
   - [aws iam
     delete-group-policy](../../../cli/latest/reference/iam/delete-group-policy.md "../../../cli/latest/reference/iam/delete-group-policy.md")
   - [aws iam
     delete-role-policy](../../../cli/latest/reference/iam/delete-role-policy.md "../../../cli/latest/reference/iam/delete-role-policy.md")

## Adding IAM policies (AWS API)

You can use the AWS API to attach managed policies that control permissions or specify a
policy that serves as a [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md"). You can also embed an inline policy.

###### To use a managed policy as a permissions policy for an entity (AWS API)

1. (Optional) To view information about a policy, call the following operations:
   - To list managed policies: [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
   - To retrieve detailed information about a managed policy: [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md")

2. To attach a managed policy to an identity (user, user group, or role), call one of the
   following operations:
   - [AttachUserPolicy](../APIReference/API_AttachUserPolicy.md "../APIReference/API_AttachUserPolicy.md")
   - [AttachGroupPolicy](../APIReference/API_AttachGroupPolicy.md "../APIReference/API_AttachGroupPolicy.md")
   - [AttachRolePolicy](../APIReference/API_AttachRolePolicy.md "../APIReference/API_AttachRolePolicy.md")

###### To use a managed policy to set a permissions boundary (AWS API)

1. (Optional) To view information about a managed policy, call the following operations:
   - To list managed policies: [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
   - To retrieve detailed information about a managed policy: [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md")

2. To use a managed policy to set the permissions boundary for an entity (user or role),
   call one of the following operations:
   - [PutUserPermissionsBoundary](../APIReference/API_PutUserPermissionsBoundary.md "../APIReference/API_PutUserPermissionsBoundary.md")
   - [PutRolePermissionsBoundary](../APIReference/API_PutRolePermissionsBoundary.md "../APIReference/API_PutRolePermissionsBoundary.md")

###### To embed an inline policy (AWS API)

To embed an inline policy in an identity (user, user group, or role that is not a
_[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_),
call one of the following operations:

- [PutUserPolicy](../APIReference/API_PutUserPolicy.md "../APIReference/API_PutUserPolicy.md")
- [PutGroupPolicy](../APIReference/API_PutGroupPolicy.md "../APIReference/API_PutGroupPolicy.md")
- [PutRolePolicy](../APIReference/API_PutRolePolicy.md "../APIReference/API_PutRolePolicy.md")

## Removing IAM policies (AWS API)

You can use the AWS API to detach managed policies that control permissions or remove a
policy that serves as a [permissions
boundary](access_policies_boundaries.md "access_policies_boundaries.md"). You can also delete an inline policy.

###### To detach a managed policy used as a permissions policy (AWS API)

1. (Optional) To view information about a policy, call the following operations:
   - To list managed policies: [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
   - To retrieve detailed information about a managed policy: [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md")

2. (Optional) To find out about the relationships between the policies and identities,
   call the following operations:
   - To list the identities (IAM users, IAM groups, and IAM roles) to which a managed policy
     is attached:
     - [ListEntitiesForPolicy](../APIReference/API_ListEntitiesForPolicy.md "../APIReference/API_ListEntitiesForPolicy.md")

   - To list the managed policies attached to an identity (a user, user group, or
     role), call one of the following operations:
     - [ListAttachedUserPolicies](../APIReference/API_ListAttachedUserPolicies.md "../APIReference/API_ListAttachedUserPolicies.md")
     - [ListAttachedGroupPolicies](../APIReference/API_ListAttachedGroupPolicies.md "../APIReference/API_ListAttachedGroupPolicies.md")
     - [ListAttachedRolePolicies](../APIReference/API_ListAttachedRolePolicies.md "../APIReference/API_ListAttachedRolePolicies.md")

3. To detach a managed policy from an identity (user, user group, or role), call one of
   the following operations:
   - [DetachUserPolicy](../APIReference/API_DetachUserPolicy.md "../APIReference/API_DetachUserPolicy.md")
   - [DetachGroupPolicy](../APIReference/API_DetachGroupPolicy.md "../APIReference/API_DetachGroupPolicy.md")
   - [DetachRolePolicy](../APIReference/API_DetachRolePolicy.md "../APIReference/API_DetachRolePolicy.md")

###### To remove a permissions boundary (AWS API)

1. (Optional) To view which managed policy is currently used to set the permissions
   boundary for a user or role, call the following operations:
   - [GetUser](../APIReference/API_GetUser.md "../APIReference/API_GetUser.md")
   - [GetRole](../APIReference/API_GetRole.md "../APIReference/API_GetRole.md")

2. (Optional) To view the users or roles on which a managed policy is used for a
   permissions boundary, call the following operation:
   - [ListEntitiesForPolicy](../APIReference/API_ListEntitiesForPolicy.md "../APIReference/API_ListEntitiesForPolicy.md")

3. (Optional) To view information about a managed policy, call the following
   operations:
   - To list managed policies: [ListPolicies](../APIReference/API_ListPolicies.md "../APIReference/API_ListPolicies.md")
   - To retrieve detailed information about a managed policy: [GetPolicy](../APIReference/API_GetPolicy.md "../APIReference/API_GetPolicy.md")

4. To remove a permissions boundary from a user or role, call one of the following
   operations:
   - [DeleteUserPermissionsBoundary](../APIReference/API_DeleteUserPermissionsBoundary.md "../APIReference/API_DeleteUserPermissionsBoundary.md")
   - [DeleteRolePermissionsBoundary](../APIReference/API_DeleteRolePermissionsBoundary.md "../APIReference/API_DeleteRolePermissionsBoundary.md")

###### To delete an inline policy (AWS API)

1. (Optional) To list all inline policies that are attached to an identity (user, user
   group, role), call one of the following operations:
   - [ListUserPolicies](../APIReference/API_ListUserPolicies.md "../APIReference/API_ListUserPolicies.md")
   - [ListGroupPolicies](../APIReference/API_ListGroupPolicies.md "../APIReference/API_ListGroupPolicies.md")
   - [ListRolePolicies](../APIReference/API_ListRolePolicies.md "../APIReference/API_ListRolePolicies.md")

2. (Optional) To retrieve an inline policy document that is embedded in an identity
   (user, user group, or role), call one of the following operations:
   - [GetUserPolicy](../APIReference/API_GetUserPolicy.md "../APIReference/API_GetUserPolicy.md")
   - [GetGroupPolicy](../APIReference/API_GetGroupPolicy.md "../APIReference/API_GetGroupPolicy.md")
   - [GetRolePolicy](../APIReference/API_GetRolePolicy.md "../APIReference/API_GetRolePolicy.md")

3. To delete an inline policy from an identity (user, user group, or role that is not a
   _[service-linked role](id_roles.md#iam-term-service-linked-role "id_roles.md#iam-term-service-linked-role")_),
   call one of the following operations:
   - [DeleteUserPolicy](../APIReference/API_DeleteUserPolicy.md "../APIReference/API_DeleteUserPolicy.md")
   - [DeleteGroupPolicy](../APIReference/API_DeleteGroupPolicy.md "../APIReference/API_DeleteGroupPolicy.md")
   - [DeleteRolePolicy](../APIReference/API_DeleteRolePolicy.md "../APIReference/API_DeleteRolePolicy.md")
