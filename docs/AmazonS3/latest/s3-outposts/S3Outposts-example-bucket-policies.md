# Bucket policy examples

With S3 on Outposts bucket policies, you can secure access to objects in your S3 on Outposts
buckets, so that only users with the appropriate permissions can access them. You can even
prevent authenticated users without the appropriate permissions from accessing your
S3 on Outposts resources.

This section presents examples of typical use cases for S3 on Outposts bucket policies. To
test these policies, replace the `user input
 placeholders` with your own information (such as your bucket name).

To grant or deny permissions to a set of objects, you can use wildcard characters
(`*`) in Amazon Resource Names (ARNs) and other values. For example, you can
control access to groups of objects that begin with a common [prefix](../../../general/latest/gr/glos-chap.md#keyprefix "../../../general/latest/gr/glos-chap.md#keyprefix") or end with a given
extension, such as `.html`.

For more information about AWS Identity and Access Management (IAM) policy language, see [Setting up IAM with S3 on Outposts](S3OutpostsIAM.md "S3OutpostsIAM.md").

###### Note

When testing [s3outposts](../../../cli/latest/reference/s3outposts.md "../../../cli/latest/reference/s3outposts.md") permissions by using the Amazon S3 console, you
must grant additional permissions that the console requires, such as
`s3outposts:createendpoint`, `s3outposts:listendpoints`, and so on.

###### Additional resources for creating bucket policies

- For a list of the IAM policy actions, resources, and condition keys you can use
  when creating an S3 on Outposts bucket policy, see [Actions, resources, and condition keys for Amazon S3 on Outposts](../../../service-authorization/latest/reference/list_amazons3onoutposts.md "../../../service-authorization/latest/reference/list_amazons3onoutposts.md").
- For guidance on creating your S3 on Outposts policy, see [Adding or editing a bucket policy for an Amazon S3 on Outposts bucket](S3OutpostsBucketPolicyEdit.md "S3OutpostsBucketPolicyEdit.md").

###### Topics

- [Managing access to an Amazon S3 on Outposts bucket based on specific IP addresses](#S3OutpostsBucketPolicyManageIPaccess "#S3OutpostsBucketPolicyManageIPaccess")

## Managing access to an Amazon S3 on Outposts bucket based on specific IP addresses

A bucket policy is a resource-based AWS Identity and Access Management (IAM) policy that you can use to grant
access permissions to your bucket and the objects in it. Only the bucket owner can
associate a policy with a bucket. The permissions attached to the bucket apply to
all of the objects in the bucket that are owned by the bucket owner. Bucket policies
are limited to 20 KB in size. For more information, see [Bucket policy](S3onOutposts.md#S3OutpostsBucketPolicies "S3onOutposts.md#S3OutpostsBucketPolicies").

### Restrict access to specific IP addresses

The following example denies all users from performing any [S3 on Outposts
operations](../userguide/S3OutpostsWorkingBuckets.md "../userguide/S3OutpostsWorkingBuckets.md") on objects in the specified buckets unless the request
originates from the specified range of IP addresses.

###### Note

When restricting access to a specific IP address, make sure that you also
specify which VPC endpoints, VPC source IP addresses, or external IP addresses
can access the S3 on Outposts bucket. Otherwise, you might lose access to the
bucket if your policy denies all users from performing any [s3outposts](../../../cli/latest/reference/s3outposts.md "../../../cli/latest/reference/s3outposts.md") operations on objects in your
S3 on Outposts bucket without the proper permissions already in place.

This policy's `Condition` statement identifies
`192.0.2.0/24` as the range of allowed
IP version 4 (IPv4) IP addresses.

The `Condition` block uses the `NotIpAddress` condition and
the `aws:SourceIp` condition key, which is an AWS wide condition key.
The `aws:SourceIp` condition key can only be used for public IP address
ranges. For more information about these condition keys, see [Actions, resources, and condition keys for S3 on Outposts](../../../service-authorization/latest/reference/list_amazons3onoutposts.md "../../../service-authorization/latest/reference/list_amazons3onoutposts.md"). The
`aws:SourceIp` IPv4 values use standard CIDR notation. For more
information, see [IAM
JSON policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress") in the
_IAM User Guide_.

###### Warning

Before using this S3 on Outposts policy, replace the
`192.0.2.0/24` IP address range in
this example with an appropriate value for your use case. Otherwise, you'll lose
the ability to access your bucket.

```
{
    "Version": "2012-10-17",
    "Id": "S3OutpostsPolicyId1",
    "Statement": [
        {
            "Sid": "IPAllow",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3-outposts:*",
            "Resource": [
                "arn:aws:aws:s3-outposts:`region`:`111122223333`:outpost/`OUTPOSTS-ID`/accesspoint/`EXAMPLE-ACCESS-POINT-NAME`",
                "arn:aws:aws:s3-outposts:`region`:`111122223333`:outpost/`OUTPOSTS-ID`/bucket/``amzn-s3-demo-bucket``"
            ],
            "Condition": {
                "NotIpAddress": {
                    "aws:SourceIp": "`192.0.2.0/24`"
                }
            }
        }
    ]
}
```

### Allow both IPv4 and IPv6 addresses

When you start using IPv6 addresses, we recommend that you update all
of your organization's policies with your IPv6 address ranges in
addition to your existing IPv4 ranges. Doing this will help to make sure that the
policies continue to work as you make the transition to IPv6.

The following S3 on Outposts example bucket policy shows how to mix IPv4 and
IPv6 address ranges to cover all of your organization's valid IP addresses. The
example policy allows access to the example IP addresses
`192.0.2.1` and
`2001:DB8:1234:5678::1` and denies
access to the addresses `203.0.113.1` and
`2001:DB8:1234:5678:ABCD::1`.

The `aws:SourceIp` condition key can only be used for public IP address
ranges. The IPv6 values for `aws:SourceIp` must be in standard CIDR
format. For IPv6, we support using `::` to represent a range of 0s
(for example, `2001:DB8:1234:5678::/64`). For more information, see
[IP address condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress") in the
_IAM User Guide_.

###### Warning

Replace the IP address ranges in this example with appropriate values for your
use case before using this S3 on Outposts policy. Otherwise, you might lose the
ability to access your bucket.

JSON

```
`{
 "Id": "S3OutpostsPolicyId2",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowIPmix",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "s3-outposts:GetObject",
 "s3-outposts:PutObject",
 "s3-outposts:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/bucket/`amzn-s3-demo-bucket`",
 "arn:aws:s3-outposts:`us-east-1`:`111122223333`:outpost/`op-01ac5d28a6a232904`/bucket/`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "`192.0.2.0/24`",
 "`2001:DB8:1234:5678::/64`"
 ]
 },
 "NotIpAddress": {
 "aws:SourceIp": [
 "`203.0.113.0/24`",
 "`2001:DB8:1234:5678:ABCD::/80`"
 ]
 }
 }
 }
 ]
}`

```
