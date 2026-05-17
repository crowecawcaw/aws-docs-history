Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Metrics in Amazon Redshift Spectrum

This topic describes system views that you can use to monitor data lake queries.

You can monitor data lake queries using the following system views:

- [SVL_S3QUERY](r_SVL_S3QUERY.md "r_SVL_S3QUERY.md")

Use the SVL_S3QUERY view to get details about data lake queries
at the segment and node slice level.

- [SVL_S3QUERY_SUMMARY](r_SVL_S3QUERY_SUMMARY.md "r_SVL_S3QUERY_SUMMARY.md")

Use the SVL_S3QUERY_SUMMARY view to get a summary of all data lake queries
that have been run on the system.
The following are some things to look for in SVL_S3QUERY_SUMMARY:

- The number of files that were processed by the Redshift Spectrum query.
- The number of bytes scanned from Amazon S3. The cost of a Redshift Spectrum query is
  reflected in the amount of data scanned from Amazon S3.
- The number of bytes returned from the Redshift Spectrum layer to the cluster. A
  large amount of data returned might affect system performance.
- The maximum duration and average duration of Redshift Spectrum requests.
  Long-running requests might indicate a bottleneck.

## Note about RG provisioned clusters

On RG provisioned clusters, Redshift Spectrum queries run on the cluster's own compute rather than on the dedicated Spectrum fleet used by RA3 and DC2 provisioned clusters. **[SVL_S3QUERY](r_SVL_S3QUERY.md "r_SVL_S3QUERY.md")** and **[SVL_S3QUERY_SUMMARY](r_SVL_S3QUERY_SUMMARY.md "r_SVL_S3QUERY_SUMMARY.md")** continue to be populated on RG clusters. The following columns have different semantics or are deprecated.

### Columns populated with different semantics on RG provisioned clusters

On RA3 and DC2 provisioned clusters, these columns describe rows, bytes, and work units moving between the cluster and the Spectrum fleet. On RG provisioned clusters, they describe the equivalent work performed by the cluster's native reader:

- **s3_scanned_rows** — rows read directly from Amazon S3 by the cluster's native reader (pre-filter).
- **s3_scanned_bytes** — total scan-range size in bytes processed by the cluster's native reader.
- **s3query_returned_rows** — rows produced after filter pushdown by the cluster's native reader.
- **s3query_returned_bytes** — bytes produced after filter pushdown by the cluster's native reader.
- **splits** — number of scan ranges consumed by the cluster's native reader.
- **total_split_size** — total size of all scan ranges consumed, in bytes.
- **max_split_size** — size of the largest scan range consumed, in bytes.

### Columns deprecated on RG provisioned clusters

These columns describe Spectrum-fleet concepts that do not exist on RG. On RG clusters they are logged as -1 in STL_S3QUERY, and therefore appear as -1 or are not meaningful in SVL_S3QUERY and SVL_S3QUERY_SUMMARY:

- **total_retries**, **max_retries** — On RG, retries occur at the Amazon S3 client level. Use STL_S3CLIENT and STL_S3CLIENT_ERROR for retry details.
- **max_request_duration**, **avg_request_duration** — RG does not use the Spectrum request model.
- **max_request_parallelism**, **avg_request_parallelism** — RG does not use Spectrum request tokens.
- **slowdown_count**, **max_concurrent_slowdown_count** — On RG, Amazon S3 slowdowns are tracked in STL_S3CLIENT.

For aggregated per-query metrics on RG clusters (partitions, files scanned, rows and bytes returned, file format, file location, listing and partition-fetch timing), you can also use the [SYS_EXTERNAL_QUERY_DETAIL](SYS_EXTERNAL_QUERY_DETAIL.md "SYS_EXTERNAL_QUERY_DETAIL.md") monitoring view.
