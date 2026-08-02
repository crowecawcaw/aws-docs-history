# AWS runtime for Apache Spark (emr-spark-8.0.0)

## emr-spark-8.0.0 supported lifecycle

The following table describes the supported lifecycle dates for Amazon EMR Spark 8.0.0.

| Support phase          | Date         |
| ---------------------- | ------------ |
| Initial release date   | May 21, 2026 |
| Standard support until | May 20, 2028 |
| End of life            | May 20, 2028 |

## emr-spark-8.0.0 application versions

This release includes the following applications: [AmazonCloudWatchAgent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md"), [Delta](https://delta.io/ "https://delta.io/"), [Hudi](https://hudi.apache.org "https://hudi.apache.org"), [Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/"), [JupyterEnterpriseGateway](https://jupyter-enterprise-gateway.readthedocs.io/en/latest/ "https://jupyter-enterprise-gateway.readthedocs.io/en/latest/"), [Livy](https://livy.incubator.apache.org/ "https://livy.incubator.apache.org/"), and [Spark](https://spark.apache.org/docs/latest/ "https://spark.apache.org/docs/latest/").

The table below lists the application versions available in this release of Amazon EMR and the application versions in the preceding three Amazon EMR releases (when applicable).

For a comprehensive history of application versions for each release of Amazon EMR, see the following topics:

- [Application versions in Amazon EMR 7.x releases](emr-release-app-versions-7.x.md "emr-release-app-versions-7.x.md")
- [Application versions in Amazon EMR 6.x releases](emr-release-app-versions-6.x.md "emr-release-app-versions-6.x.md")
- [Application versions in Amazon EMR 5.x releases](emr-release-app-versions-5.x.md "emr-release-app-versions-5.x.md")
- [Application versions in Amazon EMR 4.x releases](emr-release-app-versions-4.x.md "emr-release-app-versions-4.x.md")

Application version information| | emr-spark-8.0.0 |
| --- | --- |
| AWS SDK for Java | 2.41.32 |
| Python | 3.11, 3.12, 3.13 |
| Scala | 2.13.16 |
| AmazonCloudWatchAgent | 1.300032.2-amzn-0 |
| Delta | 4.0.0-amzn-1-spark |
| Hudi | 1.1.0-amzn-0 |
| Iceberg | 1.10.1-amzn-0 |
| JupyterEnterpriseGateway | 2.6.0 |
| Livy | 0.8.0-incubating |
| Spark | 4.0.2-amzn-0 |

## emr-spark-8.0.0 release notes

The following release notes include information for Amazon EMR release 8.0.0 (emr-spark-8.0.0), featuring Apache Spark 4.0.2.

### What's new

- **Apache Spark 4.0.2 GA** — First production-ready release of Spark 4.x on Amazon EMR, based on the branch-4.0 upstream branch with Amazon patches for performance, security, and integration.
- **Available on EC2, EKS, and Serverless** — This release is available across all Amazon EMR deployment modes.
- **ANSI SQL Mode** — Stricter type handling enabled by default, improving SQL correctness and compatibility with standard SQL behavior.
- **SQL PIPE Syntax** — New |> operator for chaining SQL operations in a more readable, pipeline-style syntax.
- **VARIANT Data Type** — Native support for semi-structured JSON data using the VARIANT type, enabling schema-on-read patterns without explicit schema definitions.
- **SQL Scripting** — Control flow statements (IF/ELSE, WHILE, FOR) and session variables for procedural SQL logic within Spark SQL.
- **SQL User-Defined Functions** — Define UDFs directly in SQL without requiring Scala/Python code.
- **Streaming Enhancements** — Arbitrary Stateful Processing API v2 with transformWithState operator and enhanced RocksDB changelog checkpointing.
- **Apache Iceberg v3 Support** — VARIANT data type support in Iceberg tables, AWS S3 Tables integration.
- **Native Fine-grained Access Control and Full Table Access (FTA)** — Supported for Iceberg, Delta Lake, and Hive tables.
- **JDK 17 Default** — Amazon Corretto 17 is the default JVM; JDK 21 is also available.
- **Scala 2.13** — Spark 4.x drops Scala 2.12 support; all components built against Scala 2.13.

### Changes and enhancements since emr-spark-8.0-preview

- Livy and JupyterEnterpriseGateway available as interactive workload applications
- Persistent Spark History Server support

### Known issues and limitations

- Spark Connect secure endpoint with Native FGAC support is not available in this release.
- Native Fine-grained Access Control (FGAC) is not available for Iceberg tables that use the VARIANT data type.
- Glue Managed Compaction is not supported on Iceberg tables that use the VARIANT data type.
- AL2023 ships Python 3.9 as the system Python, but it is not supported for PySpark workloads.
- The maximum number of steps you can add or cancel per request is 100.

### Migration from EMR 7.x (Spark 3.5.x)

When migrating from EMR 7.x (which uses Spark 3.5.x) to emr-spark-8.0.0 (Spark 4.0.2), consider using the [Spark Upgrade Agent](spark-upgrades.md "spark-upgrades.md") to assist with the migration.

- **ANSI SQL mode is default** — Stricter type coercion; implicit casts that previously succeeded may now throw errors.
- **Scala 2.13** — All Spark 4.x builds use Scala 2.13. Recompile any custom JARs built against Scala 2.12.
- **JDK 17 default** — Spark 4.0.2 supports JDK 17 (default) and JDK 21 only.
- **Python 3.11 default** — Python 3.9 is no longer the default for PySpark. Verify compatibility of your Python dependencies.
- **AWS SDK** — AWS SDK v1 for Java has been removed. Update your application to use AWS SDK v2 for improved performance and resource management.
- **S3 access** — EMRFS is no longer available. Use the S3A connector to write persistent data to Amazon S3 for better performance and compatibility. See [Optimize Amazon EMR runtime for Apache Spark with EMR S3A](https://aws.amazon.com/blogs/big-data/optimize-amazon-emr-runtime-for-apache-spark-with-emr-s3a/ "https://aws.amazon.com/blogs/big-data/optimize-amazon-emr-runtime-for-apache-spark-with-emr-s3a/"). emr-s3-select has been removed.
- **Interactive Development** — JupyterHub, Zeppelin, and Hue are no longer included. For interactive Spark development, use EMR Studio, Livy, and JupyterEnterpriseGateway.
- **Separate release train** — The release label is emr-spark-8.0.0, not emr-8.0.0. This release focuses on Spark. For Flink, HBase, Phoenix, Tez, Trino, Presto, use EMR 7.x and wait for the future emr-8.0.0 multi-engine release. Pig and Oozie are not included.
- **VPC endpoint for EMR cluster communication** — Starting with Amazon EMR Spark 8.0.0, Amazon EMR on EC2 provisions a VPC endpoint in your VPC for communication between the Amazon EMR service and your cluster when launching a cluster in private subnets. Your Amazon EMR service role must include `ec2:CreateVpcEndpoint` and `ec2:ModifyVpcEndpoint` permissions, or you must create the VPC endpoint manually before launching a cluster. The VPC endpoint service name is `aws.api.`region`.emr-service-cell01`.

  - This change updates networking requirements for private subnet clusters:

    - The service access security group (`ElasticMapReduce-ServiceAccess`), attached to the VPC endpoint, requires inbound HTTPS (port 443) from the VPC CIDR block. The port 8443/9443 rules used in Amazon EMR releases 7.x and earlier are no longer required.
    - The primary instance security group requires outbound HTTPS (port 443) to the service access security group.
    - Inbound port 8443 and outbound port 9443 rules used in Amazon EMR releases 7.x and earlier are no longer required on primary, core, and task instance security groups.
    - If you use a custom VPC endpoint policy for Amazon S3, you must allow access to the Amazon EMR instance data buckets (`aws157-instance-data-0-prod-`region`` and `aws157-instance-data-1-prod-`region``).

  - For more information, see [EMR clusters in private subnets](../ManagementGuide/emr-clusters-in-a-vpc.md#emr-vpc-private-subnet "../ManagementGuide/emr-clusters-in-a-vpc.md#emr-vpc-private-subnet"), [Amazon EMR-managed security groups](../ManagementGuide/emr-man-sec-groups.md "../ManagementGuide/emr-man-sec-groups.md"), and [Minimum Amazon S3 policy for private subnet](../ManagementGuide/private-subnet-iampolicy.md "../ManagementGuide/private-subnet-iampolicy.md") in the _Amazon EMR Management Guide_.

- The following table lists the Amazon Linux release labels, kernel versions, available dates, and supported AWS Regions.

| OsReleaseLabel (Amazon Linux version) | Amazon Linux kernel version | Available date | Supported Regions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------- | --------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2023.12.20260629.0                    | 6.1.175-219.359.amzn2023    | July 22, 2026  | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Taipei), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Malaysia), Asia Pacific (Thailand), Canada (Central), Canada West (Calgary), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Mexico (Central), South America (São Paulo), China (Beijing), China (Ningxia), AWS GovCloud (US-East), AWS GovCloud (US-West) |
| 2023.12.20260611.0                    | 6.1.174-217.345.amzn2023    | July 3, 2026   | US East (N. Virginia), US East (Ohio), US West (N. California), US West (Oregon), Africa (Cape Town), Asia Pacific (Hong Kong), Asia Pacific (Taipei), Asia Pacific (Tokyo), Asia Pacific (Seoul), Asia Pacific (Osaka), Asia Pacific (Mumbai), Asia Pacific (Hyderabad), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Jakarta), Asia Pacific (Melbourne), Asia Pacific (Malaysia), Asia Pacific (Thailand), Canada (Central), Canada West (Calgary), Europe (Frankfurt), Europe (Zurich), Europe (Stockholm), Europe (Milan), Europe (Spain), Europe (Ireland), Europe (London), Europe (Paris), Israel (Tel Aviv), Mexico (Central), South America (São Paulo), China (Beijing), China (Ningxia), AWS GovCloud (US-East), AWS GovCloud (US-West) |

