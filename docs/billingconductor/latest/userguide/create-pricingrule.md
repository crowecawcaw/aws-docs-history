# Pricing rules

You can create pricing rules in AWS Billing Conductor to customize your billing rates across your billing

groups. Pricing rules can be global, service-specific, billing entity-specific, or SKU-specific in scope. You can use pricing rules to apply a discount or markup for each respective scope. Scopes don't overlap. Scopes are applied from most to least granular when pricing rules with different scopes are contained within a single pricing plan. For global pricing rules, you can also choose to deactivate or active `Always Free Tier` rates. Pricing rules with [Always Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") deactivated defaults to the first paid tier for the usage type or operation. By default, a payer account in
with admin permissions can create pricing rules. It takes up to 24 hours after you apply a
pricing rule to a billing group to see the custom rates for your billing group reflected.

A single pricing plan can be applied to multiple billing groups.

###### Contents

- [Creating pricing rules](create-pricingrule-abc.md "create-pricingrule-abc.md")
- [Viewing the pricing rule table](table-pricingrule.md "table-pricingrule.md")
