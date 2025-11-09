# Creating a custom permissions profile in

Amazon Quick Suite

|                                            |
| ------------------------------------------ |
| \*_Applies<br>to:_<br>• Enterprise Edition |

|                                                                        |
| ---------------------------------------------------------------------- |
| Intended audience:<br>Administrators and Amazon Quick Suite developers |

In Enterprise edition, you can restrict the functionality that people can access in
Amazon Quick Suite. You can configure custom permissions at the account, role (admin, author,
reader), and user levels for all identity types in Quick Suite. _User level
custom permissions_ override a role's existing default or custom role
level permissions for the specified user. _User level custom permissions_
and _role level custom permissions_ override _account level
custom permissions_.

The following limitations apply to custom permissions.

- You can't grant permissions that are above a user's default role. For
  example, if a user has reader access, you can't grant permissions for that user
  to edit dashboards.
- To customize user or role permissions, you need to be a Amazon Quick Suite administrator
  with the following IAM permissions:

      + `quicksight:CreateCustomPermissions`
      + `quicksight:DeleteCustomPermissions`
      + `quicksight:DescribeCustomPermissions`
      + `quicksight:ListCustomPermissions`
      + `quicksight:UpdateCustomPermissions`
      + `quicksight:DescribeAccountCustomPermissions`
      + `quicksight:UpdateAccountCustomPermissions`
      + `quicksight:DeleteAccountCustomPermissions`

  You can create custom permission profiles to restrict access to any combination of the following
  features. Parent capabilities can be used to restrict access to an entire asset's feature sets. When parent
  capabilities are disabled, all associated child features will also be disabled.

Features with no parent capabilities cannot be turned off with this mechanism. Instead, they must be
restricted as individual features.

## Quick Suite parent capabilities

| Parent capability | Functionality                                 |
| ----------------- | --------------------------------------------- |
| Analyses          | Restricts all Analysis-related features       |
| Dashboards        | Restricts all Dashboards-related features     |
| Actions           | Restricts all Actions-related features        |
| Automate          | Restricts all Automation-related features     |
| Chat Agents       | Restricts all Chat Agent-related features     |
| Extensions        | Restricts all Extensions-related features     |
| Flows             | Restricts all Flows-related features          |
| Knowledge Base    | Restricts all Knowledge Base-related features |
| Research          | Restricts all Research-related features       |
| Spaces            | Restricts all Spaces-related features         |

## Quick Suite features

