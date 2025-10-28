# Creating an interface VPC endpoint for

Amazon WorkSpaces Secure Browser

You can create an interface VPC endpoint for the Amazon WorkSpaces Secure Browser service using either the
Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface
endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the following service name:

- com.amazonaws.`region`.workspaces-web
  For FIPS-supported regions, create an interface VPC endpoint for Amazon WorkSpaces Secure Browser using the
  following service name:

- com.amazonaws.`region`.workspaces-web-fips
