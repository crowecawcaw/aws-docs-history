# Making requests to S3 on Outposts over IPv6

Amazon S3 on Outposts and S3 on Outposts dual-stack endpoints support requests to S3 on Outposts
buckets using either the IPv6 or IPv4 protocol. With IPv6 support for
S3 on Outposts, you can access and operate your buckets and control plane resources through
S3 on Outposts APIs over IPv6 networks.

###### Note

[S3 on Outposts object actions](../userguide/S3OutpostsAPI.md "../userguide/S3OutpostsAPI.md") (such as `PutObject` or
`GetObject`) aren’t supported over IPv6 networks.

There are no additional charges for accessing S3 on Outposts over IPv6 networks. For more
information about S3 on Outposts, see [S3 on Outposts pricing](https://aws.amazon.com/outposts/rack/pricing/ "https://aws.amazon.com/outposts/rack/pricing/").

###### Topics

- [Getting started with IPv6](#S3Outposts-ipv6-access-getting-started "#S3Outposts-ipv6-access-getting-started")
- [Using dual-stack endpoints to make requests over an IPv6 network](#S3Outposts-ipv6-access-api "#S3Outposts-ipv6-access-api")
- [Using IPv6 addresses in IAM policies](#S3Outposts-ipv6-access-iam "#S3Outposts-ipv6-access-iam")
- [Testing IP address compatibility](#S3Outposts-ipv6-access-test-compatabilty "#S3Outposts-ipv6-access-test-compatabilty")
- [Using IPv6 with AWS PrivateLink](#S3Outposts-ipv6-privatelink "#S3Outposts-ipv6-privatelink")
- [Using S3 on Outposts dual-stack endpoints](s3-outposts-dual-stack-endpoints.md "s3-outposts-dual-stack-endpoints.md")

## Getting started with IPv6

To make a request to an S3 on Outposts bucket over IPv6, you must use a
dual-stack endpoint. The next section describes how to make requests over IPv6 by
using dual-stack endpoints.

The following are important considerations before trying to access an S3 on Outposts bucket
over IPv6:

- The client and the network accessing the bucket must be enabled to use IPv6.
- Both virtual hosted-style and path style requests are supported for IPv6 access.
  For more information, see [Using S3 on Outposts dual-stack endpoints](s3-outposts-dual-stack-endpoints.md "s3-outposts-dual-stack-endpoints.md").
- If you use source IP address filtering in your AWS Identity and Access Management (IAM) user or S3 on Outposts
  bucket policies, you must update the policies to include IPv6 address
  ranges.

###### Note

This requirement only applies to S3 on Outposts bucket operations and control plane
resources across IPv6 networks. [Amazon S3 on Outposts object
actions](../userguide/S3OutpostsAPI.md "../userguide/S3OutpostsAPI.md") aren’t supported across IPv6 networks.

- When using IPv6, server access log files output IP addresses in an
  IPv6 format. You must update existing tools, scripts, and software that you
  use to parse S3 on Outposts log files, so that they can parse the IPv6
  formatted remote IP addresses. The updated tools, scripts, and software will then
  correctly parse the IPv6 formatted remote IP addresses.

## Using dual-stack endpoints to make requests over an IPv6 network

To make requests with S3 on Outposts API calls over IPv6, you can use dual-stack endpoints
via AWS CLI or AWS SDK. The [Amazon S3 control API
operations](../userguide/S3OutpostsAPI.md#S3OutpostsAPIsBucket "../userguide/S3OutpostsAPI.md#S3OutpostsAPIsBucket") and [S3 on Outposts API
operations](../userguide/S3OutpostsAPI.md#S3OutpostsAPIs "../userguide/S3OutpostsAPI.md#S3OutpostsAPIs") work the same way whether you’re accessing S3 on Outposts over an
IPv6 protocol or IPv4 protocol. However, be aware that [S3 on Outposts object
actions](../userguide/S3OutpostsAPI.md "../userguide/S3OutpostsAPI.md") (such as `PutObject` or `GetObject`) aren’t supported
over IPv6 networks.

When using the AWS Command Line Interface (AWS CLI) and AWS SDKs, you can use a parameter or flag to
change to a dual-stack endpoint. You can also specify the dual-stack endpoint directly as an
override of the S3 on Outposts endpoint in the configuration file.

You can use a dual-stack endpoint to access an S3 on Outposts bucket over IPv6 from
any of the following:

- The AWS CLI, see [Using dual-stack endpoints from the AWS CLI](s3-outposts-dual-stack-endpoints.md#s3-outposts-dual-stack-endpoints-cli "s3-outposts-dual-stack-endpoints.md#s3-outposts-dual-stack-endpoints-cli").
- The AWS SDKs, see [Using S3 on Outposts dual-stack endpoints from the AWS SDKs](s3-outposts-dual-stack-endpoints.md#s3-outposts-dual-stack-endpoints-sdks "s3-outposts-dual-stack-endpoints.md#s3-outposts-dual-stack-endpoints-sdks").

## Using IPv6 addresses in IAM policies

Before trying to access an S3 on Outposts bucket using an IPv6 protocol, make
sure that IAM users or S3 on Outposts bucket policies used for IP address filtering are
updated to include IPv6 address ranges. If IP address filtering policies aren’t
updated to handle IPv6 addresses, you can lose access to an S3 on Outposts bucket
while trying to use the IPv6 protocol.

IAM policies that filter IP addresses use [IP address
condition operators](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress"). The following S3 on Outposts bucket policy identifies the
54.240.143.\* IP range of allowed IPv4 addresses by using IP address condition
operators. Any IP addresses outside of this range will be denied access to the S3 on Outposts
bucket (`DOC-EXAMPLE-BUCKET`). Since all IPv6 addresses are outside of the
allowed range, this policy prevents IPv6 addresses from being able to access
`DOC-EXAMPLE-BUCKET`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "s3-outposts:*",
 "Resource": "arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`OUTPOSTS-ID`/bucket/`DOC-EXAMPLE-BUCKET`/*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": "54.240.143.0/24"
 }
 }
 }
 ]
}`

```

You can modify the S3 on Outposts bucket policy's `Condition` element to allow
both IPv4 (`54.240.143.0/24`) and IPv6
(`2001:DB8:1234:5678::/64`) address ranges as shown in the following example.
You can use the same type of `Condition` block shown in the example to update
both your IAM user and bucket policies.

```
       "Condition": {
         "IpAddress": {
            "aws:SourceIp": [
              "54.240.143.0/24",
               "2001:DB8:1234:5678::/64"
             ]
          }
        }
```

Before using IPv6 you must update all relevant IAM user and bucket policies that
use IP address filtering to allow IPv6 address ranges. We recommend that you update
your IAM policies with your organization's IPv6 address ranges in addition to your
existing IPv4 address ranges. For an example of a bucket policy that allows access over
both IPv6 and IPv4, see [Restrict access to specific IP addresses](S3Outposts-example-bucket-policies.md#S3Outposts-example-bucket-policies-IP-1 "S3Outposts-example-bucket-policies.md#S3Outposts-example-bucket-policies-IP-1").

You can review your IAM user policies using the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md"). For information about editing
S3 on Outposts bucket policies, see [Adding or editing a bucket policy for an Amazon S3 on Outposts bucket](S3OutpostsBucketPolicyEdit.md "S3OutpostsBucketPolicyEdit.md").

## Testing IP address compatibility

If you're using a Linux or Unix instance, or macOS X platform, you can test your access
to a dual-stack endpoint over IPv6. For example, to test the connection to
Amazon S3 on Outposts endpoints over IPv6, use the `dig` command:

```
dig s3-outposts.us-west-2.api.aws AAAA +short
```

If your dual-stack endpoint over an IPv6 network is properly set up, the `dig` command
returns the connected IPv6 addresses. For example:

```
dig s3-outposts.us-west-2.api.aws AAAA +short

2600:1f14:2588:4800:b3a9:1460:159f:ebce

2600:1f14:2588:4802:6df6:c1fd:ef8a:fc76

2600:1f14:2588:4801:d802:8ccf:4e04:817
```

## Using IPv6 with AWS PrivateLink

S3 on Outposts supports the IPv6 protocol for AWS PrivateLink services and
endpoints. With AWS PrivateLink support for the IPv6 protocol, you can connect to
service endpoints within your VPC over IPv6 networks, from either on-premises
or other private connections. The IPv6 support for [AWS PrivateLink for S3 on Outposts](../userguide/s3-outposts-privatelink-interface-endpoints.md "../userguide/s3-outposts-privatelink-interface-endpoints.md") also allows you to integrate AWS PrivateLink with dual-stack
endpoints. For steps on how to enable IPv6 for AWS PrivateLink, see [Expedite your IPv6 adoption with AWS PrivateLink services and
endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/ "https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/").

###### Note

To update the supported IP address type from IPv4 to IPv6, see [Modify the supported IP address type](../../../vpc/latest/privatelink/configure-endpoint-service.md#supported-ip-address-types "../../../vpc/latest/privatelink/configure-endpoint-service.md#supported-ip-address-types") in the _AWS PrivateLink User
Guide_.

### Using IPv6 with AWS PrivateLink

If you’re using AWS PrivateLink with IPv6, you must create an
IPv6 or dual-stack VPC interface endpoint. For general steps on how to
create a VPC endpoint using the AWS Management Console, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint") in the
_AWS PrivateLink User Guide_.

AWS Management Console
Use the following procedure to create an interface VPC endpoint that connects
to S3 on Outposts.

1. Sign in to the AWS Management Console and open the VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Service category**, choose **AWS
   services**.
5. For **Service name**, choose the S3 on Outposts service
   (**com.amazonaws.us-east-1.s3-outposts**).
6. For VPC, choose the VPC from which you'll access S3 on Outposts.
7. For **Subnets**, choose one subnet per Availability Zone
   from which you'll access S3 on Outposts. You can't select multiple subnets from the
   same Availability Zone. For each subnet that you select, a new endpoint network interface is
   created. By default, IP addresses from the subnet IP address ranges are assigned
   to the endpoint network interfaces. To designate an IP address for an endpoint
   network interface, choose **Designate IP addresses** and enter an
   IPv6 address from the subnet address range.
8. For **IP address type**, choose
   **Dualstack**. Assign both IPv4 and IPv6 addresses to your
   endpoint network interfaces. This option is supported only if all selected
   subnets have both IPv4 and IPv6 address ranges.
9. For **Security groups**, choose the security groups to
   associate with the endpoint network interfaces for the VPC endpoint. By
   default, the default security group is associated with the VPC.
10. For **Policy**, choose **Full access** to
    allow all operations by all principals on all resources over the VPC endpoint.
    Otherwise, choose **Custom** to attach a VPC endpoint policy
    that controls the permissions that principals have toperform actions on resources
    over the VPC endpoint. This option is available only if the service supports
    VPC endpoint policies. For more information, see [Endpoint
    policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md").
11. (Optional) To add a tag, choose **Add new tag** and enter
    the tag key and the tag value.
12. Choose **Create endpoint**.

###### Example– S3 on Outposts bucket policy

To allow S3 on Outposts to interact with your VPC endpoints, you can then update
your S3 on Outposts policy like this:

```
{
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3-outposts:*",
            "Resource": "*",
            "Principal": "*"
        }
    ]
}
```

AWS CLI

###### Note

To enable the IPv6 network on your VPC endpoint, you must have
`IPv6` set for the `SupportedIpAddressType` filter for
S3 on Outposts.

The following example uses the `create-vpc-endpoint` command to
create a new dual-stack interface endpoint.

```
aws ec2 create-vpc-endpoint \
--vpc-id `vpc-12345678` \
--vpc-endpoint-type `Interface` \
--service-name `com.amazonaws.us-east-1.s3-outposts` \
--subnet-id `subnet-12345678` \
--security-group-id `sg-12345678` \
--ip-address-type `dualstack` \
--dns-options "`DnsRecordIpType=dualstack`"
```

Depending on the AWS PrivateLink service configuration, newly created endpoint
connections might need to be accepted by the VPC endpoint service provider before
they can be used. For more information, see [Accept and reject endpoint connection requests](../../../vpc/latest/privatelink/configure-endpoint-service.md#accept-reject-connection-requests "../../../vpc/latest/privatelink/configure-endpoint-service.md#accept-reject-connection-requests") in the
_AWS PrivateLink User Guide_.

The following example uses the `modify-vpc-endpoint` command to
update the IPv-only VPC endpoint to a dual-stack endpoint. The dual-stack endpoint
allows access to both the IPv4 and IPv6 networks.

```
aws ec2 modify-vpc-endpoint \
--vpc-endpoint-id `vpce-12345678` \
--add-subnet-ids `subnet-12345678` \
--remove-subnet-ids `subnet-12345678` \
--ip-address-type `dualstack` \
--dns-options "`DnsRecordIpType=dualstack`"
```

For more information about how to enable the IPv6 network for AWS PrivateLink, see
[Expedite your IPv6 adoption with AWS PrivateLink services and
endpoints](https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/ "https://aws.amazon.com/blogs/networking-and-content-delivery/expedite-your-ipv6-adoption-with-privatelink-services-and-endpoints/").
