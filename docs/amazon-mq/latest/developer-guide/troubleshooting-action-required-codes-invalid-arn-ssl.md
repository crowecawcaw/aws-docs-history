

# RabbitMQ on Amazon MQ: Invalid SSL ARN
<a name="troubleshooting-action-required-codes-invalid-arn-ssl"></a>

 RabbitMQ on Amazon MQ will raise an INVALID\_ARN\_SSL critical action required code when one or more ARNs of CA certificate truststore for EXTERNAL auth\_mechanism are invalid or inaccessible. This applies to ARNS specified in `aws.arns.ssl_options.cacertfile` or `aws.arns.management.ssl.cacertfile`, which must reference Amazon S3 or ACM PCA object containing the certificate. 

 A broker in RABBITMQ\_INVALID\_ARN\_SSL quarantine cannot authenticate client certificates during mutual TLS handshakes because no valid truststore is configured. If EXTERNAL auth mechanism is the only configured authentication method, users will be unable to connect to the broker. Invalid ARNs can be caused by malformed ARN syntax, references to non-existent S3 objects, S3 objects located in a different AWS region than the broker, or insufficient s3:GetObject/acm-pca:GetCertificateAuthorityCertificate permissions in the IAM role. 

## Diagnosing and addressing RABBITMQ\_INVALID\_ARN\_SSL
<a name="w2aac40c37b7"></a>

 To diagnose and address the RABBITMQ\_INVALID\_ARN\_SSL action required code, you must use Amazon CloudWatch Logs and the console. 

**To resolve the invalid SSL ARN issue**

1. Navigate to Amazon CloudWatch Logs Insights and run the following query against your broker's log group `/aws/amazonmq/broker/<broker-id>/general`:

   ```
   fields @timestamp, @message
   | sort @timestamp desc
   | filter @message like /error.*aws_arn_config/
   | limit 10000
   ```

1. Look for error messages similar to:

   ```
   [error] <0.209.0> aws_arn_config: {<<"could not resolve ARN 'arn:aws:acm-pca:xxxx' for configuration 'aws.arns.ssl_options.cacertfile', error: \"AWS service is unavailable\"">>,{error,"AWS service is unavailable"}}
   ```

1. Check the S3/ACM-PCA Object and fix any issues such as:
   + Verify the secret exists in the same AWS region as the broker
   + Confirm the ARN syntax is correct
   + Ensure the IAM role has s3:GetObject/acm-pca:GetCertificateAuthorityCertificate permissions

1. Update the broker configuration and reboot the broker.