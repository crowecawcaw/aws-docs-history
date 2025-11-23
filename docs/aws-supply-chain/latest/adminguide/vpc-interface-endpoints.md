# Access AWS Supply Chain using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
AWS Supply Chain. You can access AWS Supply Chain as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or Direct Connect connection.
Instances in your VPC don't need public IP addresses to access AWS Supply Chain.

You establish this private connection by creating an \*interface

endpoint\*, powered by AWS PrivateLink. We create an endpoint network interface in

each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for AWS Supply Chain.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for AWS Supply Chain

Before you set up an interface endpoint for AWS Supply Chain, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

AWS Supply Chain supports making calls to all of its API actions through the interface
endpoint.

## Create an interface endpoint for AWS Supply Chain

You can create an interface endpoint for AWS Supply Chain using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for AWS Supply Chain using the following service name:

```
com.amazonaws.`region`.`scn`
```

If you enable private DNS for the interface endpoint, you can make API requests to
AWS Supply Chain using its default Regional DNS name. For example,

``scn`.`region`.amazonaws.com`.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to AWS Supply Chain through the interface endpoint.
To control the access allowed to AWS Supply Chain from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and

IAM roles)

- The actions that can be performed
- The resources on which the actions can be performed

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for AWS Supply Chain actions

The following is an example of a custom endpoint policy. When you attach
this policy to your interface endpoint, it grants access to the listed AWS Supply Chain
actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [

            "`scn`:`action-1`",
            "`scn`:`action-2`",
            "`scn`:`action-3`"

         ],
         "Resource":"*"
      }
   ]
}
```
