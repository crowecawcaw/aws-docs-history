# Prerequisites to create a subscriber with

query access in Security Lake

You must complete the following prerequisites before you can create a subscriber with
data access in Security Lake.

## Verify permissions

Before creating a subscriber with query access, verify that you have permission to
perform the following list of actions.

To verify your permissions, use IAM to review the IAM policies that are
attached to your IAM identity. Then, compare the information in those policies to
the following list of actions that you must be allowed to perform to create a
subscriber with query access.

- `glue:PutResourcePolicy`
- `glue:DeleteResourcePolicy`
- `iam:CreateRole`
- `iam:DeleteRolePolicy`
- `iam:GetRole`
- `iam:PutRolePolicy`
- `lakeformation:GrantPermissions`
- `lakeformation:ListPermissions`
- `lakeformation:RegisterResource`
- `lakeformation:RevokePermissions`
- `ram:GetResourceShareAssociations`
- `ram:GetResourceShares`
- `ram:UpdateResourceShare`

###### Important

After you have verified the permissions:

- If you plan to use Security Lake console to add a subscriber with query access, you can skip the
  next step and proceed to [Grant Lake Formation administrator
  permissions](#permissions-lf-admin "#permissions-lf-admin").
  Security Lake creates all the necessary IAM roles or uses existing roles on your behalf.
- If you plan to use Security Lake API or CLI to add a subscriber with query access, continue
  with the next step to create an IAM role to query Security Lake data.

## Create IAM role to query Security Lake

data (API and AWS CLI-only step)

When using Security Lake API or AWS CLI to grant query access to a subscriber, you'll need to create a role named
`AmazonSecurityLakeMetaStoreManager`. Security Lake uses this role to
register AWS Glue partitions and update AWS Glue tables. You may have already created
this role while [Create necessary IAM
roles](getting-started.md#prerequisite-iam-roles "getting-started.md#prerequisite-iam-roles").

## Grant Lake Formation administrator

permissions

You'll also need to add Lake Formation administrator permissions to the IAM role that you
use to access the Security Lake console and add subscribers.

You can grant Lake Formation administrator permissions to your role by following these
steps:

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. Sign in as an administrative user.
3. If a **Welcome to Lake Formation** window appears, choose the user
   that you created or selected in Step 1, and then choose Get started.
4. If you don't see a **Welcome to Lake Formation** window, then
   perform the following steps to configure a Lake Formation Administrator.
   1. In the navigation pane, under **Permissions**,
      choose **Administrative roles and tasks**. In the
      **Data lake administrators** section, choose
      **Choose administrators**.
   2. In the **Manage data lake administrators** dialog
      box, for IAM users and roles, choose the administrator role used
      when accessing the Security Lake console, and then choose
      **Save**.

For more information about changing permissions for data lake administrators, see
[Create a data lake administrator](../../../lake-formation/latest/dg/getting-started-setup.md#create-data-lake-admin "../../../lake-formation/latest/dg/getting-started-setup.md#create-data-lake-admin") in the
_AWS Lake Formation Developer Guide_.

The IAM role must have `SELECT` privileges on the database and tables
that you want to grant a subscriber access to. For instructions on how to do this,
see [Granting
Data Catalog permissions using the named resource method](../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md "../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md") in the
_AWS Lake Formation Developer Guide_.
