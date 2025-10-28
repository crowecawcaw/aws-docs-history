# Access AWS Network Firewall using an interface endpoint

You can create a private connection between your VPC and AWS Network Firewall. You can access AWS Network Firewall
as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC don't need public IP addresses to access AWS Network Firewall.

For more information, see
[Access an AWS
service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink Guide_.

## Considerations for AWS Network Firewall

Before you set up an interface endpoint for AWS Network Firewall, review [Interface endpoint properties and
limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") in the _AWS PrivateLink Guide_.

AWS Network Firewall supports making calls to all of its API actions through the interface endpoint.

Before you set up interface VPC endpoints for Network Firewall, be aware of the following considerations:

- VPC endpoints currently don't support cross-Region requests. Ensure that you create your endpoint in the same
  Region where you plan to issue your API calls to Network Firewall.
- VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want to use your own DNS, you can use
  conditional DNS forwarding. For more information, see [DHCP Options
  Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md") in the _Amazon VPC User Guide_.
- The security group attached to the VPC endpoint must allow incoming connections on port 443 from the private
  subnet of the VPC.
- VPC interface endpoints are supported in all AWS Regions supported by Network Firewall.

## Create an interface VPC endpoint for AWS Network Firewall

You can create an interface VPC endpoint using the Amazon VPC Console.
For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _AWS PrivateLink Guide_.

When you create an interface VPC endpoint, use the following service name:

```
com.amazonaws.`region`.network-firewall
```

For example:

```
com.amazonaws.`us-west-2`.network-firewall
```

## Create a VPC endpoint policy for AWS Network Firewall

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to AWS Network Firewall through the interface endpoint.
To control the access allowed to AWS Network Firewall from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, users, and IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

## Example: VPC endpoint policy for AWS Network Firewall

The following is an example of a custom endpoint policy. When you attach this policy to your interface VPC endpoint,
it grants access to the AWS Network Firewall actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "network-firewall:ListFirewalls",
            "network-firewall:DescribeFirewall"
         ],
         "Resource":"*"
      }
   ]
}
```
