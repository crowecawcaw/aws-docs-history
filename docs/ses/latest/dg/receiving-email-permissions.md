# Giving permissions to Amazon SES for email

receiving

Some of the tasks that you can perform when you receive email in SES, such as
sending email to an Amazon Simple Storage Service (Amazon S3) bucket or calling a AWS Lambda function, require special
permissions. This section includes example policies for several common use cases.

###### Topics in this section:

- [Setting up IAM role
  permissions for Deliver to S3 bucket action](#receiving-email-permissions-s3-iam-role "#receiving-email-permissions-s3-iam-role")
- [Give SES permission to write to
  an S3 bucket](#receiving-email-permissions-s3 "#receiving-email-permissions-s3")
- [Give SES permission to use your
  AWS KMS key](#receiving-email-permissions-kms "#receiving-email-permissions-kms")
- [Give SES permission to
  invoke a AWS Lambda function](#receiving-email-permissions-lambda "#receiving-email-permissions-lambda")
- [Give SES permission to publish
  to an Amazon SNS topic that belongs to a different AWS account](#receiving-email-permissions-sns "#receiving-email-permissions-sns")

## Setting up IAM role

permissions for Deliver to S3 bucket action

The following points are applicable to this IAM role:

- It can only be used for [Deliver to S3 bucket action](receiving-email-action-s3.md "receiving-email-action-s3.md").
- It must be used if want to write to an S3 bucket that exists in a
  region where SES [Email receiving](regions.md#region-receive-email "regions.md#region-receive-email") isn't
  available.

If want to write to an S3 bucket, you can provide an IAM role with
permissions to access the relevant resources for the [Deliver to S3 bucket action](receiving-email-action-s3.md "receiving-email-action-s3.md"). You
would also need to give SES permission to assume that role to perform the action
through an IAM trust policy as explained in the [next section](#receiving-email-permissions-s3-iam-role-trust "#receiving-email-permissions-s3-iam-role-trust").

This permission policy must be pasted into the IAM role's inline policy
editor—see [Deliver to S3 bucket action](receiving-email-action-s3.md "receiving-email-action-s3.md") and follow the steps given in the
**IAM role** item. (The following example also includes optional
permissions in case you want to use SNS topic notification, or a customer managed
key in the S3 action.)

###### Note

- You have the option to set up the S3 action without specifying an
  IAM role by allowing just the SES service in the S3 bucket
  policy as shown [Give SES permission to write to
  an S3 bucket](#receiving-email-permissions-s3 "#receiving-email-permissions-s3"). This will
  work for cross-account scenarios as well.
- If you specify an IAM role for the S3 action, SES assumes
  that role for 'PutObject' operation, and the IAM permissions specified
  here will be sufficient for same account usage. However, for cross-account
  usage, you'll need an additional bucket policy that allows the IAM role to
  'PutObject' in the bucket. This is specified by the bucket owner granting
  cross-account bucket permissions as explained in [Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/userguide/example-walkthroughs-managing-access-example2.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3Access",
 "Effect": "Allow",
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 },
 {
 "Sid": "SNSAccess",
 "Effect": "Allow",
 "Action": "sns:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`my-topic`"
 },
 {
 "Sid": "KMSAccess",
 "Effect": "Allow",
 "Action": "kms:GenerateDataKey*",
 "Resource": "arn:aws:kms:`us-east-1`::`111122223333`:key/`key-id`"
 }
 ]
}`

```

Make the following changes to the preceding policy example:

- Replace `amzn-s3-demo-bucket` with the name of the
  S3 bucket that you want to write to.
- Replace `region` with the AWS Region where you
  created the receipt rule.
- Replace `111122223333` with your AWS
  account ID.
- Replace `my-topic` with the name of the SNS
  topic that you want to publish notifications to.
- Replace `key-id` with the ID of your
  KMS key.

### Trust policy for

S3 action IAM role

The following trust policy should be added into the _Trust
relationships_ of the IAM role to allow SES to assume that
role.

###### Note

The manual addition of this trust policy is only required if you did not
create your IAM role from the SES console using the steps given in the
**IAM role** item of the [Deliver to S3 bucket action](receiving-email-action-s3.md "receiving-email-action-s3.md") workflow. _When you
create the IAM role from the console, this trust policy is automatically
generated and applied to the role for you making this step
unnecessary._

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSESAssume",
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount":"`111122223333`",
 "AWS:SourceArn": "arn:aws:ses:`region`:`111122223333`:receipt-rule-set/`rule_set_name`:receipt-rule/`receipt_rule_name`"
 }
 }
 }
 ]
}`

```

Make the following changes to the preceding policy example:

- Replace `region` with the AWS Region where you
  created the receipt rule.
- Replace `111122223333` with your AWS
  account ID.
- Replace `rule_set_name` with the name of the rule
  set that contains the receipt rule that contains the deliver to Amazon S3 bucket
  action.
- Replace `receipt_rule_name` with the name of the
  receipt rule that contains the deliver to Amazon S3 bucket action.

## Give SES permission to write to

an S3 bucket

When you apply the following policy to an S3 bucket, it gives SES
permission to write to that bucket as long as it exists in a region where SES
[Email receiving](../../../general/latest/gr/ses.md#ses_inbound_endpoints "../../../general/latest/gr/ses.md#ses_inbound_endpoints") is
available—if you want to write to a bucket outside of an _Email
receiving_ region, see [Setting up IAM role
permissions for Deliver to S3 bucket action](#receiving-email-permissions-s3-iam-role "#receiving-email-permissions-s3-iam-role"). For more information
about creating receipt rules that transfer incoming email to Amazon S3, see [Deliver to S3 bucket action](receiving-email-action-s3.md "receiving-email-action-s3.md").

For more information about attaching policies to S3 buckets, see [Using Bucket Policies and User
Policies](../../../AmazonS3/latest/userguide/using-iam-policies.md "../../../AmazonS3/latest/userguide/using-iam-policies.md") in the _Amazon Simple Storage Service User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AllowSESPuts",
 "Effect":"Allow",
 "Principal":{
 "Service":"ses.amazonaws.com"
 },
 "Action":"s3:PutObject",
 "Resource":"arn:aws:s3:::`amzn-s3-demo-bucket`/*",
 "Condition":{
 "StringEquals":{
 "AWS:SourceAccount":"`111122223333`",
 "AWS:SourceArn": "arn:aws:ses:`region`:`111122223333`:receipt-rule-set/`rule_set_name`:receipt-rule/`receipt_rule_name`"
 }
 }
 }
 ]
}`

```

