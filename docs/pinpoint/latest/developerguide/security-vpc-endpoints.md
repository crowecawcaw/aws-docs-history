

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Creating an interface VPC endpoint for Amazon Pinpoint
<a name="security-vpc-endpoints"></a>

You can establish a private connection between your virtual private cloud (VPC) and an endpoint in Amazon Pinpoint by creating an interface VPC endpoint. 

Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/), a technology that allows you to privately access Amazon Pinpoint APIs without an internet gateway, NAT device, VPN connection, or Direct Connect. Instances in your VPC don't need public IP addresses to communicate with the Amazon Pinpoint APIs that integrate with AWS PrivateLink.

For more information, see the [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html). 

## Creating an interface VPC endpoints
<a name="security-vpc-endpoints-create"></a>

You can create an interface endpoint using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint ](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the AWS PrivateLink Guide.

Amazon Pinpoint supports the following service names:
+ `com.amazonaws.{{region}}.pinpoint`
+ `com.amazonaws.{{region}}.pinpoint-sms-voice-v2`

If you turn on private DNS for an interface endpoint, you can make API requests to Amazon Pinpoint using the default DNS name for the AWS Region, for example, `com.amazonaws.{{us-east-1}}.pinpoint`. For more information, see [DNS hostnames](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html#interface-endpoint-dns-hostnames) in the *AWS PrivateLink Guide*.

For a list of all the Regions and endpoints where Amazon Pinpoint is currently available, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/pinpoint.html) in the *Amazon Web Services General Reference*.

## Creating a VPC endpoint policy
<a name="security-vpc-endpoints-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

## Example: VPC endpoint policy
<a name="security-vpc-endpoints-policy-example"></a>

The following VPC endpoint policy grants access to the listed Amazon Pinpoint actions for all principals on all resources. 

```
{
"Statement": [
    {
      "Principal": "*",
      "Action": [
        "mobiletargeting:CreateCampaign",
        "mobiletargeting:CreateApp",
        "mobiletargeting:DeleteApp",
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```