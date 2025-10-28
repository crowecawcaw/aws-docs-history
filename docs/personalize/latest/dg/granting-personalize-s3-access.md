# Giving Amazon Personalize access to Amazon S3 resources

To give Amazon Personalize access to your Amazon S3 bucket, do the following:

1. If you haven't already, follow the steps in [Setting up permissions](aws-personalize-set-up-permissions.md "aws-personalize-set-up-permissions.md")
   to set up permissions so Amazon Personalize
   can access your resources in Amazon Personalize on your behalf.
2. Attach a policy to the Amazon Personalize service role (see
   [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions"))
   that allows access to your Amazon S3 bucket. For more information, see [Attaching an Amazon S3 policy to your Amazon Personalize service role](#attaching-s3-policy-to-role "#attaching-s3-policy-to-role").
3. Attach a bucket policy to the Amazon S3 bucket containing your data files so Amazon Personalize can access them.
   For more information, see [Attaching an Amazon Personalize access policy to your Amazon S3
   bucket](#attach-bucket-policy "#attach-bucket-policy").
4. If you use AWS Key Management Service (AWS KMS) for encryption, you must grant Amazon Personalize and your Amazon Personalize IAM service role
   permission to use your key. For more information, see [Giving Amazon Personalize permission to use your AWS KMS key](granting-personalize-key-access.md "granting-personalize-key-access.md").

###### Note

Because Amazon Personalize doesn’t communicate with AWS VPCs, Amazon Personalize can't interact with
Amazon S3 buckets that allow only VPC access.

###### Topics

- [Attaching an Amazon S3 policy to your Amazon Personalize service role](#attaching-s3-policy-to-role "#attaching-s3-policy-to-role")
- [Attaching an Amazon Personalize access policy to your Amazon S3
  bucket](#attach-bucket-policy "#attach-bucket-policy")

## Attaching an Amazon S3 policy to your Amazon Personalize service role

To attach an Amazon S3 policy to your Amazon Personalize role do the following:

1. Sign in to the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).
2. In the navigation pane, choose **Policies**, and choose
   **Create policy**.
3. Choose the JSON tab, and update the policy as follows. Replace `amzn-s3-demo-bucket` with the
   name of your bucket. You can use the following policy for dataset import jobs or data deletion jobs.
   If you are using a batch workflow or creating a dataset export job, Amazon Personalize needs additional permissions. See
   [Service role policy for batch workflows](#role-policy-for-batch-workflows "#role-policy-for-batch-workflows") or
   [Amazon S3 bucket policy for exporting a dataset](#bucket-policy-for-export "#bucket-policy-for-export").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PersonalizeS3BucketAccessPolicy",
 "Statement": [
 {
 "Sid": "PersonalizeS3BucketAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

4. Choose **Next: Tags**. Optionally add any tags and choose **Review**.
5. Give the policy a name.
6. (Optional) For **Description**, enter a short sentence describing
   this policy, for example, `Allow Amazon Personalize to access its Amazon S3
bucket.`
7. Choose **Create policy**.
8. In the navigation pane, choose **Roles**, and choose the role you
   created for Amazon Personalize. See [Creating an IAM role for Amazon Personalize](set-up-required-permissions.md#set-up-create-role-with-permissions "set-up-required-permissions.md#set-up-create-role-with-permissions").
9. For **Permissions**, choose
   **Attach policies**.
10. To display the policy in the list, type part of the policy name in the
    **Filter policies** filter box.
11. Choose the check box next to the policy you created earlier in this procedure.
12. Choose **Attach policy**.

Before your role is ready for use with Amazon Personalize you must also attach a bucket policy to the Amazon S3 bucket containing your data. See
[Attaching an Amazon Personalize access policy to your Amazon S3
bucket](#attach-bucket-policy "#attach-bucket-policy").

### Service role policy for batch workflows

To complete a batch worklfow, Amazon Personalize needs permission to access and add files to your Amazon S3 bucket.
Follow the steps above to attach the following policy to your Amazon Personalize role. Replace `amzn-s3-demo-bucket` with the
name of your bucket. For more information on batch workflows, see
[Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PersonalizeS3BucketAccessPolicy",
 "Statement": [
 {
 "Sid": "PersonalizeS3BucketAccessPolicy",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

### Service role policy for exporting a dataset

To export a dataset, your Amazon Personalize service role needs permission to use the `PutObject` and `ListBucket` Actions on your Amazon S3 bucket.
The following example policy grants Amazon Personalize `PutObject` and `ListBucket` permissions.
Replace `amzn-s3-demo-bucket`
with the name of your bucket and attach the policy to your service role for Amazon Personalize. For information about attaching policies to a service role see [Attaching an Amazon S3 policy to your Amazon Personalize service role](#attaching-s3-policy-to-role "#attaching-s3-policy-to-role").

```
{
    "Version": "2012-10-17",
    "Id": "PersonalizeS3BucketAccessPolicy",
    "Statement": [
        {
            "Sid": "PersonalizeS3BucketAccessPolicy",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ]
        }
    ]
}
```

## Attaching an Amazon Personalize access policy to your Amazon S3

bucket

Amazon Personalize needs permission to access the S3 bucket. You can use the following policy for dataset import jobs or data deletion jobs.
Replace `amzn-s3-demo-bucket` with the
name of your bucket. For batch workflows, see
[Amazon S3 bucket policy for batch
workflows](#bucket-policy-for-batch-workflows "#bucket-policy-for-batch-workflows").

For more information on Amazon S3 bucket policies, see [How Do I
Add an S3 Bucket Policy?](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PersonalizeS3BucketAccessPolicy",
 "Statement": [
 {
 "Sid": "PersonalizeS3BucketAccessPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "personalize.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

### Amazon S3 bucket policy for batch

workflows

For batch workflows, Amazon Personalize needs permission to access and add files to your Amazon S3 bucket.
Attach the following policy to your
bucket. Replace `amzn-s3-demo-bucket` with the
name of your bucket.

For more information on adding an Amazon S3 bucket policy to a bucket, see [How Do I
Add an S3 Bucket Policy?](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md"). For more information on batch workflows, see
[Getting batch item recommendations](getting-batch-recommendations.md "getting-batch-recommendations.md") or [Getting batch user segments](getting-user-segments.md "getting-user-segments.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "PersonalizeS3BucketAccessPolicy",
 "Statement": [
 {
 "Sid": "PersonalizeS3BucketAccessPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "personalize.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

### Amazon S3 bucket policy for exporting a dataset

To export a dataset, Amazon Personalize needs permission to use the `PutObject` and `ListBucket` Actions on your Amazon S3 bucket.
The following example policy grants the Amazon Personalize principle `PutObject` and `ListBucket` permissions.
Replace `amzn-s3-demo-bucket` with the name of your bucket and attach the policy to your bucket.
For information on adding an Amazon S3 bucket policy to a bucket, see
[How Do I Add an S3 Bucket Policy?](../../../AmazonS3/latest/user-guide/add-bucket-policy.md "../../../AmazonS3/latest/user-guide/add-bucket-policy.md") in the
Amazon Simple Storage Service User Guide.

```
{
    "Version": "2012-10-17",
    "Id": "PersonalizeS3BucketAccessPolicy",
    "Statement": [
        {
            "Sid": "PersonalizeS3BucketAccessPolicy",
            "Effect": "Allow",
            "Principal": {
                "Service": "personalize.amazonaws.com"
            },
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ]
        }
    ]
}

```
