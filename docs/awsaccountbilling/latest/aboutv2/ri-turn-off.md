

# Reserved Instances and Savings Plans discount sharing

The management account of an organization can control Reserved Instance discount and Savings Plans discount sharing for any accounts in that organization. AWS offers enhanced sharing capabilities by allowing organizations to define how commitment discounts are applied across their AWS accounts.

## Overview of sharing options
<a name="overview-of-sharing-options"></a>
+ **Organization-wide sharing** – Discounts are shared across all sharing-activated accounts in the organization.
+ **Level sharing** – You define which accounts can use the discount from a specific Reserved Instance or Savings Plan, including commitments owned by the management account.
+ **Account-level control** – You activate or deactivate sharing for each account.
+ To share a Savings Plans discount, the account that owns the Savings Plan must have sharing activated in the Reserved Instance and Savings Plans discount sharing preferences.
+ When you use Billing Conductor, by itself or with billing transfer, changes to Reserved Instance and Savings Plans sharing preferences affect the standard AWS bill.
+ When you use Billing Conductor with billing transfer, each organization controls its own sharing preferences. Sharing preferences can't span multiple organizations.

## Sharing modes
<a name="sharing-modes"></a>

### Organization-wide (open) sharing
<a name="sharing-mode-open"></a>
+ Commitments apply first to the account that owns them.
+ Any remaining discount is shared with other sharing-activated accounts in the organization.
+ This mode gives the highest overall discount for the organization.

### Prioritized sharing
<a name="sharing-mode-prioritized"></a>
+ Commitments apply first to the account that owns them.
+ Any remaining discount is shared with the accounts in the defined group, or with the accounts defined for the commitment under level sharing.
+ After that usage is covered, any remaining discount is shared with other sharing-activated accounts in the organization.
+ This mode keeps discounts within the defined accounts first while still maximizing overall utilization.

### Restricted sharing
<a name="sharing-mode-restricted"></a>
+ Commitments apply first to the account that owns them.
+ Discounts are shared only with the accounts in the defined group, or with the accounts defined for the commitment under level sharing.
+ Discounts aren't shared outside those accounts, even when the commitment has unused capacity.

## How sharing preferences apply to your bill
<a name="sharing-preferences-bill"></a>
+ Savings Plans apply first to the account that purchased them.
+ The account that owns a Savings Plan must keep sharing activated for its discount to be shared.
+ Both the account that owns a commitment and the account that receives the discount must have sharing activated.
+ Within the eligible accounts, discounts apply to the usage with the largest discount rates first.
+ You can change your preferences at any time. When you change a preference before the month closes, AWS reapplies discounts for the entire month to date based on the new preference, so your estimated bill can change.
+ The final bill for the month uses the preferences in place at 23:59:59 UTC on the last day of the month.
+ If the account that owns a Savings Plan leaves the organization, the Savings Plan no longer applies to the consolidated bill.

## Activating shared Reserved Instances and Savings Plans discounts
<a name="ri-turn-on-process"></a>

You can activate discount sharing for an account from the management account.

**To activate shared Reserved Instances and Savings Plans discounts**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).
**Note**  
Make sure that you're signed in to the management account of your organization.

1. In the navigation pane, choose **Billing preferences**.

1. Under **Reserved Instances and Savings Plans discount sharing preference by account**, select the accounts that you want to activate discount sharing for.

1. Choose **Activate**.

1. In the **Activate Reserved Instance and Savings Plan sharing** dialog box, choose **Activate**.

**Tip**  
To activate sharing for all accounts, choose **Actions**, and then choose **Activate All**.

**Tip**  
**Activate discount sharing for new member accounts**: Under **New member accounts**, select this option to automatically activate sharing for accounts that join or are created in your organization
**Download preference history (CSV)**: Export a history of your sharing preference changes

## Deactivating shared Reserved Instances and Savings Plans discounts
<a name="ri-turn-off-process"></a>

You can deactivate discount sharing for individual member accounts.

**To deactivate shared Reserved Instances and Savings Plans discounts**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. Under **Reserved Instances and Savings Plans discount sharing preference by account**, select the accounts that you want to deactivate discount sharing for.

1. Choose **Deactivate**.

1. In the **Deactivate Reserved Instance and Savings Plan sharing** dialog box, choose **Deactivate**.

**Tip**  
To deactivate sharing for all accounts, choose **Actions**, and then choose **Deactivate All**.

