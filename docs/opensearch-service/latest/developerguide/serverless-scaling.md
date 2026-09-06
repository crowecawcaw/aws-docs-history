

# Managing capacity limits for Amazon OpenSearch Serverless
<a name="serverless-scaling"></a>

With Amazon OpenSearch Serverless, you don't have to manage capacity yourself. OpenSearch Serverless automatically scales the compute capacity for your account based on the current workload. Serverless compute capacity is measured in *OpenSearch Compute Units* (OCUs). Each OCU is a combination of 6 GiB of memory and corresponding virtual CPU (vCPU), as well as data transfer to the shared storage and Amazon S3. For more information about the decoupled architecture in OpenSearch Serverless, see [How it works](serverless-overview.md#serverless-process).

OpenSearch Serverless automatically scales compute capacity for your collections. You can set a minimum and maximum OCU per collection group, separately for indexing and searching. When not actively indexing or searching, OCUs scale down to the minimum OCU value independently for indexing and search. If the minimum is set to 0, no OCUs are needed when idle. OpenSearch Serverless offers high availability by default without requiring standby nodes or redundancy configuration. Collections within a collection group can share OCUs for cost efficiency by pooling compute capacity. Only one type of collection (search, time series, or vector search) can be included in a single collection group. For more information, see [Amazon OpenSearch Serverless collection groups](serverless-collection-groups.md).

OpenSearch Serverless automatically scales out and adds OCUs as your indexing and search usage grows. When traffic decreases, capacity scales back down to the minimum number of OCUs required for your data size.

For *search* and *vector search* collections, all data is stored on hot indexes to ensure fast query response times. *Time series* collections use a combination of hot and warm storage, keeping the most recent data in hot storage to optimize query response times for more frequently accessed data. For more information, see [Choosing a collection type](serverless-overview.md#serverless-usecase).

To manage capacity for your collections and control costs, you specify minimum and maximum OCU values at the collection group level, separately for indexing and searching. Every collection belongs to a collection group, and OpenSearch Serverless automatically scales compute resources within the bounds you configure.
+ **Minimum capacity** – OpenSearch Serverless provisions this number of OCUs regardless of traffic. Use minimum capacity to avoid cold start delays when scaling from zero and to achieve deterministic startup performance for your workloads.
+ **Maximum capacity** – OpenSearch Serverless will not scale beyond this number of OCUs. Use maximum capacity as a budgetary control lever to ensure your collections always stay within a defined spend limit.

OpenSearch Serverless automatically scales the number of OCUs within your configured range to process the indexing and search workload.

**Note**  
Classic collections can be created without a collection group. For such collections, capacity settings apply at the account level and OCUs can be shared across collections as long as they use the same AWS KMS keys.

## Configuring capacity settings
<a name="serverless-scaling-configure"></a>

To configure capacity settings for a collection group in the OpenSearch Serverless console, navigate to the collection group and specify the minimum and maximum OCU values for indexing and search under **Capacity limits**.

To update capacity settings for a collection group using the AWS CLI, send an [UpdateCollectionGroup](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollectionGroup.html) request:

```
aws opensearchserverless update-collection-group \
    --id {{collection-group-id}} \
    --capacity-limits '{
        "minIndexingCapacityInOCU": {{0}},
        "maxIndexingCapacityInOCU": {{96}},
        "minSearchCapacityInOCU": {{0}},
        "maxSearchCapacityInOCU": {{96}}
    }'
```

**Note**  
For Classic collections that are not part of a collection group, capacity settings are configured at the account level using the [update-account-settings](https://docs.aws.amazon.com/cli/latest/reference/opensearchserverless/update-account-settings.html) command.

## Maximum capacity limits
<a name="serverless-scaling-limits"></a>

The maximum total of indexes a collection can contain is 1000. The minimum OCU capacity for a collection group is 0 OCUs for indexing and 0 OCUs for search. For each collection group, the maximum allowed capacity is 1,700 OCUs for indexing and 1,700 OCUs for search. You can configure the OCU count to be 2, 4, 8, 16, or any multiple of 16 up to the maximum allowed capacity.

For Classic collections, each OCU includes hot ephemeral storage of 120 GiB. OpenSearch Serverless supports up to 10 TiB of managed hot storage per collection.

For a list of all quotas, see [OpenSearch Serverless quotas](https://docs.aws.amazon.com/general/latest/gr/opensearch-service.html#opensearch-limits-serverless).

## Monitoring capacity usage
<a name="serverless-scaling-monitoring"></a>

You can monitor the `SearchOCU` and `IndexingOCU` account-level CloudWatch metrics to understand how your collections are scaling. We recommend that you configure alarms to notify you if your account is approaching a threshold for metrics related to capacity, so you can adjust your capacity settings accordingly.

You can also use these metrics to determine if your maximum capacity settings are appropriate, or if you need to adjust them. Analyze these metrics to focus your efforts for optimizing the efficiency of your collections. For more information about the metrics that OpenSearch Serverless sends to CloudWatch, see [Monitoring Amazon OpenSearch Serverless](serverless-monitoring.md).