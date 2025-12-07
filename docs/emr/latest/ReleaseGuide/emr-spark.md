# Apache Spark

[Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/") is a distributed processing framework and programming model that helps
you do machine learning, stream processing, or graph analytics with Amazon EMR clusters. Similar
to Apache Hadoop, Spark is an open-source, distributed processing system commonly used for
big data workloads. However, Spark has several notable differences from Hadoop MapReduce.
Spark has an optimized directed acyclic graph (DAG) execution engine and actively caches
data in-memory, which can boost performance, especially for certain algorithms and
interactive queries.

Spark natively supports applications written in Scala, Python, and Java. It also includes
several tightly integrated libraries for SQL ([Spark](https://spark.apache.org/sql/ "https://spark.apache.org/sql/")), machine learning ([MLlib](https://spark.apache.org/mllib/ "https://spark.apache.org/mllib/")), stream processing ([Spark streaming](https://spark.apache.org/streaming/ "https://spark.apache.org/streaming/")), and graph processing ([GraphX](https://spark.apache.org/graphx/ "https://spark.apache.org/graphx/")). These tools make it easier to
leverage the Spark framework for a wide variety of use cases.

You can install Spark on an Amazon EMR cluster along with other Hadoop applications, and it can
also leverage the Amazon EMR file system (EMRFS) to directly access data in Amazon S3. Hive is also
integrated with Spark so that you can use a HiveContext object to run Hive scripts using
Spark. A Hive context is included in the spark-shell as `sqlContext`.

For an example tutorial on setting up an EMR cluster with Spark and analyzing a sample
data set, see [Tutorial: Getting started with Amazon EMR](../ManagementGuide/emr-gs.md "../ManagementGuide/emr-gs.md") on the AWS News blog.

You can use Apache Spark Troubleshooting Agent to troubleshoot your Apache Spark applications on EMR on EC2 and EMR Serverless. To learn more, please refer to [What is Apache Spark Troubleshooting Agent for Amazon EMR](spark-troubleshoot.md "spark-troubleshoot.md").

###### Important

Apache Spark version 2.3.1, available beginning with Amazon EMR release 5.16.0, addresses [CVE-2018-8024](https://nvd.nist.gov/vuln/detail/CVE-2018-8024 "https://nvd.nist.gov/vuln/detail/CVE-2018-8024") and [CVE-2018-1334](https://nvd.nist.gov/vuln/detail/CVE-2018-1334 "https://nvd.nist.gov/vuln/detail/CVE-2018-1334"). We recommend that you migrate earlier versions of Spark to Spark version 2.3.1 or later.

The following table lists the version of Spark included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Spark.

For the version of components installed with Spark in this release, see [Release 7.12.0 Component Versions](emr-7120-release.md "emr-7120-release.md").

| Spark version information for emr-7.12.0 | Amazon EMR Release Label | Spark Version                                                                                                                                                                                                                                                                                                                                                                                          | Components Installed With Spark |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| emr-7.12.0                               | Spark 3.5.6-amzn-1       | delta, emrfs, emr-goodies, emr-ddb, emr-s3-select, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hudi, hudi-spark, iceberg, livy-server, nginx, r, spark-client, spark-history-server, spark-on-yarn, spark-yarn-slave |

The following table lists the version of Spark included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Spark.

For the version of components installed with Spark in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Spark version information for emr-6.15.0 | Amazon EMR Release Label | Spark Version                                                                                                                                                                                                                                                                                                                                                                                                 | Components Installed With Spark |
| ---------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| emr-6.15.0                               | Spark 3.4.1-amzn-2       | aws-sagemaker-spark-sdk, delta, emrfs, emr-goodies, emr-ddb, emr-s3-select, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hudi, hudi-spark, iceberg, livy-server, nginx, r, spark-client, spark-history-server, spark-on-yarn, spark-yarn-slave |

###### Note

Amazon EMR release 6.8.0 comes with Apache Spark 3.3.0. This Spark release uses Apache Log4j 2 and the `log4j2.properties` file to configure Log4j in Spark processes. If you use Spark in the cluster or create EMR clusters with custom configuration parameters, and you want to upgrade to Amazon EMR release 6.8.0, you must migrate to the new `spark-log4j2` configuration classification and key format for Apache Log4j 2. For more information, see [Migrating from Apache Log4j 1.x to Log4j
2.x](emr-spark-configure.md#spark-migrate-logj42 "emr-spark-configure.md#spark-migrate-logj42").

The following table lists the version of Spark included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Spark.

For the version of components installed with Spark in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Spark version information for emr-5.36.2 | Amazon EMR Release Label | Spark Version                                                                                                                                                                                                                                                                                                                                                                                 | Components Installed With Spark |
| ---------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| emr-5.36.2                               | Spark 2.4.8-amzn-2       | aws-sagemaker-spark-sdk, emrfs, emr-goodies, emr-ddb, emr-s3-select, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hudi, hudi-spark, livy-server, nginx, r, spark-client, spark-history-server, spark-on-yarn, spark-yarn-slave |

###### Topics

- [Create a cluster with Apache Spark](emr-spark-launch.md "emr-spark-launch.md")
- [Run Spark applications with Docker on Amazon EMR
  6.x](emr-spark-docker.md "emr-spark-docker.md")
- [Use AWS Glue Data Catalog catalog with Spark on Amazon EMR](emr-spark-glue.md "emr-spark-glue.md")
- [Working with a multi-catalog hierarchy in
  AWS Glue Data Catalog with Spark on Amazon EMR](emr-multi-catalog.md "emr-multi-catalog.md")
- [Configure Spark](emr-spark-configure.md "emr-spark-configure.md")
- [What is Apache Spark Troubleshooting Agent for Amazon EMR](spark-troubleshoot.md "spark-troubleshoot.md")
- [Optimize Spark performance](emr-spark-performance.md "emr-spark-performance.md")
- [Spark Result Fragment
  Caching](emr-spark-fragment-result-caching.md "emr-spark-fragment-result-caching.md")
- [Use the Nvidia RAPIDS Accelerator for Apache
  Spark](emr-spark-rapids.md "emr-spark-rapids.md")
- [Access the Spark shell](emr-spark-shell.md "emr-spark-shell.md")
- [Use Amazon SageMaker Spark for machine learning](emr-spark-sagemaker.md "emr-spark-sagemaker.md")
- [Write a Spark application](emr-spark-application.md "emr-spark-application.md")
- [Improve Spark performance with Amazon S3](emr-spark-s3-performance.md "emr-spark-s3-performance.md")
- [Add a Spark step](emr-spark-submit-step.md "emr-spark-submit-step.md")
- [View Spark application history](emr-spark-application-history.md "emr-spark-application-history.md")
- [Access the Spark web UIs](emr-spark-webui.md "emr-spark-webui.md")
- [Using the Spark structured
  streaming Amazon Kinesis Data Streams connector](emr-spark-structured-streaming-kinesis.md "emr-spark-structured-streaming-kinesis.md")
- [Using Amazon Redshift integration for Apache Spark with Amazon EMR](emr-spark-redshift.md "emr-spark-redshift.md")
- [Spark release history](Spark-release-history.md "Spark-release-history.md")
- [Using materialized views with
  Amazon EMR](emr-spark-materialized-views.md "emr-spark-materialized-views.md")
