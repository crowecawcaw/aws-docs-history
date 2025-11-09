# Amazon EMR release 6.4.0

## 6.4.0 application versions

This release includes the following applications: [Flink](https://flink.apache.org/ "https://flink.apache.org/"), [Ganglia](http://ganglia.info "http://ganglia.info"), [HBase](http://hbase.apache.org/ "http://hbase.apache.org/"), [HCatalog](https://cwiki.apache.org/confluence/display/Hive/HCatalog "https://cwiki.apache.org/confluence/display/Hive/HCatalog"), [Hadoop](http://hadoop.apache.org/docs/current/ "http://hadoop.apache.org/docs/current/"), [Hive](http://hive.apache.org/ "http://hive.apache.org/"), [Hudi](https://hudi.apache.org "https://hudi.apache.org"), [Hue](http://gethue.com/ "http://gethue.com/"), [JupyterEnterpriseGateway](https://jupyter-enterprise-gateway.readthedocs.io/en/latest/ "https://jupyter-enterprise-gateway.readthedocs.io/en/latest/"), [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/# "https://jupyterhub.readthedocs.io/en/latest/#"), [Livy](https://livy.incubator.apache.org/ "https://livy.incubator.apache.org/"), [MXNet](https://mxnet.incubator.apache.org/ "https://mxnet.incubator.apache.org/"), [Oozie](http://oozie.apache.org/ "http://oozie.apache.org/"), [Phoenix](https://phoenix.apache.org/ "https://phoenix.apache.org/"), [Pig](http://pig.apache.org/ "http://pig.apache.org/"), [Presto](https://prestodb.io/ "https://prestodb.io/"), [Spark](https://spark.apache.org/docs/latest/ "https://spark.apache.org/docs/latest/"), [Sqoop](http://sqoop.apache.org/ "http://sqoop.apache.org/"), [TensorFlow](https://www.tensorflow.org/ "https://www.tensorflow.org/"), [Tez](https://tez.apache.org/ "https://tez.apache.org/"), [Trino (PrestoSQL)](https://trino.io/ "https://trino.io/"), [Zeppelin](https://zeppelin.incubator.apache.org/ "https://zeppelin.incubator.apache.org/"), and [ZooKeeper](https://zookeeper.apache.org "https://zookeeper.apache.org").

The table below lists the application versions available in this release of Amazon EMR and the application versions in the preceding three Amazon EMR releases (when applicable).

For a comprehensive history of application versions for each release of Amazon EMR, see the following topics:

- [Application versions in Amazon EMR 7.x
  releases](emr-release-app-versions-7.md "emr-release-app-versions-7.md")
- [Application versions in Amazon EMR 6.x releases](emr-release-app-versions-6.md "emr-release-app-versions-6.md")
- [Application versions in Amazon EMR 5.x releases](emr-release-app-versions-5.md "emr-release-app-versions-5.md")
- [Application versions in Amazon EMR 4.x releases](emr-release-app-versions-4.md "emr-release-app-versions-4.md")

| Application version information |                  | emr-6.4.0        | emr-6.3.1        | emr-6.3.0        | emr-6.2.1 |
| ------------------------------- | ---------------- | ---------------- | ---------------- | ---------------- | --------- |
| AWS SDK for Java                | 1.12.31          | 1.11.977         | 1.11.977         | 1.11.880         |
| Python                          | 2.7, 3.7         | 2.7, 3.7         | 2.7, 3.7         | 2.7, 3.7         |
| Scala                           | 2.12.10          | 2.12.10          | 2.12.10          | 2.12.10          |
| AmazonCloudWatchAgent           | -                | -                | -                | -                |
| Delta                           | -                | -                | -                | -                |
| Flink                           | 1.13.1           | 1.12.1           | 1.12.1           | 1.11.2           |
| Ganglia                         | 3.7.2            | 3.7.2            | 3.7.2            | 3.7.2            |
| HBase                           | 2.4.4-amzn-0     | 2.2.6-amzn-1     | 2.2.6-amzn-1     | 2.2.6-amzn-0     |
| HCatalog                        | 3.1.2-amzn-5     | 3.1.2-amzn-4     | 3.1.2-amzn-4     | 3.1.2-amzn-3     |
| Hadoop                          | 3.2.1-amzn-4     | 3.2.1-amzn-3.1   | 3.2.1-amzn-3     | 3.2.1-amzn-2.1   |
| Hive                            | 3.1.2-amzn-5     | 3.1.2-amzn-4     | 3.1.2-amzn-4     | 3.1.2-amzn-3     |
| Hudi                            | 0.8.0-amzn-0     | 0.7.0-amzn-0     | 0.7.0-amzn-0     | 0.6.0-amzn-1     |
| Hue                             | 4.9.0            | 4.9.0            | 4.9.0            | 4.8.0            |
| Iceberg                         | -                | -                | -                | -                |
| JupyterEnterpriseGateway        | 2.1.0            | 2.1.0            | 2.1.0            | 2.1.0            |
| JupyterHub                      | 1.4.1            | 1.2.2            | 1.2.2            | 1.1.0            |
| Livy                            | 0.7.1-incubating | 0.7.0-incubating | 0.7.0-incubating | 0.7.0-incubating |
| MXNet                           | 1.8.0            | 1.7.0            | 1.7.0            | 1.7.0            |
| Mahout                          | -                | -                | -                | -                |
| Oozie                           | 5.2.1            | 5.2.1            | 5.2.1            | 5.2.0            |
| Phoenix                         | 5.1.2            | 5.0.0-HBase-2.0  | 5.0.0-HBase-2.0  | 5.0.0-HBase-2.0  |
| Pig                             | 0.17.0           | 0.17.0           | 0.17.0           | 0.17.0           |
| Presto                          | 0.254.1-amzn-0   | 0.245.1-amzn-0   | 0.245.1-amzn-0   | 0.238.3-amzn-1   |
| Spark                           | 3.1.2-amzn-0     | 3.1.1-amzn-0.1   | 3.1.1-amzn-0     | 3.0.1-amzn-0.1   |
| Sqoop                           | 1.4.7            | 1.4.7            | 1.4.7            | 1.4.7            |
| TensorFlow                      | 2.4.1            | 2.4.1            | 2.4.1            | 2.3.1            |
| Tez                             | 0.9.2            | 0.9.2            | 0.9.2            | 0.9.2            |
| Trino (PrestoSQL)               | 359              | 350              | 350              | 343              |
| Zeppelin                        | 0.9.0            | 0.9.0            | 0.9.0            | 0.9.0-preview1   |
| ZooKeeper                       | 3.5.7            | 3.4.14           | 3.4.14           | 3.4.14           |

## 6.4.0 release notes

The following release notes include information for Amazon EMR release 6.4.0. Changes
are relative to 6.3.0.

Initial release date: Sept 20, 2021

Updated release date: March 21, 2022

###### Supported applications

- AWS SDK for Java version 1.12.31
- CloudWatch Sink version 2.2.0
- DynamoDB Connector version 4.16.0
- EMRFS version 2.47.0
- Amazon EMR Goodies version 3.2.0
- Amazon EMR Kinesis Connector version 3.5.0
- Amazon EMR Record Server version 2.1.0
- Amazon EMR Scripts version 2.5.0
- Flink version 1.13.1
- Ganglia version 3.7.2
- AWS Glue Hive Metastore Client version 3.3.0
- Hadoop version 3.2.1-amzn-4
- HBase version 2.4.4-amzn-0
- HBase-operator-tools 1.1.0
- HCatalog version 3.1.2-amzn-5
- Hive version 3.1.2-amzn-5
- Hudi version 0.8.0-amzn-0
- Hue version 4.9.0
- Java JDK version Corretto-8.302.08.1 (build 1.8.0_302-b08)
- JupyterHub version 1.4.1
- Livy version 0.7.1-incubating
- MXNet version 1.8.0
- Oozie version 5.2.1
- Phoenix version 5.1.2
- Pig version 0.17.0
- Presto version 0.254.1-amzn-0
- Trino version 359
- Apache Ranger KMS (multi-master transparent encryption) version 2.0.0
- ranger-plugins 2.0.1-amzn-0
- ranger-s3-plugin 1.2.0
- SageMaker Spark SDK version 1.4.1
- Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_282)
- Spark version 3.1.2-amzn-0
- spark-rapids 0.4.1
- Sqoop version 1.4.7
- TensorFlow version 2.4.1
- tez version 0.9.2
- Zeppelin version 0.9.0
- Zookeeper version 3.5.7
- Connectors and drivers: DynamoDB Connector 4.16.0

