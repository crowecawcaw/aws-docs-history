# Set up additional IAM permissions

By default, users and roles don't have permission to create or modify MediaPackage
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by MediaPackage, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Elemental MediaPackage](../../../service-authorization/latest/reference/list_awselementalmediapackage.md "../../../service-authorization/latest/reference/list_awselementalmediapackage.md") in the _Service Authorization Reference_.

This section describes the permissions that you must assign to users and other AWS
identities so that they can work with MediaPackage and other AWS services that your workflows
use. After you have identified the required permissions, you will be able to design and
create the relevant policies, and attach those policies to groups of users or to roles.

This section assumes that you have already performed these tasks:

- You have signed up for MediaPackage and created an administrator.
- You have read the recommendations in [Identity and Access Management for AWS Elemental MediaPackage](security-iam.md "security-iam.md") about how to create administrators, users,
  and other AWS identities.

###### Topics

- [Create a role in the IAM console](#setting-up-create-role "#setting-up-create-role")
- [Assume the role from
  the IAM console or AWS CLI](#setting-up-create-nonadmin-roles-assume-role "#setting-up-create-nonadmin-roles-assume-role")
- [Add permissions for tagging](#requirements-for-tagging "#requirements-for-tagging")

## Create a role in the IAM console

Create a role in the IAM console for each policy that you create. This allows
users to assume a role rather than attaching individual policies to each
user.

###### To create a role in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**, and then choose **Create
   role**.
3. Under **Select trusted entity**, choose **AWS
   account**.
4. Under **An AWS account**, select the account with the
   users that will be assuming this role.
   - If a third-party will be accessing this role, it's best practice
     to select **Require external ID**. For more
     information about external IDs, see [Using an external ID for third-party access](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md") in the
     _IAM User Guide_.
   - It's best practice to require multi-factor authentication (MFA).
     You can select the check box next to **Require
     MFA**. For more information about MFA, see [Multi-factor
     authentication (MFA)](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
     _IAM User Guide_.

5. Choose **Next**.
6. Under **Permissions policies**, search for and add the
   policy with the appropriate MediaPackage permissions level.
   - For access to live functionality, choose one of the following
     options:
     - Use
       **AWSElementalMediaPackageFullAccess**
       to allow the user to perform all actions on all live
       resources in MediaPackage.
     - Use **AWSElementalMediaPackageReadOnly**
       to provide the user read-only rights for all live resources
       in MediaPackage.

7. Add policies to allow the MediaPackage console to make calls to Amazon CloudWatch
   on the user's behalf. Without these policies, the user is able to use the
   service's API only (not the console). Choose one of the following
   options:
   - Use **ReadOnlyAccess** to allow MediaPackage to
     communicate with CloudWatch, and also provide the user read-only access to
     all AWS services on your account.
   - Use **CloudWatchReadOnlyAccess**,
     **CloudWatchEventsReadOnlyAccess**, and
     **CloudWatchLogsReadOnlyAccess** to allow
     MediaPackage to communicate with CloudWatch, and limit the user's
     read-only access to CloudWatch.

8. (Optional) Set a [permissions
   boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for
   service roles, but not service-linked roles.
   1. Expand the **Permissions boundary** section and
      choose **Use a permissions boundary to control the maximum
      role permissions**. IAM includes a list of the AWS
      managed and customer managed policies in your account.
   2. Select the policy to use for the permissions boundary or choose
      **Create policy** to open a new browser tab and
      create a new policy from scratch. For more information, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the
      _IAM User Guide_.
   3. After you create the policy, close that tab and return to your
      original tab to select the policy to use for the permissions
      boundary.

9. Verify that the correct policies are added to this group, and then choose
   **Next**.
10. If possible, enter a role name or role name suffix to help you identify
    the purpose of this role. Role names must be unique within your
    AWS account. They are not distinguished by case. For example, you cannot
    create roles named both `PRODROLE` and
    `prodrole`. Because various entities might
    reference the role, you cannot edit the name of the role after it has been
    created.
11. (Optional) For **Description**, enter a description for
    the new role.
12. Choose **Edit** in the **Step 1: Select trusted
    entities** or **Step 2: Select permissions**
    sections to edit the use cases and permissions for the role.
13. (Optional) Add metadata to the user by attaching tags as key-value pairs.
    For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the
    _IAM User Guide_.
14. Review the role and then choose **Create role**.

## Assume the role from

the IAM console or AWS CLI

View the following resources for learning about granting permissions for users to
assume the role and how users can switch to the role from the IAM console or
AWS CLI.

- For more information about granting a user permissions to switch roles,
  see [Granting a user permissions to switch roles](../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md "../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md") in the
  _IAM User Guide_.
- For more information about switching roles (console), see [Switching to a role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") in the
  _IAM User Guide_.
- For more information about switching roles (AWS CLI), see [Switching
  to an IAM role (AWS CLI)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md") in the
  _IAM User Guide_.

## Add permissions for tagging

When users create channel groups, channels, or origin endpoints, they can
optionally attach tags to the resource during creation. Typically, your organization
has a policy to tag or to omit tags. There are two services that control permissions
for tagging, for two different scenarios:

- The ability to tag during channel creation is controlled by actions within
  MediaPackage.
- The ability to modify tags in existing resources is controlled by actions
  within Resource Group Tagging. See [Working with Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md") in [Getting Started with the AWS Management Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").
