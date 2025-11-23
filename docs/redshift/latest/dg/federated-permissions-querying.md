Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying catalogs registered in the AWS Glue Data Catalog with Redshift federated permissions

When you register an Amazon Redshift data warehouse to the AWS Glue Data Catalog using Amazon Redshift federated permissions, the databases in that namespace are automatically mounted in all Amazon Redshift instances in that AWS account and Region. This enables querying across multi-warehouse environments while maintaining security through global identities and fine-grained access control (FGAC) policies.

## Prerequisites

Before querying federated databases, ensure you have:

- Redshift Federated Databases should automatically be mounted on the Redshift Warehouses in the same AWS account. However, in current version of Amazon Redshift, add Redshift Service linked IAM Role `AWSServiceRoleForRedshift` as a Data Lake Read only Admin in Lakeformation. This requirement will be removed in a later release.
  - For information on service-linked roles, see [Using service-linked roles for Amazon Redshift](../mgmt/using-service-linked-roles.md "../mgmt/using-service-linked-roles.md") in the Amazon Redshift Management Guide.

- IAM actions listed in the `AmazonRedshiftFederatedAuthorization` AWS managed policy
- Proper permissions configured for the catalog objects in the source data warehouse
- Access to the Amazon Redshift data warehouse in the same AWS account and Region.

## Querying Federated Databases

You can query objects in the databases under the registered catalogs using three-part syntax for accessing tables:

```

database@namespace_catalog.schema.table

```

### Example Query

```

SELECT * FROM my_database@my_namespace.sales.transactions
WHERE transaction_date >= '2024-01-01';

```

Additionally, you can access objects from federated databases through [USE database](r_USE_command.md "r_USE_command.md").

The federated databases are also available for [direct connection](database-direct-connect.md "database-direct-connect.md").

## Security and Access Control

**Global Identities and FGAC Enforcement**

When you enable Amazon Redshift data warehouse with Federated Permissions, grants and FGAC policies defined on these objects are automatically enforced in consuming warehouses. This ensures consistent security across your multi-warehouse environment.

**Supported Security Features**

You can configure the following security controls on objects in the Amazon Redshift data warehouse, which will be enforced across all consuming warehouses

- **Column-Level Privileges (CLP)**: Grant or restrict access to specific columns
- **Row-Level Security (RLS)**: Control access to specific rows based on user attributes
- **Dynamic Data Masking (DDM)**: Automatically mask sensitive data based on user permissions
