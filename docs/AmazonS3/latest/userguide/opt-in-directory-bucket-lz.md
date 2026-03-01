# Enable accounts for Local Zones

The following topic describes how accounts are enabled for Dedicated Local Zones.

For all the services in AWS Dedicated Local Zones (Dedicated Local Zones), including Amazon S3, your administrator must
enable your AWS account before you can create or access any resource in the Dedicated Local Zone.
You can use the
[DescribeAvailabilityZones](../../../AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.md "../../../AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.md") API operation to confirm your account ID access to a Local Zone.

To further protect your data in Amazon S3, by default, you only have access to the S3 resources
that you create. Buckets in Local Zones have all S3 Block Public Access settings enabled by
default and S3 Object Ownership is set to bucket owner enforced. These settings can't be
modified. Optionally, to restrict access to only within the Local Zone network border groups, you
can use the condition key `s3express:AllAccessRestrictedToLocalZoneGroup` in your
IAM policies. For more information, see [Authenticating and authorizing for directory buckets in Local Zones](iam-directory-bucket-LZ.md "iam-directory-bucket-LZ.md").
