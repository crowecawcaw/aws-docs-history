# Permission policies for Mail Manager

The policies in this chapter are provided as a single point of reference for the policies
necessary to utilize all the different features of Mail Manager.

In the Mail Manager feature pages, links are provide that will take you to the respective section
on this page that contains the policies you need to utilize the feature. Select the copy
icon of the policy you need and paste it as directed in the respective feature
narrative.

The following policies give you permission to use the different features contained in
Amazon SES Mail Manager through resource permission policies and AWS Secrets Manager policies. If you're new to
permission policies, see [Amazon SES policy anatomy](policy-anatomy.md "policy-anatomy.md") and [Permissions policies for
AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access_examples.md "../../../secretsmanager/latest/userguide/auth-and-access_examples.md").

## Permission policies for Ingress endpoint

Both of the polices in this section are required to create an ingress endpoint. To learn how
to create an ingress endpoint and where to use these policies, see [Creating an ingress endpoint in the SES
console](eb-ingress.md#eb-ingress-create-console "eb-ingress.md#eb-ingress-create-console").

### Secrets Manager secrets resource permission

policy for ingress endpoint

The following Secrets Manager secrets resource permission policy is required to allow
SES to access the secret using the ingress endpoint resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Id",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": "secretsmanager:GetSecretValue",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`000000000000`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ses:`us-east-1`:`000000000000`:mailmanager-ingress-point/*"
 }
 }
 }
 ]
}`

```

### KMS customer managed key (CMK) key policy for

ingress endpoint

It is required to use a customer managed key (CMK) for your secret.
The following statement is required within your KMS key policy to allow SES to use your key for your secret.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "ses.amazonaws.com"
    },
    "Action": "kms:Decrypt",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": "secretsmanager.`us-east-1`.amazonaws.com",
            "aws:SourceAccount": "`000000000000`"
        },
        "ArnLike": {
            "aws:SourceArn": "arn:aws:ses:`us-east-1`:`000000000000`:mailmanager-ingress-point/*"
        }
    }
}
```

## Permission policies for SMTP relay

Both of the polices in this section are required to create an SMTP relay. To learn how to
create an SMTP relay and where to use these policies, see [Creating an SMTP relay in the SES
console](eb-relay.md#eb-relay-create-console "eb-relay.md#eb-relay-create-console").

### Secrets Manager secrets resource permission policy

for SMTP relay

The following Secrets Manager secrets resource permission policy is required to allow
SES to access the secret using the SMTP relay resource.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Principal": {
 "Service": [
 "ses.amazonaws.com"
 ]
 },
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`888888888888`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ses:`us-east-1`:`888888888888`:mailmanager-smtp-relay/*"
 }
 }
 }
 ]
}`

```

### KMS customer managed key (CMK) key policy for

SMTP relay

The following statement is required within your KMS key policy to allow SES to use your key for your secret.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:DescribeKey"
 ],
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "secretsmanager.`us-east-1`.amazonaws.com",
 "aws:SourceAccount": "`000000000000`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ses:`us-east-1`:`000000000000`:mailmanager-smtp-relay/*"
 }
 }
 }
 ]
}`

```

## Permission policies for Email archiving

###### Archiving export

The IAM identity calling `StartArchiveExport` must have access to the
destination S3 bucket configured by the following IAM policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`MyDestinationBucketName`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:PutObjectTagging",
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::`MyDestinationBucketName`/*"
 }
 ]
}`

```

This is the S3 bucket policy for the destination bucket:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": [
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "arn:aws:s3:::`MyDestinationBucketName`"
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl",
 "s3:PutObjectTagging",
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:::`MyDestinationBucketName`/*"
 }
 ]
}`

```

###### Note

Archiving doesn’t support [confused deputy condition keys](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md#access-analyzer-reference-policy-checks-security-warning-restrict-access-to-service-principal "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md#access-analyzer-reference-policy-checks-security-warning-restrict-access-to-service-principal") (aws:SourceArn, aws:SourceAccount,
aws:SourceOrgID, or aws:SourceOrgPaths). This is because Mail Manager's email archiving prevents the
confused deputy problem by testing if the calling identity has write permissions to
the export destination bucket using [Forward Access
Sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") before starting the actual export.

###### Archiving encryption at rest with KMS CMK

The IAM identity calling `CreateArchive` and `UpdateArchive`
must have access to the KMS key ARN through the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey",
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-west-2`:`111122223333`:key/`MyKmsKeyArnID`"
 }
}`

```

The following statements are required within your KMS key policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`MyUserRoleOrGroupName`"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "ses.`us-east-1`.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey*",
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Permission and trust polices to execute rule

actions

The SES rules execution role is an AWS Identity and Access Management (IAM) role that grants the rules
execution permission to access AWS services and resources. Before you create a rule in
a rule set, you must create an IAM role with a policy that allows access to the
required AWS resources. SES assumes this role when executing a rule action. For
example, you might create a rules execution role that has permission to write an email
message to a S3 bucket as a rule action to take when your rule's conditions are
met.

Thus, the following trust policy is required _in addition to_ the
individual permission policies in this section required to execute each specific rule
action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`888888888888`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:ses:`us-east-1`:`888888888888`:mailmanager-rule-set/*"
 }
 }
 }
 ]
 }`

```

###### Rule action policies

- [Write to S3 policy](#eb-policies-s3 "#eb-policies-s3")
- [Deliver to mailbox
  policy](#eb-policies-workmail "#eb-policies-workmail")
- [Send to internet
  policy](#eb-policies-internet "#eb-policies-internet")
- [Deliver to Q Business
  policy](#eb-policies-q "#eb-policies-q")
- [Publish to SNS policy](#eb-policies-sns "#eb-policies-sns")

### Permission policy for \*Write to

S3\* rule action

The following policy is required for your IAM role to use the **Write to
S3** rule action which delivers the received email to an
S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPutObject",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`MyDestinationBucketName`/*"
 ]
 },
 {
 "Sid": "AllowListBucket",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`MyDestinationBucketName`"
 ]
 }
 ]
}`

```

If you're using AWS KMS customer managed key for an S3 bucket with
server-side encryption enabled, then you'll need to add the IAM role policy action,
`"kms:GenerateDataKey*"`. Using the preceding example, adding this
action to your role policy would appear as follows:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowKMSKeyAccess",
 "Effect": "Allow",
 "Action": "kms:GenerateDataKey*",
 "Resource": "arn:aws:kms:`us-east-1`:`888888888888`:key/*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "kms:ResourceAliases": [
 "alias/`MyKeyAlias`"
 ]
 }
 }
 }
 ]
}`

```

For more information about attaching policies to AWS KMS keys, see [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

### Permission policy for \*Deliver to

mailbox\* rule action

The following policy is required for your IAM role to use the **Deliver to
mailbox** rule action which delivers the received email to an Amazon WorkMail
account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["workmail:DeliverToMailbox"],
 "Resource": "arn:aws:workmail:`us-east-1`:`888888888888`:organization/`MyWorkMailOrganizationID`>"
 }
 ]
 }`

```

### Permission policy for \*Send to

internet\* rule action

The following policy is required for your IAM role to use the **Send to internet**
rule action which sends the received email to an external domain.

###### Note

If your SES identity is using a default configuration set, you'll need
to also add the configuration set resource as shown in the following
example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["ses:SendEmail", "ses:SendRawEmail"],
 "Resource":[
 "arn:aws:ses:`us-east-1`:`888888888888`:identity/`example.com`",
 "arn:aws:ses:`us-east-1`:`888888888888`:configuration-set/`my-configuration-set`"
 ]
 }
 ]
 }`

```

### Permission policy for \*Deliver to Q

Business\* rule action

The following policies are required to use the **Deliver to Q
Business** rule action, which delivers the received email to an
Amazon Q Business index.

IAM policy required for your role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToQBusiness",
 "Effect": "Allow",
 "Action": [
 "qbusiness:BatchPutDocument"
 ],
 "Resource": [
 "arn:aws:qbusiness:`us-east-1`:`888888888888`:application/`ApplicationID`/index/`IndexID`"
 ]
 }
 ]
}`

```

Statement required within your KMS key policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToKMSKeyForQbusiness",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Encrypt",
 "kms:DescribeKey"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`888888888888`:key/*"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "qbusiness.`us-east-1`.amazonaws.com",
 "kms:CallerAccount": "`888888888888`"
 },
 "ForAnyValue:StringEquals": {
 "kms:ResourceAliases": [
 "alias/`MyKeyAlias`"
 ]
 }
 }
 }
 ]
}`

```

For more information about attaching policies to AWS KMS keys, see [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

### Permission policy for \*Publish to

SNS\* rule action

The following policies are required to use the **Publish to SNS**
rule action, which delivers the received email to an Amazon SNS topic.

IAM policy required for your role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToSNSTopic",
 "Effect": "Allow",
 "Action": [
 "sns:Publish"
 ],
 "Resource": [
 "arn:aws:sns:`us-east-1`:`888888888888`:`MySnsTopic`"
 ]
 }
 ]
}`

```

Statement required within your KMS key policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAccessToKMSKeyForSNS",
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey*",
 "kms:Encrypt",
 "kms:DescribeKey"
 ],
 "Resource": [
 "arn:aws:kms:`us-east-1`:`888888888888`:key/*"
 ],
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "qbusiness.`us-east-1`.amazonaws.com",
 "kms:CallerAccount": "`888888888888`"
 },
 "ForAnyValue:StringEquals": {
 "kms:ResourceAliases": [
 "alias/`MyKeyAlias`"
 ]
 }
 }
 }
 ]
}`

```

For more information about attaching policies to AWS KMS keys, see [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.
