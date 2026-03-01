# AWS Audit Manager and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and AWS Audit Manager by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you to
privately access Audit Manager APIs without an internet gateway, NAT device, VPN connection, or AWS
Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate
with Audit Manager APIs. Traffic between your VPC and AWS Audit Manager does not leave the AWS network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for AWS Audit Manager VPC endpoints

Before you set up an interface VPC endpoint for AWS Audit Manager, ensure that you review [Interface endpoint
properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

AWS Audit Manager supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for AWS Audit Manager

You can create a VPC endpoint for the AWS Audit Manager service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for AWS Audit Manager using the following service name:

- `com.amazonaws.`region`.auditmanager`

If you enable private DNS for the endpoint, you can make API requests to AWS Audit Manager using
its default DNS name for the Region, for example,
`auditmanager.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for AWS Audit Manager

You can attach an endpoint policy to your VPC endpoint that controls access to AWS Audit Manager.
The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling
access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

###### Example: VPC endpoint policy for AWS Audit Manager actions

The following is an example of an endpoint policy for AWS Audit Manager. When attached to an
endpoint, this policy grants access to the listed Audit Manager actions for all principals on
all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`auditmanager`:`GetAssessment`",
            "`auditmanager`:`GetServicesInScope`",
            "`auditmanager`:`ListNotifications`"
         ],
         "Resource":"*"
      }
   ]
}
```
