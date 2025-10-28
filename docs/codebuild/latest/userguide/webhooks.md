# Use webhooks with AWS CodeBuild

AWS CodeBuild supports webhook integration with GitHub, GitHub Enterprise Server, GitLab, GitLab Self Managed, and
Bitbucket.

###### Topics

- [Best practices for using webhooks with
  AWS CodeBuild](#webhook-best-practices "#webhook-best-practices")
- [Bitbucket webhook events](bitbucket-webhook.md "bitbucket-webhook.md")
- [GitHub global and organization
  webhooks](github-global-organization-webhook.md "github-global-organization-webhook.md")
- [GitHub manual webhooks](github-manual-webhook.md "github-manual-webhook.md")
- [GitHub webhook events](github-webhook.md "github-webhook.md")
- [GitLab group webhooks](gitlab-group-webhook.md "gitlab-group-webhook.md")
- [GitLab manual webhooks](gitlab-manual-webhook.md "gitlab-manual-webhook.md")
- [GitLab webhook events](gitlab-webhook.md "gitlab-webhook.md")
- [Buildkite manual webhooks](buildkite-manual-webhook.md "buildkite-manual-webhook.md")
- [Pull request comment approval](pull-request-build-policy.md "pull-request-build-policy.md")

## Best practices for using webhooks with

AWS CodeBuild

For projects that use public repositories to setup webhooks, we recommend the following
options:

Setup `ACTOR_ACCOUNT_ID` filters

Add `ACTOR_ACCOUNT_ID` filters to your project’s webhook filter
groups to specify which users can trigger a build. Every webhook event delivered
to CodeBuild comes with sender information that specifies the actor's identifier.
CodeBuild will filter the webhooks based on the regular expression pattern provided
in the filters. You can specify the specific users that are allowed to trigger
builds with this filter. For more information, see [GitHub webhook events](github-webhook.md "github-webhook.md") and [Bitbucket webhook events](bitbucket-webhook.md "bitbucket-webhook.md").

Setup `FILE_PATH` filters

Add `FILE_PATH` filters to your project’s webhook filter groups to
include or exclude the files that can trigger a build when changed. For example,
you can deny build requests for changes to the
`buildspec.yml` file using a regular expression pattern
such as `^buildspec.yml$`, along with the
`excludeMatchedPattern` property. For more information, see [GitHub webhook events](github-webhook.md "github-webhook.md") and [Bitbucket webhook events](bitbucket-webhook.md "bitbucket-webhook.md").

Scope down the permissions for your build IAM role

Builds triggered by a webhook use the IAM service role specified in the
project. We recommend setting the permissions in the service role to the minimum
set of permissions required to run the build. For example, in a test and deploy
scenario, create one project for testing and another project for deployment. The
testing project accepts webhook builds from the repository, but provides no
write permissions to your resources. The deployment project provides write
permissions to your resources, and the webhook filter is configured to only
allow trusted users to trigger builds.

Use an inline or an Amazon S3 stored buildspec

If you define your buildspec inline within the project itself, or store the
buildspec file in an Amazon S3 bucket, the buildspec file is only visible to the
project owner. This prevents pull requests from making code changes to the
buildspec file and triggering unwanted builds. For more information, see [ProjectSource.buildspec](../APIReference/API_ProjectSource.md#CodeBuild-Type-ProjectSource-buildspec "../APIReference/API_ProjectSource.md#CodeBuild-Type-ProjectSource-buildspec") in the _CodeBuild
API Reference_.
