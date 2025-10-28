# AWS Lake Formation and interface VPC endpoints

(AWS PrivateLink)

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such the IP address
range, subnets, route tables, and network gateways.

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and Lake Formation. You use this connection so that Lake Formation can communicate with
the resources in your VPC without going through the public internet.

You can establish a private connection between your VPC and AWS Lake Formation by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you to
privately access Lake Formation APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection. Instances in your VPC don't need public IP addresses to communicate with Lake Formation APIs.
Traffic between your VPC and Lake Formation does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Lake Formation VPC endpoints

Before you set up an interface VPC endpoint for Lake Formation, ensure that you review [Interface endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Lake Formation supports making calls to all of its API actions from your VPC. You can use Lake Formation with
VPC endpoints in all AWS Regions that support both Lake Formation and Amazon VPC endpoints.

## Creating an interface VPC endpoint for

Lake Formation

You can create a VPC endpoint for the Lake Formation service using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Lake Formation using the following service name:

- com.amazonaws.`region`.lakeformation

If you enable private DNS for the endpoint, you can make API requests to Lake Formation using its
default DNS name for the Region, for example,
`lakeformation.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for Lake Formation

Lake Formation supports VPC endpoint policies. An endpoint policy is a resource-based policy that you attach to a VPC endpoint
to control which AWS principals can use the endpoint to access an AWS service.

You can attach an endpoint policy to your VPC endpoint that controls access to Lake Formation. The
policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling
access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

**Example: VPC endpoint policy for Lake Formation actions**

The following example VPC endpoint policy for Lake Formation allows for credential vending using Lake Formation
permissions. You might use this policy to run queries using Lake Formation permissions from an Amazon Redshift
cluster or an Amazon EMR cluster located in a private subnet.

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lakeformation:GetDataAccess",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

###### Note

If you don't attach a policy when you create an endpoint, a default policy that allows
full access to the service is attached.

For more information, see these topics in the Amazon VPC documentation:

- [What Is
  Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md")
- [Create an Interface Endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint")
- [Use VPC endpoint
  policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-policies")
