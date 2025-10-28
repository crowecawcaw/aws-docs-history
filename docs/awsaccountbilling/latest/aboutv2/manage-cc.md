# Managing credit card and ACH direct debit

You can use the [Payment
preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences") page of the AWS Billing and Cost Management console to manage your credit cards
and ACH direct debit payment methods.

###### Topics

- [Add a credit card](#Add-cc "#Add-cc")
- [Update a credit card](#update-your-cc "#update-your-cc")
- [Troubleshoot unverified credit cards](#verify-cc "#verify-cc")
- [Delete a credit card](#delete-credit-card "#delete-credit-card")
- [Manage ACH direct debit payment methods](#manage-debit "#manage-debit")

###### Note

If you're paying with a Chinese yuan credit card, see [Use a Chinese yuan credit card](manage-payment-cny.md#yuan-cc "manage-payment-cny.md#yuan-cc").

## Add a credit card

You can use the Billing and Cost Management console to add a credit card to your account.

###### To add a credit card to your AWS account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose **Add payment method**.
4. Enter the credit card information.
5. (Optional) For **Set as default payment method**, select
   whether you want this credit card to be your default payment method.
6. Enter your card billing address.
7. (Optional) Enter the tag key and value. You can add up to 50 tags. For more information on tags, see [Managing Your Payments using tags](manage-payments-tags.md "manage-payments-tags.md").
8. Verify your information and then choose **Add payment
   method**.

## Update a credit card

You can update the expiration date, name, address, and phone number that's
associated with your credit card.

###### Note

When you add or update your credit card, AWS charges any unpaid invoices
from the previous month to the new card.

###### To update a credit card

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.

Payment methods associated with your AWS account appear in the
**Payment methods** section. 3. Select the credit card to edit and then choose
**Edit**. 4. Update the information that you want to change. 5. Verify your changes and then choose **Save
changes**.

## Troubleshoot unverified credit cards

To make a payment, you must have a valid, unexpired credit card on file.

###### To confirm that your credit card

information is up-to-date

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Review your **Payments methods**. If your credit card is
   unverified, choose **Verify** and follow the
   prompts.
4. If you still can't verify this credit card, follow these steps:
   1. Choose the payment method and then choose
      **Delete**.
   2. Choose **Add payment method**, and then enter
      your credit card information again.
   3. Follow the prompts to verify your credit card information.

###### Note

Your bank might ask for additional verification. You will be redirected to
your bank's website. For more information, see [Managing your payment verifications](manage-cc-verification.md "manage-cc-verification.md").

## Delete a credit card

Before you delete your credit card, ensure that your AWS account has another
valid payment method set as the default.

You can’t delete a payment method that is set to default.

###### To delete a credit card

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/home?#/ "https://console.aws.amazon.com/costmanagement/home?#/").
2. In the navigation pane, choose **Payment preferences**.
   Payment methods associated with your AWS account appear in the
   **Payment method** section.
3. Select the payment method and then choose
   **Delete**.
4. In the **Delete payment method?** dialog box, choose
   **Delete**.

## Manage ACH direct debit payment methods

If you meet the eligibility requirements, add a US bank account as an ACH direct
debit payment method to your payment methods.

To be eligible, you must be an Amazon Web Services customer and also meet the following
requirements:

- You created your AWS account at least 60 days ago
- You paid at least one invoice (in full) in the previous 12 months
- You paid at least $100 (cumulatively) over the previous 12 months
- You set USD as the preferred currency

If you pay by ACH direct debit, AWS provides you with your invoice and
initiates the charge to your payment method within 10 days of the start of the month. It can take up to 20 days for the payment to complete
successfully, even if the payment shows as **Succeeded** on the
AWS Billing and Cost Management console.

You can use Billing and Cost Management console to add or update a direct debit account.

###### Contents

- [Add a direct debit account](manage-cc.md#adding-direct-debit-account "manage-cc.md#adding-direct-debit-account")
- [Update direct debit
  account](manage-cc.md#updating-direct-debit-account "manage-cc.md#updating-direct-debit-account")

### Add a direct debit account

You can use the AWS Billing and Cost Management console to add a direct debit account to your
AWS payment methods. You can use any personal or business bank account,
provided that the account is located at a branch in the US.

Before you add an ACH direct debit account, have the following information
ready:

- A US bank account number
- A US bank account routing number
- The address that's associated with the bank account
- (For a personal bank account) A US driver's license number or other
  state-issued ID number
- (For a business bank account) A Federal tax ID number

###### To add a direct debit account to your

AWS account

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose **Add payment method**.
4. Choose **Bank account (ACH)**.
5. For **Account type**, choose
   **Personal** or **Business**.
6. For **Name on account**, enter the name of the principal
   account holder.
7. For **Bank routing number**, enter the nine-digit routing
   number.

Routing numbers are always nine digits long. Some banks list the routing
number first on a check. Other banks list the account number first. 8. For **Re-enter bank routing number**, enter the routing
number again. 9. For **Checking account number**, enter the account
number.

Account numbers might be up to 17 digits long. The account must be an
ACH-enabled checking account at a bank that's located in the US. 10. For **Re-enter checking account number**, enter the bank
account number again. 11. For personal bank accounts:

    1. For **Driver's license number or other state-issued
     ID**, enter the primary account holder's valid US
     driver's license or other state-issued ID number.
    2. For **State of ID issued**, enter the name of the
     state.

12. For business bank accounts, for **Tax ID**, enter the
    Federal tax ID for the business.
13. (Optional) For **Set as default payment method**, select
    whether you want this direct debit account to be your default payment
    method.
14. For **Billing address**, enter the valid US billing
    address of the primary account holder.
15. (Optional) Enter the tag key and value. You can add up to 50 tags. For more information on tags, see [Managing Your Payments using tags](manage-payments-tags.md "manage-payments-tags.md").
16. Choose **Add payment method** to agree to the
    **Terms and Conditions** and add your direct debit
    account.

### Update direct debit

account

You can update the name, address, or phone number that's associated with your
direct debit account.

###### To update a direct debit account

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.

Payment methods that are associated with your AWS account are listed
in the **Payment method** section. 3. Select the direct debit account that you want to edit and then choose
**Edit**. 4. Update the information that you want to change. 5. Verify your changes and then choose **Save
changes**.
