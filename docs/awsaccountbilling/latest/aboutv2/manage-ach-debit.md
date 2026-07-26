# Managing ACH direct debit

You can add a US bank account to your AWS account to make payments by ACH direct
debit. You can use any personal or business bank account, provided that the account
is located at a bank in the United States and payments are in USD.

We offer two ways to add a US bank account. You can link your bank account
through your online banking credentials for immediate verification, or you can
manually enter your bank account and routing number.

If you pay by ACH direct debit, AWS provides you with your invoice and
initiates the charge to your payment method within 10 days of the start of the month. It can take up to 20 days for the payment to complete
successfully, even if the payment shows as **Succeeded** in the
AWS Billing and Cost Management console.

You can use the [Payment
preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences") page of the AWS Billing and Cost Management console to perform the following US bank
account tasks:

###### Topics

- [Link your bank account to your AWS payment methods](#link-ach-bank-account "#link-ach-bank-account")
- [Manually add a direct debit account to your AWS payment methods](#manually-add-ach-bank-account "#manually-add-ach-bank-account")
- [Update your direct debit account information](#update-ach-bank-account "#update-ach-bank-account")

## Link your bank account to your AWS payment methods

You can link your US bank account to your AWS account by signing in to your
bank account. This verifies your ownership of the bank account immediately, so
you do not need to manually enter your routing and account numbers.

We work with Finicity, a Mastercard company, to
connect to your bank and securely verify ownership of your bank account. An
encrypted end-to-end connection protects your information during this one-time
validation process. We only use your personal data to verify that you own the
connected bank account.

###### To link your bank account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose **Add payment method**.
4. For **Bank account setup method**, choose
   **Link your bank account**.
5. Select your bank from the provided options.
6. Sign in to your bank account. Use the credentials for your bank
   account, not the credentials for your AWS account. Your connection is
   encrypted and your credentials are protected. We don't access or store
   your online banking credentials.

###### Note

Your bank might ask that you sign in your account with
multi-factor authentication (MFA). 7. (Optional) For **Set as default payment method**,
select whether you want this direct debit account to be your default
payment method. 8. For **Billing address information**, enter the billing
address of the primary account owner. 9. (Optional) Enter the tag key and value. You can add up to 50 tags. For
more information on tags, see [Managing Your Payments using tags](manage-payments-tags.md "manage-payments-tags.md"). 10. Choose **Add payment method** to agree to the
**Terms and Conditions** and add your bank account. Your
bank account is now verified and added to your AWS payment
methods.

###### Note

Your online banking credentials stay with your bank. We do not access or
store them. Your bank might ask for your consent to share additional
information. We can confirm your ownership of the bank account and charge
your bank account after we first collect this information. Our access to
this information will expire based on local regulations and your bank's
policy.

To remove direct debit payments from your account, see [Remove a payment method](manage-payment-method.md#manage-remove-credit "manage-payment-method.md#manage-remove-credit").

## Manually add a direct debit account to your AWS payment methods

If you meet the eligibility requirements, add a US bank account as an ACH
direct debit payment method to your payment methods.

To be eligible, you must be an Amazon Web Services customer and also meet the following
requirements:

- You created your AWS account at least 60 days ago
- You paid at least one invoice (in full) in the previous 12 months
- You paid at least $100 (cumulatively) over the previous 12 months
- You set USD as the preferred currency

Before you add a direct debit account, have the following information
ready:

- A US bank account number
- A US bank account routing number
- The address that's associated with the bank account
- (For a personal bank account) A US driver's license number or other
  state-issued ID number
- (For a business bank account) A Federal tax ID number

###### To manually add a direct debit account to your AWS account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose **Add payment method**.
4. Choose **Bank account (ACH)**.
5. For **Account type**, choose
   **Personal** or **Business**.
6. For **Name on account**, enter the name of the
   principal account holder.
7. For **Bank routing number**, enter the nine-digit
   routing number.

Routing numbers are always nine digits long. Some banks list the
routing number first on a check. Other banks list the account number
first. 8. For **Re-enter bank routing number**, enter the
routing number again. 9. For **Checking account number**, enter the account
number.

Account numbers might be up to 17 digits long. The account must be an
ACH-enabled checking account at a bank that's located in the US. 10. For **Re-enter checking account number**, enter the
bank account number again. 11. For personal bank accounts:

    1. For **Driver's license number or other state-issued
     ID**, enter the primary account holder's valid US
     driver's license or other state-issued ID number.
    2. For **State of ID issued**, enter the name of
     the state.

12. For business bank accounts, for **Tax ID**, enter the
Federal tax ID for the business. 13. (Optional) For **Set as default payment method**,
select whether you want this direct debit account to be your default
payment method. 14. For **Billing address**, enter the valid US billing
address of the primary account holder. 15. (Optional) Enter the tag key and value. You can add up to 50 tags. For
more information on tags, see [Managing Your Payments using tags](manage-payments-tags.md "manage-payments-tags.md"). 16. Choose **Add payment method** to agree to the
**Terms and Conditions** and add your direct debit
account. Your bank account is now verified and added to your AWS
payment methods.

## Update your direct debit account information

You can update the name, address, or phone number associated with your direct
debit account.

###### To update your direct debit account information

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Select the direct debit account that you want to edit, and choose
   **Edit**.
4. Update the fields that you want to change.
5. Choose **Save changes**.
