# Bitbucket app password or access token

## Prerequisites

Before you begin, you must add the proper permission scopes to your Bitbucket app
password or access token.

For Bitbucket, your app password or access token must have the following scopes.

- **repository:read**: Grants read access to
  all the repositories to which the authorizing user has access.
- **pullrequest:read**: Grants read access to
  pull requests. If your project has a Bitbucket webhook, then your app
  password or access token must have this scope.
- **webhook**: Grants access to webhooks. If
  your project has a webhook operation, then your app password or access token must have this
  scope.

For more information, see [Scopes for Bitbucket Cloud REST API](https://developer.atlassian.com/cloud/bitbucket/bitbucket-cloud-rest-api-scopes/ "https://developer.atlassian.com/cloud/bitbucket/bitbucket-cloud-rest-api-scopes/") and [OAuth on Bitbucket Cloud](https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html "https://confluence.atlassian.com/bitbucket/oauth-on-bitbucket-cloud-238027431.html") on the Bitbucket website.

## Connect Bitbucket with an app

password (console)

To use the console to connect your project to Bitbucket using an app password, do
the following when you create a project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console").

1. For **Source provider**, choose
   **Bitbucket**.
2. For **Credential**, do one of the following:
   - Choose to use account credentials to apply your account's default source credential to all projects.
     1. If you aren't connected to Bitbucket, choose **Manage account credential**.
     2. For **Credential type**, choose **App password**.

   - If you chose to use account level credentials for **Service**, choose which service you'd like to use to store your token and do the following:
     1. If you choose to use **Secrets Manager**, you can choose to use an existing secret connection or create a new secret, and then choose **Save**.
        For more information how to create a new secret, see [Create and store a token in a Secrets Manager secret](asm-create-secret.md "asm-create-secret.md").
     2. If you choose to use **CodeBuild**, enter your Bitbucket username and app password, and then choose **Save**.

   - Select **Use override credentials for this project only** to use a custom source credential to override your account's credential settings.
     1. From the populated credential list, choose one of the options under **App password**.
     2. You can also create new App password token by selecting **create a new app password connection** in the description.

## Connect Bitbucket with an access

token (console)

To use the console to connect your project to Bitbucket using an access token, do
the following when you create a project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console").

1. For **Source provider**, choose
   **Bitbucket**.
2. For **Credential**, do one of the following:
   - Choose to use account credentials to apply your account's default source credential to all projects.
     1. If you aren't connected to Bitbucket, choose **Manage account credential**.
     2. For **Credential type**, choose **Personal access token**.

   - If you chose to use account level credentials for **Service**, choose which service you'd like to use to store your token and do the following:
     1. If you choose to use **Secrets Manager**, you can choose to use an existing secret connection or create a new secret, and then choose **Save**.
        For more information how to create a new secret, see [Create and store a token in a Secrets Manager secret](asm-create-secret.md "asm-create-secret.md").
     2. If you choose to use **CodeBuild**, enter your Bitbucket personal access token, and then choose **Save**.

   - Select **Use override credentials for this project only** to use a custom source credential to override your account's credential settings.
     1. From the populated credential list, choose one of the options under **Personal access token**.
     2. You can also create new personal access token by selecting **create a new personal access token connection** in the description.

## Connect Bitbucket with an app

password or access token(CLI)

Follow these steps to use the AWS CLI to connect your project to Bitbucket using an
app password or access token. For information about using the AWS CLI with AWS CodeBuild, see the [Command line reference](cmd-ref.md "cmd-ref.md").

1. Run the **import-source-credentials** command:

```
aws codebuild import-source-credentials --generate-cli-skeleton
```

JSON-formatted data appears in the output. Copy the data to a file (for
example,
`import-source-credentials.json`)
in a location on the local computer or instance where the AWS CLI is
installed. Modify the copied data as follows, and save your results.

```
{
    "serverType": "BITBUCKET",
    "authType": "`auth-type`",
    "shouldOverwrite": "`should-overwrite`",
    "token": "`token`",
    "username": "`username`"
    }
```

Replace the following:

    * `server-type`: Required value. The source
     provider used for this credential. Valid values are GITHUB, BITBUCKET,
     GITHUB\_ENTERPRISE, GITLAB, and GITLAB\_SELF\_MANAGED.
    * `auth-type`: Required value. The type of
     authentication used to connect to a repository. Valid values are OAUTH,
     BASIC\_AUTH, PERSONAL\_ACCESS\_TOKEN, CODECONNECTIONS, and SECRETS\_MANAGER.
     For GitHub, only PERSONAL\_ACCESS\_TOKEN is allowed. BASIC\_AUTH is only
     allowed with Bitbucket app password.
    * `should-overwrite`: Optional value. Set
     to `false` to prevent overwriting the repository source
     credentials. Set to `true` to overwrite the repository
     source credentials. The default value is `true`.
    * `token`: Required value. For GitHub or
     GitHub Enterprise Server, this is the personal access token. For
     Bitbucket, this is the personal access token or app password. For the
     auth-type CODECONNECTIONS, this is the connection ARN. For the auth-type
     SECRETS\_MANAGER, this is the secret ARN.
    * `username`: Optional value. This
     parameter is ignored for GitHub and GitHub Enterprise Server source
     providers.

2. To connect your account with an app password or an access token, switch to the directory that
   contains the `import-source-credentials.json` file you
   saved in step 1 and run the
   **import-source-credentials** command again.

```
aws codebuild import-source-credentials --cli-input-json file://import-source-credentials.json
```

JSON-formatted data appears in the output with an Amazon Resource Name
(ARN).

```
{
    "arn": "arn:aws:codebuild:`region`:`account-id`:token/`server-type`"
    }
```

###### Note

If you run the **import-source-credentials**
command with the same server type and auth type a second time, the
stored access token is updated.

After your account is connected with an app password, you can use
`create-project` to create your CodeBuild project. For more
information, see [Create a build project (AWS CLI)](create-project.md#create-project-cli "create-project.md#create-project-cli"). 3. To view the connected app passwords or access tokens, run the
**list-source-credentials** command.

```
aws codebuild list-source-credentials
```

A JSON-formatted `sourceCredentialsInfos` object appears in the
output:

```
{
        "sourceCredentialsInfos": [
            {
                "authType": "`auth-type`",
                "serverType": "BITBUCKET",
                "arn": "`arn`"
            }
        ]
    }

```

The `sourceCredentialsObject` contains a list of connected
source credentials information:

    * The `authType` is the type of authentication used by
     credentials. This can be `OAUTH`,
     `BASIC_AUTH`, `PERSONAL_ACCESS_TOKEN`,
     `CODECONNECTIONS`, or `SECRETS_MANAGER`.
    * The `serverType` is the type of source provider. This
     can be `GITHUB`, `GITHUB_ENTERPRISE`,
     `BITBUCKET`, `GITLAB`, or `GITLAB_SELF_MANAGED`.
    * The `arn` is the ARN of the token.

4. To disconnect from a source provider and remove its app password or access tokens, run the
   **delete-source-credentials** command with its ARN.

```
aws codebuild delete-source-credentials --arn `arn-of-your-credentials`
```

JSON-formatted data is returned with an ARN of the deleted credentials.

```
{
    "arn": "arn:aws:codebuild:`region`:`account-id`:token/`server-type`"
    }
```