Make the following changes to the preceding policy example:

- Replace `amzn-s3-demo-bucket` with the name of the
  S3 bucket that you want to write to.
- Replace `region` with the AWS Region where you
  created the receipt rule.
- Replace `111122223333` with your AWS
  account ID.
- Replace `rule_set_name` with the name of the rule set
  that contains the receipt rule that contains the deliver to Amazon S3 bucket
  action.
- Replace `receipt_rule_name` with the name of the
  receipt rule that contains the deliver to Amazon S3 bucket action.

## Give SES permission to use your

AWS KMS key

In order for SES to encrypt your emails, it must have permission to use the
AWS KMS key that you specified when you set up your receipt rule. You can either use the
default KMS key (**aws/ses**) in your account, or use a customer
managed key that you create. If you use the default KMS key, you don't need to perform
any additional steps to give SES permission to use it. If you use a customer
managed key, you need to give SES permission to use it by adding a statement to
the key's policy.

Use the following policy statement as the key policy to allow SES to use your
customer managed key when it receives email on your domain.

```
{
  "Sid": "AllowSESToEncryptMessagesBelongingToThisAccount",
  "Effect": "Allow",
  "Principal": {
    "Service":"ses.amazonaws.com"
  },
  "Action": [
    "kms:GenerateDataKey*"
  ],
  "Resource": "*",
  "Condition":{
        "StringEquals":{
          "AWS:SourceAccount":"`111122223333`",
          "AWS:SourceArn": "arn:aws:ses:`region`:`111122223333`:receipt-rule-set/`rule_set_name`:receipt-rule/`receipt_rule_name`"
        }
      }
}
```

Make the following changes to the preceding policy example:

