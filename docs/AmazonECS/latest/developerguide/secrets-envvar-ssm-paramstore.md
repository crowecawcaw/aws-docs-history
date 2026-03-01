# Pass Systems Manager parameters through Amazon ECS environment variables

Amazon ECS allows you to inject sensitive data into your containers by storing
your sensitive data in AWS Systems Manager Parameter Store parameters and then
referencing them in your container definition.

Consider the following when using an environment variable to inject a Systems Manager secret into a
container.

- Sensitive data is injected into your container when the
  container is initially started. If the secret is subsequently
  updated or rotated, the container will not receive the updated
  value automatically. You must either launch a new task or if
  your task is part of a service you can update the service and
  use the **Force new deployment** option to
  force the service to launch a fresh task.
- For Amazon ECS tasks on AWS Fargate, the following should be
  considered:
  - To inject the full content of a secret as an
    environment variable or in a log configuration, you must
    use platform version `1.3.0` or later. For
    information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").
  - To inject a specific JSON key or version of a secret
    as an environment variable or in a log configuration,
    you must use platform version `1.4.0` or
    later (Linux) or `1.0.0` (Windows). For
    information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").

- For Amazon ECS tasks on EC2, the following should be
  considered:
  - To inject a secret using a specific JSON key or
    version of a secret, your container instance must have
    version `1.37.0` or later of the container
    agent. However, we recommend using the latest container
    agent version. For information about checking your agent
    version and updating to the latest version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

  To inject the full contents of a secret as an
  environment variable or to inject a secret in a log
  configuration, your container instance must have version
  `1.22.0` or later of the container
  agent.

- Use interface VPC endpoints to enhance security controls. You must create the
  interface VPC endpoints for Systems Manager. For information about the VPC endpoint, see
  [Improve the
  security of EC2 instances by using VPC endpoints for Systems Manager](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md") in the
  _AWS Systems Manager User Guide_.
- Your task definition must use a task execution role with the additional permissions
  for Systems Manager Parameter Store. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").
- For Windows tasks that are configured to use the `awslogs` logging driver,
  you must also set the `ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE`
  environment variable on your container instance. Use the following
  syntax:

```
<powershell>
[Environment]::SetEnvironmentVariable("ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE", $TRUE, "Machine")
Initialize-ECSAgent -Cluster <cluster name> -EnableTaskIAMRole -LoggingDrivers '["json-file","awslogs"]'
</powershell>
```

## Create the Systems Manager parameter

You can use the Systems Manager console to create a Systems Manager Parameter Store parameter for
your sensitive data. For more information, see [Create
a Systems Manager parameter (console)](../../../systems-manager/latest/userguide/parameter-create-console.md "../../../systems-manager/latest/userguide/parameter-create-console.md") or [Create a Systems Manager
parameter (AWS CLI)](../../../systems-manager/latest/userguide/param-create-cli.md "../../../systems-manager/latest/userguide/param-create-cli.md") in the
_AWS Systems Manager User Guide_.

## Add the environment variable to the container definition

Within your container definition in the task definition, specify `secrets`
with the name of the environment variable to set in the container and the full ARN of
the Systems Manager Parameter Store parameter containing the sensitive data to present to the
container. For more information, see [secrets](task_definition_parameters.md#ContainerDefinition-secrets "task_definition_parameters.md#ContainerDefinition-secrets").

The following is a snippet of a task definition showing the format when referencing a
Systems Manager Parameter Store parameter. If the Systems Manager Parameter Store parameter exists
in the same Region as the task you are launching, then you can
use either the full ARN or name of the parameter. If the parameter exists in a
different Region, then specify the full ARN.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:ssm:`region`:`aws_account_id`:parameter/`parameter_name`"
    }]
  }]
}
```

For information about how to create a task definition with the secret specified in an
environment variable, see [Creating an Amazon ECS task definition using the console](create-task-definition.md "create-task-definition.md").

## Update your application to programmatically retrieve Systems Manager Parameter Store secrets

To retrieve the sensitive data stored in the Systems Manager Parameter Store parameter, see [Code examples for Systems Manager
using AWS SDKs](../../../code-library/latest/ug/ssm_code_examples.md "../../../code-library/latest/ug/ssm_code_examples.md") in the _AWS SDK Code
Examples Code Library_.