| Feature                                      | Amazon Quick Suite behavior                                                                                                                                                                                                                                                                                                   | Parent capability |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Create Chat Agents                           | • Can't view or access any chat agents<br>• Agent library and navigation are hidden<br>• Can still access and create other Quick Suite resources, such<br>as creating spaces for file sharing with teams or flows for structured<br>interactions (as long as those capabilities are not also restricted)                      | Chat Agents       |
| Allow creators to share without approval     | • Flows cannot be shared by creators without approval                                                                                                                                                                                                                                                                         | Flows             |
| Use Bedrock models for output refinement     | • Restricts usage of Bedrock models                                                                                                                                                                                                                                                                                           | Flows             |
| Enable UI agent to perform browser tasks     | • Restricts flows UI agent from performing browser tasks                                                                                                                                                                                                                                                                      | Flows             |
| Use internet to enhance results              | • Restricts usage of web-based search in Chat Agents and Research                                                                                                                                                                                                                                                             | --                |
| Sharing analyses                             | • Access to **Share** option on the **File**<br>menu is disabled for analyses                                                                                                                                                                                                                                                 | Analyses          |
| Adding or running anomaly detection          | • Access to the **Add anomaly to sheet**<br>option on the **Insights\*<br>• menu is disabled<br>for analyses<br>• Access to the **Anomaly** option on the<br>**Objects\*<br>• menu is disabled for<br>analyses<br>• Users will not be able to add anomaly detection to<br>sheets                                              | Analyses          |
| Print Sheet                                  | • Access to the **Print** option on the<br>**File\*<br>• menu is disabled for<br>analyses<br>• Access to the **Print** option on the<br>**Export\*<br>• menu is disabled for<br>dashboards<br>• Users will not be able to print sheets                                                                                        | --                |
| Export sheet to PDF                          | • Access to the **Export to PDF** option on<br>the **File\*<br>• menu is disabled for<br>analyses<br>• Access to the **Generate PDF** option on<br>the **Export\*<br>• menu is disabled for<br>dashboards<br>• Users will not be able to export sheets to a PDF<br>file                                                       | --                |
| Creating or updating themes                  | • Access to the **Themes** option on the<br>\*_Edit_<br>• menu is disabled for<br>analyses<br>• Users will not be able to create custom themes<br>• Users will not be able to edit or update existing<br>themes                                                                                                               | --                |
| Sharing dashboards                           | • Access to the share icon on the navigation menu is disabled for<br>dashboards                                                                                                                                                                                                                                               | Dashboard         |
| Export visual to CSV                         | • Access to the **Export to CSV** option on<br>the three-dot menu for each visual is disabled for both<br>analyses and dashboards<br>• Access to the **Export Visual to CSV**<br>option on the \*_Objects_<br>• menu is disabled<br>for analyses<br>• Users will not be able to export visuals to a CSV<br>file               | --                |
| Export visual to Excel                       | • Access to the **Export to Excel** option<br>on the three-dot menu for each table is disabled for both<br>analyses and dashboards<br>• Access to the **Export Table to Excel**<br>option on the \*_Objects_<br>• menu is disabled<br>for analyses<br>• Users will not be able to export tables to an Excel<br>file           | --                |
| Creating or updating all datasets            | • Access to creating or updating all datasets will be disabled                                                                                                                                                                                                                                                                | --                |
| Creating or updating only SPICE datasets     | • Access to creating or updating SPICE datasets will be disabled                                                                                                                                                                                                                                                              | --                |
| Sharing datasets                             | • Access to sharing datasets will be disabled                                                                                                                                                                                                                                                                                 | --                |
| Viewing account SPICE capacity               | • Restricts retrieving the account's SPICE capacity                                                                                                                                                                                                                                                                           | --                |
| Creating or updating all data sources        | • Access to creating or updating all data sources will be disabled                                                                                                                                                                                                                                                            | --                |
| Sharing data sources                         | • Access to sharing data sources will be disabled                                                                                                                                                                                                                                                                             | --                |
| Creating shared folders                      | • Restricts creating shared folders                                                                                                                                                                                                                                                                                           | --                |
| Renaming shared folders                      | • Restricts renaming shared folders                                                                                                                                                                                                                                                                                           | --                |
| Creating or updating scheduled email reports | • Access to the **Schedules** option on the<br>**Schedules\*<br>• menu is disabled for<br>dashboards<br>• Access to the **Recent snapshots** option<br>on the **Schedules\*<br>• menu is disabled for<br>dashboards<br>• Users will not be able to create or update scheduled email<br>reports                                | --                |
| Subscribing to scheduled email reports       | • Users will not be able to subscribe to scheduled email reports                                                                                                                                                                                                                                                              | Dashboard         |
| CSV attachments in scheduled email reports   | • Access to the **CSV** option in the<br>**Content\*<br>• section of the<br>**Schedules\*<br>• menu is disabled for<br>dashboards<br>• Users will not be able to attach CSV files in scheduled<br>email reports                                                                                                               | --                |
| Excel attachments in scheduled email reports | • Access to the **Excel** option in the<br>**Content\*<br>• section of the<br>**Schedules\*<br>• menu is disabled for<br>dashboards<br>• Users will not be able to attach Excel files in scheduled<br>email reports                                                                                                           | --                |
| PDF attachments in scheduled email reports   | • Access to the **PDF** option in the<br>**Content\*<br>• section of the<br>**Schedules\*<br>• menu is disabled for<br>dashboards<br>• Users will not be able to attach PDF files in scheduled<br>email reports                                                                                                               | --                |
| Content within scheduled email reports       | • Users will receive the content in scheduled email reports<br>only as downloadable links that are gated behind<br>login<br>• **Include sheet in email body** and<br>**File attachment\*<br>• options in the<br>**Schedules\*<br>• menu will be<br>disregarded<br>• Images will not be included in scheduled email<br>reports | --                |
| Creating or updating threshold alerts        | • Access to the **Alerts** menu is disabled<br>for dashboards<br>• Users will not be able to create or update threshold<br>alerts                                                                                                                                                                                             | --                |

Custom permissions profiles can be created for Amazon Quick Suite accounts that are integrated
with IAM Identity Center, Active Directory, or for Amazon Quick Suite accounts that have Amazon Quick Suite managed
users. The identity type that an Amazon Quick Suite account uses determines the way an
Amazon Quick Suite admin configures a custom permissions profile.

The following procedure shows you how to control access to Amazon Quick Suite capabilities and
respective features.

###### To control access to Amazon Quick Suite capabilities and features

1. Log in to the Amazon Quick Suite console.
2. Select **Manage Quick Suite**.
3. From the admin console left navigation menu, select
   **Permissions**, and then select **Custom
   permissions**.
4. In **Custom permissions**, from **Profiles**,
   select **New profile** or choose to edit the default
   profile.
