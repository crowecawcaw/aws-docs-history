

# Marketplace Revenue Share

## How it works
<a name="raid-mrs-how-it-works"></a>

You set up each product once, then declare its Marketplace revenue share percentage for a start month and an optional end month. Add a new allocation whenever the percentage changes.
+ **Declare.** For each SaaS product, declare the share of the product's revenue that came through AWS Marketplace for the month.
+ **AWS calculates.** After the month processes, AWS takes the Marketplace share of the product's AWS Revenue Measurement attributed revenue you provide in Step 1 and distributes it across the product's Marketplace offers that were active that month, based on each offer's contract value and pay-as-you-go billing.
+ **Review.** On the 17th of the following month, review each offer's attributed revenue in the deal-level table of the Attributed Revenue dashboard in Partner Central. The deal-level table shows attribution for the components of your solution hosted in your own AWS accounts.

Override only if needed. Use the product's Revenue Attribution ID to override specific offers or to attribute revenue to co-sell opportunities.

**Note**  
If you accept the calculated amounts for all offers and have no opportunities to measure, you don't need a Revenue Attribution ID.

## Monthly timeline
<a name="raid-mrs-timeline"></a>


| Date | What happens | 
| --- | --- | 
| Through the 7th of the following month | You can change or end allocations that apply to that prior month, and enter or change cost allocation percentages. Your latest saved values are used. | 
| 8th | The prior month processes and becomes final. Only current and future months remain editable. | 
| 17th | Deal-level attributed revenue for the prior month is published to the Attributed Revenue dashboard — the same day as product-level attributed revenue. | 

## Additional capabilities
<a name="raid-mrs-capabilities"></a>
+ **Shared-infrastructure grouping.** If several of your products run on the same backend infrastructure, group them under one Marketplace Revenue Share and declare one percentage for the group. Implement AWS Revenue Measurement on the shared resources or accounts with the product code of any one product in the group; because the products are grouped, it doesn't matter which product code you choose. AWS attributes the group's revenue across the active Marketplace offers of all products in the group, based on each offer's monthly contract value and pay-as-you-go billing. A product can belong to only one group at a time.
+ **AWS deployed accounts (optional).** Optionally, you can specify AWS accounts where the grouped products are deployed. If you do not specify AWS deployed accounts for grouped products, AWS uses the revenue from all accounts where an AWS Revenue Measurement signal is detected as the base for that product's deal-level attribution calculation.
+ **Limited listings and subsidiary products.** Limited listings, and products you sell from another AWS Marketplace seller account connected through Subsidiary Account Connections, don't appear in the product dropdown. Add them manually by entering the Product ID or Product ARN (see [Product ID formats](#raid-mrs-product-id-formats)).
+ **Migration context.** Capture program and workload context on a Revenue Attribution ID so IDs created for an AWS migration engagement can be identified and reconciled to that engagement. Product and migration context captured when you create a Revenue Attribution ID is read-only and can't be changed afterward.

## Set up a Marketplace Revenue Share
<a name="raid-mrs-setup"></a>

**Step 1 – Declare your Marketplace Revenue Share**

1. Sign in to AWS Partner Central and open the Revenue attribution page.

1. On the Products and revenue shares tab, find your product. Limited listings and products in a seller account connected through Subsidiary Account Connections aren't listed; choose Add product and manually enter the Product ID or Product ARN (see [Product ID formats](#raid-mrs-product-id-formats)).

1. Select the product, choose View details, then choose Edit.

1. Choose Add new allocation. Enter the Marketplace revenue share percentage, the start month, and an optional end month.

1. (Optional) To group products that share backend infrastructure, choose Add new product. You can also list each product's AWS deployed accounts.

1. Choose Save changes. In the Attestation dialog, type confirm and choose Agree and save.

On first save, AWS assigns the Marketplace Revenue Share an ID (for example, `mrs-ab12cd34ef56g`), and the product status changes to Active. Allocations you can still change appear on the Active allocations tab; processed allocations move to the Processed allocations tab.

**Step 2 – Review deal-level attributed revenue**

On the 17th of the following month, open Partner Analytics > Attributed Revenue dashboard and go to the deal-level table. Filter by product and month, and review the attributed revenue of each offer. If the amounts are correct, no further action is needed.

**Step 3 – (Optional) Override offers or attribute opportunities**

On the Revenue attribution IDs tab, create a Revenue Attribution ID for the product, or edit its existing one. Add the offers you want to override and enter a monthly cost allocation percentage for each. Your override takes precedence, and AWS distributes the rest of the Marketplace share across the product's other offers.

ACE opportunities aren't transacted through AWS Marketplace, so AWS can't calculate their attributed revenue from the Marketplace Revenue Share. To attribute revenue to an opportunity, add it to the product's Revenue Attribution ID with a monthly cost allocation percentage. For detailed steps, see [Create and Edit Revenue Attribution IDs](raid-create-and-edit.md).

## Product ID Formats
<a name="raid-mrs-product-id-formats"></a>

When you manually add a product, enter either its Product ID or its Product ARN, exactly as shown in the AWS Marketplace Management Portal:
+ **Product ID (prod- format):** Used by most listings. Example: `prod-elvabmyn2yirl`
+ **Product ID (UUID format):** Used by some older listings that don't have a prod- Product ID. Example: `0c68b119-b122-4c7f-95e1-9e199b5163da`
+ **Product ARN:** The Amazon Resource Name of the AWS Marketplace product. Use the Product ARN, not another ARN (such as an offer, agreement, or resource ARN). Example: `arn:aws:awsmarketplace:us-east-1:038171331568:AWSMarketplace/SaaSProduct/prod-elvabmyn2yirl`