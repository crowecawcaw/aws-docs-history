

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with your Marketplace Revenue Shares

A Marketplace Revenue Share is an input for an AWS Marketplace product that declares, as a monthly percentage, the portion of the product's revenue that AWS Marketplace drives as a sales channel. AWS uses this input to correlate a partner's Marketplace-collected revenue against deal-level revenue signals.

Partners with other AWS Marketplace products that run on the same backend AWS infrastructure can add those products to the same Marketplace Revenue Share. All products in a Marketplace Revenue Share use the same monthly allocations.

Marketplace Revenue Share APIs let partners create, retrieve, update, and list Marketplace Revenue Shares, and manage their monthly allocations. Marketplace Revenue Shares also support standard AWS tagging operations.

## What is a Marketplace Revenue Share?
<a name="what-is-a-marketplace-revenue-share"></a>

A Marketplace Revenue Share has two layers:
+ **The Revenue share** — an input for an AWS Marketplace product, identified by its own ID (`mrs-` followed by 13 characters, for example `mrs-0a1b2c3d4e5f6`) and its ARN. Optionally, partners can add other products that run on the same backend AWS infrastructure, up to 25 products in total. A product can be in only one open share at a time.
+ **One or more allocations** — each allocation declares a `RevenueSharePercent` for one calendar month, and applies equally to every product in the share. A share can have many allocations over time, but at most one `ACTIVE` allocation for any given month.

For each product, partners can optionally provide typed lists of AWS account IDs:
+ **`DEPLOYMENT`** — AWS deployed accounts, the AWS accounts into which the product is deployed. Up to 1,000 accounts per product.
+ **`ORGANIZATION`** — AWS Organization accounts associated with the product. Up to 100 accounts per product. This account type is available only through the API, and AWS doesn't currently use these accounts in revenue calculations.

If partners omit `Accounts` for a product, AWS determines the accounts for that product. When partners provide account IDs, AWS validates the 12-digit format on request and validates account ownership afterward.

Allocations have these key properties:
+ **Month** — an allocation covers exactly one calendar month. `EffectiveFrom` is the first day of the month, and `EffectiveUntil` is the last day of the same month.
+ **Status** — `ACTIVE` or `INACTIVE`. On creation, the status is `ACTIVE`. Only `ACTIVE` allocations participate in revenue calculations.
+ **One active allocation per month** — within a share, a month can have at most one `ACTIVE` allocation. To replace it, partners update that allocation, or set it to `INACTIVE` before creating a new one.
+ **Edit window** — partners can create, change, or deactivate the allocation for a month until the end of the 7th day of the following month (UTC). After that, the month is finalized.

## Working with your Marketplace Revenue Shares
<a name="managing-marketplace-revenue-shares"></a>

Partners manage Marketplace Revenue Shares and their allocations through the AWS Partner Central API. The lifecycle progresses through two flows: the share flow (create, retrieve, update, list, tag) and the allocations flow (create, update, retrieve, list).

Every operation on an existing share accepts either the share ID (`mrs-`…) or the share ARN as the identifier.

### Creating a Marketplace Revenue Share
<a name="creating-a-marketplace-revenue-share"></a>

The first step is creating a Marketplace Revenue Share for an AWS Marketplace product using the `CreateMarketplaceRevenueShare` API action. To group additional products that run on the same backend AWS infrastructure, partners include them in the same request, or add them later with `UpdateMarketplaceRevenueShare`.

When creating a Marketplace Revenue Share, partners must provide:
+ **`Catalog`** — `AWS` for production or `Sandbox` for testing.
+ **`Products`** — the product, plus any additional products that run on the same backend AWS infrastructure (1 to 25 entries). Each entry has:
  + **`ProductId`** (required) — the AWS Marketplace product ID (for example, `prod-abc123def4567`) or the product ARN. The service stores and returns the product ID.
  + **`Accounts`** (optional) — at most one entry per account type. Each entry has an `AccountType` (`DEPLOYMENT` or `ORGANIZATION`) and a non-empty list of `AccountIds`.

Partners can optionally provide:
+ **`Tags`** — up to 200 key-value pairs for organizing resources at creation time. Use `TagResource` to add tags after creation.
+ **`ClientToken`** — an idempotency token that prevents duplicate creations on retry. Maximum 64 characters. AWS SDKs generate this token automatically.

Product Validation: On creation, the service verifies with AWS Marketplace that:
+ each product is owned by the caller's account or by a subsidiary account connected to the caller through Partner Account Connection;
+ each product is a `SaaS` product in Public or Limited status;
+ each product is not already in another open share.

