

# Using AWS Glue DataBrew with VPC endpoints
<a name="vpc-endpoint"></a>

If you use Amazon VPC to host your AWS resources, you can establish a private connection between your VPC and DataBrew by provisioning an VPC endpoint. Using this VPC endpoint, you can make DataBrew API calls.

 A DataBrew VPC endpoint is not required to use DataBrew with your VPC. For more information, see [Using AWS Glue DataBrew with your VPC](databrew-with-vpc.md). 

You can use AWS Glue with VPC endpoints in all AWS Regions that support both AWS Glue and VPC endpoints.

For more information, see these topics in the *Amazon VPC User Guide*:
+ [What Is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
+ [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint)