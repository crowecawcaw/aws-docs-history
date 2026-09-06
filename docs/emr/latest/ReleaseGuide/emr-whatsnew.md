

# What's new?
<a name="emr-whatsnew"></a>

This page describes the changes and functionality available in the latest releases of Amazon EMR 7.x, 6.x, and 5.x. 

These release notes are also available on the [Amazon EMR 7.13.0](emr-7130-release.md), [Amazon EMR 6.15.0](emr-6150-release.md), and [Amazon EMR 5.36.2](emr-5362-release.md) pages, along with the application versions, component versions, and available configuration classifications for each release.
+ For release notes from prior releases, see the [Amazon EMR archive of release notes](emr-whatsnew-history.md).
+ To get updates when a new Amazon EMR release is available, subscribe to the [RSS feed for Amazon EMR release notes](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/amazon-emr-release-notes.rss).

**Note**  
Later releases of Amazon EMR use AWS Signature Version 4 (SigV4) to authenticate requests to Amazon S3. We recommend that you use an Amazon EMR release that supports SigV4 so that you can access new S3 buckets and avoid interruption to your workloads. For more information and a list of Amazon EMR releases that support SigV4, see [Amazon EMR and AWS Signature Version 4](#emr-sigv4).

## Apache Spark Upgrade and Troubleshooting Agents
<a name="emr-spark-agents-whatsnew"></a>

**Apache Spark Upgrade Agent**

The Apache Spark Upgrade Agent for Amazon EMR is a conversational AI capability that accelerates Apache Spark version upgrades for your EMR applications. Traditional Spark upgrades require months of engineering effort to analyze API changes, resolve dependency conflicts, and validate functional correctness. The agent simplifies the upgrade process through natural language prompts, automated code transformation, and data quality validation.

You can use the agent to upgrade PySpark and Scala applications running on Amazon EMR on EC2 and Amazon EMR Serverless. The agent analyzes your code, identifies required changes, and performs automated transformations while maintaining your approval control over all modifications. For more details refer to [What is Apache Spark Upgrade Agent for Amazon EMR](spark-upgrades.md).

**Apache Spark Troubleshooting Agent**

The Apache Spark troubleshooting agent for Amazon EMR is a conversational AI capability that simplifies the troubleshooting of Apache Spark applications on Amazon EMR, AWS Glue and Amazon SageMaker Notebooks. Traditional Spark troubleshooting requires extensive manual analysis of logs, performance metrics, and error patterns to identify root causes and code fixes. The agent simplifies this process through natural language prompts, automated workload analysis, and intelligent code recommendations.

You can use the agent to troubleshoot PySpark and Scala applications failures. The agent analyzes your failed jobs, identifies performance bottlenecks, and provides actionable recommendations and code fixes while giving you full control over implementation decisions. For more details refer to [What is Apache Spark Troubleshooting Agent for Amazon EMR and AWS Glue](spark-troubleshoot.md).

## Amazon EMR 7.13.0 (latest release of 7.x series)
<a name="emr-7130-whatsnew"></a>

New Amazon EMR releases are made available in different Regions over a period of several days, beginning with the first Region on the initial release date. The latest release version may not be available in your Region during this period.

The following release notes include information for Amazon EMR release 7.13.0.

### What's new
<a name="emr-7130-whatsnew"></a>
+ **Python 3.11 default for PySpark and Spark workloads** — Python 3.11 is now the default Python version for PySpark and Spark workloads. Python 3.9 remains the default for all other applications. Both Python 3.9 and 3.11 are included in the release.

### Changes, enhancements, and resolved issues
<a name="emr-7130-changes"></a>
+ **Iceberg configuration property** — Amazon EMR 7.13 adds a new Iceberg configuration property, `spark.sql.catalog.spark_catalog.route-non-iceberg-drop-to-session-catalog`. When set to `true`, `DROP TABLE` on non-Iceberg managed tables in `SparkSessionCatalog` deletes both the table metadata and the underlying Amazon S3 data. The default value is `false`.

### Application upgrades
<a name="emr-7130-app-upgrades"></a>

The following applications are upgraded in this release:
+ HBase 2.6.4-amzn-0 (upgraded from 2.6.2-amzn-3)
+ Hadoop 3.4.2-amzn-0 (upgraded from 3.4.1-amzn-4)
+ Phoenix 5.3.0 (upgraded from 5.2.1)
+ Hudi 1.0.2-amzn-2 (upgraded from 1.0.2-amzn-1)
+ Trino 479-amzn-1 (upgraded from 476-amzn-1)
+ AWS SDK v2 2.42.12 (upgraded from 2.35.5)
+ AWS SDK v1 1.12.797 (upgraded from 1.12.792)
+ Spark 3.5.6-amzn-2, Hive 3.1.3-amzn-22, Tez 0.10.2-amzn-20, Presto 0.287-amzn-7, Iceberg 1.10.0-amzn-1, Delta 3.3.2-amzn-2, Flink 1.20.0-amzn-7, ZooKeeper 3.9.3-amzn-5 (amzn patch bumps)

### Known issues and limitations
<a name="emr-7130-known-issues"></a>
+ Configuring `yarn.nodemanager.log-dirs` with a value of length longer than 512 characters will cause S3 log upload to fail.
+ The following table lists the Amazon Linux release labels, kernel versions, available dates, and supported AWS Regions.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html)

