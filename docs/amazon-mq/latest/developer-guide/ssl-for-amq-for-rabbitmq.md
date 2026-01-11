# SSL certificate authentication for Amazon MQ for RabbitMQ

Amazon MQ for RabbitMQ supports authentication of broker users using X.509 client certificates. For other supported methods, see [Authentication and authorization for Amazon MQ for RabbitMQ brokers](rabbitmq-authentication.md "rabbitmq-authentication.md").

###### Note

The SSL certificate authentication plugin is only available for Amazon MQ for RabbitMQ version 4 and above.

###### Important considerations

- Client certificates must be signed by a trusted Certificate Authority (CA). Amazon MQ for RabbitMQ validates the certificate chain during authentication.
- Amazon MQ for RabbitMQ enforces the use of AWS ARNs for certificate-related settings such as CA certificates and for settings that require access to the local file system. See [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md") for more details.
- Amazon MQ automatically creates a system user named `monitoring-AWS-OWNED-DO-NOT-DELETE` with monitoring-only permissions. This user uses RabbitMQ's internal authentication system even on SSL certificate-enabled brokers and is restricted to loopback interface access only. Amazon MQ prevents deletion of this user by adding the [protected user tag](https://github.com/rabbitmq/rabbitmq-server/blob/3751301d5a851f3f0a7d0b15583e52cb81af4e6b/release-notes/4.2.0.md#enhancements-3 "https://github.com/rabbitmq/rabbitmq-server/blob/3751301d5a851f3f0a7d0b15583e52cb81af4e6b/release-notes/4.2.0.md#enhancements-3").
  For information about how to configure SSL certificate authentication for your Amazon MQ for RabbitMQ brokers, see [Using SSL certificate authentication](rabbitmq-ssl-tutorial.md "rabbitmq-ssl-tutorial.md").

###### On this page

- [Supported SSL configurations](#ssl-supported-configs "#ssl-supported-configs")
- [Additional validations for SSL configurations in Amazon MQ](#ssl-additional-validations "#ssl-additional-validations")

## Supported SSL configurations

Amazon MQ for RabbitMQ supports SSL/TLS configuration for client connections. For details about ARN support, see [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md").

### Configurations requiring ARNs

`ssl_options.cacertfile`

Use `aws.arns.ssl_options.cacertfile` instead

### SSL certificate login configurations

The following configurations control how usernames are extracted from client certificates:

`ssl_cert_login_from`

Specifies which certificate field to use for username extraction. Supported values:

- `distinguished_name` - Use the full Distinguished Name
- `common_name` - Use the Common Name (CN) field
- `subject_alternative_name` or `subject_alt_name` - Use Subject Alternative Name

`ssl_cert_login_san_type`

When using Subject Alternative Name, specifies the SAN type. Supported values: `dns`, `ip`, `email`, `uri`, `other_name`

`ssl_cert_login_san_index`

When using Subject Alternative Name, specifies the index of the SAN entry to use (zero-based). Must be a non-negative integer.

### SSL options for client connections

The following SSL options apply to client connections:

`ssl_options.verify`

Peer verification mode. Supported values: `verify_none`, `verify_peer`

`ssl_options.fail_if_no_peer_cert`

Whether to reject connections if client doesn't provide a certificate. Boolean value.

`ssl_options.depth`

Maximum certificate chain depth for verification.

`ssl_options.hostname_verification`

Hostname verification mode. Supported values: `wildcard`, `none`

### Unsupported SSL options

The following SSL configuration options are not supported:

- `ssl_options.cert`
- `ssl_options.client_renegotiation`
- `ssl_options.dh`
- `ssl_options.dhfile`
- `ssl_options.honor_cipher_order`
- `ssl_options.honor_ecc_order`
- `ssl_options.key.RSAPrivateKey`
- `ssl_options.key.DSAPrivateKey`
- `ssl_options.key.PrivateKeyInfo`
- `ssl_options.log_alert`
- `ssl_options.password`
- `ssl_options.psk_identity`
- `ssl_options.reuse_sessions`
- `ssl_options.secure_renegotiate`
- `ssl_options.versions.$version`
- `ssl_options.sni`
- `ssl_options.crl_check`

## Additional validations for SSL configurations in Amazon MQ

Amazon MQ also enforces the following additional validations for SSL certificate authentication:

- If any setting requires the use of an AWS ARN, `aws.arns.assume_role_arn` must be provided.
