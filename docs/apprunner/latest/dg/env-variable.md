# Referencing environment variables

With App Runner, you can reference secrets and configurations as environment variables in your service when you [create a
service](manage-create.md "manage-create.md") or [update a service](manage-configure.md "manage-configure.md").

You can reference non-sensitive configuration data such as timeouts and retry counts in **Plain Text** as key-value pairs. The
configuration data that you reference in **Plain Text** isn't encrypted and is visible to others in App Runner service configuration and
application logs.

###### Note

For security reasons, don't reference any sensitive data in **Plain Text** in your App Runner service.

## Referencing sensitive data as environment variables

App Runner supports securely referencing sensitive data as environment variables in your service.
Consider storing the sensitive data that you want to
reference in _AWS Secrets Manager_ or _AWS Systems Manager Parameter Store_. Then, you can securely reference them in your service as
environment variables from App Runner console or by calling the API. This effectively separates secret and parameter management from your application code and
service configuration, improving the overall security of your applications running on App Runner.

###### Note

App Runner doesn't charge you for referencing Secrets Manager and SSM Parameter Store as environment variables. However, you pay standard pricing for using Secrets Manager and
SSM Parameter Store.

For more information about pricing, see the following:

- [AWS Secrets Manager Pricing](https://aws.amazon.com/secrets-manager/pricing "https://aws.amazon.com/secrets-manager/pricing")
- [AWS SSM Parameter Store Pricing](https://aws.amazon.com/systems-manager/pricing "https://aws.amazon.com/systems-manager/pricing")

The following is the process to reference sensitive
data as environment variables:

1. Store sensitive data, such as API keys, database credentials, database connection parameters, or application versions as secrets or parameters in
   either AWS Secrets Manager or AWS Systems Manager Parameter Store.
2. Update the IAM policy of your instance role so App Runner can access the secrets and parameters stored in Secrets Manager and SSM Parameter Store. For more
   information, see [Permissions](#env-variable.sensitivedata.permissions "#env-variable.sensitivedata.permissions").
3. Securely reference the secrets and parameters as environment variables by assigning a name and providing their Amazon Resource Name (ARN). You can
   add environment variables when you [create a service](manage-create.md "manage-create.md") or [update a service's
   configuration](manage-configure.md "manage-configure.md"). You can use one of the following options to add environment variables:
   - App Runner console
   - App Runner API
   - `apprunner.yaml` configuration file

###### Note

You cannot assign `PORT` as a name for an environment variable when creating or updating your App Runner service.
It's a reserved environment variable for App Runner service.

For more information on how to reference secrets and parameters, see [Managing environment
variables](env-variable-manage.md "env-variable-manage.md").

###### Note

Since App Runner only stores the reference to secret and parameter ARNs, the sensitive data isn't visible to others in the App Runner service configuration and
application logs.

## Considerations

- Make sure that you update your instance role with appropriate permissions to access the secrets and parameters in AWS Secrets Manager or in AWS Systems Manager
  Parameter Store. For more information, see [Permissions](#env-variable.sensitivedata.permissions "#env-variable.sensitivedata.permissions").
- Make sure that AWS Systems Manager Parameter Store is in the same AWS account as the service that you want to launch or update. Currently, you can't
  reference SSM Parameter Store parameters across accounts.
- When the secrets and parameter values are rotated or changed they are not automatically updated in your App Runner service. Redeploy your App Runner service
  as App Runner only pulls secrets and parameters during deployment.
- You also have the option to directly call AWS Secrets Manager and AWS Systems Manager Parameter Store through the SDK in your App Runner service.
- To avoid errors make sure of the following when referencing them as the
  environment variables:
  - You specify the right ARN of the secret.
  - You specify the right name or ARN of the parameter.

## Permissions

To enable referencing secrets and parameters stored in the AWS Secrets Manager or SSM Parameter Store, add appropriate permissions to the IAM policy of your
_instance role_ to access Secrets Manager and SSM Parameter Store.

###### Note

App Runner can't access resources in your account without your permission. You provide the permission through updating your IAM policy.

You can use the following policy templates to update your instance role in the IAM console. You can modify these policy templates to meet your
specific requirement. For more information about updating an instance role, see [Modifying a role](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md") in the _IAM User Guide_.

###### Note

You can also copy the following templates from the App Runner console when [creating the environment
variables](env-variable-manage.md#env-variable-manage.console "env-variable-manage.md#env-variable-manage.console").

Copy, the following template to your instance role to add permission to reference _secrets_ from
_AWS Secrets Manager_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "kms:Decrypt*"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-east-1`:`111122223333`:`secret`:`my-secret`",
 "arn:aws:kms:`us-east-1`:`111122223333`:`key`/`my-key`"
 ]
 }
 ]
}`

```

Copy the following template to your instance role to add permission to reference _parameters_ from _AWS Systems Manager_
Parameter Store.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameters"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:`parameter`/`my-parameter`"
 ]
 }
 ]
}`

```
