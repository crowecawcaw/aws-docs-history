# AWS PrivateLink for

S3 on Outposts

S3 on Outposts supports AWS PrivateLink, which provides direct management access to your
S3 on Outposts storage through a private endpoint within your virtual private network. This
allows you to simplify your internal network architecture and perform management operations
on your Outposts object storage by using private IP addresses in your Virtual Private Cloud
(VPC). Using AWS PrivateLink eliminates the need to use public IP addresses or proxy
servers.

With AWS PrivateLink for Amazon S3 on Outposts, you can provision _interface VPC endpoints_ in your virtual private cloud (VPC) to access your
S3 on Outposts [bucket management](S3OutpostsAPI.md#S3OutpostsAPIsBucket "S3OutpostsAPI.md#S3OutpostsAPIsBucket") and [endpoint management](S3OutpostsAPI.md#S3OutpostsAPIs "S3OutpostsAPI.md#S3OutpostsAPIs") APIs. Interface VPC endpoints are directly
accessible from applications deployed in your VPC or on premises over your virtual private
network (VPN) or AWS Direct Connect. You can access the bucket and endpoint management APIs
through AWS PrivateLink. AWS PrivateLink doesn't support [data transfer](S3OutpostsAPI.md#S3OutpostsAPIsObject "S3OutpostsAPI.md#S3OutpostsAPIsObject") API operations, such as GET, PUT, and similar APIs. These
operations are already transferred privately through the S3 on Outposts endpoint and access point
configuration. For more information, see [Networking for S3 on Outposts](S3OutpostsNetworking.md "S3OutpostsNetworking.md").

Interface endpoints are represented by one or more elastic network interfaces (ENIs) that are
assigned private IP addresses from subnets in your VPC. Requests made to interface endpoints
for S3 on Outposts are automatically routed to S3 on Outposts bucket and endpoint management APIs on
the AWS network. You can also access interface endpoints in your VPC from on-premises
applications through AWS Direct Connect or AWS Virtual Private Network (AWS VPN). For more information about how to
connect your VPC with your on-premises network, see the [_AWS Direct Connect User
Guide_](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md") and the [_AWS Site-to-Site VPN User Guide_](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md").

Interface endpoints route requests for S3 on Outposts bucket and endpoint management APIs over
the AWS network and through AWS PrivateLink, as illustrated in the following diagram.

![Data flow diagram shows how interface endpoints route requests for S3 on Outposts bucket and endpoint management APIs.](images/s3-outposts-interface-endpoints.png)
For general information about interface endpoints, see [Interface VPC endpoints
(AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md") in the _AWS PrivateLink Guide_.

###### Topics

- [Restrictions and
  limitations](#s3-outposts-privatelink-restrictions "#s3-outposts-privatelink-restrictions")
- [Accessing S3 on Outposts
  interface endpoints](#s3-outposts-accessing-s3-interface-endpoints "#s3-outposts-accessing-s3-interface-endpoints")
- [Updating an on-premises
  DNS configuration](#s3-outposts-updating-on-premises-dns-config "#s3-outposts-updating-on-premises-dns-config")
- [Creating a VPC endpoint for
  S3 on Outposts](#s3-outposts-creating-vpc "#s3-outposts-creating-vpc")
- [Creating bucket policies and
  VPC endpoint policies for S3 on Outposts](#s3-outposts-creating-vpc-endpoint-policy "#s3-outposts-creating-vpc-endpoint-policy")

## Restrictions and

limitations

When you access S3 on Outposts bucket and endpoint management APIs through AWS PrivateLink,
VPC limitations apply. For more information, see [Interface endpoint properties and limitations](../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/privatelink/vpce-interface.md#vpce-interface-limitations") and [AWS PrivateLink quotas](../../../vpc/latest/privatelink/vpc-limits-endpoints.md "../../../vpc/latest/privatelink/vpc-limits-endpoints.md")
in the _AWS PrivateLink Guide_.

In addition, AWS PrivateLink doesn't support the following:

- [Federal Information Processing
  Standard (FIPS) endpoints](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/")
- [S3 on Outposts data transfer APIs](S3OutpostsAPI.md#S3OutpostsAPIsObject "S3OutpostsAPI.md#S3OutpostsAPIsObject"),
  for example, GET, PUT, and similar object API operations.
- Private DNS

## Accessing S3 on Outposts

interface endpoints

To access S3 on Outposts bucket and endpoint management APIs using AWS PrivateLink, you
_must_ update your applications to use endpoint-specific DNS names.
When you create an interface endpoint, AWS PrivateLink generates two types of endpoint-specific
S3 on Outposts names: _Regional_ and _zonal_.

- **Regional DNS names** – include a unique
  VPC endpoint ID, a service identifier, the AWS Region, and
  `vpce.amazonaws.com`, for example,
  ``vpce-1a2b3c4d-5e6f`.s3-outposts.us-east-1.vpce.amazonaws.com`.
- **Zonal DNS names** – include a unique
  VPC endpoint ID, the Availability Zone, a service identifier, the AWS Region,
  and `vpce.amazonaws.com`, for example,
  ``vpce-1a2b3c4d-5e6f`-**us-east-1a.**s3-outposts.us-east-1.vpce.amazonaws.com`. You
  might use this option if your architecture isolates Availability Zones. For
  example, you could use zonal DNS names for fault containment or to reduce
  Regional data transfer costs.

###### Important

S3 on Outposts interface endpoints are resolved from the public DNS domain.
S3 on Outposts does not support private DNS. Use the `--endpoint-url`
parameter for all bucket and endpoint management APIs.

### AWS CLI examples

Use the `--region` and `--endpoint-url` parameters to access
bucket management and endpoint management APIs through S3 on Outposts interface endpoints.

###### Example : Use the endpoint URL to list buckets with the S3 control API

In the following example, replace the Region
`us-east-1`, VPC endpoint URL
`vpce-1a2b3c4d-5e6f.s3.us-east-1.vpce.amazonaws.com`,
and account ID `111122223333`
with appropriate information.

```
aws s3control list-regional-buckets --region `us-east-1` --endpoint-url https://`vpce-1a2b3c4d-5e6f.s3-outposts.us-east-1.vpce.amazonaws.com` --account-id `111122223333`
```

### AWS SDK

examples

Update your SDKs to the latest version, and configure your clients to use an endpoint
URL for accessing the S3 control API for S3 on Outposts interface endpoints.

SDK for Python (Boto3)

###### Example : Use an endpoint URL to access the S3 control API

In the following example, replace the Region
`us-east-1` and VPC
endpoint URL
`vpce-1a2b3c4d-5e6f.s3-outposts.us-east-1.vpce.amazonaws.com`
with appropriate information.

```
control_client = session.client(
service_name='s3control',
region_name='`us-east-1`',
endpoint_url='https://`vpce-1a2b3c4d-5e6f.s3-outposts.us-east-1.vpce.amazonaws.com`'
)
```

For more information, see [AWS PrivateLink for Amazon S3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-privatelink.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-example-privatelink.html") in the _Boto3 developer
guide_.

SDK for Java 2.x

###### Example : Use an endpoint URL to access the S3 control API

In the following example, replace the VPC endpoint URL
`vpce-1a2b3c4d-5e6f.s3-outposts.us-east-1.vpce.amazonaws.com`
and the Region
`Region.US_EAST_1` with
appropriate information.

```
// control client
Region region = `Region.US_EAST_1`;
s3ControlClient = S3ControlClient.builder().region(region)
                                 .endpointOverride(URI.create("https://`vpce-1a2b3c4d-5e6f.s3-outposts.us-east-1.vpce.amazonaws.com`"))
                                 .build()
```

For more information, see [`S3ControlClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3control/S3ControlClient.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3control/S3ControlClient.html") in the
_AWS SDK for Java API Reference_.

## Updating an on-premises

DNS configuration

When using endpoint-specific DNS names to access the interface endpoints for S3 on Outposts
bucket management and endpoint management APIs, you don’t have to update your on-premises
DNS resolver. You can resolve the endpoint-specific DNS name with the private IP address of
the interface endpoint from the public S3 on Outposts DNS domain.

## Creating a VPC endpoint for

S3 on Outposts

To create a VPC interface endpoint for S3 on Outposts, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink
Guide_.

## Creating bucket policies and

VPC endpoint policies for S3 on Outposts

You can attach an endpoint policy to your VPC endpoint that controls access to S3 on Outposts.
You can also use the `aws:sourceVpce` condition in S3 on Outposts bucket
policies to restrict access to specific buckets from a specific VPC endpoint. With VPC
endpoint policies, you can control access to S3 on Outposts bucket management APIs and
endpoint management APIs. With bucket policies, you can control access to the
S3 on Outposts bucket management APIs. However, you can't manage access to object actions
for S3 on Outposts using `aws:sourceVpce`.

Access policies for S3 on Outposts specify the following information:

- The AWS Identity and Access Management (IAM) principal for which actions are allowed or
  denied.
- The S3 control actions that are allowed or denied.
- The S3 on Outposts resources on which actions are allowed or denied.

The following examples show policies that restrict access to a bucket or to an endpoint.
For more information about VPC connectivity, see [Network-to-VPC connectivity options](../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md "../../../whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.md") in the AWS whitepaper [Amazon Virtual
Private Cloud Connectivity Options](../../../whitepapers/latest/aws-vpc-connectivity-options/welcome.md "../../../whitepapers/latest/aws-vpc-connectivity-options/welcome.md").

###### Important

- When you apply the example policies for VPC endpoints described in this
  section, you might block your access to the bucket without intending to do
  so. Bucket permissions that limit bucket access to connections originating
  from your VPC endpoint can block all connections to the bucket. For
  information about how to fix this issue, see [My bucket policy has the wrong VPC or VPC endpoint ID. How can I fix
  the policy so that I can access the bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-regain-access/ "https://aws.amazon.com/premiumsupport/knowledge-center/s3-regain-access/") in the
  _Support Knowledge Center_.
- Before using the following example bucket policies, replace the VPC endpoint
  ID with an appropriate value for your use case. Otherwise, you won't be able
  to access your bucket.
- If your policy only allows access to an S3 on Outposts bucket from a
  specific VPC endpoint, it disables console access for that bucket because
  console requests don't originate from the specified VPC endpoint.

###### Topics

- [Example: Restricting
  access to a specific bucket from a VPC endpoint](#privatelink-example-restrict-access-to-bucket "#privatelink-example-restrict-access-to-bucket")
- [Example: Denying access from a specific VPC endpoint in an S3 on Outposts bucket
  policy](#s3-outposts-privatelink-example-deny-access-from-vpc-endpoint "#s3-outposts-privatelink-example-deny-access-from-vpc-endpoint")

### Example: Restricting

access to a specific bucket from a VPC endpoint

You can create an endpoint policy that restricts access to specific S3 on Outposts
buckets only. The following policy restricts access for the GetBucketPolicy action
only to the `example-outpost-bucket`. To use
this policy, replace the example values with your own.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1415115909151",
 "Statement": [
 {
 "Sid": "Access-to-specific-bucket-only",
 "Principal": {
 "AWS": "111122223333"
 },
 "Action": "s3-outposts:GetBucketPolicy",
 "Effect": "Allow",
 "Resource": "arn:aws:s3-outposts:`us-east-1`:`123456789012`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outpost-bucket`"
 }
 ]
}`

```

### Example: Denying access from a specific VPC endpoint in an S3 on Outposts bucket

policy

The following S3 on Outposts bucket policy denies access to GetBucketPolicy on the
`example-outpost-bucket` bucket
through the `vpce-1a2b3c4d` VPC endpoint.

The `aws:sourceVpce` condition specifies the endpoint and does not require
an Amazon Resource Name (ARN) for the VPC endpoint resource, only the endpoint ID. To use
this policy, replace the example values with your own.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1415115909152",
 "Statement": [
 {
 "Sid": "Deny-access-to-specific-VPCE",
 "Principal": {
 "AWS": "111122223333"
 },
 "Action": "s3-outposts:GetBucketPolicy",
 "Effect": "Deny",
 "Resource": "arn:aws:s3-outposts:`us-east-1`:`123456789012`:outpost/`op-01ac5d28a6a232904`/bucket/`example-outpost-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpce": "`vpce-1a2b3c4d`"
 }
 }
 }
 ]
}`

```
