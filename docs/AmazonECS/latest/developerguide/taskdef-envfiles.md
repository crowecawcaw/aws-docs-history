# Pass an individual environment variable to an Amazon ECS container

###### Important

We recommend storing your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager
Parameter Store parameters. For more information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md "specifying-sensitive-data.md").

Environment variables specified in the task definition are readable by all users and
roles that are allowed the `DescribeTaskDefinition` action for the task
definition.

You can pass environment variables to your containers in the following ways:

- Individually using the `environment` container definition parameter.
  This maps to the `--env` option to [**docker
  container run**](https://docs.docker.com/reference/cli/docker/container/run/ "https://docs.docker.com/reference/cli/docker/container/run/").
- In bulk, using the `environmentFiles` container definition parameter to
  list one or more files that contain the environment variables. The file must be
  hosted in Amazon S3. This maps to the `--env-file` option to [**docker run**](https://docs.docker.com/reference/cli/docker/container/run/ "https://docs.docker.com/reference/cli/docker/container/run/").
  The following is a snippet of a task definition showing how to specify individual
  environment variables.

```
{
    "family": "",
    "containerDefinitions": [
        {
            "name": "",
            "image": "",
            ...
            "environment": [
                {
                    "name": "`variable`",
                    "value": "`value`"
                }
            ],
            ...
        }
    ],
    ...
}
```
