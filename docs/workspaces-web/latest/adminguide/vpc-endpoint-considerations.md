

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Considerations for Amazon WorkSpaces Secure Browser
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Amazon WorkSpaces Secure Browser APIs, make sure to review the "Prerequisites" in [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html). Amazon WorkSpaces Secure Browser supports making calls to all of its API actions through the interface VPC endpoint. 

By default, full access to Amazon WorkSpaces Secure Browser is allowed through the endpoint. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.