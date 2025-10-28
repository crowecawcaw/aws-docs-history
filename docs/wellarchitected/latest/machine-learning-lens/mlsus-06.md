# MLSUS-06: Adopt sustainable storage options

Reduce the volume of data to be stored and adopt sustainable
storage options to limit the carbon impact of your workload. For
artifacts like models and log files that must be kept for
long-term compliance and audit requirements, use efficient
compression algorithms and use energy efficient cold storage. 

## Implementation plan

- **Reduce redundancy of processed
  data** - If you can easily re-create an
  infrequently accessed dataset, use the
  [Amazon S3 One Zone-IA](https://aws.amazon.com/s3/storage-classes/#__ "https://aws.amazon.com/s3/storage-classes/#__") class to minimize the total data
  stored.
- **Right size block storage for
  notebooks** - Don’t over-provision block storage
  of your notebooks and use centralized object storage
  services like Amazon S3 for common datasets to avoid data
  duplication.
- **Use efficient file
  formats** - Use
  [Parquet](https://parquet.apache.org/ "https://parquet.apache.org/")
  or [ORC](https://orc.apache.org/ "https://orc.apache.org/")
  to train your models. Compared to CSV, they can help you
  reduce
  [your
  storage by up to 87%](../../../whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.md#data-lake-optimization2 "../../../whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.md#data-lake-optimization2").
- **Migrate to more efficient
  compression algorithms** - Evaluate different
  compression algorithms and select the most efficient for
  your data. For example,
  [Zstandard](https://github.com/facebook/zstd "https://github.com/facebook/zstd")
  produces 10–15% smaller files than
  [Gzip](https://www.gzip.org/ "https://www.gzip.org/") at
  the same compression speed.

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 1, identify
  business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/")
- [Optimizing
  your AWS Infrastructure for Sustainability, Part II:
  Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/")
- [Compressing
  and archiving logs to the Amazon Glacier storage
  classes](https://aws.amazon.com/blogs/storage/compressing-and-archiving-logs-to-the-amazon-s3-glacier-storage-classes/ "https://aws.amazon.com/blogs/storage/compressing-and-archiving-logs-to-the-amazon-s3-glacier-storage-classes/")

## Metrics

- Measure and optimize the total size of your S3 buckets and
  storage class distribution, using
  [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/ "https://aws.amazon.com/s3/storage-analytics-insights/")
- If using SageMaker AI Studio, monitor and optimize the size
  of the
  [shared
  Amazon Elastic File System (Amazon EFS) volume](../../../sagemaker/latest/dg/studio-tasks-manage-storage.md "../../../sagemaker/latest/dg/studio-tasks-manage-storage.md") for
  the team.
