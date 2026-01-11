# ARN support in RabbitMQ configuration

Amazon MQ for RabbitMQ supports AWS ARNs for the values of some RabbitMQ configuration settings. This is enabled by the RabbitMQ community plugin [rabbitmq-aws](https://github.com/amazon-mq/rabbitmq-aws "https://github.com/amazon-mq/rabbitmq-aws"). This plugin is developed and maintained by Amazon MQ and can also be used in self-hosted RabbitMQ brokers not managed by Amazon MQ.

###### Important considerations

- The resolved ARN values retrieved by the aws plugin are passed directly to the RabbitMQ process at runtime. They are not stored elsewhere on the RabbitMQ node.
- Amazon MQ for RabbitMQ requires an IAM role that can be assumed by Amazon MQ to access the configured ARNs. This is configured by setting `aws.arns.assume_role_arn`.
- Users calling CreateBroker or UpdateBroker APIs with a broker configuration that includes an IAM role must have the `iam:PassRole` permission for that role.
- The IAM role must exist in the same AWS account as the RabbitMQ broker. All ARNs in the configuration must be present in the same AWS region as the RabbitMQ broker.
- Amazon MQ adds IAM global conditional keys `aws:SourceAccount` and `aws:SourceArn` when assuming the IAM role. These values must be used in the IAM policy attached to the role for [confused deputy protection](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md").

###### On this page

- [Supported keys](#arn-support-supported-keys "#arn-support-supported-keys")
- [IAM policy samples](#arn-support-iam-policy-samples "#arn-support-iam-policy-samples")
- [Access validation](#arn-support-validation "#arn-support-validation")
- [Related broker quarantine states](#arn-support-quarantine-states "#arn-support-quarantine-states")
- [Example scenario](#arn-support-example-scenario "#arn-support-example-scenario")

## Supported keys

###### Required IAM role

`aws.arns.assume_role_arn`

IAM role ARN that Amazon MQ assumes to access other AWS resources. Required when any other ARN configuration is used.

| Configuration key                 | Description                                                                                                                |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `aws.arns.ssl_options.cacertfile` | Certificate authority file for SSL/TLS client connections. Amazon MQ requires using Amazon S3 or to store the certificate. |

| Configuration key                    | Description                                                                                                                              |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `aws.arns.management.ssl.cacertfile` | Certificate authority file for management interface SSL/TLS connections. Amazon MQ requires using Amazon S3 or to store the certificate. |

| Configuration key                       | Description                                                                                                                 |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `aws.arns.auth_oauth2.https.cacertfile` | Certificate authority file for OAuth 2.0 HTTPS connections. Amazon MQ requires using Amazon S3 or to store the certificate. |

| Configuration key                           | Description                                                                                                                                                              |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `aws.arns.auth_http.ssl_options.cacertfile` | Certificate authority file for HTTP authentication SSL/TLS connections. Amazon MQ requires using Amazon S3 or to store the certificate.                                  |
| `aws.arns.auth_http.ssl_options.certfile`   | Certificate file for mutual TLS connections between Amazon MQ and the HTTP authentication server. Amazon MQ requires using Amazon S3 or to store the certificate.        |
| `aws.arns.auth_http.ssl_options.keyfile`    | Private key file for mutual TLS connections between Amazon MQ and the HTTP authentication server. Amazon MQ requires using AWS Secrets Manager to store the private key. |

| Configuration key                            | Description                                                                                                                                               |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws.arns.auth_ldap.ssl_options.cacertfile`  | Certificate authority file for LDAP SSL/TLS connections. Amazon MQ requires using Amazon S3 or to store the certificate.                                  |
| `aws.arns.auth_ldap.ssl_options.certfile`    | Certificate file for mutual TLS connections between Amazon MQ and the LDAP server. Amazon MQ requires using Amazon S3 or to store the certificate.        |
| `aws.arns.auth_ldap.ssl_options.keyfile`     | Private key file for mutual TLS connections between Amazon MQ and the LDAP server. Amazon MQ requires using AWS Secrets Manager to store the private key. |
| `aws.arns.auth_ldap.dn_lookup_bind.password` | Password for LDAP DN lookup bind. Amazon MQ requires using AWS Secrets Manager to store the password as a plaintext value.                                |
| `aws.arns.auth_ldap.other_bind.password`     | Password for LDAP other bind. Amazon MQ requires using AWS Secrets Manager to store the password as a plaintext value.                                    |

## IAM policy samples

For IAM policy examples including assume role policy documents and role policy documents, see the [CDK sample implementation](https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-ldap-activedirectory-sample/lib/rabbitmq-activedirectory-stack.ts#L232 "https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-ldap-activedirectory-sample/lib/rabbitmq-activedirectory-stack.ts#L232").

See [Using LDAP authentication and authorization](rabbitmq-ldap-tutorial.md "rabbitmq-ldap-tutorial.md") for steps on how to set up AWS Secrets Manager and Amazon S3 resources.

## Access validation

To troubleshoot scenarios where ARN values cannot be fetched, the aws plugin supports a [RabbitMQ management API endpoint](https://github.com/amazon-mq/rabbitmq-aws/blob/main/API.md "https://github.com/amazon-mq/rabbitmq-aws/blob/main/API.md") that can be called to check if Amazon MQ is able to successfully assume the role and resolve AWS ARNs. This avoids the need to update broker configuration, update broker with the new configuration revision and reboot broker to test configuration changes.

###### Note

Use of this API requires an existing RabbitMQ administrator user. Amazon MQ recommends creating test brokers with an internal user in addition to other access methods. See [enabling both OAuth 2.0 and simple (internal) authentication](oauth-tutorial.md#oauth-tutorial-config-both-auth-methods-using-cli "oauth-tutorial.md#oauth-tutorial-config-both-auth-methods-using-cli"). This user can then be used to access the validation API.

###### Note

Though aws plugin supports passing a new role as an input to the validation API, this parameter is not supported by Amazon MQ. The IAM role used for validation should match the value of `aws.arns.assume_role_arn` in broker configuration.

## Related broker quarantine states

For information about broker quarantine states related to ARN support issues, see:

- [RABBITMQ_INVALID_ASSUMEROLE](troubleshooting-action-required-codes-invalid-assumerole.md "troubleshooting-action-required-codes-invalid-assumerole.md")
- [RABBITMQ_INVALID_ARN_LDAP](troubleshooting-action-required-codes-invalid-arn-ldap.md "troubleshooting-action-required-codes-invalid-arn-ldap.md")
- [RABBITMQ_INVALID_ARN](troubleshooting-action-required-codes-invalid-arn.md "troubleshooting-action-required-codes-invalid-arn.md")

## Example scenario

- Broker `b-f0fc695e-2f9c-486b-845a-988023a3e55b` has been configured to use IAM role `<role>` to access AWS Secrets Manager secret `<arn>`
- If the role provided to Amazon MQ does not have read permission on the AWS Secrets Manager secret, the following error will be shown in RabbitMQ logs:

```
[error] <0.254.0> aws_arn_config: {handle_assume_role,{error,{assume_role_failed,"AWS service is unavailable"}}}
```

Additionally, the broker will enter the `INVALID_ASSUMEROLE` quarantine state. For more information, see [INVALID_ASSUMEROLE](troubleshooting-action-required-codes-invalid-assumerole.md "troubleshooting-action-required-codes-invalid-assumerole.md").

- LDAP authentication attempts will fail with the following error:

```
[error] <0.254.0> LDAP bind failed: invalid_credentials
```

- Fix the IAM role with the proper permissions
- Call the validation endpoint to verify if RabbitMQ is now able to access the secret:

```
curl -4su 'guest:guest' -XPUT -H 'content-type: application/json' <broker-endpoint>/api/aws/arn/validate -d '{"assume_role_arn":"arn:aws:iam::<account-id>:role/<role-name>","arns":["arn:aws:secretsmanager:<region>:<account-id>:secret:<secret-name>"]}' | jq '.'
```
