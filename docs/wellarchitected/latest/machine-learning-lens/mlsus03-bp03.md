# MLSUS03-BP03 Adopt sustainable storage options

Reduce the volume of data to be stored and adopt sustainable storage
options to limit the carbon impact of your workload. For artifacts
like models and log files that must be kept for long-term regulatory
and audit requirements, use efficient compression algorithms and use
energy efficient cold storage.

**Desired outcome:** You optimize
your ML workload storage to minimize environmental impact while
improving adherence to regulatory requirements. By implementing
efficient storage practices, you reduce data redundancy, properly
size resources, use energy-efficient storage options, and implement
effective compression techniques. This results in reduced carbon
footprint, lower storage costs, and improved overall sustainability
of your ML systems.

**Common anti-patterns:**

- Storing redundant copies of datasets across multiple locations.
- Over-provisioning storage resources for notebooks and instances.
- Using inefficient file formats like CSV instead of columnar
  formats such as parquet.
- Keeping data in high-performance storage regardless of access
  frequency.

**Benefits of establishing this best
practice:**

- Lower operational costs through efficient resource utilization.
- Improved data access performance through appropriate format
  selection.
- Improved ability to adhere to regulatory requirements through
  proper long-term storage planning.
- Reduced waste through optimization of storage resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Storage is a critical component of ML workloads, with large
datasets and model artifacts requiring significant resources. By
optimizing how you store, compress, and manage this data, you can
substantially reduce the environmental impact of your ML systems.
Consider the entire lifecycle of your data, from initial
collection through processing to long-term retention. For
frequently accessed data, choose efficient formats and compression
algorithms. For infrequently accessed data, use Amazon S3 storage
tiers that minimize energy consumption while improving your
adherence to regulatory requirements. By right-sizing your storage
resources and removing redundant data, you can achieve both
sustainability goals and cost optimization.

### Implementation steps

1. **Reduce redundancy of processed
   data**. If you can re-create an infrequently
   accessed dataset, use the
   [Amazon S3 One Zone-IA](https://aws.amazon.com/s3/storage-classes/#__ "https://aws.amazon.com/s3/storage-classes/#__") class to minimize the total data
   stored. Implement S3 Lifecycle policies to automatically
   transition objects to more energy-efficient storage tiers
   based on access patterns.
2. **Right size block storage for
   notebooks**. Don't over-provision block storage of
   your notebooks and use centralized object storage services
   like [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") for common datasets to avoid data duplication.
   Monitor usage patterns and adjust storage allocations
   accordingly.
3. **Use efficient file
   formats**. Use
   [Parquet](https://parquet.apache.org/ "https://parquet.apache.org/")
   to train your models. Compared to CSV, they can reduce
   [your
   storage by up to 87%](../../../whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.md#data-lake-optimization2 "../../../whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.md#data-lake-optimization2"). These columnar formats not only
   reduce storage requirements but also improve query
   performance.
4. **Migrate to more efficient
   compression algorithms**. Evaluate different
   compression algorithms and select the most efficient for
   your data. For example,
   [Zstandard](https://github.com/facebook/zstd "https://github.com/facebook/zstd")
   produces 10–15% smaller files than
   [Gzip](https://www.gzip.org/ "https://www.gzip.org/") at the
   same compression speed.
5. **Implement storage lifecycle
   management**. Configure
   [S3
   Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/ "https://aws.amazon.com/s3/storage-classes/intelligent-tiering/") to automatically move data
   between access tiers based on changing usage patterns. For
   long-term archival needs, use
   [S3 Glacier Deep Archive](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/") to minimize energy consumption
   for rarely accessed data.
6. **Monitor and optimize storage
   utilization**. Regularly review and clean up
   unnecessary data and snapshots. Use
   [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/ "https://aws.amazon.com/s3/storage-analytics-insights/") to gain visibility into usage
   patterns and identify optimization opportunities across your
   organization.
7. **Centralize and share
   datasets**. Implement a centralized data catalog
   using
   [AWSAWS Glue Data Catalog](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md") to make datasets discoverable and
   reusable, reducing the need for multiple copies of the same
   data.
8. **For generative AI workloads, use AI
   for intelligent data management**. Implement
   embeddings storage with efficient vector databases like
   [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") to optimize storage of large language
   model context.

## Resources

**Related documents:**

- [Understanding
  and managing Amazon S3 storage classes](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md")
- [Managing
  storage costs with Amazon S3 Intelligent-Tiering](../../../AmazonS3/latest/userguide/intelligent-tiering.md "../../../AmazonS3/latest/userguide/intelligent-tiering.md")
- [Amazon S3 Storage Analytics and Insights](https://aws.amazon.com/s3/storage-analytics-insights/ "https://aws.amazon.com/s3/storage-analytics-insights/")
- [AWS Well-Architected Framework: Performance Efficiency Pillar -
  Data Management](../performance-efficiency-pillar/data-management.md "../performance-efficiency-pillar/data-management.md")
