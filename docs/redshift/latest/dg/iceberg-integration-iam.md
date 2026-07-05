Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# IAM policy requirements for accessing clusters and namespaces registered to the Data Catalog

This topic describes the required IAM permissions for
registering provisioned clusters and serverless namespaces to the Data Catalog and accessing them with Amazon Redshift.

After you register a provisioned cluster or serverless namespace to the AWS Glue Data Catalog, you need the
following permissions to discover the creation of and changes to the subsequently created catalog.

- `glue:GetCatalog`
- `glue:GetCatalogs`
- `lakeformation:GetDataAccess`
  These permissions are included in the service-linked role `AmazonRedshiftServiceLinkedRolePolicy`.
  For more information on this role, see [Using service-linked roles for Amazon Redshift](../mgmt/using-service-linked-roles.md "../mgmt/using-service-linked-roles.md") in the _Amazon Redshift Management Guide_.
