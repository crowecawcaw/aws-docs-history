# Access Elastic Load Balancing using an interface endpoint (AWS PrivateLink)

You can establish a private connection between your virtual private cloud (VPC) and the
Elastic Load Balancing API by creating an interface VPC endpoint. You can use this connection to call the
Elastic Load Balancing API from your VPC without requiring that you attach an internet gateway, NAT instance,
or VPN connection to your VPC. The endpoint provides reliable, scalable connectivity to the
Elastic Load Balancing API, versions 2015-12-01 and 2012-06-01, which you use to create and manage your load
balancers.

Interface VPC endpoints are powered by AWS PrivateLink, a feature that enables communication
between your applications and AWS services using private IP addresses. For more information,
see [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/").

###### Limit

AWS PrivateLink does not support Network Load Balancers with more than 50 listeners.

## Create an interface endpoint for Elastic Load Balancing

Create an endpoint for Elastic Load Balancing using the following service name:

```
com.amazonaws.`region`.elasticloadbalancing
```

For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink Guide_.

## Create a VPC endpoint policy for Elastic Load Balancing

You can attach a policy to your VPC endpoint to control access to the Elastic Load Balancing API. The
policy specifies:

- The principal that can perform actions.
- The actions that can be performed.
- The resource on which the actions can be performed.

The following example shows a VPC endpoint policy that denies everyone permission to
create a load balancer through the endpoint. The example policy also grants everyone
permission to perform all other actions.

```
{
   "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "elasticloadbalancing:CreateLoadBalancer",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.
