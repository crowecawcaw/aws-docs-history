# IAM Roles Anywhere and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS Identity and Access Management Roles Anywhere by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access IAM Roles Anywhere APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with IAM Roles Anywhere APIs. Traffic between your VPC and IAM Roles Anywhere
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User
Guide_.

## Considerations for IAM Roles Anywhere VPC

endpoints

Before you set up an interface VPC endpoint for IAM Roles Anywhere, ensure that you review
[Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

IAM Roles Anywhere supports making calls to all of its API actions from your VPC.

###### Note

VPC endpoint policies are supported for IAM Roles Anywhere on all API methods except `CreateSession`.

Full access to IAM Roles Anywhere is allowed through the endpoint by default, including `CreateSession`. For more information, see [Controlling access to services with
VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

## Creating an interface VPC endpoint for

IAM Roles Anywhere

You can create a VPC endpoint for the IAM Roles Anywhere service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

Create a VPC endpoint for IAM Roles Anywhere using the following service name:

- com.amazonaws.`region`.rolesanywhere

If you enable private DNS for the endpoint, you can make API requests to IAM Roles Anywhere using its
default DNS name for the Region, for example,
`rolesanywhere.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

IAM Roles Anywhere

You can attach an endpoint policy to your VPC endpoint that controls access to
IAM Roles Anywhere. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for IAM Roles Anywhere actions

The following is an example of an endpoint policy for IAM Roles Anywhere. When attached
to an endpoint, this policy grants access to the listed IAM Roles Anywhere actions for
all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`rolesanywhere`:`CreateTrustAnchor`",
            "`rolesanywhere`:`CreateProfile`",
            "`rolesanywhere`:`UpdateProfile`"
         ],
         "Resource":"*"
      }
   ]
}
```
