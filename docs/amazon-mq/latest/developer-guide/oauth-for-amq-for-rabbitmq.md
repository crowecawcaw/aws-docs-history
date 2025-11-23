# OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ

Amazon MQ for RabbitMQ supports multiple authentication and authorization methods. For information about all supported methods, see [Authentication and authorization for Amazon MQ for RabbitMQ brokers](rabbitmq-authentication.md "rabbitmq-authentication.md").

In OAuth 2.0 authentication and authorization, broker users and their permissions are managed by an external OAuth 2.0 identity provider (IdP). User authentication and resource permissions for vhosts, exchanges, queues, and topics are centralized through the OAuth 2.0 provider's scope system. This simplifies user management and enables integration with existing identity systems.

###### Important considerations

- OAuth 2.0 integration isn't supported on Amazon MQ for ActiveMQ brokers.
- Amazon MQ for RabbitMQ doesn't support server certificate issued by a private CA.
- The RabbitMQ OAuth 2.0 plugin doesn't support token introspection endpoints and opaque access tokens. It also doesn't perform token revocation checks.
- You must include the IAM permission, `mq:UpdateBrokerAccessConfiguration`, to enable OAuth 2.0 on existing brokers.
- Amazon MQ automatically creates a system user named `monitoring-AWS-OWNED-DO-NOT-DELETE` with monitoring-only permissions. This user uses RabbitMQ's internal authentication system even on OAuth 2.0-enabled brokers and is restricted to loopback interface access only.
  For information about how to configure OAuth 2.0 for your Amazon MQ for RabbitMQ brokers, see [Using OAuth 2.0 authentication and authorization](oauth-tutorial.md "oauth-tutorial.md").

###### On this page

- [Supported OAuth 2.0 configurations](#oauth-tutorial-supported-configs "#oauth-tutorial-supported-configs")
- [Additional validations for OAuth 2.0 authentication](#oauth-tutorial-additional-validations "#oauth-tutorial-additional-validations")

## Supported OAuth 2.0 configurations

Amazon MQ for RabbitMQ supports all [configurable variables](https://www.rabbitmq.com/docs/oauth2#variables-configurable "https://www.rabbitmq.com/docs/oauth2#variables-configurable") in RabbitMQ OAuth 2.0 plugin, with the following exceptions:

- `auth_oauth2.https.cacertfile`
- `auth_oauth2.oauth_providers.{id/index}.https.cacertfile`
- `management.oauth_client_secret`

Because Amazon MQ doesn't support this key, we don't support UAA as an IdP.

- `management.oauth_resource_servers.{id/index}.oauth_client_secret`
- `auth_oauth2.signing_keys.{id/index}`

## Additional validations for OAuth 2.0 authentication

Amazon MQ also enforces the following additional validations for OAuth 2.0 authentication:

- All URLs need to start with `https://`.
- Supported signature algorithms: `Ed25519`, `Ed25519ph`, `Ed448`, `Ed448ph`, `EdDSA`, `ES256K`, `ES256`, `ES384`, `ES512`, `HS256`, `HS384`, `HS512`, `PS256`, `PS384`, `PS512`, `RS256`, `RS384`, and `RS512`.
