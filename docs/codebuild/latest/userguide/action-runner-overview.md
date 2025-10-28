# Self-hosted GitHub Actions runners in AWS CodeBuild

You can configure your project to set up self-hosted GitHub Actions runners in CodeBuild
containers to process your GitHub Actions workflow jobs. This can be done by setting up a
webhook using your CodeBuild project, and updating your GitHub Actions workflow YAML to use
self-hosted runners hosted on CodeBuild machines.

The high-level steps to configure a CodeBuild project to run GitHub Actions jobs are as
follows:

1. If you haven't done so already, create a personal access token or connect with an
   OAuth app to connect your project to GitHub.
2. Navigate to the CodeBuild console and create a CodeBuild project with a webhook and
   set up your webhook filters.
3. Update your GitHub Actions workflow YAML in GitHub to configure your build
   environment.
   For a more detailed procedure, see [Tutorial: Configure a CodeBuild-hosted GitHub
   Actions runner](action-runner.md "action-runner.md").

This feature allows your GitHub Actions workflow jobs to get native integration with
AWS, which provides security and convenience through features like IAM, AWS Secrets Manager
integration, AWS CloudTrail, and Amazon VPC. You can access latest instance types, including ARM-based
instances.

###### Topics

- [About the CodeBuild-hosted GitHub Actions
  runner](action-runner-questions.md "action-runner-questions.md")
- [Tutorial: Configure a CodeBuild-hosted GitHub
  Actions runner](action-runner.md "action-runner.md")
- [Troubleshoot the webhook](action-runner-troubleshoot-webhook.md "action-runner-troubleshoot-webhook.md")
- [Label overrides
  supported with the CodeBuild-hosted GitHub Actions runner](sample-github-action-runners-update-labels.md "sample-github-action-runners-update-labels.md")
- [Compute images
  supported with the CodeBuild-hosted GitHub Actions runner](sample-github-action-runners-update-yaml.md "sample-github-action-runners-update-yaml.md")