A request that fails any of these checks returns `ValidationException` with the reason `BUSINESS_VALIDATION_FAILED` and a message that names the product. For example: "Product prod-abc123def4567 is already in another marketplace revenue share group. Remove it from that group first."

The response returns:
+ the share's `Id` and `Arn` (format `arn:{partition}:partnercentral:{region}:{account-id}:catalog/{catalog}/marketplace-revenue-share/{share-id}`)
+ the `Catalog`
+ the `Products`, each with its `ProductId`, the resolved `ProductCode` and `ProductName`, and the number of accounts of each type
+ `CreatedDate` and `LastModifiedDate`
+ the initial `Revision`

`Revision` is a numeric string, starting at "1". It increases each time the share or one of its allocations changes, and is used for optimistic locking.

### Updating a Marketplace Revenue Share
<a name="updating-a-marketplace-revenue-share"></a>

Partners can change the products and accounts in a share using the `UpdateMarketplaceRevenueShare` API action, for example to add another product that runs on the same backend AWS infrastructure, or to update the AWS deployed accounts. The request replaces the share's complete product set, so partners send every product that should remain in the share.

When updating a Marketplace Revenue Share, partners must provide:
+ **`Catalog`** — `AWS` or `Sandbox`.
+ **`Identifier`** — the share ID or ARN.
+ **`Revision`** — the share's current revision, for optimistic locking.
+ **`Products`** — the complete set of products, in the same format as on creation.

Partners can optionally provide a `ClientToken`.

Products that are added are validated in the same way as on creation. Products that are removed are released and can be added to another share.

Closing a Share: Send an empty `Products` list to close the share. A closed share releases all of its products, can still be retrieved by its ID or ARN, and can no longer be updated. Closed shares are not returned by `ListMarketplaceRevenueShares` unless partners request them with `Identifiers`.

The response returns the share's `Id`, `Arn`, `Products`, `LastModifiedDate`, and `LatestRevision`.

### Adding allocations
<a name="adding-marketplace-revenue-share-allocations"></a>

Once a Marketplace Revenue Share is created, partners declare a revenue share percentage for a month by creating an allocation with the `CreateMarketplaceRevenueShareAllocation` API action.

When creating an allocation, partners must provide:
+ **`Catalog`** — `AWS` or `Sandbox`.
+ **`MarketplaceRevenueShareIdentifier`** — the ID or ARN of the parent share.
+ **`MarketplaceRevenueShareRevision`** — the parent share's current revision.
+ **`EffectiveFrom`** — the first day of the month (`YYYY-MM-DD`).
+ **`EffectiveUntil`** — the last day of the same month (`YYYY-MM-DD`).
+ **`RevenueSharePercent`** — the percentage of revenue collected through AWS Marketplace, as a decimal string from 0.01 to 100 with up to 2 decimal places (for example, "45.00" for 45%).

Partners can optionally provide a `ClientToken`.

The response returns:
+ the allocation's `MarketplaceRevenueShareAllocationId` (format `mrsa-` followed by 13 characters)
+ the parent share's ID, `EffectiveFrom`, `EffectiveUntil`, and `RevenueSharePercent`
+ the `Status` (`ACTIVE` on creation)
+ `CreatedDate` and `LastModifiedDate`
+ `MarketplaceRevenueShareRevision` and `MarketplaceRevenueShareLatestRevision`

Use `MarketplaceRevenueShareLatestRevision` for the next write to the share or its allocations.

### Updating allocations
<a name="updating-marketplace-revenue-share-allocations"></a>

Partners can update an allocation with the `UpdateMarketplaceRevenueShareAllocation` API action while the allocation's month is still open (until the end of the 7th day of the following month, UTC).

When updating an allocation, partners must provide:
+ **`Catalog`** — `AWS` or `Sandbox`.
+ **`MarketplaceRevenueShareIdentifier`** — the ID or ARN of the parent share.
+ **`MarketplaceRevenueShareAllocationId`** — the `mrsa-` ID of the allocation to update.
+ **`MarketplaceRevenueShareRevision`** — the parent share's current revision.

Partners can optionally provide:
+ **`RevenueSharePercent`** — the updated percentage, from 0.01 to 100.
+ **`Status`** — `ACTIVE` or `INACTIVE`. Setting the status to `INACTIVE` deactivates the allocation, so partners can create a different allocation for that month.
+ **`ClientToken`** — an idempotency token.

Optimistic Locking: Every write to a share or its allocations must send the share's current revision. If the revision is stale, the request is rejected with `ConflictException` and the reason `REVISION_MISMATCH`. Retrieve the share with `GetMarketplaceRevenueShare` to get its `LatestRevision`, then retry.

