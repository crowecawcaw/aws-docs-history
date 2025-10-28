# Support for the Apache Iceberg open standard in the lakehouse architecture of Amazon SageMaker

The lakehouse architecture provides support for [Apache
Iceberg](../../../prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.md "../../../prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.md"), enabling organizations to unify data across Amazon S3 data lakes and Amazon Redshift data
warehouses while building powerful analytics and AI/ML applications on a unified data layer.

With the lakehouse architecture, you gain the flexibility to access and query your data in-place using all
Apache Iceberg compatible tools and engines, including open-source Apache Spark. This integration
uses the AWS Glue Iceberg REST Catalog, which provides a standardized REST API interface for
managing Iceberg table metadata and enables seamless connectivity with third-party engines. For
more information, see [how to use AWS Glue Iceberg Rest Catalog
for accessing Iceberg tables in Amazon S3](../../../glue/latest/dg/connect-glu-iceberg-rest.md "../../../glue/latest/dg/connect-glu-iceberg-rest.md").

Through fine-grained permissions enforced across all analytics and ML tools, the lakehouse architecture
ensures secure data access while supporting advanced Iceberg features like ACID transactions,
schema evolution, time travel queries, and efficient row-level operations—all essential
capabilities for modern data-driven organizations seeking to process and analyze vast amounts of
information efficiently.

The lakehouse architecture also supports multiple table optimization options with Glue Catalog to enhance
the management and performance of Apache Iceberg tables that the AWS analytical engines and ETL
jobs uses. These optimizers provide efficient storage utilization, improved query performance,
and effective data management. For more information, see [Optimizing Iceberg tables](../../../glue/latest/dg/table-optimizers.md "../../../glue/latest/dg/table-optimizers.md").

With the lakehouse architecture, you can calculate and update number of distinct values (NDVs) for each
column in Iceberg tables with the AWS Glue Data Catalog. These statistics can facilitate better query
optimization, data management, and performance efficiency for data engineers and scientists
working with large-scale datasets. For more information, see [Optimizing query performance for Iceberg
tables](../../../glue/latest/dg/iceberg-column-statistics.md "../../../glue/latest/dg/iceberg-column-statistics.md").
