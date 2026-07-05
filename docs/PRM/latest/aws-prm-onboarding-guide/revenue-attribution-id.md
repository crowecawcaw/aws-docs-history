# Revenue Attribution ID

A revenue attribution ID is a unique identifier that associates your AWS Marketplace
offers and/or APN Customer Engagements (ACE) opportunities to a Marketplace product listing
allowing AWS to determine the AWS revenue generated from those offers and opportunities.
Revenue attribution builds on top of product-level Partner Revenue Measurement (PRM)
implementation. PRM is your foundation — capturing total attributed revenue across your products
or service delivery engagements. Revenue attribution is your deal-level overlay — assisting
AWS in mapping revenue to specific offers and opportunities for which you are requesting
AWS deal-level incentives.

After a revenue attribution ID is created, one or more AWS Marketplace offers or ACE
opportunities can be associated with it. For each associated deal, you can specify the cost
allocation percentage on a month-by-month basis. If you associate multiple offers or
opportunities to one revenue attribution ID, AWS splits revenue proportionally based on the
cost allocation percentages you specify.

## Key Concepts

**Revenue Attribution ID:** A unique identifier created within
that associates AWS revenue to one or more Marketplace offers and/or ACE
opportunities. You can use a revenue attribution ID in two ways:

- **Deal-level overlay:** on your existing product-level PRM
  implementation — create a revenue attribution ID, associate your applicable Marketplace offers
  and/or ACE opportunities and specify deal-level cost allocations. AWS maps your
  already-measured product revenue to those specific deals based on your inputs. No changes to
  your existing resource tags or user agent strings are required. Note that deal level revenue
  attribution remains internal to AWS.
- **Standalone identifier:** used directly as a resource tag
  value or in a user agent string to associate AWS consumption to specific deals.

**Association:** The relationship between a Revenue
Attribution ID and a Marketplace offer or ACE opportunity. Each association is configured by
adding one or more monthly cost allocation entries — one per billing month for which the deal
applies.

**Cost Allocation Percentage:** The portion of your product's
total AWS consumption that is attributable to a specific deal for a specific billing month.
Note that this input is required for multi-tenant SaaS products, including partner-hosted
components for hybrid deployments, where customers share infrastructure within partner's
accounts.

**Billing Month:** The calendar month for which the cost
allocation percentage entry applies. AWS attributes consumption attributed to your Revenue
Attribution ID for that month according to the cost allocation percentages you specify.

###### Important

No implementation rework is required for existing PRM-enabled products. If you already
implemented PRM using an AWS Marketplace listing's product code as the tag value or in the
user agent string, you do not need to change that implementation to use a Revenue Attribution
ID.

You can leverage this additional capability by creating a Revenue Attribution ID,
associating it to the PRM-enabled product in Step 1 of the Revenue Attribution ID
creation wizard, and providing your monthly deal-level cost allocation percentages in Step 2.
Revenue Attribution IDs are designed to map product-level revenue to specific AWS Marketplace
offers and/or ACE opportunities — eliminating rework.

## Prerequisites

To create and use Revenue Attribution IDs, you must have:

1. Migrated to in the AWS Console
2. At least one AWS Marketplace product listing
3. A valid buyer account ID (for AWS Marketplace offer associations)
4. An opportunity in Launched stage with a customer AWS Account ID specified (for ACE
   opportunity associations)
5. Implemented at least one Partner Revenue Measurement capability — Resource Tagging or
   User Agent String — using either your AWS Marketplace product listing's product code
   (product-level PRM) or a Revenue Attribution ID as the unique identifier.

Partners with additional AWS Marketplace Seller Accounts that are connected via
subsidiary account connections can create Revenue Attribution IDs for products that span
multiple accounts.
