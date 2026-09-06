

# Optimize queries with AWS Glue partition indexing and filtering
<a name="glue-best-practices-partition-index"></a>

When Athena queries partitioned tables, it retrieves and filters the available table partitions to the subset relevant to your query. As new data and partitions are added, more time is required to process the partitions, and query runtime can increase. If you have a table with a large number of partitions that grows over time, consider using AWS Glue partition indexing and filtering. Partition indexing allows Athena to optimize partition processing and improve query performance on highly partitioned tables. Setting up partition filtering in a table's properties is a two-step process:

1. Creating a partition index in AWS Glue.

1. Enabling partition filtering for the table.

## Creating a partition index
<a name="glue-best-practices-partition-index-creating"></a>

For steps on creating a partition index in AWS Glue, see [Working with partition indexes](https://docs.aws.amazon.com/glue/latest/dg/partition-indexes.html) in the AWS Glue Developer Guide. For the limitations on partition indexes in AWS Glue, see the [About partition indexes](https://docs.aws.amazon.com/glue/latest/dg/partition-indexes.html#partition-index-1) section on that page.

## Enabling partition filtering
<a name="glue-best-practices-partition-filtering-enabling"></a>

To enable partition filtering for the table, you must set a new table property in AWS Glue. For steps on how to set table properties in AWS Glue, refer to the [Setting up partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-setting-up.html) page. When you edit the table details in AWS Glue, add the following key-value pair to the **Table properties** section:
+ For **Key**, add `partition_filtering.enabled`
+ For **Value**, add `true`

You can disable partition filtering on this table at any time by setting the `partition_filtering.enabled` value to `false`.

After you complete the above steps, you can return to the Athena console to query the data.

For more information about using partition indexing and filtering, see [Improve Amazon Athena query performance using AWS Glue Data Catalog partition indexes](https://aws.amazon.com/blogs/big-data/improve-amazon-athena-query-performance-using-aws-glue-data-catalog-partition-indexes/) in the *AWS Big Data Blog*.