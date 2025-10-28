# Using AWS Glue DataBrew with VPC endpoints

If you use Amazon VPC to host your AWS resources, you can establish a private connection
between your VPC and DataBrew by provisioning an VPC endpoint. Using this VPC endpoint, you can make
DataBrew API calls.

A DataBrew VPC endpoint is not required to use DataBrew with your VPC. For more information,
see [Using AWS Glue DataBrew with your VPC](databrew-with-vpc.md "databrew-with-vpc.md").

You can use AWS Glue with VPC endpoints in all AWS Regions that support both AWS Glue and
VPC endpoints.

For more information, see these topics in the _Amazon VPC User Guide_:

- [What Is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
- [Creating an Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint")
