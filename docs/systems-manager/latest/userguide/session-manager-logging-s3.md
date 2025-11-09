AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Logging session data using Amazon S3

(console)

You can choose to store session log data in a specified Amazon Simple Storage Service (Amazon S3) bucket for
debugging and troubleshooting purposes. The default option is for logs to be sent to
an encrypted Amazon S3 bucket. Encryption is performed using the key specified for the
bucket, either an AWS KMS key or an Amazon S3 Server-Side Encryption (SSE) key
(AES-256).

###### Important

When you use virtual hosted–style buckets with Secure Sockets Layer (SSL), the
SSL wildcard certificate only matches buckets that don't contain periods. To
work around this, use HTTP or write your own certificate verification logic. We
recommend that you don't use periods (".") in bucket names when using virtual
hosted–style buckets.

###### Amazon S3 bucket encryption

In order to send logs to your Amazon S3 bucket with encryption, encryption must be
allowed on the bucket. For more information about Amazon S3 bucket encryption, see
[Amazon S3 Default Encryption for S3 Buckets](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md").

###### Customer managed key

If you're using a KMS key that you manage yourself to encrypt your bucket,
then the IAM instance profile attached to your instances must have explicit
permissions to read the key. If you use an AWS managed key, the instance
doesn't require this explicit permission. For more information about providing
the instance profile with access to use the key, see [Allows Key Users to Use the key](../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users "../../../kms/latest/developerguide/key-policies.md#key-policy-default-allow-users") in the
_AWS Key Management Service Developer Guide_.

Follow these steps to configure Session Manager to store session logs in an Amazon S3
bucket.

###### Note

You can also use the AWS CLI to specify or change the Amazon S3 bucket that session
data is sent to. For information, see [Update Session Manager
preferences (command line)](getting-started-configure-preferences-cli.md "getting-started-configure-preferences-cli.md").

###### To log session data using Amazon S3 (console)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Session Manager**.
3. Choose the **Preferences** tab, and then choose
   **Edit**.
4. Select the check box next to **Enable** under
   **S3 logging**.
5. (Recommended) Select the check box next to **Allow only encrypted
   S3 buckets**. With this option turned on, log data is encrypted
   using the server-side encryption key specified for the bucket. If you don't
   want to encrypt the log data that is sent to Amazon S3, clear the check box. You
   must also clear the check box if encryption isn't allowed on the S3
   bucket.
6. For **S3 bucket name**, select one of the
   following:

###### Note

We recommend that you don't use periods (".") in bucket names when
using virtual hosted–style buckets. For more information about Amazon S3
bucket-naming conventions, see [Bucket Restrictions and Limitations](../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules "../../../AmazonS3/latest/dev/BucketRestrictions.md#bucketnamingrules") in the _Amazon Simple Storage Service User Guide_.

    * **Choose a bucket name from the list**: Select an
     Amazon S3 bucket that has already been created in your account to store
     session log data.
    * **Enter a bucket name in the text box**: Enter
     the name of an Amazon S3 bucket that has already been created in your
     account to store session log data.

7. (Optional) For **S3 key prefix**, enter the name of an
   existing or new folder to store logs in the selected bucket.
8. Choose **Save**.
   For more information about working with Amazon S3 and Amazon S3 buckets, see the
   _[Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")_ and the
   _[Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")_.
