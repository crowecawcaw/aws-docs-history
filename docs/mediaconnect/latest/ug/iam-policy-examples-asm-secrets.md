# Policy examples for accessing MediaConnect

encryption keys in Secrets Manager

You can create IAM policies that allow AWS Elemental MediaConnect to read encryption keys that are
stored as secrets in AWS Secrets Manager.

When setting up static key encryption using MediaConnect, [you create an IAM
policy](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy") that you assign to MediaConnect. This policy allows MediaConnect to read the
secrets that you have stored in Secrets Manager. The settings for this policy are entirely up to
you. The policy can range from most restrictive (allowing access to only specific
secrets) to least restrictive (allowing access to any secret that you create using your
AWS account). We recommend using the most restrictive policy as a best practice.
However, the following examples show you how to set up policies with different levels of
restriction. Because MediaConnect only needs read access to secrets, all of the examples show
only the actions that are necessary to read the values that you store.

###### Note

While the following example IAM policies for Secrets Manager are broadly applicable to
various AWS services, this page specifically demonstrates their use in the context
of MediaConnect. For more information about Secrets Manager, refer to the [AWS Secrets Manager
documentation](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").

###### Topics

- [Allow read access to
  specific secrets in Secrets Manager](#iam-policy-examples-asm-specific-secrets "#iam-policy-examples-asm-specific-secrets")
- [Allow read access to
  all secrets created in a specific AWS Region in Secrets Manager](#iam-policy-examples-asm-secrets-in-a-region "#iam-policy-examples-asm-secrets-in-a-region")
- [Allow read access to all
  resources in Secrets Manager](#iam-policy-examples-asm-secrets-all "#iam-policy-examples-asm-secrets-all")

## Allow read access to

specific secrets in Secrets Manager

The following example IAM policy allows read access to specific resources
(secrets) that you create in Secrets Manager.

Replace the `placeholder text` in the ARNs with your own
information. The ARNs should represent the secrets that store the encryption keys
you want to use with MediaConnect.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-west-2`:`111122223333`:secret:`aes128-1a2b3c`",
 "arn:aws:secretsmanager:`us-west-2`:`111122223333`:secret:`aes192-4D5e6F`",
 "arn:aws:secretsmanager:`us-west-2`:`111122223333`:secret:`aes256-7g8H9i`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "secretsmanager:ListSecrets",
 "Resource": "*"
 }
 ]
}`

```

## Allow read access to

all secrets created in a specific AWS Region in Secrets Manager

The following IAM policy allows read access to all secrets that you create in a
specific AWS Region in Secrets Manager, including any encryption keys used for MediaConnect. This
policy applies to resources that you have created already and all resources that you
create in the future in the specified Region. This might be useful when managing
multiple encrypted MediaConnect flows within the same Region.

Replace the `placeholder text` in the ARNs with your own
information. The Region and account ID should represent where your secrets are
stored.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": "arn:aws:secretsmanager:`us-west-2`:`111122223333`:secret:*"
 },
 {
 "Effect": "Allow",
 "Action": "secretsmanager:ListSecrets",
 "Resource": "*"
 }
 ]
}`

```

## Allow read access to all

resources in Secrets Manager

The following IAM policy allows read access to all resources that you create in
Secrets Manager, including any encryption keys used for MediaConnect. This policy applies to
resources that you have created already and all resources that you create in the
future. This broader access might be needed when managing encrypted MediaConnect flows
across multiple regions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds",
 "secretsmanager:ListSecrets"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

For more information on setting up encryption for your MediaConnect flows, see
[Data
protection](data-protection.md "data-protection.md") in this guide. For general information about using Secrets Manager, refer
to the [AWS Secrets Manager User Guide](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md").
