# LDAP authentication and authorization for Amazon MQ for RabbitMQ

Amazon MQ for RabbitMQ supports authentication and authorization of broker users using an external LDAP server. For other supported methods, see [Authentication and authorization for Amazon MQ for RabbitMQ brokers](rabbitmq-authentication.md "rabbitmq-authentication.md").

###### Important considerations

- The LDAP server needs to be accessible over the public internet. Amazon MQ for RabbitMQ can be configured to authenticate to the LDAP server using mutual TLS.
- Amazon MQ for RabbitMQ enforces the use of AWS ARNs for sensitive LDAP settings such as passwords and for settings that require access to the local file system. See [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md") for more details.
- You must include the IAM permission, `mq:UpdateBrokerAccessConfiguration`, to enable LDAP on existing brokers.
- Amazon MQ automatically creates a system user named `monitoring-AWS-OWNED-DO-NOT-DELETE` with monitoring-only permissions. This user uses RabbitMQ's internal authentication system even on LDAP-enabled brokers and is restricted to loopback interface access only. Amazon MQ prevents deletion of this user by adding the [protected user tag](https://github.com/rabbitmq/rabbitmq-server/blob/3751301d5a851f3f0a7d0b15583e52cb81af4e6b/release-notes/4.2.0.md#enhancements-3 "https://github.com/rabbitmq/rabbitmq-server/blob/3751301d5a851f3f0a7d0b15583e52cb81af4e6b/release-notes/4.2.0.md#enhancements-3").
  For information about how to configure LDAP for your Amazon MQ for RabbitMQ brokers, see [Using LDAP authentication and authorization](rabbitmq-ldap-tutorial.md "rabbitmq-ldap-tutorial.md").

###### On this page

- [Supported LDAP configurations](#ldap-supported-configs "#ldap-supported-configs")
- [Additional validations for LDAP configurations in Amazon MQ](#ldap-additional-validations "#ldap-additional-validations")

## Supported LDAP configurations

Amazon MQ for RabbitMQ supports all configurable variables in [RabbitMQ LDAP plugin](https://www.rabbitmq.com/docs/ldap "https://www.rabbitmq.com/docs/ldap"), with the following exceptions that require AWS ARNs. For details about ARN support, see [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md").

### Configurations requiring ARNs

`auth_ldap.dn_lookup_bind.password`

Use `aws.arns.auth_ldap.dn_lookup_bind.password` instead

`auth_ldap.other_bind.password`

Use `aws.arns.auth_ldap.other_bind.password` instead

`auth_ldap.ssl_options.cacertfile`

Use `aws.arns.auth_ldap.ssl_options.cacertfile` instead

`auth_ldap.ssl_options.certfile`

Use `aws.arns.auth_ldap.ssl_options.certfile` instead

`auth_ldap.ssl_options.keyfile`

Use `aws.arns.auth_ldap.ssl_options.keyfile` instead

### Unsupported SSL options

The following SSL configuration options are also not supported:

- `auth_ldap.ssl_options.cert`
- `auth_ldap.ssl_options.client_renegotiation`
- `auth_ldap.ssl_options.dh`
- `auth_ldap.ssl_options.dhfile`
- `auth_ldap.ssl_options.honor_cipher_order`
- `auth_ldap.ssl_options.honor_ecc_order`
- `auth_ldap.ssl_options.key.RSAPrivateKey`
- `auth_ldap.ssl_options.key.DSAPrivateKey`
- `auth_ldap.ssl_options.key.PrivateKeyInfo`
- `auth_ldap.ssl_options.log_alert`
- `auth_ldap.ssl_options.password`
- `auth_ldap.ssl_options.psk_identity`
- `auth_ldap.ssl_options.reuse_sessions`
- `auth_ldap.ssl_options.secure_renegotiate`
- `auth_ldap.ssl_options.versions.$version`
- `auth_ldap.ssl_options.sni`

## Additional validations for LDAP configurations in Amazon MQ

Amazon MQ also enforces the following additional validations for LDAP authentication and authorization:

- `auth_ldap.log` cannot be set to `network_unsafe`
- LDAP server must use LDAPS. Either `auth_ldap.use_ssl` or `auth_ldap.use_starttls` must be explicitly enabled
- If any setting requires the use of an AWS ARN, `aws.arns.assume_role_arn` must be provided.
- `auth_ldap.servers` must be a valid IP address or valid FQDN
- The following keys must be a valid LDAP Distinguished Name:
  - `auth_ldap.dn_lookup_base`
  - `auth_ldap.dn_lookup_bind.user_dn`
  - `auth_ldap.other_bind.user_dn`
  - `auth_ldap.group_lookup_base`
