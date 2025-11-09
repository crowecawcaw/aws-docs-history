# Hue

Hue (Hadoop User Experience) is an open-source, web-based, graphical user interface for
use with Amazon EMR and Apache Hadoop. Hue groups together several different Hadoop
ecosystem projects into a configurable interface. Amazon EMR has also added customizations
specific to Hue in Amazon EMR. Hue acts as a front-end for applications that run on
your cluster, allowing you to interact with applications using an interface that may be more
familiar or user-friendly. The applications in Hue, such as the Hive and Pig editors,
replace the need to log in to the cluster to run scripts interactively using each
application's respective shell. After a cluster launches, you might interact entirely with
applications using Hue or a similar interface. For more information about Hue,
see [http://gethue.com](http://gethue.com "http://gethue.com").

Hue is installed by default when you launch your cluster using the Amazon EMR console. You can
choose not to install Hue by using **Advanced options** in the Amazon EMR
console when you launch a cluster, or by explicitly specifying the
`--applications` option, and omitting Hue, when you use
`create-cluster` from the AWS CLI.

###### Topics

- [Hue version information](#emr-Hue-versions "#emr-Hue-versions")
- [Supported and unsupported features of
  Hue on Amazon EMR](emr-hue-supported-features.md "emr-hue-supported-features.md")
- [Considerations](emr-hue-considerations.md "emr-hue-considerations.md")
- [Connecting to the Hue web user interface](accessing-hue.md "accessing-hue.md")
- [Using Hue with a remote database in Amazon RDS](hue-rds.md "hue-rds.md")
- [Advanced configurations for Hue](advanced-configurations.md "advanced-configurations.md")
- [Hue release history](Hue-release-history.md "Hue-release-history.md")

## Hue version information

**Hue version for
7.10.0**

The following table lists the version of Hue included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Hue.

For the version of components installed with Hue in this release, see [Release 7.10.0 Component Versions](emr-7100-release.md "emr-7100-release.md").

| Hue version information for emr-7.10.0 | Amazon EMR Release Label | Hue Version                                                                                                                                                                                                                                                                            | Components Installed With Hue |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| emr-7.10.0                             | Hue 4.11.0               | emrfs, emr-ddb, emr-goodies, emr-kinesis, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hue-server, mariadb-server, oozie-client, oozie-server |

**Hue version for
6.15.0**

The following table lists the version of Hue included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Hue.

For the version of components installed with Hue in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Hue version information for emr-6.15.0 | Amazon EMR Release Label | Hue Version                                                                                                                                                                                                                                                                            | Components Installed With Hue |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| emr-6.15.0                             | Hue 4.11.0               | emrfs, emr-ddb, emr-goodies, emr-kinesis, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hue-server, mariadb-server, oozie-client, oozie-server |

**Hue version for
5.36.2**

The following table lists the version of Hue included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Hue.

For the version of components installed with Hue in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Hue version information for emr-5.36.2 | Amazon EMR Release Label | Hue Version                                                                                                                                                                                                                                                                            | Components Installed With Hue |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| emr-5.36.2                             | Hue 4.10.0               | emrfs, emr-ddb, emr-goodies, emr-kinesis, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hue-server, mariadb-server, oozie-client, oozie-server |
