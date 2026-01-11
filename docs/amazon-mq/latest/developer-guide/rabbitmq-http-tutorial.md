# Using HTTP authentication and authorization for Amazon MQ for RabbitMQ

This tutorial describes how to configure HTTP authentication and authorization for your Amazon MQ for RabbitMQ brokers using an external HTTP server.

###### Note

The HTTP authentication plugin is only available for Amazon MQ for RabbitMQ version 4 and above.

###### On this page

- [Prerequisites to configure HTTP authentication and authorization](#rabbitmq-http-tutorial-prerequisites "#rabbitmq-http-tutorial-prerequisites")
- [Configuring HTTP authentication in RabbitMQ using AWS CLI](#rabbitmq-http-tutorial-configure-cli "#rabbitmq-http-tutorial-configure-cli")

## Prerequisites to configure HTTP authentication and authorization

You can set up the AWS resources required in this tutorial by deploying the [AWS CDK stack for Amazon MQ for RabbitMQ HTTP authentication integration](https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-http-sample/ "https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-http-sample/").

This CDK stack automatically creates all the necessary AWS resources including the HTTP authentication server, certificates, and IAM roles. See the package README for a complete list of resources created by the stack.

If you're setting up the resources manually instead of using the CDK stack, ensure you have the equivalent infrastructure in place before configuring HTTP authentication on your Amazon MQ for RabbitMQ brokers.

### Prerequisite to set up Amazon MQ

AWS CLI version >= 2.28.23 to make adding a username and password optional during broker creation.

## Configuring HTTP authentication in RabbitMQ using AWS CLI

This procedure uses AWS CLI to create and configure the necessary resources. In the following procedure, make sure to replace the placeholder values with their actual values.

1. Create a new configuration using the `create-configuration` AWS CLI command as shown in the following example.

```

aws mq create-configuration \
  --name "rabbitmq-http-config" \
  --engine-type "RABBITMQ" \
  --engine-version "4.2"

```

This command returns a response similar to the following example.

```

{
    "Arn": "arn:aws:mq:us-west-2:123456789012:configuration:c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca",
    "AuthenticationStrategy": "simple",
    "Created": "2025-07-17T16:03:01.759943+00:00",
    "Id": "c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca",
    "LatestRevision": {
        "Created": "2025-07-17T16:03:01.759000+00:00",
        "Description": "Auto-generated default for rabbitmq-http-config on RabbitMQ 4.2",
        "Revision": 1
    },
    "Name": "rabbitmq-http-config"
}

```

2. Create a configuration file called `rabbitmq.conf` to use HTTP as the authentication and authorization method, as shown in the following example. Replace all placeholder values in the template (marked with `${...}`) with actual values from your deployed AWS CDK prerequisite stack outputs or equivalent infrastructure.

```

auth_backends.1 = cache
auth_backends.2 = http
auth_cache.cached_backend = http

# HTTP authentication settings
# For more information, see https://github.com/rabbitmq/rabbitmq-auth-backend-http

# FIXME: Replace the ${...} placeholders with actual values
# from your deployed prerequisite CDK stack outputs.
auth_http.http_method = post
auth_http.user_path = ${HttpServerUserPath}
auth_http.vhost_path = ${HttpServerVhostPath}
auth_http.resource_path = ${HttpServerResourcePath}
auth_http.topic_path = ${HttpServerTopicPath}

# TLS/HTTPS configuration
auth_http.ssl_options.verify = verify_peer
auth_http.ssl_options.sni = test.amazonaws.com

# AWS integration for secure credential retrieval
# For more information, see https://github.com/amazon-mq/rabbitmq-aws

# Replace the ${...} placeholders with actual ARN values
# from your deployed prerequisite CDK stack outputs.
aws.arns.assume_role_arn = ${AmazonMqAssumeRoleArn}
aws.arns.auth_http.ssl_options.cacertfile = ${CaCertArn}

```

3. Update the configuration using the `update-configuration` AWS CLI command. Use the configuration ID from Step 3.

```

aws mq update-configuration \
  --configuration-id "<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>" \
  --data "$(cat rabbitmq.conf | base64 --wrap=0)"

```

This command returns a response similar to the following example.

```

{
    "Arn": "arn:aws:mq:us-west-2:123456789012:configuration:c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca",
    "Created": "2025-07-17T16:57:04.520931+00:00",
    "Id": "c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca",
    "LatestRevision": {
        "Created": "2025-07-17T16:57:39.172000+00:00",
        "Revision": 2
    },
    "Name": "rabbitmq-http-config",
    "Warnings": []
}

```

4. Create a broker with the HTTP configuration. Use the configuration ID and revision number from the previous steps.

```

aws mq create-broker \
  --broker-name "rabbitmq-http-test-1" \
  --engine-type "RABBITMQ" \
  --engine-version "4.2" \
  --host-instance-type "mq.m7g.large" \
  --deployment-mode "SINGLE_INSTANCE" \
  --logs '{"General": true}' \
  --publicly-accessible \
  --configuration '{"Id": "<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>","Revision": <2>}'

```

This command returns a response similar to the following example.

```

{
    "BrokerArn": "arn:aws:mq:us-west-2:123456789012:broker:rabbitmq-http-test-1:b-2a1b5133-a10c-49d2-879b-8c176c34cf73",
    "BrokerId": "b-2a1b5133-a10c-49d2-879b-8c176c34cf73"
}

```

5. Verify that the broker's status transitions from `CREATION_IN_PROGRESS` to `RUNNING`, using the `describe-broker` AWS CLI command.

```

aws mq describe-broker \
  --broker-id "<b-2a1b5133-a10c-49d2-879b-8c176c34cf73>"

```

This command returns a response similar to the following example. The `config_managed` authentication strategy indicates that the broker uses HTTP authentication method.

```

{
    "AuthenticationStrategy": "config_managed",
    ...,
    "BrokerState": "RUNNING",
    ...
}

```

6. Validate RabbitMQ access using one of the test users created by the prerequisite CDK stack

```

# FIXME: Replace ${RabbitMqHttpAuthElbStack.ConsoleUserPasswordArn} with the actual ARN from your deployed prerequisite CDK stack outputs
CONSOLE_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id ${RabbitMqHttpAuthElbStack.ConsoleUserPasswordArn} \
  --query 'SecretString' --output text)

# FIXME: Replace BrokerConsoleURL with the actual ConsoleURL retrieved by
# calling describe-broker for the broker created above
# Call management API /api/overview (should succeed)
curl -u RabbitMqConsoleUser:$CONSOLE_PASSWORD \
  https://${BrokerConsoleURL}/api/overview

# Try to create a vhost (should fail - console user only has management permissions)
curl -u RabbitMqConsoleUser:$CONSOLE_PASSWORD \
  -X PUT https://${BrokerConsoleURL}/api/vhosts/test-vhost \
  -H "Content-Type: application/json" \
  -d '{}'

```