## Amazon EMR 6.15.0 (latest release of 6.x series)
<a name="emr-6150-whatsnew"></a>

New Amazon EMR releases are made available in different Regions over a period of several days, beginning with the first Region on the initial release date. The latest release version may not be available in your Region during this period.

The following release notes include information for Amazon EMR release 6.15.0. Changes are relative to 6.14.0. For information on the release timeline, see the [6.15.0 change log](emr-6150-release.md#6150-changelog).

**New features**
+ **Application upgrades** – Amazon EMR 6.15.0 application upgrades include Apache Hadoop 3.3.6, Apache Hudi 0.14.0-amzn-0, Iceberg 1.4.0-amzn-0, and Trino 426.
+ **[Faster launches for EMR clusters that run on EC2](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-emr-ec2-clusters-5-minutes-less/)** – It's now up to 35% faster to launch an Amazon EMR on EC2 cluster. With this improvement, most customers can launch their clusters in 5 minutes or less.
+ **[CodeWhisperer for EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-codewhisperer.html)** – You can now use Amazon CodeWhisperer with Amazon EMR Studio to get real-time recommendations as you write code in JupyterLab. CodeWhisperer can complete your comments, finish single lines of code, make line-by-line recommendations, and generate fully-formed functions.
+ **[Faster job restart times with Flink](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/flink-restart.html)** – With Amazon EMR 6.15.0 and higher, several new mechanisms are available for Apache Flink to improve the job restart time during task recovery or scaling operations. This optimizes the speed of recovery and restart of execution graphs to improve job stability.
+ **[Table-level and fine-grained access control for open-table formats](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-lf-enable.html)** – With Amazon EMR 6.15.0 and higher, when you run Spark jobs on Amazon EMR on EC2 clusters that access data in the AWS Glue Data Catalog, you can use AWS Lake Formation to apply table, row, column, and cell level permissions on Hudi, Iceberg, or Delta Lake based tables.
+ **Hadoop upgrade** – Amazon EMR 6.15.0 includes an upgrade of Apache Hadoop to version 3.3.6. Hadoop 3.3.6 was the latest version at the time of the Amazon EMR 6.15 deployment, released by Apache in June 2023. Prior releases of Amazon EMR (6.9.0 to 6.14.x) used Hadoop 3.3.3.

  The upgrade includes hundreds of improvements and fixes, and features that include reconfigurable datanode parameters, `DFSAdmin` option to initiate bulk reconfiguration operations on all live datanodes, and a vectored API that allows seek-heavy readers to specify multiple ranges to read. Hadoop 3.3.6 also adds support for HDFS APIs and semantics for its write-ahead log (WAL), so that HBase can run on other storage system implementations. For more information, see the changelogs for versions [3.3.4](https://hadoop.apache.org/docs/r3.3.4/hadoop-project-dist/hadoop-common/release/3.3.4/CHANGELOG.3.3.4.html), [3.3.5](https://hadoop.apache.org/docs/r3.3.5/hadoop-project-dist/hadoop-common/release/3.3.5/CHANGELOG.3.3.5.html), and [3.3.6](https://hadoop.apache.org/docs/r3.3.6/hadoop-project-dist/hadoop-common/release/3.3.6/CHANGELOG.3.3.6.html) in the *Apache Hadoop documentation*.
+ **Support for AWS SDK for Java, version 2** - Amazon EMR 6.15.0 applications can use AWS SDK for Java versions [1.12.569](https://github.com/aws/aws-sdk-java/tree/1.12.569) or [2.20.160](https://github.com/aws/aws-sdk-java-v2/tree/2.20.160) if the application supports v2. The AWS SDK for Java 2.x is a major rewrite of the version 1.x code base. It’s built on top of Java 8\+ and adds several frequently requested features. These include support for non-blocking I/O, and the ability to plug in a different HTTP implementation at runtime. For more information, including a **Migration Guide from SDK for Java v1 to v2**, see the [AWS SDK for Java, version 2](https://docs.aws.amazon.com/sdk-for-java) guide.

**Known issues**
+ An on-cluster instance-state script that monitors health of the instance can consume excessive CPU and memory resources when there are a large number of threads and/or open file handles on the node.

**Changes, enhancements, and resolved issues**
+  Starting with Spark 3.3.1 (supported in EMR versions 6.10 and above), all executors in a decommissioning host are set to a new `ExecutorState`, called *DECOMMISSIONING* state. The executors being decommissioned cannot be used by Yarn to allocate tasks and thus it will request for new executors, if needed, for the tasks being executed. Thus, if you disable Spark DRA while using EMR Managed Scaling, EMR Auto Scaling, or any custom scaling mechanism on EMR-EC2 clusters, then Yarn may request maximum permissible executors for each job. In order to avoid this issue, leave the `spark.dynamicAllocation.enabled` property set to `TRUE` (which is the default) when you are using the above combination of features. In addition, you can also set minimum and maximum executor constraints by setting values for `spark.dynamicAllocation.maxExecutors` and `spark.dynamicAllocation.minExecutors` properties for your Spark jobs, to restrict the number of executors allocated during the job’s execution. 
+ To improve your high-availability EMR clusters, this release enables connectivity to Amazon EMR daemons on local host that use IPv6 endpoints.
+ This release enables TLS 1.2 for communication with ZooKeeper provisioned on all the primary nodes of your high-availability cluster.
+ This release improves the management of ZooKeeper transaction log files that are maintained on primary nodes to minimize scenarios where the log files grow out of bounds and interrupt cluster operations.
+ This release makes intra-node communication more resilient for high-availability EMR clusters. This improvement reduces the chance of bootstrap action failures or cluster start failures.
+ Tez in Amazon EMR 6.15.0 introduces configurations that you can specify to asynchronously open the input splits in a Tez grouped split. This results in faster performance of read queries when there are a large number of input splits in a single Tez grouped split. For more information, see [Tez asynchronous split opening](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/tez-configure.html#tez-configure-async).
+ When you launch a cluster with *the latest patch release* of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-default-ami.html).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html)

## Amazon EMR 5.36.2 (latest release of 5.x series)
<a name="emr-5362-whatsnew"></a>

New Amazon EMR releases are made available in different Regions over a period of several days, beginning with the first Region on the initial release date. The latest release version may not be available in your Region during this period.

The following release notes include information for Amazon EMR release 5.36.2. Changes are relative to 5.36.1. For information on the release timeline, see the [change log](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-5362-release.html#5362-changelog).

**Changes, enhancements, and resolved issues**
+ This releases improves cluster scale-down logic so that Amazon EMR doesn't scale-down core nodes below the HDFS replication factor setting for the cluster. This improvement fulfills data redundancy requirements, and reduces the chance that a scaling operation might stall. 
+ This release adds a new retry mechanism to the cluster scaling workflow for EMR clusters that run Presto or Trino. This improvement reduces the risk that cluster resize runs indefinitely due to a single failed resize operation. It also improves cluster utilization, because your cluster scales up and down faster.
+ Fixes an issue where cluster scale-down operations might stall while Amazon EMR gracefully decommissions a core node and it turns unhealthy before it is fully decommissioned.
+ Improves the stability of a node in a high-availability cluster with multiple primary nodes when Amazon EMR restarts a single node.
+ Optimizes log management with Amazon EMR running on Amazon EC2. As a result, you might see a slight reduction in storage costs for your cluster logs.
+ Improves the management of ZooKeeper transaction log files that are maintained on primary nodes to minimize scenarios where the log files grow out of bounds and interrupt cluster operations.
+ Fixes a rare bug which can cause a high-availability cluster with multiple primary nodes to fail due to not being able to communicate with the Yarn ResourceManager.
+ When you launch a cluster with *the latest patch release* of Amazon EMR 5.36 or higher, 6.6 or higher, or 7.0 or higher, Amazon EMR uses the latest Amazon Linux 2023 or Amazon Linux 2 release for the default Amazon EMR AMI. For more information, see [Using the default Amazon Linux AMI for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-default-ami.html).    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-whatsnew.html)

## Amazon EMR and AWS Signature Version 4
<a name="emr-sigv4"></a>

Amazon EMR releases use AWS Signature Version 4 (SigV4) to authenticate requests to Amazon S3. Buckets created in Amazon S3 after June 24, 2020 don't support requests signed by Signature Version 2 (SigV2). Buckets created on or before June 24, 2020 will continue to support SigV2. We recommend that you migrate to an Amazon EMR release that supports SigV4 so that you can access new S3 buckets and avoid interruption to your workloads. 

If you use applications that are included with Amazon EMR such as Apache Spark, Apache Hive, and Presto, you don't need to change your application code to use SigV4 . If you use custom applications that are not included with Amazon EMR, you might need to update your code to use SigV4. For more information, see [Moving from Signature Version 2 to Signature Version 4](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingAWSSDK.html#UsingAWSSDK-move-to-Sig4) in the Amazon S3 User Guide.

The following Amazon EMR releases support SigV4: emr-4.7.4, emr-4.8.5, emr-4.9.6, emr-4.10.1, emr-5.1.1, emr-5.2.3, emr-5.3.2, emr-5.4.1, emr-5.5.4, emr-5.6.1, emr-5.7.1, emr-5.8.3, emr-5.9.1, emr-5.10.1, emr-5.11.4, emr-5.12.3, emr-5.13.1, emr-5.14.2, emr-5.15.1, emr-5.16.1, emr-5.17.2, emr-5.18.1, emr-5.19.1, emr-5.20.1, emr-5.21.2, and emr-5.22.0 and higher. All 6.x and 7.x releases support SigV4.