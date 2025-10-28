# Considerations

Note these behaviors and limitations when you use the DynamoDB connector with Apache Spark or Apache Hive.

## Considerations when using the DynamoDB

connector with Apache Spark

- Spark SQL doesn't support the creation of a Hive table with the
  storage-handler option. For more information, refer to [Specifying storage format for Hive tables](https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#specifying-storage-format-for-hive-tables "https://spark.apache.org/docs/latest/sql-data-sources-hive-tables.html#specifying-storage-format-for-hive-tables") in the Apache
  Spark documentation.
- Spark SQL doesn't support the `STORED BY` operation with
  storage handler. If you want to interact with a DynamoDB table through an
  external Hive table, use Hive to create the table first.
- To translate a query to a DynamoDB query, the DynamoDB connector uses
  _predicate pushdown_. Predicate pushdown filters
  data by a column that is mapped to the partition key of a DynamoDB table.
  Predicate pushdown only operates when you use the connector with Spark
  SQL, and not with the MapReduce API.

## Considerations when using the DynamoDB

connector with Apache Hive

**Tuning the maximum number of mappers**

- If you use the `SELECT` query to read data from an external
  Hive table that maps to DynamoDB, the number of map tasks on
  EMR Serverless is calculated as the total read throughput configured
  for the DynamoDB table, divided by the throughput per map task. The default
  throughput per map task is 100.
- The Hive job can use the number of map tasks beyond the maximum number
  of containers configured per EMR Serverless application, depending upon
  the read throughput configured for DynamoDB. Also, a long-running Hive
  query can consume all of the provisioned read capacity of the DynamoDB
  table. This negatively impacts other users.
- You can use the `dynamodb.max.map.tasks` property to set an
  upper limit for map tasks. You can also use this property to tune the
  amount of data read by each map task based on the task container
  size.
- You can set the `dynamodb.max.map.tasks`property at Hive
  query level, or in the `hive-site` classification of the
  **start-job-run** command. This value must be equal
  to or greater than 1. When Hive processes your query, the resulting Hive
  job uses no more than the values of `dynamodb.max.map.tasks`
  when it reads from the DynamoDB table.

**Tuning the write throughput per task**

- Write throughput per task on EMR Serverless is calculated as the
  total write throughput that is configured for a DynamoDB table, divided by
  the value of the `mapreduce.job.maps` property. For Hive, the
  default value of this property is 2. Thusthe first two tasks in the
  final stage of Hive job can consume all of the write throughput . This
  leads to throttling of writes of other tasks in the same job or other
  jobs.
- To avoid write throttling, set the value of
  `mapreduce.job.maps` property based on the number of
  tasks in the final stage or the write throughput that you want to
  allocate per task. Set this property in the `mapred-site`
  classification of the **start-job-run** command on
  EMR Serverless.
