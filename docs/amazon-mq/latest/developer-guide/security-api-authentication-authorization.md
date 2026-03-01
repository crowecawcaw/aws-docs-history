# API authentication and authorization for Amazon MQ

Amazon MQ uses standard AWS request signing for API authentication. For more
information, see [Signing AWS
API Requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md") in the _AWS General Reference_.

###### Note

Currently, Amazon MQ doesn't support IAM authentication using resource-based
permissions or resource-based policies.

To authorize AWS users to work with brokers, configurations, and users, you must
edit your IAM policy permissions.

###### Topics

- [IAM Permissions Required to Create an Amazon MQ Broker](#security-permissions-required-to-create-broker "#security-permissions-required-to-create-broker")
- [Amazon MQ REST API permissions reference](#security-api-permissions-reference "#security-api-permissions-reference")
- [Amazon MQ additional permissions reference](#security-amq-additional-permissions "#security-amq-additional-permissions")
- [Resource-level permissions for Amazon MQ API actions](#security-supported-iam-actions-resources "#security-supported-iam-actions-resources")

## IAM Permissions Required to Create an Amazon MQ Broker

To create a broker, you must either use the `AmazonMQFullAccess` IAM
policy or include the following EC2 permissions in your IAM policy.

The following custom policy is comprised of two statements (one conditional) which
grant permissions to manipulate the resources which Amazon MQ requires to create an
ActiveMQ broker.

###### Important

- The `ec2:CreateNetworkInterface` action is required to
  allow Amazon MQ to create an elastic network interface (ENI) in your account
  on your behalf.
- The `ec2:CreateNetworkInterfacePermission` action
  authorizes Amazon MQ to attach the ENI to an ActiveMQ broker.
- The `ec2:AuthorizedService` condition key ensures that ENI
  permissions can be granted only to Amazon MQ service accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Action": [
 "mq:*",
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:DetachNetworkInterface",
 "ec2:DescribeInternetGateways",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeRouteTables",
 "ec2:DescribeSecurityGroups",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },{
 "Action": [
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DescribeNetworkInterfacePermissions"
 ],
 "Effect": "Allow",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "ec2:AuthorizedService": "mq.amazonaws.com"
 }
 }
 }]
}`

```

