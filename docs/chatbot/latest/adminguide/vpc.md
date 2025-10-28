AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Connecting to Amazon Q Developer in chat applications with interface VPC endpoints

You can use AWS PrivateLink to create a private connection between your virtual private cloud (VPC) and Amazon Q Developer in chat applications so that you can access the service as if it were in your own VPC.
This doesn't require the use of an internet gateway, network address translation (NAT) device, virtual private network (VPN) connection, or AWS Direct Connect connection.
You establish this private connection by creating an interface endpoint that is powered by AWS PrivateLink.
An interface endpoint is an elastic network interface with a private IP address

that serves as an entry point for traffic destined to a supported AWS service. The endpoint provides reliable and scalable connectivity to Amazon Q Developer in chat applications, without requiring an internet
gateway, NAT instance, or VPN connection. Instances in your VPC don't need public IP addresses to access Amazon Q Developer in chat applications. For more information, see [Amazon Virtual Private Cloud](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")

and [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint").

###### Topics

- [Creating an interface VPC endpoint for Amazon Q Developer in chat applications](#creating-vpc-endpoint "#creating-vpc-endpoint")
- [Creating a VPC endpoint policy for Amazon Q Developer in chat applications](#creating-vpc-endpoint-policy "#creating-vpc-endpoint-policy")

## Creating an interface VPC endpoint for Amazon Q Developer in chat applications

You can create a VPC endpoint for Amazon Q Developer in chat applications using the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see
[Creating an interface Endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Amazon Q Developer in chat applications using one of the following service names:

- `com.amazonaws.us-east-2.chatbot`
- `com.amazonaws.us-west-2.chatbot`
- `com.amazonaws.eu-west-1.chatbot`
- `com.amazonaws.ap-southeast-1.chatbot`

If you enable private domain name system (DNS) for the endpoint, you can make API requests to Amazon Q Developer in chat applications using its default DNS name.
For example, `chatbot.us-east-2.amazonaws.com`. For more information, see
[Accessing a service through an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#access-service-though-endpoint")
in the _Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Amazon Q Developer in chat applications

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon Q Developer in chat applications. The policy specifies the following information:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md")
in the _Amazon VPC User Guide_.

### Example: VPC endpoint policy for Amazon Q Developer in chat applications actions

The following endpoint policy grants access to the listed Amazon Q Developer in chat applications
actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "chatbot:CreateSlackChannelConfiguration",
            "chatbot:DescribeSlackChannelConfigurations",
            "chatbot:UpdateSlackChannelConfiguration"
         ],
         "Resource":"*"
      }
   ]
}


```
