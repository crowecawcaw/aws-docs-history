# Bitbucket App connections

You can use Bitbucket to connect with CodeBuild. Bitbucket App connections are
supported through [AWS CodeConnections](../../../dtconsole/latest/userguide/welcome-connections.md "../../../dtconsole/latest/userguide/welcome-connections.md").

###### Note

CodeConnections is available in less regions than CodeBuild. You can use cross-region connections in CodeBuild. Connections
created in opt-in regions, cannot be used in other regions. For more information, see
[AWS CodeConnections endpoints and quotas](../../../general/latest/gr/codestar_connections.md "../../../general/latest/gr/codestar_connections.md").

###### Topics

- [Step 1: Create a connection to Bitbucket
  (console)](#connections-bitbucket-console "#connections-bitbucket-console")
- [Step 2: Grant CodeBuild project IAM role access to use the connection](#connections-bitbucket-role-access "#connections-bitbucket-role-access")
- [Step 3: Configure CodeBuild to use the new connection](#connections-bitbucket-account-credential "#connections-bitbucket-account-credential")

## Step 1: Create a connection to Bitbucket

(console)

Use these steps to use the CodeBuild console to add a connection for your project in Bitbucket.

###### To create a connection to Bitbucket

- Follow the instructions in the _Developer Tools User Guide_ for
  [Create a connection to Bitbucket](../../../dtconsole/latest/userguide/connections-create-bitbucket.md "../../../dtconsole/latest/userguide/connections-create-bitbucket.md").

###### Note

Instead of creating or using an existing connection in your account, you can use a connection shared from another AWS account.
For more information, see [Share connections with AWS accounts](../../../dtconsole/latest/userguide/connections-share.md "../../../dtconsole/latest/userguide/connections-share.md").

## Step 2: Grant CodeBuild project IAM role access to use the connection

You can grant CodeBuild project IAM role access to use the Bitbucket tokens vended by your connection.

###### To grant CodeBuild project IAM role access

1. Create an IAM role for your CodeBuild project by following the instructions to [Allow CodeBuild to interact with other AWS
   services](setting-up-service-role.md "setting-up-service-role.md") for your CodeBuild project.
2. While following the instructions, add the following IAM policy to your CodeBuild project role to grant access to the connection.

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

## Step 3: Configure CodeBuild to use the new connection

You can configure a connection as an account level credential and use it in a project.

AWS Management Console

###### To configure a connection as an account level credential in the AWS Management Console

1. For **Source provider**, choose
   **Bitbucket**.
2. For **Credential**, do one of the following:
   - Choose **Default source credential** to use
     your account's default source credential to apply to all projects.
     1. If you aren't connected to Bitbucket, choose **Manage default source credential**.
     2. For **Credential type**, choose **CodeConnections**.
     3. In **Connection**, choose to use an existing connection or create a new connection.

   - Choose **Custom source credential** to use
     a custom source credential to override your account's default settings.
     1. For **Credential type**, choose **CodeConnections**.
     2. In **Connection**, choose to use an existing connection or create a new connection.

AWS CLI

###### To configure a connection as an account level credential in the AWS CLI

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the **import-source-credentials** command, specifying the
  `--auth-type`, `--server-type`, and `--token` for your
  connection.

Use the following command:

```
aws codebuild import-source-credentials --auth-type CODECONNECTIONS --server-type BITBUCKET --token `<connection-arn>`
```

For more information on setting up multiple tokens in your CodeBuild project, see [Configure multiple tokens as source level credentials](multiple-access-tokens.md#asm-source-credential "multiple-access-tokens.md#asm-source-credential").
