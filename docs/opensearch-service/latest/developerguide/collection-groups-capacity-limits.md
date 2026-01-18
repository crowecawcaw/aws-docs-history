# Collection group capacity

limits

Collection groups provide granular control over resource allocation through minimum
and maximum OCU limits. These limits apply to all collections within the group and
operate independently from account-level capacity settings.

By default, there is a service quota (limit) for the number of collections in a collection
group, the number of indexes in a collection, and the number of OCUs in a collection group.
For more information, see [OpenSearch Serverless quotas](limits.md "limits.md").

## Understanding collection group

capacity limits

You can configure minimum and maximum OCU limits for both indexing and search
operations at the collection group level. These limits control how OpenSearch Serverless scales
resources for collections in the group:

- **Minimum OCU** – The minimum number of OCUs
  that OpenSearch Serverless maintains for the collection group, ensuring consistent baseline
  performance.
  - If the workload requires fewer OCU's than the specified minimum value, OpenSearch Serverless would still maintain the specified minimum value of OCU's and billing would reflect the same.
  - If the workload requires higher number of OCU's than the specified minimum value, OpenSearch Serverless would maintain that level of OCU's that's required for the workload and the billing would reflect the higher OCU utilization.

- **Maximum OCU** – The maximum number of OCUs
  that OpenSearch Serverless can scale up to for the collection group, helping you control
  costs.

Collection group capacity limits are decoupled from account-level limits.
Account-level maximum OCU settings apply only to collections not associated with any
collection group, while collection group maximum OCU settings apply to collections
within that specific group.

## Valid capacity limit

values

When setting minimum and maximum OCU limits for a collection group, you can only
use values from the following set: 1, 2, 4, 8, 16, and multiples of 16 (such as 32,
48, 64, 80, 96).

Both minimum and maximum OCU limits are optional when you create a collection
group. If you don't specify a maximum OCU limit, OpenSearch Serverless uses a default value of 96
OCUs.

The minimum OCU limit must be less than or equal to the maximum OCU limit. The sum
of all maximum OCU limits across your account-level settings and all collection
groups cannot exceed 1,700 OCUs per account.

## Configuring capacity

limits

You can set capacity limits when you create a collection group or update them
later. To configure capacity limits using the AWS CLI, use the [CreateCollectionGroup](../ServerlessAPIReference/API_CreateCollectionGroup.md "../ServerlessAPIReference/API_CreateCollectionGroup.md") or [UpdateCollectionGroup](../ServerlessAPIReference/API_UpdateCollectionGroup.md "../ServerlessAPIReference/API_UpdateCollectionGroup.md") commands:

```
aws opensearchserverless create-collection-group \
    --name `my-collection-group` \
    --capacity-limits maxIndexingCapacityInOCU=`32`,maxSearchCapacityInOCU=`32`,minIndexingCapacityInOCU=`4`,minSearchCapacityInOCU=`4`
```

To update capacity limits for an existing collection group:

```
aws opensearchserverless update-collection-group \
    --id `abcdef123456` \
    --capacity-limits maxIndexingCapacityInOCU=`48`,maxSearchCapacityInOCU=`48`,minIndexingCapacityInOCU=`8`,minSearchCapacityInOCU=`8`
```

## Monitoring collection group

capacity

OpenSearch Serverless emits the following Amazon CloudWatch Logs metrics at one-minute intervals to help you
monitor OCU utilization and capacity limits at the collection group level:

- `IndexingOCU` – The number of indexing OCUs currently in use by
  the collection group.
- `SearchOCU` – The number of search OCUs currently in use by the
  collection group.

OpenSearch Serverless also emits OCU metrics at the account level for collections not
associated with any collection group. You can aggregate these metrics in CloudWatch to
visualize the sum of OCUs across all collection groups and account-level
collections.

Configure alarms to notify you when your collection group approaches its capacity
limits so you can adjust settings as needed. For more information about OpenSearch Serverless
metrics, see [Monitoring Amazon OpenSearch Serverless](serverless-monitoring.md "serverless-monitoring.md").

## How capacity limits are

enforced

OpenSearch Serverless enforces collection group capacity limits during scaling operations. When
your collections need additional resources, OpenSearch Serverless scales up to the maximum OCU
limit. When demand decreases, OpenSearch Serverless scales down but maintains at least the minimum
OCU limit to ensure consistent performance.

Capacity limits are enforced only when the collection group contains at least one
collection. Empty collection groups do not consume OCUs or enforce capacity
limits.

If a scaling operation would exceed the maximum OCU limit or violate the minimum
OCU requirement, OpenSearch Serverless rejects the operation to maintain compliance with your
configured limits.
