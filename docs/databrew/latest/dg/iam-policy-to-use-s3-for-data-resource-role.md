

# IAM policy to use Amazon S3 objects with DataBrew
<a name="iam-policy-to-use-s3-for-data-resource-role"></a>

The `AwsGlueDataBrewSpecificS3BucketPolicy` policy grants the permissions needed to access S3 on behalf of nonadministrative users.

Customize the policy as follows:

1. Replace the Amazon S3 paths in the policy so they point to the paths that you want to use. In the sample text, {{`BUCKET-NAME-1/SPECIFIC-OBJECT-NAME`}} represents a specific object or file. {{`BUCKET-NAME-2/`}} represents all objects (`*`) whose path name starts with `BUCKET-NAME-2/`. Update these to name the buckets that you are using.

1. (Optional) Use wildcards in the Amazon S3 paths to further restrict permissions. For more information, see [IAM policy elements: Variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*. 

    **Security Best Practice**: To prevent unauthorized access to Amazon S3 buckets with similar names in other AWS accounts, include the `aws:ResourceAccount` condition key in your policy. This ensures that DataBrew can only access buckets within your own AWS account, even when using wildcard resource ARNs. Add the following condition to your policy statements: 

   ```
   "Condition": {
   "StringEquals": {
   "aws:ResourceAccount": "123456789012"
   }
   }
   ```

    Replace `123456789012` with your actual AWS account ID. 

   As part of doing this, you might restrict permissions for the actions `s3:PutObject` and `s3:PutBucketCORS`. These actions are required only for users who create DataBrew projects, because those users need to be able to send output files to S3. 

For more information and to see some examples of what you can add to an IAM policy for Amazon S3, see [Bucket Policy Examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html) in the *Amazon S3 Developer Guide.*

The following table describes the permissions granted by this policy.


|  **Action**  |  **Resource**  |  **Description**  | 
| --- | --- | --- | 
|  `"s3:GetObject"`  |  `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"`  | Allows you to preview your files. | 
|  `"s3:PutObject"` <br /> `"s3:PutBucketCORS"`  |  `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"`  | Allows sending output files to S3. | 
|  `"s3:DeleteObject"`  |  `"arn:aws:s3:::bucket_name/*", "arn:aws:s3:::bucket_name"`  | Allows deleting an object.  | <a name="AwsGlueDataBrewSpecificS3BucketPolicy-console-steps"></a>

**To define the AwsGlueDataBrewSpecificS3BucketPolicy IAM policy for DataBrew (console)**

1. Download the JSON for the [`AwsGlueDataBrewSpecificS3BucketPolicy`](samples/AwsGlueDataBrewSpecificS3BucketPolicy.json.zip) IAM policy. 

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). 

1. In the navigation pane, choose **Policies**.

1. For each policy, choose **Create Policy**.

1. On the **Create Policy** screen, navigate to the **JSON** tab. 

1. Paste in the policy JSON statement over the sample statement in the editor.

1. Verify that the policy is customized to your account, security requirements, and required AWS resources. If you need to make changes, you can make them in the editor.

1. Choose **Review policy**.<a name="AwsGlueDataBrewSpecificS3BucketPolicy-cli-steps"></a>

**To define the AwsGlueDataBrewSpecificS3BucketPolicy IAM policy for DataBrew (AWS CLI)**

1. Download the JSON for [`AwsGlueDataBrewSpecificS3BucketPolicy`](samples/AwsGlueDataBrewSpecificS3BucketPolicy.json.zip). 

1. Customize the policy as described in the first step of the previous procedure.

1. Run the following command to create the policy.

   ```
   aws iam create-policy --policy-name AwsGlueDataBrewSpecificS3BucketPolicy --policy-document file://iam-policy-AwsGlueDataBrewSpecificS3BucketPolicy.json
   ```