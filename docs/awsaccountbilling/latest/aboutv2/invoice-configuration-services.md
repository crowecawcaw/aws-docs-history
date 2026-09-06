

# Using AWS invoice configuration with other services
<a name="invoice-configuration-services"></a>

Once you create an invoice unit, you can use AWS invoice configuration with other Billing and Cost Management services.

## Associating purchase orders to invoice units
<a name="invoice-configuration-services-po"></a>

You have the option to associate a purchase order to one or more invoice units.

**To associate purchase orders**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Purchase orders**.

1. Add invoice units using the following steps:
   + When creating a new purchase order

     1. Choose **Add purchase order** to create a purchase order.

     1. In the **Invoice units** field, add one or more invoice units.

     1. Complete the other fields to create a purchase order. For more information, see [Adding a purchase order](adding-po.md).
   + When you're adding invoices to an existing purchase order

     1. Choose the **Purchase order ID** to edit.

     1. On the purchase order details page, choose **Edit purchase order**.

     1. In the **Invoice units** field, add one or more invoice units.

     1. Complete editing the purchase order. For more information, see [Editing your purchase orders](edit-po.md).

**Note**  
When you delete invoice units, you must delete the corresponding purchase order association as well.

## Visualizing your costs in AWS Cost Explorer
<a name="invoice-configuration-services-ce"></a>

You can view your invoice unit costs in the AWS Cost Explorer service. For more information about Cost Explorer, see [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) in the *AWS Cost Management User Guide*.

**To visualize your costs in Cost Explorer**

1. Open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Cost Explorer**.

1. For **Date Range**, enter a time range.

1. Under **Group by**, choose `Cost categories`.

1. For **Cost category**, choose `aws:invoice:invoiceUnitName`.

1. Choose the invoice units to view the costs for.

**Note**  
It can take up to 24 hours for Cost Explorer to show your invoice unit information.