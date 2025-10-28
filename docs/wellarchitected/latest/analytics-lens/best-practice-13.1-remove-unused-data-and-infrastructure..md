# Best practice 13.1 – Remove unused data and infrastructure

Delete data that is out of its retention period, or not
needed anymore. Delete intermediate-processed data that can
be removed without business impacts. If the output of
analytics jobs is not used by anyone, consider removing such
jobs so that you don't waste resources.

## Suggestion 13.1.1 – Track data freshness

In many cases, maintaining a metadata repository for
tracking data movement will be worthwhile. This is not
only to instill confidence in the quality of the data, but
also to identify infrequently updated data, and unused
data.

## Suggestion 13.1.2 – Delete data that is out of its retention period

Data that is past its retention period should be deleted
to reduce unnecessary storage costs. Identify data through
the metadata catalog that is outside its retention period.
To reduce human effort, automate the data removal process.
If data is stored in Amazon S3, use Amazon S3 Lifecycle
configurations to expire data automatically.

## Suggestion 13.1.3 – Delete intermediate-processed data that can be removed without business impacts

Many steps in analytics processes create intermediate or
temporary datasets. Ensure that intermediate datasets are
removed if they have no further business value.

## Suggestion 13.1.4 – Remove unused analytics jobs that consume infrastructure resources but no one uses the job results

Periodically review the ownership, source, and downstream
consumers of all analytics infrastructure resources. If
downstream consumers no longer need the analytics job,
stop the job from running and remove unneeded resources.

## Suggestion 13.1.5 – Use the lowest acceptable frequency for data processing

Data processing requirements must be considered in the business context. There is no value in processing data faster than it is consumed or delivered. For example, in a sales analytics workload, it might not be necessary to perform analytics on each transaction as it arrives. In some cases, only hourly reports are needed by business management. Batch processing the transactions is more eﬃcient and can reduce unnecessary infrastructure costs between batch processing jobs.

## Suggestion 13.1.6 – Compress data to reduce cost

Data compression can significantly reduce storage and query costs. Columnar data formats like Apache Parquet stores data in columns rather than rows, allowing similar data to be stored contiguously. Using Parquet over CSV format can reduce storage costs significantly. Since services like Amazon Redshift Spectrum and Amazon Athena charge for bytes scanned, compressing data lowers the overall cost of using those services.
