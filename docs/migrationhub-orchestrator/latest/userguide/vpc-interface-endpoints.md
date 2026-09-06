

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Migration Hub Orchestrator and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and Migration Hub Orchestrator by creating an *interface VPC endpoint*. Interface endpoints are powered by AWS PrivateLink. With AWS PrivateLink, you can privately access Migration Hub Orchestrator API operations without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Migration Hub Orchestrator API operations. Traffic between your VPC and Migration Hub Orchestrator stays within the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for Migration Hub Orchestrator VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Migration Hub Orchestrator, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) and [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html) in the *Amazon VPC User Guide*. 

Migration Hub Orchestrator supports making calls to all of its API actions from your VPC. To use all of Migration Hub Orchestrator, you must create a VPC endpoint.

## Creating an interface VPC endpoint for Migration Hub Orchestrator
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for Migration Hub Orchestrator using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for Migration Hub Orchestrator using the following service name: 
+ `com.amazonaws.{{region}}.migrationhub-orchestrator` 

If you use private DNS for the endpoint, you can make API requests to Migration Hub Orchestrator using its default DNS name for the Region. For example, you can use the name `migrationhub-orchestrator.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for Migration Hub Orchestrator
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint. The VPC endpoint policy controls access to Migration Hub Orchestrator. The policy specifies the following information:
+ The principal that can perform actions
+ The actions that can be performed
+ The resources on which these actions can be performed

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Migration Hub Orchestrator actions**  
The following is an example of an endpoint policy for Migration Hub Orchestrator. When attached to an endpoint, this policy grants access to the listed Migration Hub Orchestrator actions for all principals on all resources.

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