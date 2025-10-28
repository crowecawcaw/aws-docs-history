On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Amazon Lookout for Equipment and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Lookout for Equipment by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that you can use
to privately access Lookout for Equipment APIs without an internet gateway, network address translation
(NAT) device, VPN connection, or Amazon Web Services Direct Connect connection. Instances in your VPC don't
need public IP addresses to communicate with Lookout for Equipment APIs. Traffic between your VPC and Lookout for Equipment
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (Amazon Web Services PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Lookout for Equipment VPC

endpoints

Before you set up an interface VPC endpoint for Lookout for Equipment, ensure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Lookout for Equipment supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for

Lookout for Equipment

You can create a VPC endpoint for the Lookout for Equipment service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Lookout for Equipment using the following service name:

- com.amazonaws.`region`.lookoutequipment

If you enable private DNS for the endpoint, you can make API requests to Lookout for Equipment using its
default DNS name for the Region, for example,
`lookoutequipment.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

Lookout for Equipment

You can attach an endpoint policy to your VPC endpoint that controls access to
Lookout for Equipment. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Lookout for Equipment actions

The following is an example of an endpoint policy for Lookout for Equipment. When attached
to an endpoint, this policy grants access to the listed Lookout for Equipment actions for
all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`lookoutequipment`:`ListDatasets`",
            "`lookoutequipment`:`CreateDataset`",
            "`lookoutequipment`:`DescribeDataset`",
            "`lookoutequipment`:`DeleteDataset`",
            "`lookoutequipment`:`StartDataIngestionJob`",
            "`lookoutequipment`:`DescribeDataIngestionJob`",
            "`lookoutequipment`:`ListDataIngestionJobs`",
            "`lookoutequipment`:`CreateModel`",
            "`lookoutequipment`:`DescribeModel`",
            "`lookoutequipment`:`ListModels`",
            "`lookoutequipment`:`DeleteModel`",
            "`lookoutequipment`:`CreateInferenceScheduler`",
            "`lookoutequipment`:`StartInferenceScheduler`",
            "`lookoutequipment`:`StopInferenceScheduler`",
            "`lookoutequipment`:`UpdateInferenceScheduler`",
            "`lookoutequipment`:`DescribeInferenceScheduler`",
            "`lookoutequipment`:`ListInferenceSchedulers`",
            "`lookoutequipment`:`DeleteInferenceScheduler`",
            "`lookoutequipment`:`ListInferenceExecutions`"
         ],
         "Resource":"*"
      }
   ]
}
```
