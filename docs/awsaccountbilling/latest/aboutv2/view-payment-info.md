

# View remaining invoices, unapplied funds, and payment history
<a name="view-payment-info"></a>

You can use the **Payments account summary** page in your Billing and Cost Management console to see your AWS account's financial status. This section outlines what each console component represents.

If you use transfer billing and you sign in as a bill transfer account, you see payments for charges from AWS Organizations that transfer their bills to you. When you sign in as a bill source account, you see payments for usage that occurred before billing transfer was active.

**Payments account summary**  
This page shows your consolidated view of your AWS account's financial status. This includes what you owe AWS and the funds you have available to use. This is a simplified view to understand your payment obligations and manage your available balances.

**Total outstanding balance**  
This shows the amount you currently owe, including any invoice amounts that are past due. To make a payment, see [Making payments](manage-making-a-payment.md).

**Total unapplied funds**  
This is the total amount of unused funds that are currently available in your AWS account. This might include **unapplied cash**, **credit memos**, or **Advance Pay** balance. Advance Pay balance is automatically used to pay for your invoices. For more information, see [Using Advance Pay](manage-advancepay.md).  
Your account might have unapplied funds or credit memos for various reasons, such as past overpayments, missing remittance advice, or billing adjustments. To use unapplied funds or credit memos towards your invoice payments or refund this amount, send the AWS remittance instructions using the email address in your invoice. You can also contact Support by following the instructions in [Contacting Support](billing-get-answers.md#billing-support). After you request to use your unapplied funds, you can pay the total outstanding balance excluding the unapplied funds amount.  
**Total unapplied funds** do not include AWS Credits. For more information, see [Applying AWS credits](useconsolidatedbilling-credits.md).

You can search and filter the **Payments due**, **Unapplied funds**, and **Transactions** tables described in the following procedures. Choose the gear icon to change the default columns and customize other table settings. Download items individually by choosing the appropriate ID, or choose **Download**, and then ** Download CSV** to download a CSV file of the table for reporting purposes.<a name="view-outstanding-invoices-procedure"></a>

**To view remaining invoice payments**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Payments**.

1. Choose the **Payments due** tab to view the **Payments due** table. 

   The **Payments due** table lists all your remaining invoice payments. The table shows your total invoice amount and remaining balance.

   The table includes the following statuses:
   + **Due** – Outstanding invoices with an approaching due date.
   + **Past due** – Outstanding invoices with a payment that wasn't made by the due date.
   + **Scheduled ** – Invoices with an upcoming scheduled payment.
   + **Processing ** – Invoices that a payment is currently being scheduled for.<a name="view-unapplied-funds-procedure"></a>

**To view unapplied funds**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Payments**.

1. Choose the **Unapplied funds** tab to view the **Unapplied funds** table. 

   The **Unapplied funds** table lists all unapplied credit memos. The table shows your total invoice amount and remaining balance. 

   If the status is **Unapplied**, there are available credit memos to be applied to an invoice. 

   If the status is **Partially applied**, there are credit memos where some amounts have been applied to a previous invoice.<a name="view-payment-history-procedure"></a>

**To view payment history**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Payments**.

1. Choose the **Transactions** tab to view the **Transactions** table. 

   With the **Transactions** table, you get a single, real-time view to reconcile your payments and understand your account balances. In one place, you can view the status and amounts for your invoices, payments, refunds, credit memos, and unapplied funds (payments not yet applied to an invoice). You can also view adjustments (including adjustment sub-types), enterprise Advance Pay summary, and scheduled payment status. Forgiven invoices and credit memo transactions are also included.

   For each invoice, you can view the payment method used and download the invoice PDF. You can select an invoice to complete a payment. To find specific records, you can filter and sort the table, including by purchase order. If you use transfer billing, the table also reflects your transfer billing activity.

Each invoice, payment, and credit memo in the **Transactions** table has a details page that shows how payments and credits were applied. Use it to reconcile your account when one payment covers several invoices, or when you pay one invoice in several payments.<a name="view-transaction-details-procedure"></a>

**To view transaction details**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Payments**.

1. Choose the **Transactions** tab, and then choose the ID of an invoice, payment, or credit memo to open its details page.
   + **Invoice** – The **Transaction history** table lists the payments, credit memos, and adjustments applied to the invoice, with the balance due after each one. **Additional information** shows the charge type, purchase order number, billing period, service provider, usage consolidation account, and payment method.
   + **Payment** – The **Invoices paid** table lists the invoices that the payment was applied to, with the payment's available balance after each one.
   + **Credit memo** – The **Invoices credited** table lists the invoices that the credit memo was applied to, with each invoice's starting and ending balance.

   To open a related record, choose its ID. To download the PDF, choose **Download invoice** or **Download credit memo**. Each details page has its own URL, which you can bookmark or share with others who have access to the account.