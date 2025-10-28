# Create and store a token in a Secrets Manager secret

If you choose to use to store your access token using Secrets Manager, you can use either an existing
secret connection or create a new secret. To create a new secret, do the following:

AWS Management Console

###### To create a Secrets Manager secret in the AWS Management Console

1. For **Source provider**, choose **Bitbucket**,
   **GitHub**, or **GitHub Enterprise**.
2. For **Credential**, do one of the following:
   - Choose **Default source credential** to use
     your account's default source credential to apply to all projects.
     1. If you aren't connected to your source provider, choose **Manage default source credential**.
     2. For **Credential type**, choose a credential type other than **CodeConnections**.
     3. For **Service**, choose **Secrets Manager** and for **Secrets**
        choose **New secret**.
     4. In **Secret name**, enter the name of your secret.
     5. In **Secret description - optional**, enter a description for your secret.
     6. Depending on the source provider you chose, enter your
        token or username and app password and choose **Save**.

   - Choose **Custom source credential** to use
     a custom source credential to override your account's default settings.
     1. For **Credential type**, choose a credential type other than **CodeConnections**.
     2. In **Connection**, choose **Create a secret**.
     3. In **Secret name**, enter the name of your secret.
     4. In **Secret description - optional**, enter a description for your secret.
     5. Depending on the source provider you chose, enter your
        token or username and app password, and choose **Create**.

AWS CLI

###### To create a Secrets Manager secret in the AWS CLI

- Open a terminal (Linux, macOS, or Unix) or command prompt (Windows). Use the AWS CLI to run
  the Secrets Manager **create-secret** command.

```
aws secretsmanager create-secret --region `<aws-region>` \
            --name '`<secret-name>`' \
            --description '`<secret-description>`' \
            --secret-string '{
                "ServerType":"`<server-type>`",
                "AuthType":"`<auth-type>`",
                "Token":"`<token>`"
                }' \
            --tags Key=codebuild:source,Value='' \
                Key=codebuild:source:type,Value=`<type>` \
                Key=codebuild:source:provider,Value=`<provider>`
```

The Secrets Manager secrets that CodeBuild accept must be in the same account and AWS Region as the CodeBuild project and must be in the following JSON format:

```
{
            "ServerType": ServerType,
            "AuthType: AuthType,
            "Token": string,
            "Username": string // Optional and is only used for Bitbucket app password
        }
```

| Field                     | Valid values                       | Description                                                                                                                                             |
| ------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| ServerType                | GITHUB GITHUB_ENTERPRISE BITBUCKET | The third party source provider for your Secrets Manager secret.                                                                                        |
| AuthType                  | PERSONAL_ACCESS_TOKEN BASIC_AUTH   | The type of access token used by the credentials. For GitHub, only PERSONAL_ACCESS_TOKEN is valid. BASIC_AUTH is only valid for Bitbucket app password. |
| Token                     | `string`                           | For GitHub or GitHub Enterprise, this is the personal access token. For Bitbucket, this is either the access token or the Bitbucket app password.       |
| Username                  | `string`                           | The Bitbucket username when the AuthType is BASIC_AUTH. This parameter is not valid for other types of source providers.                                | Additionally, CodeBuild uses the following resource tags on the secret to ensure the secrets are easily selectable when creating or editing projects. |
| Tag key                   | Tag value                          | Description                                                                                                                                             |
| ---                       | ---                                | ---                                                                                                                                                     |
| codebuild:source:provider | github github_enterprise bitbucket | Tells CodeBuild which provider this secret is intended for.                                                                                             |
| codebuild:source:type     | personal_access_token basic_auth   | Tells CodeBuild the type of access token in this secret.                                                                                                |
