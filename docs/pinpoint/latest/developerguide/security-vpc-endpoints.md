**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Creating an interface VPC endpoint for Amazon Pinpoint

You can establish a private connection between your virtual private cloud (VPC) and an
endpoint in Amazon Pinpoint by creating an interface VPC endpoint.

Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"), a technology that allows you to privately access Amazon Pinpoint APIs without an
internet gateway, NAT device, VPN connection, or AWS Direct Connect. Instances in your VPC don't need
public IP addresses to communicate with the Amazon Pinpoint APIs that integrate with AWS PrivateLink.

For more information, see the [AWS PrivateLink Guide](../../../vpc/latest/privatelink/what-is-privatelink.md "../../../vpc/latest/privatelink/what-is-privatelink.md").

## Creating an interface VPC endpoints

You can create an interface endpoint using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the AWS PrivateLink Guide.

Amazon Pinpoint supports the following service names:

- `com.amazonaws.`region`.pinpoint`
- `com.amazonaws.`region`.pinpoint-sms-voice-v2`

If you turn on private DNS for an interface endpoint, you can make API requests to Amazon Pinpoint
using the default DNS name for the AWS Region, for example,
`com.amazonaws.`us-east-1`.pinpoint`. For more
information, see [DNS hostnames](../../../vpc/latest/privatelink/privatelink-access-aws-services.md#interface-endpoint-dns-hostnames "../../../vpc/latest/privatelink/privatelink-access-aws-services.md#interface-endpoint-dns-hostnames") in the _AWS PrivateLink
Guide_.

For a list of all the Regions and endpoints where Amazon Pinpoint is
currently available, see [AWS
service endpoints](../../../general/latest/gr/pinpoint.md "../../../general/latest/gr/pinpoint.md") in the _Amazon Web Services General Reference_.

## Creating a VPC endpoint policy

You can attach an endpoint policy to your VPC endpoint that controls access. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

## Example: VPC endpoint policy

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
