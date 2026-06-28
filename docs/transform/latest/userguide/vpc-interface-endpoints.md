# AWS Transform and interface endpoints (AWS PrivateLink)

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

For AWS Transform custom PrivateLink documentation, see [AWS Transform custom and interface endpoints (AWS PrivateLink)](vpc-interface-endpoints-transform-custom.md "vpc-interface-endpoints-transform-custom.md").

## Considerations for AWS Transform VPC endpoints

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

AWS Transform supports the following VPC endpoint services:

| Service name    | Endpoint                                  | Note                                                                                                                                                                                                                                  |
| --------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Control plane   | `com.amazonaws.`region`.transform`        |                                                                                                                                                                                                                                       |
| Agentic API     | `com.amazonaws.`region`.transform-agents` |                                                                                                                                                                                                                                       |
| Web application | `com.amazonaws.`region`.api.transform`    | Required for the AWS Transform web application. This endpoint *_must_<br>• have private DNS enabled (the<br>*Enable DNS name<br>• option) so that<br>`api.transform.`region`.on.aws` resolves to<br>a private IP address in your VPC. |

Replace `region` with the AWS Region where your AWS Transform
profile is installed, for example,
_com.amazonaws.us-east-1.transform_.

###### Note

If you use the AWS Transform web application, the
`api.transform` endpoint is required. For the full setup
guide, see [Accessing the AWS Transform web application from a VPC](vpc-webapp-access.md "vpc-webapp-access.md").

For more information, see [Supported Regions for AWS Transform](regions.md "regions.md") and [Accessing a
service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Using an on-premises computer to connect to a AWS Transform endpoint

This section describes the process of using an on-premises computer to connect to
AWS Transform through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN
   connection between your on-premises device and your VPC.](../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md "../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md")
2. [Create an interface VPC endpoint for
   AWS Transform.](#vpc-endpoint-create "#vpc-endpoint-create")
3. [Set up an inbound Amazon Route 53 endpoint.](../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md") This will enable you to use
   the DNS name of your AWS Transform endpoint from your on-premises device.
