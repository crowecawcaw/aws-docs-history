

# Monitor AWS Secrets Manager secrets for compliance by using AWS Config
<a name="configuring-awsconfig-rules"></a>

You can use AWS Config to evaluate your secrets to see if they are in compliance with your standards. You define your internal security and compliance requirements for secrets using AWS Config rules. Then AWS Config can identify secrets that don't conform to your rules. You can also track changes to secret metadata, [rotation configuration](find-secrets-not-rotating.md), the KMS key used for secret encryption, the Lambda rotation function, and tags associated with a secret.

You can configure AWS Config to notify you of changes. For more information, see [Notifications that AWS Config sends to an Amazon SNS topic](https://docs.aws.amazon.com/config/latest/developerguide/notifications-for-AWS-Config.html).

If you have secrets in multiple AWS accounts and AWS Regions in your organization, you can aggregate that configuration and compliance data. For more information, see [Multi-account Multi-Region data aggregation](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html).

**To assess whether secrets are in compliance**
+ Follow the instructions on [Evaluating your resources with AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluating-your-resources.html), and choose one of the following rules:
  + `[secretsmanager-secret-unused](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-secret-unused.html)`— Checks whether secrets were accessed within the specified number of days.
  + `[secretsmanager-using-cmk](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-using-cmk.html)` — Checks whether secrets are encrypted using the AWS managed key `aws/secretsmanager` or a customer managed key you created in AWS KMS.
  + `[secretsmanager-rotation-enabled-check](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-rotation-enabled-check.html)` — Checks whether rotation is configured for secrets stored in Secrets Manager. 
  + `[secretsmanager-scheduled-rotation-success-check](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html)`— Checks whether the last successful rotation is within the configured rotation frequency. The minimum frequency for the check is daily. 
  + `[secretsmanager-secret-periodic-rotation](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-secret-periodic-rotation.html)`— Checks whether secrets were rotated within the specified number of days.