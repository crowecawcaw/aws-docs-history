# Using AWS invoice configuration with other

services

Once you create an invoice unit, you can use AWS invoice configuration with other Billing and Cost Management
services.

## Associating purchase orders to

invoice units

You have the option to associate a purchase order to one or more invoice
units.

###### To associate purchase

orders

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Purchase
   orders**.
3. Add invoice units using the following steps:
   - When creating a new purchase order
     1. Choose **Add purchase order** to create a
        purchase order.
     2. In the **Invoice units** field, add one
        or more invoice units.
     3. Complete the other fields to create a purchase order. For
        more information, see [Adding a purchase order](adding-po.md "adding-po.md").

   - When you're adding invoices to an existing purchase order
     1. Choose the **Purchase order ID** to
        edit.
     2. On the purchase order details page, choose **Edit
        purchase order**.
     3. In the **Invoice units** field, add one
        or more invoice units.
     4. Complete editing the purchase order. For more information,
        see [Editing your purchase orders](edit-po.md "edit-po.md").

###### Note

When you delete invoice units, you must delete the corresponding purchase
order association as well.

## Visualizing your costs in

AWS Cost Explorer

You can view your invoice unit costs in the AWS Cost Explorer service. For more information
about Cost Explorer, see [Analyzing your costs and
usage with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the _AWS Cost Management User Guide_.

###### To visualize your costs in

Cost Explorer

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Explorer**.
3. For **Date Range**, enter a time range.
4. Under **Group by**, choose
   `Cost categories`.
5. For **Cost category**, choose
   `aws:invoice:invoiceUnitName`.
6. Choose the invoice units to view the costs for.

###### Note

It can take up to 24 hours for Cost Explorer to show your invoice unit
information.
