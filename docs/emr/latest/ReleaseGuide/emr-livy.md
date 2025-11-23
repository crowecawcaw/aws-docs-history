# Apache Livy

Livy enables interaction over a REST interface with an EMR cluster running Spark. You can use the REST interface or an RPC client library to submit Spark jobs or snippets of Spark code, retrieve results synchronously or asynchronously, and manage Spark Context. For more information, see the [Apache Livy website](https://livy.incubator.apache.org/ "https://livy.incubator.apache.org/"). Livy is included in Amazon EMR release version 5.9.0 and later.

To access the Livy web interface, set up an SSH tunnel to the master node and a proxy connection. For more information, see [View web interfaces hosted on EMR clusters](../ManagementGuide/emr-web-interfaces.md "../ManagementGuide/emr-web-interfaces.md").

The following table lists the version of Livy included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Livy.

For the version of components installed with Livy in this release, see [Release 7.12.0 Component Versions](emr-7120-release.md "emr-7120-release.md").

| Livy version information for emr-7.12.0 | Amazon EMR Release Label | Livy Version                                                                                                                                                                                                                                                                                                                                      | Components Installed With Livy |
| --------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| emr-7.12.0                              | Livy 0.8.0-incubating    | emrfs, emr-goodies, emr-ddb, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hudi, hudi-spark, r, spark-client, spark-history-server, spark-on-yarn, spark-yarn-slave, livy-server, nginx |

The following table lists the version of Livy included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Livy.

For the version of components installed with Livy in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Livy version information for emr-6.15.0 | Amazon EMR Release Label | Livy Version                                                                                                                                                                                                                                                                                                                                             | Components Installed With Livy |
| --------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| emr-6.15.0                              | Livy 0.7.1-incubating    | aws-sagemaker-spark-sdk, emrfs, emr-goodies, emr-ddb, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hudi, hudi-spark, r, spark-client, spark-history-server, spark-on-yarn, spark-yarn-slave, livy-server, nginx |

The following table lists the version of Livy included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Livy.

For the version of components installed with Livy in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Livy version information for emr-5.36.2 | Amazon EMR Release Label | Livy Version                                                                                                                                                                                                                                                                                                                                             | Components Installed With Livy |
| --------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| emr-5.36.2                              | Livy 0.7.1-incubating    | aws-sagemaker-spark-sdk, emrfs, emr-goodies, emr-ddb, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hudi, hudi-spark, r, spark-client, spark-history-server, spark-on-yarn, spark-yarn-slave, livy-server, nginx |

###### Topics

- [Enabling HTTPS with Apache Livy](enabling-https.md "enabling-https.md")
- [Livy release history](Livy-release-history.md "Livy-release-history.md")
