

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with your Revenue Attribution IDs

A Revenue Attribution ID is a deal-level identifier that maps your AWS Marketplace product revenue to specific AWS Marketplace Offers and/or AWS Partner Central Opportunities. It builds on product-level AWS Revenue Measurement: AWS Revenue Measurement captures total attributed revenue for a Marketplace product, and a Revenue Attribution ID maps that revenue to specific deals according to the monthly cost allocation percentages you specify.

Partners use the AWS Partner Central API to create, retrieve, list, and update Revenue Attribution IDs, and to manage their monthly cost allocation entries asynchronously.

## What is a Revenue Attribution ID?
<a name="what-is-a-revenue-attribution-id"></a>

A Revenue Attribution ID has two layers:
+ **The attribution** — a resource that the partner names and describes, identified by an ID with the `ra-` prefix (for example, `ra-aabbccddee001`) and an ARN. Each attribution is scoped to a `Catalog` (`AWS` for production, `Sandbox` for testing) and to the partner's account. An attribution can also carry context: key-value attributes defined by AWS programs, such as the program and workload that the attribution belongs to.
+ **One or more monthly cost allocation entries** — each entry maps one Marketplace Offer or Partner Central Opportunity, one customer AWS account and one calendar month to a revenue share percentage. Entries are created and updated in batches, asynchronously, through an allocation task.

A Revenue Attribution ID can be used in two ways:
+ **As a deal-level overlay** on your existing product-level AWS Revenue Measurement implementation. Create a Revenue Attribution ID, associate your Marketplace Offers and/or Partner Central Opportunities, and AWS maps your already-measured product revenue to those deals — no changes to your existing resource tags or user agent strings are required.
+ **As a standalone identifier**, used directly as a resource tag value (`aws-apn-id` = `<RA ID>`) or in a user agent string (`APN_1.1/pc_<RA ID>$`), to attribute AWS consumption to a specific deal from the start.

## Working with your Revenue Attribution IDs
<a name="managing-revenue-attribution-ids"></a>

Partners manage Revenue Attribution IDs and their monthly cost allocation entries through the AWS Partner Central API. The lifecycle progresses through two independent flows: the attribution-record flow (create, update, retrieve, list) and the allocations flow (start a batch task, poll for results, retrieve individual entries, list entries for an attribution).

### Creating a Revenue Attribution ID
<a name="creating-a-revenue-attribution-id"></a>

The first step is creating a Revenue Attribution ID with the `CreateRevenueAttribution` API action. The returned `Id` and `Arn` can be used immediately as a resource tag value or in a user agent string to attribute AWS consumption.

When creating a Revenue Attribution ID, partners must provide:
+ **`Catalog`** — `AWS` for production or `Sandbox` for testing.
+ **`Name`** — a human-readable name for the attribution. Maximum 128 characters.
+ **`TenancyModel`** — `MULTI_TENANT` or `SINGLE_TENANT`, the tenancy model of the product that the attribution covers.

