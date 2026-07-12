The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with your Revenue Attribution IDs

A Revenue Attribution ID is a deal-level identifier that maps your AWS Marketplace
product revenue to specific AWS Marketplace Offers and/or AWS Partner Central Opportunities. It
builds on top of product-level Partner Revenue Measurement (PRM) implementation: PRM
captures total attributed revenue for a Marketplace product, and a Revenue Attribution ID
maps that revenue to specific deals according to the monthly cost allocation percentages
you specify.

The Revenue Attribution Service exposes APIs to create, retrieve, list, and update
Revenue Attribution IDs and to manage their monthly cost allocation entries
asynchronously.

## What is a Revenue Attribution ID?

A Revenue Attribution ID has two layers:

- **The attribution** a partner-named,
  partner-described resource identified by an `ra-` prefix ID (for example,
  `ra-aabbccddee001`) and an ARN. Each attribution is scoped to a
  `Catalog` (`AWS` for production, `Sandbox` for
  testing) and the partner's account.
- **One or more monthly cost allocation entries** each
  entry maps a single (Offer ID or Opportunity ID, Billing Month) combination to a
  cost-allocation percentage. Entries are managed in batches asynchronously through an
  allocation task pattern.

A Revenue Attribution ID can be used in two ways:

- **As a deal-level overlay** on your existing
  product-level PRM implementation. Create a Revenue Attribution ID, associate your
  applicable Marketplace Offers and/or ACE Opportunities, and AWS maps your
  already-measured product revenue to those specific deals — no changes to your existing
  resource tags or user agent strings are required.
- **As a standalone identifier** used directly as a
  resource-tag value (`aws-apn-id` = `<RA ID>`) or in a
  user-agent string (`APN_1.1/pc_<RA ID>$`) to attribute AWS
  consumption to a specific deal from the start.

## Working with your Revenue Attribution IDs

Partners can manage Revenue Attribution IDs and their monthly cost allocation entries
through the Revenue Attribution Service. The lifecycle progresses through two independent
flows: the attribution-record flow (create, update, retrieve, list) and the allocations
flow (start a batch task, poll for results, retrieve individual entries, list entries for
an attribution).

### Creating a Revenue Attribution ID

The first step is creating a Revenue Attribution ID using the
`CreateRevenueAttribution` API action. The returned `Id` and
`Arn` can be used immediately as a resource-tag value or in a user-agent
string to attribute AWS consumption.

When creating a Revenue Attribution ID, partners must provide:

- **`Catalog`** — `AWS` for
  production or `Sandbox` for testing.
- **`Name`** — a human-readable name for
  the attribution. Must be unique within the Catalog and the partner's account.
  Maximum 128 characters.

Partners can optionally provide:

- **`Description`** — free-text description
  of the attribution. Maximum 1024 characters.
- **`MarketplaceProduct`** — the AWS
  Marketplace product to associate with this attribution. Provide
  `ProductIdentifier` (the 25-character Marketplace product ID) and
  `TenancyModel` (`MULTI_TENANT` or
  `SINGLE_TENANT`). If omitted at creation, attribution applies across all
  consumption measured under the Revenue Attribution ID, regardless of which
  Marketplace product the customer purchased — useful when a single deployment spans
  more than one Marketplace listing.
- **`Tags`** — up to 200 key-value pairs
  for resource organization. Tag keys must be unique within the request.

Best Practice: Provide `MarketplaceProduct.ProductIdentifier` whenever
your deal is anchored to a specific Marketplace listing. This enables AWS to validate
that the product is owned by the calling partner account or by a subsidiary account
connected via Partner Account Connection (PAC), and surfaces the resolved
`ProductCode` and `ProductType` (for example, `SaaS`,
`AMI`, `ML`) in the response. If the product is not owned by an
authorized account, the API returns `ValidationException` with reason
`PRODUCT_NOT_FOUND_OR_NOT_OWNED`.

The response returns the new `Id` (format
`ra-[a-z0-9]{13}`), `Arn`, resolved
`MarketplaceProduct` attributes, and the initial `Version` number
(which starts at 1 and increments on each subsequent update).

### Adding monthly cost allocation entries

