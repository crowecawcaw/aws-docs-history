# Creating a percentage charge custom line item

Use the following steps to create a custom line item that applies either a credit or fee line item to an individual billing group.

###### To create a custom line item

1. Open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Custom line items**.
3. Choose **Create custom line item**.
4. For **Custom line item details**, enter the name of the custom line item. For naming restrictions, see [Quotas and restrictions](limits.md "limits.md").
5. For **Description**, enter a description for the custom line item. The character limit is 255.
6. For **Billing period**, choose either the existing billing period or the previous billing period.
7. For **Duration**, choose either one month or recurring (no defined end date).
8. For **Billing group**, choose a billing group. You can only associate the custom charge to one billing group at a time.
   1. (Optional) For **Allocated account**, you can apply your custom line item to a billing group account of your choice. Your custom line item is applied to the primary account of the billing group of your choice by default.

9. Choose **percentage charge** for your **custom line item type**.
10. Choose a **charge type** and enter an input amount.

A discount line item adds a credit. This reduces the amount that's charged to the
selected billing group. A markup line item adds a charge. This increases the amount
that's charged to the selected billing group. All custom line items are in USD. 11. (Optional) For **Reference values**, choose the values to include in the
calculation. By default, the billing group total cost is selected as a resource. This excludes
all flat custom line items.

    1. (Optional) By default, Savings Plans discounts are included. To exclude them from the
     calculation, select the **Exclude Savings Plans discounts** check
     box.
    2. (Optional) If you want a specific service charges to be executed by the custom line item, select **Choose the custom values using filters** and input the service code under **Value** section.

12. (Optional) Include one of more flat custom line item. Choose each applicable flat custom line item from the table that you want included in the percentage-based calculation.

###### Note

You can create percentage custom line items with no associated resources. These custom line
items show a `$0.00` value in your billing data. 13. For **Display settings**

    1. You can choose a service that you want the percentage custom line item present in the bills. The default value is `AWSBillingConductor`.
    2. Or you can select **Itemized** to have the custom line item displayed next to each applicable line item.

14. Choose **Create**.
