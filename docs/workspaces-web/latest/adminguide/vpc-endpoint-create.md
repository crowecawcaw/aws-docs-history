

# Creating an interface VPC endpoint for Amazon WorkSpaces Secure Browser
<a name="vpc-endpoint-create"></a>

You can create an interface VPC endpoint for the Amazon WorkSpaces Secure Browser service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name: 
+ com.amazonaws.{{region}}.workspaces-web

For FIPS-supported regions, create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name: 
+ com.amazonaws.{{region}}.workspaces-web-fips