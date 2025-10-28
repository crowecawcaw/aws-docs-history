This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Configure data retention for

AWS Wickr

To configure data retention for your AWS Wickr network, you must deploy the data
retention bot Docker image to a container on a host, such as a local computer or an instance
in Amazon Elastic Compute Cloud (Amazon EC2). After the bot is deployed, you can configure it to store data locally
or in an Amazon Simple Storage Service (Amazon S3) bucket. You can also configure the data retention bot to use other
AWS services like AWS Secrets Manager (Secrets Manager), Amazon CloudWatch (CloudWatch), Amazon Simple Notification Service (Amazon SNS), and AWS Key Management Service
(AWS KMS). The following topics describe how to configure and run the data retention bot for
your Wickr network.

###### Topics

- [Prerequisites to configure data retention
  for AWS Wickr](#data-retention-prerequisites "#data-retention-prerequisites")
- [Password for data retention bot in
  AWS Wickr](data-retention-password.md "data-retention-password.md")
- [Storage options for AWS Wickr
  network](data-retention-storage-options.md "data-retention-storage-options.md")
- [Environment variables to configure
  data retention bot in AWS Wickr](data-retention-bot-env-variables.md "data-retention-bot-env-variables.md")
- [Secrets Manager values for AWS Wickr](data-retention-aws-secret-values.md "data-retention-aws-secret-values.md")
- [IAM policy to use data retention with
  AWS services](data-retention-aws-services.md "data-retention-aws-services.md")
- [Start the data retention bot for your Wickr network](starting-data-retention-bot.md "starting-data-retention-bot.md")
- [Stop the data retention bot for your Wickr network](stopping-data-retention-bot.md "stopping-data-retention-bot.md")

## Prerequisites to configure data retention

for AWS Wickr

Before you get started, you must get the data retention bot name (labeled as
**Username**) and initial password from the AWS Management Console for Wickr. You
must specify both of these values the first time you start the data retention bot. You
must also enable data retention in the console. For more information, see [View data retention details in
AWS Wickr](view-data-retention-details.md "view-data-retention-details.md").
