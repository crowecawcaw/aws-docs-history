# Amazon Comprehend and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Comprehend by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access Amazon Comprehend APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with Amazon Comprehend APIs. Traffic between your VPC and Amazon Comprehend
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Amazon Comprehend VPC

endpoints

Before you set up an interface VPC endpoint for Amazon Comprehend, ensure that you review
[Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Amazon Comprehend endpoints are not available in all availability zones in a region. When you create the endpoint, use the
following command to list the availability zones.

```
aws ec2 describe-vpc-endpoint-services \
  --service-names com.amazonaws.us-west-2.comprehend
```

Amazon Comprehend supports making calls to all of its API actions from your VPC.

## Creating an interface VPC endpoint for

Amazon Comprehend

You can create a VPC endpoint for the Amazon Comprehend service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Amazon Comprehend using the following service name:

- com.amazonaws.`region`.comprehend

If you enable private DNS for the endpoint, you can make API requests to Amazon Comprehend using
its default DNS name for the Region, for example, `*comprehend.us-east-1.amazonaws.com*`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

Amazon Comprehend

You can attach an endpoint policy to your VPC endpoint that controls access to
Amazon Comprehend. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for Amazon Comprehend actions

The following is an example of an endpoint policy for Amazon Comprehend. When attached
to an endpoint, this policy grants access to the Amazon Comprehend
`DetectEntities` action for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "`comprehend`:`DetectEntities`"
         ],
         "Resource":"*"
      }
   ]
}
```
