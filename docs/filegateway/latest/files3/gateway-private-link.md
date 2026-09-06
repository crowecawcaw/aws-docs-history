

# Activating a gateway in a virtual private cloud
<a name="gateway-private-link"></a>

You can create a private connection between your on-premises gateway appliance and cloud-based storage infrastructure. You can use this connection to activate your gateway and configure it to transfer data to AWS storage services without communicating over the public internet. Using the Amazon VPC service, you can launch AWS resources, including private network interface endpoints, in a custom virtual private cloud (VPC). A VPC gives you control over network settings such as IP address range, subnets, route tables, and network gateways. For more information about VPCs, see [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon VPC User Guide*.

To activate your gateway in a VPC, use the Amazon VPC Console to [create a VPC endpoint for Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/create-vpc-endpoint) and get the VPC endpoint ID, then specify this VPC endpoint ID when you create and activate the gateway. For more information, see [Connect your Amazon S3 File Gateway to AWS](https://docs.aws.amazon.com/filegateway/latest/files3/create-gateway-file.html#connect-to-amazon-s3-file).

To configure your S3 File Gateway to transfer data through the VPC, you must create a separate VPC endpoint for Amazon S3, then specify this VPC endpoint when you create file shares for the gateway.

**Note**  
You must activate your gateway in the same region where you create the VPC endpoint for Storage Gateway, and the Amazon S3 storage that you configure for the file share must be in the same region where you create the VPC endpoint for Amazon S3.