# Receiving CloudTrail log files from multiple accounts

You can have CloudTrail deliver log files from multiple AWS accounts into a single Amazon S3
bucket. For example, you have four AWS accounts with account IDs
111111111111, 222222222222, 333333333333, and
444444444444, and you want to configure CloudTrail to deliver log files from all
four of these accounts to a bucket belonging to account 111111111111. To
accomplish this, complete the following steps in order:

1. Create a trail in the account where the destination bucket will belong
   (111111111111 in this example). Do not create a trail for any other accounts
   yet.

For instructions, see [Creating a trail with the console](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console"). 2. Update the bucket policy on your destination bucket to grant cross-account
permissions to CloudTrail.

For instructions, see [Setting bucket policy for multiple accounts](cloudtrail-set-bucket-policy-for-multiple-accounts.md "cloudtrail-set-bucket-policy-for-multiple-accounts.md"). 3. Create a trail in the other accounts (222222222222,
333333333333, and 444444444444 in this example) for which you want to log activity. When you create the trail in each account, specify the Amazon S3 bucket belonging to the account that you specified
in step 1 (111111111111 in this example). For instructions, see [Create trails in additional accounts](turn-on-cloudtrail-in-additional-accounts.md "turn-on-cloudtrail-in-additional-accounts.md").

###### Note

If you choose to enable SSE-KMS encryption, the KMS key policy must allow CloudTrail
to use the key to encrypt your log files and digest files,
and allow the users you specify to read log files or digest files in unencrypted form.
For information about manually editing the key policy, see [Configure AWS KMS key policies for CloudTrail](create-kms-key-policy-for-cloudtrail.md "create-kms-key-policy-for-cloudtrail.md").

## Redacting bucket owner account IDs

for data events called by other accounts

Historically, if CloudTrail data events were enabled in the AWS account of an Amazon S3 data
event API caller, CloudTrail showed the account ID of the S3 bucket owner in the data event
(such as `PutObject`). This occurred even if the bucket owner account did not
have S3 data events enabled.

Now, CloudTrail removes the account ID of the S3 bucket owner in the `resources`
block if both of the following conditions are met:

- The data event API call is from a different AWS account than the Amazon S3 bucket
  owner.
- The API caller received an `AccessDenied` error that was only for
  the caller account.

The owner of the resource on which the API call was made still receives the full
event.

The following event record snippets are an example of the expected behavior. In the
`Historic` snippet, the account ID 123456789012 of the S3
bucket owner is shown to an API caller from a different account. In the example of
current behavior, the account ID of the bucket owner is not shown.

```
# Historic

"resources": [
    {
        "type": "AWS::S3::Object",
        "ARNPrefix": "arn:aws:s3:::amzn-s3-demo-bucket2/"
    },
    {
        "accountId": "123456789012",
        "type": "AWS::S3::Bucket",
        "ARN": "arn:aws:s3:::amzn-s3-demo-bucket2"
    }
]
```

The following is the current behavior.

```
# Current

"resources": [
    {
        "type": "AWS::S3::Object",
        "ARNPrefix": "arn:aws:s3:::amzn-s3-demo-bucket2/"
    },
    {
        "accountId": "",
        "type": "AWS::S3::Bucket",
        "ARN": "arn:aws:s3:::amzn-s3-demo-bucket2"
    }
]
```

###### Topics

- [Setting bucket policy for multiple accounts](cloudtrail-set-bucket-policy-for-multiple-accounts.md "cloudtrail-set-bucket-policy-for-multiple-accounts.md")
- [Create trails in additional accounts](turn-on-cloudtrail-in-additional-accounts.md "turn-on-cloudtrail-in-additional-accounts.md")
