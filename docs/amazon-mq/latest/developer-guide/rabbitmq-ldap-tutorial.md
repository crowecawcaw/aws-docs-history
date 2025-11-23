# Using LDAP authentication and authorization for Amazon MQ for RabbitMQ

This tutorial describes how to configure LDAP authentication and authorization for your Amazon MQ for RabbitMQ brokers using AWS Managed Microsoft AD.

###### On this page

- [Prerequisites to configure LDAP authentication and authorization](#rabbitmq-ldap-tutorial-prerequisites "#rabbitmq-ldap-tutorial-prerequisites")
- [Configuring LDAP in RabbitMQ using AWS CLI](#rabbitmq-ldap-tutorial-configure-cli "#rabbitmq-ldap-tutorial-configure-cli")

## Prerequisites to configure LDAP authentication and authorization

You can set up the AWS resources required in this tutorial by deploying the [AWS CDK stack for Amazon MQ for RabbitMQ LDAP integration with AWS Managed Microsoft AD](https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-ldap-activedirectory-sample/ "https://github.com/aws-samples/amazon-mq-samples/blob/main/rabbitmq-samples/rabbitmq-ldap-activedirectory-sample/").

This CDK stack automatically creates all the necessary AWS resources including AWS Managed Microsoft AD, LDAP users and groups, Network Load Balancer, certificates, and IAM roles. See the package README for a complete list of resources created by the stack.

If you're setting up the resources manually instead of using the CDK stack, ensure you have the equivalent infrastructure in place before configuring LDAP on your Amazon MQ for RabbitMQ brokers.

### Prerequisite to set up Amazon MQ

AWS CLI version >= 2.28.23 to make adding a username and password optional during broker creation.

## Configuring LDAP in RabbitMQ using AWS CLI

This procedure uses AWS CLI to create and configure the necessary resources. In the following procedure, make sure to replace the placeholder values, such as configurationID and Revision, `<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>` and `<2>`, with their actual values.

1. Create a new configuration using the `create-configuration` AWS CLI command as shown in the following example.

```

aws mq create-configuration \
  --name "rabbitmq-ldap-config" \
  --engine-type "RABBITMQ" \
  --engine-version "3.13"

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
    "Description": "Auto-generated default for rabbitmq-ldap-config on RabbitMQ 3.13",
    "Revision": 1
    },
    "Name": "rabbitmq-ldap-config"
}

```

2. Create a configuration file called `rabbitmq.conf` to use LDAP as the authentication and authorization method, as shown in the following example. Replace all placeholder values in the template (marked with `${RabbitMqLdapTestStack.*}`) with actual values from your deployed AWS CDK prerequisite stack outputs or equivalent infrastructure.

```

auth_backends.1 = ldap

# LDAP authentication settings - For more information,
# see https://www.rabbitmq.com/docs/ldap#basic

# FIXME: Replace the ${RabbitMqLdapTestStack.*} placeholders with actual values
# from your deployed prerequisite CDK stack outputs.
auth_ldap.servers.1 = ${RabbitMqLdapTestStack.NlbDnsName}
auth_ldap.dn_lookup_bind.user_dn = ${RabbitMqLdapTestStack.DnLookupUserDn}
auth_ldap.dn_lookup_base = ${RabbitMqLdapTestStack.DnLookupBase}
auth_ldap.dn_lookup_attribute = ${RabbitMqLdapTestStack.DnLookupAttribute}
auth_ldap.port = 636
auth_ldap.use_ssl = true
auth_ldap.ssl_options.verify = verify_peer
auth_ldap.log = network

# AWS integration for secure credential retrieval
# - see: https://github.com/amazon-mq/rabbitmq-aws
# The aws plugin allows RabbitMQ to securely retrieve credentials and certificates
# from AWS services.

# Replace the ${RabbitMqLdapTestStack.*} placeholders with actual ARN values
# from your deployed prerequisite CDK stack outputs.
aws.arns.auth_ldap.ssl_options.cacertfile = ${RabbitMqLdapTestStack.CaCertArn}
aws.arns.auth_ldap.dn_lookup_bind.password = ${RabbitMqLdapTestStack.DnLookupUserPasswordArn}
aws.arns.assume_role_arn = ${RabbitMqLdapTestStack.AmazonMqAssumeRoleArn}

# LDAP authorization queries - For more information,
# see: https://www.rabbitmq.com/docs/ldap#authorisation

# FIXME: Replace the ${RabbitMqLdapTestStack.*} placeholders with actual group DN
# values from your deployed prerequisite CDK stack outputs
# Uses Active Directory groups created by the prerequisite CDK stack
auth_ldap.queries.tags = '''
[{administrator, {in_group, "${RabbitMqLdapTestStack.RabbitMqAdministratorsGroupDn}"}},
{management,    {in_group, "${RabbitMqLdapTestStack.RabbitMqMonitoringUsersGroupDn}"}}]
'''

# FIXME: This provides all authenticated users access to all vhosts
# - update to restrict access as required
auth_ldap.queries.vhost_access = '''
{constant, true}
'''

# FIXME: This provides all authenticated users full access to all
# queues and exchanges - update to restrict access as required
auth_ldap.queries.resource_access = '''
{for, [    {permission, configure, {constant, true}},
     {permission, write,
      {for, [{resource, queue,    {constant, true}},
             {resource, exchange, {constant, true}}]}},
     {permission, read,
      {for, [{resource, exchange, {constant, true}},
             {resource, queue,    {constant, true}}]}}
    ]
}
'''

# FIXME: This provides all authenticated users access to all topics
# - update to restrict access as required
auth_ldap.queries.topic_access = '''
{for, [{permission, write, {constant, true}},
     {permission, read,  {constant, true}}
    ]
}
'''

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
    "Arn": "arn:aws:mq:us-west-2:123456789012:configuration:c-b600ac8e-8183-4f74-a713-983e59f30e3d",
    "Created": "2025-07-17T16:57:04.520931+00:00",
    "Id": "c-b600ac8e-8183-4f74-a713-983e59f30e3d",
    "LatestRevision": {
        "Created": "2025-07-17T16:57:39.172000+00:00",
        "Revision": 2
    },
    "Name": "rabbitmq-ldap-config",
    "Warnings": []
}

```

4. Create a broker with the LDAP configuration you created in the Step 2 of this procedure. To do this, use the `create-broker` AWS CLI command as shown in the following example. In this command, provide the configuration ID and revision number you obtained in the responses of Step 1 and 2 respectively. For example, `c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca` and `2`.

```

aws mq create-broker \
 --broker-name "rabbitmq-ldap-test-1" \
 --engine-type "RABBITMQ" \
 --engine-version "3.13" \
 --host-instance-type "mq.m7g.large" \
 --deployment-mode "CLUSTER_MULTI_AZ" \
 --logs '{"General": true}' \
 --publicly-accessible \
 --configuration '{"Id": "<c-fa3390a5-7e01-4559-ae0c-eb15b38b22ca>","Revision": <2>}'

```

This command returns a response similar to the following example.

```

{
    "BrokerArn": "arn:aws:mq:us-west-2:123456789012:broker:rabbitmq-ldap-broker:b-2a1b5133-a10c-49d2-879b-8c176c34cf73",
    "BrokerId": "b-2a1b5133-a10c-49d2-879b-8c176c34cf73"
}

```

###### Broker naming restriction

The IAM role created by the prerequisite CDK stack restricts broker names to start with `rabbitmq-ldap-test`. Ensure your broker name follows this pattern or the IAM role will not have permission to assume the role for ARN resolution. 5. Verify that the broker's status transitions from `CREATION_IN_PROGRESS` to `RUNNING`, using the `describe-broker` AWS CLI command as shown in the following example. In this command, provide the broker ID you obtained in the result of the previous step For example, `b-2a1b5133-a10c-49d2-879b-8c176c34cf73`.

```

aws mq describe-broker \
 --broker-id "<b-2a1b5133-a10c-49d2-879b-8c176c34cf73>"

```

This command returns a response similar to the following example. The following response is an abbreviated version of the complete output that the `describe-broker` command returns. This response shows the broker status and the authentication strategy used to secure the broker. In this case, the `config_managed` authentication strategy indicates that the broker uses LDAP authentication method.

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

# FIXME: Replace ${RabbitMqLdapTestStack.ConsoleUserPasswordArn} with the actual ARN from your deployed prerequisite CDK stack outputs
CONSOLE_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id ${RabbitMqLdapTestStack.ConsoleUserPasswordArn} \
  --query 'SecretString' --output text)

# FIXME: Replace BrokerConsoleURL with the actual ConsoleURL retrieved by
# calling describe-broker for the broker created above
# Call management API /api/overview (should succeed)
curl -u RabbitMqConsoleUser:$CONSOLE_PASSWORD \
  https://${BrokerConsoleURL}/api/overview

# Try to create a user (should fail - console user only has monitoring permissions)
curl -u RabbitMqConsoleUser:$CONSOLE_PASSWORD \
  -X PUT https://${BrokerConsoleURL}/api/users/testuser \
  -H "Content-Type: application/json" \
  -d '{"password":"testpass","tags":"management"}'

```
