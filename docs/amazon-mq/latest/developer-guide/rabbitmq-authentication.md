# Amazon MQ for RabbitMQ Authentication and Authorization

Amazon MQ for RabbitMQ supports the following authentication and authorization methods:

## Simple authentication and authorization

In this method, broker users are stored internally in the RabbitMQ broker and managed through the web
console or management API. Permissions for vhosts, exchanges, queues, and topics are configured directly
in RabbitMQ. This is the default method. For more information, see [Simple authentication and authorization](rabbitmq-simple-auth-broker-users.md "rabbitmq-simple-auth-broker-users.md").

## OAuth 2.0 authentication and authorization

In this method, broker users and their permissions are managed by an external OAuth 2.0 identity provider (IdP). User authentication and resource permissions for vhosts, exchanges, queues, and topics are centralized through the OAuth 2.0 provider's scope system. This simplifies user management and enables integration with existing identity systems. For more information, see [OAuth 2.0 authentication and authorization](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md").

## LDAP authentication and authorization

In this method, broker users and their permissions are managed by an external LDAP directory service. User authentication and resource permissions are centralized through the LDAP server, allowing users to access RabbitMQ using their existing directory service credentials. For more information, see [LDAP authentication and authorization](ldap-for-amq-for-rabbitmq.md "ldap-for-amq-for-rabbitmq.md").

## HTTP authentication and authorization

In this method, broker users and their permissions are managed by an external HTTP server. User authentication and resource permissions are centralized through the HTTP server, allowing users to access RabbitMQ using their own Authentication and Authorization provider. For more information about this method, see [HTTP authentication and authorization](http-for-amq-for-rabbitmq.md "http-for-amq-for-rabbitmq.md").

## SSL certificate authentication

Amazon MQ supports mutual TLS (mTLS) for RabbitMQ brokers. The SSL authentication plugin uses client certificates from mTLS connections to authenticate users. In this method, broker users are authenticated using X.509 client certificates instead of username and password credentials. The client's certificate is validated against a trusted Certificate Authority (CA), and the username is extracted from a field in the certificate, such as the Common Name (CN) or Subject Alternative Name (SAN). This method provides strong authentication without transmitting credentials over the network. For more information, see [SSL certificate authentication](ssl-for-amq-for-rabbitmq.md "ssl-for-amq-for-rabbitmq.md").

###### Note

RabbitMQ supports multiple authentication and authorization methods to be used simultaneously. For example, you can enable both OAuth 2.0 and simple (internal) authentication. For more information, see the OAuth 2.0 tutorial section on [enabling both OAuth 2.0 and simple (internal) authentication](oauth-tutorial.md#oauth-tutorial-config-both-auth-methods-using-cli "oauth-tutorial.md#oauth-tutorial-config-both-auth-methods-using-cli") and the [RabbitMQ access control documentation](https://www.rabbitmq.com/docs/access-control "https://www.rabbitmq.com/docs/access-control").

Amazon MQ recommends creating an internal user when testing authentication configurations. This allows access configuration to be validated using RabbitMQ management API. For more information, see [Access validation](arn-support-rabbitmq-configuration.md#access-validation "arn-support-rabbitmq-configuration.md#access-validation").