Once a Revenue Attribution ID is created, partners associate AWS Marketplace Offers
and/or ACE Opportunities to it by submitting a batch of monthly cost allocation entries
through the `StartRevenueAttributionAllocationsTask` API action. This is an
asynchronous operation that accepts up to 250 allocation changes (`CREATE`
and/or `UPDATE`) per task.

Each allocation entry specifies:

- **Offer ID or Opportunity ID** — the unique
  identifier of the deal being associated. If a Marketplace Offer is already linked to
  an ACE Opportunity, partners only need to provide the Offer ID; AWS automatically
  attributes revenue to the linked Opportunity.
- **Billing Month** — the calendar month for which
  the cost allocation applies (for example, `2026-04`).
- **Cost Allocation %** — the portion of the
  product's total AWS consumption attributable to this deal in this billing month.
  Required for multi-tenant SaaS products, including partner-hosted components for
  hybrid deployments, where customers share infrastructure.
- **Customer AWS Account ID** — the AWS account
  of the customer that consumes the product. Required for multi-tenant SaaS
  products.

The total Cost Allocation % across all allocation entries for a given Revenue
Attribution ID and the same Billing Month must not exceed 100%. If the total exceeds
100%, the offending entry is rejected during async business validation with a per-record
error code.

Synchronous validation: `StartRevenueAttributionAllocationsTask` performs
basic shape validation synchronously (field types, patterns, batch size). If the basic
validation passes, the API returns a `TaskId` with status
`IN_PROGRESS`. Business validation (cap checks, immutability rules,
dependency lookups against Marketplace and ACE) runs asynchronously and the per-record
results are discovered through
`GetRevenueAttributionAllocationsTask`.

To monitor a submitted task, partners poll
`GetRevenueAttributionAllocationsTask` with the Revenue Attribution Resource Id or ARN. The response progresses from `IN_PROGRESS` to
`COMPLETED` (regardless of whether individual records succeeded or failed)
and returns:

- **`TaskStatus`** —
  `IN_PROGRESS`, `COMPLETED`, or `FAILED` (top-level
  task failure).
- **`RecordResults`** — for each input
  record: the assigned `AllocationId` (if successful), the per-record
  status (`SUCCEEDED` or `FAILED`), and a structured error code
  and message if the record failed.

Partners should retrieve task results promptly. After the task completes, the
per-record outcomes can be reconciled and any failed entries can be corrected and
resubmitted in a new task.

### Editing monthly cost allocation entries

Cost allocation entries are managed per billing month with these rules:

- Partners can **add a new monthly entry** for the
  current or any future billing month at any time.
- Partners can **update a monthly entry** for the
  current or any future billing month at any time.
- Partners can **update last month's entry** until
  the **7th of the current month**. This window allows
  partners to review actual usage in AWS Cost Explorer before finalizing the prior
  month's allocation.

After the 7th of the current month, attribution for the prior billing month can no
longer be modified. Updates to a current or future month's entry apply from the next
monthly billing cycle. Historical attribution for prior months is not retroactively
recalculated.

Updates to allocation entries are submitted through the same
`StartRevenueAttributionAllocationsTask` API action with
`Operation` set to `UPDATE` for each affected entry. The async
task pattern handles updates and creations uniformly.

### Updating a Revenue Attribution ID

Partners can update the `Description` of an existing Revenue Attribution
ID using the `UpdateRevenueAttribution` API action. The attribution record
itself is otherwise immutable — `Name`, `MarketplaceProduct`, and
tag-on-create values cannot be changed after creation. To re-tag the resource, use the
standard AWS tagging operations on the attribution's ARN.

When updating a Revenue Attribution ID, partners must provide:

- **`Catalog`** — `AWS` or
  `Sandbox`.
- **`Identifier`** — the `ra-`
  ID of the attribution to update.
- **`Version`** — the current version of
  the attribution for optimistic locking.

Partners can optionally provide:

- **`Description`** — the updated free-text
  description. Maximum 1024 characters.
- **`ClientToken`** — an idempotency token
  for the update.

