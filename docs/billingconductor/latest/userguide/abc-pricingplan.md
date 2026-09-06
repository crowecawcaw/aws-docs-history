

# Pricing plans
<a name="abc-pricingplan"></a>

You can use pricing plans in AWS Billing Conductor to customize the output of your billing details across your billing groups.

There are two types of pricing plans:
+ AWS managed Pricing Plan 
+ Customer managed Pricing Plan

AWS managed Pricing plans are read-only (cannot be edited or deleted), template pricing plans created by AWS. AWS supports the following managed pricing plans:
+ `BasicPricingPlan` - Calculates pro forma costs excluding non-public discount, and excludes credits, taxes, and support charges.
+ `Passthrough` - Passes the billable data, reflecting the AWS invoice, to billing group members. This option is only applicable to Billing Transfer billing groups.

**Note**  
Switching a billing group's pricing configuration to or from the Passthrough Pricing Plan results in updating the current month of cost data. For example, if the switch happens on May 15th, the data from May 1st onward will reflect the new pricing configuration.
Any existing Cost and Usage Reports (CURs) configuration will stop receiving new data after the pricing plan switch. Users need to create a new CUR configuration after the switch.

**Contents**
+ [One-level transfer example for Distribution Partners](#passthrough-one-level)
+ [Two-level transfer examples for Distribution Partners](#passthrough-two-level)
+ [Customer managed pricing plans](#customer-managed-pricingplan)
+ [Select an AWS managed pricing plan](select-pricingplan.md)
+ [Creating pricing plans](create-pricingplan.md)
+ [Viewing the pricing plan table](table-pricingplan.md)

## One-level transfer example for Distribution Partners
<a name="passthrough-one-level"></a>

The following example illustrates how the Passthrough Pricing Plan interacts in a one-level transfer scenario involving a Solution Provider and an End Customer.

Assume the End Customer's AWS invoice totals $98.

End-customer's primary view will show $98 of consumption, which is the same view that the Solution Provider will see in their account, across both 'My view' and 'Showback/Chargeback view'.

## Two-level transfer examples for Distribution Partners
<a name="passthrough-two-level"></a>

The following examples illustrate how the Passthrough Pricing Plan interacts in a two-level transfer scenario involving a Distributor, a Downstream Seller, and an End Customer.

Assume the End Customer's AWS invoice totals $98 and the Downstream Seller's Basic Pricing Plan calculates a pro forma cost of $100.

1. The Distributor applies the Passthrough Pricing Plan to the End Customer's AWS organization.

1. The Downstream Seller applies a Basic Pricing Plan (or Custom Pricing Plan) to the same End Customer's AWS organization.
+ Downstream Seller 'My view' – The Downstream Seller sees the End Customer's billable usage of $98, exactly as billed to the Distributor. This is because the Distributor's Passthrough Pricing Plan controls what the Downstream Seller sees for the End Customer's usage.
+ End Customer Primary view – The End Customer sees a pro forma cost of $100, based on the Downstream Seller's Basic or Custom Pricing Plan configuration. The End Customer's view depends exclusively on the Downstream Seller's pricing plan selection, not the Distributor's.

Assume the Distributor's Basic Pricing Plan calculates a pro forma cost of $100 for the End Customer's usage.

1. The Distributor applies a Basic Pricing Plan (or Custom Pricing Plan) to the End Customer's AWS organization.

1. The Downstream Seller applies the Passthrough Pricing Plan to the same End Customer's AWS organization.
+ Downstream Seller view – The Downstream Seller sees the End Customer's usage at the pro forma rate of $100, as determined by the Distributor's Basic or Custom Pricing Plan. The Downstream Seller's view depends on the Distributor's pricing plan selection.
+ End Customer view – The End Customer also sees the same pro forma cost of $100. Because the Downstream Seller selected the Passthrough Pricing Plan, the Distributor's rates flow through to the End Customer unchanged.

## Customer managed pricing plans
<a name="customer-managed-pricingplan"></a>

Customer managed pricing plans are customizable pricing plan controlled by the managed account. By default, a management account with admin permissions can create, update or delete pricing plans. It takes up to 24 hours after you apply a pricing plan to a billing group to see the custom rates for your billing group reﬂected.

A single pricing plan (AWS or customer managed) can be applied to multiple billing groups.

**Note**  
Updating a pricing plan also affects the billing details of each billing group, where the pricing plan is associated. If the pricing plan is associated with a billing group or set of billing groups, this change affects only the current billing period. Previous billing periods remain the same.