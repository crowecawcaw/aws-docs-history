# Pass environment variables to an Amazon ECS container

###### Important

We recommend storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager
Parameter Store parameters. For more information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md "specifying-sensitive-data.md").

Environment variable files are objects in Amazon S3 and all Amazon S3 security
considerations apply.

You can't use the `environmentFiles` parameter on Windows
containers and Windows containers on Fargate.

You can create an environment variable file and store it in Amazon S3 to pass
environment variables to your container.

By specifying environment variables in a file, you can bulk inject environment
variables. Within your container definition, specify the `environmentFiles`
object with a list of Amazon S3 buckets containing your environment variable files.

Amazon ECS doesn't enforce a size limit on the environment variables, but a large environment
variables file might fill up the disk space. Each task that uses an environment
variables file causes a copy of the file to be downloaded to disk. Amazon ECS removes the file as
part of the task cleanup.

For information about the supported environment variables, see [Advanced container definition parameters- Environment](task_definition_parameters.md#container_definition_environment "task_definition_parameters.md#container_definition_environment").

Consider the following when specifying an environment variable file in a container
definition.

- For Amazon ECS tasks on Amazon EC2, your container instances require that the container
  agent is version `1.39.0` or later to use this feature. For
  information about how to check your agent version and update to the latest
  version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").
- For Amazon ECS tasks on AWS Fargate, your tasks must use platform version
  `1.4.0` or later (Linux) to use this feature. For more
  information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").

Verify that the variable is supported for the operating system platform.
For more information, see [Container definitions](task_definition_parameters.md#container_definitions "task_definition_parameters.md#container_definitions") and [Other task definition parameters](task_definition_parameters.md#other_task_definition_params "task_definition_parameters.md#other_task_definition_params").

- The file must use the `.env` file extension and UTF-8
  encoding.
- The task execution role is required to use this feature with the additional
  permissions for Amazon S3. This allows the container agent to pull the environment
  variable file from Amazon S3. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").
- There is a limit of 10 files per task definition.
- Each line in an environment file must contain an environment variable in
  `VARIABLE=VALUE` format. Spaces or quotation marks **are** included as part of the values for Amazon ECS files.
  Lines beginning with `#` are treated as comments and are ignored. For
  more information about the environment variable file syntax, see [Set environment variables (-e, --env, --env-file)](https://docs.docker.com/reference/cli/docker/container/run/#env "https://docs.docker.com/reference/cli/docker/container/run/#env") in the Docker documentation.

The following is the appropriate syntax.

```
#This is a comment and will be ignored
VARIABLE=VALUE
ENVIRONMENT=PRODUCTION
```

- If there are environment variables specified using the
  `environment` parameter in a container definition, they take
  precedence over the variables contained within an environment file.
- If multiple environment files are specified and they contain the same
  variable, they're processed in order of entry. This means that the first value
  of the variable is used and subsequent values of duplicate variables are
  ignored. We recommend that you use unique variable names.
- If an environment file is specified as a container override, it's used.
  Moreover, any other environment files that are specified in the container
  definition is ignored.
- The following rules apply to the Fargate:
  - The file is handled similar to a native Docker env-file.
  - Container definitions that reference environment variables that are blank
    and stored in Amazon S3 do not appear in the container.
  - There is no support for shell escape handling.
  - The container entry point interperts the `VARIABLE`
    values.

## Example

The following is a snippet of a task definition showing how to specify an environment
variable file.

```
{
    "family": "",
    "containerDefinitions": [
        {
            "name": "",
            "image": "",
            ...
            "environmentFiles": [
                {
                    "value": "arn:aws:s3:::`amzn-s3-demo-bucket`/`envfile_object_name.env`",
                    "type": "s3"
                }
            ],
            ...
        }
    ],
    ...
}
```
