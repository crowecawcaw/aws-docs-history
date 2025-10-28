# Configuring Trino on Amazon EMR

###### Topics

- [Configuring connectors for Trino](#emr-trino-config-connector "#emr-trino-config-connector")
- [Monitoring](#emr-trino-monitoring "#emr-trino-monitoring")

## Configuring connectors for Trino

### Connecting to AWS Glue as your Hive metastore

It's important and useful to understand that you can configure AWS Glue Data Catalog as your Hive metastore when running queries with Trino. For additional information, including steps to set up a cluster with a Hive metastore,
see [Using the AWS Glue Data Catalog as the metastore for Hive](emr-hive-metastore-glue.md "emr-hive-metastore-glue.md").

For information on integrating EMR on EKS with AWS Glue, see the following best practices,
[EMR Containers integration with AWS Glue](https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/aws-glue/ "https://aws.github.io/aws-emr-containers-best-practices/metastore-integrations/docs/aws-glue/").

### Connecting to Iceberg tables when using Trino with Amazon EMR

Iceberg is an open table format for analytic tables. It was created for engines like Spark and Trino to query big data from the same tables, using SQL queries. It includes features like isolating data reads and writes, so a reader can
avoid querying data that's partially updated, for instance. It also supports state features, like snapshots. It provides an abstraction layer through the use of metadata and manifest files. These
describe table schema and make it easy to query data without having to know a lot of details about how it's formatted or organized. When you're connected
you can both read data from the tables update data, or write new data to the
underlying files.

There's a workshop available that shows you how to configure Iceberg tables with Amazon EMR and AWS Glue. For more information, see
[Analytics Workshop - Set Up and Use Apache Iceberg Tables on Your Data Lake](https://youtu.be/SZDYmWIStUo?si=sW35AjSWIcHu5x_p "https://youtu.be/SZDYmWIStUo?si=sW35AjSWIcHu5x_p").

### Connecting with Clients

You can connect with Trino using an available JDBC driver. For more information, see [JDBC driver](https://trino.io/docs/current/client/jdbc.html "https://trino.io/docs/current/client/jdbc.html") in
the _Trino Documentation_.

## Monitoring

You can monitor Amazon EMR clusters through the AWS Management Console. For more information,
see [View and monitor an Amazon EMR cluster as it performs work](../ManagementGuide/emr-manage-view.md "../ManagementGuide/emr-manage-view.md"). Amazon EMR also sends its monitoring metrics to Amazon CloudWatch. For more information about
monitoring an Amazon EMR cluster, see Amazon CloudWatch events and metrics from Amazon EMR.
