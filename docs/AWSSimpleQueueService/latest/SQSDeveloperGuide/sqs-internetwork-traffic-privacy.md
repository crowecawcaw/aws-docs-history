# Internetwork traffic privacy in

Amazon SQS

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon SQS is a logical entity within a VPC that allows
connectivity only to Amazon SQS. The VPC routes requests to Amazon SQS and routes responses back
to the VPC. The following sections provide information about working with VPC endpoints
and creating VPC endpoint policies.

## Amazon Virtual Private Cloud endpoints for Amazon SQS

If you use Amazon VPC to host your AWS resources, you can establish a connection
between your VPC and Amazon SQS. You can use this connection to send messages to your
Amazon SQS queues without crossing the public internet.

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a
VPC to control your network settings, such as the IP address range, subnets, route
tables, and network gateways. For more information about VPCs, see the
_[Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md")_.

To connect your VPC to Amazon SQS, you must first define an _interface VPC endpoint_, which lets you connect your VPC to other
AWS services. The endpoint provides reliable, scalable connectivity to Amazon SQS
without requiring an internet gateway, network address translation (NAT) instance,
or VPN connection. For more information, see [Tutorial: Sending a message to an Amazon SQS
queue from Amazon Virtual Private Cloud](sqs-sending-messages-from-vpc.md "sqs-sending-messages-from-vpc.md") and [Example 5: Deny access if it isn't from
a VPC endpoint](sqs-creating-custom-policies-access-policy-examples.md#deny-not-from-vpc "sqs-creating-custom-policies-access-policy-examples.md#deny-not-from-vpc") in this guide
and [Interface VPC Endpoints
(AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

###### Important

- You can use Amazon Virtual Private Cloud only with HTTPS Amazon SQS endpoints.
- When you configure Amazon SQS to send messages from Amazon VPC, you must enable private DNS and
  specify endpoints in the format
  `sqs.`us-east-2`.amazonaws.com` or `sqs.`us-east-2`.api.aws` for the dual-stack endpoint.
- Amazon SQS also supports FIPS endpoints through PrivateLink using the `com.amazonaws.region.sqs-fips` endpoint service. You can connect to FIPS endpoints in the format `sqs-fips.region.amazonaws.com`.
- When using the dual-stack endpoint in Amazon Virtual Private Cloud, requests will be sent using IPv4 and IPv6.
- Private DNS doesn't support legacy endpoints such as
  `queue.amazonaws.com` or
  ``us-east-2`.queue.amazonaws.com`.

## Creating an Amazon VPC endpoint policy for

Amazon SQS

You can create a policy for Amazon VPC endpoints for Amazon SQS in which you specify the
following:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the
_Amazon VPC User Guide_

The following example VPC endpoint policy specifies that the user
`MyUser` is allowed to send messages to the Amazon SQS queue
`MyQueue`.

```
{
   "Statement": [{
      "Action": ["sqs:SendMessage"],
      "Effect": "Allow",
      "Resource": "arn:aws:sqs:us-east-2:123456789012:MyQueue",
      "Principal": {
        "AWS": "arn:aws:iam:123456789012:user/MyUser"
      }
   }]
}
```

The following are denied:

- Other Amazon SQS API actions, such as `sqs:CreateQueue` and
  `sqs:DeleteQueue`.
- Other users and rules which attempt to use this VPC endpoint.
- `MyUser` sending messages to a different Amazon SQS queue.

###### Note

The user can still use other Amazon SQS API actions from
_outside_ the VPC. For more information, see [Example 5: Deny access if it isn't from
a VPC endpoint](sqs-creating-custom-policies-access-policy-examples.md#deny-not-from-vpc "sqs-creating-custom-policies-access-policy-examples.md#deny-not-from-vpc").
