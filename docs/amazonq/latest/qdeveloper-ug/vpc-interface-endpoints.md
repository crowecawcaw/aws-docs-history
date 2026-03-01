# Amazon Q Developer and interface endpoints (AWS PrivateLink)

###### Note

Amazon Q Developer supports interface endpoints for features available [in
your IDE](q-in-IDE.md "q-in-IDE.md"). Chatting with Amazon Q [on AWS apps and
websites](q-on-aws.md "q-on-aws.md") is not supported for VPC endpoints. Neither is the Amazon Q Developer transformation web experience.

You can establish a private connection between your VPC and Amazon Q Developer by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access Amazon Q APIs without an internet gateway, NAT device, VPN connection, or
AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to
communicate with Amazon Q APIs. Traffic between your VPC and Amazon Q does not leave the Amazon
network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for Amazon Q VPC endpoints

Before you set up an interface VPC endpoint for Amazon Q, ensure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

Amazon Q supports making calls to all of its API actions from your VPC, in the context
of services that are configured to work with Amazon Q.

## Prerequisites

Before you begin any of the procedures below, ensure that you have the
following:

- An AWS account with appropriate permissions to create and configure
  resources.
- A VPC already created in your AWS account.
- Familiarity with AWS services, especially Amazon VPC and Amazon Q.

## Creating an interface VPC endpoint for Amazon Q

You can create a VPC endpoint for the Amazon Q service using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface
endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create the following VPC endpoints for Amazon Q using the following service names:

- com.amazonaws.`region`.q
- com.amazonaws.us-east-1.codewhisperer

Replace `region` with AWS Region where your Amazon Q Developer profile is
installed. For more information, see [Supported Regions for the Q Developer console and Q Developer profile](q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions "q-admin-setup-subscribe-regions.md#qdev-console-and-profile-regions").

###### Note

The Amazon CodeWhisperer endpoint (com.amazonaws.us-east-1.codewhisperer) is only supported in
the US East (N. Virginia) Region.

If you enable private DNS for the endpoint, you can make API requests to Amazon Q using its
default DNS name for the Region, for example, `q.us-east-1.amazonaws.com`.

For more information, see [Accessing a
service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Using an on-premises computer to connect to a Amazon Q endpoint

This section describes the process of using an on-premises computer to connect to
Amazon Q through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN
   connection between your on-premises device and your VPC.](../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md "../../../vpn/latest/clientvpn-user/client-vpn-user-what-is.md")
2. [Create an interface VPC endpoint for
   Amazon Q.](#vpc-endpoint-create "#vpc-endpoint-create")
3. [Set up an inbound Amazon Route 53 endpoint.](../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md "../../../Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.md") This will enable you to use
   the DNS name of your Amazon Q endpoint from your on-premises device.

## Using an in-console coding environment to connect to a Amazon Q endpoint

This section describes the process of using an in-console coding environment to
connect to a Amazon Q endpoint.

In this context, an in-console IDE is an IDE that you access inside the AWS console,
and authenticate to with IAM. Examples include SageMaker AI Studio and AWS Glue
Studio.

1. [Create an interface VPC endpoint for
   Amazon Q.](#vpc-endpoint-create "#vpc-endpoint-create")
2. Set up Amazon Q with the in-console coding environment
   - [SageMaker AI Studio](sagemaker-setup.md "sagemaker-setup.md")
   - [AWS Glue Studio](glue-setup.md "glue-setup.md")

3. Configure the coding environment to use the Amazon Q endpoint.
   - [SageMaker AI Studio](../../../sagemaker/latest/dg/host-vpc.md "../../../sagemaker/latest/dg/host-vpc.md")
   - [AWS Glue Studio](../../../glue/latest/dg/start-connecting.md "../../../glue/latest/dg/start-connecting.md")

## Connecting to Amazon Q through AWS PrivateLink from a third-Party IDE on an Amazon EC2 instance

This section will walk you through the process of installing a third-party Integrated
Development Environment (IDE) like Visual Studio Code or JetBrains on an Amazon EC2 instance,
and configuring it to connect to Amazon Q using AWS PrivateLink.

1. [Create an interface VPC endpoint for
   Amazon Q.](#vpc-endpoint-create "#vpc-endpoint-create")
2. Launch an Amazon EC2 instance in your desired subnet within your VPC. You can
   choose an Amazon Machine Image (AMI) that is compatible with your third-party
   IDE. For example, you can select an Amazon Linux 2 AMI.
3. Connect to the Amazon EC2 instance.
4. Install and Configure the IDE (Visual Studio Code or JetBrains).
5. [Install the Amazon Q extension or
   plugin.](q-in-IDE-setup.md "q-in-IDE-setup.md")
6. Configure the IDE to connect via AWS PrivateLink.
   - [Network
     connections in Visual Studio Code](https://code.visualstudio.com/docs/setup/network "https://code.visualstudio.com/docs/setup/network")
   - [JetBrains
     remote development](https://www.jetbrains.com/help/idea/remote.html "https://www.jetbrains.com/help/idea/remote.html")
