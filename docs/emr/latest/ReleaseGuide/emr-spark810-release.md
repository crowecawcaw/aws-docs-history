

# AWS runtime for Apache Spark (emr-spark-8.1.0)
<a name="emr-spark810-release"></a>

## emr-spark-8.1.0 supported lifecycle
<a name="emr-spark810-supported-lifecycle"></a>

This release is designated as a Long Term Support (LTS) release. The following table describes the supported lifecycle dates for Amazon EMR Spark 8.1.0.


| Support phase | Date | 
| --- | --- | 
| Initial release date | September 8, 2026 | 
| Standard support until | September 7, 2029 | 
| End of life | September 8, 2029 | 

## emr-spark-8.1.0 application versions
<a name="emr-spark810-app-versions"></a>

This release includes the following applications: [AmazonCloudWatchAgent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), [Delta](https://delta.io/), [Hudi](https://hudi.apache.org), [Iceberg](https://iceberg.apache.org/), [JupyterEnterpriseGateway](https://jupyter-enterprise-gateway.readthedocs.io/en/latest/), [Livy](https://livy.incubator.apache.org/), and [Spark](https://spark.apache.org/docs/latest/).

The table below lists the application versions available in this release of Amazon EMR and the application versions in the preceding three Amazon EMR releases (when applicable).

For a comprehensive history of application versions for each release of Amazon EMR, see the following topics:
+ [Application versions in Amazon EMR 7.x releases](emr-release-app-versions-7.x.md)
+ [Application versions in Amazon EMR 6.x releases](emr-release-app-versions-6.x.md)
+ [Application versions in Amazon EMR 5.x releases](emr-release-app-versions-5.x.md)
+ [Application versions in Amazon EMR 4.x releases](emr-release-app-versions-4.x.md)


**Application version information**  

|  | emr-spark-8.1.0 | emr-spark-8.0.0 | 
| --- | --- | --- | 
| AWS SDK for Java | 2.44.5 | 2.41.32 | 
| Python | 3.11, 3.13 | 3.11, 3.13 | 
| Scala | 2.13.17 | 2.13.16 | 
| AmazonCloudWatchAgent | 1.300034.0-amzn-0 | 1.300032.2-amzn-0 | 
| Delta | 4.2.0-amzn-0 | 4.0.0-amzn-1-spark | 
| Hudi | 1.1.1-amzn-0 | 1.1.0-amzn-0 | 
| Iceberg | 1.11.0-amzn-0 | 1.10.1-amzn-0 | 
| JupyterEnterpriseGateway | 2.6.0 | 2.6.0 | 
| Livy | 0.9.0-incubating | 0.8.0-incubating | 
| Spark | 4.1.1-amzn-0 | 4.0.2-amzn-0 | 

## emr-spark-8.1.0 release notes
<a name="emr-spark810-relnotes"></a>

The following release notes include information for Amazon EMR release 8.1.0 (emr-spark-8.1.0), featuring Apache Spark 4.1.1.

### What's new
<a name="emrspark810-whatsnew"></a>
+ **Apache Spark 4.1.1** — Amazon EMR Spark 8.1.0 includes Apache Spark 4.1.1. Updated dependencies include Scala 2.13.17, Jackson 2.20.0, and Parquet-MR 1.16.0, along with new Spark features, performance improvements, and bug fixes.
+ **Iceberg v3 spec support for Spark workloads** — Amazon EMR Spark 8.1.0 extends Iceberg v3 spec support for Spark workloads. This release adds the following v3 capabilities:
  + **Geospatial data types** — Iceberg v3 tables support the `GEOMETRY` and `GEOGRAPHY` data types.
  + **Geospatial SQL functions** — Amazon EMR Spark 8.1.0 natively supports geospatial functions for Iceberg workloads. Set `spark.sql.geospatial.enabled` to `true` in your Spark configuration to enable geospatial functions. Apache Spark 4.1 supports SRID 0, 3857, and 4326 only. The following functions are supported:
    + `st_area(geom)`
    + `st_asbinary(geo[, endianness])`
    + `st_collect(geoArray)`
    + `st_convexhull(geom)`
    + `st_distance(geom1, geom2)`
    + `st_dwithin(geom1, geom2, distance)`
    + `st_geogfromwkb(wkb)`
    + `st_geomfromwkb(wkb[, srid])`
    + `st_geomfromwkt(wkt[, srid])`
    + `st_intersection(geom1, geom2)`
    + `st_intersects(geom1, geom2)`
    + `st_length(geom)`
    + `st_makeline(geomArray)`
    + `st_setsrid(geo, srid)`
    + `st_srid(geo)`
    + `st_within(geom1, geom2)`
    + `st_x(point)`
    + `st_y(point)`
  + **Nanosecond-precision timestamps** — Iceberg v3 tables support nanosecond-precision timestamp columns (`TIMESTAMP(9)` and `TIMESTAMP_NTZ(9)`).
  + **Variant shredding** — Iceberg v3 tables support variant shredding.
  + **`UNKNOWN` data type** — Iceberg v3 tables support the `UNKNOWN` data type for columns whose type is not yet defined. Columns of this type are optional, default to null, and are not stored in data files.
  + **Default values** — Iceberg v3 columns support declared default values, which apply when a writer omits the column.
+ **Extended fine-grained access control support for open table formats** — Amazon EMR Spark 8.1.0 extends fine-grained access control (FGAC) support for open table formats (OTFs). Iceberg now supports FGAC for additional operations: `DESCRIBE TABLE`, `SHOW TBLPROPERTIES`, `SHOW CREATE TABLE`, `ALTER TABLE table_name WRITE ORDERED BY`, and `ALTER TABLE table_name WRITE DISTRIBUTED BY`. Delta Lake now supports FGAC for the `VACUUM` operation.
+ **Incremental refresh improvements for Iceberg materialized views** — Incremental refresh now supports Merge-on-Read tables through change data capture. This enables fast refreshes for workloads that use updates and deletes. Refresh reads only the data files affected by a change, using per-file and manifest-level column statistics.
+ **Multi-format multi-catalog support with auto-discovery** — Spark SQL queries can now reference catalogs by name without pre-registering them in Spark configuration. Supported catalog types include cross-account catalogs and S3 Tables federated catalogs, with automatic detection of Iceberg, Delta, and Hudi table formats. To enable this feature, add the following Spark configuration: `"spark.sql.catalog.spark_catalog": "org.apache.spark.sql.connector.catalog.redirecting.RedirectingSessionCatalog", "spark.sql.catalogResolver": "com.amazonaws.glue.catalog.redirecting.GlueCatalogResolver"`

### Changes, enhancements, and resolved issues
<a name="emrspark810-changes"></a>
+ This release includes bug fixes and feature improvements for Iceberg, Hudi, and Delta. For more information, see the What's new section.
+ **Improved disk encryption verification tolerance during cluster startup** — Clusters with local disk encryption enabled in their security configuration are now more tolerant of transient network connectivity delays during instance boot. This change reduces intermittent cluster startup failures.
+ **Fixed UTF-8 multibyte character handling in Amazon EMR configurations** — Amazon EMR configurations now correctly support UTF-8 multibyte characters. This includes values with accented letters or non-Latin scripts. For more information, see [Configure applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html).
+ **Improved Secret Agent startup reliability** — Fixes two issues that could cause Amazon EMR cluster provisioning failures related to the Secret Agent security service. Certificate creation now waits for HDFS readiness before proceeding, and the startup script retries detection of the Secret Agent Java process. Together these changes reduce launch failures on clusters with slower storage initialization or heavily loaded instances.

### Known issues and limitations
<a name="emrspark810-known-issues"></a>
+ Native Apache Iceberg table encryption is applied only when you use the Hive Metastore or an Iceberg REST catalog. With the AWS Glue Data Catalog (including its Iceberg REST endpoint) and the Hadoop catalog, these properties are accepted but not enforced. As a result, data is written in plaintext. To encrypt Iceberg table data at rest with these catalogs, enable Amazon S3 server-side encryption with AWS KMS keys (SSE-KMS) on the table's Amazon S3 location.
+ Transforms that take more than one argument are not supported for Iceberg v3 tables.

## emr-spark-8.1.0 default Java versions
<a name="emr-spark810-jdk"></a>


| Application | Java / Amazon Corretto version (default is bold) | 
| --- | --- | 
| Spark | 17, 21 | 
| Livy | 17, 11, 8 | 
| Hadoop | 17, 11, 8 | 

## emr-spark-8.1.0 component versions
<a name="emr-spark810-components"></a>

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
| spark-client | 4.1.1-amzn-0 | Spark command-line clients. | 
| spark-history-server | 4.1.1-amzn-0 | Web UI for viewing logged events for the lifetime of a completed Spark application. | 
| spark-on-yarn | 4.1.1-amzn-0 | In-memory execution engine for YARN. | 
| spark-yarn-slave | 4.1.1-amzn-0 | Apache Spark libraries needed by YARN slaves. | 
| spark-rapids | 26.04.2-amzn-0 | Nvidia Spark RAPIDS plugin that accelerates Apache Spark with GPUs. | 
| zookeeper-server | 3.9.3-amzn-8 | Centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. | 
| zookeeper-client | 3.9.3-amzn-8 | ZooKeeper command line client. | 

## emr-spark-8.1.0 configuration classifications
<a name="emr-spark810-class"></a>

Configuration classifications allow you to customize applications. These often correspond to a configuration XML file for the application, such as `hive-site.xml`. For more information, see [Configure applications](emr-configure-apps.md).

Reconfiguration actions occur when you specify a configuration for instance groups in a running cluster. Amazon EMR only initiates reconfiguration actions for the classifications that you modify. For more information, see [Reconfigure an instance group in a running cluster](emr-configure-apps-running-cluster.md).


**emr-spark-8.1.0 classifications**  

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

## Amazon EMR Spark 8.1.0 change log
<a name="emrspark810-changelog"></a>


**Change log for Amazon EMR Spark 8.1.0**  

| Date | Event | Description | 
| --- | --- | --- | 
| 2026-09-08 | Docs publication | Amazon EMR Spark 8.1.0 (emr-spark-8.1.0) release notes first published | 