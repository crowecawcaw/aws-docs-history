

# RabbitMQ on Amazon MQ: Invalid ARN
<a name="troubleshooting-action-required-codes-invalid-arn"></a>

 RabbitMQ on Amazon MQ will raise an INVALID\_ARN critical action required code when one or more ARNs configured in the broker are invalid or inaccessible. This applies to ARNs used for SSL certificates, AWS Secrets Manager secrets, Amazon S3 objects, or other AWS resource references not covered by more specific quarantine codes such as RABBITMQ\_INVALID\_ARN\_LDAP or RABBITMQ\_INVALID\_ASSUMEROLE. 

 A broker in RABBITMQ\_INVALID\_ARN quarantine may experience degraded functionality depending on which ARNs are invalid. Features that depend on the inaccessible resources will be unavailable, and the broker will log errors indicating which ARN failed to resolve. The impact on broker availability depends on whether the invalid ARN is required for critical broker operations. 

## Diagnosing and addressing RABBITMQ\_INVALID\_ARN
<a name="w2aac40c39b7"></a>

 To diagnose and address the RABBITMQ\_INVALID\_ARN action required code, you must use Amazon CloudWatch Logs and the appropriate AWS service console for the affected resource. 

**To resolve the invalid ARN issue**

1. Navigate to Amazon CloudWatch Logs Insights and run the following query against your broker's log group `/aws/amazonmq/broker/<broker-id>/general`:

   ```
   fields @timestamp, @message
   | sort @timestamp desc
   | filter @message like /error.*aws_arn_config/
   | limit 10000
   ```

1. Look for error messages similar to:

   ```
   [error] <0.254.0> aws_arn_config: {<<"could not resolve ARN 'arn:aws:s3:::bucket-name/certificate.pem' for configuration 'aws.arns.auth_ldap.ssl_options.cacertfile', error: \"AWS service is unavailable\"">>,{error,"AWS service is unavailable"}}
   ```

1. Check the AWS resource and fix any issues such as:
   + Verify the resource exists in the same AWS region as the broker
   + Confirm the ARN syntax is correct
   + Ensure the IAM role has appropriate permissions to access the resource

1. Update the broker configuration and reboot the broker.