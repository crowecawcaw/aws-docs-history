# Building AWS Glue Data Catalog views

In the AWS Glue Data Catalog, a _view_ is a virtual table in which
the contents are defined by a SQL query that references one or more tables. You can create a
Data Catalog view that references up to 10 tables using SQL editors for Amazon Athena, Amazon Redshift, or
Apache Spark using EMR Serverless or AWS Glue version 5.0. Underlying reference tables for a
view can belong to the same database or different databases within the same AWS account's
Data Catalog.

You can reference standard AWS Glue tables and tables in open table formats (OTF) such as
[Apache Hudi](https://hudi.incubator.apache.org/ "https://hudi.incubator.apache.org/"), Linux Foundation
[Delta Lake](https://delta.io/ "https://delta.io/"), and [Apache Iceberg](https://iceberg.apache.org/ "https://iceberg.apache.org/"), with underlying data stored in
Amazon S3 locations registered with AWS Lake Formation. Additionally, you can create views from federated
tables from Amazon Redshift datashares that are shared with Lake Formation.

## Differentiating Data Catalog views from other view types

Data Catalog views differ from Apache Hive, Apache Spark and Amazon Athena views. The Data Catalog
view is a native feature of the AWS Glue Data Catalog, and is a multi-dialect definer-created
view. You can create a Data Catalog view using one of the supported analytics services, such
as Athena or Amazon Redshift Spectrum, and access the same view using other supported analytics
services. On the other hand, the Apache Hive, Apache Spark, and Athena views are created
independently in each analytics service, such as Athena and Amazon Redshift, and are visible and
accessible only within that service.

## What is a definer view?

A definer view is a SQL view that operates based on the permissions of the principal
that created it. The definer role has the necessary permissions to access the referenced
tables, and it runs the SQL statement that defines the view. The definer creates the
view and shares it with other users through AWS Lake Formation's fine-grained access control.

When a user queries the definer view, the query engine uses the definer role's
permissions to access the underlying reference tables. This approach enables users to
interact with the view without requiring direct access to the source tables, enhancing
security and simplifying data access management.

To set up a definer view, the definer IAM role can be within the same AWS
account as the base tables, or in a different account using cross-account definer roles. For more information about the permissions
required for the definer role, see [Prerequisites for creating views](views-prereqs.md "views-prereqs.md").

## A framework for multi-dialect views

The Data Catalog supports creating views using multiple structured query language (SQL)
dialects. SQL is a language used for storing and processing information in a relational
database and each AWS analytical engine uses its own variation of SQL, or SQL
dialect.

You create a Data Catalog view in one SQL dialect using one of the supported analytics
query engine. Subsequently, you can update the view using the `ALTER VIEW`
statement in a different SQL dialect within any other supported analytics engine.
However, each dialect must reference the same set of tables, columns, and data
types.

You can access the multiple dialects available for the view using the
`GetTable` API, AWS CLI and AWS console. Thus, the Data Catalog view is
visible and available to query across different supported analytics engines.

By defining a common view schema and metadata object that you can query from multiple
engines, Data Catalog views enable you to use uniform views across your data lake.

For more details on how the schema is resolved for each dialect, see, link to
the API reference. For more details on the matching rules for different
types, see, link to the relevant section in the API doc.

## Integrating with Lake Formation permissions

You can use AWS Lake Formation to centralize permissions management on AWS Glue Data Catalog views for
users. You can grant fine-grained permissions on the Data Catalog views using the named
resource method or LF-Tags, and share them across AWS accounts, AWS
organizations, and organizational units. You can also share and access the Data Catalog views
across AWS Regions using resource links. This allows users to provide data access
without duplicating the data source, and sharing the underlying tables.

The `CREATE VIEW` DDL statement of a Data Catalog view can reference the
standard AWS Glue tables and tables in open table formats (OTF) such as Hudi, Delta Lake,
and Iceberg with underlying data stored in Amazon S3 locations registered with Lake Formation as well
as the federated tables from Amazon Redshift datashare that are shared with Lake Formation. The tables can be
of any file format as long as the engine used to query the view supports that format.
You can also reference built in functions of the engine on which it is run but other
engine-specific resources may not be allowed. For more details, see [Data Catalog views considerations and limitations](views-notes.md "views-notes.md")

## Use cases

Following are the important use cases for Data Catalog views:

- Create and manage permissions on a single view schema. This helps you avoid
  the risk of inconsistent permissions on duplicate views created in multiple
  engines.
- Grant permissions to users on a view that references multiple tables without
  granting permissions directly on the underlying reference tables.
- Achieve row level filtering on tables using LF-Tags (where LF-Tags cascade
  only up to column level) by applying LF-Tags on views and granting LF-Tags based
  permissions to users.

## Supported AWS analytics services for

views

The following AWS analytics services support creating Data Catalog views:

- Amazon Redshift
- Amazon Athena version 3
- Apache Spark on EMR Serverless
- Apache Spark on AWS Glue version 5.0

## Additional resources

You can learn more about the Data Catalog in this guide, as well as using the following
resources:

The following video demonstrates how to create views and query them from Athena and
Amazon Redshift.

###### Topics

- [Prerequisites for creating views](views-prereqs.md "views-prereqs.md")
- [Creating Data Catalog views using DDL statements](create-views.md "create-views.md")
- [Creating Data Catalog views using AWS Glue APIs](views-api-usage.md "views-api-usage.md")
- [Granting permissions on Data Catalog views](grant-perms-views.md "grant-perms-views.md")
- [Materialized views](materialized-views.md "materialized-views.md")
