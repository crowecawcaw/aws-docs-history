

# Managing organization enrollment configurations

To enable Automation for member accounts, create an organization enrollment configuration on the root, an organizational unit (OU), or an account. AWS Compute Optimizer then enables Automation for the eligible accounts that the enrollment configuration applies to. For how enrollment configurations work, see [Organization enrollment configurations](automation-org-enrollment.md). For more information about managing enrollment configurations programmatically, see the *AWS Compute Optimizer Automation API Reference*.

## Prerequisites
<a name="automation-org-ou-configure-prereq"></a>
+ Your organization uses AWS Organizations with all features enabled.
+ You enabled trusted access for Compute Optimizer in AWS Organizations.
+ You're signed in to the management account or a delegated administrator account, and Automation is enabled for that account.

## Creating an enrollment configuration
<a name="automation-org-ou-configure-create"></a>

Create an enrollment configuration to enable Automation for accounts and set their organization rule mode.

**To create an enrollment configuration on an OU (console)**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. In the **Enrollment configurations** section, choose **Create enrollment configuration**.

1. On the **Select organizational units and accounts** page, in **Your organization**, select the OU, and then choose **Next**. You can also select the root or individual accounts. You can't select the management account or an OU or account that already has an enrollment configuration. You also can't select an account that isn't opted in to Compute Optimizer.

1. On the **Set organization rule mode** page, choose an organization rule mode for each OU and account. **Any allowed** is selected by default. To change a mode, choose the edit icon in the **Organization rule mode** column. You can also select the rows and choose **Update to any allowed** or **Update to none allowed** from **Actions**. Choose one of the following modes:
   + **Any allowed**. The management account can apply recommended actions to the accounts and include them in organization rules.
   + **None allowed**. Each account applies its own recommended actions and runs its own automation rules. Organization rules don't apply to the accounts.

1. Choose **Create enrollment configuration**.

A success banner appears, and the new enrollment configuration appears in the **Enrollment configurations** table. The enrollment configuration enables Automation for every eligible account that it applies to, whichever organization rule mode you choose. For an OU or the root, it can take up to 5 minutes to reach every account.

To see the OUs and accounts that the enrollment configuration applies to, choose **View dependents** for the OU in the **Enrollment configurations** table.

If an account's **Automation status** isn't **Active** after 5 minutes, check that the account is opted in to Compute Optimizer. Compute Optimizer enables Automation only for member accounts that are opted in.

**To update an enrollment configuration (console)**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. In the **Enrollment configurations** table, select the enrollment configurations that you want to update.

1. For **Actions**, choose **Update to any allowed** or **Update to none allowed**.

## Deleting an enrollment configuration
<a name="automation-org-ou-configure-delete"></a>

Delete an enrollment configuration when you no longer want it to set the organization rule mode for the root, an OU, or an account. Deleting an enrollment configuration doesn't disable Automation for any account.

**To delete an enrollment configuration (console)**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. In the **Enrollment configurations** table, select the enrollment configurations that you want to delete.

1. For **Actions**, choose **Delete**.

1. In the **Delete enrollment configuration** dialog box, choose **Delete**. You can't undo this action.

After you delete an enrollment configuration, the OUs and accounts that used it inherit the enrollment configuration of their closest parent that has one. If no parent has one, their organization rule mode returns to the default, **None allowed**. Automation stays enabled for these accounts.

## For more information
<a name="automation-org-ou-configure-more"></a>
+ [Organization enrollment configurations](automation-org-enrollment.md)
+ [Enabling Automation for your organization](automation-org.md)
+ Organization enrollment configuration operations in the *AWS Compute Optimizer Automation API Reference*