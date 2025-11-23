# AWS Transform and interface endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS Transform by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access the AWS Transform console without an internet gateway, NAT device, VPN connection, or
Direct Connect connection. Traffic between your VPC and AWS Transform does not leave the Amazon
network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

###### Note

- Only the AWS Transform console can be accessed thru AWS PrivateLink.
- The AWS Transform WebApp and other related services such as .NET IDE cannot be accessed thru AWS PrivateLink.

## Considerations for AWS Transform VPC

endpoints

Before you set up an interface VPC endpoint for AWS Transform, ensure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

## Prerequisites

Before you begin any of the procedures below, ensure that you have the
following:

- An AWS account with appropriate permissions to create and configure
  resources.
- A VPC already created in your AWS account.
- Familiarity with AWS services, especially Amazon VPC and AWS Transform.

## Creating an interface VPC endpoint for AWS Transform

You can create a VPC endpoint for the AWS Transform service using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface
endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create the following VPC endpoints for AWS Transform using this service name:

- com.amazonaws.`region`.transform

Replace `region` with AWS Region where your AWS Transform profile is
installed, for example, _com.amazonaws.us-east-1.transform_.

For more information, see [Supported Regions for AWS Transform](regions.md "regions.md") and [Accessing a
service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Using an on-premises computer to connect to a

AWS Transform endpoint

This section describes the process of using an on-premises computer to connect to
AWS Transform through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN
   connection between your on-premises device and your VPC.](../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md "../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md")
2. [Create an interface VPC endpoint for
   AWS Transform.](#vpc-endpoint-create "#vpc-endpoint-create")
3. [Set up an inbound Amazon Route 53 endpoint.](../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md") This will enable you to use
   the DNS name of your AWS Transform endpoint from your on-premises device.
