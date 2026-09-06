

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with your Marketplace Revenue Shares
<a name="working-with-marketplace-revenue-share"></a>

A Marketplace Revenue Share is an input for an AWS Marketplace product that declares the portion of the product's total revenue collected through AWS Marketplace. AWS uses this input to correlate a partner's Marketplace-collected revenue against other revenue signals.

The Marketplace Revenue Share Service exposes APIs to create, retrieve, and list Marketplace Revenue Share resources, and to manage their allocations (the partner-declared revenue-share percentages and effective date windows). Standard AWS tagging operations are supported on the Marketplace Revenue Share resource.

## What is a Marketplace Revenue Share?
<a name="what-is-a-marketplace-revenue-share"></a>

A Marketplace Revenue Share has two layers:
+ **The share** — an input for a single AWS Marketplace product, identified by the Marketplace `ProductId`. There is exactly one Marketplace Revenue Share per product.
+ **One or more allocations** — each allocation declares a `RevenueSharePercent` and an effective date window (`EffectiveDate`, optionally `ExpirationDate`). A share can have many allocations over time, but at any moment only one `ACTIVE` allocation may apply.

Allocations have these key properties:
+ **Status** — `ACTIVE` or `INACTIVE`. On creation, status defaults to `ACTIVE`. Only `ACTIVE` allocations participate in revenue calculations and overlap checks.
+ **Overlap invariant** — within a single share, no two `ACTIVE` allocations may have overlapping `[EffectiveDate, ExpirationDate]` ranges. At most one open-ended `ACTIVE` allocation (no `ExpirationDate`) is permitted per share at any time.

## Working with your Marketplace Revenue Shares
<a name="managing-marketplace-revenue-shares"></a>

Partners manage Marketplace Revenue Shares and their allocations through the Marketplace Revenue Share Service. The lifecycle progresses through two flows: the share flow (create, retrieve, list, tag) and the allocations flow (create, update, soft-delete, retrieve, list).

### Creating a Marketplace Revenue Share
<a name="creating-a-marketplace-revenue-share"></a>

The first step is creating a Marketplace Revenue Share for an AWS Marketplace product using the `CreateMarketplaceRevenueShare` API action. The share is identified by the Marketplace `ProductId` and serves as the container for all subsequent allocations.

When creating a Marketplace Revenue Share, partners must provide:
+ **`Catalog`** — `AWS` for production or `Sandbox` for testing.
+ **`ProductId`** — the 25-character Marketplace product ID. Pattern: `[a-z0-9]{25}`.

Partners can optionally provide:
+ **`Tags`** — up to 50 key-value pairs for resource organization at creation time. Use `TagResource` to add tags after creation.
+ **`ClientToken`** — an idempotency token to prevent duplicate creations on retry. Maximum 64 characters. SDKs auto-generate this token.

Product Validation: On creation, the service verifies with AWS Marketplace that the product is owned by the caller's account or by a subsidiary account connected to the caller via Partner Account Connection (PAC). If the product does not exist or the owning account is not authorized for the caller, the API returns `ValidationException` with reason `PRODUCT_NOT_FOUND_OR_NOT_OWNED`.

One Share Per Product: A second `CreateMarketplaceRevenueShare` call for the same `ProductId` in the same `Catalog` returns `ConflictException`.

The response returns the share's `Arn` (format `arn:{partition}:partnercentral:{region}:{account-id}:catalog/{catalog}/marketplace-revenue-share/{productId}`), the `Catalog`, the `ProductId`, the initial `Version` number (which starts at 1 and increments on each allocation mutation), and any tags applied at creation.

### Adding allocations
<a name="adding-marketplace-revenue-share-allocations"></a>

Once a Marketplace Revenue Share is created, partners declare a revenue-share percentage and an effective date window by creating an allocation through the `CreateMarketplaceRevenueShareAllocation` API action.

When creating an allocation, partners must provide:
+ **`Catalog`** — `AWS` or `Sandbox`.
+ **`MarketplaceRevenueShareIdentifier`** — the identifier of the parent share.
+ **`RevenueSharePercent`** — the percentage of the product's revenue collected through Marketplace provided as a decimal (for example, `0.45` for 45%).
+ **`EffectiveDate`** — the calendar date when this allocation becomes effective. Format: `YYYY-MM-DD`.

The response returns the allocation's `Id` (format `mrsa-[A-Za-z0-9]{13}`), the allocation status (`ACTIVE` on creation), and the parent share's bumped `Version` (a single version integer per share is bumped on every allocation mutation, used for optimistic locking on subsequent allocation updates).

