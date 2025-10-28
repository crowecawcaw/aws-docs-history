# Amazon Comprehend Medical and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Comprehend Medical by creating an
_interface VPC endpoint_. Interface VPC endpoints are powered by
[AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that you
can use to privately access Amazon Comprehend Medical APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to
communicate with Amazon Comprehend Medical APIs. Traffic between your VPC and Amazon Comprehend Medical does not
leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Amazon Comprehend Medical VPC

endpoints

Before you set up an interface VPC endpoint for Amazon Comprehend Medical, ensure that you review
[Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Amazon Comprehend Medical supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for

Amazon Comprehend Medical

You can create a VPC endpoint for the Amazon Comprehend Medical service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Amazon Comprehend Medical using the following service name:

- com.amazonaws.`region`.comprehendmedical

If you turn on private DNS for the endpoint, you can make API requests to Amazon Comprehend Medical
using its default DNS name for the Region. For example, `*comprehendmedical.us-east-1.amazonaws.com*`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

Amazon Comprehend Medical

You can attach an endpoint policy to your VPC endpoint that controls access to
Amazon Comprehend Medical. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Amazon Comprehend Medical actions

The following is an example of an endpoint policy for Amazon Comprehend Medical. When attached
to an endpoint, this policy grants access to the Amazon Comprehend Medical
`DetectEntitiesV2` action for all principals on all
resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`comprehendmedical`:`DetectEntitiesV2`"
         ],
         "Resource":"*"
      }
   ]
}
```
