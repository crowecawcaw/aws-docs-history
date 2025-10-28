AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Migration Hub Orchestrator and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Migration Hub Orchestrator by creating an
_interface VPC endpoint_. Interface endpoints are powered by
AWS PrivateLink. With AWS PrivateLink, you can privately access Migration Hub Orchestrator API operations
without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances
in your VPC don't need public IP addresses to communicate with Migration Hub Orchestrator API operations.
Traffic between your VPC and Migration Hub Orchestrator stays within the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Migration Hub Orchestrator VPC

endpoints

Before you set up an interface VPC endpoint for Migration Hub Orchestrator, ensure that you review
[Interface endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md") in the _Amazon VPC User Guide_.

Migration Hub Orchestrator supports making calls to all of its API actions from your VPC. To use all of
Migration Hub Orchestrator, you must create a VPC endpoint.

## Creating an interface VPC endpoint for

Migration Hub Orchestrator

You can create a VPC endpoint for Migration Hub Orchestrator using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Migration Hub Orchestrator using the following service name:

- `com.amazonaws.`region`.migrationhub-orchestrator`

If you use private DNS for the endpoint, you can make API requests to Migration Hub Orchestrator using
its default DNS name for the Region. For example, you can use the name
`migrationhub-orchestrator.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

Migration Hub Orchestrator

You can attach an endpoint policy to your VPC endpoint. The VPC endpoint policy
controls access to Migration Hub Orchestrator. The policy specifies the following information:

- The principal that can perform actions
- The actions that can be performed
- The resources on which these actions can be performed

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Migration Hub Orchestrator actions

The following is an example of an endpoint policy for Migration Hub Orchestrator. When attached to
an endpoint, this policy grants access to the listed Migration Hub Orchestrator actions for all
principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "migrationhub-orchestrator:ListMigrationWorkflowTemplates",
         ],
         "Resource":"*"
      }
   ]
}
```
