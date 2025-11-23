# View remaining invoices, unapplied funds, and

payment history

You can use the **Payments account summary** page in your Billing and Cost Management console to see your AWS account's financial status. This section outlines what each console component represents.

If you use transfer billing and you sign in as a bill transfer account, you see payments for charges from AWS Organizations that transfer their bills to you. When you sign in as a bill source account, you see payments for usage that occurred before billing transfer was active.

**Payments account summary**

This page shows your consolidated view of your AWS account's financial status. This includes what you owe AWS and the funds you have available to use. This is a simplified view to understand your payment obligations and manage your available balances.

**Total outstanding balance**

This shows the amount you currently owe, including any invoice amounts that are past due. To make a payment, see [Making payments](manage-making-a-payment.md "manage-making-a-payment.md").

**Total unapplied funds**

This is the total amount of unused funds that are currently available in your AWS account. This might include **unapplied cash**, **credit memos**, or **Advance Pay** balance. Advance Pay balance is automatically used to pay for your invoices. For more information, see [Using Advance Pay](manage-advancepay.md "manage-advancepay.md").

Your account might have unapplied funds or credit memos for various reasons, such as
past overpayments, missing remittance advice, or billing adjustments. To use
unapplied funds or credit memos towards your invoice payments or refund this
amount, send the AWS remittance instructions using the email address in
your invoice. You can also contact Support by following the instructions in [Contacting Support](billing-get-answers.md#billing-support "billing-get-answers.md#billing-support"). After you request
to use your unapplied funds, you can pay the total outstanding balance
excluding the unapplied funds amount.

###### Note

**Total unapplied funds** do not include AWS Credits. For more information, see [Applying AWS credits](useconsolidatedbilling-credits.md "useconsolidatedbilling-credits.md").

You can search and filter the **Payments due**,
**Unapplied funds**, and **Payment history**
tables described in the following procedures. Choose the gear icon to change the
default columns and customize other table settings. Download items individually by
choosing the appropriate ID, or choose **Download**, and then
**Download CSV** to download a CSV file of the table for
reporting purposes.

###### To view remaining invoice

payments

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payments**.
3. Choose the **Payments due** tab to view the
   **Payments due** table.

The **Payments due** table lists all your remaining
invoice payments. The table shows your total invoice amount and remaining
balance.

The table includes the following statuses:

    * **Due** – Outstanding invoices with an
     approaching due date.
    * **Past due** – Outstanding invoices with a
     payment that wasn't made by the due date.
    * **Scheduled**  – Invoices with an upcoming
     scheduled payment.
    * **Processing**  – Invoices that a payment
     is currently being scheduled for.

###### To view unapplied funds

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payments**.
3. Choose the **Unapplied funds** tab to view the
   **Unapplied funds** table.

The **Unapplied funds** table lists all unapplied credit
memos. The table shows your total invoice amount and remaining balance.

If the status is **Unapplied**, there are available
credit memos to be applied to an invoice.

If the status is **Partially applied**, there are credit
memos where some amounts have been applied to a previous invoice.

###### To view payment history

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payments**.
3. Choose the **Transactions** tab to view the
   **Transactions** table.

The **Transactions** table lists all completed
transactions with AWS.
