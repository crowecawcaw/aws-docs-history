# Self-managed GitLab runners in AWS CodeBuild

GitLab provides two execution modes to run GitLab jobs in your CI/CD pipeline. One mode is GitLab-hosted runners,
which are managed by GitLab and fully integrated with GitLab. The other mode is self-managed runners, which allows you
to bring your own customized environment to run jobs in the GitLab CI/CD pipeline.

The high-level steps to configure a CodeBuild project to run GitLab CI/CD pipeline jobs are as
follows:

1. If you haven't done so already, connect with an
   OAuth app to connect your project to GitLab.
2. Navigate to the CodeBuild console and create a CodeBuild project with a webhook and
   set up your webhook filters.
3. Update your GitLab CI/CD pipeline YAML in GitLab to configure your build
   environment.
   For a more detailed procedure, see [Tutorial: Configure a CodeBuild-hosted GitLab
   runner](sample-gitlab-runners.md "sample-gitlab-runners.md").

This feature allows your GitLab CI/CD pipeline jobs to get native integration with
AWS, which provides security and convenience through features like IAM,
AWS CloudTrail, and Amazon VPC. You can access latest instance types, including ARM-based
instances.

###### Topics

- [About the CodeBuild-hosted GitLab
  runner](gitlab-runner-questions.md "gitlab-runner-questions.md")
- [Tutorial: Configure a CodeBuild-hosted GitLab
  runner](sample-gitlab-runners.md "sample-gitlab-runners.md")
- [Label overrides
  supported with the CodeBuild-hosted GitLab runner](gitlab-runners-update-labels.md "gitlab-runners-update-labels.md")
- [Compute images
  supported with the CodeBuild-hosted GitLab runner](sample-gitlab-runners-gitlab-ci.md "sample-gitlab-runners-gitlab-ci.md")
