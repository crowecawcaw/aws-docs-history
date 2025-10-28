# Making partial payments

You can use the **Payments** page of the AWS Billing and Cost Management console to pay your
AWS bill using the partial payment method. This section outlines the procedure in the console, as well as how to troubleshoot scenarios if your payment attempt fails.

###### To make a partial payment

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payments**.

The **Payments due** table lists all outstanding
invoices. If there are no invoices that are listed, you don't need to do
anything at this time. 3. If there are outstanding invoices, select the invoices that you want to pay in the
**Payments due** table, and then choose
**Complete payment**. 4. On the **Complete a payment** page, your default payment method is
chosen.

    1. To continue with the default payment method, proceed to the next step.
    2. To use a different payment method, or if your current selection isn't eligible for partial payments, choose **Change**.
    3. To add a new payment method, see [Managing credit card and ACH direct debit](manage-cc.md "manage-cc.md").

5. In the **Payments due** table, select the invoices to pay.
6. Under the **Payment amount** column, enter the partial payment amount you're paying for each invoice.
7. Choose **Verify and pay**.

After your bank processes your payment, you're redirected to the
**Payments** page.

###### Note

- Chinese yuan (CNY) China Union Pay credit cards are not eligible for partial payments.
- Subscription invoices and AWS Marketplace invoices are not eligible for partial payments.

## Troubleshooting partial payments

If you receive an email notification that AWS failed the previous charge attempt on your payment card, attempt the following troubleshooting process.

###### To troubleshoot a partial payment charge fail

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payments**.
3. The **Payments due** table, select the invoices to pay.
4. Choose the amount to pay.
5. Choose **Complete payment**.

If the transaction continues to fail, contact your bank to understand why they are declining your transaction. Alternatively, you can pay with another eligible card.
