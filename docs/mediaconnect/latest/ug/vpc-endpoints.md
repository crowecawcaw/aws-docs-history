# MediaConnect interface VPC endpoints

(AWS PrivateLink)

You can use an interface VPC endpoint to keep all MediaConnect API request traffic
between your VPC and MediaConnect in the Amazon network, thus improving the security of
your VPC. Interface VPC endpoints don't need an internet gateway, a NAT device, or a virtual
private gateway. The VPC endpoints are powered by AWS PrivateLink, a technology that you can
use to privately access MediaConnect APIs with private IP addresses.

For more information about AWS PrivateLink and VPC endpoints, see [VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the
_Amazon VPC User Guide_.

## Considerations for

MediaConnect VPC endpoints

Before you set up an interface endpoint for MediaConnect, be sure to review [Interface endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_, and be aware of the following
considerations:

- VPC endpoints currently don't support cross-Region requests. Ensure that you
  create your endpoint in the same Region where you plan to interact with
  MediaConnect.
- VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want
  to use your own DNS, you can use conditional DNS forwarding. For more
  information, see [DHCP Options
  Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the _Amazon VPC User Guide_.
- The security group attached to the VPC endpoint must allow incoming
  connections on port 443 from the private subnet of the VPC.

## Creating the VPC Endpoints for

MediaConnect

You can create an interface endpoint for MediaConnect using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). Follow the procedure outlined in [Creating
an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

## Controlling Access to VPC Endpoints for

MediaConnect

You can control access to MediaConnect by attaching an endpoint policy to your VPC
endpoint. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for actions

The following is an example of an endpoint policy for MediaConnect. When attached
to an endpoint, this policy grants access to the listed MediaConnect actions for
all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "mediaconnect:`action-1`",
            "mediaconnect:`action-2`",
            "mediaconnect:`action-3`"
         ],
         "Resource":"*"
      }
   ]
}
```
