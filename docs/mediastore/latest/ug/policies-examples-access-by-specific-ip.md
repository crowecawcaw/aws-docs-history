End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example container policy: Access restricted to specific IP addresses

This example policy allows access to all AWS Elemental MediaStore operations on objects in the
specified container. However, the request must originate from the range of IP
addresses specified in the condition.

The condition in this statement identifies the 198.51.100.\* range of allowed
Internet Protocol version 4 (IPv4) IP addresses, with one exception:
198.51.100.188.

The `Condition` block uses the `IpAddress` and
`NotIpAddress` conditions and the `aws:SourceIp` condition
key, which is an AWS-wide condition key. The `aws:sourceIp` IPv4 values
use the standard CIDR notation. For more information, see [IP
Address Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements.md#Conditions_IPAddress") in the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessBySpecificIPAddress",
 "Effect": "Allow",
 "Action": [
 "mediastore:GetObject",
 "mediastore:DescribeObject"
 ],
 "Principal": "*",
 "Resource": "arn:aws:mediastore:`us-east-2`:`333333333333`:container/`<container name>`/*",
 "Condition": {
 "IpAddress": {
 "aws:SourceIp": [
 "198.51.100.0/24"
 ]
 },
 "NotIpAddress": {
 "aws:SourceIp": "198.51.100.188/32"
 }
 }
 }
 ]
}`

```
