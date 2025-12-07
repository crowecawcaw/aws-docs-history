# VPC endpoints for S3 Vectors

To access S3 Vectors from your virtual private cloud (VPC), Amazon S3 supports interface VPC endpoints by using AWS PrivateLink (PrivateLink).
PrivateLink provides private connectivity between your VPC and
S3 Vectors without requiring an internet gateway or NAT device. Interface endpoints are represented by one ore more elastic network interfaces (ENIs)
that are assigned private IP addresses from subnets in your VPC.
Requests to S3 Vectors over interface endpoints stay on the AWS network.

You can also
access interface endpoints in your VPC from on-premises applications through AWS Direct Connect
or AWS Virtual Private Network (AWS VPN). For more information about how to connect your VPC with your on-premises network, see
the _[AWS Direct Connect User Guide](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")_ and the _[AWS Site-to-Site VPN
User Guide](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")_. For general information about interface endpoints,
see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the
_AWS PrivateLink Guide_.

## Benefits of using PrivateLink

with S3 Vectors

Using PrivateLink with S3 Vectors provides several security and operational
benefits:

- **Enhanced security**: Traffic between your VPC
  and S3 Vectors remains within the AWS network and doesn't traverse the
  internet.
- **Simplified network architecture**: Access
  S3 Vectors without configuring internet gateways, NAT devices, or VPN
  connections.
- **Granular access control**: Use VPC endpoint
  policies to control which vector buckets and vector indexes can be accessed
  through the endpoint.
- **Compliance support**: Meet regulatory
  requirements that mandate private network connectivity for sensitive
  data.

## VPC endpoint DNS names and

resolution

When you
create a VPC endpoint, S3 Vectors generates two types of endpoint-specific DNS names: Regional and Zonal.

The Regional and Zonal DNS names of interface VPC endpoints for S3 Vectors are as
follows:

- **Regional DNS name**:
  `vpce-`1a2b3c4d-5e6f`.s3vectors.`region`.vpce.amazonaws.com`

* The regional VPC endpoint DNS name. Always resolve to private IP
  addresses.

- **Zonal DNS name**:
  `vpce-`1a2b3c4d-5e6f`-`availability_zone_code`.s3vectors.`region`.vpce.amazonaws.com`

* Zone-specific VPC endpoint DNS names. Always resolve to private IP
  addresses.

You can also use the DNS name of the public endpoint
`s3vectors.`region`.api.aws` as the private
DNS name of the endpoint service if you have private DNS enabled for the VPC
endpoint.

## IP addressing for interface

endpoints

S3 Vectors regional, zonal, and private DNS endpoints support
IPv4, IPv6, and dualstack IP types for AWS PrivateLink. For more information, see [IP address types](../../../vpc/latest/privatelink/privatelink-access-aws-services.md#aws-service-ip-address-type "../../../vpc/latest/privatelink/privatelink-access-aws-services.md#aws-service-ip-address-type") and [DNS record IP type for AWS services](../../../vpc/latest/privatelink/privatelink-access-aws-services.md#aws-services-dns-record-ip-type "../../../vpc/latest/privatelink/privatelink-access-aws-services.md#aws-services-dns-record-ip-type") in the
_AWS PrivateLink Guide_.

The following are some things you should know before trying to access S3 Vectors
vector indexes and vector buckets over IPv6 in your VPC:

- The client you use to access vectors and your S3 Vectors client must both
  have dual-stack enabled.
- If your VPC security group doesn't have IPv6 set up, you'll need to configure a rule to allow IPv6 traffic. For more information, see [Step 3: Update your security group rules](../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md#vpc-migrate-ipv6-sg-rules "../../../vpc/latest/userguide/vpc-migrate-ipv6-add.md#vpc-migrate-ipv6-sg-rules") in the _VPC User Guide_
  and [Configure security group rules](../../../ec2/latest/userguide/working-with-security-groups.md#adding-security-group-rule "../../../ec2/latest/userguide/working-with-security-groups.md#adding-security-group-rule") in the
  _Amazon EC2 User Guide_.
- If your VPC doesn't have IPv6 CIDRs assigned, you will need to manually add
  an IPv6 CIDR block to your VPC. For more information, see [Add
  IPv6 support for your VPC](../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-ipv6 "../../../vpc/latest/privatelink/vpc-endpoints-access.md#vpc-endpoint-ipv6") in the
  _AWS PrivateLink Guide_.
- If you use IP address filtering IAM policies, they must be updated to handle
  IPv6 addresses. For more information about managing access permissions with
  IAM, see [Identity and Access management in
  S3 Vectors](s3-vectors-access-management.md "s3-vectors-access-management.md").

## Creating a VPC interface endpoint for

S3 Vectors

You can create a VPC interface endpoint for S3 Vectors using the VPC console, AWS
CLI, AWS SDKs, or AWS API.

1. Open the VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, choose **AWS
   services**.
5. For **Services**, search for `s3vectors`
   and select
   `com.amazonaws.`region`.s3vectors`.
6. For **VPC**, select the VPC where you want to create
   the endpoint.
7. (Optional) Under **Additional settings**, for
   **Enable DNS name**, choose whether to enable the
   private DNS feature. When enabled, requests that use the public service
   endpoint
   (`s3vectors.`region`.api.aws`),
   such as requests made through AWS SDKs, resolve to your VPC endpoint
   instead of the public endpoint.
8. For **Subnets**, select the subnets where you want to
   create the endpoint network interfaces.
9. For **IP address type**, choose the IP address type
   for the endpoint:
   - **IPv4**: Assign IPv4 addresses to the
     endpoint network interfaces. This option is supported only if
     all selected subnets have IPv4 address ranges.
   - **IPv6**: Assign IPv6 addresses to the
     endpoint network interfaces. This option is supported only if
     all selected subnets are IPv6 only subnets.
   - **Dualstack**: Assign both IPv4 and IPv6
     addresses to the endpoint network interfaces. This option is
     supported only if all selected subnets have both IPv4 and IPv6
     address ranges.

10. For **Security groups**, select the security groups
    to associate with the endpoint network interfaces.
11. (Optional) For **Policy**, you can attach a VPC
    endpoint policy to control access to S3 Vectors through the endpoint.
    To allow all operations by all principals on all S3 Vectors resources
    over the interface endpoint, choose **Full access**. To restrict access,
    choose **Custom** and enter a policy. For more information, see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the AWS PrivateLink Guide. If you don't attach a policy, the default policy allows full
    access.
12. Choose **Create endpoint**.

To create a new VPC endpoint that returns both IPv4 and IPv6 for S3 Vectors, use the following example CLI command. For more information, see
[create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md").

```
aws ec2 create-vpc-endpoint \
    --vpc-id `vpc-12345678` \
    --service-name com.amazonaws.`region`.s3vectors \
    --vpc-endpoint-type Interface \
    --subnet-ids `subnet-12345678` `subnet-87654321` \
    --security-group-ids `sg-12345678` \
    --ip-address-type dualstack \
    --private-dns-enabled
```

The `--private-dns-enabled` parameter enables the private DNS
feature. When enabled, requests to
`s3vectors.`region`.api.aws` will
route through your VPC endpoint.

For more information about creating VPC endpoints, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _VPC User Guide_.

## VPC endpoint policies for

S3 Vectors

Similar to resource-based policies, you can attach an endpoint policy to your VPC endpoint to
control access to vector indexes and vector buckets. For more information about the endpoint policies, see [Control
access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
AWS PrivateLink Guide.

### Example VPC endpoint

policies

The following example VPC endpoint policy allows access to all S3 Vectors
operations for all principals:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3vectors:*"
      ],
      "Resource": "*"
    }
  ]
}
```

The following example VPC endpoint policy restricts access to a specific
vector bucket:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3vectors:GetVectorBucket",
        "s3vectors:ListIndexes",
        "s3vectors:GetIndex",
        "s3vectors:QueryVectors",
        "s3vectors:GetVectors"
      ],
      "Resource": [
        "arn:aws:s3vectors:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`",
        "arn:aws:s3vectors:`us-west-2`:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`/*"
      ]
    }
  ]
}
```

The following example VPC endpoint policy allows access only during business hours
using the `aws:CurrentTime` condition key:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3vectors:*",
      "Resource": "*",
      "Condition": {
        "DateGreaterThan": {
          "aws:CurrentTime": "08:00Z"
        },
        "DateLessThan": {
          "aws:CurrentTime": "18:00Z"
        }
      }
    }
  ]
}
```

