# IAM policy to use encryption

with DataBrew

The `AwsGlueDataBrewS3EncryptedPolicy` policy grants the permissions needed
to access S3 objects encrypted with AWS Key Management Service (AWS KMS) on behalf of nonadministrative users.

Customize the policy as follows:

1. Replace the Amazon S3 paths in the policy so that they point to the paths you want to
   use. In the sample text,
   `BUCKET-NAME-1/SPECIFIC-OBJECT-NAME`
   represents a specific object or file.
   `BUCKET-NAME-2/` represents all objects
   (`*`) whose path name starts with `BUCKET-NAME-2/`. Update
   these to name the buckets you are using.
2. (Optional) Use wildcards in the Amazon S3 paths to further restrict permissions. For
   more information, see [IAM policy elements: Variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md").

As part of doing this, you might restrict permissions for the actions
`s3:PutObject` and `s3:PutBucketCORS`. These actions are
required only for users who create DataBrew projects, because those users need to be
able to send output files to S3.

For more information and to see some examples of what you can add to an IAM
policy for Amazon S3, see [Bucket
Policy Examples](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md"). 3. Find the following resource ARNs in the `ToUseKms`
file.

```
  "arn:aws:kms:`AWS-REGION-NAME`:`AWS-ACCOUNT-ID-WITHOUT-DASHES`:key/`KEY-IDS`",
"arn:aws:kms:`AWS-REGION-NAME`:`AWS-ACCOUNT-ID-WITHOUT-DASHES`:key/`KEY-IDS`"
```

4. Change the example AWS account to your AWS account number (without
   hyphens).
5. Change the sample list to instead list the IAM roles you want to use. We
   recommend scoping your IAM policies to the smallest permissions set possible.
   However, you can allow your user to access all IAM roles, for example if you are
   using a personal learning account with sample data. To allow the list to access
   all IAM roles, change the sample list to one entry:
   `"arn:aws:iam::`111122223333`:role/*"`.
   The following table describes the permissions granted by this policy.

| **Action**               | **Resource**                                               | **Description**                                                        |
| ------------------------ | ---------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `"s3:GetObject"`         | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows you to preview your files.                                      |
| `"s3:ListBucket"`        | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows listing of Amazon S3 buckets from projects, datasets, and jobs. |
| `"s3:PutObject"`         | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows sending output files to S3.                                     |
| `"s3:DeleteObject"`      | `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"` | Allows deleting an object created by DataBrew.                         |
| `"kms:Decrypt"`          | `"arn:aws:kms:::key/key_ids"`                              | Allows decrypting for encrypted datasets.                              |
| `"kms:GenerateDataKey*"` | `"arn:aws:kms:::key/key_ids"`                              | Allows encrypting of job output.                                       | ###### To define the AwsGlueDataBrewS3EncryptedPolicy IAM policy for DataBrew (console) 1. Download the JSON for the [`AwsGlueDataBrewS3EncryptedPolicy`](samples/AwsGlueDataBrewS3EncryptedPolicy.json.md "samples/AwsGlueDataBrewS3EncryptedPolicy.json.md") IAM policy. 2. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). 3. In the navigation pane, choose **Policies**. 4. For each policy, choose **Create Policy**. 5. On the **Create Policy** screen, navigate to the **JSON** tab. 6. Paste in the policy JSON statement over the sample statement in the editor. 7. Verify that the policy is customized to your account, security requirements, and required AWS resources. If you need to make changes, you can make them in the editor. 8. Choose **Review policy**. ###### To define the AwsGlueDataBrewS3EncryptedPolicy IAM policy for DataBrew (AWS CLI) 1. Download the JSON for [`AwsGlueDataBrewS3EncryptedPolicy`](samples/AwsGlueDataBrewS3EncryptedPolicy.json.md "samples/AwsGlueDataBrewS3EncryptedPolicy.json.md"). 2. Customize the policy as described in the first step of the previous procedure. 3. Run the following command to create the policy. `aws iam create-policy --policy-name AwsGlueDataBrewS3EncryptedPolicy --policy-document file://iam-policy-AwsGlueDataBrewS3EncryptedPolicy.json` |
