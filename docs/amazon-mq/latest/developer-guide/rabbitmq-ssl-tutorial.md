# Using SSL certificate authentication for Amazon MQ for RabbitMQ

This tutorial describes how to configure SSL certificate authentication for your Amazon MQ for RabbitMQ brokers using a private certificate authority.

###### Note

The SSL certificate authentication plugin is only available for Amazon MQ for RabbitMQ version 4 and above.

###### On this page

- [Prerequisites to configure SSL certificate authentication](#rabbitmq-ssl-tutorial-prerequisites "#rabbitmq-ssl-tutorial-prerequisites")
- [Configuring SSL certificate authentication in RabbitMQ using AWS CLI](#rabbitmq-ssl-tutorial-configure-cli "#rabbitmq-ssl-tutorial-configure-cli")

## Prerequisites to configure SSL certificate authentication

SSL certificate authentication uses mutual TLS (mTLS) to authenticate clients using X.509 certificates. You can set up the AWS resources required in this tutorial by deploying the [AWS CDK stack for Amazon MQ for RabbitMQ mTLS integration](https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-mtls-sample/ "https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-mtls-sample/").

This CDK stack automatically creates all the necessary AWS resources including certificate authority, client certificates, and IAM roles. See the package README for a complete list of resources created by the stack.

###### Note

Before deploying the CDK stack, set the `RABBITMQ_TEST_USER_NAME` environment variable. This value will be used as the Common Name (CN) in the client certificate and must match the username you use in the tutorial steps. For example: `export RABBITMQ_TEST_USER_NAME="myuser"`

If you're setting up the resources manually instead of using the CDK stack, ensure you have the equivalent infrastructure in place before configuring SSL certificate authentication on your Amazon MQ for RabbitMQ brokers.

### Prerequisite to set up Amazon MQ

AWS CLI version >= 2.28.23 to make adding a username and password optional during broker creation.

## Configuring SSL certificate authentication in RabbitMQ using AWS CLI

This procedure uses AWS CLI to create and configure the necessary resources. In the following procedure, make sure to replace the placeholder values, such as configurationID and Revision, `<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>` and `<2>`, with their actual values.

1. Create a new configuration using the `create-configuration` AWS CLI command as shown in the following example.

```

aws mq create-configuration \
  --name "rabbitmq-ssl-config" \
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
        "Description": "Auto-generated default for rabbitmq-ssl-config on RabbitMQ 4.2",
        "Revision": 1
    },
    "Name": "rabbitmq-ssl-config"
}

```

2. Create a configuration file called `rabbitmq.conf` to use SSL certificate authentication, as shown in the following example. Replace all placeholder values in the template (marked with `${...}`) with actual values from your deployed AWS CDK prerequisite stack outputs or equivalent infrastructure.

```

auth_mechanisms.1 = EXTERNAL
ssl_cert_login_from = common_name

auth_backends.1 = internal

# Reject if no client cert
ssl_options.verify = verify_peer
ssl_options.fail_if_no_peer_cert = true

# AWS integration for secure credential retrieval
# For more information, see https://github.com/amazon-mq/rabbitmq-aws

# FIXME: Replace the ${...} placeholders with actual ARN values
# from your deployed prerequisite CDK stack outputs.
aws.arns.assume_role_arn = ${AmazonMqAssumeRoleArn}
aws.arns.ssl_options.cacertfile = ${CaCertArn}

```

3. Update the configuration using the `update-configuration` AWS CLI command as shown in the following example. In this command, add the configuration ID you received in the response of Step 1 of this procedure. For example, `c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca`.

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
    "Name": "rabbitmq-ssl-config",
    "Warnings": []
}

```

4. Create a broker with the SSL certificate authentication configuration you created in Step 2 of this procedure. To do this, use the `create-broker` AWS CLI command as shown in the following example. In this command, provide the configuration ID and revision number you obtained in the responses of Step 1 and 2 respectively. For example, `c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca` and `2`.

```

aws mq create-broker \
  --broker-name "rabbitmq-ssl-test-1" \
  --engine-type "RABBITMQ" \
  --engine-version "4.2" \
  --host-instance-type "mq.m7g.large" \
  --deployment-mode "SINGLE_INSTANCE" \
  --logs '{"General": true}' \
  --publicly-accessible \
  --configuration '{"Id": "<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>","Revision": <2>}' \
  --users '[{"Username":"testuser","Password":"testpassword"}]'

```

This command returns a response similar to the following example.

```

{
    "BrokerArn": "arn:aws:mq:us-west-2:123456789012:broker:rabbitmq-ssl-test-1:b-2a1b5133-a10c-49d2-879b-8c176c34cf73",
    "BrokerId": "b-2a1b5133-a10c-49d2-879b-8c176c34cf73"
}

```

5. Verify that the broker's status transitions from `CREATION_IN_PROGRESS` to `RUNNING`, using the `describe-broker` AWS CLI command as shown in the following example. In this command, provide the broker ID you obtained in the result of the previous step. For example, `b-2a1b5133-a10c-49d2-879b-8c176c34cf73`.

```

aws mq describe-broker \
  --broker-id "<b-2a1b5133-a10c-49d2-879b-8c176c34cf73>"

```

This command returns a response similar to the following example. The following response is an abbreviated version of the complete output that the `describe-broker` command returns. This response shows the broker status and the authentication strategy used to secure the broker. In this case, the `config_managed` authentication strategy indicates that the broker uses SSL certificate authentication method.

```

{
    "AuthenticationStrategy": "config_managed",
    ...,
    "BrokerState": "RUNNING",
    ...
}

```

6. Verify SSL certificate authentication with the following `ssl.sh` script.

Use this bash script to test connectivity to your Amazon MQ for RabbitMQ broker. This script uses your client certificate for authentication and verifies if the connection was properly configured. If it's successfully configured, you'll see your broker publish and consume messages.

If you receive an `ACCESS_REFUSED` error, you can troubleshoot your configuration settings by using the CloudWatch logs for your broker. You can find the link for the CloudWatch log group for your broker in the Amazon MQ console.

In this script, you'll need to provide the following values:

    * `USERNAME`: The common name (CN) from your client certificate.
    * `CLIENT_KEYSTORE`: Path to your client keystore file (PKCS12 format). If you used the prerequisite CDK stack, the default path is `$(pwd)/certs/client-keystore.p12`.
    * `KEYSTORE_PASSWORD`: Password for your client keystore. If you used the prerequisite CDK stack, the default password is `changeit`.
    * `BROKER_DNS`: You can find this value under **Connections** on the broker details page of the Amazon MQ console.

```
#! /bin/bash
set -e

# Client information
## FIXME: Update this value with the client ID and secret of your confidential application client
USERNAME=`<client_cert_common_name>`
CLIENT_KEYSTORE=`$(pwd)/certs/client-keystore.p12`
KEYSTORE_PASSWORD=`changeit`

BROKER_DNS=`<broker_dns>`
CONNECTION_STRING=amqps://${BROKER_DNS}:5671

# Produce/consume messages using the above connection string
QUEUES_COUNT=1
PRODUCERS_COUNT=1
CONSUMERS_COUNT=1
PRODUCER_RATE=1

finch run --rm --ulimit nofile=40960:40960 \
    -v ${CLIENT_KEYSTORE}:/certs/client-keystore.p12:ro \
    -e JAVA_TOOL_OPTIONS="-Djavax.net.ssl.keyStore=/certs/client-keystore.p12 -Djavax.net.ssl.keyStorePassword=${KEYSTORE_PASSWORD} -Djavax.net.ssl.keyStoreType=PKCS12" \
    pivotalrabbitmq/perf-test:latest \
    --queue-pattern 'test-queue-cert-%d' --queue-pattern-from 1 --queue-pattern-to $QUEUES_COUNT \
    --producers $PRODUCERS_COUNT --consumers $CONSUMERS_COUNT \
    --id "cert-test${QUEUES_COUNT}q${PRODUCERS_COUNT}p${CONSUMERS_COUNT}c${PRODUCER_RATE}r" \
    --uri ${CONNECTION_STRING} \
    --sasl-external \
    --use-default-ssl-context \
    --flag persistent --rate $PRODUCER_RATE
```