### Updating allocations
<a name="updating-marketplace-revenue-share-allocations"></a>

Partners can update an allocation using the `UpdateMarketplaceRevenueShareAllocation` API action. The updatable fields depend on whether the allocation is future-dated, currently-effective, or past-dated.

When updating an allocation, partners must provide:
+ **`Catalog`** — `AWS` or `Sandbox`.
+ **`MarketplaceRevenueShareIdentifier`** — the identifier of the parent share.
+ **`AllocationId`** — the `mrsa-` ID of the allocation to update.
+ **`MarketplaceRevenueShareVersion`** — the current version of the parent share for optimistic locking on the allocation. Bump conflicts return `ConflictException`.

Partners can optionally provide:
+ **`RevenueSharePercent`** — the updated revenue-share percentage. Editable only on future-dated allocations.
+ **`EffectiveDate`** — the updated effective date. Editable only on future-dated allocations.
+ **`ExpirationDate`** — the updated expiration date. Editable on future-dated allocations (any value `> EffectiveDate`) and on currently-effective or open-ended allocations (any value `≥ today`).
+ **`Status`** — `ACTIVE` or `INACTIVE`. Setting to `INACTIVE` soft-deletes the allocation. Editable only on future-dated allocations.
+ **`ClientToken`** — an idempotency token.

### Viewing Marketplace Revenue Share details
<a name="viewing-marketplace-revenue-share-details"></a>

Partners can retrieve complete information for a single Marketplace Revenue Share using the `GetMarketplaceRevenueShare` API action. This returns the share's `Arn`, `Catalog`, `ProductId`, `Version` (the parent share's current version), `CreatedDate`, `LastModifiedDate`, and any tags applied to the share.

Partners can retrieve a single allocation using the `GetMarketplaceRevenueShareAllocation` API action with the allocation's `Id`. This returns:
+ The allocation's `Id` and parent share's `MarketplaceRevenueShareArn`.
+ `RevenueSharePercent`, `EffectiveDate`, `ExpirationDate`.
+ `Status` (`ACTIVE` or `INACTIVE`).
+ The parent share's `MarketplaceRevenueShareVersion` for optimistic locking on subsequent updates.
+ `CreatedDate` and `LastModifiedDate`.

### Listing Marketplace Revenue Shares
<a name="listing-marketplace-revenue-shares"></a>

Partners can view all Marketplace Revenue Shares owned by their account using the `ListMarketplaceRevenueShares` API action. This returns a paginated list of share summaries.

Partners can filter results by:
+ **`Catalog`** — `AWS` or `Sandbox` (required).
+ **`ProductIds`** — a list of specific Marketplace product IDs to retrieve.

The response includes a summary for each share: `Arn`, `Catalog`, `ProductId`, the latest `Version`, `CreatedDate`, and `LastModifiedDate`.

Use `MaxResults` and `NextToken` to paginate through large result sets.

### Listing allocations
<a name="listing-marketplace-revenue-share-allocations"></a>

Partners can list the allocations for a specific Marketplace Revenue Share using the `ListMarketplaceRevenueShareAllocations` API action. This returns a paginated list of allocation summaries with filtering capabilities.

Partners can filter results by:
+ **`Status`** — `ACTIVE` or `INACTIVE`.
+ **Effective date range** — `EffectiveDateOnOrAfter` / `EffectiveDateOnOrBefore` to retrieve allocations whose effective date falls within a specific window.

The response includes summary information for each allocation: `Id`, `RevenueSharePercent`, `EffectiveDate`, `ExpirationDate`, `Status`, `MarketplaceRevenueShareVersion`, and audit timestamps.

## Tagging Marketplace Revenue Shares
<a name="tagging-marketplace-revenue-shares"></a>

Standard AWS tagging operations are supported on the Marketplace Revenue Share resource:
+ **`TagResource`** — add or overwrite tags on a Marketplace Revenue Share. Maximum 50 tags per share.
+ **`UntagResource`** — remove specific tags by key.
+ **`ListTagsForResource`** — retrieve all tags currently applied to a Marketplace Revenue Share.

Allocations do not support tags. Tag the parent share to organize related allocations.

Each tagging operation accepts the share's `Arn` (format `arn:{partition}:partnercentral:{region}:{account-id}:catalog/{catalog}/marketplace-revenue-share/{productId}`) as the resource identifier. Standard AWS tag-on-create is also supported through the `Tags` field on `CreateMarketplaceRevenueShare`.