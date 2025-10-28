# AOSPERF06-BP02 Evaluate bulk request size

Improve indexing performance and domain stability by adjusting bulk
request size to a recommended range of 3-5 MiB.

**Level of risk exposed if this best practice
is not established:** Low

**Desired outcome**: The bulk request
size is within the recommended starting range of 3 – 5 MiB, ensuring
efficient data ingestion and query performance.

**Benefits of establishing this best
practice:**

- Improved indexing performance
- Enhanced domain stability by avoiding unnecessary resource
  utilization

## Implementation guidance

Determining the optimal bulk size depends on your data and domain
configuration. However, a recommended starting point is a bulk
size of three to five MiB per request.

To optimize bulk requests, define the target document batch size
within your application. Instead of trying to determine an exact
number of documents per batch, focus on reaching a total batch
size that falls within this range.

If you have multiple systems that are sending batches to
OpenSearch, consider either using a service like
[Amazon OpenSearch Service Ingestion](https://aws.amazon.com/opensearch-service/features/ingestion/ "https://aws.amazon.com/opensearch-service/features/ingestion/"), which can queue the batches for more
effective ingestion, or ensure that the size of the batches across
all systems do not overpass the recommended range if they
simultaneously ingest data into your OpenSearch Service domain.

## Resources

- [Optimize
  bulk request size and compression](../../../opensearch-service/latest/developerguide/bp.md#bp-perf-bulk "../../../opensearch-service/latest/developerguide/bp.md#bp-perf-bulk")
