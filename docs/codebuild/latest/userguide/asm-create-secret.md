

# Create and store a token in a Secrets Manager secret
<a name="asm-create-secret"></a>

If you choose to store your access token using Secrets Manager, you can use either an existing secret connection or create a new secret. To create a new secret, do the following:

------
#### [ AWS Management Console ]

**To create a Secrets Manager secret in the AWS Management Console**

1. For **Source provider**, choose **Bitbucket**, **GitHub**, or **GitHub Enterprise**.

1. For **Credential**, do one of the following:
   + Choose **Default source credential** to use your account's default source credential to apply to all projects.

     1. If you aren't connected to your source provider, choose **Manage default source credential**.

     1. For **Credential type**, choose a credential type other than **CodeConnections**.

     1. For **Service**, choose **Secrets Manager** and for **Secrets** choose **New secret**.

     1. In **Secret name**, enter the name of your secret.

     1. In **Secret description - optional**, enter a description for your secret.

     1. Depending on the source provider you chose, enter your token or username and app password, and choose **Save**. For a Bitbucket API token, enter your Atlassian account email address and API token instead.
   + Choose **Custom source credential** to use a custom source credential to override your account's default settings.

     1. For **Credential type**, choose a credential type other than **CodeConnections**.

     1. In **Connection**, choose **Create a secret**.

     1. In **Secret name**, enter the name of your secret.

     1. In **Secret description - optional**, enter a description for your secret.

     1. Depending on the source provider you chose, enter your token or username and app password, and choose **Create**. For a Bitbucket API token, enter your Atlassian account email address and API token instead.

------
#### [ AWS CLI ]

**To create a Secrets Manager secret in the AWS CLI**
+ Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run the Secrets Manager **create-secret** command.

  ```
  aws secretsmanager create-secret --region {{<aws-region>}} \
              --name '{{<secret-name>}}' \
              --description '{{<secret-description>}}' \
              --secret-string '{
                  "ServerType":"{{<server-type>}}",
                  "AuthType":"{{<auth-type>}}",
                  "Token":"{{<token>}}"
                  }' \
              --tags Key=codebuild:source,Value='' \
                  Key=codebuild:source:type,Value={{<type>}} \
                  Key=codebuild:source:provider,Value={{<provider>}}
  ```

  The Secrets Manager secrets that CodeBuild accepts must be in the same account and AWS Region as the CodeBuild project and must be in the following JSON format:

  ```
  {
              "ServerType": ServerType,
              "AuthType: AuthType,
              "Token": string,
              "Username": string // Optional and is only used for Bitbucket app password or API token
          }
  ```    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/codebuild/latest/userguide/asm-create-secret.html)

  Additionally, CodeBuild uses the following resource tags on the secret to ensure the secrets are easily selectable when creating or editing projects.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/codebuild/latest/userguide/asm-create-secret.html)

------