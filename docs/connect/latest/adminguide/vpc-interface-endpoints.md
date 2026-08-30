# Amazon Connect Customer and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and a subset of endpoints in
Connect Customer by creating an interface VPC endpoint. Following are the supported
endpoints:

- Amazon AppIntegrations
- Customer Profiles
- Outbound campaigns
- Voice ID
- agent assist
- Connect Customer Service
  Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that you can use to privately access Connect Customer APIs
  without an internet gateway, NAT device, VPN connection, or Direct Connect connection.
  Instances in your VPC don't need public IP addresses to communicate with the Connect Customer APIs
  that integrate with AWS PrivateLink.

For more information, see the [AWS PrivateLink Guide](../../../vpc/latest/privatelink.md "../../../vpc/latest/privatelink.md").

## Creating an interface VPC endpoint for Connect Customer

You can create an interface endpoint using either the Amazon VPC console or the
AWS Command Line Interface (AWS CLI). For more information, see [Create an interface
endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink Guide_.

Connect Customer supports the following service names:

- com.amazonaws.`region`.app-integrations
- com.amazonaws.`region`.cases
- com.amazonaws.`region`.profile
- com.amazonaws.`region`.connect-campaigns
- com.amazonaws.`region`.voiceid
- com.amazonaws.`region`.wisdom (This is for
  agent assist.)
- com.amazonaws.`region`.connect
- com.amazonaws.`region`.connect-fips (This is for creating an endpoint for Connect Customer Service that complies with the Federal Information Processing Standard (FIPS).)

If you enable private DNS for an interface endpoint, you can make API requests to
Connect Customer using the default DNS name for the Region. For example,
voiceid.us-east-1.amazonaws.com. For more information, see [DNS hostnames](../../../vpc/latest/privatelink/privatelink-access-aws-services.md#interface-endpoint-dns-hostnames "../../../vpc/latest/privatelink/privatelink-access-aws-services.md#interface-endpoint-dns-hostnames") in the
_AWS PrivateLink Guide_.

## Creating a VPC endpoint policy

You can attach an endpoint policy to your VPC endpoint that controls access. The
policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control access to
services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

### Example: VPC endpoint policy

The following VPC endpoint policy grants access to the listed Connect Customer Voice ID
actions for all principals on all resources.

```
{
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
                "voiceid:CreateDomain",
                "voiceid:EvaluateSession",
                "voiceid:ListSpeakers"
            ],
            "Resource":"*",
            "Principal":"*"
        }
    ]
}
```

Following is another example. In this one, the VPC endpoint policy grants access
to the listed outbound campaigns actions for all principals on all resources.

```
{
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
                 "connect-campaigns:CreateCampaign",
                "connect-campaigns:DeleteCampaign",
                "connect-campaigns:ListCampaigns"
            ],
            "Resource":"*",
            "Principal":"*"
        }
    ]
}
```
