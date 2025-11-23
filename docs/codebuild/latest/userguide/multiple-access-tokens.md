# Multiple access tokens in CodeBuild

CodeBuild supports sourcing access tokens to third party providers from your secrets in AWS Secrets Manager or through AWS CodeConnections connections. You can set your secret or connection
as the default credential for interactions with a specified third party provider such as GitHub,
GitHub Enterprise, or Bitbucket.

You can set your source credentials at three different levels:

1. **Account level credentials for all projects:** These are default credentials for all projects in an
   AWS account. They will be used on a project when no project or source level credentials are specified.
2. **Source level credentials for a specific repository:** This is when a Secrets Manager secret or CodeConnections connection is defined on a
   project source. These credentials will only be used for operations on the specified source repository. This
   allows you to set up multiple access tokens with different permission scopes in the same project, and not use the default
   account level credentials.
3. **Project level fallback credentials:** You can set a project level fallback credential by using `NO_SOURCE` as primary source
   type and define a secret or connection on it. This is can be used when you have multiple sources on a project, but want to use the
   same credentials for them, or when you don't want to use the default account level credentials for your project.

###### Topics

- [Step 1: Create a Secrets Manager secret or a CodeConnections connection](#create-secret-connection "#create-secret-connection")
- [Step 2: Grant CodeBuild project IAM role access to Secrets Manager secrets](#asm-role-access "#asm-role-access")
- [Step 3: Configure Secrets Manager or CodeConnections tokens](#asm-account-credential "#asm-account-credential")
- [Additional setup options](#asm-credential-cfn "#asm-credential-cfn")

## Step 1: Create a Secrets Manager secret or a CodeConnections connection

Use the following instructions to create a Secrets Manager secret or a CodeConnections connection:

- [Create and store a token in a Secrets Manager secret](asm-create-secret.md "asm-create-secret.md").
- [Create a connection to GitHub](../../../dtconsole/latest/userguide/connections-create-github.md "../../../dtconsole/latest/userguide/connections-create-github.md")
- [Create a connection to to GitHub Enterprise Server](../../../dtconsole/latest/userguide/connections-create-gheserver.md "../../../dtconsole/latest/userguide/connections-create-gheserver.md")
- [Create a connection to Bitbucket](../../../dtconsole/latest/userguide/connections-create-bitbucket.md "../../../dtconsole/latest/userguide/connections-create-bitbucket.md")

## Step 2: Grant CodeBuild project IAM role access to Secrets Manager secrets

###### Note

Before you continue, you must have access to the token created in Secrets Manager or CodeConnections.

To grant CodeBuild project IAM role access to Secrets Manager or CodeConnections, you must add the following IAM policy.

###### To grant CodeBuild project IAM role access

1. Create an IAM role for your CodeBuild project by following the instructions to [Allow CodeBuild to interact with other AWS
   services](setting-up-service-role.md "setting-up-service-role.md") for your CodeBuild project.
2. Do one of the following:
   - Add the following IAM policy to your CodeBuild project role to grant access to your secret.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "secretsmanager:GetSecretValue"
    ],
    "Resource": [
    "`arn:aws:iam::*:role/Service*`"
    ]
    }
    ]
   }`

   ```

   (Optional) If you're using AWS KMS customer managed keys to encrypt a Secrets Manager secret, you can add the following policy statement to grant access.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "kms:Decrypt"
    ],
    "Resource": "`arn:aws:iam::*:role/Service*`",
    "Condition": {
    "StringEquals": {
    "kms:EncryptionContext:SecretARN": "`arn:aws:iam::*:role/Service*`"
    }
    }
    }
    ]
   }`

   ```

   - Add the following IAM policy to your CodeBuild project role to grant access to your connection.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "codeconnections:GetConnectionToken",
    "codeconnections:GetConnection"
    ],
    "Resource": [
    "`arn:aws:iam::*:role/Service*`"
    ]
    }
    ]
   }`

   ```

## Step 3: Configure Secrets Manager or CodeConnections tokens

You can set your source credentials at three different levels with either Secrets Manager or CodeConnections tokens.

### Configure Secrets Manager or CodeConnections tokens as account level credentials

You can configure a Secrets Manager secret or CodeConnections connection as an account level credential and use it in a project.

AWS Management Console

###### To configure a connection as an account level credential in the AWS Management Console

1.  For **Source provider**, choose **Bitbucket**,
    **GitHub**, or **GitHub Enterprise**.