## emr-spark-8.0.0 default Java versions

| Application | Java / Amazon Corretto version (default is bold) |
| ----------- | ------------------------------------------------ |
| Spark       | **17**, 21                                       |
| Livy        | 17, 11, **8**                                    |
| Hadoop      | **17**, 11, 8                                    |

## emr-spark-8.0.0 component versions

The components that Amazon EMR installs with this release are listed below. Some are installed as part of big-data application packages. Others are unique to Amazon EMR and installed for system processes and features. These typically start with `emr` or `aws`. Big-data application packages in the most recent Amazon EMR release are usually the latest version found in the community. We make community releases available in Amazon EMR as quickly as possible.

Some components in Amazon EMR differ from community versions. These components have a version label in the form ``CommunityVersion`-amzn-`EmrVersion``. The `EmrVersion` starts at 0. For example, if open source community component named `myapp-component` with version 2.2 has been modified three times for inclusion in different Amazon EMR releases, its release version is listed as `2.2-amzn-2`.

| Component                   | Version            | Description                                                                                                                                 |
| --------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| adot-java-agent             | 1.31.0             | A Java Agent that collects metrics from application daemons.                                                                                |
| delta                       | 4.0.0-amzn-1-spark | Delta lake is an open table format for huge analytic datasets                                                                               |
| emr-amazon-cloudwatch-agent | 1.300032.2-amzn-0  | An application that collects internal system-level metrics and custom application metrics from Amazon EC2 instances.                        |
| emr-ddb                     | 6.0.0              | Amazon DynamoDB connector for Hadoop ecosystem applications.                                                                                |
| emr-goodies                 | 3.22.0-spark       | Extra convenience libraries for the Hadoop ecosystem.                                                                                       |
| emr-notebook-env            | 1.18.0             | Conda env for emr notebook which includes jupyter enterprise gateway                                                                        |
| emr-s3-dist-cp              | 2.44.0             | Distributed copy application optimized for Amazon S3.                                                                                       |
| hadoop-client               | 3.4.2-amzn-1       | Hadoop command-line clients such as 'hdfs', 'hadoop', or 'yarn'.                                                                            |
| hadoop-hdfs-datanode        | 3.4.2-amzn-1       | HDFS node-level service for storing blocks.                                                                                                 |
| hadoop-hdfs-library         | 3.4.2-amzn-1       | HDFS command-line client and library                                                                                                        |
| hadoop-hdfs-namenode        | 3.4.2-amzn-1       | HDFS service for tracking file names and block locations.                                                                                   |
| hadoop-hdfs-zkfc            | 3.4.2-amzn-1       | ZKFC service for tracking namenodes for HA mode.                                                                                            |
| hadoop-hdfs-journalnode     | 3.4.2-amzn-1       | HDFS service for managing the Hadoop filesystem journal on HA clusters.                                                                     |
| hadoop-httpfs-server        | 3.4.2-amzn-1       | HTTP endpoint for HDFS operations.                                                                                                          |
| hadoop-kms-server           | 3.4.2-amzn-1       | Cryptographic key management server based on Hadoop's KeyProvider API.                                                                      |
| hadoop-mapred               | 3.4.2-amzn-1       | MapReduce execution engine libraries for running a MapReduce application.                                                                   |
| hadoop-yarn-nodemanager     | 3.4.2-amzn-1       | YARN service for managing containers on an individual node.                                                                                 |
| hadoop-yarn-resourcemanager | 3.4.2-amzn-1       | YARN service for allocating and managing cluster resources and distributed applications.                                                    |
| hadoop-yarn-timeline-server | 3.4.2-amzn-1       | Service for retrieving current and historical information for YARN applications.                                                            |
| hudi                        | 1.1.0-amzn-0       | Incremental processing framework to power data pipeline at low latency and high efficiency.                                                 |
| hudi-spark                  | 1.1.0-amzn-0       | Bundle library for running Spark with Hudi.                                                                                                 |
| iceberg                     | 1.10.1-amzn-0      | Apache Iceberg is an open table format for huge analytic datasets                                                                           |
| livy-server                 | 0.8.0-incubating   | REST interface for interacting with Apache Spark                                                                                            |
| nginx                       | 1.12.1             | nginx [engine x] is an HTTP and reverse proxy server                                                                                        |
| mariadb-server              | 5.5.68+            | MariaDB database server.                                                                                                                    |
| nvidia-cuda                 | 12.5.0             | Nvidia drivers and Cuda toolkit                                                                                                             |
| r                           | 4.3.2              | The R Project for Statistical Computing                                                                                                     |
| spark-client                | 4.0.2-amzn-0       | Spark command-line clients.                                                                                                                 |
| spark-history-server        | 4.0.2-amzn-0       | Web UI for viewing logged events for the lifetime of a completed Spark application.                                                         |
| spark-on-yarn               | 4.0.2-amzn-0       | In-memory execution engine for YARN.                                                                                                        |
| spark-yarn-slave            | 4.0.2-amzn-0       | Apache Spark libraries needed by YARN slaves.                                                                                               |
| spark-rapids                | 26.02.2-amzn-0     | Nvidia Spark RAPIDS plugin that accelerates Apache Spark with GPUs.                                                                         |
| zookeeper-server            | 3.9.3-amzn-6       | Centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. |
| zookeeper-client            | 3.9.3-amzn-6       | ZooKeeper command line client.                                                                                                              |

