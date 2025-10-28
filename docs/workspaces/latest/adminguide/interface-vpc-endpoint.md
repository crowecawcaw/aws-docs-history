# Make Amazon WorkSpaces API requests through a VPC interface

endpoint

You can connect directly to Amazon WorkSpaces API endpoints through an [interface
endpoint](../../../AmazonVPC/latest/UserGuide/vpce-interface.md "../../../AmazonVPC/latest/UserGuide/vpce-interface.md") in your virtual private cloud (VPC) instead of connecting over the
internet. When you use a VPC interface endpoint, communication between your VPC and the
Amazon WorkSpaces API endpoint is conducted entirely and securely within the AWS network.

###### Note

This feature can be used only for connecting to WorkSpaces API endpoints. To connect to
WorkSpaces using the WorkSpaces clients, internet connectivity is required, as described
in [IP address and port requirements for
WorkSpaces Personal](workspaces-port-requirements.md "workspaces-port-requirements.md").

The Amazon WorkSpaces API endpoints support [Amazon Virtual Private Cloud](../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md "../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md") (Amazon VPC)
interface endpoints that are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"). Each VPC endpoint is represented
by one or more [network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md")
(also known as elastic network interfaces, or ENIs) with private IP addresses in your VPC subnets.

The VPC interface endpoint connects your VPC directly to the Amazon WorkSpaces API endpoint
without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. The
instances in your VPC don't need public IP addresses to communicate with the Amazon WorkSpaces API endpoint.

You can create an interface endpoint to connect to Amazon WorkSpaces with either the AWS Management Console
or AWS Command Line Interface (AWS CLI) commands. For instructions, see [Creating an Interface Endpoint](../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint "../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint").

_After you have created a VPC endpoint_, you can use the following
example CLI commands that use the `endpoint-url` parameter to specify
interface endpoints to the Amazon WorkSpaces API endpoint:

```
aws workspaces copy-workspace-image --endpoint-url `VPC_Endpoint_ID`.workspaces.`Region`.vpce.amazonaws.com

aws workspaces delete-workspace-image --endpoint-url `VPC_Endpoint_ID.api`.workspaces.`Region`.vpce.amazonaws.com

aws workspaces describe-workspace-bundles --endpoint-url `VPC_Endpoint_ID`.workspaces.`Region`.vpce.amazonaws.com  \
   --endpoint-name `Endpoint_Name` \
   --body "`Endpoint_Body`" \
   --content-type "`Content_Type`" \
       `Output_File`
```

If you enable private DNS hostnames for your VPC endpoint, you don't need to specify
the endpoint URL. The Amazon WorkSpaces API DNS hostname that the CLI and Amazon WorkSpaces SDK use by default
(https://api.workspaces.`Region`.amazonaws.com) resolves to
your VPC endpoint.

The Amazon WorkSpaces API endpoint supports VPC endpoints in all AWS Regions where both [Amazon VPC](../../../general/latest/gr/rande.md#vpc_region "../../../general/latest/gr/rande.md#vpc_region") and
[Amazon WorkSpaces](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services")
are available. Amazon WorkSpaces supports making calls to all of its
[public APIs](../api/welcome.md "../api/welcome.md") inside
your VPC.

To learn more about AWS PrivateLink, see the [AWS PrivateLink documentation](../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md#what-is-privatelink "../../../AmazonVPC/latest/UserGuide/VPC_Introduction.md#what-is-privatelink"). For the price of VPC endpoints, see [VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/"). To learn more about VPC and endpoints, see [Amazon VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

To see a list of Amazon WorkSpaces API endpoints by Region, see
[WorkSpaces API Endpoints](workspaces-port-requirements.md#workspaces_api_endpoints "workspaces-port-requirements.md#workspaces_api_endpoints").

###### Note

Amazon WorkSpaces API endpoints with AWS PrivateLink are not supported for Federal Information
Processing Standard (FIPS) Amazon WorkSpaces API endpoints.
