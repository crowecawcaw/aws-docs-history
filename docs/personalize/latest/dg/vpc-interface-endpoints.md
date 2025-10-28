# Amazon Personalize and interface VPC endpoints

(AWS PrivateLink)

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can
establish a private connection between your VPC and Amazon Personalize. This connection allows Amazon Personalize to communicate with your resources on your VPC
without going through the public internet.

Amazon VPC is an AWS service that you use to launch AWS resources in a virtual private cloud (VPC) or virtual network that
you define. With a VPC, you have control over your network settings, such the IP address
range, subnets, route tables, and network gateways. With VPC endpoints, the AWS network
handles the routing between your VPC and AWS services.

To connect your VPC to Amazon Personalize, you define an interface VPC endpoint for Amazon Personalize. An interface endpoint is an elastic
network interface with a private IP address that serves as an entry point for traffic destined to a supported
AWS service. The endpoint provides reliable, scalable connectivity to Amazon Personalize. It doesn't require an internet gateway, a
network address translation (NAT) instance, or a VPN connection. For more information, see [What is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in the _Amazon VPC User Guide_.

Interface VPC endpoints are enabled by AWS PrivateLink. This AWS technology enables
private communication between AWS services by using an elastic network interface with
private IP addresses.

###### Note

All Amazon Personalize Federal Information Processing Standard (FIPS) endpoints are supported
by AWS PrivateLink.

###### Topics

- [Creating an interface VPC endpoint for
  Amazon Personalize](#vpc-endpoint-create "#vpc-endpoint-create")
- [Creating a VPC endpoint policy for
  Amazon Personalize](#vpc-endpoint-policy "#vpc-endpoint-policy")

## Creating an interface VPC endpoint for

Amazon Personalize

You can create a VPC endpoint for the Amazon Personalize service with either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

To create a VPC endpoint for Amazon Personalize, choose one of the following for the service. You can choose to create an ipv4, ipv6, or dualstack endpoint.

- com.amazonaws.`region`.personalize
- com.amazonaws.`region`.personalize-events
- com.amazonaws.`region`.personalize-runtime

If you enable private DNS for the endpoint, you can make API requests to Amazon Personalize using its
default DNS name for the Region, for example, `personalize.us-east-1.api.aws`.

## Creating a VPC endpoint policy for

Amazon Personalize

You can attach an endpoint policy to your VPC endpoint that controls access to
Amazon Personalize. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy allowing all Amazon Personalize actions and passRole

actions

When attached to an endpoint, this policy grants access to all Amazon Personalize actions and
passRole actions.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "`personalize`:*",
                "`iam`:`PassRole`"
            ],
            "Resource": "*"
        }
    ]
}
```

###### Example: VPC endpoint policy allowing Amazon Personalize ListDatasets actions

When attached to an endpoint, this policy grants access to the listed Amazon Personalize
ListDatasets actions.

```
{
    "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
                "`personalize`:`ListDatasets`"
            ],
            "Resource": "*"
        }
    ]
}
```
