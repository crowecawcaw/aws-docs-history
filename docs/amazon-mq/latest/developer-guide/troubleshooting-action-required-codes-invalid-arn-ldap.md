

# RabbitMQ on Amazon MQ: Invalid LDAP ARN
<a name="troubleshooting-action-required-codes-invalid-arn-ldap"></a>

 RabbitMQ on Amazon MQ will raise an INVALID\_ARN\_LDAP critical action required code when the ARN configured for the LDAP service account password is invalid or inaccessible. This applies to ARNs specified in `aws.arns.auth_ldap.dn_lookup_bind.password` or `aws.arns.auth_ldap.other_bind.password`, which must reference AWS Secrets Manager secrets containing plaintext passwords. 

 A broker in RABBITMQ\_INVALID\_ARN\_LDAP quarantine cannot authenticate with the LDAP service account, making LDAP authentication unavailable. If LDAP is the only configured authentication method, users will be unable to connect to the broker. Invalid ARNs can be caused by malformed ARN syntax, references to non-existent secrets, secrets located in a different AWS region than the broker, or insufficient secretsmanager:GetSecretValue permissions in the IAM role. 

## Diagnosing and addressing RABBITMQ\_INVALID\_ARN\_LDAP
<a name="w2aac40c33b7"></a>

 To diagnose and address the RABBITMQ\_INVALID\_ARN\_LDAP action required code, you must use Amazon CloudWatch Logs and the console. 

**To resolve the invalid LDAP ARN issue**

1. Navigate to Amazon CloudWatch Logs Insights and run the following query against your broker's log group `/aws/amazonmq/broker/<broker-id>/general`:

   ```
   fields @timestamp, @message
   | sort @timestamp desc
   | filter @message like /error.*aws_arn_config/
   | limit 10000
   ```

1. Look for error messages similar to:

   ```
   [error] <0.254.0> aws_arn_config: {<<"could not resolve ARN 'arn:aws:secretsmanager:xxx' for configuration 'aws.arns.auth_ldap.dn_lookup_bind.password', error: \"AWS service is unavailable\"">>,{error,"AWS service is unavailable"}}
   ```

1. Check the Secrets Manager secret and fix any issues such as:
   + Verify the secret exists in the same AWS region as the broker
   + Confirm the ARN syntax is correct
   + Ensure the IAM role has secretsmanager:GetSecretValue permissions

1. Update the broker configuration and reboot the broker.