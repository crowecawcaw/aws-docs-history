# Using non-AWS container images in Amazon ECS

Use private registry to store your credentials in AWS Secrets Manager, and then reference them in
your task definition. This provides a way to reference container images that exist in
private registries outside of AWS that require authentication in your task definitions.
This feature is supported by tasks hosted on Fargate, Amazon EC2 instances, and external
instances using Amazon ECS Anywhere.

###### Important

If your task definition references an image that's stored in Amazon ECR, this topic doesn't
apply. For more information, see [Using Amazon ECR
Images with Amazon ECS](../../../AmazonECR/latest/userguide/ECR_on_ECS.md "../../../AmazonECR/latest/userguide/ECR_on_ECS.md") in the _Amazon Elastic Container Registry User Guide_.

For tasks hosted on Amazon EC2 instances, this feature requires version
`1.19.0` or later of the container agent. However, we recommend using the
latest container agent version. For information about how to check your agent version and
update to the latest version, see [Updating the Amazon ECS container agent](ecs-agent-update.md "ecs-agent-update.md").

For tasks hosted on Fargate, this feature requires platform version
`1.2.0` or later. For information, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").

Within your container definition, specify the `repositoryCredentials` object
with the details of the secret that you created. The referenced secret can be from a
different AWS Region or a different account than the task using it.

###### Note

When using the Amazon ECS API, AWS CLI, or AWS SDK, if the secret exists in the same
AWS Region as the task that you're launching then you can use either the full ARN or
name of the secret. If the secret exists in a different account, the full ARN of the
secret must be specified. When using the AWS Management Console, the full ARN of the secret must be
specified always.

The following is a snippet of a task definition that shows the required parameters:

Substitute the following parameters:

- `private-repo` with the private repository host name
- `private-image` with the image name
- `arn:aws:secretsmanager:region:aws_account_id:secret:secret_name`
  with the secret Amazon Resource Name (ARN)

```
"containerDefinitions": [
    {
        "image": "`private-repo/private-image`",
        "repositoryCredentials": {
            "credentialsParameter": "`arn:aws:secretsmanager:region:aws_account_id:secret:secret_name`"
        }
    }
]
```

###### Note

Another method of enabling private registry authentication uses Amazon ECS container agent
environment variables to authenticate to private registries. This method is only
supported for tasks hosted on Amazon EC2 instances. For more information, see [Configuring Amazon ECS container instances for private Docker images](private-auth-container-instances.md "private-auth-container-instances.md") .

###### To use private registry

1. The task definition must have a task execution role. This allows the container
   agent to pull the container image. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md "task_execution_IAM_role.md").

Private registry authentication allows your Amazon ECS tasks to pull container images from private registries outside of AWS (such as Docker Hub, Quay.io, or your own private registry) that require authentication credentials. This feature uses Secrets Manager to securely store your registry credentials, which are then referenced in your task definition using the `repositoryCredentials` parameter.

For more information about configuring private registry authentication, see [Using non-AWS container images in Amazon ECS](private-auth.md "private-auth.md").

To provide access to the secrets that contain your private registry credentials, add the following permissions as an inline policy to the task execution role. For more information, see [Adding and
Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

    * `secretsmanager:GetSecretValue`—Required to retrieve the private registry credentials from Secrets Manager.
    * `kms:Decrypt`—Required only if your secret uses a custom
     KMS key and not the default key. The Amazon Resource Name (ARN) for your
     custom key must be added as a resource.

The following is an example inline policy that adds the permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "secretsmanager:GetSecretValue"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:`111122223333`:secret:secret_name",
 "arn:aws:kms:us-east-1:`111122223333`:key/key_id"
 ]
 }
 ]
}`

```

2. Use AWS Secrets Manager to create a secret for your private registry credentials. For
   information about how to create a secret, see [Create an AWS Secrets Manager
   secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User
   Guide_.

Enter your private registry credentials using the following format:

```
{
  "username" : "`privateRegistryUsername`",
  "password" : "`privateRegistryPassword`"
}
```

3. Register a task definition. For more information, see [Creating an Amazon ECS task definition using the
   console](create-task-definition.md "create-task-definition.md").
