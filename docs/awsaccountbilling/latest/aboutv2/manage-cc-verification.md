

# Managing your payment verifications
<a name="manage-cc-verification"></a>

Your bank might ask you for additional verification whenever you use a credit card to pay AWS online, add or update a credit card, or register a new AWS account. 

If your bank requires additional verification, you will be redirected to your bank's website. Follow the instructions from your bank to complete the verification process. To complete verification, your bank might ask you to:
+ Enter a one-time SMS code
+ Use your bank's mobile application to verify your credit card
+ Use biometrics or other authentication methods

**Contents**
+ [Best practices for verification](#cc-mfa-bp)
+ [Payment verification](#payment-verification)
+ [Troubleshooting payment verification](#cc-bp)
+ [AWS Organizations](#cc-awsorg)
+ [Subscription purchases](#bulk-purchases)

## Best practices for verification
<a name="cc-mfa-bp"></a>
+ Confirm that your default payment method is verified. See [Troubleshoot unverified credit cards](manage-cc.md#verify-cc).
+ Confirm that your credit card information with your bank is up-to-date. Banks send verification codes only to the registered card owner.
+ Enter the newest code. If you close the authentication portal or request a new code, you might experience a delay in receiving your newest code.
+ Enter the code as prompted. Don't enter the phone number that the code is sent from.

## Payment verification
<a name="payment-verification"></a>

You can use the AWS Billing console to confirm that your payment requires verification or to reattempt any failed payments.

You will receive an email from AWS if your bank needs to verify your payments.<a name="emea-payment-verification-process"></a>

**To verify your payment**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Payments**.

1. Under **Payments due**, locate the invoice that you want to pay and choose **Verify and pay**.

1. On the choose [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences) page, select the preferred payment method.

1. Choose **Complete payment**.

1. If your payment requires verification, you're redirected to your bank's website. To complete verification, follow the provided prompts.

After your bank processed our payment, you're redirected to the **Payments** page.

**Note**  
Your invoice appears with a **Payment processing** status until your bank completes the payment process. 
Payment cards for AWS Japan customers appear on the preference page after the verification process completes.

## Troubleshooting payment verification
<a name="cc-bp"></a>

If you can't successfully complete your verification, we recommend that you take any of the following actions:
+ Navigate to the [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences) page of the AWS Billing console and ensure that your credit card is verified. See [Troubleshoot unverified credit cards](manage-cc.md#verify-cc).
+ Navigate to the [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences) page of the AWS Billing console and update your billing contact information.
+ Contact your bank to confirm that your contact information is up to date.
+ Contact your bank for details about why your verification has failed.
+ Clear your cache and cookies or use a different browser.

## AWS Organizations
<a name="cc-awsorg"></a>

If you're a member account in AWS Organizations, your purchased services that require upfront payments might not activate until the Management account user verifies the payment. If verification is required, AWS notifies the billing contact of the Management account by email.

Establish a communication process between your Management account and member accounts.

## Subscription purchases
<a name="bulk-purchases"></a>

Suppose that you purchase multiple subscriptions at a time (or in bulk) and your bank requests verification. Then, the bank might ask you to verify each individual purchase.

Subscriptions can include immediate purchases such as Reserved Instances, Business Support plan, and Route 53 domains. Subscriptions don't include AWS Marketplace charges.

Make sure to complete validation for all purchases.