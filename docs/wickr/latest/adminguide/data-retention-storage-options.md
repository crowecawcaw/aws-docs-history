This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Storage options for AWS Wickr

network

After data retention is enabled and the data retention bot is configured for your
Wickr network, it will capture all messages and files sent within your network.
Messages are saved in files which are limited to a specific size or time limit that can
be configured using an environment variable. For more information, see [Environment variables to configure
data retention bot in AWS Wickr](data-retention-bot-env-variables.md "data-retention-bot-env-variables.md").

You can configure one of the following options for storing this data:

- Store all captured messages and files locally. This is the default option.
  It's your responsibility to move local files to another system for long-term
  storage, and to make sure the host disk does not run out of memory or
  space.
- Store all captured messages and files in an Amazon S3 bucket. The data retention
  bot will save all decrypted messages and files to the Amazon S3 bucket you specify.
  The captured messages and files are removed from the host machine after they are
  successfully saved to the bucket.
- Store all captured messages and files encrypted in an Amazon S3 bucket. The data
  retention bot will re-encrypt all captured messages and files using a key that
  you supply and save them to the Amazon S3 bucket you specify. The captured messages
  and files are removed from the host machine after they are successfully
  re-encrypted and saved to the bucket. You will need software to decrypt the
  messages and files.

For more information about creating an Amazon S3 bucket to use with your data
retention bot, see [Creating a
bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon S3 User Guide_
