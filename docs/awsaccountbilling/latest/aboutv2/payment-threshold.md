

# Payment Threshold

Payment Threshold helps verify that your card can cover your AWS usage during the billing month. If your usage in a billing month reaches your Payment Threshold, AWS verifies that your default or backup card (if enabled) has enough funds to cover it. This is not an additional charge, and your regular monthly invoice is unaffected. You can track your usage against your Payment Threshold on the **Payments** page of the AWS Management Console. For more information, see [What happens when you reach your Payment Threshold](#payment-threshold-what-happens).

AWS enrolls you in this feature automatically and sets your Payment Threshold for you, so you can't change it or request a change. AWS sets, manages, and updates this amount based on your account history, payment history, and seller of record. Your Payment Threshold appears in the console if your account is eligible. To view your Payment Threshold, see [Where to find your Payment Threshold](#payment-threshold-where-to-find).

Accounts that aren't eligible don't show a Payment Threshold in the console. To determine whether your account is eligible for the feature, see [Payment Threshold availability](#payment-threshold-availability).

## Where to find your Payment Threshold
<a name="payment-threshold-where-to-find"></a>

You can view your Payment Threshold in the console.<a name="find-payment-threshold"></a>

**To find your Payment Threshold**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Payments**.

1. In the **Summary of balances** section, find your Payment Threshold and your current usage against it.

The console shows the following details:
+ Your Payment Threshold, in your preferred currency.
+ A progress bar of your current usage against the Payment Threshold.
+ The current monthly usage.
+ The time the usage amount was last updated.
+ Your Payment Threshold status, which is one of the following:
  + Your usage is within the Payment Threshold.
  + Your usage has reached the Payment Threshold.
  + AWS verified that your card has enough funds.
  + AWS couldn't verify that your card has enough funds.
  + AWS has applied restrictions to your account.

## What happens when you reach your Payment Threshold
<a name="payment-threshold-what-happens"></a>

When your usage reaches your Payment Threshold, AWS displays this information on the **Payments** page of the console and sends you a notification by email. In the coming days, AWS verifies that your default or backup card (if enabled) has enough funds to cover the Payment Threshold. To make sure that AWS can verify the availability of funds, you can take the following actions:
+ Keep a valid credit or debit card on file.
+ Verify that your card has enough funds to cover the Payment Threshold.
+ Contact your bank if you believe that your card is valid but AWS can't verify enough funds. Your bank might be declining the verification.

You might see a temporary hold on your statement for the Payment Threshold. AWS cancels the hold as soon as it verifies your card. Your bank then releases the funds, which can take a few days depending on your bank.

After AWS verifies your card, your services continue without interruption. AWS doesn't verify your card again during this billing month. Your Payment Threshold starts again in the next billing month.

Toward the end of each month, usage against your Payment Threshold stops updating and AWS doesn't attempt a verification, because your monthly invoice is generated soon after.

**Note**  
AWS Marketplace purchases are not included when AWS calculates usage toward your Payment Threshold.

## If AWS can't verify your card
<a name="payment-threshold-cant-verify"></a>

AWS attempts to verify the availability of funds multiple times in a billing month. If AWS still can't verify enough funds after several attempts, AWS restricts your account. These restrictions prevent you from using new resources, expanding usage, or linking new accounts.

To remove the restrictions, see [How to remove restrictions from your account](#payment-threshold-remove-restrictions).

## How to remove restrictions from your account
<a name="payment-threshold-remove-restrictions"></a>

If your account is restricted because your card didn't have enough funds, you can remove the restrictions yourself. How you remove them depends on whether you have past due monthly invoices.

If you have any past due monthly invoices, take the following action:
+ Pay all past due invoices on the [Payments page](https://console.aws.amazon.com/billing/home#/paymenthistory).

If you have no past due monthly invoices, AWS lifts your restrictions when it successfully verifies the card for the Payment Threshold. To rerun the verification, use one of the following methods:
+ Add a valid new card to rerun the verification. For instructions, see [Add a credit card](manage-cc.md#Add-cc).
+ Update your existing default card to rerun the verification. For instructions, see [Update a credit card](manage-cc.md#update-your-cc).
+ Verify your unverified card in **Payments Preferences** to rerun a verification. For instructions, see [Troubleshoot unverified credit cards](manage-cc.md#verify-cc).

When you add, update, or verify your credit or debit card, AWS performs another verification for the Payment Threshold. If the verification is successful, AWS removes the restrictions automatically.

## Payment Threshold availability
<a name="payment-threshold-availability"></a>

Payment Threshold is available for accounts that pay AWS directly by credit or debit card. If your account isn't eligible, you don't see a Payment Threshold in the console.

At this time, Payment Threshold isn't available for certain AWS accounts, for example:
+ Accounts that pay by bank account, invoice, net payment terms, or credit or debit card with 3D Secure (3DS), a type of multi-factor authentication.
+ Accounts billed through a reseller or through another account, such as managed or member accounts.
+ Accounts covered by Enterprise Support.
+ Accounts in the AWS Free Tier program or the AWS fast sign-up experience.
+ Accounts associated with more than one seller of record.
+ Accounts in the China Regions or accounts whose contracting party is AWS India.