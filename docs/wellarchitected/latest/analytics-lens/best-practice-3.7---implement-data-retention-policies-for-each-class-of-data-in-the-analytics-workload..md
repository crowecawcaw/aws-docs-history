# Best practice 3.7 – Implement data retention policies for each class of data in the analytics workload

The business’s data classification policies determine how
long the analytics workload should retain the data and how
long backups should be kept. These policies help ensure that
every system follows the data security rules and compliance
requirements. The analytics workload should implement data
retention and backup policies according to these data
classification policies. For example, if the policy requires
every system to retain the operational data for five years,
the analytics systems should implement rules to keep the
in-scoped data for five years. More information on data
retention can be found in [Sustainability](sustainability.md "sustainability.md") .

## Suggestion 3.7.1 – Create backup requirements and policies based on data classifications

Data backup should be based on business requirements, such
as recovery point objective (RPO), recovery time objective
(RTO), data classifications, and the compliance and audit
requirements.

## Suggestion 3.7.2 – Create data retention requirement policies based on the data classifications

Avoid creating blanket retention policies. Instead,
policies should be tailored to individual data assets
based on their retention requirements.

For more details, refer to the following information:

- AWS Big Data Blog:
  [Building
  a cost efficient, petabyte-scale lake house with Amazon S3
  Lifecycle rules](https://aws.amazon.com/blogs/big-data/part-1-building-a-cost-efficient-petabyte-scale-lake-house-with-amazon-s3-lifecycle-rules-and-amazon-redshift-spectrum/ "https://aws.amazon.com/blogs/big-data/part-1-building-a-cost-efficient-petabyte-scale-lake-house-with-amazon-s3-lifecycle-rules-and-amazon-redshift-spectrum/")
  [and
  Amazon Redshift Spectrum: Part 1](https://aws.amazon.com/blogs/big-data/part-1-building-a-cost-efficient-petabyte-scale-lake-house-with-amazon-s3-lifecycle-rules-and-amazon-redshift-spectrum/ "https://aws.amazon.com/blogs/big-data/part-1-building-a-cost-efficient-petabyte-scale-lake-house-with-amazon-s3-lifecycle-rules-and-amazon-redshift-spectrum/")
- AWS Big Data Blog:
  [Retaining
  data streams up to one year with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/retaining-data-streams-up-to-one-year-with-amazon-kinesis-data-streams/ "https://aws.amazon.com/blogs/big-data/retaining-data-streams-up-to-one-year-with-amazon-kinesis-data-streams/")
- AWS Big Data Blog:
  [Retain
  more for less with UltraWarm for Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/retain-more-for-less-with-ultrawarm-for-amazon-opensearch-service/ "https://aws.amazon.com/blogs/big-data/retain-more-for-less-with-ultrawarm-for-amazon-opensearch-service/")

## Suggestion 3.7.3 – Create data version requirements and policies

Implement a process that captures the data version to
address, based on compliance, security, and operational
requirements.

For more details, refer to the following information:

- AWS Storage Blog:
  [Reduce
  storage costs with fewer noncurrent versions using
  Amazon S3 Lifecycle](https://aws.amazon.com/blogs/storage/reduce-storage-costs-with-fewer-noncurrent-versions-using-amazon-s3-lifecycle/ "https://aws.amazon.com/blogs/storage/reduce-storage-costs-with-fewer-noncurrent-versions-using-amazon-s3-lifecycle/")
- AWS Storage Blog:
  [Simplify
  your data lifecycle by using object tags with Amazon S3
  Lifecycle](https://aws.amazon.com/blogs/storage/simplify-your-data-lifecycle-by-using-object-tags-with-amazon-s3-lifecycle/ "https://aws.amazon.com/blogs/storage/simplify-your-data-lifecycle-by-using-object-tags-with-amazon-s3-lifecycle/")
- AWS Database Blog:
  [Implementing
  version control using Amazon DynamoDB](https://aws.amazon.com/blogs/database/implementing-version-control-using-amazon-dynamodb/ "https://aws.amazon.com/blogs/database/implementing-version-control-using-amazon-dynamodb/")
