

# Query S3 Express One Zone data
<a name="querying-express-one-zone"></a>

The Amazon S3 Express One Zone storage class is a highly performant Amazon S3 storage class that provides single-digit millisecond response times. As such, it is useful for applications that frequently access data with hundreds of thousands of requests per second.

S3 Express One Zone replicates and stores data within the same Availability Zone to optimize for speed and cost. This differs from Amazon S3 Regional storage classes, which automatically replicate data across a minimum of three AWS Availability Zones within an AWS Region.

For more information, see [What is S3 Express One Zone?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html) in the *Amazon S3 User Guide*.

## Prerequisites
<a name="querying-express-one-zone-prerequisites"></a>

Confirm that the following conditions are met before you begin:
+ **Athena engine version 3** – To use S3 Express One Zone with Athena SQL, your workgroup must be configured to use Athena engine version 3.
+ **S3 Express One Zone permissions** – When S3 Express One Zone calls an action like `GET`, `LIST`, or `PUT` on an Amazon S3 object, the storage class calls `CreateSession` on your behalf. For this reason, your IAM policy must allow the `s3express:CreateSession` action, which allows Athena to invoke the corresponding API operation.

## Considerations and limitations
<a name="querying-express-one-zone-considerations-and-limitations"></a>

When you query S3 Express One Zone with Athena, consider the following points. 
+ S3 Express One Zone buckets supports `SSE_S3` and `SSE-KMS` encryption. Athena query results are written using `SSE_S3` encryption regardless of the option that you choose in workgroup settings to encrypt query results. This limitation includes all scenarios in which Athena writes data to S3 Express One Zone buckets, including `CREATE TABLE AS` (CTAS) and `INSERT INTO` statements.
+ The AWS Glue crawler is not supported for creating tables on S3 Express One Zone data.
+ The `MSCK REPAIR TABLE` statement is not supported. As a workaround, use [ALTER TABLE ADD PARTITION](alter-table-add-partition.md).
+ No table modifying DDL statements for Apache Iceberg (that is, no `ALTER TABLE` statements) are supported for S3 Express One Zone.
+ Lake Formation is not supported with S3 Express One Zone buckets.
+ The following file and table formats are unsupported or have limited support. If formats aren't listed, but are supported for Athena (such as Parquet, ORC, and JSON), then they're also supported for use with S3 Express One Zone storage.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/athena/latest/ug/querying-express-one-zone.html)

## Get started
<a name="querying-express-one-zone-getting-started"></a>

Querying S3 Express One Zone data with Athena is straightforward. To get started, use the following procedure.

**To use Athena SQL to query S3 Express One Zone data**

1. Transition your data to S3 Express One Zone storage. For more information, see [Setting the storage class of an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-howtoset) in the *Amazon S3 User Guide*.

1. Use a [CREATE TABLE](create-table.md) statement in Athena to catalog your data in AWS Glue Data Catalog. For information about creating tables in Athena, see [Create tables in Athena](creating-tables.md) and the [CREATE TABLE](create-table.md) statement.

1. (Optional) Configure the query result location of your Athena workgroup to use an Amazon S3 *directory bucket*. Amazon S3 directory buckets are more performant that general buckets and are designed for workloads or performance-critical applications that require consistent single-digit millisecond latency. For more information, see [Directory buckets overview](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon S3 User Guide*.