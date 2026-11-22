

# Splitting and transferring AWS credits

By default, a credit applies first to the account that owns it. Any remaining amount is then shared with other sharing-activated accounts, starting with the account that has the highest spend. When one large credit is meant for several teams, the account that owns it can use up the amount intended for the others.

You can split a credit into smaller credits and transfer them to other accounts in your organization. Each account that owns a credit gets first priority to use it.

Split and transfer are separate actions. You can split a credit without transferring it, and you can transfer a credit without splitting it first.

## Key concepts
<a name="credits-split-transfer-concepts"></a>
+ **Split** — Divides a credit's remaining balance into new credits in the same account. Each new credit has its own credit ID, sharing preference and consumption tracking. The original credit's remaining balance becomes $0, and the credit stays on the **Credits** page with the status **Expired**.
+ **Transfer** — Moves a credit to another account in your organization. The receiving account becomes the owner of the credit.
+ **Credit family** — The original credit and all the credits split from it, including credits split from split credits.

## Who can split and transfer credits
<a name="credits-split-transfer-who"></a>


**Who can split and transfer credits**  

| Action | Management (payer) account | Member (linked) account | 
| --- | --- | --- | 
| Split | Any credit in the organization | Only credits it owns | 
| Transfer | Any credit, to any account in the organization | Not available | 

You can control access with the IAM actions `billing:SplitCredit` and `billing:TransferCredit`.

## What a split credit inherits
<a name="credits-split-inherits"></a>

Each new credit keeps the following from the original credit:
+ **Expiration date**. Splitting doesn't change or extend the expiration date.
+ **Applicable products**. For example, if the original credit applies only to Amazon EC2, the new credits also apply only to Amazon EC2.
+ **Credit-level sharing preference**. After the split, you can change the sharing preference of each new credit separately.

## How split and transferred credits apply
<a name="credits-split-transfer-apply"></a>
+ Each split credit is applied as a separate credit. It applies first to the account that owns it, and any unused amount is shared according to the credit's sharing preferences.
+ When you transfer a credit, its credit-level sharing preference is removed, because the new owner might not be one of the accounts that the preference allowed. After the transfer, the management account can set a new sharing preference.
+ If the receiving account has credit sharing deactivated and doesn't have enough eligible usage, the unused amount expires on the credit's expiration date. To avoid this, keep credit sharing activated for the account, or transfer the credit to an account with more usage.

## Quotas
<a name="credits-split-quotas"></a>


**Split quotas**  

| Item | Limit | 
| --- | --- | 
| Splits per credit family (total) | 100 | 
| Minimum amount of each new credit | $100 USD | 
+ A credit family can be split up to 100 times in total, including splits of split credits. After 100 splits, no credit in the family can be split again.
+ Each new credit must be at least $100.
+ The amounts of the new credits must add up exactly to the remaining balance of the credit that you split.

## Splitting a credit
<a name="credits-split-howto"></a>

The **Split credit** and **Transfer** actions are available on the credit details page.

**To split a credit**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Credits**.

1. Choose the credit to open its details page.

1. Choose **Split credit**.

1. Choose how to divide the remaining balance: **Equal split** (enter the number of new credits), **Percentage** or **Amount**. Each new credit must be at least $100.

1. Review the summary, and then confirm the split.

## Transferring a credit
<a name="credits-transfer-howto"></a>

Only the management account can transfer credits.

**To transfer a credit**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).
**Note**  
Make sure that you're signed in to the management account of your organization.

1. In the navigation pane, choose **Credits**.

1. Choose the credit to open its details page.

1. Choose **Transfer**.

1. Choose the account to receive the credit.

1. Confirm the transfer.

The transferred credit appears on the receiving account's **Credits** page immediately.

## Viewing and tracking split and transferred credits
<a name="credits-split-transfer-tracking"></a>
+ The management account can view every credit in the organization. Member accounts can view only the credits they own, including credits transferred to them.
+ The credit details page doesn't show the credit family. To trace which credits came from which original credit, use the `parentCreditId` field in the Credits API, or the `SplitCredit` and `TransferCredit` events in AWS CloudTrail.
+ In the AWS Cost and Usage Report and in billing views, each split credit appears as its own line item, under its own credit ID, when it's applied to usage. Splitting and transferring don't create line items.
+ If you have automation, budgets or alerts that refer to the original credit ID, update them to use the new credit IDs.

## Considerations
<a name="credits-split-transfer-considerations"></a>
+ **Splits can't be undone.** You can't combine split credits back into one credit. Keeping them as separate credits with the same settings gives the same result.
+ A transferred credit can be transferred again, for example back to the account that originally owned it.
+ **Transfers stay within your organization.** You can't transfer a credit to an account in a different organization.
+ **No additional cost.** You aren't charged for splitting or transferring credits.
+ **Plan before you split.** Decide which accounts should own which amounts before you split, so the credit family stays easy to track and well within the 100-split quota.

## Example
<a name="credits-split-transfer-example"></a>

Your management account has a $1,000,000 credit. You split it into a $600,000 credit and a $400,000 credit, and then transfer the $400,000 credit to the Media account. The Media account uses its $400,000 credit first, and the management account keeps the $600,000 credit. Any unused amount on either credit is shared according to that credit's sharing preferences.

## Related topics
<a name="credits-split-transfer-related"></a>
+ [Applying AWS credits](useconsolidatedbilling-credits.md)
+ [Customizing your Billing preferences](billing-pref.md)
+ [Organizing costs using AWS Cost Categories](manage-cost-categories.md)