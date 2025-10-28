# Use VPC endpoints to control access to AWS KMS resources

You can control access to AWS KMS resources and operations when the request comes from VPC
or uses a VPC endpoint. To do so, use one of the following [global condition
keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#AvailableKeys") in a [key policy](key-policies.md "key-policies.md") or [IAM policy](iam-policies.md "iam-policies.md").

- Use the `aws:sourceVpce` condition key to grant or restrict access based on
  the VPC endpoint.
- Use the `aws:sourceVpc` condition key to grant or restrict access based on
  the VPC that hosts the private endpoint.

###### Note

Use caution when creating key policies and IAM policies based on your VPC endpoint. If
a policy statement requires that requests come from a particular VPC or VPC endpoint,
requests from integrated AWS services that use an AWS KMS resource on your behalf might
fail. For help, see [Using VPC endpoint conditions in policies with AWS KMS
permissions](conditions-aws.md#conditions-aws-vpce "conditions-aws.md#conditions-aws-vpce").

Also, the `aws:sourceIP` condition key is not effective when the request
comes from an [Amazon VPC endpoint](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md"). To
restrict requests to a VPC endpoint, use the `aws:sourceVpce` or
`aws:sourceVpc` condition keys. For more information, see [Identity and access management for VPC
endpoints and VPC endpoint services](../../../vpc/latest/privatelink/vpc-endpoints-iam.md "../../../vpc/latest/privatelink/vpc-endpoints-iam.md") in the _AWS PrivateLink Guide_.

You can use these global condition keys to control access to AWS KMS keys (KMS keys),
aliases, and to operations like [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md")
that don't depend on any particular resource.

For example, the following sample key policy allows a user to perform some cryptographic
operations with a KMS key only when the request uses the specified VPC endpoint. When a user
makes a request to AWS KMS, the VPC endpoint ID in the request is compared to the
`aws:sourceVpce` condition key value in the policy. If they do not match, the
request is denied.

To use a policy like this one, replace the placeholder AWS account ID and VPC endpoint
IDs with valid values for your account.

JSON

```
`{
 "Id": "example-key-1",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnableIAMpolicies",
 "Effect": "Allow",
 "Principal": {"AWS":["`111122223333`"]},
 "Action": ["kms:*"],
 "Resource": "*"
 },
 {
 "Sid": "Restrict usage to my VPC endpoint",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:ReEncrypt*",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "aws:sourceVpce": "`vpce-1234abcdf5678c90a`"
 }
 }
 }

 ]
}`

```

You can also use the `aws:sourceVpc` condition key to restrict access to your
KMS keys based on the VPC in which VPC endpoint resides.

The following sample key policy allows commands that manage the KMS key only when they
come from `vpc-12345678`. In addition, it allows commands that use the KMS key
for cryptographic operations only when they come from `vpc-2b2b2b2b`. You might use
a policy like this one if an application is running in one VPC, but you use a second, isolated
VPC for management functions.

To use a policy like this one, replace the placeholder AWS account ID and VPC endpoint
IDs with valid values for your account.

JSON

```
`{
 "Id": "example-key-2",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAdministrativeActionsFromVPC",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": [
 "kms:Create*",
 "kms:Enable*",
 "kms:Put*",
 "kms:Update*",
 "kms:Revoke*",
 "kms:Disable*",
 "kms:Delete*",
 "kms:TagResource",
 "kms:UntagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpc": "`vpc-12345678`"
 }
 }
 },
 {
 "Sid": "`AllowKeyUsageFromVPC2b2b2b2b`",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": [
 "kms:Encrypt",
 "kms:Decrypt",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:sourceVpc": "`vpc-2b2b2b2b`"
 }
 }
 },
 {
 "Sid": "AllowReadActionsEverywhere",
 "Effect": "Allow",
 "Principal": {
 "AWS": "`111122223333`"
 },
 "Action": [
 "kms:Describe*",
 "kms:List*",
 "kms:Get*"
 ],
 "Resource": "*"
 }
 ]
}`

```
