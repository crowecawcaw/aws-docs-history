

# ARN support in RabbitMQ configuration
<a name="arn-support-rabbitmq-configuration"></a>

Amazon MQ for RabbitMQ supports AWS ARNs for the values of some RabbitMQ configuration settings. This is enabled by the RabbitMQ community plugin [rabbitmq-aws](https://github.com/amazon-mq/rabbitmq-aws). This plugin is developed and maintained by Amazon MQ and can also be used in self-hosted RabbitMQ brokers not managed by Amazon MQ.

**Important considerations**  
The resolved ARN values retrieved by the aws plugin are passed directly to the RabbitMQ process at runtime. They are not stored elsewhere on the RabbitMQ node.
Amazon MQ for RabbitMQ requires an IAM role that can be assumed by Amazon MQ to access the configured ARNs. This is configured by setting `aws.arns.assume_role_arn`.
Users calling CreateBroker or UpdateBroker APIs with a broker configuration that includes an IAM role must have the `iam:PassRole` permission for that role.
The IAM role must exist in the same AWS account as the RabbitMQ broker. All ARNs in the configuration must be present in the same AWS region as the RabbitMQ broker.
Amazon MQ adds IAM global conditional keys `aws:SourceAccount` and `aws:SourceArn` when assuming the IAM role. These values must be used in the IAM policy attached to the role for [confused deputy protection](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html).

**Topics**
+ [Supported keys](#arn-support-supported-keys)
+ [IAM policy samples](#arn-support-iam-policy-samples)
+ [Related broker quarantine states](#arn-support-quarantine-states)
+ [Example scenario](#arn-support-example-scenario)

## Supported keys
<a name="arn-support-supported-keys"></a>

`aws.arns.assume_role_arn`  
IAM role ARN that Amazon MQ assumes to access other AWS resources. Required when any other ARN configuration is used.

### AMQP endpoint
<a name="arn-support-amqp-endpoint"></a>


| Configuration key | Description | 
| --- | --- | 
| aws.arns.ssl\_options.cacertfile | Certificate authority file for SSL/TLS client connections. Amazon MQ requires using Amazon S3 or to store the certificate. | 

### RabbitMQ management plugin
<a name="arn-support-management-plugin"></a>


| Configuration key | Description | 
| --- | --- | 
| aws.arns.management.ssl.cacertfile | Certificate authority file for management interface SSL/TLS connections. Amazon MQ requires using Amazon S3 or to store the certificate. | 

### RabbitMQ OAuth 2.0 plugin
<a name="arn-support-oauth2-plugin"></a>


| Configuration key | Description | 
| --- | --- | 
| aws.arns.auth\_oauth2.https.cacertfile | Certificate authority file for OAuth 2.0 HTTPS connections. Amazon MQ requires using Amazon S3 or to store the certificate. | 

### RabbitMQ HTTP authentication plugin
<a name="arn-support-http-plugin"></a>


| Configuration key | Description | 
| --- | --- | 
| aws.arns.auth\_http.ssl\_options.cacertfile | Certificate authority file for HTTP authentication SSL/TLS connections. Amazon MQ requires using Amazon S3 or to store the certificate. | 
| aws.arns.auth\_http.ssl\_options.certfile | Certificate file for mutual TLS connections between Amazon MQ and the HTTP authentication server. Amazon MQ requires using Amazon S3 or to store the certificate. | 
| aws.arns.auth\_http.ssl\_options.keyfile | Private key file for mutual TLS connections between Amazon MQ and the HTTP authentication server. Amazon MQ requires using AWS Secrets Manager to store the private key. | 

### RabbitMQ LDAP plugin
<a name="arn-support-ldap-plugin"></a>


| Configuration key | Description | 
| --- | --- | 
| aws.arns.auth\_ldap.ssl\_options.cacertfile | Certificate authority file for LDAP SSL/TLS connections. Amazon MQ requires using Amazon S3 or to store the certificate. | 
| aws.arns.auth\_ldap.ssl\_options.certfile | Certificate file for mutual TLS connections between Amazon MQ and the LDAP server. Amazon MQ requires using Amazon S3 or to store the certificate. | 
| aws.arns.auth\_ldap.ssl\_options.keyfile | Private key file for mutual TLS connections between Amazon MQ and the LDAP server. Amazon MQ requires using AWS Secrets Manager to store the private key. | 
| aws.arns.auth\_ldap.dn\_lookup\_bind.password | Password for LDAP DN lookup bind. Amazon MQ requires using AWS Secrets Manager to store the password as a plaintext value. | 
| aws.arns.auth\_ldap.other\_bind.password | Password for LDAP other bind. Amazon MQ requires using AWS Secrets Manager to store the password as a plaintext value. | 

## IAM policy samples
<a name="arn-support-iam-policy-samples"></a>

For IAM policy examples including assume role policy documents and role policy documents, see the [CDK sample implementation](https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-ldap-activedirectory-sample/lib/rabbitmq-activedirectory-stack.ts#L232).

See [Using LDAP authentication and authorization](rabbitmq-ldap-tutorial.md) for steps on how to set up AWS Secrets Manager and Amazon S3 resources.

## Related broker quarantine states
<a name="arn-support-quarantine-states"></a>

For information about broker quarantine states related to ARN support issues, see:
+ [RABBITMQ\_INVALID\_ASSUMEROLE](troubleshooting-action-required-codes-invalid-assumerole.md)
+ [RABBITMQ\_INVALID\_ARN\_LDAP](troubleshooting-action-required-codes-invalid-arn-ldap.md)
+ [RABBITMQ\_INVALID\_ARN](troubleshooting-action-required-codes-invalid-arn.md)

## Example scenario
<a name="arn-support-example-scenario"></a>
+ Broker `b-f0fc695e-2f9c-486b-845a-988023a3e55b` has been configured to use IAM role `<role>` to access AWS Secrets Manager secret `<arn>`
+ If the role provided to Amazon MQ does not have read permission on the AWS Secrets Manager secret, the following error will be shown in RabbitMQ logs:

  ```
  [error] <0.254.0> aws_arn_config: {handle_assume_role,{error,{assume_role_failed,"AWS service is unavailable"}}}
  ```

  Additionally, the broker will enter the `INVALID_ASSUMEROLE` quarantine state. For more information, see [INVALID\_ASSUMEROLE](troubleshooting-action-required-codes-invalid-assumerole.md).
+ LDAP authentication attempts will fail with the following error:

  ```
  [error] <0.254.0> LDAP bind failed: invalid_credentials
  ```
+ Fix the IAM role with the proper permissions