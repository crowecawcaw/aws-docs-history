# Pass Systems Manager Parameter Store secrets programmatically in Amazon ECS

Systems Manager Parameter Store provides secure storage and management of secrets. You can
store data such as passwords, database strings, EC2 instance IDs and
AMI IDs, and license codes as parameter values, instead of hardcoding this information in your application. You can store values as
plain text or encrypted data.

We recommend this method of retrieving sensitive data because if the Systems Manager
Parameter Store parameter is subsequently updated, the application automatically
retrieves the latest version.

Review the following considerations before securing sensitive data in
Systems Manager Parameter Store.

- Only secrets that store text data are supported. Secrets that
  store binary data are not supported.
- Use interface VPC endpoints to enhance security
  controls.
- The VPC your task uses must use DNS resolution.
- For tasks that use EC2, you must use
  the Amazon ECS agent configuration variable
  `ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE=true` to
  use this feature. You can add it to the
  `/etc/ecs/ecs.config` file during container instance
  creation or you can add it to an existing instance and then restart
  the ECS agent. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").
- Your task definition must use a task role with the additional permissions for Systems Manager
  Parameter Store. For more information, see [Amazon ECS task IAM role](task-iam-roles.md "task-iam-roles.md").

## Create the parameter

You can use the Systems Manager console to create a Systems Manager Parameter Store parameter for your
sensitive data. For more information, see [Create
a Systems Manager parameter (console)](../../../systems-manager/latest/userguide/parameter-create-console.md "../../../systems-manager/latest/userguide/parameter-create-console.md") or [Create a Systems Manager
parameter (AWS CLI)](../../../systems-manager/latest/userguide/param-create-cli.md "../../../systems-manager/latest/userguide/param-create-cli.md") in the
_AWS Systems Manager User Guide_.

## Update your application to programmatically retrieve Systems Manager Parameter Store secrets

To retrieve the sensitive data stored in the Systems Manager Parameter Store parameter, see [Code examples for Systems Manager
using AWS SDKs](../../../code-library/latest/ug/ssm_code_examples.md "../../../code-library/latest/ug/ssm_code_examples.md") in the _AWS SDK Code
Examples Code Library_.
