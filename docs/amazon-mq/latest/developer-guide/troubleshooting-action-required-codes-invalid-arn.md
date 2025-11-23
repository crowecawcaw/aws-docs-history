# RabbitMQ on Amazon MQ: Invalid ARN

RabbitMQ on Amazon MQ will raise an INVALID_ARN critical action required code when one or more ARNs configured in the broker are invalid or inaccessible. This applies to ARNs used for SSL certificates, AWS Secrets Manager secrets, Amazon S3 objects, or other AWS resource references not covered by more specific quarantine codes such as RABBITMQ_INVALID_ARN_LDAP or RABBITMQ_INVALID_ASSUMEROLE.

A broker in RABBITMQ_INVALID_ARN quarantine may experience degraded functionality depending on which ARNs are invalid. Features that depend on the inaccessible resources will be unavailable, and the broker will log errors indicating which ARN failed to resolve. The impact on broker availability depends on whether the invalid ARN is required for critical broker operations.

## Diagnosing and addressing RABBITMQ_INVALID_ARN

To diagnose and address the RABBITMQ_INVALID_ARN action required code, you must use Amazon CloudWatch Logs and the appropriate AWS service console for the affected resource.

###### To resolve the invalid ARN issue

1. Navigate to Amazon CloudWatch Logs Insights and run the following query against your broker's log group `/amazonmq/rabbitmq-on-host/rabbitmq`:

```

fields @timestamp, @message, @logStream, @log
| sort @timestamp desc
| filter @logStream like "b-<your-broker-id>"
| filter @message like /error.*aws_arn_config/
| limit 10000

```

2. Look for error messages similar to:

```

[error] <0.254.0> aws_arn_config: {<<"could not resolve ARN 'arn:aws:s3:::bucket-name/certificate.pem' for configuration 'aws.arns.auth_ldap.ssl_options.cacertfile', error: \"AWS service is unavailable\"">>,{error,"AWS service is unavailable"}}

```

3. Check the AWS resource and fix any issues such as:
   - Verify the resource exists in the same AWS region as the broker
   - Confirm the ARN syntax is correct
   - Ensure the IAM role has appropriate permissions to access the resource

4. Validate the fix using the [ARN access validation](arn-support-rabbitmq-configuration.md#arn-support-validation "arn-support-rabbitmq-configuration.md#arn-support-validation") API endpoint before updating the broker configuration.
5. Update the broker configuration and reboot the broker.
