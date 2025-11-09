# Amazon DocumentDB connections

You can use AWS Glue for Spark to read from and write to tables in Amazon DocumentDB. You can connect to Amazon DocumentDB using
credentials stored in AWS Secrets Manager through a AWS Glue connection.

For more information about Amazon DocumentDB, consult the [Amazon DocumentDB documentation](../../../documentdb/latest/developerguide/what-is.md "../../../documentdb/latest/developerguide/what-is.md").

###### Note

Amazon DocumentDB elastic clusters are not currently supported when using the AWS Glue connector. For more information
about elastic clusters, see [Using Amazon DocumentDB elastic
clusters](../../../documentdb/latest/developerguide/docdb-using-elastic-clusters.md "../../../documentdb/latest/developerguide/docdb-using-elastic-clusters.md").

## Reading and writing to Amazon DocumentDB collections

###### Note

When you create an ETL job that connects to Amazon DocumentDB, for the `Connections`
job property, you must designate a connection object that specifies the virtual private
cloud (VPC) in which Amazon DocumentDB is running. For the connection object, the connection type
must be `JDBC`, and the `JDBC URL` must be
`mongo://`<DocumentDB_host>`:27017`.

###### Note

These code samples were developed for AWS Glue 3.0. To migrate to AWS Glue 4.0, consult [MongoDB](migrating-version-40.md#migrating-version-40-connector-driver-migration-mongodb "migrating-version-40.md#migrating-version-40-connector-driver-migration-mongodb"). The `uri` parameter has
changed.

###### Note

When using Amazon DocumentDB, `retryWrites` must be set to false in certain situations, such as when the document written specifies `_id`. For more
information, consult [Functional Differences with MongoDB](../../../documentdb/latest/developerguide/functional-differences.md#functional-differences.retryable-writes "../../../documentdb/latest/developerguide/functional-differences.md#functional-differences.retryable-writes") in the Amazon DocumentDB documentation.

The following Python script demonstrates using connection types and connection options
for reading and writing to Amazon DocumentDB.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext, SparkConf
from awsglue.context import GlueContext
from awsglue.job import Job
import time

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

output_path = "s3://some_bucket/output/" + str(time.time()) + "/"
documentdb_uri = "mongodb://<mongo-instanced-ip-address>:27017"
documentdb_write_uri = "mongodb://<mongo-instanced-ip-address>:27017"

read_docdb_options = {
    "uri": documentdb_uri,
    "database": "test",
    "collection": "coll",
    "username": "username",
    "password": "1234567890",
    "ssl": "true",
    "ssl.domain_match": "false",
    "partitioner": "MongoSamplePartitioner",
    "partitionerOptions.partitionSizeMB": "10",
    "partitionerOptions.partitionKey": "_id"
}

write_documentdb_options = {
    "retryWrites": "false",
    "uri": documentdb_write_uri,
    "database": "test",
    "collection": "coll",
    "username": "username",
    "password": "pwd"
}

# Get DynamicFrame from  DocumentDB
dynamic_frame2 = glueContext.create_dynamic_frame.from_options(connection_type="documentdb",
                                                               connection_options=read_docdb_options)

# Write DynamicFrame to MongoDB and DocumentDB
glueContext.write_dynamic_frame.from_options(dynamic_frame2, connection_type="documentdb",
                                             connection_options=write_documentdb_options)

job.commit()
```

The following Scala script demonstrates using connection types and connection options
for reading and writing to Amazon DocumentDB.

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.MappingSpec
import com.amazonaws.services.glue.errors.CallSite
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import com.amazonaws.services.glue.DynamicFrame
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._

object GlueApp {
  val DOC_URI: String = "mongodb://<mongo-instanced-ip-address>:27017"
  val DOC_WRITE_URI: String = "mongodb://<mongo-instanced-ip-address>:27017"
  lazy val documentDBJsonOption = jsonOptions(DOC_URI)
  lazy val writeDocumentDBJsonOption = jsonOptions(DOC_WRITE_URI)
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)

    // Get DynamicFrame from DocumentDB
    val resultFrame2: DynamicFrame = glueContext.getSource("documentdb", documentDBJsonOption).getDynamicFrame()

    // Write DynamicFrame to DocumentDB
    glueContext.getSink("documentdb", writeJsonOption).writeDynamicFrame(resultFrame2)

    Job.commit()
  }

  private def jsonOptions(uri: String): JsonOptions = {
    new JsonOptions(
      s"""{"uri": "${uri}",
         |"database":"test",
         |"collection":"coll",
         |"username": "username",
         |"password": "pwd",
         |"ssl":"true",
         |"ssl.domain_match":"false",
         |"partitioner": "MongoSamplePartitioner",
         |"partitionerOptions.partitionSizeMB": "10",
         |"partitionerOptions.partitionKey": "_id"}""".stripMargin)
  }
}
```

## Amazon DocumentDB connection option reference

Designates a connection to Amazon DocumentDB (with MongoDB compatibility).

Connection options differ for a source connection and a sink connection.

### "connectionType": "Documentdb" as

source

Use the following connection options with `"connectionType": "documentdb"` as
a source:

- `"uri"`: (Required) The Amazon DocumentDB host to read from, formatted as
  `mongodb://<host>:<port>`.
- `"database"`: (Required) The Amazon DocumentDB database to read from.
- `"collection"`: (Required) The Amazon DocumentDB collection to read from.
- `"username"`: (Required) The Amazon DocumentDB user name.
- `"password"`: (Required) The Amazon DocumentDB password.
- `"ssl"`: (Required if using SSL) If your connection uses SSL, then you
  must include this option with the value `"true"`.
- `"ssl.domain_match"`: (Required if using SSL) If your connection uses
  SSL, then you must include this option with the value `"false"`.
- `"batchSize"`: (Optional): The number of documents to return per batch,
  used within the cursor of internal batches.
- `"partitioner"`: (Optional): The class name of the partitioner for
  reading input data from Amazon DocumentDB. The connector provides the following
  partitioners:
  - `MongoDefaultPartitioner` (default) (Not supported in AWS Glue 4.0)
  - `MongoSamplePartitioner` (Not supported in AWS Glue 4.0)
  - `MongoShardedPartitioner`
  - `MongoSplitVectorPartitioner`
  - `MongoPaginateByCountPartitioner`
  - `MongoPaginateBySizePartitioner` (Not supported in AWS Glue 4.0)

- `"partitionerOptions"` (Optional): Options for the designated
  partitioner. The following options are supported for each partitioner:

      + `MongoSamplePartitioner`: `partitionKey`,
       `partitionSizeMB`, `samplesPerPartition`
      + `MongoShardedPartitioner`: `shardkey`
      + `MongoSplitVectorPartitioner`: `partitionKey`,
       partitionSizeMB
      + `MongoPaginateByCountPartitioner`: `partitionKey`,
       `numberOfPartitions`
      + `MongoPaginateBySizePartitioner`: `partitionKey`,
       partitionSizeMB

  For more information about these options, see [Partitioner Configuration](https://docs.mongodb.com/spark-connector/master/configuration/#partitioner-conf "https://docs.mongodb.com/spark-connector/master/configuration/#partitioner-conf") in the MongoDB documentation.

### "connectionType": "Documentdb" as

sink

Use the following connection options with `"connectionType": "documentdb"` as
a sink:

- `"uri"`: (Required) The Amazon DocumentDB host to write to, formatted as
  `mongodb://<host>:<port>`.
- `"database"`: (Required) The Amazon DocumentDB database to write to.
- `"collection"`: (Required) The Amazon DocumentDB collection to write to.
- `"username"`: (Required) The Amazon DocumentDB user name.
- `"password"`: (Required) The Amazon DocumentDB password.
- `"extendedBsonTypes"`: (Optional) If `true`, allows extended
  BSON types when writing data to Amazon DocumentDB. The default is `true`.
- `"replaceDocument"`: (Optional) If `true`, replaces the whole
  document when saving datasets that contain an `_id` field. If
  `false`, only fields in the document that match the fields in the dataset
  are updated. The default is `true`.
- `"maxBatchSize"`: (Optional): The maximum batch size for bulk operations
  when saving data. The default is 512.
- `"retryWrites"`: (Optional): Automatically retry certain write operations a single
  time if AWS Glue encounters a network error.
