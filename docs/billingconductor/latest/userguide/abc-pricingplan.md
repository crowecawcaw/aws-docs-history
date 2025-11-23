# Pricing plans

You can use pricing plans in AWS Billing Conductor to customize the output of your billing details across
your billing groups.

There are two types of pricing plans:

- AWS managed Pricing Plan
- Customer managed Pricing Plan
  AWS managed Pricing plans are read-only (cannot be edited or deleted), template pricing plans created by AWS.
  AWS supports the `BasicPricingPlan` as a managed pricing plan. This is plan calculates pro forma costs pre-discounts, and exclude credits, taxes and support charges.

Customer managed pricing plans are customizable pricing plan controlled by the managed account. By default, a management account with admin permissions can create, update or delete pricing plans. It takes up to 24 hours after you apply a pricing plan to a billing group to see the custom rates for your billing group reﬂected.

A single pricing plan (AWS or customer managed) can be applied to multiple billing groups.

###### Note

Updating a pricing plan also affects the billing details of each billing group, where the
pricing plan is associated. If the pricing plan is associated with a billing group or set of
billing groups, this change affects only the current billing period. Previous billing
periods remain the same.

###### Contents

- [Select an AWS managed pricing plan](select-pricingplan.md "select-pricingplan.md")
- [Creating pricing plans](create-pricingplan.md "create-pricingplan.md")
- [Viewing the pricing plan table](table-pricingplan.md "table-pricingplan.md")
