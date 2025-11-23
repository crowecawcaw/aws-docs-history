# Controlling access from VPC

endpoints with bucket policies

You can use Amazon S3 bucket policies to control access to buckets from specific virtual private cloud (VPC)
endpoints or
specific VPCs. This section contains example bucket policies that
you
can
use
to control Amazon S3 bucket access from VPC endpoints. To learn how to set up VPC endpoints, see
[VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the
_VPC User Guide_.

A
VPC enables you to launch AWS resources into a virtual network that
you define. A VPC endpoint enables you to create a private connection between your VPC and
another AWS service.
This
private connection doesn't
require
access over the internet, through a
virtual private
network
(VPN)
connection, through a NAT instance, or through Direct Connect.

A VPC endpoint for Amazon S3 is a logical entity within a VPC that allows connectivity only to
Amazon S3. The VPC endpoint routes requests to Amazon S3 and routes responses back to the VPC. VPC
endpoints change only how requests are routed. Amazon S3 public endpoints and DNS names will
continue to work with VPC endpoints. For important information about using VPC endpoints
with Amazon S3, see [Gateway endpoints](../../../vpc/latest/userguide/vpce-gateway.md "../../../vpc/latest/userguide/vpce-gateway.md")
and [Gateway
endpoints
for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md") in the _VPC User Guide_.

VPC endpoints for Amazon S3 provide two ways to control access to your Amazon S3 data:

- You can control the requests, users, or groups that are allowed through a specific
  VPC endpoint. For information about this type of access control, see [Controlling
  access
  to
  VPC
  endpoints
  using endpoint policies](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the
  _VPC User Guide_.
- You can control which VPCs or VPC endpoints have access to your buckets by using
  Amazon S3 bucket policies. For examples of this type of bucket policy access control, see
  the following topics on restricting access.

###### Topics

- [Restricting
  access to a specific VPC endpoint](#example-bucket-policies-restrict-accesss-vpc-endpoint "#example-bucket-policies-restrict-accesss-vpc-endpoint")
- [Restricting access to a
  specific VPC](#example-bucket-policies-restrict-access-vpc "#example-bucket-policies-restrict-access-vpc")
- [Restricting
  access to an IPv6 VPC endpoint](#example-bucket-policies-ipv6-vpc-endpoint "#example-bucket-policies-ipv6-vpc-endpoint")

###### Important

When applying the Amazon S3 bucket policies for VPC endpoints described in this section,
you might block your access to the bucket
unintentionally.
Bucket permissions that are intended to specifically limit bucket access to connections
originating from your VPC endpoint can block all connections to the bucket. For
information about how to fix this issue, see [How do I fix
my
bucket policy
when it
has the wrong VPC or VPC endpoint
ID?](https://aws.amazon.com/premiumsupport/knowledge-center/s3-regain-access/ "https://aws.amazon.com/premiumsupport/knowledge-center/s3-regain-access/")
in the _AWS Support Knowledge Center_.

## Restricting

access to a specific VPC endpoint

The following is an example of an Amazon S3 bucket policy that restricts access to a
specific bucket,
`awsexamplebucket1`,
only from the VPC endpoint with the ID `vpce-1a2b3c4d`.
If the specified
endpoint is not used,
the
policy denies all access to the
bucket.
The `aws:SourceVpce` condition
specifies
the endpoint. The `aws:SourceVpce` condition doesn't
require
an Amazon Resource Name (ARN) for the VPC endpoint resource, only the VPC endpoint ID.
For more information about using conditions in a policy, see [Bucket policy examples using condition keys](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md").

###### Important

- Before using the following example policy, replace the VPC endpoint ID
  with an appropriate value for your use case. Otherwise, you won't be able to
  access your bucket.
- This policy disables console access to the specified
  bucket
  because console requests don't originate from the specified VPC
  endpoint.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1415115909152",
 "Statement": [
 {
 "Sid": "Access-to-specific-VPCE-only",
 "Principal": "*",
 "Action": "s3:*",
 "Effect": "Deny",
 "Resource": ["arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"],
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpce": "`vpce-0abcdef1234567890`"
 }
 }
 }
 ]
}`

```

## Restricting access to a

specific VPC

You can create a bucket policy that restricts access to a specific VPC by using the
`aws:SourceVpc` condition. This is useful if you have multiple VPC
endpoints configured in the same VPC, and you want to manage access to your Amazon S3 buckets
for all of your endpoints. The following is an example of a policy that denies access to
`awsexamplebucket1` and its objects from anyone outside VPC
`vpc-111bbb22`.
If the specified
VPC isn't used,
the
policy denies all access to the
bucket.
This statement doesn't
grant access
to
the bucket. To grant access,
you
must
add a separate
`Allow`
statement. The `vpc-111bbb22` condition key doesn't
require
an ARN for the VPC resource, only the VPC ID.

###### Important

- Before using the following example policy, replace the VPC ID with an
  appropriate value for your use case. Otherwise, you won't be able to access
  your bucket.
- This policy disables console access to the specified
  bucket
  because console requests don't originate from the specified VPC.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy1415115909153",
 "Statement": [
 {
 "Sid": "Access-to-specific-VPC-only",
 "Principal": "*",
 "Action": "s3:*",
 "Effect": "Deny",
 "Resource": ["arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"],
 "Condition": {
 "StringNotEquals": {
 "aws:SourceVpc": "vpc-1a2b3c4d"
 }
 }
 }
 ]
}`

```

## Restricting

access to an IPv6 VPC endpoint

The following example policy denies all Amazon S3 (`s3:`) actions on the `amzn-s3-demo-bucket` bucket and its objects, unless the request originates from the specified VPC endpoint (`vpce-0a1b2c3d4e5f6g`) and the source IP address matches the provided IPv6 CIDR block.

```
{
   "Version": "2012-10-17",
   "Id": "Policy1415115909154",
   "Statement": [
     {
       "Sid": "AccessSpecificIPv6VPCEOnly",
       "Action": "s3:*",
       "Effect": "Deny",
       "Resource": ["arn:aws:s3:::``amzn-s3-demo-bucket``",
                    "arn:aws:s3:::``amzn-s3-demo-bucket``/*"],
       "Condition": {
         "StringNotEquals": {
           "aws:SourceVpc": "`vpc-0a1b2c3d4e5f6g4h2`"
         },
        "NotIpAddress": {
          "aws:VpcSourceIp": "2001:db8::/32"
        }
       }
     }
   ]
}

```

For information on how to restrict access to your bucket based on specific IPs or VPCs, see [How do I allow only specific VPC endpoints or IP addresses to access my Amazon S3 bucket?](https://repost.aws/knowledge-center/block-s3-traffic-vpc-ip "https://repost.aws/knowledge-center/block-s3-traffic-vpc-ip") in the AWS re:Post Knowledge Center.
