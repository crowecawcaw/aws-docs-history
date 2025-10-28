# Managing your purchase orders

You can use your Billing and Cost Management console to manage your purchase orders and configure how they
reflect on your invoices. You have the option to add multiple purchase orders with multiple
line items. Based on your configurations, we select the purchase order that best matches
with your invoice. You can manage purchase orders if you're using a regular AWS account or
an AWS Organizations management account. For more information about accessing the feature, see [Overview of managing access permissions](control-access-billing.md "control-access-billing.md").

Each purchase order can have several line items, and every line item is used for matching
with invoices. The following types of line items are available:

- **ALL** – All charges on your AWS
  account.
- **AWS Monthly Usage** – Your AWS monthly
  invoice charges.
- **AWS Subscription Purchase** – Your
  subscription invoice charges; for example, upfront charges for Reserved Instances
  (RI) and Support charges.
- **AWS Marketplace Transaction** – Your purchase order line item for
  invoice charges from an AWS Marketplace transaction. This is available only for the
  following entities, because all AWS Marketplace invoices are generated from these seller of records: Amazon Web Services Inc., Amazon Web Services Australia Pty Ltd, Amazon Web Services EMEA SARL, Amazon Web Services Korea LLC, Amazon Web Services Japan G.K.. If you use consolidated billing and an authorized linked account provides purchase orders for an AWS Marketplace transaction, AWS Marketplace creates a corresponding purchase order resource in your payer account. This purchase order is then associated with the relevant invoices for that transaction. Buyer accounts with the `UpdatePurchaseOrders` permission can create purchase orders that appear in the payer account.
- **AWS Marketplace Blanket Usage** – Your default purchase order for
  AWS Marketplace invoice charges. This is available only for the
  following entities, because all AWS Marketplace invoices are generated from these seller of records: AWS Inc., AWS EMEA SARL, AWS Australia, and AWS New Zealand. All invoices with AWS Marketplace subscriptions contain an **AWS Marketplace Blanket
  Usage** line item, unless the subscription has a transaction-specific
  purchase order. If the subscription has a transaction-specific purchase order, then
  your invoice has an **AWS Marketplace Transaction** line item instead.
- **AWS Professional Services and Training Purchase** – Your default
  purchase order line item for invoice charges from AWS Professional Services and
  Training. This applies to all consulting, in-person, or digital training services,
  and is only available for the AWS Inc. entity. This line item only supports
  invoices outside of your normal monthly billing cycle.
  Many criteria and parameters are used to determine the optimal purchase order for your
  invoices. You can create up to 100 active purchase orders with up to 100 line items for each
  regular account or AWS Organizations management account.

When an invoice is generated, all purchase orders that are added to your
management account are considered for association. Then, expired or suspended purchase orders
are filtered out, leaving only the active purchase orders. Your invoice’s billing entity is
matched with the “Bill from” entity in your purchase order, filtering out those that don’t
match. For example, if you have a purchase order added for the AWS Inc. entity (PO_1), and
another one for the AWS EMEA SARL entity (PO_2). If you purchase a Reserved Instance from
AWS Europe, only PO_2 will be considered for invoice association.

Next, we evaluate line item configurations to determine the best fit for your invoice. To
be matched with a line item, the invoice's billing period must be within the line item's
start and end month, and it must also match the line item type. If multiple line items
match, we use the line item with the most specific type for invoice association. For
example, if you have an RI invoice, we use the subscription line item instead of ALL if both
are configured.

Lastly, the line items with enough balance to cover your invoice amount are selected above
the out of balance line items. If line items that belong to multiple purchase orders match
all criteria precisely, we use the purchase order that was most recently updated to match
the invoice.

###### Topics

- [Setting up purchase order configurations](setup-po-lineitem.md "setup-po-lineitem.md")
- [Adding a purchase order](adding-po.md "adding-po.md")
- [Editing your purchase orders](edit-po.md "edit-po.md")
- [Deleting your purchase orders](delete-po.md "delete-po.md")
- [Viewing your purchase orders](viewing-po.md "viewing-po.md")
- [Reading your purchase order details page](reading-po-details.md "reading-po-details.md")
- [Enabling purchase order notifications](notify-po-details.md "notify-po-details.md")
- [Use tags to manage access
  to purchase orders](manage-access-to-purchase-orders-with-tags.md "manage-access-to-purchase-orders-with-tags.md")
