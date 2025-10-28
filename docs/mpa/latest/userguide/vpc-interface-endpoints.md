# Access Multi-party approval using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
Multi-party approval. You can access Multi-party approval as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC don't need public IP addresses to access Multi-party approval.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for Multi-party approval.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Multi-party approval

Before you set up an interface endpoint for Multi-party approval, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Multi-party approval supports making calls to all of its API actions through the interface
endpoint.

VPC endpoint policies are not supported for Multi-party approval. By default, full access to
Multi-party approval is allowed through the interface endpoint. Alternatively, you can associate
a security group with the endpoint network interfaces to control traffic to Multi-party approval
through the interface endpoint.

## Create an interface endpoint for Multi-party approval

You can create an interface endpoint for Multi-party approval using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Multi-party approval using the following service name:

```
com.amazonaws.`region`.mpa
```

If you enable private DNS for the interface endpoint, you can make API requests to
Multi-party approval using its default Regional DNS name. For example,
`com.amazonaws.us-east-1.mpa`.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to Multi-party approval through the interface endpoint.
To control the access allowed to Multi-party approval from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Multi-party approval actions

The following is an example of a custom endpoint policy. When you attach
this policy to your interface endpoint, it grants access to the listed Multi-party approval
actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "`mpa`:`GetIdentitySource`",
            "`mpa`:`GetApprovalTeam`"
         ],
         "Resource":"*"
      }
   ]
}
```
