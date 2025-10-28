# Deliver to S3 bucket action

The **Deliver to S3 bucket** action delivers the mail to an
S3 bucket and can optionally notify you through SNS and more. This action has
the following options.

- S3 bucket – The name of the S3
  bucket to which to save received emails. You can also create a new S3 bucket
  when you set up your action by choosing **Create S3 Bucket**. Amazon SES
  provides you the raw, unmodified email, which is typically in Multipurpose Internet
  Mail Extensions (MIME) format. For more information about MIME format, see [RFC 2045](https://tools.ietf.org/html/rfc2045 "https://tools.ietf.org/html/rfc2045").

###### Important

    + The Amazon S3 bucket must exist in a region where SES [Email receiving](regions.md#region-receive-email "regions.md#region-receive-email") is available; otherwise, you must
     use the IAM role option explained below.
    + When you save your emails to an S3 bucket, the default maximum
     email size (including headers) is 40 MB.
    + SES does not support receipt rules that upload to S3
     buckets enabled with object lock configured with a default retention
     period.
    + If applying encryption on your S3 bucket by specifying your own
     KMS key, be sure to use the fully qualified KMS key ARN, and not the KMS
     key alias; using the alias can result in data encrypted with a KMS key
     that belongs to the requester, and not the bucket administrator. See
     [Using encryption for cross-account operations](../../../AmazonS3/latest/userguide/bucket-encryption.md#bucket-encryption-update-bucket-policy "../../../AmazonS3/latest/userguide/bucket-encryption.md#bucket-encryption-update-bucket-policy").

- Object key prefix – An optional key name
  prefix to use within the S3 bucket. Key name prefixes enable you to organize
  your S3 bucket in a folder structure. For example, if you use
  _Email_ as your **Object key prefix**, your
  emails will appear in your S3 bucket in a folder named
  _Email_.
- Message encryption – The option to encrypt
  received email messages before delivering them to your S3 bucket.
- KMS encryption key – (Available if
  _Message encryption_ is selected.) The AWS KMS key that
  SES should use to encrypt your emails before saving them to the S3
  bucket. You can use the default KMS key or a customer managed key that you created
  in KMS.

###### Note

The KMS key you choose must be in the same AWS region as the SES
endpoint you use to receive email.

    + To use the default KMS key, choose **aws/ses** when you
     set up the receipt rule in the SES console. If you use the SES
     API, you can specify the default KMS key by providing an ARN in the form of
     `arn:aws:kms:REGION:AWSACCOUNTID:alias/aws/ses`. For example,
     if your AWS account ID is 123456789012 and you want to use the default KMS
     key in the us-east-1 region, the ARN of the default KMS key would
     be
     `arn:aws:kms:us-east-1:123456789012:alias/aws/ses`.
     If you use the default KMS key, you don't need to perform any extra steps to
     give SES permission to use the key.
    + To use a customer managed key that you created in KMS, provide the ARN of
     the KMS key and ensure that you add a statement to your key's policy to give
     SES permission to use it. For more information about giving
     permissions, see [Giving permissions to Amazon SES for email
     receiving](receiving-email-permissions.md "receiving-email-permissions.md").

For more information about using KMS with SES, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/services-ses.md "../../../kms/latest/developerguide/services-ses.md"). If you do not
specify a KMS key in the console or API, SES will not encrypt your
emails.

###### Important

Your mail is encrypted by SES using the S3 encryption client
before the mail is submitted to S3 for storage. It is not encrypted using
S3 server-side encryption. This means that you must use the S3
encryption client to decrypt the email after retrieving it from S3, as
the service has no access to use your KMS keys for decryption. This encryption
client is available in the [AWS SDK for Java](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/") and the [AWS SDK for Ruby](https://aws.amazon.com/sdk-for-ruby/ "https://aws.amazon.com/sdk-for-ruby/"). For more information, see the [Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md "../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md").

- IAM role – An IAM role used by
  SES to access the resources in the _Deliver to S3_
  action (Amazon S3 bucket, SNS topic, and KMS key). If not provided, you'll need to
  explicitly give permissions to SES to access each resource
  individually—see [Giving permissions to Amazon SES for email
  receiving](receiving-email-permissions.md "receiving-email-permissions.md").

If you want to write to an S3 bucket that exists in a region where
SES _Email receiving_ isn't available, you must use an
IAM role that has the write to S3 permission policy as an inline policy of
the role. You can apply the permission policy for this action directly from the
console:

    1. Choose **Create new role** in the **IAM
     role** field and enter a name followed by **Create
     role**. (The IAM trust policy for this role will
     automatically be generated in the background.)
    2. Because the IAM trust policy was automatically generated, you'll only
     need to add the action's permission policy to the
     role—select **View role** under the
     **IAM role** field to open the IAM console.
    3. Under the **Permissions** tab, choose **Add
     permissions** and select **Create inline
     policy**.
    4. On the **Specify permissions** page, select
     **JSON** in the **Policy
     editor**.
    5. Copy and paste the permission policy from [IAM role
     permissions for S3 action](receiving-email-permissions.md#receiving-email-permissions-s3-iam-role "receiving-email-permissions.md#receiving-email-permissions-s3-iam-role") into the
     **Policy editor** and replace the data in red text with
     your own. (Be sure to delete any example code in the editor.)
    6. Choose **Next**.
    7. Review and create your permission policy for the IAM role by choosing
     **Create policy**.
    8. Select your browser's tab where you have the SES **Create
     rule**–**Add actions** page open and
     continue with the remaining steps for creating rules.

- SNS topic – The name or ARN of the Amazon SNS
  topic to notify when an email is saved to the S3 bucket. An example of an
  SNS topic ARN is
  _arn:aws:sns:us-east-1:123456789012:MyTopic_.
  You can also create an SNS topic when you set up your action by choosing
  **Create SNS Topic**. For more information about SNS
  topics, see the [Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg/CreateTopic.md "../../../sns/latest/dg/CreateTopic.md").

###### Note

    + The SNS topic you choose must be in the same AWS region as
     the SES endpoint you use to receive email.
    + Only use *customer managed* KMS key encryption
     with SNS topics you associate with SES receipt rules as
     you will be required to edit the KMS key policy to allow SES to
     publish to SNS. This is in contrast with *AWS
     managed* KMS key policies which cannot be edited by
     design.
