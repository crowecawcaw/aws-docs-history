# GitHub and GitHub Enterprise Server access

token

## Access token prerequisites

Before you begin, you must add the proper permission scopes to your GitHub access
token.

For GitHub, your personal access token must have the following scopes.

- **repo**: Grants full control of private
  repositories.
- **repo:status**: Grants read/write access to
  public and private repository commit statuses.
- **admin:repo_hook**: Grants full control of
  repository hooks. This scope is not required if your token has the
  `repo` scope.
- **admin:org_hook**: Grants full control of organization hooks.
  This scope is only required if you are using the organization webhook feature.

For more information, see [Understanding scopes for OAuth apps](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/ "https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/") on the GitHub website.

If you are using fine-grained personal access tokens, depending on your use case, your personal
access token might need the following permissions:

- **Contents: Read-only**: Grants access to private repositories.
  This permission is required if you are using private repositories as source.
- **Commit statuses: Read and write**: Grants permission to create
  commit statuses. This permission is required if your project has webhook set up, or you have report
  build status feature enabled.
- **Webhooks: Read and write**: Grants permission to manage webhooks.
  This permission is required if your project has webhook set up.
- **Pull requests: Read-only**: Grants permission to access pull requests.
  This permission is required if your webhook has a `FILE_PATH` filter on pull request events.
- **Administration: Read and write**: This permission is required if you are using the
  self-hosted GitHub Actions runner feature with CodeBuild. For more details, see [Create a registration token for a repository](https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28#create-a-registration-token-for-a-repository "https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28#create-a-registration-token-for-a-repository") and [Tutorial: Configure a CodeBuild-hosted GitHub
  Actions runner](action-runner.md "action-runner.md").

###### Note

If you want to access organization repositories, make sure you specify the organization as the resource owner of the access token.

For more information, see [Permissions required for fine-grained personal access tokens](https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2022-11-28 "https://docs.github.com/en/rest/authentication/permissions-required-for-fine-grained-personal-access-tokens?apiVersion=2022-11-28") on the GitHub website.

## Connect GitHub with an access token

(console)

To use the console to connect your project to GitHub using an access token, do the
following when you create a project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console").

1. For **Source provider**, choose
   **GitHub**.
2. For **Credential**, do one of the following:
   - Choose to use account credentials to apply your account's default source credential to all projects.
     1. If you aren't connected to GitHub, choose **Manage account credential**.
     2. For **Credential type**, choose **Personal access token**.

   - If you chose to use account level credentials for **Service**, choose which service you'd like to use to store your token and do the following:
     1. If you choose to use **Secrets Manager**, you can choose to use an existing secret connection or create a new secret, and then choose **Save**.
        For more information how to create a new secret, see [Create and store a token in a Secrets Manager secret](asm-create-secret.md "asm-create-secret.md").
     2. If you choose to use **CodeBuild**, enter your GitHub personal access token, and then choose **Save**.

   - Select **Use override credentials for this project only** to use a custom source credential to override your account's credential settings.
     1. From the populated credential list, choose one of the options under **Personal access token**.
     2. You can also create new personal access token by selecting **create a new personal access token connection** in the description.

## Connect GitHub with an access token

(CLI)

Follow these steps to use the AWS CLI to connect your project to GitHub using an
access token. For information about using the AWS CLI with AWS CodeBuild, see the [Command line reference](cmd-ref.md "cmd-ref.md").

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
    "serverType": "`server-type`",
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

2. To connect your account with an access token, switch to the directory that
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

After your account is connected with an access token, you can use
`create-project` to create your CodeBuild project. For more
information, see [Create a build project (AWS CLI)](create-project.md#create-project-cli "create-project.md#create-project-cli"). 3. To view the connected access tokens, run the
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
                "serverType": "`server-type`",
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

4. To disconnect from a source provider and remove its access tokens, run the
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
