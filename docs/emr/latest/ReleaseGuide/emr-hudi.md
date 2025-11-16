# Hudi

[Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") is an open-source data management framework used to simplify incremental
data processing and data pipeline development by providing record-level insert, update,
upsert, and delete capabilities. _Upsert_ refers to the ability to insert
records into an existing dataset if they do not already exist or to update them if they do.
By efficiently managing how data is laid out in Amazon S3, Hudi allows data to be ingested and
updated in near real time. Hudi carefully maintains metadata of the actions performed on the
dataset to help ensure that the actions are atomic and consistent.

Hudi is integrated with [Apache Spark](https://aws.amazon.com/emr/features/spark/ "https://aws.amazon.com/emr/features/spark/"), [Apache Hive](https://hive.apache.org/ "https://hive.apache.org/"), and [Presto](https://prestodb.github.io "https://prestodb.github.io"). In
Amazon EMR release versions 6.1.0 and later, Hudi is also integrated with [Trino (PrestoSQL)](https://trino.io/ "https://trino.io/").

With Amazon EMR release version 5.28.0 and later, EMR installs Hudi components by default
when Spark, Hive, Presto, or Flink are installed. You can use Spark or the Hudi
DeltaStreamer utility to create or update Hudi datasets. You can use Hive, Spark, Presto, or
Flink to query a Hudi dataset interactively or build data processing pipelines using
_incremental pull_. Incremental pull refers to the ability to pull
only the data that changed between two actions.

These features make Hudi suitable for the following use cases:

- Working with streaming data from sensors and other Internet of Things (IoT)
  devices that require specific data insertion and update events.
- Complying with data privacy regulations in applications where users might choose
  to be forgotten or modify their consent for how their data can be used.
- Implementing a [change data capture (CDC) system](https://en.wikipedia.org/wiki/Change_data_capture "https://en.wikipedia.org/wiki/Change_data_capture") that allows you to apply changes to a
  dataset over time.
  The following table lists the version of Hudi included in the latest release of the Amazon EMR 7.x series, along with the components that Amazon EMR installs with Hudi.

For the version of components installed with Hudi in this release, see [Release 7.11.0 Component Versions](emr-7110-release.md "emr-7110-release.md").

| Hudi version information for emr-7.11.0 | Amazon EMR Release Label | Hudi Version   | Components Installed With Hudi |
| --------------------------------------- | ------------------------ | -------------- | ------------------------------ |
| emr-7.11.0                              | Hudi 1.0.2-amzn-0        | Not available. |

The following table lists the version of Hudi included in the latest release of the Amazon EMR 6.x series, along with the components that Amazon EMR installs with Hudi.

For the version of components installed with Hudi in this release, see [Release 6.15.0 Component Versions](emr-6150-release.md "emr-6150-release.md").

| Hudi version information for emr-6.15.0 | Amazon EMR Release Label | Hudi Version   | Components Installed With Hudi |
| --------------------------------------- | ------------------------ | -------------- | ------------------------------ |
| emr-6.15.0                              | Hudi 0.14.0-amzn-0       | Not available. |

###### Note

Amazon EMR release 6.8.0 comes with [Apache Hudi](https://hudi.apache.org/ "https://hudi.apache.org/") 0.11.1; however, Amazon EMR 6.8.0 clusters are also compatible with the open-source `hudi-spark3.3-bundle_2.12` from Hudi 0.12.0.

The following table lists the version of Hudi included in the latest release of the Amazon EMR 5.x series, along with the components that Amazon EMR installs with Hudi.

For the version of components installed with Hudi in this release, see [Release 5.36.2 Component Versions](emr-5362-release.md "emr-5362-release.md").

| Hudi version information for emr-5.36.2 | Amazon EMR Release Label | Hudi Version   | Components Installed With Hudi |
| --------------------------------------- | ------------------------ | -------------- | ------------------------------ |
| emr-5.36.2                              | Hudi 0.10.1-amzn-1       | Not available. |

###### Topics

- [How Hudi works](emr-hudi-how-it-works.md "emr-hudi-how-it-works.md")
- [Considerations and limitations for using
  Hudi on Amazon EMR](emr-hudi-considerations.md "emr-hudi-considerations.md")
- [Create a cluster with
  Hudi installed](emr-hudi-installation-and-configuration.md "emr-hudi-installation-and-configuration.md")
- [Work with a Hudi dataset](emr-hudi-work-with-dataset.md "emr-hudi-work-with-dataset.md")
- [Use the Hudi CLI](emr-hudi-cli.md "emr-hudi-cli.md")
- [Hudi release history](Hudi-release-history.md "Hudi-release-history.md")