2.  For **Credential**, do one of the following:
    - Choose **Default source credential** to use
      your account's default source credential to apply to all projects.
      1. If you aren't connected to your source provider, choose **Manage default source credential**.
      2. For **Credential type**, choose a credential type.
      3. If you chose **CodeConnections**, choose to use an existing connection or create a new connection.

      If you chose a different credential type, for **Service** choose which service you'd like to use to store your token and do the following:

          + If you chose to use **Secrets Manager**, you can choose to use an existing
           secret connection or create a new secret and choose **Save**. For more information how to create a new secret, see [Create and store a token in a Secrets Manager secret](asm-create-secret.md "asm-create-secret.md").
          + If you chose to use **CodeBuild**, enter your
           token or your username and app password, and choose **Save**.

    - Choose **Custom source credential** to use
      a custom source credential to override your account's default settings.
      1. For **Credential type**, choose a credential type.
      2. In **Connection**, choose to use an existing connection or create a new connection.

AWS CLI

###### To configure a connection as an account level credential in the AWS CLI

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the **import-source-credentials** command.

Use the following command to configure a Secrets Manager secret:

```
aws codebuild import-source-credentials \
    --token "`<secret-arn>`" \
    --server-type `<source-provider>` \
    --auth-type SECRETS_MANAGER \
    --region `<aws-region>`
```

Use the following command to configure a CodeConnections connection:

```
aws codebuild import-source-credentials \
    --token "`<connection-arn>`" \
    --server-type `<source-provider>` \
    --auth-type CODECONNECTIONS \
    --region `<aws-region>`
```

This command allows you to import a token as the account level default source credentials. When you import a credential
using the [ImportSourceCredentials](../APIReference/API_ImportSourceCredentials.md "../APIReference/API_ImportSourceCredentials.md") API,
CodeBuild will use the token for all interactions with the source provider, such as webhooks, build status reporting and git clone operations
unless a more specific set of credentials has been configured in the project.

You can now use the token in your build project and run it. For more information, see [Create a build project in AWS CodeBuild](create-project.md "create-project.md") and [Run AWS CodeBuild builds manually](run-build.md "run-build.md").

### Configure multiple tokens as source level credentials

To use Secrets Manager secrets or CodeConnections connections as source level credentials, directly reference the token in CodeBuild project, and start a build.

AWS Management Console

###### To configure multiple tokens as source level credentials in the AWS Management Console

1. For **Source provider**, choose
   **GitHub**.
2. For **Credential**, do one of the following:
   - Choose **Default source credential** to use
     your account's default source credential to apply to all projects.
     1. If you aren't connected to GitHub, choose **Manage default source credential**.
     2. For **Credential type**, choose **GitHub App**.
     3. In **Connection**, choose to use an existing connection or create a new connection.

   - Choose **Custom source credential** to use
     a custom source credential to override your account's default settings.
     1. For **Credential type**, choose **GitHub App**.
     2. In **Connection**, choose to use an existing connection or create a new connection.

3. Choose **Add source** and repeat the process of choosing your
   source provider and credentials.

AWS CLI

###### To configure multiple tokens as source level credentials in the AWS CLI

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the **create-project** command.

Use the following command:

```
aws codebuild create-project --region `<aws-region>` \
    --name `<project-name>` \
    --artifacts type=NO_ARTIFACTS \
    --environment "type=LINUX_CONTAINER,
                   computeType=BUILD_GENERAL1_SMALL,
                   image=aws/codebuild/amazonlinux-x86_64-standard:5.0" \
    --service-role `<service-role-name>` \
    --source "type=GITHUB,
              location=`<github-repository-1>`,
              auth={type=SECRETS_MANAGER,resource=`<secret-or-connection-arn-1>`}" \
    --secondary-sources "type=GITHUB,
              location=`<github-repository-2>`,
              auth={type=SECRETS_MANAGER,resource=`<secret-or-connection-arn-2>`},
              sourceIdentifier=secondary"

aws codebuild start-build --region `<aws-region>` --project-name `<project-name>`
```

### Set a project level source credential fallback

To set up project level source credential fallback, use `NO_SOURCE` for your project's primary source and reference the token.

```
aws codebuild create-project \
    --name `<project-name>` \
    --service-role `<service-role-name>` \
    --artifacts type=NO_ARTIFACTS \
    --environment "type=LINUX_CONTAINER,
                   computeType=BUILD_GENERAL1_SMALL,
                   image=aws/codebuild/amazonlinux-x86_64-standard:5.0" \
    --service-role `<service-role-name>` \
    --source "type=NO_SOURCE,
              auth={type=SECRETS_MANAGER,resource=`<secret-or-connection-arn>`},
              buildspec=`<buildspec>`"
    --secondary-sources "type=GITHUB,
                         location=`<github-repository>`,
                         sourceIdentifier=secondary"

aws codebuild start-build --region `<aws-region>` --project-name `<project_name>`
```

