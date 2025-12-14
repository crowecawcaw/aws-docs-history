# AWS Security Hub CSPM and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS Security Hub CSPM by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access Security Hub CSPM APIs without an internet gateway, NAT device, VPN connection, or
AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to
communicate with Security Hub CSPM APIs. Traffic between your VPC and Security Hub CSPM does not leave the Amazon
network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets. For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in
the _Amazon Virtual Private Cloud Guide_.

## Considerations for Security Hub CSPM VPC

endpoints

Before you set up an interface VPC endpoint for Security Hub CSPM, ensure that you review the
prerequisites and other information in the [Amazon Virtual Private Cloud Guide](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md").

Security Hub CSPM supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for

Security Hub CSPM

You can create a VPC endpoint for the Security Hub CSPM service using either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _Amazon Virtual Private Cloud Guide_.

Create a VPC endpoint for Security Hub CSPM using the following service name:

`com.amazonaws.`region`.securityhub`

Where `region` is the Region code for the applicable
AWS Region.

If you enable private DNS for the endpoint, you can make API requests to Security Hub CSPM using
its default DNS name for the Region, for example,
`securityhub.us-east-1.amazonaws.com` for the US East (N. Virginia) Region.

## Creating a VPC endpoint policy for Security Hub CSPM

You can attach an endpoint policy to your VPC endpoint that controls access to Security Hub CSPM.
The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control
access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon Virtual Private Cloud Guide_.

###### Example: VPC endpoint policy for Security Hub CSPM actions

The following is an example of an endpoint policy for Security Hub CSPM. When attached to an
endpoint, this policy grants access to the listed Security Hub CSPM actions for all principals
on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "securityhub:getFindings",
            "securityhub:getEnabledStandards",
            "securityhub:getInsights"
         ],
         "Resource":"*"
      }
   ]
}
```

## Shared subnets

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared
with you. However, you can use the VPC endpoints in subnets that are shared with you.
For information about VPC sharing, see [Share your VPC subnets with other
accounts](../../../vpc/latest/userguide/vpc-sharing.md "../../../vpc/latest/userguide/vpc-sharing.md") in the _Amazon Virtual Private Cloud Guide_.
