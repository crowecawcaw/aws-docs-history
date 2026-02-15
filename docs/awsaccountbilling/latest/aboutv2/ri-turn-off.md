# Reserved Instances and Savings Plans discount sharing

The management account of an organization can control Reserved Instance discount and Savings Plans discount sharing for any accounts in that organization. AWS offers enhanced sharing capabilities by allowing organizations to define how commitment discounts are applied across their AWS accounts.

## Overview of Sharing Options

AWS provides flexible options for sharing Reserved Instances and Savings Plans discounts:

- **Organization-wide sharing**: Sharing across all accounts in the organization
- **Group-based sharing**: Define specific account groups for targeted discount sharing
- **Account-level control**: Activate or deactivate sharing for individual accounts
- To share the Savings Plans discount, the Savings Plans owner account must be active in the RI and Savings Plans discount sharing preferences. This enables the discount usage across other eligible linked accounts in the organization.
- When you use Billing Conductor alone or with billing transfer, changes to Reserved Instances and Savings Plans sharing preferences affect the standard AWS bill.
- When you use Billing Conductor with billing transfer, each AWS Organizations controls its own sharing preferences. You can't share these preferences across multiple AWS Organizations.

### Sharing Modes

###### Organization-wide sharing

- Commitments benefit the account owner first
- After satisfying the account owner, remaining benefits can be shared with other organization accounts
- Maximizes overall commitment discount rates

###### Prioritized Group Sharing

- Commitments benefit the account owner first
- After satisfying the account owner, commitments are shared with accounts within defined groups
- After satisfying the group's usage, remaining benefits can be shared with other organization accounts
- Maximizes overall commitment utilization and discount rates while prioritizing specific groups

###### Restricted Group Sharing

- Commitments benefit the account owner first
- Commitments are exclusively shared within defined account groups
- No sharing occurs outside designated groups, even with unused capacity

###### Note

###### Account Grouping Requirements

Group sharing uses AWS Cost Categories to define account groups:

- Each account can only belong to one sharing group
- Payer account cannot be part of a sharing group
- Cost Categories must be configured through the AWS Billing Console
- Only the **Accounts** dimension can be used when creating or editing sharing groups
- The Cost Category **Uncategorized costs** default value must not overlap with any sharing group name
- Existing Cost Categories can be reused if it meets the Reserved Instances and Savings Plan group sharing requirements or new ones created specifically for group sharing

###### Note

###### The following criteria must be met:

Group sharing uses AWS Cost Categories to define account groups:

- Savings Plans first apply to the purchasing account
- The Savings Plans owner account must remain active in sharing preferences
- Both purchasing and benefit receiving accounts must have sharing activated to share discounts
- Accounts with the largest calculated savings are prioritized
- You can change your preference at any time. Each estimated bill is computed by using the last set of preferences. The final bill for the month is calculated based on the preferences set at 23:59:59 UTC time on the last day of the month.
- If a Savings Plans owner account leaves the organization, Savings Plans no longer apply to the consolidated bill

## Deactivating shared Reserved Instances and Savings Plans

discounts

You can deactivate sharing discounts for individual member accounts.

###### To deactivate shared Reserved Instances and Savings Plans discounts

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Billing
   preferences**.
3. Under **Reserved Instances and Savings Plans discount sharing preference by
   account**, select the accounts that you want to deactivate
   discount sharing for.
4. Choose **Deactivate**.
5. In the **Deactivate Reserved Instance and Savings Plan sharing
   dialog box**, choose **Deactivate**.

###### Tip

You can also choose **Actions** and then choose
**Deactivate All** to deactivate Reserved Instance and Savings Plans sharing
for all accounts.

## Activating shared Reserved Instances and Savings Plans

discounts

You can use the console to activate Reserved Instance sharing discounts for an
account.

You can share Savings Plans with a set of accounts. You can either choose to not share
the benefit with other accounts, or to open up line item eligibility for the
entire consolidated billing family of accounts.

###### To activate shared Reserved Instances and Savings Plans discounts

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").

###### Note

Ensure that you're signed in to the management account of your
AWS Organizations. 2. In the navigation pane, choose **Billing
preferences**. 3. Under **Reserved Instances and Savings Plans discount sharing preference by
account**, select the accounts that you want to activate
discount sharing for. 4. Choose **Activate**. 5. In the **Activate Reserved Instance and Savings Plan sharing**
dialog box, choose **Activate**.

###### Tip

You can also choose **Actions** and then choose
**Activate All** to activate Reserved Instance and Savings Plans sharing for
all accounts.

## Selecting sharing modes:

1. Navigate to **Billing preferences** in the AWS Billing Console
2. Under **Reserved Instances and Savings Plans discount sharing preference**, select **Edit**
3. Choose your sharing mode (Prioritized or Restricted)
4. Define account groups using Cost Categories
5. Configure sharing preferences for each group

###### Note

###### Important Requirements and Limitations

- Deactivating Reserved Instance and Savings Plans discount sharing can result in higher monthly bills
- The Savings Plans owner account must remain active in sharing preferences for discounts to apply to other accounts
- Group-based sharing may result in some underutilized commitments in Restricted mode