5. In **New profile**, do the following:
   - In **Restrict capabilities** – Choose whether to
     allow specific capabilities for your system by checking or unchecking the
     appropriate options.
   - In **Restrict features** – Choose whether to allow
     specific features by checking or unchecking the appropriate options.

## Creating a custom permissions

profile for a Amazon Quick Suite account that is integrated with IAM Identity Center or Active
Directory

Amazon Quick Suite account admins can use the following procedure to create a custom
permissions profile for a Amazon Quick Suite account that is integrated with IAM Identity Center or Active
Directory.

###### To create a custom permissions profile for a Amazon Quick Suite account that is

integrated with IAM Identity Center or Active Directory

1. Sign in to the [AWS Management
   Console](https://aws.amazon.com/console "https://aws.amazon.com/console").
2. Open Amazon Quick Suite.
3. The Amazon Quick Suite Admin console opens. Choose **Custom Permissions**.
4. The **Manage custom permissions** page opens. Choose one of
   the following options.
   - To create a new custom permissions profile, choose
     **Create**.
   - To edit or view an existing custom permissions profile, choose the
     ellipsis (three dots) next to the profile that you want, and then choose
     **Edit**.

5. If you want to create or update a custom permissions profile, make selections
   for the following items.
   - For **Name**, enter a name for the custom permissions
     profile.
   - For **Restrictions**, choose the options that you
     want to deny. Any option that you don't choose is allowed. For
     example, if you don't want users to create or update data sources,
     but you want them to be able to do everything else, choose only
     **Creating or updating data sources**.

6. Choose **Create** or **Update** to confirm
   your choices. To go back without making any changes, choose
   **Back**.
7. Once you are done making changes, record the name of the custom permissions
   profile. Provide the name of the custom permissions profile to API users so that
   they can apply the custom permissions profile to roles or users.

## Creating a

custom permissions profile for a Amazon Quick Suite account that uses Amazon Quick Suite managed
users

Amazon Quick Suite account admins can use the following procedure to create a custom
permissions profile for a Amazon Quick Suite account that uses Amazon Quick Suite managed
users.

###### To create a custom permissions profile for Amazon Quick Suite managed users

1. Open the [Quick Suite console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. From any page in the Amazon Quick Suite console, choose **Manage
   Quick Suite** at the top right corner.

Only Amazon Quick Suite administrators have access to the **Manage
Quick Suite** menu option. If you don't have access to the
**Manage Quick Suite** menu, contact your Amazon Quick Suite
administrator for assistance. 3. Choose **Custom permissions**. You can also choose the
**Manage users** section, and then choose **Manage
custom permissions**. 4. The **Manage custom permissions** page opens. Choose one of
the following options.

    * To create a new custom permissions profile, choose
     **Create**.
    * To edit or view an existing custom permissions profile, choose the
     ellipsis (three dots) next to the profile that you want, and then choose
     **Edit**.

5. If you want to create or update a custom permissions profile, make selections
   for the following items.
   - For **Name**, enter a name for the custom permissions
     profile.
   - For **Restrictions**, choose the options that you
     want to deny. Any option that you don't choose is allowed. For
     example, if you don't want users to create or update data sources,
     but you want them t be able to do everything else, choose only
     **Creating or updating data sources**.

6. Choose **Create** or **Update** to confirm
   your choices. To go back without making any changes, choose
   **Back**.
7. Once you are done making changes, record the name of the custom permissions
   profile. Provide the name of the custom permissions profile to API users so that
   they can apply the custom permissions profile to roles or users.

After you create a custom permissions profile, use Amazon Quick Suite APIs to add or
change the custom permissions profile that is assigned to a user, role, or account. Users with
sufficient permissions can also use the [`AWS::QuickSight::CustomPermissions`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermissions.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermissions.md") AWS CloudFormation resource to
manage Amazon Quick Suite custom permissions profiles. Use the following topics to learn more
about managing custom permissions profiles with the Amazon Quick Suite APIs.

- [Apply a custom permissions profile to a Amazon Quick Suite
  role with the Amazon Quick Suite API](../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-role.md "../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-role.md")
- [Apply a custom permissions profile to a user with the
  Amazon Quick Suite API](../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-iam-user.md "../../../quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-iam-user.md")

## Apply a

custom permissions profile to a Amazon Quick Suite role with the Amazon Quick Suite API

After you create a custom permissions profile, use the Amazon Quick Suite APIs to add or
change the custom permissions profile that is assigned to a role.

Before you begin, you need to set up and configure the AWS CLI. For more information
about installing the AWS CLI, see [Install or update the latest
version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md")
in the AWS Command Line Interface User guide. You also need permissions to use the Amazon Quick Suite
API.

The following example calls the `UpdateRoleCustomPermission` API to update
the custom permissions that are assigned to a role.

```
aws quicksight update-role-custom-permission \
--role `ROLE` \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--custom-permissions-name `PERMISSIONNAME` \
--region `REGION`
```

The following example returns the custom permissions profile that is assigned to a
role.

```
aws quicksight describe-role-custom-permission \
--role `ROLE` \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--region `REGION`
```

The following example deletes a custom permissions profile from a role.

```
aws quicksight delete-role-custom-permission \
--role `ROLE` \
--aws-account-id `AWSACCOUNTID` \
--namespace default \
--region `REGION`
```

## Apply

a custom permissions profile to a user with the Amazon Quick Suite API

The following example applies a custom permissions profile to a user.

```
aws quicksight update-user-custom-permission \
    --aws-account-id `AWSACCOUNTID` \
    --namespace `default` \
    --user-name `USER_NAME` \
    --custom-permissions-name `myCustomPermission`
```

The following example deletes a custom permissions profile from a user.

```
aws quicksight delete-user-custom-permission \
    --aws-account-id `AWSACCOUNTID` \
    --namespace `default`
```

The following example adds custom permissions to a new Amazon Quick Suite IAM user.

```
aws quicksight register-user \
    --iam-arn arn:aws:iam::`AWSACCOUNTID`:user/`USER` \
    --identity-type IAM \
    --user-role AUTHOR \
    --custom-permissions-name `custom-permissions-profile-name` \
    --email `EMAIL` \
    --aws-account-id `AWSACCOUNTID` \
    --namespace default \
```

You can also associate an existing IAM user with a new permissions profile. The
following example updated the custom permissions profile of an existing IAM
user.

```
aws quicksight update-user \
    --user-name `USERNAME` \
    --role AUTHOR \
    --custom-permissions-name `custom-permissions-profile-name` \
    --email `EMAIL` \
    --aws-account-id `AWSACCOUNTID` \
    --namespace default \
```

The example below removes an existing user from a permissions profile.

```
aws quicksight update-user \
    --user-name `USERNAME` \
    --role AUTHOR \
    --unapply-custom-permissions \
    --email `EMAIL` \
    --aws-account-id `AWSACCOUNTID` \
    --namespace default
```

To test the custom permissions that are applied to a role or user, log in to the
user's account. When a user logs into Amazon Quick Suite, they are granted the highest
privilege role that they have access to. The highest privileged role a user can be
granted is Admin. The lowest privileged role that a user can be granted is Reader. For
more information about roles in Amazon Quick Suite, see [Managing user
access inside Amazon Quick Suite](../../../quicksight/latest/user/managing-users.md "../../../quicksight/latest/user/managing-users.md").

If you assign a custom permissions profile that restricts data source sharing to the
author's role, that author is no longer able to access the controls that allow data
source sharing. Instead, the affected author has view-only permissions to the data
source.

## Apply

a custom permissions profile to an account

###### To apply a custom permissions profile to an account

1. Open the [Quick Suite console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. From the top right, choose the profile icon.
3. Choose **Manage Quick Suite**. Only Amazon Quick Suite
   administrators will be able to view this page.
4. Choose **Custom permissions**. You can also choose the
   **Manage users** section, and then choose
   **Manage Custom Permissions** if your Quick Suite account uses
   Quick Suite managed users.
5. Locate the desired account custom permission. In the options menu under
   **Actions**, choose **Set as account
   profile**.

### Apply a custom permissions profile to an account using the Quick Suite

APIs

After you have created a custom permissions profile, use the Quick Suite API
to add or change the custom permissions profile that is assigned to an
account.

Before you begin, you will need to set up and configure the AWS CLI. For more
information about installing the AWS CLI, see see [Install or update the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Configure the AWS
CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the AWS Command Line Interface user guide. You also need the
following IAM permissions: `quicksight:UpdateAccountPermission`,
`quicksight:DescribeAccountPermission`, and
`quicksight:DeleteAccountCustomPermission`.

The following example calls the `UpdateAccountPermission` API to update
the custom permissions that are assigned to an account.

```
aws quicksight update-account-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name `PERMISSIONNAME` \
--region `REGION`
```

The following example returns the custom permissions profile that is assigned to
an account.

```
aws quicksight describe-account-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--region `REGION`
```

The following example unapplies a custom permissions profile from an
account.

```
aws quicksight delete-account-custom-permission \
--aws-account-id `AWSACCOUNTID` \
--region `REGION`
```
