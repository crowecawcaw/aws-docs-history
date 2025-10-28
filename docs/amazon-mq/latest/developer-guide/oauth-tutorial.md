# Using OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ

This tutorial describes how to configure [OAuth 2.0 authentication](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md") for your Amazon MQ for RabbitMQ brokers using Amazon Cognito as the OAuth 2.0 provider.

###### Note

Amazon Cognito is not available in China (Beijing) and China (Ningxia).

###### Important

This tutorial is specific to Amazon Cognito, but you can use other identity providers (IdPs). For more information, see [OAuth 2.0 Authentication Examples](https://www.rabbitmq.com/docs/oauth2-examples "https://www.rabbitmq.com/docs/oauth2-examples").

###### On this page

- [Prerequisites to configure OAuth 2.0 authentication](#oauth-tutorial-prerequisites "#oauth-tutorial-prerequisites")
- [Configuring OAuth 2.0 authentication with Amazon Cognito using AWS CLI](#oauth-tutorial-config-cognito-using-cli "#oauth-tutorial-config-cognito-using-cli")
- [Configuring OAuth 2.0 and simple authentication with Amazon Cognito](#oauth-tutorial-config-both-auth-methods-using-cli "#oauth-tutorial-config-both-auth-methods-using-cli")

## Prerequisites to configure OAuth 2.0 authentication

You can set the Amazon Cognito resources required in this tutorial by deploying the AWS CDK stack, [Amazon Cognito stack for RabbitMQ OAuth 2 plugin](https://github.com/aws-samples/amazon-mq-samples/tree/main/rabbitmq-samples/rabbitmq-oauth2-cognito-sample "https://github.com/aws-samples/amazon-mq-samples/tree/main/rabbitmq-samples/rabbitmq-oauth2-cognito-sample"). If you're setting up Amazon Cognito manually, make sure that you fulfill the following prerequisites before configuring OAuth 2.0 on your Amazon MQ for RabbitMQ brokers:

###### Prerequisites to set up Amazon Cognito

- Set up an Amazon Cognito endpoint by creating a user pool. To do this, see the blog titled [How to use OAuth 2.0 in Amazon Cognito: Learn about the different OAuth 2.0 grants](https://aws.amazon.com/blogs/security/how-to-use-oauth-2-0-in-amazon-cognito-learn-about-the-different-oauth-2-0-grants/ "https://aws.amazon.com/blogs/security/how-to-use-oauth-2-0-in-amazon-cognito-learn-about-the-different-oauth-2-0-grants/").
- Create a resource server called `rabbitmq` in the user pool with the following scopes defined: `read:all`, `write:all`, `configure:all`,
  and `tag:administrator`. These scopes will be associated with RabbitMQ permissions.

For information about creating a resource server, see [Defining a resource server for your user pool (AWS Management Console)](../../../cognito/latest/developerguide/cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-console "../../../cognito/latest/developerguide/cognito-user-pools-define-resource-servers.md#cognito-user-pools-define-resource-servers-console") in the _Amazon Cognito Developer Guide_.

- Create the following application clients:
  - Application client for the user pool of type `Machine-to-Machine application`. This is a confidential client with a client secret that will be used for RabbitMQ AMQP clients. For more information about application clients and creating one, see [App client types](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md#user-pool-settings-client-app-client-types "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md#user-pool-settings-client-app-client-types") and [Creating an app client](../../../cognito/latest/developerguide/user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-console-create "../../../cognito/latest/developerguide/user-pool-settings-client-apps.md#cognito-user-pools-app-idp-settings-console-create").
  - Application client for the user pool of type `Single-page application`. This is a public client that will be used to log in users into the RabbitMQ management console. You must update this application client to include the endpoint of the Amazon MQ for RabbitMQ broker you'll create in the following procedure as an allowed callback URL. For more information, see [Setting up managed login with the Amazon Cognito console](../../../cognito/latest/developerguide/cognito-user-pools-managed-login.md#set-up-managed-login "../../../cognito/latest/developerguide/cognito-user-pools-managed-login.md#set-up-managed-login").

###### Prerequisite to set up Amazon MQ

- A working [Docker](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/") installation to run a bash script that verifies whether or not the OAuth 2.0 setup is successful.
- AWS CLI version >= `2.28.23` to make adding a username and password optional during broker creation.

## Configuring OAuth 2.0 authentication with Amazon Cognito using AWS CLI

The following procedure shows how to set up OAuth 2.0 authentication for your Amazon MQ for RabbitMQ brokers using Amazon Cognito as the IdP. This procedure uses AWS CLI to create and configure the necessary resources.

In the following procedure, make sure to replace the placeholder values, such as configurationID and Revision, `<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>` and `<2>`, with their actual values.

1. Create a new configuration using the [create-configuration](../../../cli/latest/reference/mq/create-configuration.md "../../../cli/latest/reference/mq/create-configuration.md") AWS CLI command as shown in the following example.

```
aws mq create-configuration \
  --name "`rabbitmq-oauth2-config`" \
  --engine-type "RABBITMQ" \
  --engine-version "3.13"
```

This command returns a response similar to the following example.

```
{
    "Arn": "arn:aws:mq:`us-west-2`:`123456789012`:configuration:c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca",
    "AuthenticationStrategy": "simple",
    "Created": "2025-07-17T16:03:01.759943+00:00",
    "Id": "**c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca**",
    "LatestRevision": {
    "Created": "2025-07-17T16:03:01.759000+00:00",
    "Description": "Auto-generated default for rabbitmq-oauth2-config on RabbitMQ 3.13",
    "Revision": 1
    },
    "Name": "rabbitmq-oauth2-config"
}
```

2. Create a configuration file called `rabbitmq.conf` to use OAuth 2.0 as the authentication and authorization method, as shown in the following example.

```
auth_backends.1 = oauth2

# FIXME: Update this value with the token signing key URL of your Amazon Cognito user pool.
# If you used the AWS CDK stack to deploy Amazon Cognito, this is one of the stack outputs.
auth_oauth2.jwks_url = `${RabbitMqOAuth2TestStack.JwksUri}`
auth_oauth2.resource_server_id = rabbitmq
# Amazon Cognito does not include an audience field in access tokens
auth_oauth2.verify_aud = false

# Amazon Cognito does not allow * in its custom scopes. Use aliases to translate between Amazon Cognito and RabbitMQ.
auth_oauth2.scope_prefix = rabbitmq/
auth_oauth2.scope_aliases.1.alias = rabbitmq/read:all
auth_oauth2.scope_aliases.1.scope = rabbitmq/read:*/*
auth_oauth2.scope_aliases.2.alias = rabbitmq/write:all
auth_oauth2.scope_aliases.2.scope = rabbitmq/write:*/*
auth_oauth2.scope_aliases.3.alias = rabbitmq/configure:all
auth_oauth2.scope_aliases.3.scope = rabbitmq/configure:*/*

# Allow OAuth 2.0 login for RabbitMQ management console
management.oauth_enabled = true
# FIXME: Update this value with the client ID of your public application client
management.oauth_client_id = `${RabbitMqOAuth2TestStack.ManagementConsoleAppClientId}`
# FIXME: Update this value with the base JWKS URI (without /.well-known/jwks.json)
auth_oauth2.issuer = `${RabbitMqOAuth2TestStack.Issuer}`
management.oauth_scopes = rabbitmq/tag:administrator
```

This configuration uses [scope aliases](https://www.rabbitmq.com/docs/oauth2#scope-translation "https://www.rabbitmq.com/docs/oauth2#scope-translation") to map the scopes defined in Amazon Cognito to RabbitMQ compatible scopes. 3. Update the configuration using the [update-configuration](../../../cli/latest/reference/mq/update-configuration.md "../../../cli/latest/reference/mq/update-configuration.md") AWS CLI command as shown in the following example. In this command, add the configuration ID you received in the response of Step 1 of this procedure. For example, `c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca`.

```
aws mq update-configuration \
  --configuration-id "`<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>`" \
  --data "$(cat rabbitmq.conf | base64 --wrap=0)"
```

This command returns a response similar to the following example.

```
{
    "Arn": "arn:aws:mq:`us-west-2`:`123456789012`:configuration:c-b600ac8e-8183-4f74-a713-983e59f30e3d",
    "Created": "2025-07-17T16:57:04.520931+00:00",
    "Id": "c-b600ac8e-8183-4f74-a713-983e59f30e3d",
    "LatestRevision": {
        "Created": "2025-07-17T16:57:39.172000+00:00",
        "Revision": **2**
    },
    "Name": "rabbitmq-oauth2-config",
    "Warnings": []
}
```

4. Create a broker with the OAuth 2.0 configuration you created in the Step 2 of this procedure. To do this, use the [create-broker](../../../cli/latest/reference/mq/create-broker.md "../../../cli/latest/reference/mq/create-broker.md") AWS CLI command as shown in the following example. In this command, provide the configuration ID and revision number you obtained in the responses of Step 1 and 2 respectively. For example, `c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca` and `2`.

```
aws mq create-broker \
 --broker-name "rabbitmq-oauth2-broker" \
 --engine-type "RABBITMQ" \
 --engine-version "3.13" \
 --host-instance-type "mq.m7g.large" \
 --deployment-mode "CLUSTER_MULTI_AZ" \
 --logs '{"General": true}' \
 --publicly-accessible \
 --configuration '{"Id": "`<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>`","Revision": `<2>`}' \

```

This command returns a response similar to the following example.

```
{
    "BrokerArn": "arn:aws:mq:`us-west-2`:`123456789012`:broker:rabbitmq-oauth2-broker:b-2a1b5133-a10c-49d2-879b-8c176c34cf73",
    "BrokerId": "b-2a1b5133-a10c-49d2-879b-8c176c34cf73"
}
```

5. Verify that the broker's status transitions from `CREATION_IN_PROGRESS` to `RUNNING`, using the [describe-broker](../../../cli/latest/reference/mq/describe-broker.md "../../../cli/latest/reference/mq/describe-broker.md") AWS CLI command as shown in the following example. In this command, provide the broker ID you obtained in the result of the previous step For example, `b-2a1b5133-a10c-49d2-879b-8c176c34cf73`.

```
aws mq describe-broker \
 --broker-id "`<b-2a1b5133-a10c-49d2-879b-8c176c34cf73>`"
```

This command returns a response similar to the following example. The following response is an abbreviated version of the complete output that the `describe-broker` command returns. This response shows the broker status and the authentication strategy used to secure the broker. In this case, the `config_managed` authentication strategy indicates that the broker uses OAuth 2 authentication method.

```
{
    "AuthenticationStrategy": "config_managed",
    ...,
    "BrokerState": "RUNNING",
    ...
}
```

To log in to the RabbitMQ management console using OAuth2,
the broker endpoint needs to be added as a valid callback URL in the corresponding Amazon Cognito app client.
For more information, refer to Step 5 in the setup of our sample
[Amazon Cognito CDK stack](https://github.com/aws-samples/amazon-mq-samples/tree/main/rabbitmq-samples/rabbitmq-oauth2-cognito-sample#step-5-update-callback-urls-if-using-placeholder-urls "https://github.com/aws-samples/amazon-mq-samples/tree/main/rabbitmq-samples/rabbitmq-oauth2-cognito-sample#step-5-update-callback-urls-if-using-placeholder-urls"). 6. Verify OAuth 2.0 authentication and authorization with the following `perf-test.sh` script.

Use this bash script to test connectivity to your Amazon MQ for RabbitMQ broker. This script obtains a token from Amazon Cognito and verifies if the connection was properly configured. If it’s successfully configured, you’ll see your broker publish and consume messages.

If you receive an `ACCESS_REFUSED` error, you can troubleshoot your configuration settings by using the CloudWatch logs for your broker. You can find the link for the CloudWatch log group for your broker in the Amazon MQ console.

In this script, you'll need to provide the following values:

    * `CLIENT_ID` and `CLIENT_SECRET`: You can find these values on the **App clients** page of the Amazon Cognito console.
    * Cognito domain: You can find this on the Amazon Cognito console. Under **Branding**, choose **Domain**. On the **Domain** page, you can find this value under the **Resource servers** section.
    * Amazon MQ broker endpoint: You can find this value under **Connections** on the broker details page of the Amazon MQ console.

```
#! /bin/bash
set -e

# Client information
## FIXME: Update this value with the client ID and secret of your confidential application client
CLIENT_ID=`${RabbitMqOAuth2TestStack.AmqpAppClientId}`
CLIENT_SECRET=`${RabbitMqOAuth2TestStack.AmqpAppClientSecret}`

# FIXME: Update this value with the domain of your Amazon Cognito user pool
RESPONSE=$(curl -X POST `${RabbitMqOAuth2TestStack.TokenEndpoint}` \
                -H "Content-Type: application/x-www-form-urlencoded" \
                -d "grant_type=client_credentials&client_id=`${CLIENT_ID}`&client_secret=`${CLIENT_SECRET}`&scope=rabbitmq/configure:all rabbitmq/read:all rabbitmq/tag:administrator rabbitmq/write:all")


# Extract the access_token from the response.
# This token will be passed in the password field when connecting to the broker.
# Note that the username is left blank, the field is ignored by the plugin.
BROKER_PASSWORD=$(echo ${RESPONSE} | jq -r '.access_token')

# FIXME: Update this value with the endpoint of your broker. For example, `b-89424106-7e0e-4abe-8e98-8de0dada7630.mq.us-east-1.on.aws`.
BROKER_DNS=`<broker_dns>`
CONNECTION_STRING=amqps://:${BROKER_PASSWORD}@${BROKER_DNS}:5671

# Produce/consume messages using the above connection string
QUEUES_COUNT=1
PRODUCERS_COUNT=1
CONSUMERS_COUNT=1
PRODUCER_RATE=1

docker run -it --rm --ulimit nofile=40960:40960 pivotalrabbitmq/perf-test:latest \
    --queue-pattern 'test-queue-%d' --queue-pattern-from 1 --queue-pattern-to $QUEUES_COUNT \
    --producers $PRODUCERS_COUNT --consumers $CONSUMERS_COUNT \
    --id "test${QUEUES_COUNT}q${PRODUCERS_COUNT}p${CONSUMERS_COUNT}c${PRODUCER_RATE}r" \
    --uri ${CONNECTION_STRING} \
    --flag persistent --rate $PRODUCER_RATE
```

## Configuring OAuth 2.0 and simple authentication with Amazon Cognito

When you create a broker with OAuth 2.0 authentication, you can specify one of the following authentication methods:

- **OAuth 2.0 only**: To use this method, don't provide a username and password while creating the broker. The [previous procedure](#oauth-tutorial-config-cognito-using-cli "#oauth-tutorial-config-cognito-using-cli") shows how to use only OAuth 2.0 authentication method.
- **Both OAuth 2.0 and simple authentication**: To use this method, provide a username and password while creating the broker. Also, add `auth_backends.2 = internal` to your broker configuration, as shown in the following procedure.

In the following procedure, make sure to replace the placeholder values, such as `<ConfigurationId>` and `<Revision>`, with their actual values.

1. To use both the authentication methods, create your broker configuration, as shown in the following example.

```
auth_backends.1 = oauth2
auth_backends.2 = internal

# FIXME: Update this value with the token signing key URL of your Amazon Cognito user pool
auth_oauth2.jwks_url = `${RabbitMqOAuth2TestStack.JwksUri}`
auth_oauth2.resource_server_id = rabbitmq
auth_oauth2.verify_aud = false

auth_oauth2.scope_prefix = rabbitmq/
auth_oauth2.scope_aliases.1.alias = rabbitmq/read:all
auth_oauth2.scope_aliases.1.scope = rabbitmq/read:*/*
auth_oauth2.scope_aliases.2.alias = rabbitmq/write:all
auth_oauth2.scope_aliases.2.scope = rabbitmq/write:*/*
auth_oauth2.scope_aliases.3.alias = rabbitmq/configure:all
auth_oauth2.scope_aliases.3.scope = rabbitmq/configure:*/*
```

This configuration uses [scope aliases](https://www.rabbitmq.com/docs/oauth2#scope-translation "https://www.rabbitmq.com/docs/oauth2#scope-translation") to map the scopes defined in Amazon Cognito to RabbitMQ compatible scopes. 2. Create a broker that uses both the authentication methods, as shown in the following example.

```
aws mq create-broker \
 --broker-name "rabbitmq-oauth2-broker-with-internal-user" \
 --engine-type "RABBITMQ" \
 --engine-version "3.13" \
 --host-instance-type "mq.m7g.large" \
 --deployment-mode "CLUSTER_MULTI_AZ" \
 --logs '{"General": true}' \
 --publicly-accessible \
 --configuration '{"Id": "`<ConfigurationId>`","Revision": `<Revision>`}' \
 --users '[{"Username":"`<myUser>`","Password":"`<myPassword11>`"}]'
```

3. Verify the broker status and the configuration for setting up the authentication method was successful as described in Steps 5 and 6 of the [Configuring OAuth 2.0 authentication with Amazon Cognito](#oauth-tutorial-config-cognito-using-cli "#oauth-tutorial-config-cognito-using-cli") procedure.
