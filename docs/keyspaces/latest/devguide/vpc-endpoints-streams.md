# Using Amazon Keyspaces CDC streams with interface VPC endpoints

Interface VPC endpoints enable private communication between your virtual private cloud
(VPC) running in Amazon VPC and Amazon Keyspaces. Interface VPC endpoints are powered by AWS PrivateLink,
which is an AWS service that enables private communication between VPCs and AWS
services.

AWS PrivateLink enables this by using an elastic network interface with private IP addresses
in your VPC so that network traffic does not leave the Amazon network. Interface VPC
endpoints don't require an internet gateway, NAT device, VPN connection, or Direct Connect
connection. For more information, see [Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") and
[Interface VPC endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md").

###### Topics

- [Using interface VPC endpoints for
  Amazon Keyspaces CDC streams](#using-interface-vpc-endpoints-streams "#using-interface-vpc-endpoints-streams")
- [Amazon Keyspaces CDC streams interface VPC endpoints](#interface-vpc-endpoints-streams-types "#interface-vpc-endpoints-streams-types")
- [Create Amazon Keyspaces CDC streams interface VPC endpoint](#create-interface-vpc-endpoints-streams "#create-interface-vpc-endpoints-streams")
- [Update an Amazon Keyspaces CDC streams interface VPC endpoint](#update-interface-vpc-endpoints-streams "#update-interface-vpc-endpoints-streams")
- [List streams using an Amazon Keyspaces CDC streams interface VPC endpoint](#list-interface-vpc-endpoints-streams "#list-interface-vpc-endpoints-streams")
- [Create a policy for an Amazon Keyspaces CDC streams interface VPC endpoint](#interface-vpc-endpoints-streams-policy "#interface-vpc-endpoints-streams-policy")

## Using interface VPC endpoints for

Amazon Keyspaces CDC streams

You can use an interface VPC endpoint so that traffic between Amazon Keyspaces CDC streams and your Amazon VPC
resources starts flowing through the interface VPC endpoint. You can use VPC endpoint policies
to restrict access to your CDC streams.

For more information about Amazon Keyspaces CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](cdc.md "cdc.md").

## Amazon Keyspaces CDC streams interface VPC endpoints

When you create an interface endpoint, Amazon Keyspaces CDC streams generates two types of endpoint-specific
DNS name for the stream: _Regional_ and _Zonal_.

**Regional**
The Regional DNS name includes the following information:

- a unique Amazon VPC endpoint ID
- a service identifier
- the AWS Region
- the `vpce.amazonaws.com` suffix

For an Amazon VPC endpoint with the ID `vpce-1a2b3c4d`, the generated DNS name
might be look similar to the following example: `vpce-1a2b3c4d-5e6f.cassandra-streams.us-east-1.vpce.amazonaws.com`.

**Zonal**
The Zonal DNS name includes the [Availability
Zone](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") in addition to the information in the Regional DNS name.
The generated DNS name for the Amazon VPC endpoint with the ID `vpce-1a2b3c4d` would look like in the following example,
note that the AWS Region now includes the Availability Zone:
`vpce-1a2b3c4d-5e6f-us-east-1a.cassandra-streams.us-east-1.vpce.amazonaws.com`

You can use this option if your architecture isolates Availability Zones. For example, you could use it for fault
containment or to reduce Regional data transfer costs.

###### Note

To achieve optimal reliability, we recommend deploying your service across a minimum of three Availability Zones.

## Create Amazon Keyspaces CDC streams interface VPC endpoint

You can use the AWS CLI or the AWS SDK to access Amazon Keyspaces CDC Streams API operations through Amazon Keyspaces CDC Streams interface endpoints.
For a complete listing of all available API operations, see [_Amazon Keyspaces Streams API Reference_](../StreamsAPIReference/Welcome.md "../StreamsAPIReference/Welcome.md").

For more information about how to create VPC endpoints, see [create an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the Amazon VPC User Guide.

To create a VPC endpoint, you can use the syntax in the following example.

```
aws ec2 create-vpc-endpoint \
  --region `us-east-1` \
  --service-name api.aws.`us-east-1`.cassandra-streams \
  --vpc-id `client-vpc-id` \
  --subnet-ids `client-subnet-id` \
  --vpc-endpoint-type Interface \
  --security-group-ids `client-sg-id`
```

## Update an Amazon Keyspaces CDC streams interface VPC endpoint

To update a VPC endpoint, you can use the syntax in the following example.

```
aws ec2 modify-vpc-endpoint \
  --region `us-east-1` \
  --vpc-endpoint-id `client-vpc-id` \
  --policy-document `policy-document` \ #example optional parameter
  --add-security-group-ids `security-group-ids` \ #example optional parameter
```

## List streams using an Amazon Keyspaces CDC streams interface VPC endpoint

To list the streams that are using a VPC endpoint, you can use the syntax in the following example. Make sure
to replace the Region and the DNS name of the VPC endpoint ID with your own information.

```
aws keyspacesstreams \
  --endpoint `https://vpce-1a2b3c4d-5e6f.cassandra-streams.us-east-1.vpce.amazonaws.com` \
  --region `us-east-1` \
  list-streams
```

## Create a policy for an Amazon Keyspaces CDC streams interface VPC endpoint

You can attach an endpoint policy to your Amazon VPC endpoint that controls access to Amazon Keyspaces CDC streams.
The policy specifies the following information:

- The AWS Identity and Access Management (IAM) principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

To restrict access to specific Amazon Keyspaces CDC streams to only allow specific AWS services in your Amazon VPC access, you can use the following
example.

The following stream policy grants access to any IAM principal for the actions `cassandra:GetStream`
and `cassandra:GetRecords` for the specified stream `2025-02-20T11:22:33.444` attached
to the resource `/keyspace/mykeyspace/table/mytable/` belonging to account `123456788901`.
To use this endpoint policy, make sure to replace the Region, account ID, and resource with stream label.

```
{
"Version": "2012-10-17",
  "Id": "Policy1216114807515",
  "Statement": [
    { "Sid": "Access-to-specific-stream-only",
      "Principal": "*",
      "Action": [
        "cassandra:GetStream",
        "cassandra:GetRecords"
      ],
      "Effect": "Allow",
      "Resource": ["arn:aws:cassandra:`us-east-1`:`111122223333`:`/keyspace/mykeyspace/table/mytable/stream/2025-02-20T11:22:33.444`"]
    }
  ]
}
```

###### Note

Amazon Keyspaces doesn't support Gateway endpoints for CDC streams.
