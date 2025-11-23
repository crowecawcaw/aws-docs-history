# Presto

###### Important

Presto, the previous version of Trino, is still available for use with Amazon EMR. However, we highly recommend Trino going forward for use with Amazon EMR. Also note that Trino
and Presto can't run simultaneously on the same cluster. For more information, see [Trino](emr-trino.md "emr-trino.md").

[Presto](https://aws.amazon.com/big-data/what-is-presto/ "https://aws.amazon.com/big-data/what-is-presto/") is a fast SQL
query engine designed for interactive analytic queries over large datasets from multiple
sources. For more information, see the [Presto
website](https://prestodb.io/ "https://prestodb.io/").
Presto is included in Amazon EMR releases 5.0.0 and later. Earlier releases include Presto as a sandbox application. For more information, see [Amazon EMR 4.x release versions](emr-release-4x.md "emr-release-4x.md"). Amazon EMR release versions 6.1.0 and later support [Trino](https://trino.io/ "https://trino.io/") in addition to Presto. For more
information, see [PrestoDB installation](emr-presto-considerations.md#emr-prestodb-prestosql "emr-presto-considerations.md#emr-prestodb-prestosql").

The following table lists the version of Presto included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Presto.

For the version of components installed with Presto in this release, see [Release 7.12.0 Component Versions](emr-7120-release.md "emr-7120-release.md").

| Presto version information for emr-7.12.0 | Amazon EMR Release Label | Presto Version                                                                                                                                                                                                                                                                                                                 | Components Installed With Presto |
| ----------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| emr-7.12.0                                | Presto 0.287-amzn-6      | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-hdfs-zkfc, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hive-client, hudi, hudi-presto, hcatalog-server, mariadb-server, presto-coordinator, presto-worker |

The following table lists the version of Presto included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Presto.

For the version of components installed with Presto in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Presto version information for emr-6.15.0 | Amazon EMR Release Label | Presto Version                                                                                                                                                                                                                                                                                               | Components Installed With Presto |
| ----------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| emr-6.15.0                                | Presto 0.283-amzn-0      | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hive-client, hudi, hudi-presto, hcatalog-server, mariadb-server, presto-coordinator, presto-worker |

The following table lists the version of Presto included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Presto.

For the version of components installed with Presto in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Presto version information for emr-5.36.2 | Amazon EMR Release Label | Presto Version                                                                                                                                                                                                                                                                                               | Components Installed With Presto |
| ----------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| emr-5.36.2                                | Presto 0.267-amzn-1      | emrfs, emr-goodies, hadoop-client, hadoop-hdfs-datanode, hadoop-hdfs-library, hadoop-hdfs-namenode, hadoop-kms-server, hadoop-yarn-nodemanager, hadoop-yarn-resourcemanager, hadoop-yarn-timeline-server, hive-client, hudi, hudi-presto, hcatalog-server, mariadb-server, presto-coordinator, presto-worker |

###### Topics

- [Using Presto with the AWS Glue Data Catalog](emr-presto-glue.md "emr-presto-glue.md")
- [Using S3 Select Pushdown with Presto to improve
  performance](emr-presto-s3select.md "emr-presto-s3select.md")
- [Adding database connectors](presto-adding-db-connectors.md "presto-adding-db-connectors.md")
- [Using SSL/TLS and configuring LDAPS with Presto on
  Amazon EMR](presto-ssl.md "presto-ssl.md")
- [Activating Presto strict mode](presto-strict-mode.md "presto-strict-mode.md")
- [Handling Spot Instance loss in Presto](presto-spot-loss.md "presto-spot-loss.md")
- [Using Presto automatic scaling with Graceful
  Decommission](presto-graceful-autoscale.md "presto-graceful-autoscale.md")
- [Considerations with Presto on
  Amazon EMR](emr-presto-considerations.md "emr-presto-considerations.md")
- [Presto release history](Presto-release-history.md "Presto-release-history.md")
