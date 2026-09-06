

# Apache Flink
<a name="emr-flink"></a>

[Apache Flink](https://flink.apache.org/) is a streaming dataflow engine that you can use to run real-time stream processing on high-throughput data sources. Flink supports event time semantics for out-of-order events, exactly-once semantics, backpressure control, and APIs optimized to write both streaming and batch applications.

Additionally, Flink has connectors for third-party data sources, such as the following:
+ [Amazon Kinesis Data Streams](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kinesis/)
+ [Apache Kafka](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/kafka/)
+ [Flink Elasticsearch Connector](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/elasticsearch/)
+ [Twitter Streaming API](https://nightlies.apache.org/flink/flink-docs-release-1.14/docs/connectors/datastream/twitter/)
+ [Cassandra](https://nightlies.apache.org/flink/flink-docs-stable/docs/connectors/datastream/cassandra/)

Amazon EMR supports Flink as a YARN application so that you can manage resources along with other applications within a cluster. Flink-on-YARN allows you to submit transient Flink jobs, or you can create a long-running cluster that accepts multiple jobs and allocates resources according to the overall YARN reservation.

Flink is included in Amazon EMR release versions 5.1.0 and later.

**Note**  
Support for the `FlinkKinesisConsumer` class was added in Amazon EMR release version 5.2.1.

The following table lists the version of Flink included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Flink.

For the version of components installed with Flink in this release, see [Release 7.13.0 Component Versions](emr-7130-release.md).


**Flink version information for emr-7.13.0**  

| Amazon EMR Release Label | Flink Version | Components Installed With Flink | 
| --- | --- | --- | 
| emr-7.13.0 | Flink 1.20.0-amzn-7 | emrfs, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, flink-client, flink-jobmanager-config, hudi, delta | 

The following table lists the version of Flink included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Flink.

For the version of components installed with Flink in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md).


**Flink version information for emr-6.15.0**  

| Amazon EMR Release Label | Flink Version | Components Installed With Flink | 
| --- | --- | --- | 
| emr-6.15.0 | Flink 1.17.1-amzn-1 | emrfs, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, flink-client, flink-jobmanager-config, hudi, delta-standalone-connectors | 

The following table lists the version of Flink included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Flink.

For the version of components installed with Flink in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md).


**Flink version information for emr-5.36.2**  

| Amazon EMR Release Label | Flink Version | Components Installed With Flink | 
| --- | --- | --- | 
| emr-5.36.2 | Flink 1.14.2 | emrfs, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, flink-client, flink-jobmanager-config | 

**Topics**
+ [Creating a cluster with Flink](flink-create-cluster.md)
+ [Configuring Flink in Amazon EMR](flink-configure.md)
+ [Working with Flink jobs in Amazon EMR](flink-jobs.md)
+ [Use the Scala shell](flink-scala.md)
+ [Finding the Flink web interface](flink-web-interface.md)
+ [Flink autoscaler](flink-autoscaler.md)
+ [Optimizing job restart times for task recovery and scaling operations](flink-restart.md)
+ [Working with Flink jobs from Zeppelin in Amazon EMR](flink-zeppelin.md)
+ [Flink release history](Flink-release-history.md)