

# AWS runtime for Apache Spark (emr-spark-8.2.0)

## emr-spark-8.2.0 supported lifecycle
<a name="emr-spark820-supported-lifecycle"></a>

This release is designated as a Long Term Support (LTS) release. The following table describes the supported lifecycle dates for Amazon EMR Spark 8.2.0.


| Support phase | Date | 
| --- | --- | 
| Initial release date | November 18, 2026 | 
| Standard support until | November 17, 2029 | 
| End of life | November 18, 2029 | 

## emr-spark-8.2.0 application versions
<a name="emr-spark820-app-versions"></a>

This release includes the following applications: [AmazonCloudWatchAgent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), [Delta](https://delta.io/), [Hudi](https://hudi.apache.org), [Iceberg](https://iceberg.apache.org/), [JupyterEnterpriseGateway](https://jupyter-enterprise-gateway.readthedocs.io/en/latest/), [Livy](https://livy.incubator.apache.org/), and [Spark](https://spark.apache.org/docs/latest/).

The table below lists the application versions available in this release of Amazon EMR and the application versions in the preceding three Amazon EMR releases (when applicable).

For a comprehensive history of application versions for each release of Amazon EMR, see the following topics:
+ [Application versions in Amazon EMR 7.x releases](emr-release-app-versions-7.x.md)
+ [Application versions in Amazon EMR 6.x releases](emr-release-app-versions-6.x.md)
+ [Application versions in Amazon EMR 5.x releases](emr-release-app-versions-5.x.md)
+ [Application versions in Amazon EMR 4.x releases](emr-release-app-versions-4.x.md)


**Application version information**  

|  | emr-spark-8.2.0 | emr-spark-8.1.0 | 
| --- | --- | --- | 
| AWS SDK for Java | 2.55.8 | 2.44.5 | 
| Python | 3.11, 3.13 | 3.11, 3.13 | 
| Scala | 2.13.17 | 2.13.17 | 
| AmazonCloudWatchAgent | 1.300034.0-amzn-0 | 1.300034.0-amzn-0 | 
| Delta | 4.2.0-amzn-0 | 4.2.0-amzn-0 | 
| Hudi | 1.1.1-amzn-0 | 1.1.1-amzn-0 | 
| Iceberg | 1.11.0-amzn-0 | 1.11.0-amzn-0 | 
| JupyterEnterpriseGateway | 2.6.0 | 2.6.0 | 
| Livy | 0.9.0-incubating | 0.9.0-incubating | 
| Spark | 4.1.3-amzn-0 | 4.1.1-amzn-0 | 
| NVIDIA cuDF plugin for Apache Spark (GPU) | 26.08.1-amzn-0 | 26.04.2-amzn-0 | 

## emr-spark-8.2.0 release notes
<a name="emr-spark820-relnotes"></a>

The following release notes include information for Amazon EMR release 8.2.0 (emr-spark-8.2.0), featuring Apache Spark 4.1.3.

### What's new
<a name="emrspark820-whatsnew"></a>
+ **Apache Spark 4.1.3** — Amazon EMR Spark 8.2.0 includes Apache Spark 4.1.3. Updated dependencies include Apache ORC 2.2.2 and AWS SDK for Java v2 2.55.8, along with new Spark features, performance improvements, and bug fixes. For GPU workloads, Amazon EMR Spark 8.2.0 supports version 26.08.1 of the NVIDIA cuDF plugin for Apache Spark (formerly the RAPIDS Accelerator for Apache Spark).
+ **Concurrent Delta Lake writes on Amazon S3 from multiple clusters** — You can now write to the same Delta Lake table on Amazon S3 from multiple Spark jobs or clusters at the same time, without the Amazon DynamoDB-based log store. Delta commits use Amazon S3 conditional writes. When two writers commit at the same time, only one commit succeeds. The other writer receives a standard Delta commit conflict, which it can retry.
+ **Materialized view enhancements** — This release includes the following improvements for materialized views in the AWS Glue Data Catalog:
  + **Incremental refresh** — Materialized views can refresh incrementally and fall back to a full refresh when needed. On Iceberg v3 tables, materialized views without aggregations, such as projections, filters, and inner joins, now refresh incrementally by default, whether the refresh is triggered manually or automatically. Materialized views over Hive Parquet base tables can refresh incrementally for append-only changes.
  + **Fine-grained access control** — On clusters with AWS Lake Formation fine-grained access control (FGAC), you can create and refresh Iceberg materialized views in the AWS Glue Data Catalog. The base tables' row filters and column masks are applied, based on the FGAC policies of the view's definer. Because a materialized view is an Iceberg table, you can also define FGAC policies on the materialized view itself for additional protection.
  + **Spark Declarative Pipelines** — Materialized views defined in Spark Declarative Pipelines can now be stored as Iceberg materialized views in the AWS Glue Data Catalog. Unlike materialized views created with SQL, a pipeline run leaves them unchanged when their definition and sources haven't changed. Otherwise, the pipeline refreshes them incrementally when possible. To opt in, set `spark.sql.pipelines.materializedView.implWithGlueIcebergMVMode` to `GLUE_ICEBERG_MV_PREFERRED`. Refresh skipping and incremental refresh also require `spark.sql.optimizer.incrementalMVRefresh.enabled` set to `true`. The setting applies to materialized views that the pipeline creates after you opt in. A view that can't be stored as an AWS Glue materialized view is created as a regular AWS Glue Iceberg table, as before.
  + **Schema evolution** — Materialized views now support schema evolution with `CREATE OR REPLACE`.
+ **Governed custom user-defined functions with Lake Formation fine-grained access control** — Spark jobs on clusters that use Lake Formation FGAC can now call administrator-approved custom user-defined functions (UDFs) packaged as Lake Formation custom code artifacts. Approved artifact JARs load automatically when the application starts, so you no longer pass them with `--jars`. Row filters can call these functions by their database-qualified name, and queries that call unapproved functions are rejected. Governed UDFs work in Spark Connect sessions and when the driver runs on a core node. Cluster operators can turn off governed UDFs, limit which AWS Glue UDFs are allowed, and configure how long Lake Formation access contexts last and when they refresh. The job's execution role needs the `lakeformation:GetTemporaryGlueFunctionCredentials` permission.
+ **Trusted identity propagation for steps, sessions, and live UIs** — Steps and interactive sessions (Spark Connect and Livy) can now carry IAM Identity Center trusted identity context into the runtime role sessions that Amazon EMR assumes on your behalf. This works on clusters that use runtime roles, IAM Identity Center, or Lake Formation FGAC. Downstream services, including Lake Formation and Amazon S3 Access Grants, can then authorize and audit access as the original user. Running steps and sessions pick up refreshed identity context without being relaunched. The persistent Spark History Server now shows each user as the owner of their completed applications.

  Amazon EMR also removes the temporary operating system user that it creates for each workload, along with that user's HDFS home directory and credentials, shortly after the application finishes. This cleanup is on by default. To turn it off, set `emr.secretagent.users.teardown.enabled` to `false`.
+ **Spark Connect on multi-primary clusters** — Amazon EMR now supports Spark Connect sessions on multi-primary clusters running emr-spark-8.2.0 and later.
+ **New S3A settings for EMRFS-to-S3A migration** — Two new opt-in parameters, `fs.s3a.emrfs.compatibility.folder.marker.as.dir` and `fs.s3a.emrfs.compatibility.marker.empty`, help you migrate from EMRFS to S3A. Both parameters default to `false`.
+ **More Iceberg operations under fine-grained access control** — On clusters with Lake Formation FGAC, you can now run `ALTER TABLE ... SET LOCATION`, `ALTER TABLE ... WRITE ORDERED BY`, `ALTER TABLE ... WRITE DISTRIBUTED BY`, and the `add_files` and `register_table` procedures on Iceberg tables.
+ **Spark Connect and Amazon S3 enhancements under fine-grained access control** — On clusters with Lake Formation FGAC, Spark Connect sessions support more query plans and expressions, including creating SQL user-defined functions. Jobs can also set a custom AWS KMS encryption context for Amazon S3 server-side encryption and add custom S3A request headers.
+ **Lineage capture for Spark jobs** — Amazon EMR 8.2.0 adds the `glue-openlineage-spark` library, which automatically captures OpenLineage-compatible lineage from Apache Spark jobs and publishes it to the AWS Glue Data Catalog or a custom transport. Captured lineage includes input and output datasets and columns, schemas, user identity, and more. This library replaces the `datazone-openlineage-spark` library. It's installed at a fixed path that doesn't include a version number, so Spark configurations that reference it continue to work after you upgrade.
+ **Spark Operator version 2 on Amazon EMR on EKS** — The Spark Operator for Amazon EMR on EKS is upgraded to version 2, based on open-source Spark Operator 2.5.0. For more information, see the Amazon EMR on EKS emr-spark-8.2.0 release notes.
+ **Trusted identity propagation on Amazon EMR on EKS** — Amazon EMR on EKS now supports trusted identity propagation for IAM federated users, for both batch jobs and interactive Spark Connect and Livy sessions. For more information, see the Amazon EMR on EKS emr-spark-8.2.0 release notes.

### Changes, enhancements, and resolved issues
<a name="emrspark820-changes"></a>
+ **Lake Formation fine-grained access control fixes** — Fixed Spark queries on clusters that use Lake Formation FGAC that could fail with `AccessDeniedException` when reading AWS Glue Data Catalog tables, loading Lake Formation-governed Iceberg tables, or reading tables with enhanced row-level security policies. Row and cell filters that use double-quoted column names, including reserved words and names with spaces, dots, or backticks, now work. Full table access now applies to DataSource V2 reads. Jobs with FGAC no longer fail when writing to Amazon S3 through the S3A committers, including magic committer multipart uploads. Spark no longer re-fetches access rules that it already has, which reduces query planning overhead.
+ **Expanded Spark support under fine-grained access control** — More Spark SQL features now work on clusters with FGAC. These include `uuid()`, variant expressions, column default values, typed null literals, the HyperLogLog sketch functions (`hll_sketch_agg`, `hll_union_agg`, `hll_sketch_estimate`, and `hll_union`), typed Datasets and user-defined function encoders, and Apache Hudi incremental and change data queries (`hudi_table_changes`). Jobs can also set more Spark configuration options, including the AWS Glue catalog separator, the parallelism for parallel partition discovery, and the legacy setting that allows `CREATE TABLE AS SELECT` into a non-empty location. Classes and settings that were allowed in earlier releases are restored, so workloads behave the same way on newer releases.
+ **Secret Agent scaling and reliability** — Amazon EMR improves its credential service (Secret Agent) in the following ways:
  + The CPU cap is removed by default. You can still set one with `emr.secretagent.cpu.quota.percent`.
  + Connections between nodes are reused instead of opened for each call.
  + User provisioning latency is reduced by up to 97% under high job concurrency on clusters with runtime roles.
  + Fixed a deadlock in the credential cache that could stall jobs and Livy sessions while they waited for credentials.
  + Fixed a TLS handshake error that caused FGAC jobs to fail on clusters whose nodes use a custom private DNS domain.
+ **Failure reason for external Hive metastore connection errors** — Amazon EMR now reports the correct failure reason when a cluster fails to launch because it can't connect to an external Hive metastore. Previously, this failure was reported as a generic error.
+ **Cluster and step management fixes** — Steps are handled more safely when a primary node is patched, replaced, or fails over. Running steps finish or are cleanly canceled, and steps aren't run twice. On multi-primary clusters, patching confirms a healthy quorum before and after services stop, and the cluster can recover when two of its three primary nodes fail. The primary node no longer restarts repeatedly at startup, clusters can start faster, and a rare race condition that could prevent the primary node from finishing startup is fixed. Errors during primary node decommissioning are now reported instead of being treated as successes. Bootstrap action logs no longer show a false failure when all actions succeed, and steps that fail during step user setup show a clear failure reason in `DescribeStep` and `ListSteps`. Running many steps at once is faster, and a canceled pending step can no longer start running.
+ **Faster log delivery** — Amazon EMR now publishes step logs to Amazon S3 as soon as a step reaches a terminal state, instead of waiting for the next periodic upload. You can also publish YARN container logs as soon as a container or application reaches a terminal state. To turn this on, set `yarn.emr.logpush.notify.enabled` to `true` in the `yarn-site` configuration classification. This option is off by default. This release also improves cluster reliability by cleaning up disk space on the `/emr` volume more reliably on long-running clusters.
+ **S3A fixes** — This release includes the following S3A fixes:
  + Restored S3A support for AWS KMS encryption context (backport of HADOOP-19197). Delegation tokens remain compatible with earlier Amazon EMR releases.
  + Fixed S3A credential provider lookup to use the correct class loader when loading custom provider classes from user JARs when `fs.s3a.classloader.isolation` is set to `false` (backport of HADOOP-19733).
  + Fixed S3A ignoring the configured upload checksum algorithm (`fs.s3a.create.checksum.algorithm`) for requests made through a credentials resolver (`fs.s3a.credentials.resolver`).
  + Fixed S3A client-side encryption (CSE) ranged reads that returned truncated data or incorrect lengths.
  + Fixed the S3A magic committer V2 running with 8 threads by default instead of the intended 32 (`fs.s3a.committer.threads`).
  + Fixed cross-Region S3 bucket access that failed with HTTP 301 errors. When neither `fs.s3a.endpoint` nor `fs.s3a.endpoint.region` is set, the Region from a regional `fs.s3n.endpoint` is now mapped to `fs.s3a.endpoint.region` instead of `fs.s3a.endpoint`.
+ **Clusters launched from Amazon Linux minimal AMIs** — Fixed an issue where clusters that use a custom AMI based on an Amazon Linux minimal AMI could fail to start because system utilities needed during node setup weren't installed.
+ **YARN ResourceManager recovery turned on by default** — Amazon EMR now turns on the Apache Hadoop YARN `yarn.resourcemanager.recovery.enabled` configuration by default, so running applications are more resilient to a YARN ResourceManager restart.
+ **Secondary private IP address on the primary node** — On clusters with a single primary node, Amazon EMR now attaches a secondary private IP address to the primary node and configures the cluster daemons to receive traffic on both private IP addresses. We recommend that you use the secondary private IP address when you need to communicate with the primary node.
+ **Cassandra daemon heap usage** — Amazon EMR 8.2.0 optimizes the heap memory that the Cassandra daemon uses during compaction. Previously, the heap could be exhausted on long-running clusters and cause step or cluster failures.
+ **JupyterHub MERGE reconfiguration** — On clusters with JupyterHub, MERGE reconfiguration requests that change only other classifications, such as `yarn-site`, now succeed. The JupyterHub health check continues to use the cluster's configured port.

### Known issues and limitations
<a name="emrspark820-known-issues"></a>
+ **Unexpected error message when you lack AWS Lake Formation permissions in fine-grained access control mode** – On Amazon EMR on EC2 clusters that use Lake Formation fine-grained access control, you might not have access to a Lake Formation registered table. In this case, the query fails with the following error message:

  ```
  org.sparkproject.fgac.grpc.StatusRuntimeException: INTERNAL
  ```

  The expected error message is the following:

  ```
  org.apache.spark.fgac.error.AccessDeniedException: Unable to verify existence of default database: ... Insufficient Lake Formation permission(s): Required Describe on default
  ```
+ **Iceberg catalogs defined in the cluster's spark-defaults classification fail** – On Amazon EMR on EC2 clusters that use Lake Formation fine-grained access control, every read through an Apache Iceberg catalog that you define in the cluster's `spark-defaults` classification fails during table resolution. This affects both a named `SparkCatalog` and the `spark_catalog` override that uses `SparkSessionCatalog`. The query fails with the following error message:

  ```
  SparkFGACException: Spark FGAC experienced an internal error
  ```

  The same catalog keys work when you pass them for each step with `--conf`.

  Workaround: Remove `catalog-impl` from the cluster's `spark-defaults` classification.
+ **PySpark PyPI package import failures** – On Amazon EMR on EC2, `emr-spark-8.2.0` installs the Python 3.11 libraries (for example, `boto3` and `cycler`) outside the search path of `/usr/bin/python3.11`, so PySpark can't import them. Code that imports these libraries fails, and so do `sc.install_pypi_package` and Livy sessions that install PyPI packages, including Amazon SageMaker Unified Studio sessions that use Library Management. The failure shows an error such as `ModuleNotFoundError: No module named 'six'`. Amazon EMR Serverless and Amazon EMR on EKS aren't affected.

  Workaround: When you create your cluster, add the `emr-8-2-pypi-ba.sh` bootstrap action from the [aws-emr-utilities](https://github.com/aws-samples/aws-emr-utilities/tree/main/utilities/emr-spark-8-2-0) repository on GitHub. The bootstrap action installs these libraries for `/usr/bin/python3.11` and keeps the versions that the release already ships.

## emr-spark-8.2.0 default Java versions
<a name="emr-spark820-jdk"></a>


| Application | Java / Amazon Corretto version (default is bold) | 
| --- | --- | 
| Spark | 17, 21 | 
| Livy | 17, 11, 8 | 
| Hadoop | 17, 11, 8 | 

## emr-spark-8.2.0 component versions
<a name="emr-spark820-components"></a>

The components that Amazon EMR installs with this release are listed below. Some are installed as part of big-data application packages. Others are unique to Amazon EMR and installed for system processes and features. These typically start with `emr` or `aws`. Big-data application packages in the most recent Amazon EMR release are usually the latest version found in the community. We make community releases available in Amazon EMR as quickly as possible.

Some components in Amazon EMR differ from community versions. These components have a version label in the form `{{CommunityVersion}}-amzn-{{EmrVersion}}`. The `{{EmrVersion}}` starts at 0. For example, if open source community component named `myapp-component` with version 2.2 has been modified three times for inclusion in different Amazon EMR releases, its release version is listed as `2.2-amzn-2`.


| Component | Version | Description | 
| --- | --- | --- | 
| adot-java-agent | 1.31.0 | A Java Agent that collects metrics from application daemons. | 
| delta | 4.2.0-amzn-0 | Delta lake is an open table format for huge analytic datasets | 
| emr-amazon-cloudwatch-agent | 1.300034.0-amzn-0 | An application that collects internal system-level metrics and custom application metrics from Amazon EC2 instances. | 
| emr-ddb | 6.1.0 | Amazon DynamoDB connector for Hadoop ecosystem applications. | 
| emr-goodies | 3.23.0-spark | Extra convenience libraries for the Hadoop ecosystem. | 
| emr-notebook-env | 1.18.0 | Conda env for emr notebook which includes jupyter enterprise gateway | 
| emr-s3-dist-cp | 2.46.0 | Distributed copy application optimized for Amazon S3. | 
| hadoop-client | 3.4.2-amzn-3 | Hadoop command-line clients such as 'hdfs', 'hadoop', or 'yarn'. | 
| hadoop-hdfs-datanode | 3.4.2-amzn-3 | HDFS node-level service for storing blocks. | 
| hadoop-hdfs-library | 3.4.2-amzn-3 | HDFS command-line client and library | 
| hadoop-hdfs-namenode | 3.4.2-amzn-3 | HDFS service for tracking file names and block locations. | 
| hadoop-hdfs-zkfc | 3.4.2-amzn-3 | ZKFC service for tracking namenodes for HA mode. | 
| hadoop-hdfs-journalnode | 3.4.2-amzn-3 | HDFS service for managing the Hadoop filesystem journal on HA clusters. | 
| hadoop-httpfs-server | 3.4.2-amzn-3 | HTTP endpoint for HDFS operations. | 
| hadoop-kms-server | 3.4.2-amzn-3 | Cryptographic key management server based on Hadoop's KeyProvider API. | 
| hadoop-mapred | 3.4.2-amzn-3 | MapReduce execution engine libraries for running a MapReduce application. | 
| hadoop-yarn-nodemanager | 3.4.2-amzn-3 | YARN service for managing containers on an individual node. | 
| hadoop-yarn-resourcemanager | 3.4.2-amzn-3 | YARN service for allocating and managing cluster resources and distributed applications. | 
| hadoop-yarn-timeline-server | 3.4.2-amzn-3 | Service for retrieving current and historical information for YARN applications. | 
| hudi | 1.1.1-amzn-0 | Incremental processing framework to power data pipeline at low latency and high efficiency. | 
| hudi-spark | 1.1.1-amzn-0 | Bundle library for running Spark with Hudi. | 
| iceberg | 1.11.0-amzn-0 | Apache Iceberg is an open table format for huge analytic datasets | 
| livy-server | 0.9.0-incubating | REST interface for interacting with Apache Spark | 
| nginx | 1.12.1 | nginx [engine x] is an HTTP and reverse proxy server | 
| mariadb-server | 5.5.68\+ | MariaDB database server. | 
| nvidia-cuda | 12.5.0 | Nvidia drivers and Cuda toolkit | 
| r | 4.3.2 | The R Project for Statistical Computing | 
| spark-client | 4.1.3-amzn-0 | Spark command-line clients. | 
| spark-history-server | 4.1.3-amzn-0 | Web UI for viewing logged events for the lifetime of a completed Spark application. | 
| spark-on-yarn | 4.1.3-amzn-0 | In-memory execution engine for YARN. | 
| spark-yarn-slave | 4.1.3-amzn-0 | Apache Spark libraries needed by YARN slaves. | 
| spark-rapids | 26.08.1-amzn-0 | Nvidia Spark RAPIDS plugin that accelerates Apache Spark with GPUs. | 
| zookeeper-server | 3.9.3-amzn-8 | Centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. | 
| zookeeper-client | 3.9.3-amzn-8 | ZooKeeper command line client. | 

## emr-spark-8.2.0 configuration classifications
<a name="emr-spark820-class"></a>

Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `hive-site.xml`. For more information, see [Configure applications](emr-configure-apps.md).

Reconfiguration actions occur when you specify a configuration for instance groups in a running cluster. Amazon EMR only initiates reconfiguration actions for the classifications that you modify. For more information, see [Reconfigure an instance group in a running cluster](emr-configure-apps-running-cluster.md).


**emr-spark-8.2.0 classifications**  

| Classifications | Description | Reconfiguration Actions | 
| --- | --- | --- | 
| capacity-scheduler | Change values in Hadoop's capacity-scheduler.xml file. | Restarts the ResourceManager service. | 
| container-executor | Change values in Hadoop YARN's container-executor.cfg file. | Not available. | 
| container-log4j | Change values in Hadoop YARN's container-log4j.properties file. | Not available. | 
| core-site | Change values in Hadoop's core-site.xml file. | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode. Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer. Additionally restarts Hadoop KMS, Hadoop Httpfs, and MapReduce-HistoryServer. | 
| docker-conf | Change docker related settings. | Not available. | 
| hadoop-env | Change values in the Hadoop environment for all Hadoop components. | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode. Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer. Additionally restarts MapReduce-HistoryServer. | 
| hadoop-log4j | Change values in Hadoop's log4j.properties file. | Restarts the Hadoop HDFS services SecondaryNamenode, Datanode, and Journalnode. Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer. Additionally restarts Hadoop KMS, Hadoop Httpfs, and MapReduce-HistoryServer. | 
| hadoop-ssl-server | Change hadoop ssl server configuration | Not available. | 
| hadoop-ssl-client | Change hadoop ssl client configuration | Not available. | 
| hdfs-encryption-zones | Configure HDFS encryption zones. | This classification should not be reconfigured. | 
| hdfs-env | Change values in the HDFS environment. | Restarts Hadoop HDFS services Namenode, Datanode, and ZKFC. | 
| hdfs-site | Change values in HDFS's hdfs-site.xml. | Restarts the Hadoop HDFS services Namenode, SecondaryNamenode, Datanode, ZKFC, and Journalnode. Additionally restarts Hadoop Httpfs. | 
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
| yarn-env | Change values in the YARN environment. | Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer. Additionally restarts MapReduce-HistoryServer. | 
| yarn-site | Change values in YARN's yarn-site.xml file. | Restarts the Hadoop YARN services ResourceManager, NodeManager, ProxyServer, and TimelineServer. Additionally restarts Livy Server and MapReduce-HistoryServer. | 
| zookeeper-config | Change values in ZooKeeper's zoo.cfg file. | Restarts Zookeeper server. | 
| zookeeper-logback | Change values in ZooKeeper's logback.xml file. | Restarts Zookeeper server. | 
| cloudwatch-logs | Configure CloudWatch Logs integration for EMR cluster nodes. | Not available. | 
| emr-metrics | Change emr metric settings for this node. | Restarts the CloudWatchAgent service. | 

## Amazon EMR Spark 8.2.0 change log
<a name="emrspark820-changelog"></a>


**Change log for Amazon EMR Spark 8.2.0**  

| Date | Event | Description | 
| --- | --- | --- | 
| 2026-11-18 | Docs publication | Amazon EMR Spark 8.2.0 (emr-spark-8.2.0) release notes first published | 