# AWS Billing Conductor

resource-based policy examples

###### Topics

- [Restricting Amazon S3 bucket access to specific IP addresses](#security_iam_resource-based-policy-examples-restrict-bucket-by-ip "#security_iam_resource-based-policy-examples-restrict-bucket-by-ip")

## Restricting Amazon S3 bucket access to specific IP addresses

The following example grants permissions to any user to perform any Amazon S3 operations
on objects in the specified bucket. However, the request must originate from the range
of IP addresses specified in the condition.

The condition in this statement identifies the 54.240.143.\* range of allowed Internet
Protocol version 4 (IPv4) IP addresses, with one exception: 54.240.143.188.

The `Condition` block uses the `IpAddress` and
`NotIpAddress` conditions and the `aws:SourceIp` condition key,
which is an AWS wide condition key. For more information about these condition keys,
see [Specifying Conditions in a
Policy](../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md "../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md"). The`aws:sourceIp` IPv4 values use the standard CIDR
notation. For more information, see [IP Address Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "S3PolicyId1",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "Condition": {
 "IpAddress": {"aws:SourceIp": "54.240.143.0/24"},
 "NotIpAddress": {"aws:SourceIp": "54.240.143.188/32"}
 }
 }
 ]
}`

```
