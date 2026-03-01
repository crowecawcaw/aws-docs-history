# Pass secrets for Amazon ECS logging configuration

You can use the `secretOptions` parameter in `logConfiguration` to pass sensitive data used for logging.

You can store the secret in Secrets Manager or Systems Manager.

## Use Secrets Manager

Within your container definition, when specifying a
`logConfiguration` you can specify `secretOptions`
with the name of the log driver option to set in the container and the full
ARN of the Secrets Manager secret containing the sensitive data to present to the
container. For more information about creating secrets, see [Create an AWS Secrets Manager](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md").

The following is a snippet of a task definition showing the format when
referencing an Secrets Manager secret.

```
{
  "containerDefinitions": [{
    "logConfiguration": [{
      "logDriver": "`splunk`",
      "options": {
        "splunk-url": "`https://your_splunk_instance:8088`"
      },
      "secretOptions": [{
        "name": "`splunk-token`",
        "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`secret_name-AbCdEf`"
      }]
    }]
  }]
}
```

## Add the environment variable to the container definition

Within your container definition, specify `secrets` with the name of the
environment variable to set in the container and the full ARN of the Systems Manager
Parameter Store parameter containing the sensitive data to present to the
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

## Use Systems Manager

You can inject sensitive data in a log configuration. Within your
container definition, when specifying a `logConfiguration` you
can specify `secretOptions` with the name of the log driver
option to set in the container and the full ARN of the Systems Manager Parameter Store
parameter containing the sensitive data to present to the container.

###### Important

If the Systems Manager Parameter Store parameter exists in the same Region as the
task you are launching, then you can use either the full ARN or name of the
parameter. If the parameter exists in a different Region, then
specify the full ARN.

The following is a snippet of a task definition showing the format when
referencing a Systems Manager Parameter Store parameter.

```
{
  "containerDefinitions": [{
    "logConfiguration": [{
      "logDriver": "`fluentd`",
      "options": {
        "tag": "`fluentd demo`"
      },
      "secretOptions": [{
        "name": "`fluentd-address`",
        "valueFrom": "arn:aws:ssm:`region`:`aws_account_id`:parameter:/`parameter_name`"
      }]
    }]
  }]
}
```
