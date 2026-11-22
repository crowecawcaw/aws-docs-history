

# Revenue Attribution ID

A revenue attribution ID is a unique identifier that associates your AWS Marketplace offers and/or APN Customer Engagements (ACE) opportunities to a Marketplace product listing, allowing AWS to determine the AWS revenue generated from those offers and opportunities. Revenue attribution IDs build on top of product-level AWS Revenue Measurement. AWS Revenue Measurement is your foundation – it captures the total attributed revenue across your products and service delivery engagements. Revenue attribution is the deal-level overlay that maps that revenue to the specific offers and opportunities for which you request AWS deal-level incentives.

You can achieve deal-level attribution in two ways:


| Approach | Best for | What you provide | 
| --- | --- | --- | 
| Marketplace Revenue Share (automated) | SaaS products listed on AWS Marketplace | A Marketplace revenue share percentage for each product (or group of products that share infrastructure), for a start month and an optional end month. AWS calculates attributed revenue for each active Marketplace offer. | 
| Revenue Attribution ID (manual) | Co-sell opportunities, overrides of offer amounts calculated from a Marketplace Revenue Share, and products not covered by the Marketplace Revenue Share (for example, non-SaaS products) | Associations to offers and/or opportunities and a monthly cost allocation percentage for each. | 

Both approaches use Revenue Attribution IDs. With the Marketplace Revenue Share, AWS calculates offer-level attribution for you, and you create a Revenue Attribution ID only to override an offer or to attribute revenue to an ACE opportunity. With the manual approach, you associate each offer or opportunity with a Revenue Attribution ID and enter a monthly cost allocation percentage for each. If you associate multiple deals with one Revenue Attribution ID, AWS splits revenue proportionally based on the percentages you specify.

The Marketplace Revenue Share adds to — and does not replace — the existing Revenue Attribution ID experience. AWS does not create Revenue Attribution IDs for you, and your existing Revenue Attribution IDs continue to work unchanged.

## Key Concepts
<a name="raid-key-concepts"></a>

**Revenue Attribution ID:** A unique identifier created within AWS Partner Central that associates AWS revenue to one or more AWS Marketplace offers and/or ACE opportunities. You can use a revenue attribution ID in two ways:
+ **Deal-level overlay:** on your existing product-level AWS Revenue Measurement implementation — create a revenue attribution ID, associate your applicable AWS Marketplace offers and/or ACE opportunities and specify deal-level cost allocations. AWS maps your already-measured product revenue to those specific deals based on your inputs. No changes to your existing resource tags or user agent strings are required. Note that deal level revenue attribution remains internal to AWS.
+ **Standalone identifier:** used directly as a resource tag value or in a user agent string to associate AWS consumption to specific deals.

**Association:** The relationship between a Revenue Attribution ID and a Marketplace offer or ACE opportunity. Each association is configured by adding one or more monthly cost allocation entries – one per billing month for which the deal applies.

**Cost Allocation Percentage:** The portion of your product's product-level AWS Revenue Measurement attributed revenue that you assign to a specific offer or opportunity for a specific billing month. It's required for ACE opportunities, for overrides of calculated offer amounts, and for multi-tenant products that don't use the Marketplace Revenue Share (including partner-hosted components of hybrid deployments). For eligible products with a Marketplace Revenue Share, AWS calculates offer-level attribution automatically, so you don't need to enter a cost allocation percentage for every offer.

**Billing Month:** The calendar month for which the allocation applies. AWS attributes consumption attributed to your Revenue Attribution ID for that month according to the cost allocation percentages you specify.

**Marketplace Revenue Share:** An input you provide for an AWS Marketplace product, or for a group of products that share backend infrastructure. It declares what portion of the product's revenue came through AWS Marketplace as a go-to-market channel. AWS uses it to attribute your product-level AWS Revenue Measurement attributed revenue to your active Marketplace offers automatically. A Marketplace Revenue Share includes the product or products, any optional AWS deployed accounts, and its allocations. A product can belong to only one Marketplace Revenue Share at a time. On first save, AWS assigns it an ID (for example, `mrs-ab12cd34ef56g`). With the Marketplace Revenue Share, you create one Revenue Attribution ID per product — only when you need to override a calculated offer amount or attribute revenue to a co-sell opportunity — and reuse it every month.

**Marketplace revenue share percentage:** The percentage of a product's revenue that came through AWS Marketplace as a go-to-market channel in a given month (for example, 50% if half of the product's revenue came through Marketplace).

**Allocation:** A time-bound entry that sets a percentage. For a Marketplace Revenue Share, an allocation is the Marketplace revenue share percentage for a start month and an optional end month. For a Revenue Attribution ID, an allocation is the cost allocation percentage for one offer or opportunity for one billing month.

**Share status:** Active means an allocation is in effect for the current month or a future month. Action required means no allocation is in effect for the current month or any future month, either because none has been declared or because the last allocation has ended.

**Override:** A cost allocation percentage you enter for an offer on a Revenue Attribution ID. It replaces the attributed revenue AWS calculated for that offer from the Marketplace Revenue Share. AWS distributes the remaining Marketplace share across the product's other active offers.

**Attributed revenue:** The dollar amount AWS attributes to a product or deal for a month.

**Deal-level attributed revenue table:** The section of the Attributed Revenue dashboard in Partner Analytics that shows the attributed revenue of each offer and opportunity, for the components of your solution hosted in your own AWS accounts. Note your attributed revenue is based on the Marketplace Revenue Shares and Revenue Attribution IDs you provide.

**Important**  
No implementation rework is required for existing AWS Revenue Measurement-enabled products. If you already implemented AWS Revenue Measurement using an AWS Marketplace listing's product code as the tag value or in the user agent string, you do not need to change that implementation to use a Revenue Attribution ID.  
You can leverage this additional capability by creating a Revenue Attribution ID, associating it to the AWS Revenue Measurement-enabled product in Step 1 of the AWS Partner Central Revenue Attribution ID creation wizard, and providing your monthly deal-level cost allocation percentages in Step 2. Revenue Attribution IDs are designed to map product-level revenue to specific AWS Marketplace offers and/or ACE opportunities — eliminating rework.

## Prerequisites
<a name="raid-prerequisites"></a>

To create and use Revenue Attribution IDs, you must have:

1. Migrated to AWS Partner Central in the AWS Console

1. At least one AWS Marketplace product listing

1. A valid buyer account ID (for AWS Marketplace offer associations)

1. An opportunity in Launched stage with a customer AWS Account ID specified (for ACE opportunity associations)

1. Implemented at least one AWS Revenue Measurement method: AWS Marketplace Metering, Resource Tagging, User Agent String, Identity Tagging, or Account Tagging for SaaS products. Use your AWS Marketplace product listing's product code (product-level) or, for Resource Tagging and User Agent String, a Revenue Attribution ID as the unique identifier.

Partners with additional AWS Marketplace Seller Accounts that are connected via subsidiary account connections can create Revenue Attribution IDs for products that span multiple accounts.

### Additional prerequisites for the Marketplace Revenue Share
<a name="raid-mrs-prerequisites"></a>
+ A SaaS product listing on AWS Marketplace hosted in a partner owned account.
+ Product-level AWS Revenue Measurement implemented with your listing's product code (for example, `aws-apn-id-{{partner-central-aws-account-id}} = pc:{{product code}}`).
+ Your AWS Marketplace seller account linked to your AWS Partner Central account. Connect any additional seller accounts through Subsidiary Account Connections.