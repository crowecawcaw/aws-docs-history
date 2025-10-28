# Amazon S3 in AWS GovCloud (US)

Amazon Simple Storage Service (Amazon S3) is storage for the internet. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web. You can accomplish these tasks using the simple and intuitive web interface of the AWS Management Console.

## How Amazon Simple Storage Service differs for AWS GovCloud (US)

- Amazon Route 53 Private DNS for VPCs is currently not supported for Amazon S3 endpoints.
- You cannot do a direct copy of the contents of an Amazon S3 bucket in the
  AWS GovCloud (US) Regions to or from another AWS Region.
- If you use Amazon S3 policies, use the AWS GovCloud (US) Amazon Resource Name (ARN) identifier.
  For more information, see [Amazon Resource Names (ARNs)
  in AWS GovCloud (US) Regions](using-govcloud-arns.md "using-govcloud-arns.md").
- In the AWS GovCloud (US) Regions, Amazon S3 has three endpoints. If you are processing
  export-controlled data, use one of the SSL endpoints. If you have FIPS requirements, use a
  FIPS 140-3 endpoint (https://s3-fips.us-gov-west-1.amazonaws.com or
  https://s3-fips.us-gov-east-1.amazonaws.com).
- Amazon S3 bucket names are unique to the AWS GovCloud (US) Regions. Bucket names in the
  AWS GovCloud (US) Regions are not shared across other AWS Regions.
- Multi-factor authentication (MFA) delete is not available in the
  AWS GovCloud (US) Regions.
- [Amazon S3 Transfer Acceleration](../../../AmazonS3/latest/userguide/transfer-acceleration.md "../../../AmazonS3/latest/userguide/transfer-acceleration.md")
  is not available in the AWS GovCloud (US) Regions.
- Amazon S3 Storage Lens is not available in the AWS GovCloud (US) Regions.
- Amazon S3 Object Lambda Access Points are available in the AWS GovCloud (US) Regions for SSL
  endpoints. Object Lambda Access Points are not available for FIPS endpoints.
- Amazon S3 presigned URLs are available only through the AWS Command Line Interface (AWS CLI) and AWS
  SDKs.
- Bucket-style aliases for your Amazon S3 Object Lambda Access Points are not
  available.
- Amazon S3 Express One Zone is not available in the AWS GovCloud (US) Regions.
- Amazon S3 Tables is not available in the AWS GovCloud (US) Regions.
- Amazon S3 Metadata is not available in the AWS GovCloud (US) Regions.
- Access points for directory buckets are not available in the AWS GovCloud (US) Regions.
- You cannot use S3 access points to access file data stored on Amazon FSx file systems.

## Documentation for Amazon Simple Storage Service

[Amazon Simple Storage Service documentation](https://aws.amazon.com/documentation/s3/ "https://aws.amazon.com/documentation/s3/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon S3 metadata is not permitted to contain export-controlled data. This metadata
  includes all configuration data that you enter when creating and maintaining your Amazon S3
  buckets, such as bucket names.
- Do not enter export-controlled data in the following fields:
  - Resource tags
