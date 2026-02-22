# RabbitMQ on Amazon MQ: Invalid HTTP ARN

RabbitMQ on Amazon MQ will raise an INVALID_ARN_HTTP critical action required code when one or more ARNs of SSL certificates or key file for HTTP auth_backend are invalid or inaccessible. This applies to ARNS specified in `aws.arns.auth_http.ssl_options.cacertfile`, `aws.arns.auth_http.ssl_options.certfile` or `aws.arns.auth_http.ssl_options.keyfile`, which must reference Amazon S3 objects and AWS Secrets Manager secrets containing certificates and private key.

A broker in RABBITMQ_INVALID_ARN_HTTP quarantine cannot authenticate via the HTTP server. If HTTP is the only configured authentication method, users will be unable to connect to the broker. Invalid ARNs can be caused by malformed ARN syntax, references to non-existent secrets, secrets located in a different AWS region than the broker, or insufficient s3:GetObject/secretsmanager:GetSecretValue permissions in the IAM role.

## Diagnosing and addressing RABBITMQ_INVALID_ARN_HTTP

To diagnose and address the RABBITMQ_INVALID_ARN_HTTP action required code, you must use Amazon CloudWatch Logs and the console.

###### To resolve the invalid HTTP ARN issue

1. Navigate to Amazon CloudWatch Logs Insights and run the following query against your broker's log group `/aws/amazonmq/broker/<broker-id>/general`:

```

fields @timestamp, @message
| sort @timestamp desc
| filter @message like /error.*aws_arn_config/
| limit 10000

```

2. Look for error messages similar to:

```

[error] <0.209.0> aws_arn_config: {<<"could not resolve ARN 'arn:aws:s3:::xxxx' for configuration 'aws.arns.auth_http.ssl_options.certfile', error: \"AWS service is unavailable\"">>,{error,"AWS service is unavailable"}}

```

3. Check the S3 Object/Secrets Manager secret and fix any issues such as:
   - Verify the resource exists in the same AWS region as the broker
   - Confirm the ARN syntax is correct
   - Ensure the IAM role has s3:GetObject and secretsmanager:GetSecretValue permissions

4. Validate the fix using the [ARN access validation](arn-support-rabbitmq-configuration.md#arn-support-validation "arn-support-rabbitmq-configuration.md#arn-support-validation") API endpoint before updating the broker configuration.
5. Update the broker configuration and reboot the broker.