## emr-spark-8.0.0 configuration classifications

Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `hive-site.xml`. For more information, see [Configure applications](emr-configure-apps.md "emr-configure-apps.md").

Reconfiguration actions occur when you specify a configuration for instance groups in a running cluster. Amazon EMR only initiates reconfiguration actions for the classifications that you modify. For more information, see [Reconfigure an instance group in a running cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

emr-spark-8.0.0 classifications| Classifications | Description | Reconfiguration Actions |
| --- | --- | --- |
| capacity-scheduler | Change values in Hadoop's capacity-scheduler.xml file. | Restarts the ResourceManager service. |
| container-executor | Change values in Hadoop YARN's container-executor.cfg file. | Not available. |
| container-log4j | Change values in Hadoop YARN's container-log4j.properties file. | Not available. |
| core-site | Change values in Hadoop's core-site.xml file. | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts Hadoop KMS, Hadoop Httpfs, and MapReduce-HistoryServer. |
| docker-conf | Change docker related settings. | Not available. |
| hadoop-env | Change values in the Hadoop environment for all Hadoop components. | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts MapReduce-HistoryServer. |
| hadoop-log4j | Change values in Hadoop's log4j.properties file. | Restarts the Hadoop HDFS services SecondaryNamenode, Datanode, and Journalnode.<br>Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts Hadoop KMS, Hadoop Httpfs, and MapReduce-HistoryServer. |
| hadoop-ssl-server | Change hadoop ssl server configuration | Not available. |
| hadoop-ssl-client | Change hadoop ssl client configuration | Not available. |
| hdfs-encryption-zones | Configure HDFS encryption zones. | This classification should not be reconfigured. |
| hdfs-env | Change values in the HDFS environment. | Restarts Hadoop HDFS services Namenode, Datanode, and ZKFC. |
| hdfs-site | Change values in HDFS's hdfs-site.xml. | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode.<br>Additionally restarts Hadoop Httpfs. |
| httpfs-env | Change values in the HTTPFS environment. | Restarts Hadoop Httpfs service. |
| httpfs-site | Change values in Hadoop's httpfs-site.xml file. | Restarts Hadoop Httpfs service. |
| hadoop-kms-acls | Change values in Hadoop's kms-acls.xml file. | Not available. |
| hadoop-kms-env | Change values in the Hadoop KMS environment. | Restarts Hadoop-KMS service. |
| hadoop-kms-java-home | Change Hadoop's KMS java home | Not available. |
| hadoop-kms-log4j | Change values in Hadoop's kms-log4j.properties file. | Not available. |
| hadoop-kms-site | Change values in Hadoop's kms-site.xml file. | Restarts Hadoop-KMS. |
| hudi-env | Change values in the Hudi environment. | Not available. |
| hudi-defaults | Change values in Hudi's hudi-defaults.conf file. | Not available. |
| iceberg-defaults | Change values in Iceberg's iceberg-defaults.conf file. | Not available. |
| delta-defaults | Change values in Delta's delta-defaults.conf file. | Not available. |
| jupyter-notebook-conf | Change values in Jupyter Notebook's jupyter\_notebook\_config.py file. | Not available. |
| jupyter-s3-conf | Configure Jupyter Notebook S3 persistence. | Not available. |
| jupyter-sparkmagic-conf | Change values in Sparkmagic's config.json file. | Not available. |
| livy-conf | Change values in Livy's livy.conf file. | Restarts Livy Server. |
| livy-env | Change values in the Livy environment. | Restarts Livy Server. |
| livy-log4j2 | Change Livy log4j2.properties settings. | Restarts Livy Server. |
| mapred-env | Change values in the MapReduce application's environment. | Restarts Hadoop MapReduce-HistoryServer. |
| mapred-site | Change values in the MapReduce application's mapred-site.xml file. | Restarts Hadoop MapReduce-HistoryServer. |
| spark | Amazon EMR-curated settings for Apache Spark. | This property modifies spark-defaults. See actions there. |
| spark-defaults | Change values in Spark's spark-defaults.conf file. | Restarts Spark history server and Spark thrift server. |
| spark-env | Change values in the Spark environment. | Restarts Spark history server and Spark thrift server. |
| spark-hive-site | Change values in Spark's hive-site.xml file | Not available. |
| spark-log4j2 | Change values in Spark's log4j2.properties file. | Restarts Spark history server and Spark thrift server. |
| spark-metrics | Change values in Spark's metrics.properties file. | Restarts Spark history server and Spark thrift server. |
| yarn-env | Change values in the YARN environment. | Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts MapReduce-HistoryServer. |
| yarn-site | Change values in YARN's yarn-site.xml file. | Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer.<br>Additionally restarts Livy Server and MapReduce-HistoryServer. |
| zookeeper-config | Change values in ZooKeeper's zoo.cfg file. | Restarts Zookeeper server. |
| zookeeper-logback | Change values in ZooKeeper's logback.xml file. | Restarts Zookeeper server. |
| cloudwatch-logs | Configure CloudWatch Logs integration for EMR cluster nodes. | Not available. |
| emr-metrics | Change emr metric settings for this node. | Restarts the CloudWatchAgent service. |

## EMR Spark 8.0.0 change log

Change log for EMR Spark 8.0.0| Date | Event | Description |
| --- | --- | --- |
| 2026-05-21 | Docs publication | Amazon EMR Spark 8.0.0 (emr-spark-8.0.0) release notes first published |
