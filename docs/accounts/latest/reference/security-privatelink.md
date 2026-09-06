

# AWS PrivateLink for AWS Account Management
<a name="security-privatelink"></a>

The following information is relevant for all AWS accounts.

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can access the AWS Account Management service from within the VPC without having to cross the public internet. 

Amazon VPC lets you launch AWS resources in a custom virtual network. You can use a VPC to control your network settings, such as the IP address range, subnets, route tables, and network gateways. For more information about VPCs, see the *[Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/)*.

To connect your Amazon VPC to Account Management, you must first define an *interface VPC endpoint*, which lets you connect your VPC to other AWS services. The endpoint provides reliable, scalable connectivity, without requiring an internet gateway, network address translation (NAT) instance, or VPN connection. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*.

## Creating the Endpoint
<a name="vpc-endpoint-create"></a>

You can create an AWS Account Management endpoint in your VPC using the AWS Management Console, the AWS Command Line Interface (AWS CLI), an AWS SDK, the AWS Account Management API, or CloudFormation.

For information about creating and configuring an endpoint using the Amazon VPC console or the AWS CLI, see [Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/create-endpoint-service.html) in the *Amazon VPC User Guide.*

**Note**  
When you create an endpoint, specify Account Management as the service that you want your VPC to connect to, using the following format:  

```
com.amazonaws.us-east-1.account
```
You must use the string exactly as shown, specifying the `us-east-1` Region. As a global service, Account Management is hosted in only that one AWS Region.

For information about creating and configuring an endpoint using CloudFormation, see the [AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html) resource in the *CloudFormation User Guide*.

## Amazon VPC Endpoint Policies
<a name="vpc-endpoint-policy"></a>

You can control what actions can be performed through this service endpoint by attaching an endpoint policy when you create the Amazon VPC endpoint. You can create complex IAM rules by attaching multiple endpoint policies. For more information, see:
+  [Amazon Virtual Private Cloud endpoint policies for Account Management](vpc-iam.md) 
+  [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*. 