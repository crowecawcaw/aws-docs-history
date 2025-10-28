# Create a private connection between a VPC and Amazon EBS

You can establish a private connection between your VPC and Amazon EBS by creating an
_interface VPC endpoint_, powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"). You can access Amazon EBS as if it were in
your VPC, without using an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection. Instances in your VPC don't need public IP addresses to communicate with
Amazon EBS.

We create an endpoint network interface in each subnet that you enable for the interface
endpoint.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

###### Note

Amazon Data Lifecycle Manager supports IPv4 interface VPC endpoints for all commercial and AWS GovCloud (US)
Regions, and IPv6 interface VPC endpoints for commercial Regions only.

## Considerations for Amazon EBS VPC endpoints

Before you set up an interface VPC endpoint for Amazon EBS, review
[Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

By default, full access to Amazon EBS is allowed through the endpoint. You can control
access to the interface endpoint using VPC endpoint policies. You can attach an endpoint policy
to your VPC endpoint that controls access to Amazon EBS. The policy specifies the following
information:

- The **principal** that can perform actions.
- The **actions** that can be performed.
- The **resources** on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

The following is an example of an endpoint policy for Amazon EBS. When attached to
an endpoint, this policy grants all users permission to get summary information about
Amazon Data Lifecycle Manager policies.

```
{
  "Statement": [{
    "Action": "dlm:GetLifecyclePolicies",
    "Effect": "Allow",
    "Principal": "*",
    "Resource": "*"
  }]
}
```

## Create an interface VPC endpoint for Amazon EBS

You can create a VPC endpoint for Amazon EBS using either the Amazon VPC console or the AWS Command Line Interface
(AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create a VPC endpoint for Amazon EBS using the following service name:

- `com.amazonaws.`region`.dlm`

If you enable private DNS for the endpoint, you can make API requests to Amazon EBS using
its default DNS name for the Region, for example, `dlm.us-east-1.amazonaws.com`.
