# Add a Git repository to your Amazon SageMaker AI

account (CLI)

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

Use the `create-code-repository` AWS CLI command to add a Git
repository to Amazon SageMaker AI to give users access to external resources. Specify a
name for the repository as the value of the `code-repository-name`
argument. The name must be 1 to 63 characters. Valid characters are a-z, A-Z,
0-9, and - (hyphen). Also specify the following:

- The default branch
- The URL of the Git repository

###### Note

Do not provide a username in the URL. Add the sign-in credentials
in AWS Secrets Manager as described in the next step.

- The Amazon Resource Name (ARN) of an AWS Secrets Manager secret that
  contains the credentials to use to authenticate the repository as the
  value of the `git-config` argument
  For information about creating and storing a secret, see [Creating a Basic Secret](../../../secretsmanager/latest/userguide/manage_create-basic-secret.md "../../../secretsmanager/latest/userguide/manage_create-basic-secret.md") in the _AWS Secrets Manager User
  Guide_. The following command creates a new repository named
  `MyRespository` in your Amazon SageMaker AI account that points to a Git
  repository hosted at `https://github.com/myprofile/my-repo"`.

For Linux, OS X, or Unix:

```
aws sagemaker create-code-repository \
                    --code-repository-name "MyRepository" \
                    --git-config Branch=`branch`,RepositoryUrl=https://github.com/myprofile/my-repo,SecretArn=arn:aws:secretsmanager:us-east-2:012345678901:secret:my-secret-ABc0DE

```

For Windows:

```
aws sagemaker create-code-repository ^
                    --code-repository-name "MyRepository" ^
                    --git-config "{\"Branch\":\"master\", \"RepositoryUrl\" :
                    \"https://github.com/myprofile/my-repo\", \"SecretArn\" : \"arn:aws:secretsmanager:us-east-2:012345678901:secret:my-secret-ABc0DE\"}"

```

###### Note

The secret must have a staging label of `AWSCURRENT` and must
be in the following format:

`{"username": `UserName`, "password":
 `Password`}`

For GitHub repositories, we recommend using a personal access
token.
