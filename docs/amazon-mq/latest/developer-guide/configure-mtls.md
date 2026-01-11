# Configuring mTLS

Amazon MQ for RabbitMQ supports mutual TLS (mTLS) for secure connections to various endpoints and external services. mTLS provides enhanced security by requiring both client and server to authenticate using certificates.

###### Note

The use of private certificate authorities for mTLS is only available for Amazon MQ for RabbitMQ version 4 and above.

###### Important

Amazon MQ for RabbitMQ enforces the use of AWS ARNs for certificate and private key files. See [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md") for more details.

###### On this page

- [AMQP endpoint](#mtls-amqp-endpoint "#mtls-amqp-endpoint")
- [RabbitMQ management plugin](#mtls-management-plugin "#mtls-management-plugin")
- [RabbitMQ OAuth 2.0 plugin](#mtls-oauth2-plugin "#mtls-oauth2-plugin")
- [RabbitMQ HTTP authentication plugin](#mtls-http-plugin "#mtls-http-plugin")
- [RabbitMQ LDAP plugin](#mtls-ldap-plugin "#mtls-ldap-plugin")
- [AMQP client connections](#mtls-amqp-client "#mtls-amqp-client")

## AMQP endpoint

Configure mTLS for client connections to the AMQP endpoint. This is used with SSL certificate authentication. For supported configurations, see [SSL certificate authentication](ssl-for-amq-for-rabbitmq.md "ssl-for-amq-for-rabbitmq.md").

## RabbitMQ management plugin

Configure mTLS for connections to the RabbitMQ management interface.

###### Note

Strict mTLS is not supported for the management API.

###### Supported configurations

`aws.arns.management.ssl.cacertfile`

Certificate authority file for validating client certificates connecting to the management interface.

`management.ssl.verify`

Peer verification mode. Supported values: `verify_none`, `verify_peer`

`management.ssl.depth`

Maximum certificate chain depth for verification.

`management.ssl.hostname_verification`

Hostname verification mode. Supported values: `wildcard`, `none`

###### Unsupported SSL options

The following SSL configuration values are not supported:

- `management.ssl.cert`
- `management.ssl.client_renegotiation`
- `management.ssl.dh`
- `management.ssl.dhfile`
- `management.ssl.fail_if_no_peer_cert`
- `management.ssl.honor_cipher_order`
- `management.ssl.honor_ecc_order`
- `management.ssl.key.RSAPrivateKey`
- `management.ssl.key.DSAPrivateKey`
- `management.ssl.key.PrivateKeyInfo`
- `management.ssl.log_alert`
- `management.ssl.password`
- `management.ssl.psk_identity`
- `management.ssl.reuse_sessions`
- `management.ssl.secure_renegotiate`
- `management.ssl.versions.$version`
- `management.ssl.sni`

## RabbitMQ OAuth 2.0 plugin

Configure mTLS for connections from Amazon MQ to the OAuth 2.0 identity provider. For supported configurations, see [OAuth 2.0 authentication and authorization](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md").

## RabbitMQ HTTP authentication plugin

Configure mTLS for connections from Amazon MQ to the HTTP authentication server. For supported configurations, see [HTTP authentication and authorization](http-for-amq-for-rabbitmq.md "http-for-amq-for-rabbitmq.md").

## RabbitMQ LDAP plugin

Configure mTLS for connections from Amazon MQ to the LDAP server. For supported configurations, see [LDAP authentication and authorization](ldap-for-amq-for-rabbitmq.md "ldap-for-amq-for-rabbitmq.md").

## AMQP client connections

Configure TLS peer verification for AMQP client connections used by federation and shovel. For more information, see [AMQP client SSL configuration](rabbitmq-amqp-client-ssl-configuration.md "rabbitmq-amqp-client-ssl-configuration.md").

###### Important

Amazon MQ does not currently support configuring client certificates for AMQP client connections. As a result, federation and shovel cannot connect to mTLS-enabled brokers that require client certificate authentication.
