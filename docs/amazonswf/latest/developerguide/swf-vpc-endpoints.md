

# Amazon VPC endpoints for Amazon SWF
<a name="swf-vpc-endpoints"></a>

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a connection between your Amazon VPC and Amazon Simple Workflow Service workflows. You can use this connection with your Amazon SWF workflows without crossing the public internet. 

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to control your network settings, such as the IP address range, subnets, route tables, and network gateways. For more information about VPCs, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/).

To connect your Amazon VPC to Amazon SWF you must first define an *interface VPC endpoint*, which lets you connect your VPC to other AWS services. The endpoint provides reliable, scalable connectivity, without requiring an internet gateway, network address translation (NAT) instance, or VPN connection. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*.

## Creating the Endpoint
<a name="swf-vpc-endpoint-create"></a>

You can create an Amazon SWF endpoint in your VPC using the AWS Management Console, the AWS Command Line Interface (AWS CLI), an AWS SDK, the Amazon SWF API, or CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or the AWS CLI, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide.*

**Note**  
 When you create an endpoint, specify Amazon SWF as the service that you want your VPC to connect to. In the Amazon VPC console, service names vary based on the AWS Region. For example, in the US East (N. Virginia) Region, the service name for Amazon SWF is **com.amazonaws.us-east-1.swf**.

For information about creating and configuring an endpoint using CloudFormation, see the [AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html) resource in the *CloudFormation User Guide*.

## Amazon VPC Endpoint Policies
<a name="swf-vpc-endpoint-policy"></a>

To control connectivity access to Amazon SWF you can attach an AWS Identity and Access Management (IAM) endpoint policy while creating an Amazon VPC endpoint. You can create complex IAM rules by attaching multiple endpoint policies. For more information, see:
+  [Amazon Virtual Private Cloud Endpoint Policies for Amazon SWF](swf-vpc-iam.md) 
+  [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) 