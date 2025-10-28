# Creating policies and non-administrative roles

By default, users and roles don't have permission to create or modify MediaPackage
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by MediaPackage, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Elemental MediaPackage](../../../service-authorization/latest/reference/list_awselementalmediapackage.md "../../../service-authorization/latest/reference/list_awselementalmediapackage.md") in the _Service Authorization Reference_.

This section describes how you can create policies and create non-administrative roles so that users can create or modify MediaPackage
resources. This section also describes how your users can assume that role to grant secure and temporary credentials.

###### Topics

- [(Optional) Step 1: Create an IAM
  policy for Amazon CloudFront](#setting-up-create-non-admin-iam-cf "#setting-up-create-non-admin-iam-cf")
- [(Optional) Step 2: Create an IAM policy for
  MediaPackage VOD](#setting-up-create-non-admin-iam-vod "#setting-up-create-non-admin-iam-vod")
- [Step 3: Create a role in the IAM console](#setting-up-create-role "#setting-up-create-role")
- [Step 4: Assume the
  role from the IAM console or AWS CLI](#setting-up-create-nonadmin-roles-assume-role "#setting-up-create-nonadmin-roles-assume-role")

## (Optional) Step 1: Create an IAM

policy for Amazon CloudFront

If you or your users will create Amazon CloudFront distributions from the AWS Elemental MediaPackage
live console, create an IAM policy that allows access to CloudFront.

For more information about using CloudFront with MediaPackage, see [Working with CDNs](cdns.md "cdns.md").

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudfront:GetDistribution",
                "cloudfront:CreateDistributionWithTags",
                "cloudfront:UpdateDistribution",
                "cloudfront:CreateDistribution",
                "cloudfront:TagResource",
                "tag:GetResources"
            ],
            "Resource": "*"
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.

## (Optional) Step 2: Create an IAM policy for

MediaPackage VOD

If you or your users will be using video on demand (VOD) functionality in
MediaPackage, create an IAM policy that allows access to resources for the
`mediapackage-vod` service.

The following sections describe how to create a policy that allows all actions, and one
that allows read-only rights. You can customize the policies by adding or removing actions
to fit your workflows.

### Policy for full VOD access

This policy allows the user to perform all actions on all VOD resources.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "mediapackage-vod:*",
            "Resource": "*"
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.

### Policy for read-only VOD access

This policy allows the user to view all VOD resources.

###### To use the JSON policy editor to create a policy

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane on the left, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose **Get
Started**. 3. At the top of the page, choose **Create policy**. 4. In the **Policy editor** section, choose the
**JSON** option. 5. Enter the following JSON policy document:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "mediapackage-vod:List*",
                "mediapackage-vod:Describe*"
            ],
            "Resource": "*"
        }
    ]
}
```

6. Choose **Next**.

###### Note

You can switch between the **Visual** and **JSON**
editor options anytime. However, if you make changes or choose **Next**
in the **Visual** editor, IAM might restructure your policy to
optimize it for the visual editor. For more information, see [Policy restructuring](../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure "../../../IAM/latest/UserGuide/troubleshoot_policies.md#troubleshoot_viseditor-restructure")
in the _IAM User Guide_. 7. On the **Review and create** page, enter a **Policy
name** and a **Description** (optional) for the policy that
you are creating. Review **Permissions defined in this policy** to see
the permissions that are granted by your policy. 8. Choose **Create policy** to save your new policy.

## Step 3: Create a role in the IAM console

Create a role in the IAM console for each policy that you create. This allows users to assume
a role rather than attaching individual policies to each user.

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
     You can select the check box next to **Require MFA**. For
     more information about MFA, see [Multi-factor
     authentication (MFA)](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in the
     _IAM User Guide_.

5. Choose **Next**.
6. Under **Permissions policies**, search for and add the
   policy with the appropriate MediaPackage permissions level.
   - For access to live functionality, choose one of the following options:
     - Use
       **AWSElementalMediaPackageFullAccess**
       to allow the user to perform all actions on all live
       resources in MediaPackage.
     - Use **AWSElementalMediaPackageReadOnly**
       to provide the user read-only rights for all live resources
       in MediaPackage.

   - For access to video on demand (VOD) functionality, use the policy
     that you created in [(Optional) Step 2: Create an IAM policy for
     MediaPackage VOD](#setting-up-create-non-admin-iam-vod "#setting-up-create-non-admin-iam-vod").

7. Add policies to allow the MediaPackage console to make calls to Amazon CloudWatch
   on the user's behalf. Without these policies, the user is able to use the
   service's API only (not the console). Choose one of the following options:
   - Use **ReadOnlyAccess** to allow MediaPackage to
     communicate with CloudWatch, and also provide the user read-only access to
     all AWS services on your account.
   - Use **CloudWatchReadOnlyAccess**,
     **CloudWatchEventsReadOnlyAccess**, and
     **CloudWatchLogsReadOnlyAccess** to allow
     MediaPackage to communicate with CloudWatch, and limit the user's
     read-only access to CloudWatch.

8. (Optional) If this user will create Amazon CloudFront distributions from the
   MediaPackage console, attach the policy that you created in [(Optional) Step 1: Create an IAM
   policy for Amazon CloudFront](#setting-up-create-non-admin-iam-cf "#setting-up-create-non-admin-iam-cf").
9. (Optional) Set a [permissions
   boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"). This is an advanced feature that is available for
   service roles, but not service-linked roles.
   1. Expand the **Permissions boundary** section and choose
      **Use a permissions boundary to control the maximum role
      permissions**. IAM includes a list of the AWS managed and
      customer managed policies in your account.
   2. Select the policy to use for the
      permissions boundary or choose **Create policy** to open a
      new browser tab and create a new policy from scratch. For more information,
      see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the
      _IAM User Guide_.
   3. After you create the policy,
      close that tab and return to your original tab to select the policy to use
      for the permissions boundary.

10. Verify that the correct policies are added to this group, and then choose
    **Next**.
11. If possible, enter a role name or role name suffix to help you identify
    the purpose of this role. Role names must be unique within your
    AWS account. They are not distinguished by case. For example, you cannot
    create roles named both `PRODROLE` and
    `prodrole`. Because various entities might
    reference the role, you cannot edit the name of the role after it has been
    created.
12. (Optional) For **Description**, enter a description for
    the new role.
13. Choose **Edit** in the **Step 1: Select trusted
    entities** or **Step 2: Select permissions**
    sections to edit the use cases and permissions for the role.
14. (Optional) Add metadata to the user by attaching tags as key-value pairs.
    For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the
    _IAM User Guide_.
15. Review the role and then choose **Create role**.

## Step 4: Assume the

role from the IAM console or AWS CLI

View the following resources for learning about granting permissions for users to assume
the role and how users can switch to the role from the IAM console or AWS CLI.

- For more information about granting a user permissions to switch roles,
  see [Granting a user permissions to switch roles](../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md "../../../IAM/latest/UserGuide/id_roles_use_permissions-to-switch.md") in the
  _IAM User Guide_.
- For more information about switching roles (console), see [Switching to a role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md") in the
  _IAM User Guide_.
- For more information about switching roles (AWS CLI), see [Switching
  to an IAM role (AWS CLI)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-cli.md") in the
  _IAM User Guide_.
