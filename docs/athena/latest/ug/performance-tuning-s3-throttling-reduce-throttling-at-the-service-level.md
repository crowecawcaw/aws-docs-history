# Reduce throttling at the service level

To avoid Amazon S3 throttling at the service level, you can monitor your usage and adjust
your [service
quotas](../../../general/latest/gr/s3.md#limits_s3 "../../../general/latest/gr/s3.md#limits_s3"), or you use certain techniques like partitioning. The following are
some of the conditions that can lead to throttling:

- Exceeding your account's API request limits
  – Amazon S3 has default API request limits that are based on account type and
  usage. If you exceed the maximum number of requests per second for a single
  prefix, your requests may be throttled to prevent overload of the Amazon S3
  service.
- Insufficient partitioning of data – If
  you do not properly partition your data and transfer a large amount of data,
  Amazon S3 can throttle your requests. For more information about partitioning, see
  the [Use
  partitioning](performance-tuning-s3-throttling-optimizing-your-tables.md#performance-tuning-s3-throttling-use-partitioning "performance-tuning-s3-throttling-optimizing-your-tables.md#performance-tuning-s3-throttling-use-partitioning") section
  in this document.
- Large number of small objects – If
  possible, avoid having a large number of small files. Amazon S3 has a limit of [5500 GET
  requests](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md") per second per partitioned prefix, and your Athena queries
  share this same limit. If you scan millions of small objects in a single query,
  your query will likely be throttled by Amazon S3.
  To avoid excess scanning, you can use AWS Glue ETL to periodically compact your files, or
  you partition the table and add partition key filters. For more information, see the
  following resources.

- [How can I
  configure an AWS Glue ETL job to output larger files?](https://aws.amazon.com/premiumsupport/knowledge-center/glue-job-output-large-files/ "https://aws.amazon.com/premiumsupport/knowledge-center/glue-job-output-large-files/") (_AWS Knowledge Center_)
- [Reading input files in larger groups](../../../glue/latest/dg/grouping-input-files.md "../../../glue/latest/dg/grouping-input-files.md") (_AWS Glue Developer Guide_)
