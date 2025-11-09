# Use interface VPC endpoints (AWS PrivateLink) to create a private connection between your VPC and Amazon Bedrock

You can use AWS PrivateLink to create a private connection between your VPC and
Amazon Bedrock. You can access Amazon Bedrock as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC don't need public IP addresses to access Amazon Bedrock.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for Amazon Bedrock.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Amazon Bedrock VPC

endpoints

Before you set up an interface endpoint for Amazon Bedrock, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Amazon Bedrock supports making the following API calls through VPC
endpoints.

| Category                                                                                                                                                                               | Endpoint suffix         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [Amazon Bedrock Control Plane API actions](../APIReference/API_Operations_Amazon_Bedrock.md "../APIReference/API_Operations_Amazon_Bedrock.md")                                        | `bedrock`               |
| [Amazon Bedrock Runtime API actions](../APIReference/API_Operations_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Amazon_Bedrock_Runtime.md")                              | `bedrock-runtime`       |
| [Amazon Bedrock Agents Build-time API actions](../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock.md")              | `bedrock-agent`         |
| [Amazon Bedrock Agents Runtime API actions](../APIReference/API_Operations_Agents_for_Amazon_Bedrock_Runtime.md "../APIReference/API_Operations_Agents_for_Amazon_Bedrock_Runtime.md") | `bedrock-agent-runtime` |

**Availability Zones**

Amazon Bedrock and Amazon Bedrock Agents endpoints are available in multiple Availability Zones.

## Create an interface endpoint for Amazon Bedrock

You can create an interface endpoint for Amazon Bedrock using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Amazon Bedrock using any of the following service
names:

- `com.amazonaws.`region`.bedrock`
- `com.amazonaws.`region`.bedrock-runtime`
- `com.amazonaws.`region`.bedrock-agent`
- `com.amazonaws.`region`.bedrock-agent-runtime`

After you create the endpoint, you have the option to enable a private DNS hostname. Enable this setting by selecting Enable Private DNS Name in the VPC console when you create the VPC endpoint.

If you enable private DNS for the interface endpoint, you can make API requests to
Amazon Bedrock using its default Regional DNS name. The following examples show the format of the default Regional DNS names.

- `bedrock.`region`.amazonaws.com`
- `bedrock-runtime.`region`.amazonaws.com`
- `bedrock-agent.`region`.amazonaws.com`
- `bedrock-agent-runtime.`region`.amazonaws.com`

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Amazon Bedrock through the interface endpoint.
To control the access allowed to Amazon Bedrock from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Amazon Bedrock actions

The following is an example of a custom endpoint policy. When you attach
this resource-based policy to your interface endpoint, it grants access to the listed Amazon Bedrock
actions for all principals on all resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": "*",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel",
 "bedrock:InvokeModelWithResponseStream"
 ],
 "Resource":"*"
 }
 ]
}`

```
