# Trino

Trino is an open-source query engine that's designed for interactive queries on a wide range of data
sources. These can include relational databases, file-based data, HDFS data, and
others. The most common purpose for Trino with Amazon EMR is to run complex SQL queries on large datasets stored in Amazon S3. It's also compliant with
ANSI SQL, which makes it familiar to database engineers, data analysts, and data scientists who are familiar with SQL.

###### Note

PrestoSQL was renamed to Trino in December 2020. Amazon EMR versions 6.4.0 and later generally refer to [Trino](https://trino.io/ "https://trino.io/"), while earlier release versions refer to PrestoSQL.

###### Important

PrestoSQL, the previous version of Trino, is still available for use with Amazon EMR. However, we highly recommend Trino going forward for use with Amazon EMR. Also note that Trino and PrestoSQL can't run simultaneously
on the same cluster.

The following table lists the version of Trino included in the latest release
of Amazon EMR 7.x, along with components that Amazon EMR installs with Trino. For the version of components installed with Trino in this release, see [Release 7.11.0
Component Versions](emr-7110-release.md "emr-7110-release.md").

| Trino (PrestoSQL) version information for emr-7.11.0 | Amazon EMR Release Label   | Trino (PrestoSQL) Version                                                                                                                                                                                                                                                                                                   | Components Installed With Trino (PrestoSQL) |
| ---------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| emr-7.11.0                                           | trino-prestosql 475-amzn-0 | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hive-client, hudi, hudi-trino, hcatalog-server, mariadb-server, trino-coordinator, trino-worker |

###### Topics

- [Trino history and design](emr-trino-intro-history.md "emr-trino-intro-history.md")
- [Getting started with Trino](emr-trino-getting-started.md "emr-trino-getting-started.md")
- [Configuring Trino on Amazon EMR](emr-trino-config.md "emr-trino-config.md")
- [Best practices for Trino on Amazon EMR](emr-trino-advanced.md "emr-trino-advanced.md")
- [Trino Considerations](Trino-considerations.md "Trino-considerations.md")
- [Trino release history](Trino-release-history.md "Trino-release-history.md")
