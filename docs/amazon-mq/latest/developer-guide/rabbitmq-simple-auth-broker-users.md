# Simple authentication and authorization

## Amazon MQ for RabbitMQ broker users

###### Note

This topic describes managing broker users with RabbitMQ's default internal authentication and authorization mechanism. For information about all supported authentication and authorization methods, see [Amazon MQ for RabbitMQ Authentication and Authorization](rabbitmq-authentication.md "rabbitmq-authentication.md").

Every AMQP 0-9-1 client connection has an associated user. This user must be authenticated.
Each client connection also targets a virtual host (vhost). The user must have a set of permissions for this vhost.
A user may have permission to **configure**,
**write** to, and **read** from queues and exchanges
in a vhost. You specify user credentials and the target vhost when the connection is established.

When you first create an Amazon MQ for RabbitMQ broker, Amazon MQ uses the sign-in credentials you provide to create a RabbitMQ user with the
`administrator` tag. You can then add and manage users via the RabbitMQ [management API](https://www.rabbitmq.com/management.html "https://www.rabbitmq.com/management.html") or the
RabbitMQ web console. You can also use the RabbitMQ web console or the management API to set or modify user permissions and tags.

###### Note

RabbitMQ users will not be stored or displayed via the Amazon MQ [Users](../api-reference/brokers-broker-id-users.md "../api-reference/brokers-broker-id-users.md") API.

###### Important

Amazon MQ for RabbitMQ does not support the username "guest", and will
delete the default guest account when you create a new broker.
Amazon MQ will also periodically delete any customer created account called "guest".

To create a new user with the RabbitMQ management API, use the following API endpoint and request body.
Replace `username` and `password` with your new sign-in credentials.

```
PUT /api/users/`username` HTTP/1.1

    {"password":"`password`","tags":"administrator"}
```

###### Important

- Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames.
  Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for
  private or sensitive data.
- If you've forgotten the admin password you set while creating the broker, you cannot reset your credentials.
  If you've created multiple administrators, you can log in using another admin user and reset or recreate your credentials.
  If you have only one admin user, you must delete the broker and create a new one with new credentials. We recommend consuming or backing up messages
  before deleting the broker.

The `tags` key is mandatory, and is a comma-separated list of tags for the user. Amazon MQ supports
`administrator`, `management`, `monitoring`, and `policymaker` user tags.

You can set permissions for an individual user by using the following API endpoint and request body. Replace
`vhost` and `username` with your information. For the default vhost `/`, use `%2F`.

```
PUT /api/permissions/`vhost`/`username` HTTP/1.1

    {"configure":".*","write":".*","read":".*"}
```

###### Note

The `configure`, `read`, and `write` keys are all mandatory.

By using the wildcard `.*` value, this operation will grant read, write, and configure permissions for all queues in the specified vhost to the user.
For more information about managing users via the RabbitMQ management API, see [RabbitMQ Management HTTP API](https://rawcdn.githack.com/rabbitmq/rabbitmq-server/main/deps/rabbitmq_management/priv/www/api/index.html "https://rawcdn.githack.com/rabbitmq/rabbitmq-server/main/deps/rabbitmq_management/priv/www/api/index.html").
