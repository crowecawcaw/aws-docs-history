

# Data residency workloads
<a name="directory-bucket-data-residency"></a>

S3 directory buckets are available in AWS Dedicated Local Zones and in select AWS Local Zones. AWS Dedicated Local Zones (Dedicated Local Zones) are a type of AWS infrastructure that is fully managed by AWS, built for exclusive use by you or your community, and placed in a location or data center specified by you to help comply with regulatory requirements. Dedicated Local Zones are a type of AWS Local Zones (Local Zones) offering. For more information, see [AWS Dedicated Local Zones](https://aws.amazon.com/dedicatedlocalzones/).

In Dedicated Local Zones, you can create S3 directory buckets to store data in a specific data perimeter, which helps support data residency and isolation use cases. Directory buckets in Dedicated Local Zones can support the S3 Express One Zone and S3 One Zone-Infrequent Access (S3 One Zone-IA; Z-IA) storage classes. 

A Local Zone is a type of AWS infrastructure that places select compute, storage, and other services near large populations and industry centers. To learn more, see [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/). You can create S3 directory buckets to store data in a specific data perimeter, which helps support data residency use cases. Directory buckets in Local Zones support the S3 One Zone-Infrequent Access (S3 One Zone-IA; Z-IA) storage class. For more information about supported locations, see [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/).

You can use the directory buckets in Local Zones using the AWS Management Console, REST API, AWS Command Line Interface (AWS CLI), and AWS SDKs. 

For more information about working with the directory buckets in Local Zones, see the following topics:

**Topics**
+ [Concepts for directory buckets in Local Zones](s3-lzs-for-directory-buckets.md)
+ [Enable accounts for Local Zones](opt-in-directory-bucket-lz.md)
+ [Private connectivity from your VPC](connectivity-lz-directory-buckets.md)
+ [Creating a directory bucket in a Local Zone](create-directory-bucket-LZ.md)
+ [Authenticating and authorizing for directory buckets in Local Zones](iam-directory-bucket-LZ.md)