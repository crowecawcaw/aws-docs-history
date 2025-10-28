# Private registry authentication for jobs

Private registry authentication for jobs using AWS Secrets Manager enables you to store your credentials securely and then
reference them in your job definition. This provides a way to reference container images that exist in private
registries outside of AWS that require authentication in your job definitions. This feature is supported by jobs
hosted on Amazon EC2 instances and Fargate.

###### Important

If your job definition references an image that's stored in Amazon ECR, this topic doesn't apply. For more
information, see [Using Amazon ECR Images with Amazon ECS](../../../AmazonECR/latest/userguide/ECR_on_ECS.md "../../../AmazonECR/latest/userguide/ECR_on_ECS.md") in the
_Amazon Elastic Container Registry User Guide_.

For jobs hosted on Amazon EC2 instances, this feature requires version `1.19.0` or later of the container
agent. However, we recommend using the latest container agent version. For information about how to check your agent
version and update to the latest version, see [Updating the Amazon ECS container agent](../../../AmazonECS/latest/developerguide/ecs-agent-update.md "../../../AmazonECS/latest/developerguide/ecs-agent-update.md") in the
_Amazon Elastic Container Service Developer Guide_.

For jobs hosted on Fargate, this feature requires platform version `1.2.0` or later. For
information, see [AWS Fargate Linux platform versions](../../../AmazonECS/latest/developerguide/platform-linux-fargate.md "../../../AmazonECS/latest/developerguide/platform-linux-fargate.md") in the _Amazon Elastic Container Service Developer Guide_.

Within your container definition, specify the `repositoryCredentials` object with the details of the
secret that you created. The secret you reference can be from a different AWS Region or a different account than the
job using it.

###### Note

When using the AWS Batch API, AWS CLI, or AWS SDK, if the secret exists in the same AWS Region as the job that
you're launching then you can use either the full ARN or name of the secret. If the secret exists in a different
account, the full ARN of the secret must be specified. When using the AWS Management Console, the full ARN of the secret must be
specified always.

The following is a snippet of a job definition that shows the required parameters:

```
"containerProperties": [
  {
    "image": "`private-repo/private-image`",
    "repositoryCredentials": {
      "credentialsParameter": "arn:aws:secretsmanager:`region`:`123456789012`:secret:`secret_name`"
    }
  }
]
```
