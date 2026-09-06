

# AWS CodeConnections and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and AWS CodeConnections by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access AWS CodeConnections APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with AWS CodeConnections APIs, because traffic between your VPC and AWS CodeConnections does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for AWS CodeConnections VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for AWS CodeConnections, ensure that you review [Interface endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-interface-endpoints.html#vpc-endpoints-actions) in the *Amazon VPC User Guide*. 

AWS CodeConnections supports making calls to all of its API actions from your VPC. 

VPC endpoints are supported in all AWS CodeConnections Regions.

## VPC endpoint concepts
<a name="vpc-endpoint-concepts"></a>

The following are the key concepts for VPC endpoints:

VPC endpoint  
The entry point in your VPC that enables you to connect privately to a service. The following are the different types of VPC endpoints. You create the type of VPC endpoint required by the supported service.  
+ [VPC endpoints for AWS CodeConnections actions](https://docs.aws.amazon.com/dtconsole/latest/userguide/vpc-interface-endpoints.html#vpc-endpoints-actions)
+ [VPC endpoints for AWS CodeConnections webhooks](https://docs.aws.amazon.com/dtconsole/latest/userguide/vpc-interface-endpoints.html#vpc-endpoints-webhooks)

AWS PrivateLink  
A technology that provides private connectivity between VPCs and services.

## VPC endpoints for AWS CodeConnections actions
<a name="vpc-endpoints-actions"></a>

You can manage VPC endpoints for the AWS CodeConnections service.

### Creating interface VPC endpoints for AWS CodeConnections actions
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the AWS CodeConnections service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

To start using connections with your VPC, create an interface VPC endpoint for AWS CodeConnections. When you create a VPC endpoint for AWS CodeConnections, choose **AWS Services**, and in **Service Name**, choose: 
+ **com.amazonaws.{{region}}.codestar-connections.api**: This option creates a VPC endpoint for AWS CodeConnections API operations. For example, choose this option if your users use the AWS CLI, the AWS CodeConnections API, or the AWS SDKs to interact with AWS CodeConnections for operations such as `CreateConnection`, `ListConnections`, and `CreateHost`.

For the **Enable DNS name** option, if you select private DNS for the endpoint, you can make API requests to AWS CodeConnections using its default DNS name for the Region, for example, `codestar-connections.us-east-1.amazonaws.com`. 

**Important**  
Private DNS is enabled by default for endpoints created for AWS services and AWS Marketplace Partner services.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

### Creating a VPC endpoint policy for AWS CodeConnections actions
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to AWS CodeConnections. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Note**  
The com.amazonaws.{{region}}.codestar-connections.webhooks endpoint does not support policies.

**Example: VPC endpoint policy for AWS CodeConnections actions**  
The following is an example of an endpoint policy for AWS CodeConnections. When attached to an endpoint, this policy grants access to the listed AWS CodeConnections actions for all principals on all resources.

```
{
  "Statement": [
    {
      "Sid": "GetConnectionOnly",
      "Principal": "*",
      "Action": [
        "codestar-connections:GetConnection"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

## VPC endpoints for AWS CodeConnections webhooks
<a name="vpc-endpoints-webhooks"></a>

AWS CodeConnections creates webhook endpoints for you when you create or delete a host with VPC configuration. The endpoint name is **com.amazonaws.{{region}}.codestar-connections.webhooks**.

With the VPC endpoint for GitHub webhooks, hosts can send event data via webhooks to your integrated AWS services over the Amazon network.

**Important**  
When you set up your host for GitHub Enterprise Server, AWS CodeConnections creates a VPC endpoint for webhooks event data for you. If you created your host before November 24, 2020, and you want to use VPC PrivateLink webhook endpoints, you must first [delete](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-delete.html) your host and then [create](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-create.html) a new host.

AWS CodeConnections manages the lifecycle of these endpoints. To delete the endpoint, you must delete the corresponding host resource.

### How webhook endpoints for AWS CodeConnections hosts are used
<a name="vpc-webhook-endpoints"></a>

The webhook endpoint is where webhooks from third-party repositories are sent for AWS CodeConnections processing. A webhook describes a customer action. When you perform a `git push`, the webhook endpoint receives a webhook from the provider detailing the push. For example, AWS CodeConnections can notify CodePipeline to start your pipeline.

For cloud providers, such as Bitbucket, or GitHub Enterprise Server hosts that do not use a VPC, the webhook VPC endpoint does not apply because the providers are sending webhooks to AWS CodeConnections where the Amazon network is not used.