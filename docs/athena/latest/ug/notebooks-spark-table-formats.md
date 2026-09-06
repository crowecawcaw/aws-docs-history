

# Use non-Hive table formats in Athena for Spark
<a name="notebooks-spark-table-formats"></a>

**Note**  
This page refers to using Python libraries in the release version Pyspark engine version 3. Refer to [Amazon EMR 7.12](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-7120-release.html) for supported open table format versions.

When you work with sessions and notebooks in Athena for Spark, you can use Linux Foundation Delta Lake, Apache Hudi, and Apache Iceberg tables, in addition to Apache Hive tables.

## Considerations and limitations
<a name="notebooks-spark-table-formats-considerations-and-limitations"></a>

When you use table formats other than Apache Hive with Athena for Spark, consider the following points:
+ In addition to Apache Hive, only one table format is supported per notebook. To use multiple table formats in Athena for Spark, create a separate notebook for each table format. For information about creating notebooks in Athena for Spark, see [Step 7: Create your own notebook](notebooks-spark-getting-started.md#notebooks-spark-getting-started-creating-your-own-notebook).
+ The Delta Lake, Hudi, and Iceberg table formats have been tested on Athena for Spark by using AWS Glue as the metastore. You might be able to use other metastores, but such usage is not currently supported.
+ To use the additional table formats, override the default `spark_catalog` property, as indicated in the Athena console and in this documentation. These non-Hive catalogs can read Hive tables, in addition to their own table formats.

## Table versions
<a name="notebooks-spark-table-formats-versions"></a>

The following table shows supported non-Hive table versions in Amazon Athena for Apache Spark.



| Table format | Supported version | 
| --- | --- | 
| Apache Iceberg | 1.2.1 | 
| Apache Hudi | 0.13 | 
| Linux Foundation Delta Lake | 2.0.2 | 

In Athena for Spark, these table format `.jar` files and their dependencies are loaded onto the classpath for Spark drivers and executors.

For an *AWS Big Data Blog* post that shows how to work with Iceberg, Hudi, and Delta Lake table formats using Spark SQL in Amazon Athena notebooks, see [Use Amazon Athena with Spark SQL for your open-source transactional table formats](https://aws.amazon.com/blogs/big-data/use-amazon-athena-with-spark-sql-for-your-open-source-transactional-table-formats/).

**Topics**
+ [Considerations and limitations](#notebooks-spark-table-formats-considerations-and-limitations)
+ [Table versions](#notebooks-spark-table-formats-versions)
+ [Iceberg](notebooks-spark-table-formats-apache-iceberg.md)
+ [Hudi](notebooks-spark-table-formats-apache-hudi.md)
+ [Delta Lake](notebooks-spark-table-formats-linux-foundation-delta-lake.md)