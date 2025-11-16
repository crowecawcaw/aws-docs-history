# Apache Tez

Apache Tez is a framework that creates a complex directed acyclic graph (DAG) of tasks for
processing data. You can use it as an alternative to Hadoop MapReduce for some use cases.
For example, you can run Pig and Hive workflows with Hadoop MapReduce or you can use Tez as
an execution engine. For more information, see [https://tez.apache.org/](https://tez.apache.org/ "https://tez.apache.org/"). Amazon EMR releases 4.7.0 and higher include Tez.

The following table lists the version of Tez included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Tez.

For the version of components installed with Tez in this release, see [Release 7.11.0 Component Versions](emr-7110-release.md "emr-7110-release.md").

| Tez version information for emr-7.11.0 | Amazon EMR Release Label | Tez Version                                                                                                                                                                                                                                                           | Components Installed With Tez |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| emr-7.11.0                             | Tez 0.10.2-amzn-18       | emrfs, emr-goodies, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, tez-on-yarn, tez-on-worker |

The following table lists the version of Tez included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Tez.

For the version of components installed with Tez in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Tez version information for emr-6.15.0 | Amazon EMR Release Label | Tez Version                                                                                                                                                                                                                                         | Components Installed With Tez |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| emr-6.15.0                             | Tez 0.10.2-amzn-6        | emrfs, emr-goodies, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, tez-on-yarn, tez-on-worker |

The following table lists the version of Tez included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Tez.

For the version of components installed with Tez in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Tez version information for emr-5.36.2 | Amazon EMR Release Label | Tez Version                                                                                                                                                                                                                          | Components Installed With Tez |
| -------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| emr-5.36.2                             | Tez 0.9.2                | emrfs, emr-goodies, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, tez-on-yarn |

###### Topics

- [Creating a cluster with Tez](tez-create-cluster.md "tez-create-cluster.md")
- [Configuring Tez](tez-configure.md "tez-configure.md")
- [Tez web UI](tez-web-ui.md "tez-web-ui.md")
- [Timeline Server](tez-timeline-server.md "tez-timeline-server.md")
- [Tez release history](Tez-release-history.md "Tez-release-history.md")
