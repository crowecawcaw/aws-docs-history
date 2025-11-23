# RabbitMQ on Amazon MQ: Invalid IAM Assume Role

RabbitMQ on Amazon MQ will raise an INVALID_ASSUMEROLE critical action required code when the IAM role ARN specified in `aws.arns.assume_role_arn` is invalid or cannot be assumed by Amazon MQ. This can occur when the role does not exist, is in a different AWS account than the broker, or lacks the necessary trust relationship with mq.amazonaws.com.

A broker in RABBITMQ_INVALID_ASSUMEROLE quarantine cannot retrieve credentials or certificates required for LDAP authentication, rendering LDAP authentication unavailable. If LDAP is the only configured authentication method, users will be unable to connect to the broker. The IAM role is required by Amazon MQ to access AWS resources referenced by ARNs in the broker configuration, such as AWS Secrets Manager secrets or Amazon S3 objects used for LDAP authentication.

## Diagnosing and addressing RABBITMQ_INVALID_ASSUMEROLE

To diagnose and address the RABBITMQ_INVALID_ASSUMEROLE action required code, you must use Amazon CloudWatch Logs and the AWS Identity and Access Management console.

###### To resolve the invalid assume role issue

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

[error] <0.254.0> aws_arn_config: {handle_assume_role,{error,{assume_role_failed,"AWS service is unavailable"}}}

```

3. Check the IAM role configuration and fix any issues such as:
   - Ensure the role exists in the same AWS account as the broker
   - Verify the trust policy allows mq.amazonaws.com to assume the role
   - Confirm the role has appropriate permissions to access the required AWS resources

4. Validate the fix using the [ARN access validation](arn-support-rabbitmq-configuration.md#arn-support-validation "arn-support-rabbitmq-configuration.md#arn-support-validation") API endpoint before updating the broker configuration.
5. Update the broker configuration and reboot the broker.
