

# S3 Tables AWS Regions, endpoints, and service quotas
<a name="s3-tables-regions-quotas"></a>

The following sections include the supported AWS Regions and service quotas for S3 Tables.

**Topics**
+ [S3 Tables AWS Regions and endpoints](#s3-tables-regions)
+ [S3 Tables quotas](#s3-tables-quotas)
+ [S3 Tables table migration quotas](#s3-tables-migration-quotas)

## S3 Tables AWS Regions and endpoints
<a name="s3-tables-regions"></a>

For a list of Regions S3 Tables is currently available in, see [Amazon S3 endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_region). To connect programmatically to an AWS service, you use an endpoint. For more information, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).

S3 Tables supports dual-stack endpoints for public access and AWS PrivateLink. Dual-stack endpoints allow you to access S3 tables buckets using the Internet Protocol version 6 (IPv6), in addition to the IPv4 protocol, depending on what your network supports.

S3 Tables dual-stack endpoints use the following naming convention: `s3tables.{{aws-region}}.api.aws` 

For a complete list of S3 Tables endpoints, see [Amazon S3 endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_region).

## S3 Tables quotas
<a name="s3-tables-quotas"></a>

Quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. The following are the quotas for S3 Tables resources. For more Amazon S3 quota information, see [Amazon S3 quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html#limits_s3).


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Table Buckets | 100 | To request a quota increase, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). | The number of Amazon S3 table buckets that you can create per AWS Region in an account. | 
| Namespaces | 10,000 | To request a quota increase, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). | The number of Amazon S3 table namespaces that you can create per table bucket. | 
| Tables | 10,000 | To request a quota increase, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase). | The number of Amazon S3 tables that you can create per table bucket. | 

## S3 Tables table migration quotas
<a name="s3-tables-migration-quotas"></a>

The following are the quotas for S3 Tables table migration.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Source objects per migration | 1,000,000,000 | No | The maximum number of objects in the source table that can be migrated in a single migration. | 
| Column type nesting depth | 20 | No | The maximum nesting depth of column types, like a map of lists in the source table schema. Columns nested deeper than this limit are reported as unsupported in the table compatibility report. | 
| Partitions per source table | 100,000 | No | The maximum number of partitions in the source table that can be migrated. | 
| Source object size | 10 GiB | No | The maximum size of a single source object that can be migrated. | 
| Concurrent migrations per account | 10 | No | The number of concurrent migrations allowed per account. | 
| Concurrent migrations per destination table | 1 | No | The number of concurrent migrations allowed per destination table at any time. | 