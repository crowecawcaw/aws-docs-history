

# Amazon VPC endpoints for Amazon Braket
<a name="braket-privatelink"></a>

You can establish a private connection between your VPC and Amazon Braket by creating an interface VPC endpoint. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/), a technology that enables access to Braket APIs without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with Braket APIs.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets.

With AWS PrivateLink, traffic between your VPC and Braket does not leave the Amazon network, which increases the security of data that you share with cloud-based applications, because it reduces your data's exposure to the public internet. For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the Amazon VPC User Guide.

**Topics**
+ [Considerations for Amazon Braket VPC endpoints](#braket-privatelink-considerations)
+ [Set up Braket and PrivateLink](#braket-set-up-privatelink)
+ [Additional information about creating an endpoint](#braket-more-about-endpoints)
+ [Control access with Amazon VPC endpoint policies](#braket-control-endpoint-access)

## Considerations for Amazon Braket VPC endpoints
<a name="braket-privatelink-considerations"></a>

Before you set up an interface VPC endpoint for Braket, ensure that you review [ Interface endpoint prerequisites](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#prerequisites-interface-endpoints) in the *Amazon VPC User Guide*.

Braket supports making calls to all of its [API actions](https://docs.aws.amazon.com/braket/latest/APIReference/API_Operations.html) from your VPC.

By default, full access to Braket is allowed through the VPC endpoint. You can control access if you specify VPC endpoint policies. For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

## Set up Braket and PrivateLink
<a name="braket-set-up-privatelink"></a>

To use AWS PrivateLink with Amazon Braket, you must create an Amazon Virtual Private Cloud (Amazon VPC) endpoint as an interface, and then connect to the endpoint through the Amazon Braket API service.

Here are the general steps of this process, which are explained in detail in later sections.
+ Configure and launch an Amazon VPC to host your AWS resources. If you already have a VPC, you can skip this step.
+ Create an Amazon VPC endpoint for Braket 
+ Connect and run Braket quantum tasks through your endpoint

### Step 1: Launch an Amazon VPC if needed
<a name="step-1-launch-an-amazon-vpc-if-needed"></a>

Remember that you can skip this step if your account already has a VPC in operation.

A VPC controls your network settings, such as the IP address range, subnets, route tables, and network gateways. Essentially, you are launching your AWS resources in a custom virtual network. For more information about VPCs, see the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

Open the [Amazon VPC console](https://aws.amazon.com/vpc/) and create a new VPC with subnets, security groups, and network gateways.

### Step 2: Create an interface VPC endpoint for Braket
<a name="step-2-create-an-interface-vpc-endpoint-for-braket"></a>

You can create a VPC endpoint for the Braket service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *Amazon VPC User Guide*.

To create a VPC endpoint in the console, open the [Amazon VPC console](https://aws.amazon.com/vpc/), open the **Endpoints** page, and proceed to create the new endpoint. Make note of the endpoint ID for later reference. It is required as part of the `—endpoint-url` flag when you are making certain calls to the Braket API.

Create the VPC endpoint for Braket using the following service name:
+  `com.amazonaws.substitute_your_region.braket` 

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.

### Step 3: Connect and run Braket quantum tasks through your endpoint
<a name="step-3-connect-and-run-braket-tasks-through-your-endpoint"></a>

After you have created a VPC endpoint, you can run CLI commands that include the `endpoint-url` parameter to specify interface endpoints to the API or runtime, such as the following example:

```
aws braket search-quantum-tasks --endpoint-url VPC_Endpoint_ID.braket.substituteYourRegionHere.vpce.amazonaws.com
```

If you enable private DNS hostnames for your VPC endpoint, you don't need to specify the endpoint as a URL in your CLI commands. Instead, the Amazon Braket API DNS hostname, which the CLI and Braket SDK use by default, resolves to your VPC endpoint. It has the form shown in the following example:

```
https://braket.substituteYourRegionHere.amazonaws.com
```

The blog post called [Direct access to Amazon SageMaker AI notebooks from Amazon VPC by using an AWS PrivateLink endpoint](https://aws.amazon.com/blogs/machine-learning/securing-all-amazon-sagemaker-api-calls-with-aws-privatelink/) provides an example of how to set up an endpoint to make secure connections to SageMaker notebooks, which are similar to Amazon Braket notebooks.

If you're following the steps in the blog post, remember to substitute the name ** Amazon Braket ** for ** Amazon SageMaker AI**. For **Service Name** enter `com.amazonaws.us-east-1.braket` or substitute your correct AWS Region name into that string, if your Region is not *us-east-1*.

## Additional information about creating an endpoint
<a name="braket-more-about-endpoints"></a>
+ For information about how to create a VPC with private subnets, see [Create a VPC with private subnets.](https://docs.aws.amazon.com/batch/latest/userguide/create-public-private-vpc.html) 
+ For information about creating and configuring an endpoint using the Amazon VPC console or the AWS CLI, see [Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *Amazon VPC User Guide*.
+ For information about creating and configuring an endpoint using CloudFormation, see the [AWS::EC2::VPCEndpoint](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html) resource in the *CloudFormation User Guide*.

## Control access with Amazon VPC endpoint policies
<a name="braket-control-endpoint-access"></a>

To control connectivity access to Amazon Braket, you can attach an AWS Identity and Access Management (IAM) endpoint policy to your Amazon VPC endpoint. The policy specifies the following information:
+ The principal (user or role) that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

 **Example: VPC endpoint policy for Braket actions** 

The following example shows an endpoint policy for Braket. When attached to an endpoint, this policy grants access to the listed Braket actions for all principals on all resources.

```
{
 "Statement":[
 {
   "Principal":"*",
   "Effect":"Allow",
   "Action":[
     “braket:action-1",
     “braket:action-2",
     “braket:action-3”
     ],
   "Resource":"*"
   }
  ]
}
```

You can create complex IAM rules by attaching multiple endpoint policies. For more information and examples, see:
+  [Amazon Virtual Private Cloud Endpoint Policies for Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/vpc-endpoints.html#vpc-iam) 
+  [Creating Granular IAM Permissions for Non-Admin Users](https://docs.aws.amazon.com/step-functions/latest/dg/concept-create-iam-advanced.html) 
+  [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) 