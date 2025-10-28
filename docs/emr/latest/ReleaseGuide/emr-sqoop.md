# Apache Sqoop

###### Note

The last release to include Apache Sqoop was Amazon EMR Release 7.4. Apache Sqoop will be removed from Amazon EMR Release 7.5
and higher releases.

Apache Sqoop is a tool for transferring data between Amazon S3, Hadoop, HDFS, and RDBMS
databases. For more information, see the [Apache Sqoop
website](http://sqoop.apache.org/ "http://sqoop.apache.org/").
Sqoop is included in Amazon EMR releases 5.0.0 and later. Earlier releases include Sqoop as a sandbox application. For more information, see [Amazon EMR 4.x release versions](emr-release-4x.md "emr-release-4x.md").

###### Topics

- [Sqoop version information](#emr-sqoop-versions "#emr-sqoop-versions")
- [Considerations with Sqoop on Amazon EMR](emr-sqoop-considerations.md "emr-sqoop-considerations.md")
- [Sqoop release history](Sqoop-release-history.md "Sqoop-release-history.md")

## Sqoop version information

**Sqoop version for version 7.4.**

The following table lists the version of Sqoop included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Sqoop.

| Sqoop version information for emr-7.4.0 | Amazon EMR Release Label | Sqoop Version                                                                                                                                                                                                                                                                        | Components Installed With Sqoop                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------- | ------------------------------- |
| emr-7.4.0                               | Sqoop 1.4.7              | emrfs, emr-ddb, emr-goodies, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, mariadb-server, sqoop-client | **Sqoop version for 6.15.0** The following table lists the version of Sqoop included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Sqoop. For the version of components installed with Sqoop in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md"). Sqoop version information for emr-6.15.0 | Amazon EMR Release Label | Sqoop Version | Components Installed With Sqoop |
| ---                                     | ---                      | ---                                                                                                                                                                                                                                                                                  |
| emr-6.15.0                              | Sqoop 1.4.7              | emrfs, emr-ddb, emr-goodies, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, mariadb-server, sqoop-client | **Sqoop version for 5.36.2** The following table lists the version of Sqoop included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Sqoop. For the version of components installed with Sqoop in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md"). Sqoop version information for emr-5.36.2 | Amazon EMR Release Label | Sqoop Version | Components Installed With Sqoop |
| ---                                     | ---                      | ---                                                                                                                                                                                                                                                                                  |
| emr-5.36.2                              | Sqoop 1.4.7              | emrfs, emr-ddb, emr-goodies, hadoop-client, hadoop-mapred, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-httpfs-server, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, mariadb-server, sqoop-client |
