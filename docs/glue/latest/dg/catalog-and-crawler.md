# Data discovery and cataloging in AWS Glue

The AWS Glue Data Catalog is a centralized repository that stores metadata about your organization's
data sets. It acts as an index to the location, schema, and runtime metrics of your data
sources. The metadata is stored in metadata tables, where each table represents a single data
store.

You can populate the Data Catalog using a crawler, which automatically scans your data sources
and extracts metadata. A crawler can connect to data sources that are internal (AWS-based) and external to AWS.

For more information about the supported data sources, see [Supported data sources for crawling](crawler-data-stores.md "crawler-data-stores.md")

You can also create tables in the Data Catalog manually by defining the table structure, schema,
and partitioning structure according to your specific requirements.

For more information about creating metadata tables manually, see [Defining metadata manually](populate-dg-manual.md "populate-dg-manual.md").

You can use the information in the Data Catalog to create and monitor your ETL jobs. The Data Catalog integrates with other AWS analytics services, providing a unified view of data
sources making it easier to manage and analyze data.

- Amazon Athena – Store and query table metadata in the Data Catalog for the Amazon S3 data using
  SQL.
- AWS Lake Formation – Centrally define and manage fine-grained data access policies and audit data
  access.
- Amazon EMR – Access data sources defined in the Data Catalog for big data
  processing.
- Amazon SageMaker AI – Quickly and confidently build, train, and deploy
  machine learning models.

###### Key features of the Data Catalog

The following are the key aspects of the Data Catalog.

Metadata repository

The Data Catalog acts as a central metadata repository, storing information about the
location, schema, and properties of your data sources. This metadata is organized into
databases and tables, similar to a traditional relational database catalog.

Automatic data discoverability

AWS Glue crawlers can automatically discover and catalog new or updated data sources, reducing
the overhead of manual metadata management and ensuring that your Data Catalog remains
up-to-date. By cataloging your data sources, the Data Catalog makes it easier for users and
applications to discover and understand the available data assets within your
organization, promoting data reuse and collaboration.

The Data Catalog supports a wide range of data sources, including Amazon S3, Amazon RDS, Amazon Redshift,
Apache Hive, and more. It can automatically infer and store metadata from these sources
using AWS Glue crawlers.

For more information see, [Using crawlers to populate the Data Catalog](add-crawler.md "add-crawler.md") .

Schema management

The Data Catalog automatically captures and manages the schema of your data sources,
including schema inference, evolution, and versioning. You can update your schema and partitions in the Data Catalog
using AWS Glue ETL jobs.

Table optimization

For better read performance by AWS analytics services such as Amazon Athena and Amazon EMR,
and AWS Glue ETL jobs, the Data Catalog provides managed compaction (a process that compacts small
Amazon S3 objects into larger objects) for Iceberg tables in the Data Catalog. You can use
AWS Glue console, AWS Lake Formation console, AWS CLI, or AWS API to enable or disable compaction for
individual Iceberg tables that are in the Data Catalog.

For more information, see [Optimizing Iceberg tables](table-optimizers.md "table-optimizers.md").

Column statistics

You can compute column-level statistics for Data Catalog tables in data formats such as Parquet, ORC, JSON, ION, CSV, and XML without setting up additional data pipelines.
Column statistics help you to understand data profiles by getting insights about values within a column.
The Data Catalog supports generating statistics for column values such as minimum value, maximum value, total null values, total distinct values, average length of values, and total occurrences of true values.

For more information, see [Optimizing query performance using column statistics](column-statistics.md "column-statistics.md").

Data lineage

The Data Catalog maintains a record of the transformations and operations performed on your
data, providing data lineage information. This lineage information is valuable for
auditing, compliance, and understanding the data's provenance.

Integration with other AWS services

The Data Catalog seamlessly integrates with other AWS services, such as AWS Lake Formation,
Amazon Athena, Amazon Redshift Spectrum, and Amazon EMR. This integration allows you to query and analyze data
across various data stores using a single, consistent metadata layer.

Security and access control

AWS Glue integrates with AWS Lake Formation to support fine-grained access control for Data Catalog resources, allowing
you to manage permissions and secure access to your data assets based on your
organization's policies and requirements. AWS Glue integrates with AWS Key Management Service (AWS KMS) to encrypt metadata that's stored in the Data Catalog.

###### Topics

- [Populating the AWS Glue Data Catalog](populate-catalog-methods.md "populate-catalog-methods.md")
- [Populating and managing transactional tables](populate-otf.md "populate-otf.md")
- [Managing the Data Catalog](manage-catalog.md "manage-catalog.md")
- [Accessing the Data Catalog](access_catalog.md "access_catalog.md")
- [AWS Glue Data Catalog best practices](best-practice-catalog.md "best-practice-catalog.md")
- [Monitoring Data Catalog usage metrics in Amazon CloudWatch](data-catalog-cloudwatch-metrics.md "data-catalog-cloudwatch-metrics.md")
- [AWS Glue Schema registry](schema-registry.md "schema-registry.md")
