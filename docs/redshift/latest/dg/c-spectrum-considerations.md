Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift Spectrum limitations

This topic describes limitations for using Redshift Spectrum.

Note the following considerations when you use Redshift Spectrum:

- The Amazon Redshift cluster and the Amazon S3 bucket must be in the same AWS Region.
- Redshift Spectrum doesn't support enhanced VPC routing with provisioned clusters. To access your Amazon S3 data, you might need to perform additional
  configuration steps. For more information, see [Redshift Spectrum and enhanced VPC routing](../mgmt/spectrum-enhanced-vpc.md "../mgmt/spectrum-enhanced-vpc.md") in the _Amazon Redshift Management Guide_.
- Redshift Spectrum supports Amazon S3 access point aliases. For more information,
  see [Using a bucket–style alias for your access point](../../../AmazonS3/latest/userguide/access-points-alias.md "../../../AmazonS3/latest/userguide/access-points-alias.md") in the _Amazon Simple Storage Service User Guide_.
  However, Redshift Spectrum doesn't support VPC with Amazon S3 access point aliases.
  For more information, see [Redshift Spectrum and enhanced VPC routing](../mgmt/spectrum-enhanced-vpc.md "../mgmt/spectrum-enhanced-vpc.md") in the _Amazon Redshift Management Guide_.
- You can't perform update or delete operations on external tables. To create a new external table in the specified schema, you can use CREATE EXTERNAL TABLE. For more information about CREATE EXTERNAL TABLE, see [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md "r_CREATE_EXTERNAL_TABLE.md"). To
  insert the results of a SELECT query into existing external tables on external
  catalogs, you can use INSERT (external table). For more information about INSERT
  (external table), see [INSERT (external table)](r_INSERT_external_table.md "r_INSERT_external_table.md").
- Unless you are using an AWS Glue Data Catalog that is enabled for AWS Lake Formation, you can't
  control user permissions on an external table. Instead, you can grant and revoke
  permissions on the external schema. For more information about working with AWS Lake Formation,
  see [Redshift Spectrum and AWS Lake Formation](spectrum-lake-formation.md "spectrum-lake-formation.md").
- To run Redshift Spectrum queries, the database user must have permission to
  create temporary tables in the database. The following example grants temporary
  permission on the database `spectrumdb` to the
  `spectrumusers` user group.

```
grant temp on database spectrumdb to group spectrumusers;
```

For more information, see [GRANT](r_GRANT.md "r_GRANT.md").

- When using the Athena Data Catalog or AWS Glue Data Catalog as a metadata store,
  see [Quotas and
  Limits](../mgmt/amazon-redshift-limits.md "../mgmt/amazon-redshift-limits.md") in the _Amazon Redshift Management Guide_.
- Redshift Spectrum doesn't support Amazon EMR with Kerberos.
