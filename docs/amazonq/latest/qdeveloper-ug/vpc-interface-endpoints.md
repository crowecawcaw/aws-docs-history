

# Amazon Q Developer and interface endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

**Note**  
Amazon Q Developer supports interface endpoints for features available [in your IDE](q-in-IDE.md). Chatting with Amazon Q [on AWS apps and websites](q-on-aws.md) is not supported for VPC endpoints. Neither is the Amazon Q Developer transformation web experience.

You can establish a private connection between your VPC and Amazon Q Developer by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access Amazon Q APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Amazon Q APIs. Traffic between your VPC and Amazon Q does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

## Considerations for Amazon Q VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Amazon Q, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

Amazon Q supports making calls to all of its API actions from your VPC, in the context of services that are configured to work with Amazon Q. 

## Prerequisites
<a name="qdev-endpoint-prereq"></a>

Before you begin any of the procedures below, ensure that you have the following:
+ An AWS account with appropriate permissions to create and configure resources.
+ A VPC already created in your AWS account.
+ Familiarity with AWS services, especially Amazon VPC and Amazon Q.

## Creating an interface VPC endpoint for Amazon Q
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the Amazon Q service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create the following VPC endpoints for Amazon Q using the following service names: 
+ com.amazonaws.{{region}}.q 
+ com.amazonaws.us-east-1.codewhisperer

Replace {{region}} with AWS Region where your Amazon Q Developer profile is installed. For more information, see [Supported Regions for the Q Developer console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions).

**Note**  
The Amazon CodeWhisperer endpoint (com.amazonaws.us-east-1.codewhisperer) is only supported in the US East (N. Virginia) Region.

If you enable private DNS for the endpoint, you can make API requests to Amazon Q using its default DNS name for the Region, for example, `q.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Using an on-premises computer to connect to a Amazon Q endpoint
<a name="qdev-endpoint-on-prem"></a>

This section describes the process of using an on-premises computer to connect to Amazon Q through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN connection between your on-premises device and your VPC.](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html)

1. [Create an interface VPC endpoint for Amazon Q.](#vpc-endpoint-create)

1. [Set up an inbound Amazon Route 53 endpoint.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) This will enable you to use the DNS name of your Amazon Q endpoint from your on-premises device.

## Using an in-console coding environment to connect to a Amazon Q endpoint
<a name="qdev-endpoint-console"></a>

This section describes the process of using an in-console coding environment to connect to a Amazon Q endpoint.

In this context, an in-console IDE is an IDE that you access inside the AWS console, and authenticate to with IAM. Examples include SageMaker AI Studio and AWS Glue Studio.

1. [Create an interface VPC endpoint for Amazon Q.](#vpc-endpoint-create)

1. Set up Amazon Q with the in-console coding environment
   + [SageMaker AI Studio](sagemaker-setup.md)
   + [AWS Glue Studio](glue-setup.md)

1. Configure the coding environment to use the Amazon Q endpoint.
   + [SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html)
   + [AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/start-connecting.html)

## Connecting to Amazon Q through AWS PrivateLink from a third-Party IDE on an Amazon EC2 instance
<a name="qdev-endpoint-ec2"></a>

This section will walk you through the process of installing a third-party Integrated Development Environment (IDE) like Visual Studio Code or JetBrains on an Amazon EC2 instance, and configuring it to connect to Amazon Q using AWS PrivateLink.

1. [Create an interface VPC endpoint for Amazon Q.](#vpc-endpoint-create)

1. Launch an Amazon EC2 instance in your desired subnet within your VPC. You can choose an Amazon Machine Image (AMI) that is compatible with your third-party IDE. For example, you can select an Amazon Linux 2 AMI.

1. Connect to the Amazon EC2 instance.

1. Install and Configure the IDE (Visual Studio Code or JetBrains).

1. [Install the Amazon Q extension or plugin.](q-in-IDE-setup.md)

1. Configure the IDE to connect via AWS PrivateLink.
   + [Network connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network)
   + [JetBrains remote development](https://www.jetbrains.com/help/idea/remote.html)