For more information, see [Step 2: create a user and get your AWS credentials](amazon-mq-setting-up.md#create-iam-user "amazon-mq-setting-up.md#create-iam-user") and [Never Modify or Delete the Amazon MQ Elastic Network Interface](best-practices-activemq.md#never-modify-delete-elastic-network-interface "best-practices-activemq.md#never-modify-delete-elastic-network-interface").

## Amazon MQ REST API permissions reference

The following table lists Amazon MQ REST APIs and the corresponding IAM
permissions.

| Amazon MQ REST APIs and Required Permissions                                                                                                                                                                                          | Amazon MQ REST APIs                | Required Permissions |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | -------------------- |
| [`CreateBroker`](../api-reference/rest-api-brokers.md#CreateBroker "../api-reference/rest-api-brokers.md#CreateBroker")                                                                                                               | `mq:CreateBroker`                  |
| [`CreateConfiguration`](../api-reference/rest-api-configurations.md#CreateConfiguration "../api-reference/rest-api-configurations.md#CreateConfiguration")                                                                            | `mq:CreateConfiguration`           |
| [`CreateTags`](../api-reference/tags-resource-arn.md#CreateTags "../api-reference/tags-resource-arn.md#CreateTags")                                                                                                                   | `mq:CreateTags`                    |
| [`CreateUser`](../api-reference/rest-api-user.md#CreateUser "../api-reference/rest-api-user.md#CreateUser")                                                                                                                           | `mq:CreateUser`                    |
| [`DeleteBroker`](../api-reference/rest-api-broker.md#DeleteBroker "../api-reference/rest-api-broker.md#DeleteBroker")                                                                                                                 | `mq:DeleteBroker`                  |
| [`DeleteUser`](../api-reference/rest-api-user.md#DeleteUser "../api-reference/rest-api-user.md#DeleteUser")                                                                                                                           | `mq:DeleteUser`                    |
| [`DescribeBroker`](../api-reference/rest-api-broker.md#DescribeBroker "../api-reference/rest-api-broker.md#DescribeBroker")                                                                                                           | `mq:DescribeBroker`                |
| [`DescribeConfiguration`](../api-reference/rest-api-configuration.md#DescribeConfiguration "../api-reference/rest-api-configuration.md#DescribeConfiguration")                                                                        | `mq:DescribeConfiguration`         |
| [`DescribeConfigurationRevision`](../api-reference/rest-api-configuration-revision.md#DescribeConfigurationRevision "../api-reference/rest-api-configuration-revision.md#DescribeConfigurationRevision")                              | `mq:DescribeConfigurationRevision` |
| [`DescribeUser`](../api-reference/brokers-broker-id-users-username.md#DescribeUser "../api-reference/brokers-broker-id-users-username.md#DescribeUser")                                                                               | `mq:DescribeUser`                  |
| [`ListBrokers`](../api-reference/rest-api-brokers.md#ListBrokers "../api-reference/rest-api-brokers.md#ListBrokers")                                                                                                                  | `mq:ListBrokers`                   |
| [`ListConfigurationRevisions`](../api-reference/rest-api-configuration-revisions.md#rest-api-configuration-revisions-methods-get "../api-reference/rest-api-configuration-revisions.md#rest-api-configuration-revisions-methods-get") | `mq:ListConfigurationRevisions`    |
| [`ListConfigurations`](../api-reference/rest-api-configurations.md#ListConfigurations "../api-reference/rest-api-configurations.md#ListConfigurations")                                                                               | `mq:ListConfigurations`            |
| [`ListTags`](../api-reference/tags-resource-arn.md#ListTags "../api-reference/tags-resource-arn.md#ListTags")                                                                                                                         | `mq:ListTags`                      |
| [`ListUsers`](../api-reference/rest-api-users.md#ListUsers "../api-reference/rest-api-users.md#ListUsers")                                                                                                                            | `mq:ListUsers`                     |
| [`RebootBroker`](../api-reference/rest-api-broker-reboot.md#RebootBroker "../api-reference/rest-api-broker-reboot.md#RebootBroker")                                                                                                   | `mq:RebootBroker`                  |
| [`UpdateBroker`](../api-reference/rest-api-broker.md#UpdateBroker "../api-reference/rest-api-broker.md#UpdateBroker")                                                                                                                 | `mq:UpdateBroker`                  |
| [`UpdateConfiguration`](../api-reference/rest-api-configuration.md#UpdateConfiguration "../api-reference/rest-api-configuration.md#UpdateConfiguration")                                                                              | `mq:UpdateConfiguration`           |
| [`UpdateUser`](../api-reference/rest-api-user.md#UpdateUser "../api-reference/rest-api-user.md#UpdateUser")                                                                                                                           | `mq:UpdateUser`                    |

## Amazon MQ additional permissions reference

The following table lists the Amazon MQ API and the additional IAM permission required for specific features, such as OAuth 2.0 authentication.

| Amazon MQ REST API                                                                                                      | Permission                           | Description                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [UpdateBroker](../api-reference/brokers-broker-id.md#UpdateBroker "../api-reference/brokers-broker-id.md#UpdateBroker") | `mq:UpdateBrokerAccessConfiguration` | You need this permission to update authentication and authorization options in the associated broker configuration. For more information, see [OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md"). |

## Resource-level permissions for Amazon MQ API actions

The term _resource-level permissions_ refers to the ability to
specify the resources on which users are allowed to perform actions. Amazon MQ has
partial support for resource-level permissions. For certain Amazon MQ actions, you can
control when users are allowed to use those actions based on conditions that have to
be fulfilled, or specific resources that users are allowed to use.

The following table describes the Amazon MQ API actions that currently support
resource-level permissions, as well as the supported resources, resource ARNs, and
condition keys for each action.

###### Important

If an Amazon MQ API action is not listed in this table, then it does not support
resource-level permissions. If an Amazon MQ API action does not support
resource-level permissions, you can grant users permission to use the action,
but you have to specify a \* wildcard for the resource element of your policy
statement.

| API Action                                                                                                                                                                                               | Resource Types (\*required)                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`CreateConfiguration`](../api-reference/rest-api-configurations.md#CreateConfiguration "../api-reference/rest-api-configurations.md#CreateConfiguration")                                               | [configurations\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                   |
| [`CreateTags`](../api-reference/tags-resource-arn.md#CreateTags "../api-reference/tags-resource-arn.md#CreateTags")                                                                                      | [brokers](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies"), [configurations](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies") |
| [`CreateUser`](../api-reference/rest-api-user.md#CreateUser "../api-reference/rest-api-user.md#CreateUser")                                                                                              | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`DeleteBroker`](../api-reference/rest-api-broker.md#DeleteBroker "../api-reference/rest-api-broker.md#DeleteBroker")                                                                                    | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`DeleteUser`](../api-reference/rest-api-user.md#DeleteUser "../api-reference/rest-api-user.md#DeleteUser")                                                                                              | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`DescribeBroker`](../api-reference/rest-api-broker.md#DescribeBroker "../api-reference/rest-api-broker.md#DescribeBroker")                                                                              | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`DescribeConfiguration`](../api-reference/rest-api-configuration.md#DescribeConfiguration "../api-reference/rest-api-configuration.md#DescribeConfiguration")                                           | [configurations\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                   |
| [`DescribeConfigurationRevision`](../api-reference/rest-api-configuration-revision.md#DescribeConfigurationRevision "../api-reference/rest-api-configuration-revision.md#DescribeConfigurationRevision") | [configurations\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                   |
| [`DescribeUser`](../api-reference/brokers-broker-id-users-username.md#DescribeUser "../api-reference/brokers-broker-id-users-username.md#DescribeUser")                                                  | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`ListConfigurationRevisions`](../api-reference/rest-api-configuration-revisions.md#ListConfigurationRevisions "../api-reference/rest-api-configuration-revisions.md#ListConfigurationRevisions")        | [configurations\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                   |
| [`ListConfigurationRevisions`](../api-reference/rest-api-configuration-revisions.md#ListConfigurationRevisions "../api-reference/rest-api-configuration-revisions.md#ListConfigurationRevisions")        | [configurations\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                   |
| [`ListTags`](../api-reference/tags-resource-arn.md#ListTags "../api-reference/tags-resource-arn.md#ListTags")                                                                                            | [brokers](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies"), [configurations](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies") |
| [`ListUsers`](../api-reference/rest-api-users.md#ListUsers "../api-reference/rest-api-users.md#ListUsers")                                                                                               | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`RebootBroker`](../api-reference/rest-api-broker-reboot.md#RebootBroker "../api-reference/rest-api-broker-reboot.md#RebootBroker")                                                                      | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`UpdateBroker`](../api-reference/rest-api-broker.md#UpdateBroker "../api-reference/rest-api-broker.md#UpdateBroker")                                                                                    | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
| [`UpdateConfiguration`](../api-reference/rest-api-configuration.md#UpdateConfiguration "../api-reference/rest-api-configuration.md#UpdateConfiguration")                                                 | [configurations\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                   |
| [`UpdateUser`](../api-reference/rest-api-user.md#UpdateUser "../api-reference/rest-api-user.md#UpdateUser")                                                                                              | [brokers\*](../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonmq.md#amazonmq-resources-for-iam-policies")                                                                                                                                                                                          |
