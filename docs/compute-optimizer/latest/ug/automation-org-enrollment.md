

# Organization enrollment configurations

With an organization enrollment configuration, you enable AWS Compute Optimizer Automation for member accounts and set their organization rule mode. When Automation is enabled for a member account, the account can use recommended actions and automation rules, and the management account or a delegated administrator can view its recommended actions. The organization rule mode controls whether the management account can also apply recommended actions to the account and include it in organization rules. You can create an enrollment configuration on the root, an organizational unit (OU), or an account.
+ An enrollment configuration on the root applies to every member account in your organization, including accounts that join later. For more information, see [Enrollment configurations on the root](#automation-org-enrollment-root).
+ An enrollment configuration on an OU applies to every account in the OU and its child OUs, including accounts that join later.
+ An enrollment configuration on an account applies to that member account only.

Only the management account or a delegated administrator can create, view, update, and delete enrollment configurations. For the steps, see [Managing organization enrollment configurations](automation-org-ou-configure.md).

## Organization rule mode
<a name="automation-org-enrollment-mode"></a>

Each enrollment configuration sets one of the following organization rule modes for the accounts that it applies to:
+ **Any allowed**. The management account can apply recommended actions to the account and include it in organization rules.
+ **None allowed**. The account applies its own recommended actions and runs its own automation rules. Organization rules don't apply to it.

The enrollment configuration enables Automation for the accounts that it applies to. The organization rule mode doesn't affect whether Automation is enabled. It controls only whether the management account can apply recommended actions to those accounts and include them in organization rules.

## Enrollment configurations on the root
<a name="automation-org-enrollment-root"></a>

An enrollment configuration on the root applies to every member account in your organization. New accounts join the organization at the root, so the enrollment configuration also applies to them when they join. An OU or account with its own enrollment configuration uses that enrollment configuration instead of the one on the root. Enrollment configurations can't be created for the management account, and an enrollment configuration on the root doesn't apply to it.

## How enrollment configurations work
<a name="automation-org-enrollment-how"></a>
+ When you create or update an enrollment configuration, Compute Optimizer enables Automation for every eligible member account that it applies to and sets their organization rule mode. An eligible account is a member account that is opted in to Compute Optimizer. For an enrollment configuration on an account, the change takes effect immediately. For an enrollment configuration on an OU or the root, it can take up to 5 minutes to reach every account.
+ An account that joins or moves into an OU with an enrollment configuration, or into a child of that OU, inherits the enrollment configuration. Compute Optimizer then enables Automation for the account.
+ An enrollment configuration on an OU or account takes precedence over the one on its parent. To keep organization rules off an OU under a parent with **Any allowed**, create a **None allowed** enrollment configuration on that OU.
+ While an enrollment configuration applies to a member account, the account can't disable Automation. In the member account, **Disable Automation for account** is turned off. To return enrollment control to the member account, delete the enrollment configuration that applies to it.
+ Deleting an enrollment configuration doesn't disable Automation for any account. After you delete an enrollment configuration, the OUs and accounts that used it inherit the enrollment configuration of their closest parent that has one. If no parent has one, their organization rule mode returns to the default, **None allowed**.
+ You can delete only an enrollment configuration that's on an OU or account itself, not one that it inherits. To change the organization rule mode for an OU or account that inherits an enrollment configuration, create an enrollment configuration on it. You can also update the enrollment configuration on the parent.
+ An enrollment configuration on an OU or the root applies to a delegated administrator in the same way as to other member accounts.

## How Compute Optimizer determines an account's organization rule mode
<a name="automation-org-enrollment-determine"></a>

Compute Optimizer checks the following sources in order and uses the first one that applies to the account:

1. An enrollment configuration on the account.

1. The enrollment configuration on the closest parent OU or the root.

1. The organization rule mode set directly on the account, when no enrollment configuration applies to the account.

1. The default organization rule mode, **None allowed**.

The **Source** column in the **Organization status** window shows which source applies.

## Organization rule modes set directly on an account
<a name="automation-org-enrollment-account-level"></a>

You can set the organization rule mode directly on a member account only when no enrollment configuration applies to it. When an enrollment configuration applies to the account, the enrollment configuration replaces the mode set directly on the account. If you later delete every enrollment configuration that applies to the account, its organization rule mode returns to the default, **None allowed**. It doesn't return to the mode that was set directly on the account.

To check an account's Automation status, its organization rule mode, and where the mode comes from, view the organization status:

**To view the organization status**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. In the navigation pane, choose **Account management** under the **Preferences** section.

1. Choose the **Automation** tab.

1. In the **Enrollment configurations** section, choose **View organization status**.

1. In the **Organization status** window, enter the account's name, ID, or email address in the search box.

The **Organization status** window lists the root, each OU, and each account. Under **Organization rule mode**, the **Mode** column shows the mode and the **Source** column shows where it comes from. The following table describes each value.


| Column | Value | Meaning | 
| --- | --- | --- | 
| Automation status | Active | Automation is enabled, and the account can apply recommended actions and run automation rules. | 
| Automation status | Inactive | Automation is disabled, and the account's automation rules are stopped. | 
| Mode | Any allowed | The management account can apply recommended actions to the account and include it in organization rules. | 
| Mode | None allowed | The account applies its own recommended actions and runs its own automation rules. Organization rules don't apply to it. | 
| Source | Applied | An enrollment configuration is on this OU or account. | 
| Source | Inherited from *name* (*ID*) | The OU or account uses the enrollment configuration on the parent OU or root shown. | 
| Source | Direct | The organization rule mode is set directly on the account. No enrollment configuration applies to it. | 
| Source | Default | No enrollment configuration applies, so the organization rule mode is **None allowed**. | 

**Automation status** applies only to accounts, so the root and OUs show a dash (-). The management account appears in the list, but enrollment configurations don't apply to it.

## When an account moves
<a name="automation-org-enrollment-moves"></a>

If you move accounts between OUs in AWS Organizations, an account's organization rule mode can change.

After an account moves to a different OU, Compute Optimizer determines its organization rule mode from its new position. If an enrollment configuration applies at the new position, the account uses that enrollment configuration. Otherwise, its organization rule mode is the default, **None allowed**. To set a different mode, create an enrollment configuration on the account.

An enrollment configuration on the account stays with the account when it moves. Moving an account doesn't disable Automation for it.

## Viewing enrollment configurations and their effect
<a name="automation-org-enrollment-viewing"></a>

You can view enrollment configurations and their effect on the **Automation** tab of the **Account management** page.
+ The **Enrollment configurations** table lists each enrollment configuration that you created. Each row shows its **Name**, **ID**, **Type** (Root, Organizational unit, or Account), **Organization rule mode**, and **Dependents**. It doesn't list OUs and accounts that inherit an enrollment configuration. To find an enrollment configuration, enter its name or ID in the search box.
+ To view the OUs and accounts that inherit an enrollment configuration on an OU or the root, choose **View dependents**. The panel shows the enrollment configuration's type, ID, and organization rule mode, and lists the OUs and accounts that inherit it. It doesn't include OUs or accounts that have their own enrollment configuration, or anything under them.
+ To view the Automation status and organization rule mode of every OU and account, and the source of each organization rule mode, choose **View organization status**.
+ After you create, update, or delete an enrollment configuration, it can take up to 5 minutes for OU and account statuses to update.

## For more information
<a name="automation-org-enrollment-more"></a>
+ [Managing organization enrollment configurations](automation-org-ou-configure.md)
+ [Enabling Automation for your organization](automation-org.md)
+ [Rule scope](automation-rules.md#automation-rules-scope) in [Automation rules](automation-rules.md)
+ Organization enrollment configuration operations in the *AWS Compute Optimizer Automation API Reference*