# DevOps Guru and interface VPC endpoints

(AWS PrivateLink)

You can use VPC endpoints when you call Amazon DevOps Guru APIs. When you use VPC endpoints, your
API calls are more secure because they are contained within your VPC and do not access the
internet. For more information, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the
_Amazon DevOps Guru API Reference_.

You establish a private connection between your VPC and DevOps Guru by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access DevOps Guru APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with DevOps Guru APIs. Traffic between your VPC and DevOps Guru does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for DevOps Guru VPC

endpoints

Before you set up an interface VPC endpoint for DevOps Guru, ensure that you
review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

DevOps Guru supports making calls to
all of its API actions from your VPC.

## Creating an interface VPC endpoint for

DevOps Guru

You can create a VPC endpoint for the DevOps Guru service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for DevOps Guru using the following service name:

- com.amazonaws.`region`.devops-guru

If you enable private DNS for the endpoint, you can make API requests to DevOps Guru using
its default DNS name for the Region, for example,
`devops-guru.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

DevOps Guru

You can attach an endpoint policy to your VPC endpoint that controls access to
DevOps Guru. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for DevOps Guru actions

The following is an example of an endpoint policy for DevOps Guru. When attached
to an endpoint, this policy grants access to the listed DevOps Guru actions for
all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`devops-guru`:`AddNotificationChannel`",
            "`devops-guru`:`ListInsights`",
            "`devops-guru`:`ListRecommendations`"
         ],
         "Resource":"*"
      }
   ]
}
```