Partners can optionally provide:
+ **`Description`** — a free-text description of the attribution. Maximum 1024 characters.
+ **`ProductIdentifier`** — the AWS Marketplace product ID or product ARN to associate with this attribution. If omitted, the attribution applies across all consumption measured under the Revenue Attribution ID, regardless of which Marketplace product the customer purchased. This is useful when a single deployment spans more than one Marketplace listing.
+ **`Context`** — program-defined key-value attributes. For details, see [Adding context to a Revenue Attribution ID](#adding-context-to-a-revenue-attribution-id) below.
+ **`Tags`** — up to 200 key-value pairs for organizing resources. Tag keys must be unique within the request.
+ **`ClientToken`** — an idempotency token. AWS SDKs generate this token automatically.

**Best Practice:** Provide `ProductIdentifier` whenever your deal is anchored to a specific Marketplace listing. AWS then validates that the product is owned by the calling partner account, or by a subsidiary account connected to it through Partner Account Connection, and returns the resolved product attributes in the response. If the product is not owned by an authorized account, the API returns `ValidationException`.

The response returns:
+ the new `Id` (format `ra-[a-z0-9]{13}`) and `Arn`
+ `Name`, `Description`, and `TenancyModel`
+ the resolved `MarketplaceProduct` attributes: `ProductId`, `ProductCode`, and `ProductName`
+ the stored `Context`
+ the initial `Revision`

`Revision` is a numeric string, starting at "1", that increases with each subsequent change.

### Adding context to a Revenue Attribution ID
<a name="adding-context-to-a-revenue-attribution-id"></a>

`Context` lets partners label a Revenue Attribution ID with key-value attributes defined by AWS programs. Partners can then find attributions by those attributes with `ListRevenueAttributions`.

`Context` is supported on `CreateRevenueAttribution`, `UpdateRevenueAttribution`, `GetRevenueAttribution` and `ListRevenueAttributions`.

The following keys are supported. Keys are case-sensitive: for example, `program` is rejected.


| Key | Meaning | 
| --- | --- | 
| Program | The AWS partner program that the attribution belongs to | 
| Workload | The workload that is migrated or deployed | 
| ProgramEngagementId | The ID of the partner's engagement in that program | 

Context rules:
+ A `Context` map can contain up to 10 entries. Each key can appear only once.
+ Values are free text: printable ASCII, 1 to 1024 characters.
+ An unsupported key returns `ValidationException` with the reason `REQUEST_VALIDATION_FAILED`. The `FieldList` names the field (for example, `Context.<key>`) and lists the supported keys.
+ Don't put sensitive information in context values.

On `UpdateRevenueAttribution`, `Context` is a full replacement. Omit it to keep the stored context, or send an empty map (`{}`) to clear it. `GetRevenueAttribution` with a `Revision` returns the context that was stored at that revision.

### Adding monthly cost allocation entries
<a name="adding-monthly-cost-allocation-entries"></a>

Once a Revenue Attribution ID is created, partners associate Marketplace Offers and/or Partner Central Opportunities with it by submitting a batch of monthly allocation entries through the `StartRevenueAttributionAllocationsTask` API action. This is an asynchronous operation that accepts up to 250 allocation changes per task. Each change has an `Action` of `CREATE` or `UPDATE`.

The request takes the `Catalog`, the `RevenueAttributionIdentifier` (ID or ARN), the attribution's current `RevenueAttributionRevision` and the list of `RevenueShareAllocations`. Partners can also provide an optional `Description` and a `ClientToken`.

Each allocation entry specifies:
+ **`EntityType` and `EntityIdentifier`** — `OFFER` with a Marketplace Offer ID, or `OPPORTUNITY` with a Partner Central Opportunity ID. If a Marketplace Offer is already linked to a Partner Central Opportunity, partners only need to provide the Offer ID; AWS automatically attributes revenue to the linked Opportunity.
+ **`CustomerAwsAccountId`** — the AWS account of the customer that consumes the product.
+ **`EffectiveFrom` and `EffectiveUntil`** — the first and last day of the calendar month that the entry applies to (`YYYY-MM-DD`).
+ **`RevenueSharePercent`** — the portion of the product's total AWS consumption attributable to this deal in this month, as a decimal string (for example, "25.00").
+ **`RevenueAttributionAllocationId`** — required for `UPDATE`, to identify the entry to change.
+ **`Status`** (optional) — `ACTIVE` or `INACTIVE`.

The total `RevenueSharePercent` across all active entries of a Revenue Attribution ID for the same month must not exceed 100%. An entry that would exceed it is rejected during asynchronous validation with the error code `ALLOCATION_CAP_EXCEEDED`.

**Synchronous validation:** `StartRevenueAttributionAllocationsTask` validates the request shape synchronously: field types, patterns, and batch size. If the request passes, the API returns a `TaskId` with the status `IN_PROGRESS`. Business validation runs asynchronously: the cap check, finalized months, and lookups against AWS Marketplace and Partner Central.

To monitor a task, call `GetRevenueAttributionAllocationsTask` with the Revenue Attribution ID or ARN. It returns the attribution's latest task:
+ **`Status`** — `IN_PROGRESS`, `COMPLETE`, or `FAILED`.
+ `StartedAt`, `EndedAt`, and `TotalRevenueAttributionAllocationRecords`.
+ **`ErrorDetailList`** — one item for each record that failed, with its `EntityType`, `EntityId`, `CustomerAwsAccountId`, `EffectiveFrom`, `EffectiveUntil`, `Action`, an `ErrorCode`, and an `ErrorMessage`. Error codes are `ALLOCATION_CAP_EXCEEDED`, `RESOURCE_NOT_FOUND`, `IMMUTABLE_ALLOCATION`, `ACCESS_DENIED`, `INVALID_VALUE`, `CONCURRENT_MODIFICATION`, and `INTERNAL_ERROR`.
+ **`RevenueAttributionLatestRevision`** — the attribution's revision after the task.

Retrieve task results promptly. Once the task completes, reconcile the outcome of each record, then correct any failed entries and resubmit them in a new task.

### Editing monthly cost allocation entries
<a name="editing-monthly-cost-allocation-entries"></a>

Allocation entries are managed per month, with these rules:
+ Partners can add or update an entry for the current month or any future month at any time.
+ Partners can update last month's entry until the end of the 7th day of the current month (UTC). This window allows partners to review actual usage in AWS Cost Explorer before finalizing the prior month's allocation.
+ After the 7th of the current month, the prior month is finalized and can no longer be changed. A change to a finalized month is rejected with the error code `IMMUTABLE_ALLOCATION`. Updates to a current or future month apply from the next monthly billing cycle. Attribution for prior months is not recalculated retroactively.

Updates are submitted through the same `StartRevenueAttributionAllocationsTask` API action, with `Action` set to `UPDATE` for each affected entry.

### Updating a Revenue Attribution ID
<a name="updating-a-revenue-attribution-id"></a>

Partners can update the `Description` and `Context` of an existing Revenue Attribution ID with the `UpdateRevenueAttribution` API action. The attribution record is otherwise immutable: `Name`, `TenancyModel`, the associated product and the values tagged on creation can't be changed after creation. To re-tag the resource, use the standard AWS tagging operations on the attribution's ARN.

When updating a Revenue Attribution ID, partners must provide:
+ **`Catalog`** — `AWS` or `Sandbox`.
+ **`Identifier`** — the ID or ARN of the attribution to update.
+ **`Revision`** — the attribution's current revision, for optimistic locking.

Partners can optionally provide:
+ **`Description`** — the updated description. Maximum 1024 characters.
+ **`Context`** — the full replacement context map. Omit it to keep the stored context, or send `{}` to clear it.
+ **`ClientToken`** — an idempotency token for the update.

**Optimistic Locking:** The `Revision` field ensures that an update applies only if the attribution hasn't changed since it was last retrieved. If the submitted `Revision` doesn't match the current one, the update is rejected with `ConflictException` and the reason `REVISION_MISMATCH`. As a best practice, retrieve the latest revision with `GetRevenueAttribution` before each update.

### Viewing Revenue Attribution ID details
<a name="viewing-revenue-attribution-id-details"></a>

Partners can retrieve a single Revenue Attribution ID with the `GetRevenueAttribution` API action, by ID or ARN. This returns:

Resource metadata:
+ The unique identifier (`Id`) and the Amazon Resource Name (`Arn`).
+ The `Catalog` that the attribution belongs to.
+ `Name`, `Description`, and `TenancyModel`.
+ `Context`.
+ The returned `Revision` and the `LatestRevision`. Use the latest revision for subsequent updates.
+ `EffectiveFrom` and `EffectiveUntil`: the range covered by the attribution's allocations.
+ `TotalActiveRevenueAttributionAllocationCount` and `TotalRevenueAttributionAllocationCount`.

Marketplace product attributes (if a product was associated on creation):
+ `ProductId`: the Marketplace product ID provided by the partner.
+ `ProductCode`: the AWS Marketplace product code resolved from `ProductId`.
+ `ProductName`: the display name of the Marketplace product.

Audit information:
+ `CreatedDate` and `LastModifiedDate`.

Optionally, provide a `Revision` in the request to retrieve an earlier revision of the attribution. Omit it to get the latest.

To retrieve a specific monthly allocation entry, use the `GetRevenueAttributionAllocation` API action with the attribution's ID or ARN and the entry's `RevenueAttributionAllocationId`. This returns:
+ the `EntityType`, `EntityIdentifier`, and `EntityName`
+ the `CustomerAwsAccountId`
+ `EffectiveFrom`, `EffectiveUntil`, and `RevenueSharePercent`
+ the entry's `Status`
+ the attribution's revisions
+ `CreatedDate` and `LastModifiedDate`

### Listing Revenue Attribution IDs
<a name="listing-revenue-attribution-ids"></a>

Partners can view the Revenue Attribution IDs in their account with the `ListRevenueAttributions` API action. This returns a paginated list of attribution summaries, with filtering and sorting.

Partners can filter results by:
+ **`Catalog`** (required) — `AWS` or `Sandbox`.
+ **`Identifiers`** — up to 100 attribution IDs or ARNs.
+ **`CreatedAfter` and `CreatedBefore`** — a creation time range.
+ **`ContextFilters`** — up to 5 filters, each with a context `Key` and, optionally, up to 20 `Values`.
  + A filter with `Values` matches attributions whose value for that key equals any of the values.
  + A filter without `Values` matches attributions that have the key.
  + Filters are combined with AND, and each key can appear at most once.

Sort the results with `SortBy` (`LastModifiedDate`) and `SortOrder` (`ASCENDING` or `DESCENDING`).

Each summary includes:
+ `Arn`, `Id`, `Catalog`, `Name`, and `TenancyModel`
+ the resolved `MarketplaceProduct` attributes
+ `Context`
+ `CreatedDate` and `LastModifiedDate`
+ the `LatestRevision`, `EffectiveFrom`, and `EffectiveUntil`
+ `TotalActiveRevenueAttributionAllocationCount` and `TotalRevenueAttributionAllocationCount`

Example: list attributions in the Migration Acceleration Program (MAP) that have a program engagement ID:

### Listing monthly cost allocation entries
<a name="listing-monthly-cost-allocation-entries"></a>

Partners can list the monthly allocation entries of a specific Revenue Attribution ID with the `ListRevenueAttributionAllocations` API action. This returns a paginated list of allocation summaries.

Partners can filter results by:
+ **`EntityTypeFilters` and `EntityIdentifierFilters`** — entries for specific Offers or Opportunities.
+ **`CustomerAwsAccountIdFilters`** — entries for specific customer AWS accounts.
+ **`StatusFilter`** — `ACTIVE` or `INACTIVE`.
+ **Effective date ranges** — `AfterEffectiveFrom` / `BeforeEffectiveFrom` and `AfterEffectiveUntil` / `BeforeEffectiveUntil`, for example to list the entries for one month.

Sort the results with `SortBy` (`EffectiveFrom`) and `SortOrder` (`ASCENDING` or `DESCENDING`).

Each summary includes:
+ the `RevenueAttributionAllocationId`
+ the `EntityType`, `EntityIdentifier`, and `EntityName`
+ the `CustomerAwsAccountId`
+ `EffectiveFrom`, `EffectiveUntil`, and `RevenueSharePercent`
+ the entry's `Status`
+ audit timestamps

**Dashboard Building:** The combination of `ListRevenueAttributions` and `ListRevenueAttributionAllocations` supports partner dashboards. For example:
+ All Revenue Attribution IDs created in the last 30 days.
+ All Revenue Attribution IDs for a given program, using `ContextFilters` on `Program`.
+ All monthly allocation entries for a specific Marketplace Offer.
+ All allocation entries for the current month, to check that the totals don't exceed 100% for each attribution.
+ All Revenue Attribution IDs with at least one active allocation entry (`TotalActiveRevenueAttributionAllocationCount > 0`).