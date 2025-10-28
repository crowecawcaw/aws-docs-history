# IAM policy to use Amazon S3 objects with

DataBrew

The `AwsGlueDataBrewSpecificS3BucketPolicy` policy grants the permissions
needed to access S3 on behalf of nonadministrative users.

Customize the policy as follows:

1. Replace the Amazon S3 paths in the policy so they point to the paths that you want to
   use. In the sample text,
   `BUCKET-NAME-1/SPECIFIC-OBJECT-NAME`
   represents a specific object or file.
   `BUCKET-NAME-2/` represents all objects
   (`*`) whose path name starts with `BUCKET-NAME-2/`. Update
   these to name the buckets that you are using.
2. (Optional) Use wildcards in the Amazon S3 paths to further restrict permissions. For
   more information, see [IAM policy elements: Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the
   _IAM User Guide_.

**Security Best Practice**: To prevent unauthorized access to Amazon S3 buckets with similar names in
other AWS accounts, include the `aws:ResourceAccount` condition key in your policy. This ensures that
DataBrew can only access buckets within your own AWS account, even when using wildcard resource ARNs. Add the following
condition to your policy statements:

```
"Condition": {
"StringEquals": {
"aws:ResourceAccount": "123456789012"
}
}
```

Replace `123456789012` with your actual AWS account ID.

As part of doing this, you might restrict permissions for the actions
`s3:PutObject` and `s3:PutBucketCORS`. These actions are
required only for users who create DataBrew projects, because those users need to be
able to send output files to S3.
For more information and to see some examples of what you can add to an IAM policy for
Amazon S3, see [Bucket Policy
Examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md") in the _Amazon S3 Developer Guide._

The following table describes the permissions granted by this policy.

| **Action**                            | **Resource**                                               | **Description**                    |
| ------------------------------------- | ---------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"s3:GetObject"`                      | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows you to preview your files.  |
| `"s3:PutObject"` `"s3:PutBucketCORS"` | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows sending output files to S3. |
| `"s3:DeleteObject"`                   | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows deleting an object.         | ###### To define the AwsGlueDataBrewSpecificS3BucketPolicy IAM policy for DataBrew (console) 1. Download the JSON for the [`AwsGlueDataBrewSpecificS3BucketPolicy`](samples/AwsGlueDataBrewSpecificS3BucketPolicy.json.md "samples/AwsGlueDataBrewSpecificS3BucketPolicy.json.md") IAM policy. 2. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). 3. In the navigation pane, choose **Policies**. 4. For each policy, choose **Create Policy**. 5. On the **Create Policy** screen, navigate to the **JSON** tab. 6. Paste in the policy JSON statement over the sample statement in the editor. 7. Verify that the policy is customized to your account, security requirements, and required AWS resources. If you need to make changes, you can make them in the editor. 8. Choose **Review policy**. ###### To define the AwsGlueDataBrewSpecificS3BucketPolicy IAM policy for DataBrew (AWS CLI) 1. Download the JSON for [`AwsGlueDataBrewSpecificS3BucketPolicy`](samples/AwsGlueDataBrewSpecificS3BucketPolicy.json.md "samples/AwsGlueDataBrewSpecificS3BucketPolicy.json.md"). 2. Customize the policy as described in the first step of the previous procedure. 3. Run the following command to create the policy. `aws iam create-policy --policy-name AwsGlueDataBrewSpecificS3BucketPolicy --policy-document file://iam-policy-AwsGlueDataBrewSpecificS3BucketPolicy.json` |
