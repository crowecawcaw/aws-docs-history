# Reviewing your monthly billing best practices

AWS uses information that you provide in the AWS Billing and Cost Management console to prepare and issue
your invoices with proper header information, such as your preferred payment currency, tax
settings, business legal name and address.

If this information is missing or inaccurate, AWS might issue inaccurate invoices that
you can't use or process.

Follow this 10-minute checklist before the end of the monthly billing period to review
your invoice and ensure that your information is up-to-date in your AWS account.

###### Contents

- [Check purchase order balance and
  expiration](monthly-billing-checklist.md#check-po-balanceexpiration "monthly-billing-checklist.md#check-po-balanceexpiration")
- [Review tax settings](monthly-billing-checklist.md#review-tax-settings "monthly-billing-checklist.md#review-tax-settings")
- [Enable tax setting
  inheritance](monthly-billing-checklist.md#turning-on-tax-setting-inheritance "monthly-billing-checklist.md#turning-on-tax-setting-inheritance")
- [Update billing contact
  information](monthly-billing-checklist.md#update-billing-contact-information "monthly-billing-checklist.md#update-billing-contact-information")
- [Review payment currency](monthly-billing-checklist.md#review-payment-currency "monthly-billing-checklist.md#review-payment-currency")

## Check purchase order balance and

expiration

As part of the procure-to-pay process, you can use purchase orders to procure
AWS services and approve invoices for payment. To avoid issues with billing and
payment, verify that your purchase orders aren't expired or out-of-balance.

###### To check purchase order balance and expiration

1. Navigate to the [Purchase orders](https://console.aws.amazon.com/billing/home#/purchaseorders "https://console.aws.amazon.com/billing/home#/purchaseorders") page in the AWS Billing and Cost Management console. The purchase
   order dashboard shows the state of your purchase orders.
2. Choose a purchase order to see the **Purchase order
   details** page.
3. Review the purchase order **Balance** and
   **Expiration** fields.

###### Tip

- You can set up email notifications so that you can proactively take action
  on expiring or out-of-balance purchase orders. For more information, see
  [Enabling purchase order notifications](notify-po-details.md "notify-po-details.md").
- To add a purchase order to use in your invoices, see [Adding a purchase order](adding-po.md "adding-po.md").

## Review tax settings

To determine your account's location for tax purposes, AWS uses the tax registration
number (TRN) and the business legal address associated with your account. A TRN is also
known as a value-added tax (VAT) number, VAT ID, VAT registration number, or business
registration number.

###### To review tax settings

1. Navigate to the [Tax
   settings](https://console.aws.amazon.com/billing/home#/tax-settings "https://console.aws.amazon.com/billing/home#/tax-settings") page in the Billing and Cost Management console.
2. Under the **Tax registrations** tab, select the account IDs
   to edit.
3. Under **Manage tax registration**,
   choose **Edit**.
4. Enter your updated information and then choose **Update**.

For more information, see [Updating and deleting
tax registration numbers](manage-account-payment.md#manage-account-payment-update-delete-tax-numbers "manage-account-payment.md#manage-account-payment-update-delete-tax-numbers").

## Enable tax setting

inheritance

The management account and member accounts that are part of AWS Organizations can have different
TRNs or the same TRN. Unless your organization needs to use different TRNs for member
accounts, we recommend that you enable tax settings inheritance.

After you enable this setting from the management account, your tax registration
information is added to your member accounts in your organization. This saves you time
so that you don't need to enter this information for individual accounts. Tax invoices
are processed with consistent tax information, and your usage from member accounts will
consolidate to a single tax invoice.

###### To enable tax settings inheritance

1. Navigate to the [Tax
   settings](https://console.aws.amazon.com/billing/home#/tax-settings "https://console.aws.amazon.com/billing/home#/tax-settings") page in the Billing and Cost Management console.
2. Under **Tax registrations**, select **Enable tax
   settings inheritance**.
3. In the dialog box, choose **Enable**.

For information about how to manage documents required for US tax exemptions, see
[Managing your US tax
exemptions](manage-account-payment.md#manage-account-tax-awstaxexemption "manage-account-payment.md#manage-account-tax-awstaxexemption").

## Update billing contact

information

Verify that your billing contact information is correct. AWS uses these contacts to
contact you about any billing or payment related communications. You can add additional
billing contacts in two ways:

- The **Payment preferences** page
- The **Accounts** page

###### To add billing contacts from the Payments preference page

1. Navigate to the [Payment
   preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods "https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods") page in the Billing and Cost Management console.
2. In the **Default payment preferences** section, review the
   **Billing contact email** field. AWS uses this contact
   for any billing or payment related communications.
3. Choose **Edit**.
4. In the **Billing contact email -
   _optional_** field, enter the email addresses
   that you want AWS to send billing related email notifications, payment
   reminders and payment support notifications to. You can add up to 15 email
   addresses.
5. Choose **Save changes**.

You can add alternate contacts so that AWS has an alternate email address to contact
about issues with your account, even if the AWS account root user contact is unavailable. For the
Billing alternate contact, you can specify the email address to receive the invoice.
Your alternate contact will be authorized to communicate with AWS for billing,
invoice, and payment issues.

The alternate contact doesn't have to be a specific person. For example, you can add
an email distribution list if you have a team that manages billing, operations, and
security related issues.

###### To update alternate contact information from the Accounts page

1. Navigate to the [Accounts](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") page in the Billing and Cost Management console and scroll down to the
   **Alternate contacts** section.
2. For the **Billing** field, review the contact information and
   confirm the email address where you want your invoices delivered.

For more information about how to use alternate contacts, see [Adding or updating alternate
contacts](billing-getting-started.md#manage-account-payment-alternate-contacts "billing-getting-started.md#manage-account-payment-alternate-contacts").

## Review payment currency

The payment currency is the currency that your default payment method will be
charged in. This is also the currency displayed on your invoice under your default
service provider. Some organizations can't process invoices that are issued in the wrong
currency, so it's important to ensure that your payment currency is accurate.

###### To review your payment currency

1. Navigate to [Payment
   preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods "https://console.aws.amazon.com/billing/home#/paymentpreferences/paymentmethods") in the Billing and Cost Management console.
2. In the **Default payment preferences** section,
   choose **Edit**.
3. In the **Payment currency** section, ensure that the
   **Default payment currency** is correct.

For more information about payment methods, see [Managing credit card and ACH direct debit](manage-cc.md "manage-cc.md").
