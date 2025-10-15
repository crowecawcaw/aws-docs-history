# Data residency workloads

AWS Dedicated Local Zones (Dedicated Local Zones) are a type of AWS Infrastructure that are fully managed by AWS,
 built for exclusive use by you or your community, and placed in a location or data center
 specified by you to help comply with regulatory requirements. Dedicated Local Zones are a type of AWS Local Zones
 (Local Zones) offering. For more information, see [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/ "https://aws.amazon.com/dedicatedlocalzones/").

In Dedicated Local Zones, you can create S3 directory buckets to store data in a specific data
 perimeter, which helps support data residency and isolation use cases.

 Directory buckets in Dedicated Local Zones can support the S3 Express One Zone and S3 One Zone-Infrequent Access (S3 One Zone-IA; Z-IA) storage classes.
 Directory buckets are not currently available in other [AWS Local Zones locations](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/").
 

You can use the
 AWS Management Console, REST API, AWS Command Line Interface (AWS CLI), and AWS SDKs in Dedicated Local Zones. 

For more information about working with the directory buckets in Local Zones, see the following topics:

###### Topics

* [Concepts for directory buckets in
 Local Zones](s3-lzs-for-directory-buckets.md "s3-lzs-for-directory-buckets.md")
* [Enable accounts for Local Zones](opt-in-directory-bucket-lz.md "opt-in-directory-bucket-lz.md")
* [Private connectivity from your
 VPC](connectivity-lz-directory-buckets.md "connectivity-lz-directory-buckets.md")
* [Creating a directory bucket in a Local Zone](create-directory-bucket-LZ.md "create-directory-bucket-LZ.md")
* [Authenticating and authorizing for
 directory buckets in Local Zones](iam-directory-bucket-LZ.md "iam-directory-bucket-LZ.md")
