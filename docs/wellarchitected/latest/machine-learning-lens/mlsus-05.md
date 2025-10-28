# MLSUS-05: Implement data lifecycle policies aligned with your sustainability goals

Classify data to understand its significance to your workload
and your business outcomes. Use this information to determine
when you can move data to more energy-efficient storage or
safely delete it.

Define data retention periods that support your sustainability
goals while meeting, but not exceeding, your business
requirements.

## Implementation plan

- **Define lifecycle policies for all
  your data classification types** - Determine the
  requirements for the retention and deletion of your data.
- **Manage the lifecycle of all your
  data** - Automatically enforce deletion timelines
  to minimize the total storage requirements of your
  workload using
  [Amazon S3 Lifecycle policies](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").
- **Automatically optimize storage
  sustainability based on access patterns** - Use
  [Amazon S3 Intelligent-Tiering storage class](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/ "https://aws.amazon.com/s3/storage-classes/intelligent-tiering/") to
  automatically move your data to the most sustainable
  access tier when access patterns change.

## Documents

- [Managing
  your storage lifecycle](../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md "../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md") on Amazon S3
- [Amazon S3 Intelligent-Tiering](../../../AmazonS3/latest/userguide/intelligent-tiering.md "../../../AmazonS3/latest/userguide/intelligent-tiering.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 1, identify
  business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/")

## Metrics

- Measure and optimize the total size of your S3 buckets and
  storage class distribution, using
  [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/ "https://aws.amazon.com/s3/storage-analytics-insights/")
