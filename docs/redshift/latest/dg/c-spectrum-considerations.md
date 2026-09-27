

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Amazon Redshift Spectrum limitations
<a name="c-spectrum-considerations"></a>

This topic describes limitations for using Redshift Spectrum.

Note the following considerations when you use Redshift Spectrum:
+ For RA3 and DC2 provisioned clusters using Redshift Spectrum, the cluster and the Amazon S3 bucket must be in the same AWS Region. Provisioned RG clusters and Amazon Redshift Serverless include an integrated data lake query engine that runs on the cluster's own compute resources and supports querying Amazon S3 data across AWS Regions.
+ When enhanced VPC routing is turned on, Redshift Spectrum queries against data lake tables in Amazon S3 require VPC endpoints for Amazon S3 and AWS Glue so the cluster can reach your data and catalog. Note that Spectrum scans your Amazon S3 data on an AWS-managed fleet outside your VPC, so this data-scan traffic doesn't pass through your VPC even with enhanced VPC routing turned on. For configuration steps, see [Querying data lake tables with enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/spectrum-enhanced-vpc.html) in the *Amazon Redshift Management Guide*.
+ Redshift Spectrum supports Amazon S3 access point aliases. For more information, see [Using a bucket–style alias for your access point](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-alias.html) in the *Amazon Simple Storage Service User Guide*. However, Redshift Spectrum doesn't support VPC with Amazon S3 access point aliases. For more information, see [Querying data lake tables with enhanced VPC routing](https://docs.aws.amazon.com/redshift/latest/mgmt/spectrum-enhanced-vpc.html) in the *Amazon Redshift Management Guide*.
+ You can't perform update or delete operations on external tables. To create a new external table in the specified schema, you can use CREATE EXTERNAL TABLE. For more information about CREATE EXTERNAL TABLE, see [CREATE EXTERNAL TABLE](r_CREATE_EXTERNAL_TABLE.md). To insert the results of a SELECT query into existing external tables on external catalogs, you can use INSERT (external table). For more information about INSERT (external table), see [INSERT (external table)](r_INSERT_external_table.md).
+ Unless you are using an AWS Glue Data Catalog that is enabled for AWS Lake Formation, you can't control user permissions on an external table. Instead, you can grant and revoke permissions on the external schema. For more information about working with AWS Lake Formation, see [Redshift Spectrum and AWS Lake Formation](spectrum-lake-formation.md).
+ To run Redshift Spectrum queries, the database user must have permission to create temporary tables in the database. The following example grants temporary permission on the database `spectrumdb` to the `spectrumusers` user group. 

  ```
  grant temp on database spectrumdb to group spectrumusers;
  ```

  For more information, see [GRANT](r_GRANT.md).
+ When using the Athena Data Catalog or AWS Glue Data Catalog as a metadata store, see [Quotas and Limits](https://docs.aws.amazon.com/redshift/latest/mgmt/amazon-redshift-limits.html) in the *Amazon Redshift Management Guide*. 
+ Redshift Spectrum doesn't support Amazon EMR with Kerberos.