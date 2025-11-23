# Customizing your AWS payment preferences

You can use the [Payment
preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences") page of the AWS Billing and Cost Management console to perform the following tasks
for all payment types:

###### Topics

- [View your payment methods](#manage-view-credit "#manage-view-credit")
- [Designate a default payment
  method](#manage-designate-default "#manage-designate-default")
- [Remove a payment method](#manage-remove-credit "#manage-remove-credit")
- [Changing the currency to
  pay your bill](#manage-account-payment-change-currency "#manage-account-payment-change-currency")
- [Adding additional billing contact
  email addresses](#manage-billing-contact-emails "#manage-billing-contact-emails")
  For a list of accepted payment methods organized by AWS service providers ("SOR", "seller of record), see [What payment methods does AWS accept?](https://repost.aws/knowledge-center/accepted-payment-methods "https://repost.aws/knowledge-center/accepted-payment-methods") in the _Knowledge Center_.

For a full list of supported currencies, see [What currencies does AWS currently support?](https://repost.aws/knowledge-center/supported-aws-currencies "https://repost.aws/knowledge-center/supported-aws-currencies").

###### Notes

- IAM users need explicit permission to access some of the pages in the
  Billing console. For more information, see [Overview of managing access permissions](control-access-billing.md "control-access-billing.md").
- You can also use the **Payment preferences** page to manage
  your credit cards and direct debit accounts. For more information, see [Managing credit card and ACH direct debit](manage-cc.md "manage-cc.md") and [Manage ACH direct debit payment methods](manage-cc.md#manage-debit "manage-cc.md#manage-debit").
- If you use billing transfer, the bill transfer account controls the payment preferences for invoices of AWS Organizations that transfer their bills. The bill source account can configure and change existing payment preferences. However, these preferences don't take effect while billing transfer is active.

## View your payment methods

You can use the console to view the payment methods that are associated with your
account.

###### To view payment methods that are associated with your

AWS account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences").

Payment methods that are associated with your AWS account are listed in the
**Payment method** section.

## Designate a default payment

method

You can use the console to designate a default payment method for your AWS account.

If you receive invoices from more than one AWS service provider (seller of record or
SOR), you can use payment profiles to assign a unique payment method for each one. For
more information, see [Using payment profiles](manage-paymentprofiles.md "manage-paymentprofiles.md").

###### To designate a default payment method

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose [Payment preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences").

Payment methods that are associated with your AWS account are listed in
the **Payment method** section. 3. Next to the payment method that you want to use as your default payment
method, choose **Set as default**.

###### Note

More information or actions might be required, depending on your payment
method. Additional actions might include completing your tax registration
information or choosing a supported payment currency.

## Remove a payment method

You can use the console to remove a payment method from your account.

###### To remove a payment method from your

AWS account

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Ensure that your account has another valid payment method set as the
   default.
4. Select a payment method to remove, and choose
   **Delete**.
5. In the **Delete payment method** dialog box, choose
   **Delete**.

## Changing the currency to

pay your bill

To change the currency that you use to pay your bill, for example, from Danish
kroner to South African rand, perform the following procedure. For a full list of currencies supported by AWS, see [What currencies does AWS currently support?](https://repost.aws/knowledge-center/supported-aws-currencies "https://repost.aws/knowledge-center/supported-aws-currencies") in the _AWS Knowledge Center_.

###### To change the local currency that's associated with

your account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the navigation bar in the upper-right corner, choose your account name (or alias), and choose **Account**.
3. In the navigation pane, choose **Payment
   preferences**.
4. In the **Default payment preferences** section, choose
   **Edit**.
5. On the **Payment currency** section, choose the payment
   currency you want to use.
6. Choose **Save changes**.

If you receive invoices from multiple AWS service providers ("SOR", "seller of
record"), you can create a payment profile for each AWS service provider that
specifies each currency you prefer to use. For more information, see [Using payment profiles](manage-paymentprofiles.md "manage-paymentprofiles.md").

## Adding additional billing contact

email addresses

Use additional billing contacts to contact another person about billing related
items impacting your AWS accounts. Additional billing contacts will be contacted
with the root account contact and alternate billing contact about billing
events.

###### Notes

- If you use credit or debit cards as your payment method, see [Adding or updating alternate
  contacts](billing-getting-started.md#manage-account-payment-alternate-contacts "billing-getting-started.md#manage-account-payment-alternate-contacts").
- If you have pay by invoice as your payment method, you can use the
  following procedure to add additional billing contacts to receive
  emails.

###### To add additional billing contacts to your

account

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/home?#/ "https://console.aws.amazon.com/costmanagement/home?#/").
2. In the navigation pane, choose **Payment
   preferences**.
3. In the **Default payment preferences** section, choose
   **Edit**.
4. For **Billing contact email**, enter the additional
   billing contact email messages that you want AWS to send billing-related
   email notifications to.
5. Choose **Save changes**.
