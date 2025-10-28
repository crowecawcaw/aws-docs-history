# Using purchase orders for AWS Marketplace transactions

When you use purchase orders (POs) in AWS Marketplace and the AWS Billing console, you receive
invoices from AWS that include a purchase order (PO) number that you define. This approach
simplifies payment processing and cost allocation. In AWS Marketplace, out-of-cycle invoices include
purchases that are billed either immediately or according to a defined payment schedule in a
private offer. Generally, pay-as-you-go charges appear on a consolidated AWS Marketplace monthly usage
invoice.

## Using purchase orders for AWS Marketplace

transactions

You can add a PO at transaction time. AWS generates invoices
based on the provided PO, with each invoice associated with a single PO number.

###### To specify a PO in AWS Marketplace:

1. Find a product on AWS Marketplace and prepare to purchase it.
2. During the purchase process, under **Purchase order (PO) number**, choose
   **Add a purchase order**.
3. Enter your PO number in the **Purchase order number**
   field.

Your PO number is the identifier that you use to track it in your system. It's usually issued by an internal system or process and can be up to 200 characters in length. 4. (Optional) Specify the PO line number in the **Purchase
order line** field. The PO line number defaults to **1**. We recommend changing
the default only when you have a multi-line purchase order.

For transactions that result in multiple invoices, AWS Marketplace supports multiple POs.
You may encounter one or more of the following choices:

- **No PO number** – No PO numbers appear with your charges.
  This option provides no additional tracking or invoice details. If you have a PO in the billing console,
  it may still apply to this purchase.
- **One PO number for all charges** – Applies one purchase order to all fixed and pay-as-you-go charges,
  including one-time fees, recurring subscriptions, and usage-based services.
- **Separate PO numbers for fixed and usage charges** – Assign one PO number
  for all your fixed charges, such as up-front and recurring
  payments, and a separate PO number for all pay-as-you-go charges.
- **Unique PO numbers for each individual charge** – Specify a unique PO
  number for each charge on your account.

In addition, you can assign line numbers from purchase orders to the charges in a subscrition.

For information about a PO, including POs provided during AWS Marketplace
transactions, [view your purchase orders](../../../awsaccountbilling/latest/aboutv2/viewing-po.md "../../../awsaccountbilling/latest/aboutv2/viewing-po.md")
in the AWS Billing console.

## Adding a purchase order

during a transaction

The following steps explain how to add a PO number during a transaction.

From the **Offer acceptance** page, find the PO number.

1. Choose either one PO number for all charges or multiple PO
   numbers for individual charges.
2. Enter the PO number. The number can be up to 200 characters in
   length.
3. (Optional) If you have a multi-line purchase order, enter the PO line number. Otherwise, the PO line defaults to **1**. We recommend changing the default
   only when you have a multi-line purchase order.

## Updating a purchase order after a transaction

After subscribing to an AWS Marketplace product, you can use the **Subscription details** page to add a PO number. When a PO is
associated with a charge, the invoice for that charge includes
your PO number. You can provide the same PO number or different PO
numbers for each charge. For more information about usage charges, see
the [AWS Billing console](https://aws.amazon.com/aws-cost-management/aws-billing/faqs/ "https://aws.amazon.com/aws-cost-management/aws-billing/faqs/").

###### Note

You can only enter PO numbers for future charges.

###### To update a PO

1. From the **Subscription detail** page, navigate to the **Charge summary** container.
2. For each charge line item, you can enter a PO number in the **Purchase order numbers** column.
3. (Optional) If you have a multi-line purchase order, enter the PO line number. Otherwise, the PO line defaults to **1**. We recommend changing the default
   only when you have a multi-line purchase order.

###### Note

To add or update a purchase after invoice creation, contact
[AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

## Using blanket-usage purchase

orders

To separate AWS Marketplace charges from other POs, create
a PO with an AWS Marketplace blanket-usage line item in the
AWS Billing console. AWS Marketplace invoice transactions include the
blanket-usage PO that you specify if certain criteria and
parameters match (for example, billing entities). If you enter a PO
number in AWS Marketplace that differs from your blanket PO, the charge isn't
applied to your blanket PO.

For more information, see [Managing your purchase
orders](../../../awsaccountbilling/latest/aboutv2/manage-purchaseorders.md "../../../awsaccountbilling/latest/aboutv2/manage-purchaseorders.md").
