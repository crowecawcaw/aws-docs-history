# Access Amazon Application Recovery Controller (ARC) zonal shift using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
Amazon Application Recovery Controller (ARC) zonal shift. You can access ARC zonal shift as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Instances in your VPC don't need public IP addresses to access ARC zonal shift.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for ARC zonal shift.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for ARC zonal shift

Before you set up an interface endpoint for ARC zonal shift, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

ARC zonal shift supports making calls to all of its API actions through the interface
endpoint.

## Create an interface endpoint for ARC zonal shift

You can create an interface endpoint for ARC zonal shift using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for ARC zonal shift using the following service name:

```
com.amazonaws.`region`.arc-zonal-shift
```

If you enable private DNS for the interface endpoint, you can make API requests to
ARC zonal shift using its default Regional DNS name. For example,
`arc-zonal-shift.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to ARC zonal shift through the interface endpoint.
To control the access allowed to ARC zonal shift from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for ARC zonal shift actions

The following is an example of a custom endpoint policy. When you attach
this policy to your interface endpoint, it grants access to the listed ARC zonal shift
actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "arc-zonal-shift:ListManagedResources",
            "arc-zonal-shift:StartZonalShift",
            "arc-zonal-shift:CancelZonalShift"
         ],
         "Resource":"*"
      }
   ]
}
```

The `Resource` can also be listed as `arn:aws:elasticloadbalancing:us-east-`1:111122223333`:loadbalancer/app/Testing/`1111111ecd42dc05``.