- Replace `region` with the AWS Region where you
  created the receipt rule.
- Replace `111122223333` with your AWS
  account ID.
- Replace `rule_set_name` with the name of the rule set
  that contains the receipt rule that you've associated with email
  receiving.
- Replace `receipt_rule_name` with the name of the
  receipt rule that you've associated with email receiving.

If you're using AWS KMS to send encrypted messages to an S3 bucket with
server-side encryption enabled, then you need to add the policy action,
`"kms:Decrypt"`. Using the preceding example, adding this action to your
policy would appear as follows:

```
{
  "Sid": "AllowSESToEncryptMessagesBelongingToThisAccount",
  "Effect": "Allow",
  "Principal": {
    "Service":"ses.amazonaws.com"
  },
  "Action": [
    "kms:Decrypt",
    "kms:GenerateDataKey*"
  ],
  "Resource": "*",
  "Condition":{
        "StringEquals":{
          "AWS:SourceAccount":"`111122223333`",
          "AWS:SourceArn": "arn:aws:ses:`region`:`111122223333`:receipt-rule-set/`rule_set_name`:receipt-rule/`receipt_rule_name`"
        }
      }
}
```

For more
information about attaching policies to AWS KMS keys, see [Using Key Policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

## Give SES permission to

invoke a AWS Lambda function

To enable SES to call a AWS Lambda function, you can choose the function when
you create a receipt rule in the SES console. When you do, SES
automatically adds the necessary permissions to the function.

Alternatively, you can use the `AddPermission` operation in the AWS Lambda
API to attach a policy to a function. The following call to the
`AddPermission` API gives SES permission to invoke your Lambda
function.
For more information about attaching policies to
Lambda functions, see [AWS Lambda
Permissions](../../../lambda/latest/dg/intro-permission-model.md "../../../lambda/latest/dg/intro-permission-model.md") in the _AWS Lambda Developer Guide_.

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "ses.amazonaws.com",
  "SourceAccount": "`111122223333`",
  "SourceArn": "arn:aws:ses:`region`:`111122223333`:receipt-rule-set/`rule_set_name`:receipt-rule/`receipt_rule_name`",
  "StatementId": "GiveSESPermissionToInvokeFunction"
}
```

Make the following changes to the preceding policy example:

- Replace `region` with the AWS Region where you
  created the receipt rule.
- Replace `111122223333` with your AWS
  account ID.
- Replace `rule_set_name` with the name of the rule set
  that contains the receipt rule where you created your Lambda function.
- Replace `receipt_rule_name` with the name of the
  receipt rule containing your Lambda function.

## Give SES permission to publish

to an Amazon SNS topic that belongs to a different AWS account

To publish notifications to a topic in a separate AWS account, you must attach a
policy to the Amazon SNS topic. The SNS topic must be in the same Region as the domain and
receipt rule set.

The following policy gives SES permission to publish to an Amazon SNS topic in a
separate AWS account.

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
 "Action": "SNS:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`topic_name`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`444455556666`",
 "AWS:SourceArn": "arn:aws:ses:`us-east-1`:`777788889999`:receipt-rule-set/`rule_set_name`:receipt-rule/`rule_name`"
 }
 }
 }
 ]
}`

```

Make the following changes to the preceding policy example:

- Replace `topic_region` with the AWS Region that the
  Amazon SNS topic was created in.
- Replace `sns_topic_account_id` with the ID of the
  AWS account that owns the Amazon SNS topic.
- Replace `topic_name` with the name of the Amazon SNS topic
  that you want to publish notifications to.
- Replace `aws_account_id` with the ID of the AWS
  account that is configured to receive email.
- Replace `receipt_region` with the AWS Region where
  you created the receipt rule.
- Replace `rule_set_name` with the name of the rule set
  that contains the receipt rule where you created your publish to Amazon SNS topic
  action.
- Replace `receipt_rule_name` with the name of the
  receipt rule containing the publish to Amazon SNS topic action.

If your Amazon SNS topic uses AWS KMS for server-side encryption, you have to add permissions
to the AWS KMS key policy. You can add permissions by attaching the following policy to
the AWS KMS key policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSESToUseKMSKey",
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```
