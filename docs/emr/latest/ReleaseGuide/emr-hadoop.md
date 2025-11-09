# Apache Hadoop

[Apache Hadoop](https://aws.amazon.com/elasticmapreduce/details/hadoop/ "https://aws.amazon.com/elasticmapreduce/details/hadoop/") is an
open-source Java software framework that supports massive data processing across a cluster
of instances. It can run on a single instance or thousands of instances. Hadoop uses many
processing models, such as MapReduce and Tez, to distribute processing across multiple
instances and also uses a distributed file system called HDFS to store data across multiple
instances. Hadoop monitors the health of instances in the cluster and can recover from the
failure of one or more nodes. In this way, Hadoop provides increased processing and storage
capacity, as well as high availability. For more information, see the[Hadoop documentation](http://hadoop.apache.org "http://hadoop.apache.org").

The following table lists the version of Hadoop included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Hadoop.

For the version of components installed with Hadoop in this release, see [Release 7.10.0 Component Versions](emr-7100-release.md "emr-7100-release.md").

| Hadoop version information for emr-7.10.0 | Amazon EMR Release Label | Hadoop Version                                                                                                                                                                                                                                                                      | Components Installed With Hadoop |
| ----------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| emr-7.10.0                                | Hadoop 3.4.1-amzn-2      | emrfs, emr-ddb, emr-goodies, emr-kinesis, emr-s3-dist-cp, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-mapred, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server |

The following table lists the version of Hadoop included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Hadoop.

For the version of components installed with Hadoop in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Hadoop version information for emr-6.15.0 | Amazon EMR Release Label | Hadoop Version                                                                                                                                                                                                                                                                      | Components Installed With Hadoop |
| ----------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| emr-6.15.0                                | Hadoop 3.3.6-amzn-1      | emrfs, emr-ddb, emr-goodies, emr-kinesis, emr-s3-dist-cp, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-mapred, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server |

The following table lists the version of Hadoop included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Hadoop.

For the version of components installed with Hadoop in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Hadoop version information for emr-5.36.2 | Amazon EMR Release Label | Hadoop Version                                                                                                                                                                                                                                                                      | Components Installed With Hadoop |
| ----------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| emr-5.36.2                                | Hadoop 2.10.1-amzn-4     | emrfs, emr-ddb, emr-goodies, emr-kinesis, emr-s3-dist-cp, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-mapred, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server |

Beginning with Amazon EMR 5.18.0, you can use the Amazon EMR artifact repository to build your job code against the exact versions of libraries and dependencies that are available with specific Amazon EMR releases. For more information, see [Checking dependencies using the Amazon EMR artifact repository](emr-artifact-repository.md "emr-artifact-repository.md").

###### Topics

- [Configure Hadoop](emr-hadoop-config.md "emr-hadoop-config.md")
- [Transparent encryption in HDFS on Amazon EMR](emr-encryption-tdehdfs.md "emr-encryption-tdehdfs.md")
- [Create or run a Hadoop application](emr-hadoop-application.md "emr-hadoop-application.md")
- [Read restored objects](emr-hadoop-read-restore-objects.md "emr-hadoop-read-restore-objects.md")
- [Turn on non-uniform memory access awareness for YARN
  containers](hadoop-numa.md "hadoop-numa.md")
- [YARN container bin packing](Hadoop-container-yarn.md "Hadoop-container-yarn.md")
- [Hadoop version history](Hadoop-release-history.md "Hadoop-release-history.md")