## Configuring S3 Vectors

clients for VPC endpoints

When using VPC endpoints with S3 Vectors, you can configure your S3 Vectors clients
to use either the service DNS name or the VPC endpoint DNS name.

SDK for Python
The following example shows how to configure the S3 Vectors
client in SDK for Python (Boto3) to use a VPC endpoint:

```
import boto3

# Using service DNS name (requires private DNS feature enabled on VPC endpoint)
s3vectors_client = boto3.client(
    's3vectors',
    region_name='us-west-2',
    endpoint_url='https://s3vectors.us-west-2.api.aws'
)

# Using VPC endpoint DNS name
s3vectors_client = boto3.client(
    's3vectors',
    region_name='us-west-2',
    endpoint_url='https://vpce-12345678.s3vectors.us-west-2.vpce.amazonaws.com'
)
```

## Troubleshooting VPC

endpoints

If you're experiencing issues with your interface VPC endpoint, consider the
following troubleshooting steps:

- **DNS resolution**: Verify that DNS queries for
  the endpoint resolve to private IP addresses within your VPC CIDR
  range when using private DNS.
- **Security groups**: Ensure that the security
  group associated with the VPC endpoint allows inbound HTTPS traffic (port 443)
  from your VPC resources.
- **Route tables**: Verify that your subnet route
  tables don't have conflicting routes that might redirect traffic away from the
  VPC endpoint.
- **VPC endpoint policy**: Check that your VPC
  endpoint policy allows the necessary S3 Vectors actions and resources.
- **Client configuration**: If the private DNS
  feature is disabled, configure your S3 Vectors client to use the VPC endpoint
  DNS name instead of the service DNS name.

## Monitoring VPC endpoint

usage

You can monitor your S3 Vectors VPC endpoint usage through
CloudTrail [NetworkActivity](../../../awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-network-events-with-cloudtrail.md") events logs.

For more information about S3 Vectors logging, see [Logging with AWS CloudTrail for S3 Vectors](s3-vectors-logging.md "s3-vectors-logging.md").
