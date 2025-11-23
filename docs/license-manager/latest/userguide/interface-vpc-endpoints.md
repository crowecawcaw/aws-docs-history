# License Manager and interface VPC endpoints with

AWS PrivateLink

You can establish a private connection between your virtual private cloud (VPC) and
AWS License Manager by creating an interface VPC endpoint. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that you can use
to privately access the License Manager API without an internet gateway, NAT device, VPN connection,
or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate
with License Manager. Traffic between your VPC and License Manager does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

## Create an interface VPC endpoint for License Manager

Create an interface endpoint for License Manager using one of the following service
names:

- com.amazonaws.`region`.license-manager
- com.amazonaws.`region`.license-manager-fips

If you enable private DNS for the endpoint, you can make API requests to License Manager using
its default DNS name for the Region. For example,
`license-manager.`region`.amazonaws.com`.

For more information, see [Creating an
Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

## Create a VPC endpoint policy for License Manager

You can attach a policy to your VPC endpoint to control access to License Manager. The policy
specifies the following information:

- The principal that can perform actions
- The actions that can be performed
- The resource on which the actions can be performed

The following is an example of an endpoint policy for License Manager. When attached to an
endpoint, this policy grants access to the specified License Manager actions for all principals on
all resources.

```
{
   "Statement": [
        {
            "Principal": "*",
            "Effect": "Allow",
            "Action": [
              "license-manager:*"
            ],
            "Resource": "*"
        }
    ]
}
```

For more information, see [Controlling access to services
using VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.
