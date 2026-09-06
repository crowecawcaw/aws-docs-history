

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# Amazon Lookout for Equipment and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and Amazon Lookout for Equipment by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that you can use to privately access Lookout for Equipment APIs without an internet gateway, network address translation (NAT) device, VPN connection, or Amazon Web Services Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Lookout for Equipment APIs. Traffic between your VPC and Lookout for Equipment does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (Amazon Web Services PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for Lookout for Equipment VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Lookout for Equipment, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

Lookout for Equipment supports making calls to all of its API actions from your VPC. 

## Creating an interface VPC endpoint for Lookout for Equipment
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the Lookout for Equipment service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for Lookout for Equipment using the following service name: 
+ com.amazonaws.{{region}}.lookoutequipment 

If you enable private DNS for the endpoint, you can make API requests to Lookout for Equipment using its default DNS name for the Region, for example, `lookoutequipment.us-east-1.amazonaws.com`. 

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for Lookout for Equipment
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Lookout for Equipment. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for Lookout for Equipment actions**  
The following is an example of an endpoint policy for Lookout for Equipment. When attached to an endpoint, this policy grants access to the listed Lookout for Equipment actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "{{lookoutequipment}}:{{ListDatasets}}",
            "{{lookoutequipment}}:{{CreateDataset}}",
            "{{lookoutequipment}}:{{DescribeDataset}}",
            "{{lookoutequipment}}:{{DeleteDataset}}",            
            "{{lookoutequipment}}:{{StartDataIngestionJob}}",
            "{{lookoutequipment}}:{{DescribeDataIngestionJob}}",
            "{{lookoutequipment}}:{{ListDataIngestionJobs}}",
            "{{lookoutequipment}}:{{CreateModel}}",
            "{{lookoutequipment}}:{{DescribeModel}}",
            "{{lookoutequipment}}:{{ListModels}}",            
            "{{lookoutequipment}}:{{DeleteModel}}",
            "{{lookoutequipment}}:{{CreateInferenceScheduler}}",
            "{{lookoutequipment}}:{{StartInferenceScheduler}}",
            "{{lookoutequipment}}:{{StopInferenceScheduler}}",
            "{{lookoutequipment}}:{{UpdateInferenceScheduler}}",
            "{{lookoutequipment}}:{{DescribeInferenceScheduler}}",            
            "{{lookoutequipment}}:{{ListInferenceSchedulers}}",
            "{{lookoutequipment}}:{{DeleteInferenceScheduler}}",
            "{{lookoutequipment}}:{{ListInferenceExecutions}}"
         ],
         "Resource":"*"
      }
   ]
}
```