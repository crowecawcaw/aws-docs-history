

# AWS Transform and interface endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and AWS Transform by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access the AWS Transform console without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Traffic between your VPC and AWS Transform does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

**Note**  
For AWS Transform custom PrivateLink documentation, see [AWS Transform custom and interface endpoints (AWS PrivateLink)](vpc-interface-endpoints-transform-custom.md).

## Considerations for AWS Transform VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for AWS Transform, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

## Prerequisites
<a name="transform-endpoint-prereq"></a>

Before you begin any of the procedures below, ensure that you have the following:
+ An AWS account with appropriate permissions to create and configure resources.
+ A VPC already created in your AWS account.
+ Familiarity with AWS services, especially Amazon VPC and AWS Transform.

## Creating an interface VPC endpoint for AWS Transform
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the AWS Transform service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

AWS Transform supports the following VPC endpoint services:


| Service name | Endpoint | Note | 
| --- | --- | --- | 
| Control plane | com.amazonaws.{{region}}.transform |  | 
| Agentic API | com.amazonaws.{{region}}.transform-agents |  | 
| Web application | com.amazonaws.{{region}}.api.transform | Required for the AWS Transform web application. This endpoint must have private DNS enabled (the Enable DNS name option) so that api.transform.{{region}}.on.aws resolves to a private IP address in your VPC. | 

Replace {{region}} with the AWS Region where your AWS Transform profile is installed, for example, *com.amazonaws.us-east-1.transform*.

**Note**  
If you use the AWS Transform web application, the `api.transform` endpoint is required. For the full setup guide, see [Accessing the AWS Transform web application from a VPC](vpc-webapp-access.md).

For more information, see [Supported Regions for AWS Transform](regions.md) and [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Using an on-premises computer to connect to a AWS Transform endpoint
<a name="transform-endpoint-on-prem"></a>

This section describes the process of using an on-premises computer to connect to AWS Transform through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN connection between your on-premises device and your VPC.](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html)

1. [Create an interface VPC endpoint for AWS Transform.](#vpc-endpoint-create)

1. [Set up an inbound Amazon Route 53 endpoint.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) This will enable you to use the DNS name of your AWS Transform endpoint from your on-premises device.