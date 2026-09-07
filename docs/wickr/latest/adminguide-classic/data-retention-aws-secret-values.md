

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Secrets Manager values for AWS Wickr
<a name="data-retention-aws-secret-values"></a>

You can use Secrets Manager to store the data retention bot credentials and AWS service information. For more information about creating a Secrets Manager secret, see [Create an AWS Secrets Manager secret ](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the *Secrets Manager User Guide*.

The Secrets Manager secret can have the following values:
+ `password` – The data retention bot password.
+ `s3_bucket_name` – The name of the Amazon S3 bucket where messages and files will be stored. If not set, the default file streaming will be used.
+ `s3_region` – The AWS Region of the Amazon S3 bucket where messages and files will be stored.
+ `s3_folder_name` – The optional folder name in the Amazon S3 bucket where messages and files will be stored. This folder name will be preceded with the key for messages and files saved to the Amazon S3 bucket.
+ `kms_master_key_arn` – The ARN of the AWS KMS master key used to re-encrypt the message files and files on the data retention bot before they are saved to the Amazon S3 bucket.
+ `kms_region` – The AWS Region where the AWS KMS master key is located.
+ `sns_topic_arn` – The ARN of the Amazon SNS topic that you want data retention events sent to.