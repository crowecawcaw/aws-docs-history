

# Applying AWS credits
<a name="useconsolidatedbilling-credits"></a>

AWS credits are automatically applied to bills to help cover costs that are associated with eligible services. For more information about eligible services, see [Redeem Your AWS Promotional Credit](https://aws.amazon.com/awscredits/). Credits are applied until they are exhausted or they expire.

For any questions about AWS credits in general or any credits that have already expired, contact Support. For more information about how to contact Support, see [Getting help with your bills and payments](billing-get-answers.md).

Viewing AWS credits
+ To view your credit balance since the last billing date, navigate to the **Credits** page in the **Billing** console. You can find the credit balance under the **Amount remaining** column. Your credit balance is updated each month at the *end* of the current billing cycle. For example, if you already applied a credit to an invoice this month, the **Amount remaining** column will be updated at the end of this billing cycle. 
+ To view your estimated credit balance for the current month, navigate to the **Bills** page in the **Billing** console, and then choose the **Savings** tab. This credit balance is updated monthly and shows your latest estimated credit balance.

Viewing credit details

To view detailed information about a specific credit, navigate to the **Credits** page in the **Billing** console and select the credit. The credit details page displays the following information:
+ **Credit ID** — The unique identifier for the credit.
+ **Credit type** — The type of credit (for example, **Promotion**).
+ **Status** — The current status of the credit. The following statuses are possible:
  + **Active** — The credit is set to be consumed and will be applied to eligible charges.
  + **Paused** — The credit is turned off but can be turned back on to be consumed. To change a credit's status between **Active** and **Paused**, use the status toggle on the credit details page.
  + **Exhausted** — The credit has a zero balance remaining and has been fully consumed.
  + **Expired** — The credit has passed its expiration date and is no longer available for use.
+ **Amount remaining** — The remaining balance of the credit as of the last billing cycle.
+ **Estimated amount remaining** — The estimated remaining balance of the credit for the current month, updated daily.
+ **Start date** — The date the credit becomes effective.
+ **Expiration date** — The date the credit expires.
+ **Applicable products** — The AWS services that the credit can be applied to.
+ **Account ID** — The AWS account that owns the credit.

The credit details page also includes an **Application history** tab that shows how the credit has been allocated, including the recipient account, service, product, and amount for each allocation.

The credit details page also displays the credit's sharing preference configuration. For more information, see [Credit-level sharing preferences](#credit-level-sharing-preferences).

Viewing AWS credits for billing transfer users
+ When you sign in as a bill source account, your credits apply to the standard AWS bill sent to your bill transfer account. These credits don't appear in your pro forma billing artifacts (Bills page, Cost Explorer, or AWS Cost and Usage Report) unless the bill transfer account enables credits in the pro forma domain. Your **Credits** page no longer displays your credit balance. The page shows the total amount of credit redeemed as a static value until all credits are redeemed.
+ When you sign in as a bill transfer account, you can view credit applications for each AWS Organizations that transfers bills to you by using billing view functionality in chargeable billing views in Cost Explorer, AWS Cost and Usage Report, and the **Bills** page. The **Credits** page doesn't support billing view functionality. You can only view credits redeemed in your own AWS Organizations and credits from bill source organizations when you have an IAM role in those organizations.

**Topics**
+ [Step 1: Choosing the credits to apply](#selecting-credits-to-apply)
+ [Step 2: Choose where to apply your credits](#selecting-usage-to-apply-credits-to)
+ [Step 3: Applying AWS credits across single and multiple accounts](#credits-for-orgs)
+ [Step 4: Sharing AWS credits](#credit-sharing)

## Step 1: Choosing the credits to apply
<a name="selecting-credits-to-apply"></a>

This section explains how AWS credits apply in a single or standalone AWS account. If an AWS account has more than one credit, the available credits apply in the following order:

**The order of how credits apply if an AWS account has more than one credit**

1. The soonest to expire amongst the credits

1. The credit with the least number of eligible services

1. The oldest of all credits

For example, Jorge has two credits available to him. Credit one is for 10 dollars, it expires January 2026, and it can be used for either Amazon S3 or Amazon EC2. Credit two is for 5 dollars, it expires December 2026, and it can be used only for Amazon EC2. Jorge has sufficient AWS charges to apply all credits. AWS selects credit one for application first because it expires sooner than credit two.

**Note**  
If you have remaining, eligible usage after credit is consumed, the process will repeat until your credits are consumed or your usage is covered.
Credit is applied to the largest services charge (for example, Amazon EC2, Amazon S3). Then, the consumption will continue in a descending pattern for the remainder of the service charges.
Credits don't require customer selection to apply during the billing process. AWS will automatically apply eligible credits to applicable services.

## Step 2: Choose where to apply your credits
<a name="selecting-usage-to-apply-credits-to"></a>

This section shows how AWS credits apply in an AWS Organizations when credit sharing is turned on.

**The order of how credits are applied in an AWS Organizations when credit sharing is activated**

1. Account that owns the credit is covered for the service charges

1. Credits are applied towards the AWS account with the highest spend

1. Within the linked account, the charges are grouped by specific fields and credits are applied to the group with the highest charges

1. Within this group, credits are applied to the highest charge first

The process repeats until the credit is consumed, or all customer spend is covered.

AWS applies the credit to the largest available charge across all eligible sellers of record. This means that AWS tries to apply your credits before they expire. So they might use a generic credit for a specific service.

For example, Jorge has two credits available to him. Credit one is for 10 dollars, expires January 2026, and can be used for either Amazon S3 or Amazon EC2. Credit two is for 5 dollars, expires December 2026, and can be used only for Amazon EC2. Jorge has two AWS charges: 100 dollars for Amazon EC2 and 50 dollars for Amazon S3. AWS applies credit one, which expires in January, to the Amazon EC2 charge, which leaves him with a 90-dollar Amazon EC2 charge and a 50-dollar Amazon S3 charge. AWS applies credit two to the remaining 90 dollars of Amazon EC2 usage, and Jorge has to pay 85 dollars for Amazon EC2 and 50 dollars for Amazon S3. He has now used all of his credits.

**Note**  
When you sign in as a bill source account, you are responsible for managing credit sharing for accounts in your AWS Organizations. The bill transfer account can't control credit sharing unless you provide them with a cross-organization role to modify these preferences.

## Step 3: Applying AWS credits across single and multiple accounts
<a name="credits-for-orgs"></a>

The following rules specify how AWS applies credits to bills for single accounts and for organizations by default (Credit sharing turned on):
+ The billing cycle begins on the first day of each month.
+ Suppose that an AWS account is owned on the first day of the month by an individual who isn't part of an organization. Later in the month, that individual account joins an organization. In this situation, AWS applies that individual's credits to their individual bill for their usage for that month. That is, AWS applies the credit up to the day that the individual joined the organization.
**Note**  
An individual's account credits don't cover the account usage from the day that the individual joined the organization to the end of that month. For this period, the individual's account credits aren't applied to the bill. However, starting the next month, AWS applies the individual's account credits to the organization.
+ If an account is owned by an organization at the start of the month, AWS applies credits redeemed by the payer account or by any linked account to the organization's bill, even if the account leaves the organization in the same month. The start of the month begins one second after 0:00 UTC\+0. For example, assume that an account leaves an organization on August 1. AWS still applies the August credits the account redeemed to the organization's bill because the account belonged to the organization during that calendar month.
+ If an individual leaves an organization during the month, AWS begins applying credits to the individual's account on the first day of the following month.
+ Credits are shared with all accounts that join an organization at any point in the month. However, the organization's shared credit pool consists of only credits from accounts that have been part of the organization since the first day of the month.

For example, assume that Susan owns a single account on the first day of the month and then joins an organization during the month. Also assume that she redeems her credits on any day after she joins the organization. AWS applies her credits to her account for usage she incurred from the first of the month to the day that she joined the organization. However, from the first day of the next month, AWS applies the credits to the organization's bill. If Susan leaves the organization, any credits that she redeems are also applied to the organization's bill until the first of the month after her departure. Starting the month after her departure, AWS applies Susan's credits to her bill instead of the organization's bill.

In another example, assume that Susan owns a single account on January 1 and joins an organization on January 11. If Susan redeems 100 dollars of credits on January 18, AWS applies them to her account for the usage that she incurred for the month of January. From February 1st onwards, Susan's credits are applied to the organization's consolidated bill. If Susan has 50 dollars of credits and leaves the organization on April 16, her credits are applied to the organization's consolidated bill for April. From May onward, Susan's credits are applied to her account.

## Step 4: Sharing AWS credits
<a name="credit-sharing"></a>

You can manage credit sharing in your organization using two levels of control:
+ **Credit sharing preference activation** — Activate or deactivate credit sharing for accounts in your organization. Accounts must have credit sharing activated to give or receive shared credits.
+ **Credit-level sharing preferences** — Define which accounts can use a specific credit based on your cost allocation structure using Cost Categories.

You can turn off credit sharing on the **Billing preferences** page on the Billing and Cost Management console. The following rules specify how credits are applied to bills for single accounts and for organizations when credit sharing is turned off:
+ The billing cycle begins on the first day of each month.
+ Credits are applied to only the account that received the credits.
+ Bills are calculated using the credit sharing preference that is active on the last day of the month.
+ In an organization, only the payer account can turn credit sharing off or on. The payer account user can also select which accounts credits can be shared with.

### Credit sharing preference activation
<a name="consolidated-billing-credit-sharing-preferences"></a>

You can activate or deactivate credit sharing for member accounts in your billing family. Accounts must have credit sharing activated to participate in credit sharing. This includes both giving credits to and receiving credits from other accounts in the same organization.

**Note**  
This section is only available for the management account (payer account) as part of AWS Organizations.  
When you use billing transfer and sign in as a bill transfer account, you can control sharing preferences only for accounts in your AWS Organizations. Each bill source account controls sharing preferences for accounts in their own AWS Organizations.

**To manage credit sharing preference activation for member accounts**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Billing preferences**.

1. In the **Credit sharing preferences** section, choose **Edit**.

1. To activate or deactivate credit sharing for specific accounts, select them from the table, and then choose **Activate** or **Deactivate**.

1. To activate or deactivate credit sharing for all accounts, choose **Actions**, and then choose **Activate All** or **Deactivate All**.

1. Choose **Update**.

**Tip**  
To activate credit sharing for new accounts that join your organization, select **Default sharing for newly created member accounts**.
To download a history of your credit sharing preferences, choose **Download preference history (CSV)**.

### Credit-level sharing preferences
<a name="credit-level-sharing-preferences"></a>

You can configure sharing preferences at the individual credit level to control which linked accounts can use a specific credit. Credit-level sharing preferences use Cost Categories to define the sharing group based on your cost allocation structure.

**Note**  
**Prerequisite:** Both the credit owner account and the recipient accounts must have credit sharing activated. For more information, see [Credit sharing preference activation](#consolidated-billing-credit-sharing-preferences)  
This section is only available for the management account (payer account) as part of AWS Organizations.

**To configure a credit-level sharing preference**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Billing and Payments**, choose **Credits**.

1. Select the credit you want to configure sharing for.

1. In the **Sharing preference** section, choose **Edit**.

1. For **Cost category**, select an existing cost category from the dropdown, or choose **create a new cost category** to define your sharing group. If you don't see a newly created cost category, choose the **Refresh** button.

1. For **Rule**, select a rule to define which accounts are included in the sharing group.

1. Review the **Selected preference details** section to confirm the cost category, rule, and list of accounts that will be included in the sharing group.

1. Choose **Save**.

**To edit a credit-level sharing preference**

1. Navigate to the credit details page.

1. In the **Sharing preference** section, choose **Edit**.

1. Update the **Cost category** or **Rule** as needed.

1. Review the updated **Selected preference details**.

1. Choose **Save**.

**To remove a credit-level sharing preference**

1. Navigate to the credit details page.

1. In the **Sharing preference** section, choose **Remove association**.

**Note**  
When a credit-level sharing preference is removed, the credit reverts to the default sharing behavior based on the credit sharing activation settings for accounts in your organization.