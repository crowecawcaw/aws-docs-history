# Pass Secrets Manager secrets through Amazon ECS environment

variables

When you inject a secret as an environment variable, you can specify the full contents of
a secret, a specific JSON key within a secret. This helps you control the sensitive data
exposed to your container. For more information about secret versioning, see [What's in
a Secrets Manager secret?](../../../secretsmanager/latest/userguide/whats-in-a-secret.md#term_version "../../../secretsmanager/latest/userguide/whats-in-a-secret.md#term_version") in the _AWS Secrets Manager User Guide_.

The following should be considered when using an environment variable to inject a Secrets Manager
secret into a container.

- Sensitive data is injected into your container when the
  container is initially started. If the secret is subsequently
  updated or rotated, the container will not receive the updated
  value automatically. You must either launch a new task or if
  your task is part of a service you can update the service and
  use the **Force new deployment** option to
  force the service to launch a fresh task.
- Applications that run on the container and container logs and debugging tools
  have access to the environment variables.
- For Amazon ECS tasks on AWS Fargate, consider the following:
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

- Use interface VPC endpoints to enhance security controls and connect to Secrets Manager through a private
  subnet. You must create the interface VPC endpoints for Secrets Manager. For information about the
  VPC endpoint, see [Create VPC
  endpoints](../../../secretsmanager/latest/userguide/setup-create-vpc.md "../../../secretsmanager/latest/userguide/setup-create-vpc.md") in the _AWS Secrets Manager User Guide_. For more information
  about using Secrets Manager and Amazon VPC, see [How to connect to Secrets Manager service within a Amazon VPC](https://aws.amazon.com/blogs/security/how-to-connect-to-aws-secrets-manager-service-within-a-virtual-private-cloud/ "https://aws.amazon.com/blogs/security/how-to-connect-to-aws-secrets-manager-service-within-a-virtual-private-cloud/").
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

- Your task definition must use a task execution role with the additional permissions
  for Secrets Manager. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

## Create the AWS Secrets Manager

secret

You can use the Secrets Manager console to create a secret for your sensitive data. For more
information, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the
_AWS Secrets Manager User Guide_.

## Add the

environment variable to the container definition

Within your container definition, you can specify the
following:

- The `secrets` object containing the name of the
  environment variable to set in the container
- The Amazon Resource Name (ARN) of the Secrets Manager secret
- Additional parameters that contain the sensitive data to
  present to the container

The following example shows the full syntax that must be specified for
the Secrets Manager secret.

```
arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`secret-name`:`json-key`:`version-stage`:`version-id`
```

The following section describes the additional parameters. These
parameters are optional, but if you do not use them, you must include
the colons `:` to use the default values. Examples are
provided below for more context.

`json-key`

Specifies the name of the key in a key-value pair with the
value that you want to set as the environment variable
value. Only values in JSON format are supported. If you do
not specify a JSON key, then the full contents of the secret
is used.

`version-stage`

Specifies the staging label of the version of a secret
that you want to use. If a version staging label is
specified, you cannot specify a version ID. If no version
stage is specified, the default behavior is to retrieve the
secret with the `AWSCURRENT` staging
label.

Staging labels are used to keep track of different
versions of a secret when they are either updated or
rotated. Each version of a secret has one or more staging
labels and an ID.

`version-id`

Specifies the unique identifier of the version of a secret
that you want to use. If a version ID is specified, you
cannot specify a version staging label. If no version ID is
specified, the default behavior is to retrieve the secret
with the `AWSCURRENT` staging label.

Version IDs are used to keep track of different versions
of a secret when they are either updated or rotated. Each
version of a secret has an ID. For more information, see
[Key Terms and Concepts for
AWS Secrets Manager](../../../secretsmanager/latest/userguide/terms-concepts.md#term_secret "../../../secretsmanager/latest/userguide/terms-concepts.md#term_secret") in the
_AWS Secrets Manager User Guide_.

### Example container

definitions

The following examples show ways in which you can reference Secrets Manager
secrets in your container definitions.

###### Example referencing a full secret

The following is a snippet of a task definition showing the
format when referencing the full text of a Secrets Manager secret.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`secret_name-AbCdEf`"
    }]
  }]
}
```

To access the value of this secret from within the container
you would need to call the
`$environment_variable_name`.

###### Example referencing full secrets

The following is a snippet of a task definition showing the
format when referencing the full text of multiple Secrets Manager secrets.

```
{
  "containerDefinitions": [{
     "secrets": [
      {
        "name": "`environment_variable_name1`",
         "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`secret_name-AbCdEf`"
      },
      {
        "name": "`environment_variable_name2`",
         "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`secret_name-abcdef`"
      },
      {
        "name": "`environment_variable_name3`",
        "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`secret_name-ABCDEF`"
      }
    ]
  }]
}
```

To access the value of this secret from within the container you would need to call
the `$environment_variable_name1`,
`$environment_variable_name2`, and
`$environment_variable_name3`.

###### Example referencing a specific key within a secret

The following shows an example output from a [get-secret-value](../../../cli/latest/reference/secretsmanager/get-secret-value.md "../../../cli/latest/reference/secretsmanager/get-secret-value.md") command that displays the contents
of a secret along with the version staging label and version ID
associated with it.

```
{
    "ARN": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`",
    "Name": "`appauthexample`",
    "VersionId": "`871d9eca-18aa-46a9-8785-981ddEXAMPLE`",
    "SecretString": "{\"`username1`\":\"`password1`\",\"`username2`\":\"`password2`\",\"`username3`\":\"`password3`\"}",
    "VersionStages": [
        "`AWSCURRENT`"
    ],
    "CreatedDate": 1581968848.921
}
```

Reference a specific key from the previous output in a
container definition by specifying the key name at the end of
the ARN.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`:`username1`::"
    }]
  }]
}
```

###### Example referencing a specific secret version

The following shows an example output from a [describe-secret](../../../cli/latest/reference/secretsmanager/describe-secret.md "../../../cli/latest/reference/secretsmanager/describe-secret.md") command that displays the
unencrypted contents of a secret along with the metadata for all
versions of the secret.

```
{
    "ARN": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`",
    "Name": "`appauthexample`",
    "Description": "Example of a secret containing application authorization data.",
    "RotationEnabled": false,
    "LastChangedDate": 1581968848.926,
    "LastAccessedDate": 1581897600.0,
    "Tags": [],
    "VersionIdsToStages": {
        "`871d9eca-18aa-46a9-8785-981ddEXAMPLE`": [
            "`AWSCURRENT`"
        ],
        "`9d4cb84b-ad69-40c0-a0ab-cead3EXAMPLE`": [
            "`AWSPREVIOUS`"
        ]
    }
}
```

Reference a specific version staging label from the previous
output in a container definition by specifying the key name at
the end of the ARN.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`::`AWSPREVIOUS`:"
    }]
  }]
}
```

Reference a specific version ID from the previous output in a
container definition by specifying the key name at the end of
the ARN.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`:::`9d4cb84b-ad69-40c0-a0ab-cead3EXAMPLE`"
    }]
  }]
}
```

###### Example referencing a specific key and version staging label of a

secret

The following shows how to reference both a specific key
within a secret and a specific version staging label.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`:`username1`:`AWSPREVIOUS`:"
    }]
  }]
}
```

To specify a specific key and version ID, use the following
syntax.

```
{
  "containerDefinitions": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:secretsmanager:`region`:`aws_account_id`:secret:`appauthexample-AbCdEf`:`username1`::`9d4cb84b-ad69-40c0-a0ab-cead3EXAMPLE`"
    }]
  }]
}
```

For information about how to create a task definition with the secret specified in an
environment variable, see [Creating an Amazon ECS task definition using the
console](create-task-definition.md "create-task-definition.md").
