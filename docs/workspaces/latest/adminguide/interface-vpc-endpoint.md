

# Make Amazon WorkSpaces API requests through a VPC interface endpoint
<a name="interface-vpc-endpoint"></a>

You can connect directly to Amazon WorkSpaces API endpoints through an [interface endpoint](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html) in your virtual private cloud (VPC) instead of connecting over the internet. When you use a VPC interface endpoint, communication between your VPC and the Amazon WorkSpaces API endpoint is conducted entirely and securely within the AWS network.

**Note**  
This feature can be used only for connecting to WorkSpaces API endpoints. To connect to WorkSpaces using the WorkSpaces clients, internet connectivity is required, as described in [IP address and port requirements for WorkSpaces Personal](workspaces-port-requirements.md).

The Amazon WorkSpaces API endpoints support [Amazon Virtual Private Cloud](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html) (Amazon VPC) interface endpoints that are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/). Each VPC endpoint is represented by one or more [network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) (also known as elastic network interfaces, or ENIs) with private IP addresses in your VPC subnets.

The VPC interface endpoint connects your VPC directly to the Amazon WorkSpaces API endpoint without an internet gateway, NAT device, VPN connection, or Direct Connect connection. The instances in your VPC don't need public IP addresses to communicate with the Amazon WorkSpaces API endpoint.

You can create an interface endpoint to connect to Amazon WorkSpaces with either the AWS Management Console or AWS Command Line Interface (AWS CLI) commands. For instructions, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html#create-interface-endpoint).

*After you have created a VPC endpoint*, you can use the following example CLI commands that use the `endpoint-url` parameter to specify interface endpoints to the Amazon WorkSpaces API endpoint:

```
aws workspaces copy-workspace-image --endpoint-url {{VPC_Endpoint_ID}}.workspaces.{{Region}}.vpce.amazonaws.com

aws workspaces delete-workspace-image --endpoint-url {{VPC_Endpoint_ID.api}}.workspaces.{{Region}}.vpce.amazonaws.com

aws workspaces describe-workspace-bundles --endpoint-url {{VPC_Endpoint_ID}}.workspaces.{{Region}}.vpce.amazonaws.com  \
   --endpoint-name {{Endpoint_Name}} \
   --body "{{Endpoint_Body}}" \
   --content-type "{{Content_Type}}" \
       {{Output_File}}
```

If you enable private DNS hostnames for your VPC endpoint, you don't need to specify the endpoint URL. The Amazon WorkSpaces API DNS hostname that the CLI and Amazon WorkSpaces SDK use by default (https://api.workspaces.{{Region}}.amazonaws.com) resolves to your VPC endpoint.

The Amazon WorkSpaces API endpoint supports VPC endpoints in all AWS Regions where both [Amazon VPC](https://docs.aws.amazon.com/general/latest/gr/rande.html#vpc_region) and [Amazon WorkSpaces](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services) are available. Amazon WorkSpaces supports making calls to all of its [public APIs](https://docs.aws.amazon.com/workspaces/latest/api/welcome.html) inside your VPC.

To learn more about AWS PrivateLink, see the [AWS PrivateLink documentation](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html#what-is-privatelink). For the price of VPC endpoints, see [VPC Pricing](https://aws.amazon.com/vpc/pricing/). To learn more about VPC and endpoints, see [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

To see a list of Amazon WorkSpaces API endpoints by Region, see [WorkSpaces API Endpoints](workspaces-port-requirements.md#workspaces_api_endpoints).