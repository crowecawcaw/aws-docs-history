# Create a private connection between a VPC and AWS Transfer Family

APIs

You can establish a private connection between your VPC and AWS Transfer Family APIs by creating an
_interface VPC endpoint_, powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"). You can access AWS Transfer Family APIs as if it were
in your VPC, without using an internet gateway, NAT device, VPN connection, or AWS Direct
Connect connection. Instances in your VPC don't need public IP addresses to communicate with
AWS Transfer Family APIs.

We create an endpoint network interface in each subnet that you enable for the interface
endpoint. For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.
Before you set up an interface VPC endpoint for AWS Transfer Family APIs, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

## Controlling access using VPC endpoint

policies

By default, full access to AWS Transfer Family APIs is allowed through the endpoint. You can
control access to the interface endpoint using VPC endpoint policies. You can attach an
endpoint policy to your VPC endpoint that controls access to AWS Transfer Family APIs. The policy
specifies the following information:

- The **principal** that can perform
  actions.
- The **actions** that can be performed.
- The **resources** on which actions can be
  performed.

For more information, see [Controlling access to
services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

The following is an example of an endpoint policy for AWS Transfer Family APIs. When attached to
an endpoint, this policy grants access to all AWS Transfer Family APIs actions on all resources,
except those that are tagged with key `Environment` and value
`Test`.

```
{
    "Statement": [{
        "Effect": "Deny",
        "Action": "transfer:StartFileTransfer",
        "Principal": "*",
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "aws:ResourceTag/Environment": "Test"
            }
        }
    }, {
        "Effect": "Allow",
        "Action": "transfer:*",
        "Principal": "*",
        "Resource": "*"
    }]
}
```

## Create an interface VPC endpoint for AWS Transfer Family

APIs

You can create a VPC endpoint for AWS Transfer Family APIs using either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink
Guide_.

Create a VPC endpoint for AWS Transfer Family APIs using one of the following service
names:

- `com.amazonaws.`region`.transfer`
- `com.amazonaws.`region`.transfer-fips` —
  To create an interface VPC endpoint that complies with the Federal Information
  Processing Standard (FIPS) Publication 140-3 US government standard.

If you enable private DNS for the endpoint, you can make API requests to AWS Transfer Family APIs
using its default DNS name for the Region, for example,
`transfer.us-east-1.amazonaws.com`.
