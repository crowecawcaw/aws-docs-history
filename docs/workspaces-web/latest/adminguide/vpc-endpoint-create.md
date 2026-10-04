

Amazon WorkSpaces Secure Browser will no longer be open to new customers starting October 29, 2026. If you would like to use Amazon WorkSpaces Secure Browser, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [Amazon WorkSpaces Secure Browser availability change](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/workspaces-secure-browser-maintenance-mode.html). 

# Creating an interface VPC endpoint for Amazon WorkSpaces Secure Browser
<a name="vpc-endpoint-create"></a>

You can create an interface VPC endpoint for the Amazon WorkSpaces Secure Browser service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name: 
+ com.amazonaws.{{region}}.workspaces-web

For FIPS-supported regions, create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name: 
+ com.amazonaws.{{region}}.workspaces-web-fips