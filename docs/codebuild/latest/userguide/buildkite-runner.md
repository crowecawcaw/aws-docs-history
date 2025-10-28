# Self-managed Buildkite runner in AWS CodeBuild

You can configure your project to set up self-hosted Buildkite runners in CodeBuild containers
to process your Buildkite jobs. This can be done by setting up a webhook using your CodeBuild
project, and updating your Buildkite pipeline YAML steps to use self-hosted runners hosted
on CodeBuild machines.

The high-level steps to configure a CodeBuild project to run Buildkite jobs are as
follows:

- Navigate to the CodeBuild console and create a CodeBuild project with the Buildkite runner
  project runner type configuration
- Add a `job.scheduled` webhook to your Buildkite organization.
- Update your Buildkite pipeline YAML steps in Buildkite to configure your build
  environment.
  For a more detailed procedure, see [Tutorial: Configure a CodeBuild-hosted Buildkite
  runner](sample-runner-buildkite.md "sample-runner-buildkite.md"). This feature allows your Buildkite jobs to
  get native integration with AWS, which provides security and convenience through features
  like IAM, AWS Secrets Manager, AWS CloudTrail, and Amazon VPC. You can access the latest instance types,
  including ARM-based instances.