### Viewing Marketplace Revenue Share details
<a name="viewing-marketplace-revenue-share-details"></a>

Partners can retrieve a single Marketplace Revenue Share with the `GetMarketplaceRevenueShare` API action, by ID or ARN. Optionally, provide a `Revision` to retrieve an earlier revision of the share. The response returns:
+ `Id`, `Arn`, and `Catalog`
+ the `Products`, each with its `ProductId`, `ProductCode`, `ProductName` and, for each account type, the account count and the full list of `AccountIds`
+ `Revision` (the revision returned) and `LatestRevision`
+ `EffectiveFrom` and `EffectiveUntil`: the range covered by the share's allocations
+ `TotalActiveMarketplaceRevenueShareAllocationCount` and `TotalMarketplaceRevenueShareAllocationCount`
+ `CreatedDate` and `LastModifiedDate`

`GetMarketplaceRevenueShare` is the only operation that returns the full account ID lists. Create, update, and list responses return account counts only.

Partners can retrieve a single allocation with the `GetMarketplaceRevenueShareAllocation` API action, using the share ID or ARN and the allocation's `MarketplaceRevenueShareAllocationId`. The response returns:
+ `MarketplaceRevenueShareAllocationId` and the parent share's ID
+ `RevenueSharePercent`, `EffectiveFrom`, and `EffectiveUntil`
+ `Status` (`ACTIVE` or `INACTIVE`)
+ `MarketplaceRevenueShareRevision` and `MarketplaceRevenueShareLatestRevision`
+ `CreatedDate` and `LastModifiedDate`

### Listing Marketplace Revenue Shares
<a name="listing-marketplace-revenue-shares"></a>

Partners can view the Marketplace Revenue Shares owned by their account with the `ListMarketplaceRevenueShares` API action. This returns a paginated list of share summaries.

Partners can filter results by:
+ **`Catalog`** (required) — `AWS` or `Sandbox`.
+ **`Identifiers`** — up to 100 share IDs or ARNs.
+ **`ProductIds`** — up to 10 AWS Marketplace product IDs.
+ **`ProductCodes`** — up to 10 AWS Marketplace product codes.
+ **`CreatedAfter` and `CreatedBefore`** — a creation time range.

Sort the results with `SortBy` (`LastModifiedDate`) and `SortOrder` (`ASCENDING` or `DESCENDING`).

Each summary includes:
+ `Id`, `Arn`, and `Catalog`
+ the `Products`, with account counts
+ `LatestRevision`, `EffectiveFrom`, and `EffectiveUntil`
+ the active and total allocation counts
+ `CreatedDate` and `LastModifiedDate`

Use `MaxResults` (1 to 100) and `NextToken` to paginate through large result sets.

### Listing allocations
<a name="listing-marketplace-revenue-share-allocations"></a>

Partners can list the allocations of a specific Marketplace Revenue Share with the `ListMarketplaceRevenueShareAllocations` API action. This returns a paginated list of allocation summaries.

Partners can filter results by:
+ **`StatusFilter`** — `ACTIVE` or `INACTIVE`.
+ **Effective date ranges** — `AfterEffectiveFrom` / `BeforeEffectiveFrom` and `AfterEffectiveUntil` / `BeforeEffectiveUntil`.
+ **`MarketplaceRevenueShareRevision`** — list the allocations as of an earlier revision of the share.

Sort the results with `SortBy` (`EffectiveFrom`) and `SortOrder` (`ASCENDING` or `DESCENDING`).

Each summary includes:
+ `MarketplaceRevenueShareAllocationId`
+ `RevenueSharePercent`, `EffectiveFrom`, and `EffectiveUntil`
+ `Status`
+ `CreatedDate` and `LastModifiedDate`

## Tagging Marketplace Revenue Shares
<a name="tagging-marketplace-revenue-shares"></a>

Standard AWS tagging operations are supported on the Marketplace Revenue Share resource:
+ **`TagResource`** — add or overwrite tags on a Marketplace Revenue Share.
+ **`UntagResource`** — remove specific tags by key.
+ **`ListTagsForResource`** — retrieve all tags currently applied to a Marketplace Revenue Share.

Allocations do not support tags. Tag the parent share to organize related allocations.

Each tagging operation takes the share's ARN as the resource identifier (format `arn:{partition}:partnercentral:{region}:{account-id}:catalog/{catalog}/marketplace-revenue-share/{share-id}`). Tagging on creation is also supported through the `Tags` field of `CreateMarketplaceRevenueShare`.