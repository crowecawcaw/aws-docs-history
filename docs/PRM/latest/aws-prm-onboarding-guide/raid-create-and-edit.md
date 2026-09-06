

# Create and Edit Revenue Attribution IDs
<a name="raid-create-and-edit"></a>

This section covers how to create a Revenue Attribution ID, add and edit monthly cost allocation percentages, and implement PRM using the Revenue Attribution ID as the unique identifier.

## Creating a Revenue Attribution ID
<a name="raid-creating"></a>

The Revenue Attribution ID creation flow guides you through three steps. To get started, navigate to the [Revenue attribution](https://us-east-1.console.aws.amazon.com/partnercentral/revenue-attr?region=us-east-1) under Sell menu in AWS Partner Central Console.

### Step 1: Select your AWS Marketplace Product
<a name="raid-step1"></a>

On this page, select the AWS Marketplace product you want to associate with the Revenue Attribution ID. Only your AWS Marketplace products are eligible for selection. The product code from the selected listing is automatically associated with the Revenue Attribution ID.

If you want to associate a product owned by a subsidiary AWS account that is not directly available in the dropdown, you can manually enter the Marketplace product ID within the wizard.

Alternatively, if multiple AWS Marketplace products share the same underlying AWS resources — for example, a single deployment that spans more than one AWS Marketplace product listing — you can proceed without selecting a specific product. In this case, attribution applies across all consumption measured under the Revenue Attribution ID, regardless of which product you purchased.

### Step 2: Associate offers or opportunities
<a name="raid-step2"></a>

On this page, you associate your Revenue Attribution ID with the AWS Marketplace offers and/or ACE opportunities and provide cost allocation percentages on a month-by-month basis.

Each entry includes the following information:
+ **Offer ID or Opportunity ID:** The unique identifier of the deal you are associating. If an AWS Marketplace offer is already linked to an ACE opportunity, you only need to provide the Offer ID — AWS automatically attributes revenue to the associated opportunity.
+ **Name:** A descriptive name for the associated entry to help you identify it in your dashboard.
+ **Customer AWS Account ID:** The AWS account where the customer consumes your product. Required for multi-tenant SaaS products.
+ **Billing Month:** The calendar month (for example, April 2026) for which the cost allocation percentage applies.
+ **Cost Allocation %:** The portion of your product's total AWS consumption attributable to this deal for the specified billing month. Required for multi-tenant SaaS deployments and for any case where two or more deal associations are concurrently active in the same billing month.

To cover a deal that spans multiple billing months, add one entry per month. Each (Offer ID or Opportunity ID, Billing Month) combination is a separate entry. This per-month design allows you to adjust cost allocation percentages as deal economics change and ensures the prior month's allocation matches actual measured consumption.

The total Cost Allocation % across all entries for a given Revenue Attribution ID and the same Billing Month must not exceed 100%.

### Step 3: Review and Submit
<a name="raid-step3"></a>

Review your Revenue Attribution ID name, associated Marketplace product, offers and opportunities, and the specified monthly cost allocation percentages. Submit to create the Revenue Attribution ID.

## Adding and editing monthly cost allocation percentages
<a name="raid-adding-editing-allocations"></a>

Cost allocation entries are managed per billing month. You can:
+ **Add a new monthly entry** for a current or future billing month at any time.
+ **Update a monthly entry** for the current or a future billing month at any time.
+ **Update last month's entry** until the 7th of the current month. This window gives you time to review actual usage in AWS Cost Explorer before finalizing the prior month's allocation.

After the 7th of the current month, attribution for the prior billing month can no longer be modified. Updates to a current or future month's entry apply from the next monthly billing cycle. Historical attribution for prior months is not retroactively recalculated.