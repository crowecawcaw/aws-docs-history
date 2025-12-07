# GPU-acceleration for vector indexing

GPU-acceleration helps you build large-scale vector databases faster and more efficiently. You
can enable this feature on new or existing OpenSearch domains and OpenSearch Serverless collections.
This feature uses GPU-acceleration to reduce the time needed to index data into vector indexes.

With GPU-acceleration, you can increase vector indexing speed by up to 10X at a quarter of the indexing cost.

## Prerequisites

GPU-acceleration is supported on OpenSearch domains running OpenSearch version
`3.1` or later, and OpenSearch Serverless collections. For more information, see [Upgrading Amazon OpenSearch Service domains](version-migration.md "version-migration.md"), [UpdateDomainConfig](../APIReference/API_UpdateDomainConfig.md "../APIReference/API_UpdateDomainConfig.md"),
and [UpdateCollection](../ServerlessAPIReference/API_UpdateCollection.md "../ServerlessAPIReference/API_UpdateCollection.md")
APIs.

## How it works

Vector indexes require significant compute resources to build data structures such as Hierarchical Navigable
Small Worlds (HNSW) graphs. When you enable GPU-acceleration on your domain or collection, OpenSearch automatically detects
opportunities to accelerate your index builds and offloads the index builds
to GPU instances. OpenSearch Service manages the GPU instances on your behalf, assigning them to your domain or collection
when needed. This means you don't manage utilization or pay for idle time.

You pay only for useful processing through Compute Units (OCU) - Vector
Acceleration. Each Vector Acceleration OCU is a combination of approximately 8 GiB of CPU memory,
2 vCPUs, and 6 GiB of GPU memory. For more information, see [GPU Acceleration Pricing](#gpu-acceleration-pricing "#gpu-acceleration-pricing").

To enable GPU acceleration for your domain or collection, see [Enabling GPU-acceleration](gpu-acceleration-enabling.md "gpu-acceleration-enabling.md").

## GPU Acceleration Pricing

AWS charges you when OpenSearch detects opportunities to accelerate your domain's or
collection's index build workloads. Each Vector Acceleration OCU is a combination of
approximately 8 GiB of CPU memory, 2 vCPUs, and 6 GiB of GPU memory.

AWS bills OCU with second-level granularity. In your account statement, you'll see an entry for compute
in OCU-hours.

For example, when you use GPU-acceleration for one hour to create an index, using 2 vCPU and 1 GiB
of GPU memory, you're billed 1 OCU. If you use 9 GiB of CPU memory while using GPU-acceleration,
you're billed 2 OCU.

OpenSearch Serverless adds additional OCUs in increments of 1 OCU based on the compute power and storage
needed to support your collections. You can configure a maximum number of OCUs for your
account in order to control costs.

###### Note

The number of OCUs provisioned at any time can vary and isn't exact. Over time, the
algorithm that OpenSearch and OpenSearch Serverless uses will continue to improve in order to better
minimize system usage.

For full pricing details, see [Amazon OpenSearch Service Pricing](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").

## GPU-acceleration and write operations

GPU-acceleration is activated when OpenSearch's vector ingestion rate (MB/sec) is within a range. On OpenSearch domains, you have the flexibility to [configure this range](https://docs.opensearch.org/3.2/vector-search/remote-index-build/#using-the-remote-index-build-service "https://docs.opensearch.org/3.2/vector-search/remote-index-build/#using-the-remote-index-build-service") through `index.knn.remote_index_build.size.min` and `index.knn.remote_index_build.size.max`. For example, with the lower range default of 50 MB, writing
15,000 full-precision vectors with 768 dimension between [refresh
intervals](bp.md#bp-perf "bp.md#bp-perf") will trigger GPU-acceleration by default.

Data is written with the following API operations:

- [Flush](https://docs.opensearch.org/latest/api-reference/index-apis/flush/ "https://docs.opensearch.org/latest/api-reference/index-apis/flush/")
- [Bulk](https://docs.opensearch.org/latest/api-reference/document-apis/bulk/ "https://docs.opensearch.org/latest/api-reference/document-apis/bulk/")
- [Reindex](https://docs.opensearch.org/latest/api-reference/document-apis/reindex/ "https://docs.opensearch.org/latest/api-reference/document-apis/reindex/")
- [Index](https://docs.opensearch.org/latest/api-reference/index-apis/index/ "https://docs.opensearch.org/latest/api-reference/index-apis/index/")
- [Update](https://docs.opensearch.org/latest/api-reference/document-apis/update-document/ "https://docs.opensearch.org/latest/api-reference/document-apis/update-document/")
- [Delete](https://docs.opensearch.org/latest/api-reference/document-apis/delete-document/ "https://docs.opensearch.org/latest/api-reference/document-apis/delete-document/")
- [Force Merge](https://docs.opensearch.org/latest/api-reference/index-apis/force-merge/ "https://docs.opensearch.org/latest/api-reference/index-apis/force-merge/")

GPU-acceleration is activated with both automatic and [manual](https://docs.opensearch.org/latest/api-reference/index-apis/force-merge/ "https://docs.opensearch.org/latest/api-reference/index-apis/force-merge/")
segment merges.

## Supported index

configurations

The [Faiss](https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#faiss-engine "https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#faiss-engine") engine supports GPU-acceleration.

The following configurations do not support GPU-acceleration:

- [Faiss product quantization](https://docs.opensearch.org/latest/vector-search/optimizing-storage/faiss-product-quantization/ "https://docs.opensearch.org/latest/vector-search/optimizing-storage/faiss-product-quantization/")
- [Inverted File Index (IVF)](https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#ivf-parameters "https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#ivf-parameters")
- [Non-Metric Space Library](https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#nmslib-engine-deprecated "https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#nmslib-engine-deprecated")
- [Lucene engine](https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#lucene-engine "https://docs.opensearch.org/latest/field-types/supported-field-types/knn-methods-engines/#lucene-engine")

## Best practices

Follow these best practices to maximize the benefits of GPU-acceleration for your vector search workloads:

- **Increase index clients** - To take full advantage of GPUs during the index build, increase the number of index clients that are ingesting data into OpenSearch. This allows for better parallelization and utilization of GPU resources.
- **Adjust approximate threshold** - Change the `index.knn.advanced.approximate_threshold` setting to ensure that smaller segment index builds are not happening, which improves the overall speed of ingestion. A value of 10,000 is a good starting point. For collections, you must explicitly specify a value for this setting.
- **Optimize shard size** - Try creating shards that have at least 1 million documents. Shards with fewer than this number of documents may not see overall benefits from GPU-acceleration.
