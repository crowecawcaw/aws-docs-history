# AWS PrivateLink for DynamoDB

With AWS PrivateLink for DynamoDB, you can provision *interface Amazon VPC
endpoints* (interface endpoints) in your virtual private cloud (Amazon VPC). These
endpoints are directly accessible from applications that are on premises over VPN and Direct Connect,
or in a different AWS Region over [Amazon VPC peering](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md"). Using AWS PrivateLink
and interface endpoints, you can simplify private network connectivity from your applications to
DynamoDB.

Applications in your VPC do not need public IP addresses to communicate
with DynamoDB using VPC interface endpoints for DynamoDB operations. Interface endpoints are
represented by one or more elastic network interfaces (ENIs) that are assigned private IP
addresses from subnets in your Amazon VPC. Requests to DynamoDB over interface endpoints stay on the
Amazon network. You can also access interface endpoints in your Amazon VPC from on-premises
applications through AWS Direct Connect or AWS Virtual Private Network (Site-to-Site VPN). For more information about how to
connect your Amazon VPC with your on-premises network, see the [Direct Connect User Guide](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") and the [AWS Site-to-Site VPN User Guide](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md").

For general information about interface endpoints, see [Interface Amazon VPC endpoints
(AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in the _AWS PrivateLink Guide_. AWS PrivateLink is also
supported for Amazon DynamoDB Streams endpoints. For more information, see [AWS PrivateLink for DynamoDB Streams](privatelink-streams.md "privatelink-streams.md").

###### Topics

- [Types of Amazon VPC endpoints for Amazon DynamoDB](#types-of-vpc-endpoints-for-ddb "#types-of-vpc-endpoints-for-ddb")
- [Considerations when using AWS PrivateLink for Amazon DynamoDB](#privatelink-considerations "#privatelink-considerations")
- [Creating an Amazon VPC endpoint](#ddb-creating-vpc "#ddb-creating-vpc")
- [Accessing Amazon DynamoDB interface endpoints](#accessing-ddb-interface-endpoints "#accessing-ddb-interface-endpoints")
- [Accessing DynamoDB tables and control API operations from DynamoDB interface endpoints](#accessing-tables-apis-from-interface-endpoints "#accessing-tables-apis-from-interface-endpoints")
- [Updating an on-premises DNS configuration](#updating-on-premises-dns-config "#updating-on-premises-dns-config")
- [Creating an Amazon VPC endpoint policy for DynamoDB](#creating-vpc-endpoint-policy "#creating-vpc-endpoint-policy")
- [Using DynamoDB endpoints with AWS Management Console Private Access](#ddb-endpoints-private-access "#ddb-endpoints-private-access")
- [AWS PrivateLink for DynamoDB Streams](privatelink-streams.md "privatelink-streams.md")
- [Using AWS PrivateLink for DynamoDB Accelerator (DAX)](dax-private-link.md "dax-private-link.md")

## Types of Amazon VPC endpoints for Amazon DynamoDB

You can use two types of Amazon VPC endpoints to access Amazon DynamoDB: _gateway
endpoints_ and _interface endpoints_ (by using AWS PrivateLink).
A _gateway endpoint_ is a gateway that you specify in your
route table to access DynamoDB from your Amazon VPC over the AWS network. _Interface endpoints_ extend the functionality of gateway endpoints by using
private IP addresses to route requests to DynamoDB from within your Amazon VPC, on premises, or from
an Amazon VPC in another AWS Region by using Amazon VPC peering or AWS Transit Gateway. For
more information, see [What is Amazon VPC peering?](../../../vpc/latest/peering/what-is-vpc-peering.md "../../../vpc/latest/peering/what-is-vpc-peering.md") and [Transit Gateway vs Amazon VPC peering](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway-vs-vpc-peering.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/transit-gateway-vs-vpc-peering.md").

Interface endpoints are compatible with gateway endpoints. If you have an existing gateway
endpoint in the Amazon VPC, you can use both types of endpoints in the same Amazon VPC.

| Gateway endpoints for DynamoDB                                  | Interface endpoints for DynamoDB                                                                                     |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| In both cases, your network traffic remains on the AWS network. |
| Use Amazon DynamoDB public IP addresses                         | Use private IP addresses from your Amazon VPC to access Amazon DynamoDB                                              |
| Do not allow access from on premises                            | Allow access from on premises                                                                                        |
| Do not allow access from another AWS Region                     | Allow access from an Amazon VPC endpoint in another AWS Region by using Amazon VPC<br>peering or AWS Transit Gateway |
| Not billed                                                      | Billed                                                                                                               |

For more information about gateway endpoints, see [Gateway Amazon VPC endpoints](../../../vpc/latest/privatelink/vpce-gateway.md "../../../vpc/latest/privatelink/vpce-gateway.md") in the
_AWS PrivateLink Guide_.

## Considerations when using AWS PrivateLink for Amazon DynamoDB

Amazon VPC considerations apply to AWS PrivateLink for Amazon DynamoDB. For more information, see
[Interface
endpoint considerations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md") in the
_AWS PrivateLink Guide_. In addition, the following restrictions
apply.

AWS PrivateLink for Amazon DynamoDB does not support the following:

- Transport Layer Security (TLS) 1.1
- Private and Hybrid Domain Name System (DNS) services

You can submit up to 50,000 requests per second for each AWS PrivateLink endpoint that you
enable.

###### Note

Network connectivity timeouts to AWS PrivateLink endpoints are not within the scope of
DynamoDB error responses and need to be appropriately handled by your applications connecting
to the PrivateLink endpoints.

## Creating an Amazon VPC endpoint

To create an Amazon VPC interface endpoint, see [Create an Amazon VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink
Guide_.

## Accessing Amazon DynamoDB interface endpoints

When you create an interface endpoint, DynamoDB generates two types of endpoint-specific,
DynamoDB DNS names: _Regional_ and _Zonal_.

- A _Regional_ DNS name includes a unique Amazon VPC endpoint ID, a
  service identifier, the AWS Region, and `vpce.amazonaws.com` in its name. For
  example, for Amazon VPC endpoint ID `vpce-1a2b3c4d`, the
  DNS name generated might be similar to
  ``vpce-1a2b3c4d-5e6f`.dynamodb.us-east-1.vpce.amazonaws.com`.
- A _Zonal_ DNS name includes the Availability Zone—for
  example, ``vpce-1a2b3c4d-5e6f`-**us-east-1a.**dynamodb.us-east-1.vpce.amazonaws.com`. You might use
  this option if your architecture isolates Availability Zones. For example, you could use
  it for fault containment or to reduce Regional data transfer costs.

###### Note

To achieve optimal reliability, we recommend deploying your service across a minimum of three availability zones.

## Accessing DynamoDB tables and control API operations from DynamoDB interface endpoints

You can use the AWS CLI or AWS SDKs to access DynamoDB tables and control API operations
through DynamoDB interface endpoints.

### AWS CLI examples

To access DynamoDB tables or DynamoDB control API operations through DynamoDB
interface endpoints in AWS CLI commands, use the `--region` and
`--endpoint-url` parameters.

**Example: Create a VPC endpoint**

```
aws ec2 create-vpc-endpoint \
--region us-east-1 \
--service-name com.amazonaws.us-east-1.dynamodb \
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

**Example: List tables using an endpoint URL**

In the following example, replace the Region `us-east-1` and the DNS name of
the VPC endpoint ID `vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com`
with your own information.

```
aws dynamodb --region us-east-1 --endpoint https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com list-tables
```

### AWS SDK examples

To access DynamoDB tables or DynamoDB control API operations through DynamoDB interface endpoints
when using the AWS SDKs, update your SDKs to the latest version. Then, configure your
clients to use an endpoint URL for accessing a table or DynamoDB control API operation through
DynamoDB interface endpoints.

SDK for Python (Boto3)

###### Example: Use an endpoint URL to access a DynamoDB table

In the following example, replace the Region `us-east-1` and VPC
endpoint ID
`https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com` with
your own information.

```
ddb_client = session.client(
service_name='dynamodb',
region_name='us-east-1',
endpoint_url='https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com'
)
```

SDK for Java 1.x

###### Example: Use an endpoint URL to access a DynamoDB table

In the following example, replace the Region `us-east-1` and VPC
endpoint ID
`https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com` with
your own information.

```
//client build with endpoint config
final AmazonDynamoDB dynamodb = AmazonDynamoDBClientBuilder.standard().withEndpointConfiguration(
        new AwsClientBuilder.EndpointConfiguration(
                "https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com",
                Regions.DEFAULT_REGION.getName()
        )
).build();
```

SDK for Java 2.x

###### Example: Use an endpoint URL to access DynamoDB table

In the following example, replace the Region us-east-1 and VPC endpoint ID
https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com with your own
information.

```
Region region = Region.US_EAST_1;
dynamoDbClient = DynamoDbClient.builder().region(region)
.endpointOverride(URI.create("https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.amazonaws.com"))
.build()

```

## Updating an on-premises DNS configuration

When using endpoint-specific DNS names to access the interface endpoints for DynamoDB, you
don’t have to update your on-premises DNS resolver. You can resolve the endpoint-specific DNS
name with the private IP address of the interface endpoint from the public DynamoDB DNS domain.

### Using interface endpoints to access DynamoDB without a gateway endpoint or an internet gateway in the Amazon VPC

Interface endpoints in your Amazon VPC can route both in-Amazon VPC applications and on-premises
applications to DynamoDB over the Amazon network, as illustrated in the following
diagram.

![Data flow diagram showing access from on-premises and in-Amazon VPC apps to DynamoDB; by using an interface endpoint and AWS PrivateLink.](images/PrivateLink-interfaceEndpoints.png)

The diagram illustrates the following:

- Your on-premises network uses Direct Connect or Site-to-Site VPN to connect to Amazon VPC A.
- Your applications on-premises and in Amazon VPC A use endpoint-specific DNS names to
  access DynamoDB through the DynamoDB interface endpoint.
- On-premises applications send data to the interface endpoint in the Amazon VPC through
  Direct Connect (or Site-to-Site VPN). AWS PrivateLink moves the data from the interface endpoint to DynamoDB
  over the AWS network.
- In-Amazon VPC applications also send traffic to the interface endpoint. AWS PrivateLink
  moves the data from the interface endpoint to DynamoDB over the AWS network.

### Using gateway endpoints and interface endpoints together in the same Amazon VPC to access DynamoDB

You can create interface endpoints and retain the existing gateway endpoint in the same
Amazon VPC, as the following diagram shows. By taking this approach, you allow in-Amazon VPC
applications to continue accessing DynamoDB through the gateway endpoint, which is not billed.
Then, only your on-premises applications would use interface endpoints to access DynamoDB. To
access DynamoDB this way, you must update your on-premises applications to use
endpoint-specific DNS names for DynamoDB.

![Data-flow diagram showing access to DynamoDB by using gateway endpoints and interface endpoints together.](images/PL-Image2-InterfaceAndGatewayEP.png)

The diagram illustrates the following:

- On-premises applications use endpoint-specific DNS names to send data to the
  interface endpoint within the Amazon VPC through Direct Connect (or Site-to-Site VPN). AWS PrivateLink moves the
  data from the interface endpoint to DynamoDB over the AWS network.
- Using default Regional DynamoDB names, in-Amazon VPC applications send data to the gateway
  endpoint that connects to DynamoDB over the AWS network.

For more information about gateway endpoints, see [Gateway Amazon VPC endpoints](../../../vpc/latest/privatelink/vpce-gateway.md "../../../vpc/latest/privatelink/vpce-gateway.md") in the
_Amazon VPC User Guide_.

## Creating an Amazon VPC endpoint policy for DynamoDB

You can attach an endpoint policy to your Amazon VPC endpoint that controls access to DynamoDB.
The policy specifies the following information:

- The AWS Identity and Access Management (IAM) principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

###### Topics

- [Example: Restricting access to a specific table from an Amazon VPC endpoint](#privatelink-example-restrict-access-to-bucket "#privatelink-example-restrict-access-to-bucket")

### Example: Restricting access to a specific table from an Amazon VPC endpoint

You can create an endpoint policy that restricts access to only specific DynamoDB tables.
This type of policy is useful if you have other AWS services in your Amazon VPC that use
tables. The following table policy restricts access to only the
`DOC-EXAMPLE-TABLE`. To use this endpoint policy,
replace `DOC-EXAMPLE-TABLE` with the name of your
table.

JSON

```
`{
"Version":"2012-10-17",
 "Id": "Policy1216114807515",
 "Statement": [
 { "Sid": "Access-to-specific-table-only",
 "Principal": "*",
 "Action": [
 "dynamodb:GetItem",
 "dynamodb:PutItem"
 ],
 "Effect": "Allow",
 "Resource": ["arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`DOC-EXAMPLE-TABLE`",
 "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`DOC-EXAMPLE-TABLE`/*"]
 }
 ]
}`

```

## Using DynamoDB endpoints with AWS Management Console Private Access

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
- `streams.dynamodb.<region>.amazonaws.com` that routes traffic to the VPC
  endpoint `com.amazonaws.<region>.dynamodb-streams`.