## Level sharing for individual Reserved Instances and Savings Plans
<a name="level-sharing"></a>

Level sharing lets you choose which accounts can use the discount from a specific Reserved Instance or Savings Plan. Use level sharing when a specific commitment was purchased for a particular team, project or business unit.

Level sharing works within your account-level sharing preferences. It can narrow the set of accounts that receive a commitment's discount, but it can't extend the discount to an account whose sharing is deactivated.

### How level sharing applies
<a name="level-sharing-how-it-applies"></a>
+ The commitment applies first to eligible usage in the account that owns it.
+ The remaining discount applies to the accounts defined in the commitment's level sharing preference.
+ With prioritized mode, any remaining discount then applies to other sharing-activated accounts in the organization. With restricted mode, the discount doesn't apply outside the defined accounts.
+ Within each set of eligible accounts, the discount applies to the usage with the highest savings percentage first. For more information, see [Understanding how Savings Plans apply to your usage](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) in the *Savings Plans User Guide*.

### How level sharing and group sharing work together
<a name="level-sharing-and-group-sharing"></a>
+ A level sharing preference on a commitment overrides the organization's group sharing preference for that commitment.
+ Commitments without a level sharing preference follow the organization's group or open sharing preference.

## Setting up level sharing for a Reserved Instance or Savings Plan
<a name="level-sharing-setup"></a>

You set up level sharing on the detail page of each commitment.

**To configure level sharing for a Reserved Instance or Savings Plan**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).
**Note**  
Make sure that you're signed in to the management account of your organization.

1. In the navigation pane, choose **Inventory** under **Savings Plans** or under **Reservations**.

1. Choose the commitment to open its detail page.

1. In the **Sharing preferences** section, choose **Manage sharing preference**.

1. For **Mode**, choose **Prioritized** or **Restricted**.

1. For **Cost category**, select a Cost Category with the Benefit level sharing association, or choose **Create cost category**. If you don't see a Cost Category that you just created, choose the refresh button.

1. For **Rule**, select the rule that defines the accounts that can use this commitment.

1. Review **Selected rule details** to confirm the Cost Category, rule and accounts, and then choose **Save**.

**To remove a level sharing preference**

1. Open the commitment's detail page from **Inventory**.

1. In the **Sharing preferences** section, choose **Remove sharing preference**.

After you remove the preference, the commitment follows the organization's sharing preference.

## Setting up group sharing
<a name="ri-select-sharing-mode"></a>

**To choose a group sharing mode**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. Under **Reserved Instances and Savings Plans discount sharing preference**, choose **Edit**.

1. Choose **Prioritized sharing group** or **Restricted sharing group**.

1. For **Cost category**, select a Cost Category with the Benefit group sharing association, or choose **Create cost category**. If you don't see a Cost Category that you just created, choose the refresh button.

1. Review the impact warning, and then save your preference.

## Cost Category requirements for sharing
<a name="sharing-cost-category-requirements"></a>

**Note**  
Group sharing and level sharing use AWS Cost Categories to define accounts:  
Group sharing uses a Cost Category with the Benefit group sharing association. Level sharing uses a Cost Category with the Benefit level sharing association. You can use one Cost Category for Reserved Instances, Savings Plans and credits.
Each account can belong to only one sharing group.
Only one Cost Category can be associated with group sharing for an organization at a time.
You must create and edit Cost Categories for sharing in the Billing and Cost Management console.
Only the **Accounts** dimension can be used in Cost Category rules for sharing.
The Cost Category default value for uncategorized costs must not match the name of any sharing group.
For level sharing, each Cost Category rule defines a set of accounts that can use a commitment. The rule must include the account that owns the commitment, and the Cost Category must belong to the management account.
You can reuse an existing Cost Category if it meets these requirements, or create a new one for sharing.
Cost Categories already associated with Reserved Instance and Savings Plans group sharing keep working. They aren't converted to the Benefit group sharing association, and a Cost Category can't have both associations.

## Important considerations
<a name="sharing-considerations"></a>

**Note**  
Deactivating Reserved Instance and Savings Plans discount sharing can increase your monthly bill.
Group sharing and level sharing can lower overall savings compared with open sharing, because discounts stay within the accounts you define.
Changes appear on the estimated bill for the current month. The final bill uses the preferences in place at 23:59:59 UTC on the last day of the month.