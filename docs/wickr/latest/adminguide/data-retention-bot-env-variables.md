This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Environment variables to configure

data retention bot in AWS Wickr

You can use the following environment variables to configure the data retention bot.
You set these environment variables using the `-e` option when you run the
data retention bot Docker image. For more information, see [Start the data retention bot for your Wickr network](starting-data-retention-bot.md "starting-data-retention-bot.md").

###### Note

These environment variables are optional unless otherwise specified.

Use the following environment variables to specify the data retention bot
credentials:

- `WICKRIO_BOT_NAME` — The name of the data retention bot.
  This variable is _required_ when you run the data retention
  bot Docker image.
- `WICKRIO_BOT_PASSWORD` — The initial password for the data
  retention bot. For more information, see [Prerequisites to configure data retention
  for AWS Wickr](configure-data-retention.md#data-retention-prerequisites "configure-data-retention.md#data-retention-prerequisites"). This variable is
  _required_ if you don't plan to start the data retention
  bot with a password prompt or you don't plan to use Secrets Manager to store the data
  retention bot credentials.
  Use the following environment variables to configure the default data retention
  streaming capabilities:

- `WICKRIO_COMP_MESGDEST` – The path name to the directory
  where messages will be streamed. The default value is
  `/tmp/`<botname>`/compliance/messages`.
- `WICKRIO_COMP_FILEDEST` – The path name to the directory
  where files will be streamed. The default value is
  `/tmp/`<botname>`/compliance/attachments`.
- `WICKRIO_COMP_BASENAME` – The base name for the received
  messages files. The default value is `receivedMessages`.
- `WICKRIO_COMP_FILESIZE` – The maximum file size for a
  received messages file in kibibyte (KiB). A new file is started when the max
  size is reached. The default value is `1000000000`, as in 1024
  GiB.
- `WICKRIO_COMP_TIMEROTATE` – The amount of time, in minutes,
  for which the data retention bot will put received messages into a received
  messages file. A new file is started when the time limit is reached. You can
  only use the file size or time to limit the size of the received messages file.
  The default value is `0`, as in no limit.
  Use the following environment variable to define the default AWS Region to
  use.

- `AWS_DEFAULT_REGION` – The default AWS Region to use for
  AWS services like Secrets Manager (not used for Amazon S3 or AWS KMS). The
  `us-east-1` Region is used by default if this environment
  variable is not defined.
  Use the following environment variables to specify the Secrets Manager secret to use when you
  opt to use Secrets Manager to store the data retention bot credentials and AWS service
  information. For more information about the values you can store in Secrets Manager see [Secrets Manager values for AWS Wickr](data-retention-aws-secret-values.md "data-retention-aws-secret-values.md").

- `AWS_SECRET_NAME` – The name of the Secrets Manager secret that
  contains the credentials and AWS service information needed by the data
  retention bot.
- `AWS_SECRET_REGION` – The AWS Region that the AWS secret
  is located in. If you are using AWS secrets and this value is not defined the
  `AWS_DEFAULT_REGION` value will be used.

###### Note

You can store all of the following environment variables as values in Secrets Manager. If
you opt to use Secrets Manager, and you store these values there, then you don't need to
specify them as environment variables when you run the data retention bot Docker
image. You only need to specify the `AWS_SECRET_NAME` environment
variable described earlier in this guide. For more information, see [Secrets Manager values for AWS Wickr](data-retention-aws-secret-values.md "data-retention-aws-secret-values.md").

Use the following environment variables to specify the Amazon S3 bucket when you opt to
store messages and files to a bucket.

- `WICKRIO_S3_BUCKET_NAME` – The name of the Amazon S3 bucket where
  messages and files will be stored.
- `WICKRIO_S3_REGION` – The AWS Region of the Amazon S3 bucket
  where messages and files will be stored.
- `WICKRIO_S3_FOLDER_NAME` – The optional folder name in the
  Amazon S3 bucket where messages and files will be stored. This folder name will be
  preceded with the key for messages and files saved to the Amazon S3 bucket.
  Use the following environment variables to specify the AWS KMS details when you opt to
  use client side encryption to re-encrypt files when saving them to an Amazon S3
  bucket.

- `WICKRIO_KMS_MSTRKEY_ARN` – The Amazon Resource Name (ARN)
  of the AWS KMS master key used to re-encrypt the message files and files on the
  data retention bot before they are saved to the Amazon S3 bucket.
- `WICKRIO_KMS_REGION` – The AWS Region where the AWS KMS
  master key is located.
  Use the following environment variable to specify the Amazon SNS details when you opt to
  send data retention events to an Amazon SNS topic. The events sent include startup, shutdown,
  as well as error conditions.

- `WICKRIO_SNS_TOPIC_ARN` – The ARN of the Amazon SNS topic that
  you want data retention events sent to.
  Use the following environment variable to send data retention metrics to CloudWatch. If
  specified, the metrics will be generated every 60 seconds.

- `WICKRIO_METRICS_TYPE` – Set the value of this environment
  variable to `cloudwatch` to send metrics to CloudWatch.
