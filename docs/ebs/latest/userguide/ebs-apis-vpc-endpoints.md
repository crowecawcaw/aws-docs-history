# Create a private connection between a VPC and EBS direct APIs

You can establish a private connection between your VPC and EBS direct APIs by creating an
_interface VPC endpoint_, powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"). You can access EBS direct APIs as if it were in
your VPC, without using an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection. Instances in your VPC don't need public IP addresses to communicate with
EBS direct APIs.

We create an endpoint network interface in each subnet that you enable for the interface
endpoint.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for EBS direct APIs VPC endpoints

Before you set up an interface VPC endpoint for EBS direct APIs, review
[Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

By default, full access to EBS direct APIs is allowed through the endpoint. You can control
access to the interface endpoint using VPC endpoint policies. You can attach an endpoint policy
to your VPC endpoint that controls access to EBS direct APIs. The policy specifies the following
information:

- The **principal** that can perform actions.
- The **actions** that can be performed.
- The **resources** on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

The following is an example of an endpoint policy for EBS direct APIs. When attached to an
endpoint, this policy grants access to all EBS direct APIs actions on all resources, except snapshots
that are tagged with key `Environment` and value `Test`.

```
{
    "Statement": [
        {
            "Effect": "Deny",
            "Action": "ebs:*",
            "Principal": "*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Environment": "Test"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "ebs:*",
            "Principal": "*",
            "Resource": "*"
        }
    ]
}
```

## Create an interface VPC endpoint for EBS direct APIs

You can create a VPC endpoint for EBS direct APIs using either the Amazon VPC console or the AWS Command Line Interface
(AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create a VPC endpoint for EBS direct APIs using one of the following service names:

- `com.amazonaws.`region`.ebs`
- `com.amazonaws.`region`.ebs-fips` — To create an interface
  VPC endpoint that complies with the Federal Information Processing Standard (FIPS) Publication 140-2 US
  government standard.

###### Note

FIPS-compliant interface VPC endpoints can be created for the following Regions:
`us-east-1` | `us-east-2` | `us-west-1` | `us-west-2` |
`ca-central-1` | `ca-west-1`. FIPS-compliant interface VPC endpoints
support both IPv4 and IPv6 traffic.

If you enable private DNS for the endpoint, you can make API requests to EBS direct APIs using
its default DNS name for the Region, for example, `ebs.us-east-1.amazonaws.com`.
