**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Migrating a protection pack (web ACL): automated migration

###### To automatically migrate a protection pack (web ACL) configuration from AWS WAF Classic to AWS WAF

1. Sign in to the AWS Management Console and open the AWS WAF console at
   [https://console.aws.amazon.com/wafv2/homev2](https://console.aws.amazon.com/wafv2/homev2 "https://console.aws.amazon.com/wafv2/homev2").
2. Choose **Switch to AWS WAF Classic** and review your configuration
   settings for the protection pack (web ACL). Make note of the settings, considering the caveats and
   limitations described in the preceding section, [Migration caveats and limitations](waf-migrating-caveats.md "waf-migrating-caveats.md").
3. In the informational dialogue at the top,
   locate the sentence that starts with **Migrate protection packs (web ACLs)** and choose the link to the **migration wizard**. This launches the migration wizard.

If you don't see the informational dialogue, you might have closed it since you launched the AWS WAF Classic console. In the navigation bar, choose **Switch to new AWS WAF** then choose **Switch to AWS WAF Classic**, and the informational dialogue should reappear. 4. Select the protection pack (web ACL) that you want to migrate. 5. For **Migration configuration**, provide an Amazon S3 bucket to use for the
template. You need an Amazon S3 bucket that's configured properly for the
migration API, to store the AWS CloudFormation template that it generates.

    * If the bucket is encrypted, the encryption must use Amazon S3 (SSE-S3) keys. The migration doesn't support encryption with AWS Key Management Service (SSE-KMS) keys.
    * The bucket name must start with `aws-waf-migration-`. For example,
     `aws-waf-migration-my-web-acl`.
    * The bucket must be in the Region where you are deploying the template. For example, for
     a protection pack (web ACL) in `us-west-2`, you must use an Amazon S3 bucket in
     `us-west-2` and you must deploy the template stack to
     `us-west-2`.

6. For **S3 bucket policy**, we recommend choosing **Auto apply the
   bucket policy required for migration**. Alternatively, if you want
   to manage the bucket on your own, you must manually apply the following bucket
   policy:
   - For global Amazon CloudFront applications (`waf`):

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "apiv2migration.waf.amazonaws.com"
    },
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::<BUCKET_NAME>/AWSWAF/<CUSTOMER_ACCOUNT_ID>/*"
    }
    ]
   }`

   ```

   - For regional Amazon API Gateway or Application Load Balancer applications (`waf-regional`):

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "apiv2migration.waf-regional.amazonaws.com"
    },
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::<BUCKET_NAME>/AWSWAF/<CUSTOMER_ACCOUNT_ID>/*"
    }
    ]
   }`

   ```

7. For **Choose how to handle rules that cannot be migrated**, choose either
   to exclude rules that can't be migrated, or to stop the migration. For
   information about rules that can't be migrated, see [Migration caveats and limitations](waf-migrating-caveats.md "waf-migrating-caveats.md").
8. Choose **Next**.
9. For **Create AWS CloudFormation template**, verify your settings, then
   choose **Start creating AWS CloudFormation template** to begin the
   migration process. This can take a few minutes, depending on the complexity of
   your protection pack (web ACL).
10. In **Create and run AWS CloudFormation stack to complete migration**, you
    can choose to go to the AWS CloudFormation console to create a stack from the
    template, to create the new protection pack (web ACL) and its resources. To do this, choose
    **Create AWS CloudFormation stack**.
    After the automatic migration process completes, you're ready to proceed to the manual follow-up steps. See [Migrating a protection pack (web ACL): manual follow-up](waf-migrating-procedure-manual-finish.md "waf-migrating-procedure-manual-finish.md").
