

# Using Amazon Polly with interface VPC endpoints
<a name="using-polly-with-vpc-endpoints"></a>

 If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and Amazon Polly. You can use this connection to synthesize speech with Amazon Polly without traversing the public internet. 

 Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define. With a VPC, you have control over your network settings, such the IP address range, subnets, route tables, and network gateways. To connect your VPC to Amazon Polly, you define an *interface VPC endpoint* for Amazon Polly. This type of endpoint enables you to connect your VPC to AWS services. The endpoint provides reliable, scalable connectivity to Amazon Polly without requiring an internet gateway, network address translation (NAT) instance, or VPN connection. For more information, see the [What is Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon VPC User Guide*. 

 Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services using an elastic network interface with private IP addresses. For more information, see [ New - AWS PrivateLink for AWS services](https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/). 

 The following steps are for users of Amazon VPC. For more information, see [ Getting Started](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon VPC User Guide*. 

## Availability
<a name="Availability"></a>

 VPC endpoints are supported in all the [ Regions where Amazon Polly is supported](https://docs.aws.amazon.com/general/latest/gr/pol.html). For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/). 

FIPS endpoints are available in the following regions:
+ US East (N. Virginia) (us-east-1)
+ US East (Ohio) (us-east-2)
+ US West (N. California) (us-west-1)
+ US West (Oregon) (us-west-2)
+ AWS GovCloud (US-West) (us-gov-west-1)
+ Canada (Central) (ca-central-1)

The FIPS endpoints are of the form `com.amazonaws.{{REGION}}.polly-fips`.

## Creating a VPC endpoint for Amazon Polly
<a name="creating-a-vpc-endpoint"></a>

 To start using Amazon Polly with your VPC, create an interface VPC endpoint for Amazon Polly. The service to choose is **com.amazonaws.{{Region}}.polly.** You don't need to change any settings for Amazon Polly. For more information, see [ Creating an Interface Endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint.html) in the *Amazon VPC User Guide.* 

## Testing the connection between your VPC and Amazon Polly
<a name="testing-vpc-and-polly-connection"></a>

 After you create the endpoint, you can test the connection. 

 **To test the connection between your VPC and your Amazon Polly endpoint** 

1.  Connect to an Amazon EC2 instance that resides in your VPC. For information about connecting, see [ Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) or [ Connecting to your Windows instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html) in the Amazon EC2 documentation. 

1.  From the instance, use `aws polly describe-voices` from the AWS CLI to list available Amazon Polly voices. 

 If the response to the command includes the list of available Amazon Polly voices, the command has succeeded, and your VPC endpoint is working. 

## Controlling access to your Amazon Polly endpoint
<a name="controlling-access-to-vpc-endpoint"></a>

 A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you create or modify the endpoint. If you don't attach a policy when you create an endpoint, we attach a default policy for you that allows full access to the service. An endpoint policy doesn't override or replace IAM user policies or service-specific policies. It's a separate policy for controlling access from the endpoint to the specified service. 

Endpoint policies must be written in JSON format.

 For more information, see [ Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

 The following is an example of an endpoint policy for Amazon Polly. This policy enables users connecting to Amazon Polly through the VPC to describe voices and synthesize speech with Amazon Polly, and prevents them from performing other Amazon Polly actions. 

```
{
  "Statement": [
    {
      "Sid": "SynthesisAndDescribeVoicesOnly",
      "Principal": "*",
      "Action": [
        "polly:DescribeVoices",
        "polly:SynthesizeSpeech"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

 **To modify the VPC endpoint policy for Amazon Polly** 

1.  Open the Amazon VPC console at [https://console.aws.amazon.com/vpc](https://console.aws.amazon.com/vpc/). 

1.  In the navigation pane, choose **Endpoints**. 

1. If you have not already created the endpoint for Amazon Polly, choose **Create endpoint**. Then select **com.amazonaws.{{Region}}.polly** and choose **Create endpoint**. 

1.  Select the **com.amazonaws.{{Region}}.polly** endpoint, and choose the **Policy** tab in the lower half of the screen. 

1.  Choose **Edit Policy** and make the changes to the policy. 

## Support for VPC context keys
<a name="support-for-vpc-context-keys"></a>

 Amazon Polly supports the `aws:SourceVpc` and `aws:SourceVpce` context keys that can limit access to specific VPCs or specific VPC endpoints. These keys work only when the user is using VPC endpoints. For more information, see [ Keys Available for Some Services](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-service-available) in the *IAM user Guide*. 