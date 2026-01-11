# HTTP authentication and authorization for Amazon MQ for RabbitMQ

Amazon MQ for RabbitMQ supports authentication and authorization of broker users using an external HTTP server. For other supported methods, see [Authentication and authorization for Amazon MQ for RabbitMQ brokers](rabbitmq-authentication.md "rabbitmq-authentication.md").

###### Note

The HTTP authentication plugin is only available for Amazon MQ for RabbitMQ version 4 and above.

###### Important considerations

- The HTTP server needs to be accessible over the public internet. Amazon MQ for RabbitMQ can be configured to authenticate to the HTTP server using mutual TLS.
- Amazon MQ for RabbitMQ enforces the use of AWS ARNs for settings that require access to the local file system. See [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md") for more details.
- You must include the IAM permission, `mq:UpdateBrokerAccessConfiguration`, to enable HTTP authentication on existing brokers.
- Amazon MQ automatically creates a system user named `monitoring-AWS-OWNED-DO-NOT-DELETE` with monitoring-only permissions. This user uses RabbitMQ's internal authentication system even on HTTP-enabled brokers and is restricted to loopback interface access only. Amazon MQ prevents deletion of this user by adding the [protected user tag](https://github.com/rabbitmq/rabbitmq-server/blob/3751301d5a851f3f0a7d0b15583e52cb81af4e6b/release-notes/4.2.0.md#enhancements-3 "https://github.com/rabbitmq/rabbitmq-server/blob/3751301d5a851f3f0a7d0b15583e52cb81af4e6b/release-notes/4.2.0.md#enhancements-3").
  For information about how to configure HTTP authentication for your Amazon MQ for RabbitMQ brokers, see [Using HTTP authentication and authorization](rabbitmq-http-tutorial.md "rabbitmq-http-tutorial.md").

###### On this page

- [Supported HTTP configurations](#http-supported-configs "#http-supported-configs")
- [Additional validations for HTTP configurations in Amazon MQ](#http-additional-validations "#http-additional-validations")

## Supported HTTP configurations

Amazon MQ for RabbitMQ supports all configurable variables in [RabbitMQ HTTP authentication plugin](https://github.com/rabbitmq/rabbitmq-auth-backend-http "https://github.com/rabbitmq/rabbitmq-auth-backend-http"), with the following exceptions that require AWS ARNs. For details about ARN support, see [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md").

### Configurations requiring ARNs

`auth_http.ssl_options.cacertfile`

Use `aws.arns.auth_http.ssl_options.cacertfile` instead

`auth_http.ssl_options.certfile`

Use `aws.arns.auth_http.ssl_options.certfile` instead

`auth_http.ssl_options.keyfile`

Use `aws.arns.auth_http.ssl_options.keyfile` instead

### Unsupported SSL options

The following SSL configuration options are also not supported:

- `auth_http.ssl_options.cert`
- `auth_http.ssl_options.client_renegotiation`
- `auth_http.ssl_options.dh`
- `auth_http.ssl_options.dhfile`
- `auth_http.ssl_options.honor_cipher_order`
- `auth_http.ssl_options.honor_ecc_order`
- `auth_http.ssl_options.key.RSAPrivateKey`
- `auth_http.ssl_options.key.DSAPrivateKey`
- `auth_http.ssl_options.key.PrivateKeyInfo`
- `auth_http.ssl_options.log_alert`
- `auth_http.ssl_options.password`
- `auth_http.ssl_options.psk_identity`
- `auth_http.ssl_options.reuse_sessions`
- `auth_http.ssl_options.secure_renegotiate`
- `auth_http.ssl_options.versions.$version`
- `auth_http.ssl_options.sni`
- `auth_http.ssl_options.crl_check`

## Additional validations for HTTP configurations in Amazon MQ

Amazon MQ also enforces the following additional validations for HTTP authentication and authorization:

- `auth_http.http_method` must be either `get` or `post`
- The following path configurations must use HTTPS URLs:
  - `auth_http.user_path`
  - `auth_http.vhost_path`
  - `auth_http.resource_path`
  - `auth_http.topic_path`

- If any setting requires the use of an AWS ARN, `aws.arns.assume_role_arn` must be provided.
