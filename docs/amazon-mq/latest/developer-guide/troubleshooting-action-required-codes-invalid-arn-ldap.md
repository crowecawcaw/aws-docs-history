# RabbitMQ on Amazon MQ: Invalid LDAP ARN

RabbitMQ on Amazon MQ will raise an INVALID_ARN_LDAP critical action required code when the ARN configured for the LDAP service account password is invalid or inaccessible. This applies to ARNs specified in `aws.arns.auth_ldap.dn_lookup_bind.password` or `aws.arns.auth_ldap.other_bind.password`, which must reference AWS Secrets Manager secrets containing plaintext passwords.

A broker in RABBITMQ_INVALID_ARN_LDAP quarantine cannot authenticate with the LDAP service account, making LDAP authentication unavailable. If LDAP is the only configured authentication method, users will be unable to connect to the broker. Invalid ARNs can be caused by malformed ARN syntax, references to non-existent secrets, secrets located in a different AWS region than the broker, or insufficient secretsmanager:GetSecretValue permissions in the IAM role.

## Diagnosing and addressing RABBITMQ_INVALID_ARN_LDAP

To diagnose and address the RABBITMQ_INVALID_ARN_LDAP action required code, you must use Amazon CloudWatch Logs and the console.

###### To resolve the invalid LDAP ARN issue

1. Navigate to Amazon CloudWatch Logs Insights and run the following query against your broker's log group `/aws/amazonmq/broker/<broker-id>/general`:

```

fields @timestamp, @message
| sort @timestamp desc
| filter @message like /error.*aws_arn_config/
| limit 10000

```

2. Look for error messages similar to:

```

[error] <0.254.0> aws_arn_config: {<<"could not resolve ARN 'arn:aws:secretsmanager:xxx' for configuration 'aws.arns.auth_ldap.dn_lookup_bind.password', error: \"AWS service is unavailable\"">>,{error,"AWS service is unavailable"}}

```

3. Check the Secrets Manager secret and fix any issues such as:
   - Verify the secret exists in the same AWS region as the broker
   - Confirm the ARN syntax is correct
   - Ensure the IAM role has secretsmanager:GetSecretValue permissions

4. Validate the fix using the [ARN access validation](arn-support-rabbitmq-configuration.md#arn-support-validation "arn-support-rabbitmq-configuration.md#arn-support-validation") API endpoint before updating the broker configuration.
5. Update the broker configuration and reboot the broker.
