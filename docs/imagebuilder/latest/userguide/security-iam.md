# Identity and Access Management integration for Image Builder

###### Topics

- [Audience](#security-iam-audience "#security-iam-audience")
- [Authenticating with identities](#security-iam-authentication "#security-iam-authentication")
- [How Image Builder works with IAM policies and roles](security_iam_service-with-iam.md "security_iam_service-with-iam.md")
- [Manage data perimeters for S3 bucket
  download access in Image Builder](security-iam-data-perimeter.md "security-iam-data-perimeter.md")
- [Image Builder identity-based policies](security-iam-identity-based-policies.md "security-iam-identity-based-policies.md")
- [Image Builder
  resource-based policies](#security-iam-resource-based-policies "#security-iam-resource-based-policies")
- [Use AWS managed policies for EC2 Image Builder](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Use IAM service-linked roles for
  Image Builder](image-builder-service-linked-role.md "image-builder-service-linked-role.md")
- [Troubleshoot IAM issues in Image Builder](security_iam_troubleshoot.md "security_iam_troubleshoot.md")

## Audience

How you use AWS Identity and Access Management (IAM) differs based on your role:

- **Service user** - request permissions from your
  administrator if you cannot access features (see [Troubleshoot IAM issues in Image Builder](security_iam_troubleshoot.md "security_iam_troubleshoot.md"))
- **Service administrator** - determine user access and
  submit permission requests (see [How Image Builder works with IAM policies and roles](security_iam_service-with-iam.md "security_iam_service-with-iam.md"))
- **IAM administrator** - write policies to manage
  access (see [Image Builder
  identity-based policies](security_iam_service-with-iam.md#security_iam_id-based-policy-examples "security_iam_service-with-iam.md#security_iam_id-based-policy-examples"))

## Authenticating with identities

For detailed information about how to provide authentication for people and processes
in your AWS account, see [Identities](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

## Image Builder

resource-based policies

For information about how to create a component, see [Use components to customize your Image Builder image](manage-components.md "manage-components.md").

### Restricting Image Builder component access to specific IP addresses

The following example grants permissions to any user to perform any Image Builder
operations on components. However, the request must originate from the range of IP
addresses specified in the condition.

The condition in this statement identifies the 54.240.143.\* range of allowed
Internet Protocol version 4 (IPv4) IP addresses, with one exception:
54.240.143.188.

The `Condition` block uses the `IpAddress` and
`NotIpAddress` conditions and the `aws:SourceIp` condition
key, which is an AWS-wide condition key. For more information about these
condition keys, see [Specifying
Conditions in a Policy](../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md "../../../AmazonS3/latest/userguide/amazon-s3-policy-keys.md"). The`aws:sourceIp` IPv4 values use the
standard CIDR notation. For more information, see [IP Address Condition Operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_IPAddress") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "IBPolicyId1",
 "Statement": [
 {
 "Sid": "IPAllow",
 "Effect": "Allow",
 "Action": "imagebuilder:GetComponent",
 "Resource": "arn:aws:imagebuilder:*::`examplecomponent`/*",
 "Condition": {
 "IpAddress": {"aws:SourceIp": "54.240.143.0/24"},
 "NotIpAddress": {"aws:SourceIp": "54.240.143.188/32"}
 }
 }
 ]
}`

```
