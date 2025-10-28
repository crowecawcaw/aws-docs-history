# Reserved Instances and Savings Plans discount sharing

The management account of an organization can deactivate Reserved Instance discount and Savings Plans
discount sharing for any accounts in that organization, including the
management account. This means that Reserved Instances and Savings Plans discounts aren't shared between
any accounts that have deactivated sharing.

To share an Reserved Instance or Savings Plans discount with an account, both accounts must have
sharing activated. You can change your preference at any time. Each estimated bill
is computed by using the last set of preferences. The final bill for the month is
calculated based on the preferences set at 23:59:59 UTC time on the last day of the
month.

If Savings Plans sharing is turned on for an AWS Organizations account, then it must meet the following criteria:

- At least one account in the consolidated billing family must have AWS compute usage for the Savings Plans to apply to the management account's bill.
- Savings Plans first apply usage in the purchasing account. If there are any unused hourly commitments, the Savings Plans automatically applies them to other accounts in the organization that have sharing turned on. Accounts with the largest calculated savings are prioritized.
- To apply discounts to other eligible linked accounts, the Savings Plans opener account must be
  included and activated under the RI and Savings Plans discount sharing
  preferences.
- If the Savings Plans owner account is removed or deactivated from the sharing preferences, the Savings Plans discount no longer applies to the other eligible linked accounts.
- If a Savings Plans owner member account leaves or is removed from the organization, the Savings Plans no longer apply to the consolidated bill.

###### Important

- Deactivating Reserved Instance and Savings Plans discount sharing can result in a higher monthly
  bill.
- To share the Savings Plans discount, the Savings Plans owner account must be active in the RI and Savings Plans discount sharing preferences. This enables the discount usage across other eligible linked accounts in the organization.

###### Topics

- [Deactivating shared Reserved Instances and Savings Plans
  discounts](#ri-turn-off-process "#ri-turn-off-process")
- [Activating shared Reserved Instances and Savings Plans
  discounts](#ri-turn-on-process "#ri-turn-on-process")

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
5. In the **Deactivate Reserved Instance and Savings Plan sharing**
   dialog box, choose **Deactivate**.

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
