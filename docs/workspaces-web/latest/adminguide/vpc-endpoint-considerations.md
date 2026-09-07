

# Considerations for Amazon WorkSpaces Secure Browser
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Amazon WorkSpaces Secure Browser APIs, make sure to review the "Prerequisites" in [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). Amazon WorkSpaces Secure Browser supports making calls to all of its API actions through the interface VPC endpoint. 

By default, full access to Amazon WorkSpaces Secure Browser is allowed through the endpoint. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.