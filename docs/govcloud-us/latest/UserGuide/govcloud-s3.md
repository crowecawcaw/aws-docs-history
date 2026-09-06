

# Amazon S3 in AWS GovCloud (US)
<a name="govcloud-s3"></a>

Amazon Simple Storage Service (Amazon S3) is storage for the internet. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web. You can accomplish these tasks using the simple and intuitive web interface of the AWS Management Console.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Simple Storage Service differs
<a name="govcloud-s3-diffs"></a>

The following differences apply to Amazon Simple Storage Service:
+ {r53long} Private DNS for VPCs is currently not supported for Amazon S3 endpoints.
+ You cannot do a direct copy of the contents of an Amazon S3 bucket in the AWS GovCloud (US) Regions to or from another AWS Region.
+ If you use Amazon S3 policies, use the AWS GovCloud (US) Amazon Resource Name (ARN) identifier. For more information, see [Amazon Resource Names (ARNs) in AWS GovCloud (US) Regions](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/using-govcloud-arns.html).
+ In the AWS GovCloud (US) Regions, Amazon S3 has three endpoints. If you are processing export-controlled data, use one of the SSL endpoints. If you have FIPS requirements, use a FIPS 140-3 endpoint (https://s3-fips.us-gov-west-1.amazonaws.com or https://s3-fips.us-gov-east-1.amazonaws.com).
+  Amazon S3 bucket names are unique to the AWS GovCloud (US) Regions. Bucket names in the AWS GovCloud (US) Regions are not shared across other AWS Regions.
+ Multi-factor authentication (MFA) delete is not available.
+  [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html) is not available.
+  Amazon S3 Object Lambda Access Points are available in the AWS GovCloud (US) Regions for SSL endpoints. Object Lambda Access Points are not available for FIPS endpoints.
+  Amazon S3 presigned URLs are available only through the AWS Command Line Interface (AWS CLI) and AWS SDKs.
+ Bucket-style aliases for your Amazon S3 Object Lambda Access Points are not available.
+  Amazon S3 Express One Zone is not available.
+  Amazon S3 Tables replication is not available.
+ Access points for directory buckets are not available.
+ You cannot use S3 access points to access file data stored on Amazon FSx file systems.

## Documentation
<a name="govcloud-s3-docs"></a>
+  [Amazon S3 documentation](https://docs.aws.amazon.com/documentation/s3/) 

## Export-controlled content
<a name="govcloud-s3-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon S3 metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon S3 buckets, such as bucket names.
+ Do not enter export-controlled data in the following fields:
  + Resource tags