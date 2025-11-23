# Appendix A: GitHub (via OAuth app) source

actions

This appendix provides information about (via OAuth app) of the GitHub action in
CodePipeline.

###### Note

While we don’t recommend using the GitHub (via OAuth app) action, existing pipelines with
the GitHub (via OAuth app) action will continue to work without any impact. For a pipeline
with a GitHub (via OAuth app) action, CodePipeline uses OAuth-based tokens to connect to your GitHub
repository. By contrast, the GitHub action (via GitHub App) uses a connection resource to
associate AWS resources to your GitHub repository. The connection resource uses app-based
tokens to connect. For more information about updating your pipeline to the recommended GitHub
action that uses a connection, see [Update a GitHub (via OAuth app) source action
to a GitHub (via GitHub App) source action](update-github-action-connections.md "update-github-action-connections.md"). For more information about OAuth-based
GitHub access in contrast to app-based GitHub access, see [https://docs.github.com/en/developers/apps/differences-between-github-apps-and-oauth-apps](https://docs.github.com/en/developers/apps/differences-between-github-apps-and-oauth-apps "https://docs.github.com/en/developers/apps/differences-between-github-apps-and-oauth-apps").

To integrate with GitHub, CodePipeline uses a GitHub OAuth application for your pipeline. CodePipeline
uses webhooks to manage change detection for your pipeline with the GitHub (via OAuth app)
source action.

###### Note

When you configure a GitHub (via GitHub App) source action in CloudFormation, you do not include
any GitHub token information or add a webhook resource. You configure a connections resource
as shown in [AWS::CodeStarConnections::Connection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.md") in the _CloudFormation User
Guide._

This reference contains the following sections for the GitHub (via OAuth app) action:

- For information about how to add a GitHub (via OAuth app) source action and webhook to a
  pipeline, see [Adding a GitHub (via OAuth app) source
  action](#appendix-github-methods "#appendix-github-methods").
- For information about the configuration parameters and example YAML/JSON snippets for a
  GitHub (via OAuth app) source action, see [GitHub (via OAuth app) source action
  reference](#action-reference-GitHub "#action-reference-GitHub").

###### Important

When creating CodePipeline webhooks, do not use your own credentials or reuse the same secret
token across multiple webhooks. For optimal security, generate a unique secret token for each
webhook you create. The secret token is an arbitrary string that you provide, which GitHub
uses to compute and sign the webhook payloads sent to CodePipeline, for protecting the integrity and
authenticity of the webhook payloads. Using your own credentials or reusing the same token
across multiple webhooks can lead to security vulnerabilities.

###### Note

If a secret token was provided, it will be redacted in the response.

###### Topics

- [Adding a GitHub (via OAuth app) source
  action](#appendix-github-methods "#appendix-github-methods")
- [GitHub (via OAuth app) source action reference](#action-reference-GitHub "#action-reference-GitHub")

## Adding a GitHub (via OAuth app) source

action

You add GitHub (via OAuth app) source actions to CodePipeline by:

- Using the CodePipeline console **Create pipeline** wizard ([Create a custom pipeline (console)](pipelines-create.md#pipelines-create-console "pipelines-create.md#pipelines-create-console")) or
  **Edit action** page to choose the **GitHub** provider
  option. The console creates a webhook that starts your pipeline when the source
  changes.
- Using the CLI to add the action configuration for the `GitHub` action and
  creating additional resources as follows:
  - Using the `GitHub` example action configuration in [GitHub (via OAuth app) source action
    reference](#action-reference-GitHub "#action-reference-GitHub") to
    create the action as shown in [Create a pipeline (CLI)](pipelines-create.md#pipelines-create-cli "pipelines-create.md#pipelines-create-cli").
  - Disabling periodic checks and creating the change detection manually, because the
    change detection method defaults to starting the pipeline by polling the source. You
    migrate your polling pipeline to webhooks for GitHub (via OAuth app) actions.

## GitHub (via OAuth app) source action

reference

###### Note

While we don’t recommend using the GitHub (via OAuth app) action, existing pipelines with
the GitHub (via OAuth app) action will continue to work without any impact. For a pipeline
with a GitHub GitHub (via OAuth app) source action, CodePipeline uses OAuth-based tokens to connect
to your GitHub repository. By contrast, the new GitHub action (via GitHub App) uses a
connection resource to associate AWS resources to your GitHub repository. The connection
resource uses app-based tokens to connect. For more information about updating your
pipeline to the recommended GitHub action that uses a connection, see [Update a GitHub (via OAuth app) source action
to a GitHub (via GitHub App) source action](update-github-action-connections.md "update-github-action-connections.md").

Triggers the pipeline when a new commit is made on the configured GitHub repository and
branch.

To integrate with GitHub, CodePipeline uses an OAuth application or a personal access token for
your pipeline. If you use the console to create or edit your pipeline, CodePipeline creates a
GitHub webhook that starts your pipeline when a change occurs in the repository.

You must have already created a GitHub account and repository before you connect the
pipeline through a GitHub action.

If you want to limit the access CodePipeline has to repositories, create a GitHub account and
grant the account access only to those repositories you want to integrate with CodePipeline. Use
that account when you configure CodePipeline to use GitHub repositories for source stages in
pipelines.

For more information, see the [GitHub developer
documentation](https://developer.github.com "https://developer.github.com") on the GitHub website.

###### Topics

- [Action type](#action-reference-GitHub-type "#action-reference-GitHub-type")
- [Configuration parameters](#action-reference-GitHub-config "#action-reference-GitHub-config")
- [Input artifacts](#action-reference-GitHub-input "#action-reference-GitHub-input")
- [Output artifacts](#action-reference-GitHub-output "#action-reference-GitHub-output")
- [Output variables](#action-reference-GitHub-variables "#action-reference-GitHub-variables")
- [Action declaration (GitHub
  example)](#action-reference-GitHub-example "#action-reference-GitHub-example")
- [Connecting to GitHub (OAuth)](#action-reference-GitHub-auth "#action-reference-GitHub-auth")
- [See also](#action-reference-GitHub-links "#action-reference-GitHub-links")

### Action type

- Category: `Source`
- Owner: `ThirdParty`
- Provider: `GitHub`
- Version: `1`

### Configuration parameters

**Owner**

Required: Yes

The name of the GitHub user or organization who owns the GitHub
repository.

**Repo**

Required: Yes

The name of the repository where source changes are to be detected.

**Branch**

Required: Yes

The name of the branch where source changes are to be detected.

**OAuthToken**

Required: Yes

Represents the GitHub authentication token that allows CodePipeline to perform
operations on your GitHub repository. The entry is always displayed as a
mask of four asterisks. It represents one of the following values:

- When you use the console to create the pipeline, CodePipeline uses an
  OAuth token to register the GitHub connection.
- When you use the AWS CLI to create the pipeline, you can pass your
  GitHub personal access token in this field. Replace the asterisks
  (\*\*\*\*) with your personal access token copied from GitHub. When you
  run `get-pipeline` to view the action configuration, the
  four-asterisk mask is displayed for this value.
- When you use an CloudFormation template to create the pipeline, you must
  first store the token as a secret in AWS Secrets Manager. You include the
  value for this field as a dynamic reference to the stored secret in
  Secrets Manager, such as
  `{{resolve:secretsmanager:MyGitHubSecret:SecretString:token}}`.

For more information about GitHub scopes, see the [GitHub Developer API
Reference](https://developer.github.com/v3/oauth/#scopes "https://developer.github.com/v3/oauth/#scopes") on the GitHub website.

**PollForSourceChanges**

Required: No

`PollForSourceChanges` controls whether CodePipeline polls the GitHub
repository for source changes. We recommend that you use webhooks to detect
source changes instead. For more information about configuring webhooks, see
[Migrate polling pipelines to
webhooks (GitHub (via OAuth app) source actions) (CLI)](update-change-detection.md#update-change-detection-cli-github "update-change-detection.md#update-change-detection-cli-github") or [Update pipelines for push
events (GitHub (via OAuth app) source actions) (CloudFormation template)](update-change-detection.md#update-change-detection-cfn-github "update-change-detection.md#update-change-detection-cfn-github").

###### Important

If you intend to configure webhooks, you must set
`PollForSourceChanges` to `false` to avoid
duplicate pipeline executions.

Valid values for this parameter:

- `True`: If set, CodePipeline polls your repository for source
  changes.

###### Note

If you omit `PollForSourceChanges`, CodePipeline defaults
to polling your repository for source changes. This behavior is
the same as if `PollForSourceChanges` is set to
`true`.

- `False`: If set, CodePipeline does not poll your repository
  for source changes. Use this setting if you intend to configure a
  webhook to detect source changes.

### Input artifacts

- **Number of artifacts:**
  `0`
- **Description:** Input artifacts do not apply for
  this action type.

### Output artifacts

- **Number of artifacts:**
  `1`
- **Description:** The output artifact of this
  action is a ZIP file that contains the contents of the configured repository and
  branch at the commit specified as the source revision for the pipeline
  execution. The artifacts generated from the repository are the output artifacts
  for the GitHub action. The source code commit ID is displayed in CodePipeline as the
  source revision for the triggered pipeline execution.

### Output variables

When configured, this action produces variables that can be referenced by the action
configuration of a downstream action in the pipeline. This action produces variables
which can be viewed as output variables, even if the action doesn't have a namespace.
You configure an action with a namespace to make those variables available to the
configuration of downstream actions.

For more information about variables in CodePipeline, see [Variables reference](reference-variables.md "reference-variables.md").

**CommitId**

The GitHub commit ID that triggered the pipeline execution. Commit IDs are
the full SHA of the commit.

**CommitMessage**

The description message, if any, associated with the commit that triggered
the pipeline execution.

**CommitUrl**

The URL address for the commit that triggered the pipeline.

**RepositoryName**

The name of the GitHub repository where the commit that triggered the
pipeline was made.

**BranchName**

The name of the branch for the GitHub repository where the source change
was made.

**AuthorDate**

The date when the commit was authored, in timestamp format.

**CommitterDate**

The date when the commit was committed, in timestamp format.

### Action declaration (GitHub

example)

YAML

```
Name: Source
Actions:
  - InputArtifacts: []
    ActionTypeId:
      Version: '1'
      Owner: ThirdParty
      Category: Source
      Provider: GitHub
    OutputArtifacts:
      - Name: SourceArtifact
    RunOrder: 1
    Configuration:
      Owner: MyGitHubAccountName
      Repo: MyGitHubRepositoryName
      PollForSourceChanges: 'false'
      Branch: main
      OAuthToken: '{{resolve:secretsmanager:MyGitHubSecret:SecretString:token}}'
    Name: ApplicationSource

```

JSON

```
{
    "Name": "Source",
    "Actions": [
        {
            "InputArtifacts": [],
            "ActionTypeId": {
                "Version": "1",
                "Owner": "ThirdParty",
                "Category": "Source",
                "Provider": "GitHub"
            },
            "OutputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "RunOrder": 1,
            "Configuration": {
                "Owner": "MyGitHubAccountName",
                "Repo": "MyGitHubRepositoryName",
                "PollForSourceChanges": "false",
                "Branch": "main",
                "OAuthToken": "{{resolve:secretsmanager:MyGitHubSecret:SecretString:token}}"
            },
            "Name": "ApplicationSource"
        }
    ]
},
```

### Connecting to GitHub (OAuth)

The first time you use the console to add a GitHub repository to a pipeline, you are
asked to authorize CodePipeline access to your repositories. The token requires the following
GitHub scopes:

- The `repo` scope, which is used for full control to read and pull
  artifacts from public and private repositories into a pipeline.
- The `admin:repo_hook` scope, which is used for full control of
  repository hooks.

When you use the CLI or an CloudFormation template, you must provide the value for a personal
access token that you have already created in GitHub.

### See also

The following related resources can help you as you work with this action.

- Resource reference for the [AWS CloudFormation User Guide
  AWS::CodePipeline::Webhook](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.md") – This includes field definitions,
  examples, and snippets for the resource in CloudFormation.
- Resource reference for the [AWS CloudFormation User Guide AWS::CodeStar::GitHubRepository](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.md") – This
  includes field definitions, examples, and snippets for the resource in
  CloudFormation.
- [Tutorial: Create a pipeline that builds and
  tests your Android app with AWS Device Farm](tutorials-codebuild-devicefarm.md "tutorials-codebuild-devicefarm.md") – This tutorial
  provides a sample build spec file and sample application to create a pipeline
  with a GitHub source. It builds and tests an Android app with CodeBuild and
  AWS Device Farm.
