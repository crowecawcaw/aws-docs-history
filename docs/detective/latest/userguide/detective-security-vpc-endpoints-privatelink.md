# Amazon Detective and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Detective by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access Detective APIs without an internet gateway, NAT device, VPN connection, or
AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to
communicate with Detective APIs. Traffic between your VPC and Detective does not leave the Amazon
network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in the _AWS PrivateLink Guide_.

## Considerations for Detective VPC

endpoints

Before you set up an interface VPC endpoint for Detective, ensure that you review [Interface endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") in the _AWS PrivateLink Guide_.

Detective supports making calls to all of its API actions from your VPC.

Detective supports FIPS in the following Regions:

- US East (N. Virginia)
- US East (Ohio)
- US West (N. California)
- US West (Oregon)
- Canada (Central)

## Creating an interface VPC endpoint for

Detective

You can create a VPC endpoint for the Detective service using either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

Create a VPC endpoint for Detective using the following service name:

- com.amazonaws.`region`.detective
- com.amazonaws.`region`.detective-fips

If you enable private DNS for the endpoint, you can make API requests to Detective using
its default DNS name for the Region, for example,
`api.detective.`us-east-1`.amazonaws.com`. For more information, see
[Amazon Detective endpoints](../../../general/latest/gr/detective.md "../../../general/latest/gr/detective.md") in the _Amazon Web Services General Reference_.

For more information, see [Access a service through an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#access-service-though-endpoint") in the
_AWS PrivateLink Guide_.

## Creating a VPC endpoint policy for Detective

You can attach an endpoint policy to your VPC endpoint that controls access to Detective.
The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control
access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Detective actions

The following is an example of an endpoint policy for Detective. When attached to an
endpoint, this policy grants access to the listed Detective actions for all principals
on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "detective:ListGraphs",
            "detective:ListMembers"
         ],
         "Resource":"*"
      }
   ]
}
```

## Shared subnets

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared
with you. However, you can use the VPC endpoints in subnets that are shared with you.
For information about VPC sharing, see [Share your VPC with other
accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon VPC User Guide_.
