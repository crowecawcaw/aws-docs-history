

# Best Practices for Enabling Application Settings Persistence
<a name="best-practices-app-settings-persistence"></a>

To enable application settings persistence without providing internet access to your instances, use a VPC endpoint. This endpoint must be in the VPC to which your WorkSpaces Applications instances are connected. You must attach a custom policy to enable WorkSpaces Applications access to the endpoint. For information about how to create the custom policy, see the *Home Folders and VPC Endpoints* section in [Networking and Access for Amazon WorkSpaces Applications](managing-network.md). For more information about private Amazon S3 endpoints, see [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html) and [Endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-s3.html) in the *Amazon VPC User Guide*.