When using `NO_SOURCE`, a buildspec typically is provided within the source model
as it is not directly configured to use an external source to fetch the [buildspec](build-spec-ref.md "build-spec-ref.md").
Commonly, a `NO_SOURCE` source will handle cloning all relevant repositories from within the
buildspec. To ensure the configured credentials are available for those operations, you can enable the
`git-credential-helper` option in the buildspec.

```
env:
  git-credential-helper: yes
```

During the build, CodeBuild will then read the `AuthServer` field from the configured token
and use the token credentials for all git requests to that particular third party source provider.

## Additional setup options

You can configure Secrets Manager account level credentials by using CloudFormation templates. You
can use the following CloudFormation template to set an account level credential:

```
Parameters:
  GitHubToken:
    Type: String
    NoEcho: true
    Default: placeholder
Resources:
  CodeBuildAuthTokenSecret:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: CodeBuild auth token
      Name: codebuild-auth-token
      SecretString:
        !Join
          - ''
          - - '{"ServerType":"GITHUB","AuthType":"PERSONAL_ACCESS_TOKEN","Token":"'
            - !Ref GitHubToken
            - '"}'
      Tags:
        - Key: codebuild:source:provider
          Value: github
        - Key: codebuild:source:type
          Value: personal_access_token
  CodeBuildSecretsManagerAccountCredential:
    Type: AWS::CodeBuild::SourceCredential
    Properties:
      ServerType: GITHUB
      AuthType: SECRETS_MANAGER
      Token: !Ref CodeBuildAuthTokenSecret
```

###### Note

If you're also creating a project in the same stack, use the CloudFormation attribute [DependsOn](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.md")
to ensure the `AccountCredential` is created before the project.

You can also configure Secrets Manager multiple source level credentials by using CloudFormation templates. You
can use the following CloudFormation template to use multiple tokens to pull in multiple sources:

```
Parameters:
  GitHubTokenOne:
    Type: String
    NoEcho: true
    Default: placeholder
  GitHubTokenTwo:
    Type: String
    NoEcho: true
    Default: placeholder

Resources:
  CodeBuildSecretsManagerProject:
    Type: AWS::CodeBuild::Project
    Properties:
      Name: codebuild-multitoken-example
      ServiceRole: `<service-role>`
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: aws/codebuild/amazonlinux-x86_64-standard:5.0
      Source:
        Type: GITHUB
        Location: `<github-repository-one>`
        Auth:
          Type: SECRETS_MANAGER
          Resource: !Ref CodeBuildAuthTokenSecretOne
      SecondarySources:
        - Type: GITHUB
          Location: `<github-repository-two>`
          Auth:
            Type: SECRETS_MANAGER
            Resource: !Ref CodeBuildAuthTokenSecretTwo
          SourceIdentifier: secondary
      Artifacts:
        Type: NO_ARTIFACTS
      LogsConfig:
        CloudWatchLogs:
          Status: ENABLED
  CodeBuildProjectIAMRoleSecretAccess:
    Type: AWS::IAM::RolePolicy
    Properties:
      RoleName: `<role-name>`
      PolicyName: CodeBuildProjectIAMRoleSecretAccessPolicy
      PolicyDocument:
        Version: '2012-10-17		 	 	 '
        Statement:
          - Effect: Allow
            Action:
              - secretsmanager:GetSecretValue
            Resource:
              - !Ref CodeBuildAuthTokenSecretOne
              - !Ref CodeBuildAuthTokenSecretTwo
  CodeBuildAuthTokenSecretOne:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: CodeBuild auth token one
      Name: codebuild-auth-token-one
      SecretString:
        !Join
          - ''
          - - '{"ServerType":"GITHUB","AuthType":"PERSONAL_ACCESS_TOKEN","Token":"'
            - !Ref GitHubTokenOne
            - '"}'
      Tags:
        - Key: codebuild:source:provider
          Value: github
        - Key: codebuild:source:type
          Value: personal_access_token
  CodeBuildAuthTokenSecretTwo:
    Type: AWS::SecretsManager::Secret
    Properties:
      Description: CodeBuild auth token two
      Name: codebuild-auth-token-two
      SecretString:
        !Join
          - ''
          - - '{"ServerType":"GITHUB","AuthType":"PERSONAL_ACCESS_TOKEN","Token":"'
            - !Ref GitHubTokenTwo
            - '"}'
      Tags:
        - Key: codebuild:source:provider
          Value: github
        - Key: codebuild:source:type
          Value: personal_access_token
```
