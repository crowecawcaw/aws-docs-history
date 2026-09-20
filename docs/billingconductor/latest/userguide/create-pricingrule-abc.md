

# Creating pricing rules
<a name="create-pricingrule-abc"></a>

Use the following steps to create a pricing rule.

**To create a pricing rule**

1. Open AWS Billing Conductor at [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/).

1. In the navigation pane, choose **Pricing configuration**.

1. Choose the **Pricing rules** tab.

1. Choose **Create pricing rules**.

1. For **Pricing rule details**, enter the name of the pricing rule. For naming restrictions, see [Quotas and restrictions](limits.md).

1. (Optional) For **Description**, enter a description for the pricing rule.

1. For **Scope**, choose `Global`, `Service`, `Billing entity`, or `SKU`.
   + Global - applies to all usage.
   + Service - only applies to a given service. When choosing service, choose a service code to configure the pricing rates for. When you choose a service, choose the service code from the Price List Query API that you want to adjust.
   + Billing entity - only applies to a given billing entity. A billing entity is the seller of services provided by AWS, their affiliates, or third-party providers selling services through AWS Marketplace.
   + SKU - only applies to the unique combination of service (product) code, usage type, and/or operation.

1. For **Type**, choose one of the following types. The available types depend on the scope you chose:
   + **Discount** - apply a percentage-based discount. This type is available for all scopes.
   + **Markup** - apply a percentage-based markup. This type is available for all scopes.
   + **Free Tier settings** - turn the AWS Free Tier on or off for your billing group usage. This type is available for global and service scopes.
   + **Custom** - set your own rates and usage tier ranges for a specific SKU. This type is available for the SKU scope only.

1. Complete the configuration for the type you chose.
   + For **Discount** or **Markup**, enter the **Percentage** amount.

     If you enter **0** as the percentage, the pricing plan defaults to the AWS On-Demand rate. If you enter a decimal value, it will be rounded to the nearest 2 decimal places.
**Note**  
The percentage displays on the member account's bills page. For example, `EC2 t3.micro on-demand (+20%)`.
   + For **Free Tier settings**, use the **Free Tier** toggle to turn the Always Free Tier on or off. Always Free Tier is on unless you explicitly turn it off. When it's off, rates default to the first paid tier for the usage type or operation.
   + For **Custom**, complete the **Rate configuration** table to set your own rates for the SKU:
     + The **Rate configuration** table is pre-populated from the AWS On-Demand pricing for the selected SKU. It has three columns: **From** and **To** define the usage range, and **Rate value** is the rate for that range.
     + In the **Rate value** column, set the rate for each range directly instead of entering a percentage. Rate values support up to 10 decimal places and can't exceed twice the highest On-Demand rate for the SKU.
     + If the SKU supports On-Demand pricing by usage tiers, you can customize the **From** and **To** breakpoints and the **Rate value** for each tier. You can also change the number of tiers by adding or removing ranges. The number of ranges can't exceed the original number of On-Demand pricing tiers for the SKU. Ranges must be contiguous. Each range's **To** value must match the next range's **From** value. The first range always starts at 0, and the last range has no upper bound.
     + To discard your changes and restore the original On-Demand ranges and rates, choose **Reset to On-Demand rates**.
**Note**  
Custom rates apply to On-Demand usage only. They don't affect Reserved Instance and AWS Savings Plans purchases.

1. (Optional) To create another pricing rule in the same workflow, choose **Add pricing rule**.

1. Choose **Create pricing rule**.