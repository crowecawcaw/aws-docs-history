

# Pricing rules
<a name="create-pricingrule"></a>

You can create pricing rules in AWS Billing Conductor to customize your billing rates across your billing groups. Pricing rules can be global, service-specific, billing entity-specific, or SKU-specific in scope. You can use pricing rules to apply a discount or markup for each respective scope. Scopes don't overlap. When pricing rules with different scopes are contained within a single pricing plan, scopes are applied from most to least granular.

For global and service pricing rules, you can also choose to deactivate or activate Always Free Tier rates. Pricing rules with [Always Free Tier](https://aws.amazon.com/free/) deactivated default to the first paid tier for the usage type or operation.

By default, a payer account with admin permissions can create pricing rules. It takes up to 24 hours after you apply a pricing rule to a billing group to see the custom rates for your billing group reflected.

For SKU-scoped pricing rules, you can customize rates and usage tiering ranges. The custom rate replaces the AWS public On-Demand rate for that specific SKU (a service, usage type, and operation combination). If the SKU has multiple usage tiers, you can customize the usage ranges and the rate for each tier. This is useful if you've negotiated a flat rate or custom rate structure with your customer. It lets your pro forma bill reflect that rate directly. A SKU-scoped custom rate rule takes precedence over broader-scope markup or discount rules for that SKU. You can have only one pricing rule per SKU.

**Note**  
Custom rates apply to On-Demand usage only. They don't affect Reserved Instance and AWS Savings Plans purchases.

A single pricing plan can be applied to multiple billing groups.

**Contents**
+ [Creating pricing rules](create-pricingrule-abc.md)
+ [Viewing the pricing rule table](table-pricingrule.md)