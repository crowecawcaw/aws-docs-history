

# Using Amazon S3 VPC Endpoints for WorkSpaces Pools Features
<a name="managing-network-vpce-iam-policy"></a>

When you enable Application Settings Persistence for a WorkSpaces Pool or Home folders for a WorkSpaces Pool directory, WorkSpaces uses the VPC you specify for your directory to provide access to Amazon Simple Storage Service (Amazon S3) buckets. To enable WorkSpaces Pools access to your private S3 endpoint, attach the following custom policy to your VPC endpoint for Amazon S3. For more information about private Amazon S3 endpoints, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) and [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.

------
#### [ Commercial AWS Regions ]

Use the following policy for resources in the commercial AWS Regions.

------
#### [ AWS GovCloud (US) Regions ]

Use the following policy for resources in the commercial AWS GovCloud (US) Regions.

------