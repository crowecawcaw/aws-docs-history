Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying catalogs registered in the AWS Glue Data Catalog

After you register an Amazon Redshift data warehouse to the AWS Glue Data Catalog and set permissions for the resulting
catalog in AWS Lake Formation, the catalog is automatically mounted in all Amazon Redshift instances with access to the source data warehouse
in the same account and AWS Region. You can then query that catalog as you would a local cluster or workgroup.
You can also query catalogs registered to the AWS Glue Data Catalog using any SQL engine that supports the Apache Iceberg REST Open API.
For more information on querying catalogs in the AWS Glue Data Catalog using the Apache Iceberg REST API, see
[Accessing the Data Catalog](../../../glue/latest/dg/access_catalog.md "../../../glue/latest/dg/access_catalog.md")
in the _AWS Glue Developer Guide_. For information on the Apache Iceberg REST API, see the
[Apache Iceberg REST Open API specification](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml "https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml").

To query a catalog, you must first set the permissions for the catalog using AWS Lake Formation. For more information on setting
permissions for catalogs in AWS Lake Formation, see
[Setting up permissions for Amazon Redshift datashares](../../../lake-formation/latest/dg/setup-ds-perms.md "../../../lake-formation/latest/dg/setup-ds-perms.md")
in the _AWS Lake Formation Developer Guide_. You also need an IAM role with the `AmazonRedshiftServiceLinkedRolePolicy`
managed policy attached. For information on service-linked roles, see
[Using service-linked roles for Amazon Redshift](../mgmt/using-service-linked-roles.md "../mgmt/using-service-linked-roles.md")
in the _Amazon Redshift Management Guide_.

Note that queries against catalogs must follow the following three-part syntax for accessing tables:

```
database@namespace.schema.table
```

For general information on querying Amazon Redshift data warehouses, see
[Query a database](../mgmt/query-databases.md "../mgmt/query-databases.md")
in the _Amazon Redshift Management Guide_.

Querying using the query editor v2
After setting permissions for an account to access a managed workgroup,
that managed workgroup appears in the tree-view panel under the external databases section of
your serverless database. You can query the managed workgroup
the same way that you would query an internal Amazon Redshift provisioned cluster or serverless workgroup,
using the three-part syntax format `database@namespace/cluster.schema.table`. See
the following sample statement:

```
SELECT price FROM sales_db@mynamespace.sales_schema.inventory_table
```

Querying using the Data API
You can query managed workgroups using the Amazon Redshift Data API the same way that you would query an internal
Amazon Redshift provisioned cluster or serverless workgroup, passing the Amazon Resource Name (ARN) of the catalog
into the relevant `database` attribute. Consider the following example that creates a table in a catalog.

```
aws redshift-data execute-statement —sql 'CREATE TABLE IF NOT EXISTS "dev@test-rms-catalog".public.t1 (c1 INT, c2 VARCHAR(10));' —database arn:aws:glue:us-east-1:550022730026:catalog/test-rms-catalog
```