###### New features

- **[Managed scaling] Spark shuffle data managed scaling optimization** - For Amazon EMR versions 5.34.0 and
  later, and EMR versions 6.4.0 and later, managed scaling is now Spark shuffle data aware
  (data that Spark redistributes across partitions to perform specific operations). For more information
  on shuffle operations, see [Using EMR managed scaling in Amazon EMR](../ManagementGuide/emr-managed-scaling.md "../ManagementGuide/emr-managed-scaling.md") in the _Amazon EMR Management Guide_ and [Spark Programming Guide](https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations "https://spark.apache.org/docs/latest/rdd-programming-guide.html#shuffle-operations").
- On Apache Ranger-enabled Amazon EMR clusters, you can use Apache Spark SQL to insert data into or update the Apache Hive metastore tables using `INSERT INTO`, `INSERT OVERWRITE`, and `ALTER TABLE`.
  When using ALTER TABLE with Spark SQL, a partition location must be the child directory of a table location. Amazon EMR does not currently support inserting data into a partition where the partition location is different from the table location.
- PrestoSQL has been
  [renamed to Trino.](https://trino.io/blog/2020/12/27/announcing-trino.html "https://trino.io/blog/2020/12/27/announcing-trino.html")
- Hive: Execution of simple SELECT queries with LIMIT clause are accelerated by stopping the query execution as soon as the number of records mentioned in LIMIT clause is fetched.
  Simple SELECT queries are queries that do not have GROUP BY / ORDER by clause or queries that do not have a reducer stage. For example,
  `SELECT * from <TABLE> WHERE <Condition> LIMIT <Number>`.

###### Hudi Concurrency Control

- Hudi now supports Optimistic Concurrency Control (OCC), which can be leveraged with write operations like UPSERT and INSERT to allow changes from multiple writers to the same Hudi table. This is file-level OCC, so any two commits (or writers) can write to the same table, if their changes do not conflict.
  For more information, see the
  [Hudi concurrency control](https://hudi.apache.org/docs/concurrency_control/ "https://hudi.apache.org/docs/concurrency_control/").
- Amazon EMR clusters have Zookeeper installed, which can be leveraged as the lock provider for OCC. To make it easier to use this feature, Amazon EMR clusters have the following properties pre-configured:

```
hoodie.write.lock.provider=org.apache.hudi.client.transaction.lock.ZookeeperBasedLockProvider
hoodie.write.lock.zookeeper.url=<`EMR Zookeeper URL`>
hoodie.write.lock.zookeeper.port=<`EMR Zookeeper Port`>
hoodie.write.lock.zookeeper.base_path=/hudi
```

To enable OCC, you need to configure the following properties either with their Hudi job options or at the cluster-level using the Amazon EMR configurations API:

```
hoodie.write.concurrency.mode=optimistic_concurrency_control
hoodie.cleaner.policy.failed.writes=LAZY (Performs cleaning of failed writes lazily instead of inline with every write)
hoodie.write.lock.zookeeper.lock_key=`<Key to uniquely identify the Hudi table>` (Table Name is a good option)
```

###### Hudi Monitoring: Amazon CloudWatch integration to report Hudi Metrics

- Amazon EMR supports publishing Hudi Metrics to Amazon CloudWatch. It is enabled by setting the following required configurations:

```
hoodie.metrics.on=true
hoodie.metrics.reporter.type=CLOUDWATCH
```

- The following are optional Hudi configurations that you can change:

| Setting                                         | Description                                                                 | Value                                                                                                  |
| ----------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| hoodie.metrics.cloudwatch.report.period.seconds | Frequency (in seconds) at which to report metrics to Amazon CloudWatch      | Default value is 60s, which is fine for the default one minute resolution offered by Amazon CloudWatch |
| hoodie.metrics.cloudwatch.metric.prefix         | Prefix to be added to each metric name                                      | Default value is empty (no prefix)                                                                     |
| hoodie.metrics.cloudwatch.namespace             | Amazon CloudWatch namespace under which metrics are published               | Default value is Hudi                                                                                  |
| hoodie.metrics.cloudwatch.maxDatumsPerRequest   | Maximum number of datums to be included in one request to Amazon CloudWatch | Default value is 20, which is same as Amazon CloudWatch default                                        |

###### Amazon EMR Hudi configurations support and improvements

- Customers can now leverage EMR Configurations API and Reconfiguration feature to configure Hudi configurations at cluster level. A new file based configuration support has been introduced via /etc/hudi/conf/hudi-defaults.conf along the lines of other applications like Spark, Hive etc. EMR configures few defaults to improve user experience:

—
`hoodie.datasource.hive_sync.jdbcurl` is configured to the cluster Hive server URL and no longer needs to be specified. This is particularly useful when running a job in Spark cluster mode, where you previously had to specify the Amazon EMR master IP.

— HBase specific configurations, which are useful for using HBase index with Hudi.

— Zookeeper lock provider specific configuration, as discussed under concurrency control, which makes it easier to use Optimistic Concurrency Control (OCC).

- Additional changes have been introduced to reduce the number of configurations that you need to pass, and to infer automatically where possible:

— The
`partitionBy` keyword can be used to specify the partition column.

— When enabling Hive Sync, it is no longer mandatory to pass
`HIVE_TABLE_OPT_KEY, HIVE_PARTITION_FIELDS_OPT_KEY, HIVE_PARTITION_EXTRACTOR_CLASS_OPT_KEY`. Those values can be inferred from the Hudi table name and partition field.

—
`KEYGENERATOR_CLASS_OPT_KEY` is not mandatory to pass, and can be inferred from simpler cases of
`SimpleKeyGenerator` and
`ComplexKeyGenerator`.

###### Hudi Caveats

- Hudi does not support vectorized execution in Hive for Merge on Read (MoR) and Bootstrap tables. For example,
  `count(*)` fails with Hudi realtime table when
  `hive.vectorized.execution.enabled` is set to true.
  As a workaround, you can disable vectorized reading by setting
  `hive.vectorized.execution.enabled` to
  `false`.
- Multi-writer support is not compatible with the Hudi bootstrap feature.
- Flink Streamer and Flink SQL are experimental features in this release. These features are not recommended for use in production deployments.

###### Changes, enhancements, and resolved issues

This is a release to fix issues with Amazon EMR Scaling when it fails to scale up/scale down a cluster successfully or causes application failures.

- Previously, manual restart of the resource manager on a multi-master cluster caused Amazon EMR on-cluster daemons, like Zookeeper, to reload all previously decommissioned or lost nodes in the Zookeeper znode file. This caused default limits to be exceeded in certain situations. Amazon EMR now removes the decommissioned or lost node records older than one hour from the Zookeeper file and the internal limits have been increased.
- Fixed an issue where scaling requests failed for a large, highly utilized cluster when Amazon EMR on-cluster daemons were running health checking activities, such as gathering YARN node state and HDFS node state. This was happening because on-cluster daemons were not able to communicate the health status data of a node to internal Amazon EMR components.
- Improved EMR on-cluster daemons to correctly track the node states when IP addresses are reused to improve reliability during scaling operations.
- [SPARK-29683](https://issues.apache.org/jira/browse/SPARK-29683 "https://issues.apache.org/jira/browse/SPARK-29683"). Fixed an issue where job failures occurred during cluster scale-down as Spark was assuming all available nodes were deny-listed.
- [YARN-9011](https://issues.apache.org/jira/browse/YARN-9011 "https://issues.apache.org/jira/browse/YARN-9011"). Fixed an issue where job failures occurred due to a race condition in YARN decommissioning when cluster tried to scale up or down.
- Fixed issue with step or job failures during cluster scaling by ensuring that the node states are always consistent between the Amazon EMR on-cluster daemons and YARN/HDFS.
- Fixed an issue where cluster operations such as scale down and step submission failed for Amazon EMR clusters enabled with Kerberos authentication. This was because the Amazon EMR on-cluster daemon did not renew the Kerberos ticket, which is required to securely communicate with HDFS/YARN running on the primary node.
- **Configuring a cluster to fix Apache YARN Timeline Server version 1 and 1.5 performance issues**

Apache YARN Timeline Server version 1 and 1.5 can cause performance issues with very active, large EMR clusters, particularly with `yarn.resourcemanager.system-metrics-publisher.enabled=true`, which is the default setting in Amazon EMR.
An open source YARN Timeline Server v2 solves the performance issue related to YARN Timeline Server scalability.

Other workarounds for this issue include:

    + Configuring yarn.resourcemanager.system-metrics-publisher.enabled=false in yarn-site.xml.
    + Enabling the fix for this issue when creating a cluster, as described below.

The following Amazon EMR releases contain a fix for this YARN Timeline Server performance issue.

EMR 5.30.2, 5.31.1, 5.32.1, 5.33.1, 5.34.x, 6.0.1, 6.1.1, 6.2.1, 6.3.1, 6.4.x

To enable the fix on any of the above specified Amazon EMR releases, set these properties to `true` in a configurations JSON file that is passed in using the [`aws emr create-cluster` command parameter](emr-configure-apps-create-cluster.md "emr-configure-apps-create-cluster.md"): `--configurations file://./configurations.json`. Or enable the fix using the [reconfiguration console UI](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

Example of the configurations.json file contents:

```
[
{
"Classification": "yarn-site",
"Properties": {
"yarn.resourcemanager.system-metrics-publisher.timeline-server-v1.enable-batch": "true",
"yarn.resourcemanager.system-metrics-publisher.enabled": "true"
},
"Configurations": []
}
]
```

- WebHDFS and HttpFS server are disabled by default. You can re-enable WebHDFS using the Hadoop configuration, `dfs.webhdfs.enabled`. HttpFS server can be started by using `sudo systemctl start hadoop-httpfs`.
- HTTPS is now enabled by default for Amazon Linux repositories. If you are using an Amazon S3 VPCE policy to restrict access to specific buckets, you must add the new Amazon Linux bucket ARN
  `arn:aws:s3:::amazonlinux-2-repos-$region/*` to your policy (replace
  `$region` with the region where the endpoint is).
  For more information, see this topic in the AWS discussion forums.
  [Announcement: Amazon Linux 2 now supports the ability to use HTTPS while connecting to package repositories](https://forums.aws.amazon.com/ann.jspa?annID=8528 "https://forums.aws.amazon.com/ann.jspa?annID=8528") .
- Hive: Write query performance is improved by enabling the use of a scratch directory on HDFS for the last job. The temporary data for final job is written to HDFS instead of Amazon S3 and performance is improved because the data is moved from HDFS to the final table location (Amazon S3) instead of between Amazon S3 devices.
- Hive: Query compilation time improvement up to 2.5x with Glue metastore Partition Pruning.
- By default, when built-in UDFs are passed by Hive to the Hive Metastore Server, only a subset of those built-in UDFs are passed to the Glue Metastore since Glue supports only limited expression
  operators. If you set
  `hive.glue.partition.pruning.client=true`, then all partition pruning happens on the client side. If the you set
  `hive.glue.partition.pruning.server=true`, then all partition pruning happens on the server side.

###### Known issues

- Hue queries do not work in Amazon EMR 6.4.0 because Apache Hadoop HttpFS server is disabled by default. To use Hue on Amazon EMR 6.4.0, either manually start HttpFS server on the Amazon EMR primary node using `sudo systemctl start hadoop-httpfs`, or [use an Amazon EMR step](../ManagementGuide/add-step-cli.md "../ManagementGuide/add-step-cli.md").
- The Amazon EMR Notebooks feature used with Livy user impersonation does not work because HttpFS is disabled by default. In this case, the EMR notebook cannot connect to the cluster that has Livy impersonation enabled. The workaround is to start HttpFS server before connecting the EMR notebook to the cluster using `sudo systemctl start hadoop-httpfs`.
- In Amazon EMR version 6.4.0, Phoenix does not support the Phoenix connectors component.
- To use Spark actions with Apache Oozie, you must add the following configuration to your Oozie `workflow.xml` file. Otherwise, several critical libraries such as Hadoop and EMRFS will be missing from the classpath of the Spark executors that Oozie launches.

```
<spark-opts>--conf spark.yarn.populateHadoopClasspath=true</spark-opts>
```

- When you use Spark with Hive partition location formatting to read data in Amazon S3, and you
  run Spark on Amazon EMR releases 5.30.0 to 5.36.0, and 6.2.0 to 6.9.0, you might encounter an
  issue that prevents your cluster from reading data correctly. This can happen if your
  partitions have all of the following characteristics:

      + Two or more partitions are scanned from the same table.
      + At least one partition directory path is a prefix of at least one other partition directory
       path, for example, `s3://bucket/table/p=a` is a prefix of
       `s3://bucket/table/p=a b`.
      + The first character that follows the prefix in the other partition directory has a UTF-8
       value that’s less than than the `/` character (U+002F). For example, the
       space character (U+0020) that occurs between a and b in `s3://bucket/table/p=a
       b` falls into this category. Note that there are 14 other non-control
       characters: `!"#$%&‘()*+,-`. For more information, see [UTF-8 encoding table and Unicode
       characters](https://www.utf8-chartable.de/ "https://www.utf8-chartable.de/").

  As a workaround to this issue, set the
  `spark.sql.sources.fastS3PartitionDiscovery.enabled` configuration to
  `false` in the `spark-defaults` classification.

## 6.4.0 component versions

The components that Amazon EMR installs with this release are listed below. Some are installed as part of big-data application packages. Others are unique to Amazon EMR and installed for system processes and features. These typically start with `emr` or `aws`. Big-data application packages in the most recent Amazon EMR release are usually the latest version found in the community. We make community releases available in Amazon EMR as quickly as possible.

Some components in Amazon EMR differ from community versions. These components have a version label in the form ``CommunityVersion`-amzn-`EmrVersion``. The `EmrVersion` starts at 0. For example, if open source community component named `myapp-component` with version 2.2 has been modified three times for inclusion in different Amazon EMR releases, its release version is listed as `2.2-amzn-2`.

| Component                   | Version          | Description                                                                                                                                 |
| --------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| aws-sagemaker-spark-sdk     | 1.4.1            | Amazon SageMaker Spark SDK                                                                                                                  |
| emr-ddb                     | 4.16.0           | Amazon DynamoDB connector for Hadoop ecosystem applications.                                                                                |
| emr-goodies                 | 3.2.0            | Extra convenience libraries for the Hadoop ecosystem.                                                                                       |
| emr-kinesis                 | 3.5.0            | Amazon Kinesis connector for Hadoop ecosystem applications.                                                                                 |
| emr-notebook-env            | 1.3.0            | Conda env for emr notebook which includes jupyter enterprise gateway                                                                        |
| emr-s3-dist-cp              | 2.18.0           | Distributed copy application optimized for Amazon S3.                                                                                       |
| emr-s3-select               | 2.1.0            | EMR S3Select Connector                                                                                                                      |
| emrfs                       | 2.47.0           | Amazon S3 connector for Hadoop ecosystem applications.                                                                                      |
| flink-client                | 1.13.1           | Apache Flink command line client scripts and applications.                                                                                  |
| flink-jobmanager-config     | 1.13.1           | Managing resources on EMR nodes for Apache Flink JobManager.                                                                                |
| ganglia-monitor             | 3.7.2            | Embedded Ganglia agent for Hadoop ecosystem applications along with the Ganglia monitoring agent.                                           |
| ganglia-metadata-collector  | 3.7.2            | Ganglia metadata collector for aggregating metrics from Ganglia monitoring agents.                                                          |
| ganglia-web                 | 3.7.1            | Web application for viewing metrics collected by the Ganglia metadata collector.                                                            |
| hadoop-client               | 3.2.1-amzn-4     | Hadoop command-line clients such as 'hdfs', 'hadoop', or 'yarn'.                                                                            |
| hadoop-hdfs-datanode        | 3.2.1-amzn-4     | HDFS node-level service for storing blocks.                                                                                                 |
| hadoop-hdfs-library         | 3.2.1-amzn-4     | HDFS command-line client and library                                                                                                        |
| hadoop-hdfs-namenode        | 3.2.1-amzn-4     | HDFS service for tracking file names and block locations.                                                                                   |
| hadoop-hdfs-journalnode     | 3.2.1-amzn-4     | HDFS service for managing the Hadoop filesystem journal on HA clusters.                                                                     |
| hadoop-httpfs-server        | 3.2.1-amzn-4     | HTTP endpoint for HDFS operations.                                                                                                          |
| hadoop-kms-server           | 3.2.1-amzn-4     | Cryptographic key management server based on Hadoop's KeyProvider API.                                                                      |
| hadoop-mapred               | 3.2.1-amzn-4     | MapReduce execution engine libraries for running a MapReduce application.                                                                   |
| hadoop-yarn-nodemanager     | 3.2.1-amzn-4     | YARN service for managing containers on an individual node.                                                                                 |
| hadoop-yarn-resourcemanager | 3.2.1-amzn-4     | YARN service for allocating and managing cluster resources and distributed applications.                                                    |
| hadoop-yarn-timeline-server | 3.2.1-amzn-4     | Service for retrieving current and historical information for YARN applications.                                                            |
| hbase-hmaster               | 2.4.4-amzn-0     | Service for an HBase cluster responsible for coordination of Regions and execution of administrative commands.                              |
| hbase-region-server         | 2.4.4-amzn-0     | Service for serving one or more HBase regions.                                                                                              |
| hbase-client                | 2.4.4-amzn-0     | HBase command-line client.                                                                                                                  |
| hbase-rest-server           | 2.4.4-amzn-0     | Service providing a RESTful HTTP endpoint for HBase.                                                                                        |
| hbase-thrift-server         | 2.4.4-amzn-0     | Service providing a Thrift endpoint to HBase.                                                                                               |
| hcatalog-client             | 3.1.2-amzn-5     | The 'hcat' command line client for manipulating hcatalog-server.                                                                            |
| hcatalog-server             | 3.1.2-amzn-5     | Service providing HCatalog, a table and storage management layer for distributed applications.                                              |
| hcatalog-webhcat-server     | 3.1.2-amzn-5     | HTTP endpoint providing a REST interface to HCatalog.                                                                                       |
| hive-client                 | 3.1.2-amzn-5     | Hive command line client.                                                                                                                   |
| hive-hbase                  | 3.1.2-amzn-5     | Hive-hbase client.                                                                                                                          |
| hive-metastore-server       | 3.1.2-amzn-5     | Service for accessing the Hive metastore, a semantic repository storing metadata for SQL on Hadoop operations.                              |
| hive-server2                | 3.1.2-amzn-5     | Service for accepting Hive queries as web requests.                                                                                         |
| hudi                        | 0.8.0-amzn-0     | Incremental processing framework to power data pipline at low latency and high efficiency.                                                  |
| hudi-presto                 | 0.8.0-amzn-0     | Bundle library for running Presto with Hudi.                                                                                                |
| hudi-trino                  | 0.8.0-amzn-0     | Bundle library for running Trino with Hudi.                                                                                                 |
| hudi-spark                  | 0.8.0-amzn-0     | Bundle library for running Spark with Hudi.                                                                                                 |
| hue-server                  | 4.9.0            | Web application for analyzing data using Hadoop ecosystem applications                                                                      |
| jupyterhub                  | 1.4.1            | Multi-user server for Jupyter notebooks                                                                                                     |
| livy-server                 | 0.7.1-incubating | REST interface for interacting with Apache Spark                                                                                            |
| nginx                       | 1.12.1           | nginx [engine x] is an HTTP and reverse proxy server                                                                                        |
| mxnet                       | 1.8.0            | A flexible, scalable, and efficient library for deep learning.                                                                              |
| mariadb-server              | 5.5.68+          | MariaDB database server.                                                                                                                    |
| nvidia-cuda                 | 10.1.243         | Nvidia drivers and Cuda toolkit                                                                                                             |
| oozie-client                | 5.2.1            | Oozie command-line client.                                                                                                                  |
| oozie-server                | 5.2.1            | Service for accepting Oozie workflow requests.                                                                                              |
| opencv                      | 4.5.0            | Open Source Computer Vision Library.                                                                                                        |
| phoenix-library             | 5.1.2            | The phoenix libraries for server and client                                                                                                 |
| phoenix-query-server        | 5.1.2            | A light weight server providing JDBC access as well as Protocol Buffers and JSON format access to the Avatica API                           |
| presto-coordinator          | 0.254.1-amzn-0   | Service for accepting queries and managing query execution among presto-workers.                                                            |
| presto-worker               | 0.254.1-amzn-0   | Service for executing pieces of a query.                                                                                                    |
| presto-client               | 0.254.1-amzn-0   | Presto command-line client which is installed on an HA cluster's stand-by masters where Presto server is not started.                       |
| trino-coordinator           | 359              | Service for accepting queries and managing query execution among trino-workers.                                                             |
| trino-worker                | 359              | Service for executing pieces of a query.                                                                                                    |
| trino-client                | 359              | Trino command-line client which is installed on an HA cluster's stand-by masters where Trino server is not started.                         |
| pig-client                  | 0.17.0           | Pig command-line client.                                                                                                                    |
| r                           | 4.0.2            | The R Project for Statistical Computing                                                                                                     |
| ranger-kms-server           | 2.0.0            | Apache Ranger Key Management System                                                                                                         |
| spark-client                | 3.1.2-amzn-0     | Spark command-line clients.                                                                                                                 |
| spark-history-server        | 3.1.2-amzn-0     | Web UI for viewing logged events for the lifetime of a completed Spark application.                                                         |
| spark-on-yarn               | 3.1.2-amzn-0     | In-memory execution engine for YARN.                                                                                                        |
| spark-yarn-slave            | 3.1.2-amzn-0     | Apache Spark libraries needed by YARN slaves.                                                                                               |
| spark-rapids                | 0.4.1            | Nvidia Spark RAPIDS plugin that accelerates Apache Spark with GPUs.                                                                         |
| sqoop-client                | 1.4.7            | Apache Sqoop command-line client.                                                                                                           |
| tensorflow                  | 2.4.1            | TensorFlow open source software library for high performance numerical computation.                                                         |
| tez-on-yarn                 | 0.9.2            | The tez YARN application and libraries.                                                                                                     |
| webserver                   | 2.4.41+          | Apache HTTP server.                                                                                                                         |
| zeppelin-server             | 0.9.0            | Web-based notebook that enables interactive data analytics.                                                                                 |
| zookeeper-server            | 3.5.7            | Centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. |
| zookeeper-client            | 3.5.7            | ZooKeeper command line client.                                                                                                              |

## 6.4.0 configuration classifications

Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `hive-site.xml`. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

Reconfiguration actions occur when you specify a configuration for instance groups in a running cluster. Amazon EMR only initiates reconfiguration actions for the classifications that you modify. For more information, see [Reconfigure an instance group in a
running cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

| emr-6.4.0 classifications       | Classifications                                                             | Description                                                                                                                                                                                                                                                                                                                                                   | Reconfiguration Actions |
| ------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| capacity-scheduler              | Change values in Hadoop's capacity-scheduler.xml file.                      | Restarts the ResourceManager service.                                                                                                                                                                                                                                                                                                                         |
| container-executor              | Change values in Hadoop YARN's container-executor.cfg file.                 | Not available.                                                                                                                                                                                                                                                                                                                                                |
| container-log4j                 | Change values in Hadoop YARN's container-log4j.properties file.             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| core-site                       | Change values in Hadoop's core-site.xml file.                               | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts Hadoop KMS, Ranger KMS, HiveServer2, Hive MetaStore, Hadoop Httpfs, and MapReduce-HistoryServer.                                 |
| docker-conf                     | Change docker related settings.                                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| emrfs-site                      | Change EMRFS settings.                                                      | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts HBaseRegionserver, HBaseMaster, HBaseThrift, HBaseRest, HiveServer2, Hive MetaStore, Hadoop Httpfs, and MapReduce-HistoryServer. |
| flink-conf                      | Change flink-conf.yaml settings.                                            | Restarts Flink history server.                                                                                                                                                                                                                                                                                                                                |
| flink-log4j                     | Change Flink log4j.properties settings.                                     | Restarts Flink history server.                                                                                                                                                                                                                                                                                                                                |
| flink-log4j-session             | Change Flink log4j-session.properties settings for Kubernetes/Yarn session. | Restarts Flink history server.                                                                                                                                                                                                                                                                                                                                |
| flink-log4j-cli                 | Change Flink log4j-cli.properties settings.                                 | Restarts Flink history server.                                                                                                                                                                                                                                                                                                                                |
| hadoop-env                      | Change values in the Hadoop environment for all Hadoop components.          | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts PhoenixQueryserver, HiveServer2, Hive MetaStore, and MapReduce-HistoryServer.                                                    |
| hadoop-log4j                    | Change values in Hadoop's log4j.properties file.                            | Restarts the Hadoop HDFS services SecondaryNamenode, Datanode, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts Hadoop KMS, Hadoop Httpfs, and MapReduce-HistoryServer.                                                                                          |
| hadoop-ssl-server               | Change hadoop ssl server configuration                                      | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hadoop-ssl-client               | Change hadoop ssl client configuration                                      | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hbase                           | Amazon EMR-curated settings for Apache HBase.                               | Custom EMR specific property. Sets emrfs-site and hbase-site configs. See those for their associated restarts.                                                                                                                                                                                                                                                |
| hbase-env                       | Change values in HBase's environment.                                       | Restarts the HBase services RegionServer, HBaseMaster, ThriftServer, RestServer.                                                                                                                                                                                                                                                                              |
| hbase-log4j                     | Change values in HBase's hbase-log4j.properties file.                       | Restarts the HBase services RegionServer, HBaseMaster, ThriftServer, RestServer.                                                                                                                                                                                                                                                                              |
| hbase-metrics                   | Change values in HBase's hadoop-metrics2-hbase.properties file.             | Restarts the HBase services RegionServer, HBaseMaster, ThriftServer, RestServer.                                                                                                                                                                                                                                                                              |
| hbase-policy                    | Change values in HBase's hbase-policy.xml file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hbase-site                      | Change values in HBase's hbase-site.xml file.                               | Restarts the HBase services RegionServer, HBaseMaster, ThriftServer, RestServer.<br>Additionally restarts Phoenix QueryServer.                                                                                                                                                                                                                                |
| hdfs-encryption-zones           | Configure HDFS encryption zones.                                            | This classification should not be reconfigured.                                                                                                                                                                                                                                                                                                               |
| hdfs-env                        | Change values in the HDFS environment.                                      | Restarts Hadoop HDFS services Namenode, Datanode, and ZKFC.                                                                                                                                                                                                                                                                                                   |
| hdfs-site                       | Change values in HDFS's hdfs-site.xml.                                      | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Additionally restarts Hadoop Httpfs.                                                                                                                                                                                                                       |
| hcatalog-env                    | Change values in HCatalog's environment.                                    | Restarts Hive HCatalog Server.                                                                                                                                                                                                                                                                                                                                |
| hcatalog-server-jndi            | Change values in HCatalog's jndi.properties.                                | Restarts Hive HCatalog Server.                                                                                                                                                                                                                                                                                                                                |
| hcatalog-server-proto-hive-site | Change values in HCatalog's proto-hive-site.xml.                            | Restarts Hive HCatalog Server.                                                                                                                                                                                                                                                                                                                                |
| hcatalog-webhcat-env            | Change values in HCatalog WebHCat's environment.                            | Restarts Hive WebHCat server.                                                                                                                                                                                                                                                                                                                                 |
| hcatalog-webhcat-log4j2         | Change values in HCatalog WebHCat's log4j2.properties.                      | Restarts Hive WebHCat server.                                                                                                                                                                                                                                                                                                                                 |
| hcatalog-webhcat-site           | Change values in HCatalog WebHCat's webhcat-site.xml file.                  | Restarts Hive WebHCat server.                                                                                                                                                                                                                                                                                                                                 |
| hive                            | Amazon EMR-curated settings for Apache Hive.                                | Sets configurations to launch Hive LLAP service.                                                                                                                                                                                                                                                                                                              |
| hive-beeline-log4j2             | Change values in Hive's beeline-log4j2.properties file.                     | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hive-parquet-logging            | Change values in Hive's parquet-logging.properties file.                    | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hive-env                        | Change values in the Hive environment.                                      | Restarts HiveServer2, HiveMetastore, and Hive HCatalog-Server.<br>Runs Hive schemaTool CLI commands to verify hive-metastore.                                                                                                                                                                                                                                 |
| hive-exec-log4j2                | Change values in Hive's hive-exec-log4j2.properties file.                   | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hive-llap-daemon-log4j2         | Change values in Hive's llap-daemon-log4j2.properties file.                 | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hive-log4j2                     | Change values in Hive's hive-log4j2.properties file.                        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hive-site                       | Change values in Hive's hive-site.xml file                                  | Restarts HiveServer2, HiveMetastore, and Hive HCatalog-Server.<br>Runs Hive schemaTool CLI commands to verify hive-metastore.<br>Also restarts Oozie and Zeppelin.                                                                                                                                                                                            |
| hiveserver2-site                | Change values in Hive Server2's hiveserver2-site.xml file                   | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hue-ini                         | Change values in Hue's ini file                                             | Restarts Hue. Also activates Hue config override CLI commands to pick up new configurations.                                                                                                                                                                                                                                                                  |
| httpfs-env                      | Change values in the HTTPFS environment.                                    | Restarts Hadoop Httpfs service.                                                                                                                                                                                                                                                                                                                               |
| httpfs-site                     | Change values in Hadoop's httpfs-site.xml file.                             | Restarts Hadoop Httpfs service.                                                                                                                                                                                                                                                                                                                               |
| hadoop-kms-acls                 | Change values in Hadoop's kms-acls.xml file.                                | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hadoop-kms-env                  | Change values in the Hadoop KMS environment.                                | Restarts Hadoop-KMS service.                                                                                                                                                                                                                                                                                                                                  |
| hadoop-kms-log4j                | Change values in Hadoop's kms-log4j.properties file.                        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hadoop-kms-site                 | Change values in Hadoop's kms-site.xml file.                                | Restarts Hadoop-KMS and Ranger-KMS service.                                                                                                                                                                                                                                                                                                                   |
| hudi-env                        | Change values in the Hudi environment.                                      | Not available.                                                                                                                                                                                                                                                                                                                                                |
| hudi-defaults                   | Change values in Hudi's hudi-defaults.conf file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| jupyter-notebook-conf           | Change values in Jupyter Notebook's jupyter_notebook_config.py file.        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| jupyter-hub-conf                | Change values in JupyterHubs's jupyterhub_config.py file.                   | Not available.                                                                                                                                                                                                                                                                                                                                                |
| jupyter-s3-conf                 | Configure Jupyter Notebook S3 persistence.                                  | Not available.                                                                                                                                                                                                                                                                                                                                                |
| jupyter-sparkmagic-conf         | Change values in Sparkmagic's config.json file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| livy-conf                       | Change values in Livy's livy.conf file.                                     | Restarts Livy Server.                                                                                                                                                                                                                                                                                                                                         |
| livy-env                        | Change values in the Livy environment.                                      | Restarts Livy Server.                                                                                                                                                                                                                                                                                                                                         |
| livy-log4j                      | Change Livy log4j.properties settings.                                      | Restarts Livy Server.                                                                                                                                                                                                                                                                                                                                         |
| mapred-env                      | Change values in the MapReduce application's environment.                   | Restarts Hadoop MapReduce-HistoryServer.                                                                                                                                                                                                                                                                                                                      |
| mapred-site                     | Change values in the MapReduce application's mapred-site.xml file.          | Restarts Hadoop MapReduce-HistoryServer.                                                                                                                                                                                                                                                                                                                      |
| oozie-env                       | Change values in Oozie's environment.                                       | Restarts Oozie.                                                                                                                                                                                                                                                                                                                                               |
| oozie-log4j                     | Change values in Oozie's oozie-log4j.properties file.                       | Restarts Oozie.                                                                                                                                                                                                                                                                                                                                               |
| oozie-site                      | Change values in Oozie's oozie-site.xml file.                               | Restarts Oozie.                                                                                                                                                                                                                                                                                                                                               |
| phoenix-hbase-metrics           | Change values in Phoenix's hadoop-metrics2-hbase.properties file.           | Not available.                                                                                                                                                                                                                                                                                                                                                |
| phoenix-hbase-site              | Change values in Phoenix's hbase-site.xml file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| phoenix-log4j                   | Change values in Phoenix's log4j.properties file.                           | Restarts Phoenix-QueryServer.                                                                                                                                                                                                                                                                                                                                 |
| phoenix-metrics                 | Change values in Phoenix's hadoop-metrics2-phoenix.properties file.         | Not available.                                                                                                                                                                                                                                                                                                                                                |
| pig-env                         | Change values in the Pig environment.                                       | Not available.                                                                                                                                                                                                                                                                                                                                                |
| pig-properties                  | Change values in Pig's pig.properties file.                                 | Restarts Oozie.                                                                                                                                                                                                                                                                                                                                               |
| pig-log4j                       | Change values in Pig's log4j.properties file.                               | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-log                      | Change values in Presto's log.properties file.                              | Restarts Presto-Server (for PrestoDB)                                                                                                                                                                                                                                                                                                                         |
| presto-config                   | Change values in Presto's config.properties file.                           | Restarts Presto-Server (for PrestoDB)                                                                                                                                                                                                                                                                                                                         |
| presto-password-authenticator   | Change values in Presto's password-authenticator.properties file.           | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-env                      | Change values in Presto's presto-env.sh file.                               | Restarts Presto-Server (for PrestoDB)                                                                                                                                                                                                                                                                                                                         |
| presto-node                     | Change values in Presto's node.properties file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-blackhole      | Change values in Presto's blackhole.properties file.                        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-cassandra      | Change values in Presto's cassandra.properties file.                        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-hive           | Change values in Presto's hive.properties file.                             | Restarts Presto-Server (for PrestoDB)                                                                                                                                                                                                                                                                                                                         |
| presto-connector-jmx            | Change values in Presto's jmx.properties file.                              | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-kafka          | Change values in Presto's kafka.properties file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-localfile      | Change values in Presto's localfile.properties file.                        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-memory         | Change values in Presto's memory.properties file.                           | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-mongodb        | Change values in Presto's mongodb.properties file.                          | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-mysql          | Change values in Presto's mysql.properties file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-postgresql     | Change values in Presto's postgresql.properties file.                       | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-raptor         | Change values in Presto's raptor.properties file.                           | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-redis          | Change values in Presto's redis.properties file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-redshift       | Change values in Presto's redshift.properties file.                         | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-tpch           | Change values in Presto's tpch.properties file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| presto-connector-tpcds          | Change values in Presto's tpcds.properties file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-log                       | Change values in Trino's log.properties file.                               | Restarts Trino-Server (for Trino)                                                                                                                                                                                                                                                                                                                             |
| trino-config                    | Change values in Trino's config.properties file.                            | Restarts Trino-Server (for Trino)                                                                                                                                                                                                                                                                                                                             |
| trino-password-authenticator    | Change values in Trino's password-authenticator.properties file.            | Restarts Trino-Server (for Trino)                                                                                                                                                                                                                                                                                                                             |
| trino-env                       | Change values in Trino's trino-env.sh file.                                 | Restarts Trino-Server (for Trino)                                                                                                                                                                                                                                                                                                                             |
| trino-node                      | Change values in Trino's node.properties file.                              | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-blackhole       | Change values in Trino's blackhole.properties file.                         | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-cassandra       | Change values in Trino's cassandra.properties file.                         | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-hive            | Change values in Trino's hive.properties file.                              | Restarts Trino-Server (for Trino)                                                                                                                                                                                                                                                                                                                             |
| trino-connector-jmx             | Change values in Trino's jmx.properties file.                               | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-kafka           | Change values in Trino's kafka.properties file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-localfile       | Change values in Trino's localfile.properties file.                         | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-memory          | Change values in Trino's memory.properties file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-mongodb         | Change values in Trino's mongodb.properties file.                           | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-mysql           | Change values in Trino's mysql.properties file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-postgresql      | Change values in Trino's postgresql.properties file.                        | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-raptor          | Change values in Trino's raptor.properties file.                            | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-redis           | Change values in Trino's redis.properties file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-redshift        | Change values in Trino's redshift.properties file.                          | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-tpch            | Change values in Trino's tpch.properties file.                              | Not available.                                                                                                                                                                                                                                                                                                                                                |
| trino-connector-tpcds           | Change values in Trino's tpcds.properties file.                             | Not available.                                                                                                                                                                                                                                                                                                                                                |
| ranger-kms-dbks-site            | Change values in dbks-site.xml file of Ranger KMS.                          | Restarts Ranger KMS Server.                                                                                                                                                                                                                                                                                                                                   |
| ranger-kms-site                 | Change values in ranger-kms-site.xml file of Ranger KMS.                    | Restarts Ranger KMS Server.                                                                                                                                                                                                                                                                                                                                   |
| ranger-kms-env                  | Change values in the Ranger KMS environment.                                | Restarts Ranger KMS Server.                                                                                                                                                                                                                                                                                                                                   |
| ranger-kms-log4j                | Change values in kms-log4j.properties file of Ranger KMS.                   | Not available.                                                                                                                                                                                                                                                                                                                                                |
| ranger-kms-db-ca                | Change values for CA file on S3 for MySQL SSL connection with Ranger KMS.   | Not available.                                                                                                                                                                                                                                                                                                                                                |
| spark                           | Amazon EMR-curated settings for Apache Spark.                               | This property modifies spark-defaults. See actions there.                                                                                                                                                                                                                                                                                                     |
| spark-defaults                  | Change values in Spark's spark-defaults.conf file.                          | Restarts Spark history server and Spark thrift server.                                                                                                                                                                                                                                                                                                        |
| spark-env                       | Change values in the Spark environment.                                     | Restarts Spark history server and Spark thrift server.                                                                                                                                                                                                                                                                                                        |
| spark-hive-site                 | Change values in Spark's hive-site.xml file                                 | Not available.                                                                                                                                                                                                                                                                                                                                                |
| spark-log4j                     | Change values in Spark's log4j.properties file.                             | Restarts Spark history server and Spark thrift server.                                                                                                                                                                                                                                                                                                        |
| spark-metrics                   | Change values in Spark's metrics.properties file.                           | Restarts Spark history server and Spark thrift server.                                                                                                                                                                                                                                                                                                        |
| sqoop-env                       | Change values in Sqoop's environment.                                       | Not available.                                                                                                                                                                                                                                                                                                                                                |
| sqoop-oraoop-site               | Change values in Sqoop OraOop's oraoop-site.xml file.                       | Not available.                                                                                                                                                                                                                                                                                                                                                |
| sqoop-site                      | Change values in Sqoop's sqoop-site.xml file.                               | Not available.                                                                                                                                                                                                                                                                                                                                                |
| tez-site                        | Change values in Tez's tez-site.xml file.                                   | Restart Oozie and HiveServer2.                                                                                                                                                                                                                                                                                                                                |
| yarn-env                        | Change values in the YARN environment.                                      | Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts MapReduce-HistoryServer.                                                                                                                                                                                                            |
| yarn-site                       | Change values in YARN's yarn-site.xml file.                                 | Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts Livy Server and MapReduce-HistoryServer.                                                                                                                                                                                            |
| zeppelin-env                    | Change values in the Zeppelin environment.                                  | Restarts Zeppelin.                                                                                                                                                                                                                                                                                                                                            |
| zeppelin-site                   | Change configuration settings in zeppelin-site.xml.                         | Restarts Zeppelin.                                                                                                                                                                                                                                                                                                                                            |
| zookeeper-config                | Change values in ZooKeeper's zoo.cfg file.                                  | Restarts Zookeeper server.                                                                                                                                                                                                                                                                                                                                    |
| zookeeper-log4j                 | Change values in ZooKeeper's log4j.properties file.                         | Restarts Zookeeper server.                                                                                                                                                                                                                                                                                                                                    |
