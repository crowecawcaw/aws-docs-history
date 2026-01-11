# Managing your Bacs direct debit payment

method

AWS Europe customers can add a bank account to allow Bacs direct debit payments. You can
use any personal or business bank account, provided that the account is located in the UK and payments are made using British pound (GBP).

If you pay by UK direct debit, AWS provides your invoice and initiates the charge to your payment method within three business days. It can take up to six business days for the payment to complete successfully, even if the payment shows as **Succeeded** in the
AWS Billing console.

You can use the [Payment
preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences") page of the AWS Billing console to perform the following UK direct debit tasks:

###### Contents

- [Verify and link your bank account to
  your AWS Europe payment methods](manage-bacs-emea.md#direct-link-verify-account-bacs "manage-bacs-emea.md#direct-link-verify-account-bacs")
- [Update your direct
  debit account information](manage-bacs-emea.md#update-your-direct-debit-account-information-bacs "manage-bacs-emea.md#update-your-direct-debit-account-information-bacs")
- [Bacs direct debit guarantee](manage-bacs-emea.md#payments-guarantee-bacs "manage-bacs-emea.md#payments-guarantee-bacs")

## Verify and link your bank account to

your AWS Europe payment methods

You can verify and link a Bacs direct debit account to your AWS account by
signing in to your bank account and approving a penny charge. You must sign in to your bank account to verify ownership of the bank
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
4. Choose **Bacs Direct Debit** and **Choose bank**.
5. Choose your bank from the provided options.
6. Sign in to your bank account to confirm the penny charge. Use the credentials for your bank account,
   _not_ the credentials for your AWS account. Your
   connection is encrypted and your credentials are protected. AWS won't
   access or store your online banking credentials.
7. Choose **Confirm payment**. The information that you share will
   only be used to confirm your ownership of the bank account and to prevent
   fraud. You will be refunded immediately.
8. For **Billing address information**, enter the billing
   address of the primary account owner.
9. Choose **Add payment method** to agree to the
   **Terms and Conditions** and add your direct debit
   account. Your bank account is now verified and added to your AWS Europe payment
   methods.

###### Note

AWS won't access or store your online banking credentials. AWS will ask
for your explicit consent and will only request the following information from
your bank:

- Name of account holder
- Account number
- Mandate ID
  Your bank might ask for your consent to share additional information. However,
  any additional information won't be shared with AWS. AWS can confirm your
  ownership of the bank account and charge your bank account after we first
  collect this information. AWS access to this information will expire based on
  local regulations and your bank’s policy.

To remove direct debit payments from your account, see [Remove a payment method](manage-payment-method.md#manage-remove-credit "manage-payment-method.md#manage-remove-credit"). To
remove AWS data access to your bank information, see the [TrueLayer documentation](https://support.truelayer.com/hc/en-us/articles/360025794833-Can-my-users-revoke-their-access-to-TrueLayer "https://support.truelayer.com/hc/en-us/articles/360025794833-Can-my-users-revoke-their-access-to-TrueLayer").

## Update your direct

debit account information

You can update the name, address, or phone number that's associated with your
Bacs direct debit account.

###### To update your Bacs direct debit account

information

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.

Payment methods that are associated with your AWS account are listed in
the **Payment method** section. 3. Select the direct debit account that you want to edit, and choose
**Edit**. 4. Update the fields that you want to change. 5. At the bottom of the dialog box, choose **Save
changes**.

## Bacs direct debit guarantee

This guarantee is offered by all banks and building societies that accept instructions to pay by direct debit.

- If there are any changes to the amount, date, or frequency of your direct debit, AWS Europe will notify you two business days in advance of your account being debited or as otherwise agreed.
- If you request AWS Europe to collect a payment, we will provide confirmation of the amount and date at the time of the request.
- If an error is made in the payment of your direct debit by AWS Europe or your bank or building society, you are entitled to a full and immediate refund of the amount paid from your bank or building society.
- If you receive a refund you are not entitled to, you must repay it when requested by AWS Europe.
- You can cancel a direct debit at any time by contacting your bank or building society. Written
  confirmation might be required. You must also notify AWS.
