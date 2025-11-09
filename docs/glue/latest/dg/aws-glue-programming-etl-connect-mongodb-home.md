# MongoDB connections

You can use AWS Glue for Spark to read from and write to tables in MongoDB and MongoDB Atlas in AWS Glue 4.0 and
later versions. You can connect to MongoDB using username and password credentials credentials stored in
AWS Secrets Manager through a AWS Glue connection.

For more information about MongoDB, consult the [MongoDB documentation](https://www.mongodb.com/docs/ "https://www.mongodb.com/docs/").

## Configuring MongoDB connections

To connect to MongoDB from AWS Glue, you will need your MongoDB credentials, `mongodbUser` and `mongodbPass`.

To connect to MongoDB from AWS Glue, you may need some prerequisites:

- If your MongoDB instance is in an Amazon VPC, configure Amazon VPC to allow your AWS Glue job to communicate
  with the MongoDB instance without traffic traversing the public internet.

In Amazon VPC, identify or create a **VPC**, **Subnet** and
**Security group** that AWS Glue will use while executing the job. Additionally, you
need to ensure Amazon VPC is configured to permit network traffic between your MongoDB instance and this
location. Based on your network layout, this may require changes to security group rules, Network ACLs,
NAT Gateways and Peering connections.

You can then proceed to configure AWS Glue for use with MongoDB.

###### To configure a connection to MongoDB:

1. Optionally, in AWS Secrets Manager, create a secret using your MongoDB credentials.
   To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for
     the key `username` with the value `mongodbUser`.

   When selecting **Key/value pairs**, create a pair for
   the key `password` with the value `mongodbPass`.

2. In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
   - When selecting a **Connection type**, select **MongoDB** or **MongoDB Atlas**.
   - When selecting **MongoDB URL** or **MongoDB Atlas URL**, provide the hostname of your MongoDB instance.

   A MongoDB URL is provided in the format `mongodb://`mongoHost`:`mongoPort`/`mongoDBname``.

   A MongoDB Atlas URL is provided in the format `mongodb+srv://`mongoHost`:`mongoPort`/`mongoDBname``.

   Providing the default database for the connection, `mongoDBname` is optional.
   - If you chose to create an Secrets Manager secret, choose the AWS Secrets Manager **Credential type**.

   Then, in **AWS Secret** provide `secretName`.
   - If you choose to provide **Username and password**, provide
     `mongodbUser` and `mongodbPass`.

3. In the following situations, you may require additional configuration:
   - For MongoDB instances hosted on AWS in an Amazon VPC
     - You will need to provide Amazon VPC connection information to the AWS Glue connection that
       defines your MongoDB security credentials. When creating or updating your
       connection, set **VPC**, **Subnet** and
       **Security groups** in **Network options**.

After creating a AWS Glue MongoDB connection, you will need to perform the following actions before calling your connection method:

- If you chose to create an Secrets Manager secret, grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

To use your AWS Glue MongoDB connection in AWS Glue for Spark, provide the `connectionName` option in your connection
method call. Alternatively, you can follow the steps in [Working with MongoDB connections in ETL jobs](integrate-with-mongo-db.md "integrate-with-mongo-db.md") to use the
connection in conjunction with the AWS Glue Data Catalog.

## Reading from MongoDB using a AWS Glue connection

**Prerequisites:**

- A MongoDB collection you would like to read from. You will need identification information for the
  collection.

A MongoDB collection is identified by a database name and a collection name,
`mongodbName`, `mongodbCollection`.

- A AWS Glue MongoDB connection configured to provide auth information. Complete the steps in the previous procedure, _To configure a connection to MongoDB_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
mongodb_read = glueContext.create_dynamic_frame.from_options(
    connection_type="mongodb",
    connection_options={
        "connectionName": "`connectionName`",
        "database": "`mongodbName`",
        "collection": "`mongodbCollection`",
        "partitioner": "com.mongodb.spark.sql.connector.read.partitioner.SinglePartitionPartitioner",
        "partitionerOptions.partitionSizeMB": "10",
        "partitionerOptions.partitionKey": "_id",
        "disableUpdateUri": "false",
    }
)
```

## Writing to MongoDB tables

This example writes information from an existing DynamicFrame, `dynamicFrame` to
MongoDB.

**Prerequisites:**

- A MongoDB collection you would like to write to. You will need identification information for the
  collection.

A MongoDB collection is identified by a database name and a collection name,
`mongodbName`, `mongodbCollection`.

- A AWS Glue MongoDB connection configured to provide auth information. Complete the steps in the previous procedure, _To configure a connection to MongoDB_ to configure your auth
  information. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
glueContext.write_dynamic_frame.from_options(
    frame=`dynamicFrame`,
    connection_type="mongodb",
    connection_options={
        "connectionName": "`connectionName`",
        "database": "`mongodbName`",
        "collection": "`mongodbCollection`",
        "disableUpdateUri": "false",
        "retryWrites": "false",
    },
)
```

## Reading and writing to MongoDB tables

This example writes information from an existing DynamicFrame, `dynamicFrame` to
MongoDB.

**Prerequisites:**

- A MongoDB collection you would like to read from. You will need identification information for the collection.

A MongoDB collection you would like to write to. You will need identification information for the collection.

A MongoDB collection is identified by a database name and a collection name,
`mongodbName`, `mongodbCollection`.

- MongoDB auth information, `mongodbUser` and `mongodbPassword`.

For example:

Python

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
mongo_uri = "mongodb://<mongo-instanced-ip-address>:27017"
mongo_ssl_uri = "mongodb://<mongo-instanced-ip-address>:27017"
write_uri = "mongodb://<mongo-instanced-ip-address>:27017"

read_mongo_options = {
    "uri": mongo_uri,
    "database": "`mongodbName`",
    "collection": "`mongodbCollection`",
    "username": "`mongodbUsername`",
    "password": "`mongodbPassword`",
    "partitioner": "MongoSamplePartitioner",
    "partitionerOptions.partitionSizeMB": "10",
    "partitionerOptions.partitionKey": "_id"}

ssl_mongo_options = {
    "uri": mongo_ssl_uri,
    "database": "`mongodbName`",
    "collection": "`mongodbCollection`",
    "ssl": "true",
    "ssl.domain_match": "false"
}

write_mongo_options = {
    "uri": write_uri,
    "database": "`mongodbName`",
    "collection": "`mongodbCollection`",
    "username": "`mongodbUsername`",
    "password": "`mongodbPassword`",
}

# Get DynamicFrame from MongoDB
dynamic_frame = glueContext.create_dynamic_frame.from_options(connection_type="mongodb",
                                                              connection_options=read_mongo_options)

# Write DynamicFrame to MongoDB
glueContext.write_dynamic_frame.from_options(dynamicFrame, connection_type="mongodb", connection_options=write_mongo_options)

job.commit()
```

Scala

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
  val DEFAULT_URI: String = "mongodb://<mongo-instanced-ip-address>:27017"
  val WRITE_URI: String = "mongodb://<mongo-instanced-ip-address>:27017"
  lazy val defaultJsonOption = jsonOptions(DEFAULT_URI)
  lazy val writeJsonOption = jsonOptions(WRITE_URI)
  def main(sysArgs: Array[String]): Unit = {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)

    // Get DynamicFrame from MongoDB
    val dynamicFrame: DynamicFrame = glueContext.getSource("mongodb", defaultJsonOption).getDynamicFrame()

    // Write DynamicFrame to MongoDB
    glueContext.getSink("mongodb", writeJsonOption).writeDynamicFrame(dynamicFrame)

    Job.commit()
  }

  private def jsonOptions(uri: String): JsonOptions = {
    new JsonOptions(
      s"""{"uri": "${uri}",
         |"database":"`mongodbName`",
         |"collection":"`mongodbCollection`",
         |"username": "`mongodbUsername`",
         |"password": "`mongodbPassword`",
         |"ssl":"true",
         |"ssl.domain_match":"false",
         |"partitioner": "MongoSamplePartitioner",
         |"partitionerOptions.partitionSizeMB": "10",
         |"partitionerOptions.partitionKey": "_id"}""".stripMargin)
  }
}
```

## MongoDB connection option reference

Designates a connection to MongoDB. Connection options differ for a source connection and
a sink connection.

These connection properties are shared between source and sink connections:

- `connectionName` — Used for Read/Write. The name of a AWS Glue MongoDB connection
  configured to provide auth and networking information to your connection method. When a AWS Glue
  connection is configured as described in the previous section, [Configuring MongoDB connections](#aws-glue-programming-etl-connect-mongodb-configure "#aws-glue-programming-etl-connect-mongodb-configure"), providing
  `connectionName` will replace the need to provide the `"uri"`,
  `"username"` and `"password"` connection options.
- `"uri"`: (Required) The MongoDB host to read from, formatted as
  `mongodb://<host>:<port>`. Used in AWS Glue versions prior to AWS Glue 4.0.
- `"connection.uri"`: (Required) The MongoDB host to read from, formatted as
  `mongodb://<host>:<port>`. Used in AWS Glue 4.0 and later versions.
- `"username"`: (Required) The MongoDB user name.
- `"password"`: (Required) The MongoDB password.
- `"database"`: (Required) The MongoDB database to read from. This option
  can also be passed in `additional_options` when calling
  `glue_context.create_dynamic_frame_from_catalog` in your job script.
- `"collection"`: (Required) The MongoDB collection to read from. This
  option can also be passed in `additional_options` when calling
  `glue_context.create_dynamic_frame_from_catalog` in your job script.

### "connectionType": "mongodb" as

source

Use the following connection options with `"connectionType": "mongodb"` as a
source:

- `"ssl"`: (Optional) If `true`, initiates an SSL connection.
  The default is `false`.
- `"ssl.domain_match"`: (Optional) If `true` and
  `ssl` is `true`, domain match check is performed. The default is
  `true`.
- `"batchSize"`: (Optional): The number of documents to return per batch,
  used within the cursor of internal batches.
- `"partitioner"`: (Optional): The class name of the partitioner for
  reading input data from MongoDB. The connector provides the following
  partitioners:
  - `MongoDefaultPartitioner` (default) (Not supported in AWS Glue 4.0)
  - `MongoSamplePartitioner` (Requires MongoDB 3.2 or later) (Not supported in AWS Glue 4.0)
  - `MongoShardedPartitioner` (Not supported in AWS Glue 4.0)
  - `MongoSplitVectorPartitioner` (Not supported in AWS Glue 4.0)
  - `MongoPaginateByCountPartitioner` (Not supported in AWS Glue 4.0)
  - `MongoPaginateBySizePartitioner` (Not supported in AWS Glue 4.0)
  - `com.mongodb.spark.sql.connector.read.partitioner.SinglePartitionPartitioner`
  - `com.mongodb.spark.sql.connector.read.partitioner.ShardedPartitioner`
  - `com.mongodb.spark.sql.connector.read.partitioner.PaginateIntoPartitionsPartitioner`

- `"partitionerOptions"` (Optional): Options for the designated
  partitioner. The following options are supported for each partitioner:

      + `MongoSamplePartitioner`: `partitionKey`,
       `partitionSizeMB`, `samplesPerPartition`
      + `MongoShardedPartitioner`: `shardkey`
      + `MongoSplitVectorPartitioner`: `partitionKey`,
       `partitionSizeMB`
      + `MongoPaginateByCountPartitioner`: `partitionKey`,
       `numberOfPartitions`
      + `MongoPaginateBySizePartitioner`: `partitionKey`,
       `partitionSizeMB`

  For more information about these options, see [Partitioner Configuration](https://docs.mongodb.com/spark-connector/master/configuration/#partitioner-conf "https://docs.mongodb.com/spark-connector/master/configuration/#partitioner-conf") in the MongoDB documentation.

### "connectionType": "mongodb" as sink

Use the following connection options with `"connectionType": "mongodb"` as a
sink:

- `"ssl"`: (Optional) If `true`, initiates an SSL connection.
  The default is `false`.
- `"ssl.domain_match"`: (Optional) If `true` and
  `ssl` is `true`, domain match check is performed. The default is
  `true`.
- `"extendedBsonTypes"`: (Optional) If `true`, allows extended
  BSON types when writing data to MongoDB. The default is `true`.
- `"replaceDocument"`: (Optional) If `true`, replaces the whole
  document when saving datasets that contain an `_id` field. If
  `false`, only fields in the document that match the fields in the dataset
  are updated. The default is `true`.
- `"maxBatchSize"`: (Optional): The maximum batch size for bulk operations
  when saving data. The default is 512.
- `"retryWrites"`: (Optional): Automatically retry certain write operations a single
  time if AWS Glue encounters a network error.
