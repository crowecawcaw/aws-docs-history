# Resource control

policy examples

The example [resource control policies
(RCPs)](orgs_manage_policies_rcps.md "orgs_manage_policies_rcps.md") displayed in this topic are for information purposes only. For data perimeter examples, see [Data Perimeter Policy Examples](https://github.com/aws-samples/data-perimeter-policy-examples/tree/main "https://github.com/aws-samples/data-perimeter-policy-examples/tree/main") in GitHub.

###### Before using these examples

Before you use these example RCPs in your organization, do the following:

- Carefully review and customize the RCPs for your unique requirements.
- Thoroughly test the RCPs in your environment with the AWS services that you
  use.
  The example policies in this section demonstrate the implementation and use of
  RCPs. They're **_not_** intended to be interpreted as official AWS
  recommendations or best practices to be implemented exactly as shown. It is your
  responsibility to carefully test any policies for its suitability to
  solve the business requirements of your environment. Deny-based resource control
  policies can unintentionally limit or block your use of AWS services unless
  you add the necessary exceptions to the policy.

## General examples

###### Topics

- [RCPFullAWSAccess](#example-rcp-full-aws-access "#example-rcp-full-aws-access")
- [Cross-service confused deputy protection](#example-rcp-confused-deputy "#example-rcp-confused-deputy")
- [Restrict access to only HTTPS connections to your resources](#example-rcp-enforce-ssl "#example-rcp-enforce-ssl")
- [Consistent Amazon S3 bucket policy controls](#example-rcp-consistent-bucket "#example-rcp-consistent-bucket")

### RCPFullAWSAccess

The following policy is an AWS managed policy and is automatically attached to the organization root, every OU, and
every account in your organization, when you enable resource control policies (RCPs). You cannot detach this policy.
This default RCP allows all principals and actions access to your resources, meaning until you start creating and attaching RCPs, all your existing IAM permissions continue to operate as they did.
You do not need to test the effect of this policy as it will allow existing authorization
behavior to continue for your resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": "*",
 "Action": "*",
 "Resource": "*"
 }
 ]
}`

```

### Cross-service confused deputy protection

Some AWS services (calling services) use their AWS service principal
to access AWS resources from other AWS services (called services).
When an actor not intended to have access to an AWS resource attempts
to use the trust of an AWS service principal to interact with resources
that they are not intended to have access to it is known as the cross-service confused deputy problem. For more information, see [The confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _IAM User Guide_

The following policy requires that AWS service principals accessing your resources only do so on behalf of requests from your organization.
This policy applies the control only on requests that have `aws:SourceAccount`
present so that service integrations that do not require the use of `aws:SourceAccount` aren't impacted. If the `aws:SourceAccount` is present in the request context, the `Null` condition will evaluate to `true`, causing the
`aws:SourceOrgID` key to be enforced.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceConfusedDeputyProtection",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "s3:*",
 "sqs:*",
 "kms:*",
 "secretsmanager:*",
 "sts:*"
 ],
 "Resource": "*",
 "Condition": {
 "StringNotEqualsIfExists": {
 "aws:SourceOrgID": "`my-org-id`",
 "aws:SourceAccount": [
 "`third-party-account-a`",
 "`third-party-account-b`"
 ]
 },
 "Bool": {
 "aws:PrincipalIsAWSService": "true"
 },
 "Null": {
 "aws:SourceArn": "false"
 }
 }
 }
 ]
}`

```

### Restrict access to only HTTPS connections to your resources

The following policy requires that access to your resources only occurs on encrypted connections over HTTPS (TLS).
This can help you prevent potential attackers from manipulating network traffic.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceSecureTransport",
 "Effect": "Deny",
 "Principal": "*",
 "Action": [
 "sts:*",
 "s3:*",
 "sqs:*",
 "secretsmanager:*",
 "kms:*"
 ],
 "Resource": "*",
 "Condition": {
 "BoolIfExists": {
 "aws:SecureTransport": "false"
 }
 }
 }
 ]
}`

```

### Consistent Amazon S3 bucket policy controls

The following RCP contains multiple statements to enforce consistent access controls on
Amazon S3 buckets in your organization.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "EnforceS3TlsVersion",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": "*",
 "Condition": {
 "NumericLessThan": {
 "s3:TlsVersion": [
 "1.2"
 ]
 }
 }
 },
 {
 "Sid": "EnforceKMSEncryption",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:PutObject",
 "Resource": "*",
 "Condition": {
 "Null": {
 "s3:x-amz-server-side-encryption-aws-kms-key-id": "true"
 }
 }
 }
 ]
}`

```

- The statement ID `EnforceS3TlsVersion` – Require a minimum
  TLS version of 1.2 for access to S3 buckets.
- The statement ID `EnforceKMSEncryption` – Require objects to
  be server-side encrypted with KMS keys.
