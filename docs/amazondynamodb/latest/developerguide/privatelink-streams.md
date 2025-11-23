# AWS PrivateLink for DynamoDB Streams

With AWS PrivateLink for Amazon DynamoDB Streams, you can provision interface Amazon VPC endpoints
(interface endpoints) in your virtual private cloud (Amazon VPC). These endpoints are directly
accessible from applications that are on premises over VPN and Direct Connect, or in a
different AWS Region over Amazon VPC peering. Using AWS PrivateLink and interface endpoints, you
can simplify private network connectivity from your applications to DynamoDB Streams.

Applications in your Amazon VPC do not need public IP addresses to communicate with DynamoDB Streams using
Amazon VPC interface endpoints for DynamoDB Streams operations. Interface endpoints are represented by one or
more elastic network interfaces (ENIs) that are assigned private IP addresses from subnets in
your Amazon VPC. Requests to DynamoDB Streams over interface endpoints stay on the Amazon network. You can also
access interface endpoints in your Amazon VPC from on-premises applications through Direct Connect or
AWS Virtual Private Network (AWS VPN). For more information about how to connect your AWS Virtual Private Network with your
on-premises network, see the [_Direct Connect User Guide_](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") and the [_AWS Site-to-Site VPN User Guide_](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md").

For general information about interface endpoints, see [Interface Amazon VPC endpoints](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") (AWS PrivateLink).

###### Note

Only interface endpoints are supported for DynamoDB Streams. Gateway endpoints are not supported.

###### Topics

- [Considerations when using
  AWS PrivateLink for Amazon DynamoDB Streams](#privatelink-streams-considerations "#privatelink-streams-considerations")
- [Creating an Amazon VPC endpoint](#privatelink-streams-vpc-endpoint "#privatelink-streams-vpc-endpoint")
- [Accessing Amazon DynamoDB Streams interface endpoints](#privatelink-streams-accessing-ddb-interface-endpoints "#privatelink-streams-accessing-ddb-interface-endpoints")
- [Accessing DynamoDB Streams API operations from DynamoDB Streams interface endpoints](#privatelink-streams-accessing-api-operations-from-interface-endpoints "#privatelink-streams-accessing-api-operations-from-interface-endpoints")
- [AWS SDK examples](#privatelink-streams-aws-sdk-examples "#privatelink-streams-aws-sdk-examples")
- [Creating an Amazon VPC endpoint policy for
  DynamoDB Streams](#privatelink-streams-creating-vpc-endpoint-policy "#privatelink-streams-creating-vpc-endpoint-policy")
- [Using DynamoDB endpoints with
  AWS Management Console Private Access](#ddb-streams-endpoints-private-access "#ddb-streams-endpoints-private-access")

## Considerations when using

AWS PrivateLink for Amazon DynamoDB Streams

Amazon VPC considerations apply to AWS PrivateLink for Amazon DynamoDB Streams. For more information, see
[interface endpoint
considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md").
The following restrictions apply.

AWS PrivateLink for Amazon DynamoDB Streams doesn't support the following:

- Transport Layer Security (TLS) 1.1
- Private and Hybrid Domain Name System (DNS) services

###### Note

Network connectivity timeouts to AWS PrivateLink endpoints are not within the scope of DynamoDB Streams
error responses and need to be appropriately handled by your applications connecting to
the AWS PrivateLink endpoints.

## Creating an Amazon VPC endpoint

To create an Amazon VPC interface endpoint, see [Create an Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink
Guide_.

## Accessing Amazon DynamoDB Streams interface endpoints

When you create an interface endpoint, DynamoDB generates two types of endpoint-specific,
DynamoDB Streams DNS names: _Regional_ and _Zonal_.

- A _Regional_ DNS name includes a unique Amazon VPC endpoint ID, a
  service identifier, the AWS Region, and `vpce.amazonaws.com` in its name.
  For example, for Amazon VPC endpoint ID
  `vpce-1a2b3c4d`, the DNS name generated might be
  similar to
  ``vpce-1a2b3c4d-5e6f`.streams.dynamodb.us-east-1.vpce.amazonaws.com`.
- A _Zonal_ DNS name includes the Availability Zone—for
  example, ``vpce-1a2b3c4d-5e6f`-**us-east-1a.**streams.dynamodb.us-east-1.vpce.amazonaws.com`. You
  might use this option if your architecture isolates Availability Zones. For example, you
  could use it for fault containment or to reduce Regional data transfer costs.

## Accessing DynamoDB Streams API operations from DynamoDB Streams interface endpoints

You can use the AWS CLI or AWS SDKs to access DynamoDB Streams API operations
through DynamoDB Streams interface endpoints.

### AWS CLI examples

To access DynamoDB Streams or API operations through DynamoDB Streams interface endpoints in AWS CLI commands,
use the `--region` and `--endpoint-url` parameters.

**Example: Create a VPC endpoint**

```
aws ec2 create-vpc-endpoint \
--region us-east-1 \
--service-name com.amazonaws.us-east-1.dynamodb-streams \
--vpc-id client-vpc-id \
--subnet-ids client-subnet-id \
--vpc-endpoint-type Interface \
--security-group-ids client-sg-id

```

**Example: Modify a VPC endpoint**

```
aws ec2 modify-vpc-endpoint \
--region us-east-1 \
--vpc-endpoint-id client-vpc-endpoint-id \
--policy-document policy-document \ #example optional parameter
--add-security-group-ids security-group-ids \ #example optional parameter
# any additional parameters needed, see Privatelink documentation for more details
```

**Example: List streams using an endpoint URL**

In the following example, replace the Region `us-east-1` and the DNS name
of the VPC endpoint ID
`vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com` with your
own information.

```
aws dynamodbstreams --region us-east-1 —endpoint https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com list-streams
```

## AWS SDK examples

To access Amazon DynamoDB Streams API operations through DynamoDB Streams interface endpoints when using the
AWS SDKs, update your SDKs to the latest version. Then, configure your clients to use an
endpoint URL for DynamoDB Streams API operation through DynamoDB Streams interface endpoints.

SDK for Python (Boto3)

###### Example: Use an endpoint URL to access a DynamoDB stream

In the following example, replace the Region `us-east-1` and VPC
endpoint ID
`https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com` with
your own information.

```
ddb_streams_client = session.client(
service_name='dynamodbstreams',
region_name='us-east-1',
endpoint_url='https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com'
)
```

SDK for Java 1.x

###### Example: Use an endpoint URL to access a DynamoDB stream

In the following example, replace the Region `us-east-1` and VPC
endpoint ID
`https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com` with
your own information.

```
//client build with endpoint config
final AmazonDynamoDBStreams dynamodbstreams = AmazonDynamoDBStreamsClientBuilder.standard().withEndpointConfiguration(
        new AwsClientBuilder.EndpointConfiguration(
                "https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com",
                Regions.DEFAULT_REGION.getName()
        )
).build();
```

SDK for Java 2.x

###### Example: Use an endpoint URL to access DynamoDB stream

In the following example, replace the Region `us-east-1` and VPC
endpoint ID
`https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com` with
your own information.

```
Region region = Region.US_EAST_1;
dynamoDbStreamsClient = DynamoDbStreamsClient.builder().region(region)
.endpointOverride(URI.create("https://vpce-1a2b3c4d-5e6f.streams.dynamodb.us-east-1.vpce.amazonaws.com"))
.build()

```

## Creating an Amazon VPC endpoint policy for

DynamoDB Streams

You can attach an endpoint policy to your Amazon VPC endpoint that controls access to DynamoDB Streams.
The policy specifies the following information:

- The AWS Identity and Access Management (IAM) principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

###### Topics

- [Example:
  Restricting access to a specific stream from an Amazon VPC endpoint](#privatelink-streams-example-restrict-access-to-bucket "#privatelink-streams-example-restrict-access-to-bucket")

### Example:

Restricting access to a specific stream from an Amazon VPC endpoint

You can create an endpoint policy that restricts access to only specific DynamoDB Streams.
This type of policy is useful if you have other AWS services in your Amazon VPC that use
DynamoDB Streams. The following stream policy restricts access to only the
stream `2025-02-20T11:22:33.444` attached to
`DOC-EXAMPLE-TABLE`. To use this endpoint policy,
replace `DOC-EXAMPLE-TABLE` with the name of your
table and `2025-02-20T11:22:33.444` with the stream label.

JSON

```
`{
"Version":"2012-10-17",
 "Id": "Policy1216114807515",
 "Statement": [
 { "Sid": "Access-to-specific-stream-only",
 "Principal": "*",
 "Action": [
 "dynamodb:DescribeStream",
 "dynamodb:GetRecords"
 ],
 "Effect": "Allow",
 "Resource": ["arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`table-name`/stream/`2025-02-20T11:22:33.444`"]
 }
 ]
}`

```

###### Note

Gateway endpoints aren't supported in DynamoDB Streams.

## Using DynamoDB endpoints with

AWS Management Console Private Access

You must set up DNS configuration for DynamoDB and DynamoDB Streams when using VPC endpoints with the
[DynamoDB console](https://console.aws.amazon.com/dynamodb "https://console.aws.amazon.com/dynamodb") in [AWS Management Console Private
Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md").

To configure DynamoDB to be accessible in AWS Management Console Private Access, you must create the
following two VPC endpoints:

- `com.amazonaws.<region>.dynamodb`
- `com.amazonaws.<region>.dynamodb-streams`

When you create the VPC endpoints, navitage to the Route53 console and create a private
hosted zone for DynamoDB using the regional endpoint
`dynamodb.us-east-1.amazonaws.com`.

Create the following two alias records in the private hosted zone:

- `dynamodb.<region>.amazonaws.com` that routes traffic to the VPC
  endpoint `com.amazonaws.<region>.dynamodb`.
- `streams.dynamodb.<region>.amazonaws.com` that routes traffic to the
  VPC endpoint `com.amazonaws.<region>.dynamodb-streams`.