Optimistic Locking: The `Version` field ensures updates apply only if the
attribution hasn't changed since it was last retrieved. If the submitted
`Version` doesn't match the current resource version, the update is rejected
with `ConflictException` and a message including the submitted and current
version numbers. Best practice is to retrieve the latest version with
`GetRevenueAttribution` before each update.

### Viewing Revenue Attribution ID details

Partners can retrieve complete information for a single Revenue Attribution ID using
the `GetRevenueAttribution` API action. This returns:

Resource Metadata:

- Unique identifier (`Id`) and Amazon Resource Name
  (`Arn`).
- The `Catalog` in which the attribution exists.
- `Name` and `Description`.
- The retrieved `Version` and the `LatestVersion` (use the
  latest for subsequent updates).

Marketplace Product Attributes (if `MarketplaceProduct` was set at
creation):

- `ProductId` — the Marketplace product ID provided by the
  partner.
- `ProductCode` — the AWS Marketplace product code resolved from
  `ProductId`.
- `ProductType` — `SaaS`, `AMI`,
  `Container`, `ML`, `Data`, or
  `Professional Services`.
- `TenancyModel` — `MULTI_TENANT` or
  `SINGLE_TENANT`.

Audit Information:

- `CreatedDate` and `LastModifiedDate`.

Partners can optionally provide a specific `Version` in the request to
retrieve a historical version of the attribution. Omit `Version` to return
the latest.

To retrieve a specific monthly cost allocation entry, partners use the
`GetRevenueAttributionAllocation` API action with the entry's
`AllocationId`. This returns the Offer ID or Opportunity ID, Billing Month,
Cost Allocation %, Customer AWS Account ID, and the entry's status and audit
information.

### Listing Revenue Attribution IDs

Partners can view all Revenue Attribution IDs in their account using the
`ListRevenueAttributions` API action. This returns a paginated list of
attribution summaries with filtering and sorting capabilities.

Partners can filter results by:

- **`Catalog`** — `AWS` or
  `Sandbox` (required).
- **`Identifiers`** — a list of up to 100
  specific `ra-` IDs to retrieve.
- **`CreatedAfter` /
  `CreatedBefore`** — filter by creation timestamp range
  (inclusive).

Partners can configure result sorting using the `Sort`
parameter:

- `SortBy` — `CreatedDate` or
  `LastModifiedDate`.
- `SortOrder` — `ASCENDING` or
  `DESCENDING`.

The response includes a summary for each attribution: `Arn`,
`Id`, `Catalog`, `Name`, resolved
`MarketplaceProduct` attributes, `CreatedDate`,
`LastModifiedDate`, the latest `Version`, and
`TotalRevenueAttributionAssociationCount` (the number of active monthly cost
allocation entries linked to the attribution).

Use `MaxResults` (default 25, maximum 100) and `NextToken` to
paginate through large result sets. The response includes a `NextToken` if
additional pages are available.

### Listing monthly cost allocation entries

Partners can list the monthly cost allocation entries for a specific Revenue
Attribution ID using the `ListRevenueAttributionAllocations` API action. This
returns a paginated list of allocation summaries with filtering capabilities.

Partners can filter results by:

- **`MarketplaceOfferId`** — list only
  entries associated with a specific Marketplace Offer.
- **`AwsPartnerCentralOpportunityId`** —
  list only entries associated with a specific Partner Central Opportunity.
- **`BillingMonth`** — list only entries
  for a specific calendar month.

The response includes summary information for each entry: the
`AllocationId`, the associated Offer ID or Opportunity ID, the Customer
AWS Account ID, the Billing Month, the Cost Allocation %, the entry's name and
status, and audit timestamps.

Dashboard Building: The combination of `ListRevenueAttributions` and
`ListRevenueAttributionAllocations` is designed to support partner dashboard
creation. Partners can build views such as:

- All Revenue Attribution IDs created in the last 30 days, sorted by creation
  date.
- All monthly cost allocation entries for a specific Marketplace Offer across
  multiple Revenue Attribution IDs.
- All cost allocation entries for the current billing month, to validate that
  totals do not exceed 100% per attribution.
- All Revenue Attribution IDs that have at least one active allocation entry
  (`TotalRevenueAttributionAssociationCount > 0`).
