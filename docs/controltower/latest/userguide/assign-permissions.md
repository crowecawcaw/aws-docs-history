# Create roles and assign permissions

Roles and permissions give you access to resources, in AWS Control Tower and in other
AWS services, including programmatic access to resources.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:

      + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the *IAM User Guide*.
      + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the *IAM User Guide*.

  For more information about using IAM to delegate permissions, see [Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
  _IAM User Guide_.

###### Note

When setting up an AWS Control Tower landing zone, you'll need a user or role with
the **AdministratorAccess** managed policy.
(arn:aws:iam::aws:policy/AdministratorAccess)

###### To create a role for an AWS service (IAM console)

1.  Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2.  In the navigation pane of the IAM console, choose **Roles**, and
    then choose **Create role**.
3.  For **Trusted entity type**, choose **AWS service**.
4.  For **Service or use case**, choose a service, and then choose the use case. Use cases are defined by the service to include the trust policy
    that the service requires.
5.  Choose **Next**.
6.  For **Permissions policies**, the options depend on the use case that you selected:
    - If the service defines the permissions for the role, you can't select permissions policies.
    - Select from a limited set of permission polices.
    - Select from all permission policies.
    - Select no permissions policies, create the policies after the role is created, and then attach the policies to the role.

7.  (Optional) Set a [permissions
    boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for service roles, but
    not service-linked roles.
    1. Open the **Set permissions boundary** section, and then choose
       **Use a permissions boundary to control the maximum role
       permissions**.

    IAM includes a list of the AWS managed and customer-managed policies in your account. 2. Select the policy to use for the permissions boundary.

8.  Choose **Next**.
9.  For **Role name**, the options depend on the service:
    - If the service defines the role name, you can't edit the role name.
    - If the service defines a prefix for the role name, you can enter an optional suffix.
    - If the service doesn't define the role name, you can name the role.

    ###### Important

    When you name a role, note the following:

        + Role names must be unique within your AWS account, and can't be made unique by case.


        For example, don't create roles named both `PRODROLE` and
         `prodrole`. When a role name is used in a policy or as part of an ARN, the role name is case sensitive, however when a role name appears to customers in the console, such as during the sign-in process, the role name is case insensitive.
        + You can't edit the name of the role after it's created because other entities might reference the role.

10. (Optional) For **Description**, enter a description for the role.
11. (Optional) To edit
    the use cases and permissions for the role, in the **Step 1: Select trusted
    entities** or **Step 2: Add permissions** sections, choose **Edit**.
12. (Optional) To help identify, organize, or search for the role, add tags as key-value pairs. For more
    information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
13. Review the role, and then choose **Create role**.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter or paste a JSON policy document. For details about the IAM policy language, see
[IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md"). 6. Resolve any security warnings, errors, or general warnings generated during [policy validation](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md"), and then choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON
or YAML policy template that you can use in AWS CloudFormation templates.

To do this, in the **Policy editor** choose
**Actions**, and then choose **Generate CloudFormation
template**. To learn more about AWS CloudFormation, see [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_. 8. When you are finished adding permissions to the policy, choose
**Next**. 9. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 10. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 11. Choose **Create policy** to save your new policy.

###### To use the visual editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. Choose **Create policy**. 4. In the **Policy editor** section, find the **Select a
service** section, and then choose an AWS service. You can use the search box
at the top to limit the results in the list of services. You can choose only one service
within a visual editor permission block. To grant access to more than one service, add
multiple permission blocks by choosing **Add more permissions**. 5. In **Actions allowed**, choose the actions to add to the policy. You
can choose actions in the following ways:

    * Select the check box for all actions.
    * Choose **Add actions** to enter the name of a specific action. You
     can use a wildcard character (`*`) to specify multiple actions.
    * Select one of the **Access level** groups to choose all actions
     for the access level (for example, **Read**,
     **Write**, or **List**).
    * Expand each of the **Access level** groups to choose individual
     actions.

By default, the policy that you are creating allows the actions that you choose. To
deny the chosen actions instead, choose **Switch to deny permissions**.
Because [IAM denies by
default](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md"), we recommend as a security best practice that you allow permissions to
only those actions and resources that a user needs. Create a JSON statement to
deny permissions only if you want to override a permission separately allowed by another
statement or policy. We recommend that you limit the number of deny permissions to a
minimum because they can increase the difficulty of troubleshooting permissions. 6. For **Resources**, if the service and actions that you selected in
the previous steps do not support choosing [specific resources](../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-resources "../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-resources"), all resources are allowed and you cannot edit this section.

If you chose one or more actions that support [resource-level permissions](../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-resources "../../../IAM/latest/UserGuide/access_controlling.md#access_controlling-resources"), then the
visual editor lists those resources. You can then expand **Resources** to
specify resources for your policy.

You can specify resources in the following ways:

    * Choose **Add ARNs** to specify resources by their Amazon Resource
     Names (ARN). You can use the visual ARN editor or list ARNs manually. For more
     information about ARN syntax, see [Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md")
     in the *IAM User Guide*. For information about using ARNs in
     the `Resource` element of a policy, see [IAM JSON policy elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the *IAM User Guide*.
    * Choose **Any in this account** next to a resource to grant
     permissions to any resources of that type.
    * Choose **All** to choose all resources for the service.

7. (Optional) Choose **Request conditions -
   _optional_** to add conditions to the policy that you are
   creating. Conditions limit a JSON policy statement's effect. For example, you can specify
   that a user is allowed to perform the actions on the resources only when that user's
   request happens within a certain time range. You can also use commonly used conditions to
   limit whether a user must be authenticated by using a multi-factor authentication (MFA)
   device. Or you can require that the request originate from within a certain range of IP
   addresses. For lists of all of the context keys that you can use in a policy condition,
   see [Actions, resources, and condition keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") in the
   _Service Authorization Reference_.

You can choose conditions in the following ways:

    * Use check boxes to select commonly used conditions.
    * Choose **Add another condition** to specify other conditions.
     Choose the condition's **Condition Key**,
     **Qualifier**, and **Operator**, and then enter a
     **Value**. To add more than one value, choose
     **Add**. You can consider the values as being connected by a
     logical `OR` operator. When you are finished, choose **Add
     condition**.

To add more than one condition, choose **Add another condition**
again. Repeat as needed. Each condition applies only to this one visual editor permission
block. All the conditions must be true for the permission block to be considered a match.
In other words, consider the conditions to be connected by a logical `AND`
operator.

For more information about the **Condition** element, see [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_. 8. To add more permission blocks, choose **Add more permissions**. For
each block, repeat steps 2 through 5.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure") in the _IAM User Guide_. 9. (Optional) When you create or edit a policy in the AWS Management Console, you can generate a JSON
or YAML policy template that you can use in AWS CloudFormation templates.

To do this, in the **Policy editor** choose
**Actions**, and then choose **Generate CloudFormation
template**. To learn more about AWS CloudFormation, see [AWS Identity and Access Management resource type reference](../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md "../../../AWSCloudFormation/latest/UserGuide/AWS_IAM.md") in the
_AWS CloudFormation User Guide_. 10. When you are finished adding permissions to the policy, choose
**Next**. 11. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review the **Permissions defined in this policy** to
make sure that you have granted the intended permissions. 12. (Optional) Add metadata to the policy by attaching tags as key-value pairs. For more
information about using tags in IAM, see [Tags for AWS Identity and Access Management resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_. 13. Choose **Create policy** to save your new policy.
**To grant programmatic access**

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                        | To                                                                                                                 | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Workforce identity<br>(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the<br>_AWS Command Line Interface User Guide_.<br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center<br>authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                          |
| IAM                                                          | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or<br>AWS APIs.                  | Following the instructions in [Using temporary<br>credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IAM                                                          | (Not recommended)Use long-term credentials to sign programmatic requests<br>to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.<br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in<br>the _AWS Command Line Interface User Guide_.<br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the<br>_AWS SDKs and Tools Reference Guide_.<br>• For AWS APIs, see [Managing access keys for<br>IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. |

## Protect against attackers

For more information about how to help protect against attackers when you
grant permissions to other AWS service principals, see [Optional conditions for your role trust relationships](conditions-for-role-trust.md "conditions-for-role-trust.md"). By
adding certain conditions to your policies, you can help prevent a specific
type of attack, known as a _confused
deputy_ attack, which occurs if an entity coerces a
more-privileged entity to perform an action, such as with cross-service
impersonation. For general information about policy conditions, also see
[Specifying conditions in a policy](access-control-overview.md#specifying-conditions "access-control-overview.md#specifying-conditions").

For more information about using identity-based policies with AWS Control Tower, see
[Using identity-based policies (IAM
policies) for AWS Control Tower](access-control-managing-permissions.md "access-control-managing-permissions.md"). For more information
about users, groups, roles, and permissions, see [Identities (Users, Groups, and Roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in
the _IAM User Guide_.
