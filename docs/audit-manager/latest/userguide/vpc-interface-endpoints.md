

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# AWS Audit Manager and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and AWS Audit Manager by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access Audit Manager APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Audit Manager APIs. Traffic between your VPC and AWS Audit Manager does not leave the AWS network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for AWS Audit Manager VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for AWS Audit Manager, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

AWS Audit Manager supports making calls to all of its API actions from your VPC. 

## Creating an interface VPC endpoint for AWS Audit Manager
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the AWS Audit Manager service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for AWS Audit Manager using the following service name: 
+ `com.amazonaws.{{region}}.auditmanager` 

If you enable private DNS for the endpoint, you can make API requests to AWS Audit Manager using its default DNS name for the Region, for example, `auditmanager.us-east-1.amazonaws.com`. 

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for AWS Audit Manager
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to AWS Audit Manager. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for AWS Audit Manager actions**  
The following is an example of an endpoint policy for AWS Audit Manager. When attached to an endpoint, this policy grants access to the listed Audit Manager actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "{{auditmanager}}:{{GetAssessment}}",
            "{{auditmanager}}:{{GetServicesInScope}}",
            "{{auditmanager}}:{{ListNotifications}}"
         ],
         "Resource":"*"
      }
   ]
}
```