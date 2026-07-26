# Managing credit cards

You can use the [Payment
preferences](https://console.aws.amazon.com/billing/home#/paymentpreferences "https://console.aws.amazon.com/billing/home#/paymentpreferences") page of the AWS Billing and Cost Management console to manage your credit
cards.

###### Topics

- [Add a credit card](#Add-cc "#Add-cc")
- [Update a credit card](#update-your-cc "#update-your-cc")
- [Troubleshoot unverified credit cards](#verify-cc "#verify-cc")
- [Delete a credit card](#delete-credit-card "#delete-credit-card")

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

###### To confirm that your credit card information is up-to-date

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
