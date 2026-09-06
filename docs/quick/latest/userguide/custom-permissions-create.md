

# Creating custom permissions profiles
<a name="custom-permissions-create"></a>

Custom permissions profiles can be created for Amazon Quick accounts that are integrated with IAM Identity Center, Active Directory, or for Quick accounts that have Quick managed users. The identity type that an Quick account uses determines the way an Quick admin configures a custom permissions profile.

## Creating or editing a custom permissions profile (Quick console)
<a name="custom-permissions-create-console"></a>

**To create a custom permissions profile**

1. Open the [Quick console](https://aws.amazon.com/quicksight/).

1. Choose **Manage Quick**.

1. In the left navigation, choose **Permissions**, and then choose **Custom permissions**.

1. On the **Custom permissions** page, choose **Create profile**.

1. For **Profile name**, enter a descriptive name for the profile.

1. (Optional) For **Description**, enter a description.

1. (Optional) To restrict a whole capability category, turn on the corresponding toggle in the **Restrict capabilities** section – for example, **Restrict AI capabilities**. Quick restricts all capabilities in that category for users assigned to this profile, including capabilities that it launches later. Allow any capabilities in the category that your users need in the **Capabilities & features** section. For more information, see [Deny by Default](custom-permissions-governance.md).

1. In the **Capabilities & features** section, choose which capabilities to restrict. Capabilities are organized into four groups: **AI capabilities**, **BI capabilities**, **Connectors**, and **Administration**. Expand a capability to view and configure its individual features. Review the preview panel on the right to see the effect of your selections.
   + To restrict an entire group of features, select the parent capability.
   + To restrict specific features, expand the parent capability and select only the features you want to restrict.

1. Choose **Create**.

**Important**  
Test custom permissions configurations in a development or staging account before applying them to production users to verify the behavior matches your expectations.

After you create the profile, Quick takes you to the assignment page where you can assign it to users, roles, or the account. For more information, see [Assigning custom permissions profiles](custom-permissions-assign.md).

**To edit an existing custom permissions profile**

1. On the **Custom permissions** page, locate the profile you want to edit.

1. Choose the actions menu next to the profile, and then choose **Edit**.

1. Make your changes to the profile configuration, including the profile name, Deny by Default settings, and capability restrictions.

1. Choose **Update** to save your changes.

## Creating a custom permissions profile (AWS CLI)
<a name="custom-permissions-create-cli"></a>

Before you begin, you need to set up and configure the AWS CLI. For more information about installing the AWS CLI, see [Install or update the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the AWS Command Line Interface User guide.

**Use the latest CLI version**  
Use the latest version of the AWS Command Line Interface. Quick adds capability identifiers to the AWS Command Line Interface as it releases new capabilities. If you receive `Unknown parameter in Capabilities` for a capability that appears in the console, update the AWS Command Line Interface and try again.

The following example creates a custom permissions profile with `ExportToCsv` and `ExportToPdf` denied.

```
aws quicksight create-custom-permissions \
--aws-account-id {{AWSACCOUNTID}} \
--custom-permissions-name {{PERMISSIONNAME}} \
--capabilities '{"ExportToCsv": "DENY", "ExportToPdf": "DENY"}'
```