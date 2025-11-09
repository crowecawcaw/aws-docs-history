# S3 Tables AWS Regions, endpoints, and service

quotas

The following sections include the supported AWS Regions and service quotas for
S3 Tables.

###### Topics

- [S3 Tables AWS Regions and endpoints](#s3-tables-regions "#s3-tables-regions")
- [S3 Tables quotas](#s3-tables-quotas "#s3-tables-quotas")

## S3 Tables AWS Regions and endpoints

For a list of Regions S3 Tables is currently available in, see [Amazon S3 endpoints](../../../general/latest/gr/s3.md#s3_region "../../../general/latest/gr/s3.md#s3_region"). To connect
programmatically to an AWS service, you use an endpoint. For more information, see [AWS service endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

S3 Tables supports dual-stack endpoints for public access and AWS PrivateLink. Dual-stack endpoints allow you to access S3 tables buckets using the Internet Protocol version 6 (IPv6), in addition to the IPv4 protocol, depending on what your network supports.

S3 Tables dual-stack endpoints use the following naming convention:
`s3tables.`aws-region`.api.aws`

For
a complete list of S3 Tables endpoints, see [Amazon S3 endpoints](../../../general/latest/gr/s3.md#s3_region "../../../general/latest/gr/s3.md#s3_region").

## S3 Tables quotas

Quotas, also referred to as limits, are the maximum number of service resources or
operations for your AWS account. The following are the quotas for S3 Tables resources. For more Amazon S3
quota information, see [Amazon S3 quotas](../../../general/latest/gr/s3.md#limits_s3 "../../../general/latest/gr/s3.md#limits_s3").

| Name          | Default | Adjustable                                                                                                                                                                                                                             | Description                                                                                |
| ------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Table Buckets | 10      | To request a quota increase, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). | The number of Amazon S3 table buckets that you can create per AWS Region in an<br>account. |
| Namespaces    | 10,000  | To request a quota increase, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). | The number of Amazon S3 table namespaces that you can create per table bucket.             |
| Tables        | 10,000  | To request a quota increase, contact [Support](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase"). | The number of Amazon S3 tables that you can create per table bucket.                       |
