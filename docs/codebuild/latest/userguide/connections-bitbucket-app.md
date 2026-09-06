

# Bitbucket App connections
<a name="connections-bitbucket-app"></a>

You can use Bitbucket to connect with CodeBuild. Bitbucket App connections are supported through [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections.html).

**Note**  
CodeConnections is available in fewer regions than CodeBuild. You can use cross-region connections in CodeBuild. Connections created in opt-in Regions cannot be used in other Regions. For more information, see [AWS CodeConnections endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/codestar_connections.html).

**Topics**
+ [Step 1: Create a connection to Bitbucket (console)](#connections-bitbucket-console)
+ [Step 2: Grant CodeBuild project IAM role access to use the connection](#connections-bitbucket-role-access)
+ [Step 3: Configure CodeBuild to use the new connection](#connections-bitbucket-account-credential)
+ [Bitbucket OAuth rotating refresh tokens](#connections-bitbucket-migrate-from-oauth)

## Step 1: Create a connection to Bitbucket (console)
<a name="connections-bitbucket-console"></a>

Use these steps to use the CodeBuild console to add a connection for your project in Bitbucket.

**To create a connection to Bitbucket**
+ Follow the instructions in the *Developer Tools User Guide* for [Create a connection to Bitbucket](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create-bitbucket.html).

**Note**  
Instead of creating or using an existing connection in your account, you can use a connection shared from another AWS account. For more information, see [Share connections with AWS accounts](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-share.html).

## Step 2: Grant CodeBuild project IAM role access to use the connection
<a name="connections-bitbucket-role-access"></a>

You can grant CodeBuild project IAM role access to use the Bitbucket tokens vended by your connection.

**To grant CodeBuild project IAM role access**

1. Create an IAM role for your CodeBuild project by following the instructions to [Allow CodeBuild to interact with other AWS services](setting-up-service-role.md) for your CodeBuild project.

1. While following the instructions, add the following IAM policy to your CodeBuild project role to grant access to the connection.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "codeconnections:GetConnectionToken",
                   "codeconnections:GetConnection"
               ],
               "Resource": [
                   "{{arn:aws:iam::*:role/Service*}}"
               ]
           }
       ]
   }
   ```

------

## Step 3: Configure CodeBuild to use the new connection
<a name="connections-bitbucket-account-credential"></a>

You can configure a connection as an account level credential and use it in a project.

------
#### [ AWS Management Console ]

**To configure a connection as an account level credential in the AWS Management Console**

1. For **Source provider**, choose **Bitbucket**. 

1. For **Credential**, do one of the following:
   + Choose **Default source credential** to use your account's default source credential to apply to all projects.

     1. If you aren't connected to Bitbucket, choose **Manage default source credential**.

     1. For **Credential type**, choose **CodeConnections**.

     1. In **Connection**, choose to use an existing connection or create a new connection.
   + Choose **Custom source credential** to use a custom source credential to override your account's default settings.

     1. For **Credential type**, choose **CodeConnections**.

     1. In **Connection**, choose to use an existing connection or create a new connection.

------
#### [ AWS CLI ]

**To configure a connection as an account level credential in the AWS CLI**
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the **import-source-credentials** command, specifying the `--auth-type`, `--server-type`, and `--token` for your connection.

  Use the following command:

  ```
  aws codebuild import-source-credentials --auth-type CODECONNECTIONS --server-type BITBUCKET --token {{<connection-arn>}}
  ```

------

For more information about setting up multiple tokens in your CodeBuild project, see [Configure multiple tokens as source level credentials](multiple-access-tokens.md#asm-source-credential).

## Bitbucket OAuth rotating refresh tokens
<a name="connections-bitbucket-migrate-from-oauth"></a>

Atlassian now enforces single-use rotating refresh tokens for Bitbucket OAuth. Each time you use a refresh token, Bitbucket invalidates it and returns a new one. For more information, see [Bitbucket OAuth single-use refresh tokens (CHANGE-3052)](https://developer.atlassian.com/cloud/bitbucket/changelog/#CHANGE-3052) on the Atlassian developer website.

### Required action for Secrets Manager-stored credentials
<a name="connections-bitbucket-oauth-sm-action"></a>

If you store Bitbucket OAuth credentials in Secrets Manager, add the `secretsmanager:PutSecretValue` permission to your CodeBuild service role. With this permission, CodeBuild can write the updated refresh token back to your secret after each token refresh. Without this permission, the next build after a token refresh fails.

The following example IAM policy statement grants the required permission:

```
{
    "Effect": "Allow",
    "Action": "secretsmanager:PutSecretValue",
    "Resource": "arn:aws:secretsmanager:*:*:secret:codebuild/*"
}
```

If you use the CodeBuild-managed option, no changes are needed. CodeBuild handles token rotation automatically.

### Migrate to AWS CodeConnections (recommended)
<a name="connections-bitbucket-migrate-to-codeconnections"></a>

We recommend migrating to AWS CodeConnections for Bitbucket integration. AWS CodeConnections uses a separate authorization mechanism that rotating refresh tokens do not affect. You don't need to manage tokens or add permissions.

To migrate to AWS CodeConnections, complete the following steps:

1. Open the Developer Tools console. Choose **Settings**, **Connections**, then **Create connection**. Select **Bitbucket** as the provider.

1. Authorize the AWS CodeConnections app in your Bitbucket workspace. This requires *Administer workspace* permission in Bitbucket.

1. Add the following permissions to your CodeBuild service role: `codeconnections:GetConnectionToken` and `codeconnections:GetConnection`.

1. Set the connection as your default credential:

   ```
   aws codebuild import-source-credentials --auth-type CODECONNECTIONS --server-type BITBUCKET --token {{<connection-arn>}}
   ```

1. All projects using the default credential switch automatically. Update projects that use custom, per-project credentials individually. Use the console or the `UpdateProject` API.