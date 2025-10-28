# Connect to data sources

You can use Amazon Athena to query data stored in different locations and formats in a
_dataset_. This dataset might be in CSV, JSON, Avro, Parquet, or some
other format.

The tables and databases that you work with in Athena to run queries are based on
_metadata_. Metadata is data about the underlying data in your
dataset. How that metadata describes your dataset is called the _schema_.
For example, a table name, the column names in the table, and the data type of each column
are schema, saved as metadata, that describe an underlying dataset. In Athena, we call a
system for organizing metadata a _data catalog_ or a
_metastore_. The combination of a dataset and the data catalog that
describes it is called a _data source_.

The relationship of metadata to an underlying dataset depends on the type of data source
that you work with. Relational data sources like MySQL, PostgreSQL, and SQL Server tightly
integrate the metadata with the dataset. In these systems, the metadata is most often
written when the data is written. Other data sources, like those built using [Hive](https://hive.apache.org "https://hive.apache.org"), allow you to define metadata on-the-fly when
you read the dataset. The dataset can be in a variety of formats—for example, CSV,
JSON, Parquet, or Avro.

Athena natively supports the AWS Glue Data Catalog. The AWS Glue Data Catalog is a data catalog built on top of
other datasets and data sources such as Amazon S3, Amazon Redshift, and Amazon DynamoDB. You can also connect
Athena to other data sources by using a variety of connectors.

###### Topics

- [Use AWS Glue Data Catalog to connect to your data](data-sources-glue.md "data-sources-glue.md")
- [Use Amazon Athena Federated Query](federated-queries.md "federated-queries.md")
- [Use Amazon DataZone in Athena](datazone-using.md "datazone-using.md")
- [Use an external Hive metastore](connect-to-data-source-hive.md "connect-to-data-source-hive.md")
- [Manage your data sources](data-sources-managing.md "data-sources-managing.md")
