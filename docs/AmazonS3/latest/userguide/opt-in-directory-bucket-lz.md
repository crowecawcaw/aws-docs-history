

# Enable accounts for Local Zones
<a name="opt-in-directory-bucket-lz"></a>

The following topics describe how accounts are enabled for AWS Local Zones:

## AWS Local Zones
<a name="opt-in-lz"></a>

To get started using AWS Local Zones, you must first opt in to a Local Zone through the AWS Global View console or the AWS CLI. To learn more, see [Getting started with AWS Local Zones](https://docs.aws.amazon.com/local-zones/latest/ug/getting-started.html). You can use the [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) API operation to confirm your account ID access to a list of AWS Local Zones.

## AWS Dedicated Local Zones
<a name="opt-in-dlz"></a>

For all the services in AWS Dedicated Local Zones (Dedicated Local Zones), including Amazon S3, your administrator must enable your AWS account before you can create or access any resource in the Dedicated Local Zone. You can use the [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) API operation to confirm your account ID access to a Local Zone.

## Data protection for directory buckets in Local Zones
<a name="data-protection-directory-bucket-lz"></a>

To further protect your data in Amazon S3, by default, you only have access to the S3 resources that you create. Buckets in Local Zones have all S3 Block Public Access settings enabled by default and S3 Object Ownership is set to bucket owner enforced. These settings can't be modified. Optionally, to restrict access to only within the Local Zone network border groups, you can use the condition key `s3express:AllAccessRestrictedToLocalZoneGroup` in your IAM policies. For more information, see [Authenticating and authorizing for directory buckets in Local Zones](iam-directory-bucket-LZ.md).