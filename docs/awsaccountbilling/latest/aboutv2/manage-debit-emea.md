# Managing your SEPA direct debit payment

method

AWS Europe customers can add a bank account to allow SEPA direct debit payments. You can
use any personal or business bank account, provided that the account is located at a
branch in a SEPA-supported country and payments are in the Euro currency.

If you pay by SEPA direct debit, AWS provides you with your invoice and
initiates the charge to your payment method either the following day or the invoice due date, whichever is latest. It can take up to 5 business days for the payment to complete
successfully, even if the payment shows as **Succeeded** in the
AWS Billing console.

You can use the [Payment
preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences") page of the AWS Billing console to perform the following SEPA
direct debit tasks:

###### Contents

- [Verify and link your bank account to
  your AWS Europe payment methods](manage-debit-emea.md#direct-link-verify-account "manage-debit-emea.md#direct-link-verify-account")
- [Manually add a direct debit
  account to your AWS Europe payment methods](manage-debit-emea.md#manually-add-direct-debit-account-emea "manage-debit-emea.md#manually-add-direct-debit-account-emea")
- [Update your direct
  debit account information](manage-debit-emea.md#update-your-direct-debit-account-information "manage-debit-emea.md#update-your-direct-debit-account-information")

## Verify and link your bank account to

your AWS Europe payment methods

###### Note

To use this feature, you must have a billing address in Germany, Netherlands, Spain, United Kingdom, France, Italy, Finland, Ireland, Austria, or Belgium. To
change your billing address, see [Update your direct
debit account information](#update-your-direct-debit-account-information "#update-your-direct-debit-account-information").

You can verify and link a SEPA direct debit account to your AWS account by
signing in to your bank account. We ask that you to sign in to your bank account, so
that we can verify your identity and confirm your ownership of the bank
account.

AWS works with TrueLayer to connect to your bank and securely
verify ownership of your bank account. Your information is protected with an
encrypted end-to-end connection during this one-time validation process. Your
personal data won’t be shared or used beyond the purpose of verifying that you're
the owner of the connected bank account.

If you don't have access to the bank account sign in credentials, you can create
an IAM entity (such as a user or role) for the bank account owner to provide them
access to the Billing console. Then, they can update the AWS account payment
method. We recommend that you don't share sensitive information, including username,
password, or payment methods for your account. For more information, see the
following topics:

- [Overview of managing access permissions](control-access-billing.md "control-access-billing.md")
- [Best practices to protect your account's root
  user](../../../accounts/latest/reference/best-practices-root-user.md "../../../accounts/latest/reference/best-practices-root-user.md") in the _AWS Account Management Reference
  Guide_

###### To verify and link your bank account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose **Add payment method**.
4. Choose **Bank account**.
5. Choose **Sign in to your bank**.
6. Choose **Link your bank account**.
7. Select your bank name.
8. Choose **Allow**. The information that you share will
   only be used to confirm your ownership of the bank account and to prevent
   fraud.
9. Sign in to your bank account. Use the credentials for your bank account,
   _not_ the credentials for your AWS account. Your
   connection is encrypted and your credentials are protected. AWS won't
   access or store your online banking credentials.

###### Note

Your bank might ask that you sign in your account with multi-factor
authentication (MFA). 10. For **Billing address information**, enter the billing
address of the primary account owner. 11. Choose **Add payment method** to agree to the
**Terms and Conditions** and add your direct debit
account. Your bank account is now verified and added to your AWS Europe payment
methods.

###### Note

AWS won't access or store your online banking credentials. AWS will ask
for your explicit consent and will only request the following information from
your bank:

- Name of account holder
- Account number
  Your bank might ask for your consent to share additional information. However,
  any additional information won't be shared with AWS. AWS can confirm your
  ownership of the bank account and charge your bank account after we first
  collect this information. AWS access to this information will expire based on
  local regulations and your bank’s policy.

To remove direct debit payments from your account, see [Remove a payment method](manage-payment-method.md#manage-remove-credit "manage-payment-method.md#manage-remove-credit"). To
remove AWS data access to your bank information, see the [TrueLayer documentation](https://support.truelayer.com/hc/en-us/articles/360025794833-Can-my-users-revoke-their-access-to-TrueLayer "https://support.truelayer.com/hc/en-us/articles/360025794833-Can-my-users-revoke-their-access-to-TrueLayer").

## Manually add a direct debit

account to your AWS Europe payment methods

To manually add a direct debit account, you must meet the following
requirements:

- Paid at least one invoice in full in the previous 12 months
- Paid at least 100 (USD or EUR) cumulatively over the previous 2 months.

Before you add your payment method, you need the following information:

- Bank Identifier Code (BIC)
- International Bank Account Number (IBAN)
- The address that the bank associates with the account

###### To manually add a SEPA direct debit account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose **Add payment method**.
4. Choose **Bank account**.
5. For **Account Holder Name**, enter the name of the
   principal account holder.
6. For **BIC (Swift Code)**, enter the 8 or 11 digit number.
   Routing numbers are either 8 or 11 digits long.
7. For **Confirm BIC (Swift Code)**, reenter the BIC. Don't
   copy and paste.
8. For **IBAN**, enter the digits for the IBAN.
9. For **Reenter IBAN**, reenter the IBAN digits. Don't copy
   and paste.
10. For **Make Default**, select whether you want this direct
    debit account to be your default payment method.
11. For **Billing Address information**, enter the billing
    address of the primary account holder.
12. Choose **Add bank account** to agree to the
    **Terms and Conditions** and add your direct debit
    account.

## Update your direct

debit account information

You can update the name, address, or phone number that's associated with your
direct debit account.

###### To update your direct debit account

information

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.

Payment methods that are associated with your AWS account are listed in
the **Payment method** section. 3. Select the direct debit account that you want to edit, and choose
**Edit**. 4. Update the fields that you want to change. 5. At the bottom of the dialog box, choose **Save
changes**.
