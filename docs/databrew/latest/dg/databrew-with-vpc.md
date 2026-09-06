

# Using AWS Glue DataBrew with your VPC
<a name="databrew-with-vpc"></a>

If you use Amazon VPC to host your AWS resources, you can configure AWS Glue DataBrew to route traffic through your virtual private cloud (VPC) based on the Amazon VPC service. DataBrew does this by first provisioning an elastic network interface in the subnet that you specify. DataBrew then attaches the security group that you specify to that network interface to control access. The specified security group must have self-referencing inbound and outbound rules for all traffic. Also, your VPC must have DNS hostnames and resolution turned on. For more information, see [Setting Up a VPC to Connect to JDBC Data Stores](https://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-glue-access.html) in the *AWS Glue Developer Guide*.

For AWS Glue Data Catalog datasets, VPC information is configured when you create an AWS Glue connection in the Data Catalog. To create Data Catalog tables for this connection, run a crawler from the AWS Glue console. For more information, see [Populating the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) in the *AWS Glue Developer Guide*. 

For database datasets, specify your VPC information when you create the connection from the DataBrew console.

To use AWS Glue DataBrew with a VPC subnet without a [NAT](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html), you must have a gateway VPC endpoint to Amazon S3 and a VPC endpoint for the AWS Glue interface. For more information, see [Create a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-gateway.html#create-gateway-endpoint) and [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html) in the Amazon VPC documentation. The elastic interface provisioned by DataBrew does not have a public IPv4 address, and so it does not support use of a VPC Internet Gateway.

Amazon S3 interface endpoints are not supported at this time. If you are using AWS Secrets Manager to store your secret, you need a route to Secrets Manager. If you are using encryption, you need a route to AWS Key Management Service (AWS KMS). 