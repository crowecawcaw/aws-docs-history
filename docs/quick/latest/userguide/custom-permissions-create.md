# Creating custom permissions profiles

###### Important

Applies to: Enterprise Edition

Intended audience: Administrators and Amazon Quick developers

Custom permissions profiles can be created for Amazon Quick accounts that are integrated
with IAM Identity Center, Active Directory, or for Quick accounts that have
Quick managed users. The identity type that an Quick account uses
determines the way an Quick admin configures a custom permissions
profile.

## Creating or editing a custom permissions profile (Quick console)

###### To create a custom permissions profile

1. Open the [Quick console](https://aws.amazon.com//quicksight/ "https://aws.amazon.com//quicksight/").
2. Choose **Manage Quick**.
3. In the left navigation, choose **Permissions**, and
   then choose **Custom permissions**.
4. On the **Custom permissions** page, choose
   **Create profile**.
5. For **Profile name**, enter a descriptive name for the
   profile.
6. (Optional) For **Description**, enter a description.
7. (Optional) To restrict future capabilities in a category, turn on the
   Deny by Default toggle in the **Restrict capabilities**
   section. When enabled for a category, any new capability that
   Quick launches in that category is automatically blocked for
   users assigned to this profile. For more information, see [Deny by Default](custom-permissions-governance.md "custom-permissions-governance.md").
8. In the **Capabilities & features** section, choose
   which capabilities to restrict. Capabilities are displayed in a hierarchy
   tree organized by parent capability. Expand a parent capability to view
   and configure its individual features. Review the live preview panel on
   the right to see the effect of your selections.

   - To restrict an entire group of features, select the parent
     capability.
   - To restrict specific features, expand the parent capability
     and select only the features you want to restrict.

9. Choose **Create**.

###### Important

Test custom permissions configurations in a development or staging account before applying
them to production users to verify the behavior matches your expectations.

After you create the profile, Quick takes you to the assignment
page where you can assign it to users, roles, or the account. For more
information, see [Assigning custom permissions profiles](custom-permissions-assign.md "custom-permissions-assign.md").

###### To edit an existing custom permissions profile

1. On the **Custom permissions** page, locate the profile
   you want to edit.
2. Choose the actions menu next to the profile, and then
   choose **Edit**.
3. Make your changes to the profile configuration, including the profile
   name, Deny by Default settings, and capability restrictions.
4. Choose **Update** to save your changes.

## Creating a custom permissions profile (AWS CLI)

Before you begin, you need to set up and configure the AWS CLI. For more
information about installing the AWS CLI, see [Install or update the latest
version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") and [Configure the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md")
in the AWS Command Line Interface User guide.

The following example creates a custom permissions profile with
`ExportToCsv` and `ExportToPdf` denied.

```
aws quicksight create-custom-permissions \
--aws-account-id `AWSACCOUNTID` \
--custom-permissions-name `PERMISSIONNAME` \
--capabilities '{"ExportToCsv": "DENY", "ExportToPdf": "DENY"}'
```
