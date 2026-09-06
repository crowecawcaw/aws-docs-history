

# Find secrets that aren't rotated
<a name="find-secrets-not-rotating"></a>

You can use AWS Config to evaluate your secrets to see if they are rotating in compliance with your standards. You define your internal security and compliance requirements for secrets using AWS Config rules. Then AWS Config can identify secrets that don't conform to your rules. You can also track changes to secret metadata, rotation configuration, the KMS key used for secret encryption, the Lambda rotation function, and tags associated with a secret.

If you have secrets in multiple AWS accounts and AWS Regions in your organization, you can aggregate that configuration and compliance data. For more information, see [Multi-account Multi-Region data aggregation](https://docs.aws.amazon.com/config/latest/developerguide/aggregate-data.html).

**To assess whether secrets are rotating**

1. Follow the instructions on [Evaluating your resources with AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluating-your-resources.html), and choose from of the following rules:
   + `[secretsmanager-rotation-enabled-check](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-rotation-enabled-check.html)` — Checks whether rotation is configured for secrets stored in Secrets Manager. 
   + `[secretsmanager-scheduled-rotation-success-check](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-scheduled-rotation-success-check.html)`— Checks whether the last successful rotation is within the configured rotation frequency. The minimum frequency for the check is daily. 
   + `[secretsmanager-secret-periodic-rotation](https://docs.aws.amazon.com/config/latest/developerguide/secretsmanager-secret-periodic-rotation.html)`— Checks whether secrets were rotated within the specified number of days.

1. Optionally, configure AWS Config to notify you when secrets aren't compliant. For more information, see [Notifications that AWS Config sends to an Amazon SNS topic](https://docs.aws.amazon.com/config/latest/developerguide/notifications-for-AWS-Config.html).