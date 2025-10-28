# Amazon Kendra Amazon Kendra Intelligent

Ranking and interface VPC endpoints (AWS PrivateLink)

You can establish a private connection between your VPC and Amazon Kendra by creating
an _interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that allows you
to privately access Amazon Kendra APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with Amazon Kendra APIs. Traffic between your VPC and Amazon Kendra
doesn't leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

## Considerations for Amazon Kendra and

Amazon Kendra Intelligent Ranking VPC endpoints

Before you set up an interface VPC endpoint for Amazon Kendra or Amazon Kendra
Intelligent Ranking, make sure that you review the [prerequisites](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_Amazon VPC User Guide_.

Amazon Kendra and Amazon Kendra Intelligent Ranking supports making calls to
all of its API actions from your VPC.

## Creating an interface VPC endpoint for

Amazon Kendra and Amazon Kendra Intelligent Ranking

You can create a VPC endpoint for the Amazon Kendra or Amazon Kendra Intelligent
Ranking service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI).

Create a VPC endpoint for Amazon Kendra using the following service name:

- com.amazonaws.`region`.kendra

Create a VPC endpoint for Amazon Kendra Intelligent Ranking using the following
service name:

- aws.api.`region`.kendra-ranking

After you create a VPC endpoint, you can use the following example AWS CLI command that
uses the `endpoint-url` parameter to specify an interface endpoint to the
Amazon Kendra API:

```
aws kendra list-indices --endpoint-url https://`VPC endpoint`
```

`VPC endpoint` is the DNS name generated when the
interface endpoint is created. This name includes the VPC endpoint ID, and the Amazon Kendra
service name, which includes the region. For example,
`vpce-1234-abcdef.kendra.us-west-2.vpce.amazonaws.com`.

If you activate private DNS for the endpoint, you can make API requests to
Amazon Kendra using its default DNS name for the region. For example,
`kendra.us-east-1.amazonaws.com`.

For more information, see [Creating an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

Amazon Kendra and Amazon Kendra Intelligent Ranking

You can attach an endpoint policy to your VPC endpoint that controls access to
Amazon Kendra or Amazon Kendra Intelligent Ranking.

The policy for Amazon Kendra or Amazon Kendra Intelligent Ranking specifies the
following information:

- The principal/authorized user that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

###### Example: VPC endpoint policy for Amazon Kendra actions

The following is an example of an endpoint policy for Amazon Kendra. When attached
to an endpoint, this policy grants access to all available Amazon Kendra actions for
all principals/authorized users on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "kendra:*"
         ],
         "Resource":"*"
      }
   ]
}
```

###### Example: VPC endpoint policy for Amazon Kendra Intelligent Ranking actions

The following is an example of an endpoint policy for Amazon Kendra Intelligent
Ranking. When attached to an endpoint, this policy grants access to all available
Amazon Kendra Intelligent Ranking actions for all principals/authorized users on
all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "kendra-ranking:*"
         ],
         "Resource":"*"
      }
   ]
}
```

For more information, see [Controlling access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.
