# Connecting to DynamoDB with

Amazon EMR Serverless

In this tutorial, you upload a subset of data from the [United States Board on
Geographic Names](https://www.usgs.gov/us-board-on-geographic-names "https://www.usgs.gov/us-board-on-geographic-names") to an Amazon S3 bucket and then use Hive or Spark on
Amazon EMR Serverless to copy the data to an Amazon DynamoDB table for querying.

## Step 1: Upload data to an Amazon S3

bucket

To create an Amazon S3 bucket, follow the instructions in [Creating a bucket](../../../AmazonS3/latest/user-guide/create-bucket.md "../../../AmazonS3/latest/user-guide/create-bucket.md") in
the _Amazon Simple Storage Service Console User Guide_. Replace references to
`amzn-s3-demo-bucket` with the name of
your newly created bucket. Now your EMR Serverless application is ready to run
jobs.

1. Download the sample data archive `features.zip` with the
   following command.

```
wget https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/samples/features.zip
```

2. Extract the `features.txt` file from the archive and access the
   first the few lines in the file:

```
unzip features.zip
head features.txt
```

The result should appear similar to the following.

```
1535908|Big Run|Stream|WV|38.6370428|-80.8595469|794
875609|Constable Hook|Cape|NJ|40.657881|-74.0990309|7
1217998|Gooseberry Island|Island|RI|41.4534361|-71.3253284|10
26603|Boone Moore Spring|Spring|AZ|34.0895692|-111.410065|3681
1506738|Missouri Flat|Flat|WA|46.7634987|-117.0346113|2605
1181348|Minnow Run|Stream|PA|40.0820178|-79.3800349|1558
1288759|Hunting Creek|Stream|TN|36.343969|-83.8029682|1024
533060|Big Charles Bayou|Bay|LA|29.6046517|-91.9828654|0
829689|Greenwood Creek|Stream|NE|41.596086|-103.0499296|3671
541692|Button Willow Island|Island|LA|31.9579389|-93.0648847|98
```

The fields in each line here indicate a unique identifier, name, type of
natural feature, state, latitude in degrees, longitude in degrees, and
height in feet. 3. Upload your data to Amazon S3

```
aws s3 cp features.txt s3://`amzn-s3-demo-bucket`/features/
```

## Step 2: Create a Hive

table

Use Apache Spark or Hive to create a new Hive table that contains the uploaded
data in Amazon S3.

Spark
To create a Hive table with Spark, run the following command.

```
import org.apache.spark.sql.SparkSession

val sparkSession = SparkSession.builder().enableHiveSupport().getOrCreate()

sparkSession.sql("CREATE TABLE `hive_features` \
    (feature_id BIGINT, \
    feature_name STRING, \
    feature_class STRING, \
    state_alpha STRING, \
    prim_lat_dec DOUBLE, \
    prim_long_dec DOUBLE, \
    elev_in_ft BIGINT) \
    ROW FORMAT DELIMITED \
    FIELDS TERMINATED BY '|' \
    LINES TERMINATED BY '\n' \
    LOCATION 's3://`amzn-s3-demo-bucket`/features';")
```

You now have a populated Hive table with data from the
`features.txt` file. To verify that your data is in the
table, run a Spark SQL query as shown in the following example.

```
sparkSession.sql(
    "SELECT state_alpha, COUNT(*) FROM `hive_features` GROUP BY state_alpha;")
```

Hive
To create a Hive table with Hive, run the following command.

```
CREATE TABLE `hive_features`
    (feature_id             BIGINT,
    feature_name            STRING ,
    feature_class           STRING ,
    state_alpha             STRING,
    prim_lat_dec            DOUBLE ,
    prim_long_dec           DOUBLE ,
    elev_in_ft              BIGINT)
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY '|'
    LINES TERMINATED BY '\n'
    LOCATION 's3://`amzn-s3-demo-bucket`/features';
```

You now have a Hive table that contains data from the
`features.txt` file. To verify that your data is in the
table, run a HiveQL query, as shown in the following example.

```
SELECT state_alpha, COUNT(*) FROM `hive_features` GROUP BY state_alpha;
```

## Step 3: Copy data to DynamoDB

Use Spark or Hive to copy data to a new DynamoDB table.

Spark
To copy data from the Hive table that you created in the previous step
to DynamoDB, follow **Steps 1-3** in [Copy data to DynamoDB](../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.md "../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.md"). This creates a new DynamoDB table called
`Features`. You can then read data directly from the text
file and copy it to your DynamoDB table, as the following example
shows.

```
import com.amazonaws.services.dynamodbv2.model.AttributeValue
import org.apache.hadoop.dynamodb.DynamoDBItemWritable
import org.apache.hadoop.dynamodb.read.DynamoDBInputFormat
import org.apache.hadoop.io.Text
import org.apache.hadoop.mapred.JobConf
import org.apache.spark.SparkContext

import scala.collection.JavaConverters._

object EmrServerlessDynamoDbTest {

    def main(args: Array[String]): Unit = {

        jobConf.set("dynamodb.input.tableName", "Features")
        jobConf.set("dynamodb.output.tableName", "Features")
        jobConf.set("dynamodb.region", "`region`")

        jobConf.set("mapred.output.format.class", "org.apache.hadoop.dynamodb.write.DynamoDBOutputFormat")
        jobConf.set("mapred.input.format.class", "org.apache.hadoop.dynamodb.read.DynamoDBInputFormat")

        val rdd = sc.textFile("s3://`amzn-s3-demo-bucket`/ddb-connector/")
            .map(row => {
                val line = row.split("\\|")
                val item = new DynamoDBItemWritable()

                val elevInFt = if (line.length > 6) {
                    new AttributeValue().withN(line(6))
                } else {
                    new AttributeValue().withNULL(true)
                }

                item.setItem(Map(
                    "feature_id" -> new AttributeValue().withN(line(0)),
                    "feature_name" -> new AttributeValue(line(1)),
                    "feature_class" -> new AttributeValue(line(2)),
                    "state_alpha" -> new AttributeValue(line(3)),
                    "prim_lat_dec" -> new AttributeValue().withN(line(4)),
                    "prim_long_dec" -> new AttributeValue().withN(line(5)),
                    "elev_in_ft" -> elevInFt)
                    .asJava)
                (new Text(""), item)
        })
        rdd.saveAsHadoopDataset(jobConf)
    }
}
```

Hive
To copy data from the Hive table that you created in the previous step
to DynamoDB, follow the instructions in [Copy data to DynamoDB](../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.md "../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.md").

## Step 4: Query data from DynamoDB

Use Spark or Hive to query your DynamoDB table.

Spark
To query data from the DynamoDB table that you created in the previous
step, use either Spark SQL or the Spark MapReduce API.

###### Example – Query your DynamoDB table with Spark SQL

The following Spark SQL query returns a list of all the feature
types in alphabetical order.

```
val dataFrame = sparkSession.sql("SELECT DISTINCT feature_class \
    FROM ddb_features \
    ORDER BY feature_class;")
```

The following Spark SQL query returns a list of all lakes that
begin with the letter _M_.

```
val dataFrame = sparkSession.sql("SELECT feature_name, state_alpha \
    FROM ddb_features \
    WHERE feature_class = 'Lake' \
    AND feature_name LIKE 'M%' \
    ORDER BY feature_name;")
```

The following Spark SQL query returns a list of all states with at
least three features that are higher than one mile.

```
val dataFrame = sparkSession.dql("SELECT state_alpha, feature_class, COUNT(*) \
    FROM ddb_features \
    WHERE elev_in_ft > 5280 \
    GROUP by state_alpha, feature_class \
    HAVING COUNT(*) >= 3 \
    ORDER BY state_alpha, feature_class;")
```

###### Example – Query your DynamoDB table with the Spark MapReduce

API

The following MapReduce query returns a list of all the feature
types in alphabetical order.

```
val df = sc.hadoopRDD(jobConf, classOf[DynamoDBInputFormat], classOf[Text], classOf[DynamoDBItemWritable])
    .map(pair => (pair._1, pair._2.getItem))
    .map(pair => pair._2.get("feature_class").getS)
    .distinct()
    .sortBy(value => value)
    .toDF("feature_class")
```

The following MapReduce query returns a list of all lakes that
begin with the letter _M_.

```
val df = sc.hadoopRDD(jobConf, classOf[DynamoDBInputFormat], classOf[Text], classOf[DynamoDBItemWritable])
    .map(pair => (pair._1, pair._2.getItem))
    .filter(pair => "Lake".equals(pair._2.get("feature_class").getS))
    .filter(pair => pair._2.get("feature_name").getS.startsWith("M"))
    .map(pair => (pair._2.get("feature_name").getS, pair._2.get("state_alpha").getS))
    .sortBy(_._1)
    .toDF("feature_name", "state_alpha")
```

The following MapReduce query returns a list of all states with at
least three features that are higher than one mile.

```
val df = sc.hadoopRDD(jobConf, classOf[DynamoDBInputFormat], classOf[Text], classOf[DynamoDBItemWritable])
    .map(pair => pair._2.getItem)
    .filter(pair => pair.get("elev_in_ft").getN != null)
    .filter(pair => Integer.parseInt(pair.get("elev_in_ft").getN) > 5280)
    .groupBy(pair => (pair.get("state_alpha").getS, pair.get("feature_class").getS))
    .filter(pair => pair._2.size >= 3)
    .map(pair => (pair._1._1, pair._1._2, pair._2.size))
    .sortBy(pair => (pair._1, pair._2))
    .toDF("state_alpha", "feature_class", "count")
```

Hive
To query data from the DynamoDB table that you created in the previous
step, follow the instructions in [Query the data in the DynamoDB table](../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.md "../../../amazondynamodb/latest/developerguide/EMRforDynamoDB.Tutorial.md").
