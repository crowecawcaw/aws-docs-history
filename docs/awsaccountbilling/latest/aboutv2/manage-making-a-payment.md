# Making payments

You can use the **Payments** page of the AWS Billing and Cost Management console to pay your AWS bill using the process in this section.

AWS charges your default payment method automatically at the beginning of
each month. If that charge doesn't process successfully, you can use the console to
update your payment method and make a payment.

When you sign in as a bill transfer account:

- You are responsible for paying charges for AWS Organizations that transfer their bills to you.
- You can pay these charges using standard payment processes.
- You aren't responsible for charges from before billing transfer was active or after it's withdrawn.
  When you sign in as a bill source account:

- You might see payments due for usage that occurred before billing transfer was active.
- You are responsible for all charges from before billing transfer was active, even if you receive the invoice after activation.
  For example, if you accept a billing transfer invitation on November 15, the billing transfer becomes active on December 1. In early December, you receive invoices for usage through November 30. If you have unpaid November bills, you continue to receive payment requests after December, even while billing transfer is active.

###### Note

If you pay by ACH direct debit, AWS provides you with your invoice and
initiates the charge to your payment method within 10 days of the start of the month. It can take 3–5 days for your payment to succeed.
For more information, see [Manage ACH direct debit payment methods](manage-cc.md#manage-debit "manage-cc.md#manage-debit").

Before making a payment, ensure that the payment method that you want to be
automatically charged in the future is set as your default payment method. If you're
using a credit card, confirm that your credit card isn't expired. For more
information, see [Designate a default payment
method](manage-payment-method.md#manage-designate-default "manage-payment-method.md#manage-designate-default") and [Managing credit card and ACH direct debit](manage-cc.md "manage-cc.md").

###### To make a payment

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payments**.

The **Payments due** table lists all outstanding
invoices. If there are no invoices that are listed, you don't need to do
anything at this time. 3. If there are outstanding invoices, select the invoice that you want to pay
in the **Payments due** table, and then choose
**Complete payment**. 4. On the **Complete a payment** page, your default payment
method is selected if it's eligible for you to use to pay the invoice. If
you want to use a different payment method or choose an eligible payment
method, choose **Change**. 5. Confirm that the summary matches what you want to pay, and choose
**Verify and pay**.

After your bank processes your payment, you're redirected to the
**Payments** page.

Suppose that you pay by ACH direct debit, and you receive an email message
from AWS saying that AWS can't charge your bank account and will try
again. Then, work with your bank to understand what went wrong.

If you receive an email saying that AWS failed the last attempt to
charge your bank account, select the invoice to pay in the
**Payments due** table. Then, choose **Complete
payment** to pay the invoice. If you have questions about
issues with charging your bank account or paying an overdue balance, create
a case in the [Support
Center](https://console.aws.amazon.com/support/home?# "https://console.aws.amazon.com/support/home?#").

If you pay by electronic funds transfer and your account payment is
overdue, create a case in the [Support Center](https://console.aws.amazon.com/support/home?# "https://console.aws.amazon.com/support/home?#").
