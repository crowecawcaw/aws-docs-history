# About the CodeBuild-hosted GitLab

runner

The following are some common questions about the CodeBuild-hosted GitLab
runner.

## What source types are supported for CodeBuild-hosted GitLab runners?

CodeBuild-hosted GitLab runners are supported for the `GITLAB` and `GITLAB_SELF_MANAGED` source type.

## When should I include the image and

instance overrides in the label?

You can include the image and instance overrides in the label in order to specify
different build environment for each of your GitLab CI/CD pipeline jobs. This can
be done without the need to create multiple CodeBuild projects or webhooks.

## Can I use CloudFormation for this feature?

Yes, you can include a filter group in your CloudFormation template that specifies a GitLab workflow job event filter in your project webhook.

```
Triggers:
  Webhook: true
  FilterGroups:
    - - Type: EVENT
        Pattern: WORKFLOW_JOB_QUEUED
```

For more information, see [Filter GitLab webhook events (CloudFormation)](gitlab-webhook-events-cfn.md "gitlab-webhook-events-cfn.md").

If you need help setting up project credentials in your CloudFormation template, see [AWS::CodeBuild::SourceCredential](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.md") in the
_AWS CloudFormation User Guide_ for more information.

## How can I mask secrets when using this

feature?

By default, secrets that are printed in the log is not masked. If you would like to mask your secrets,
you can do so by updating your CI/CD environment variable settings:

###### To mask secrets in GitLab

1. In your **GitLab Settings**, choose **CI/CD**.
2. In **Variables**, choose **Edit** for the secret you'd like to mask.
3. In **Visibility**, select **Mask variable**, and then choose
   **Update variable** to save your changes.

## Can I receive GitLab webhook events from multiple projects within a single group?

CodeBuild supports group webhooks, which receive events from a specified GitLab group.
For more information, see [GitLab group webhooks](gitlab-group-webhook.md "gitlab-group-webhook.md").

## Can I execute a job in docker executor for the self-managed

runner? For example, I want to run a pipeline job on a specific image to maintain the same build
environment in a separate and isolated container.

You can run the GitLab self-managed runner in CodeBuild with a specific image by [creating the project
with a custom image](create-project.md#environment-image.console "create-project.md#environment-image.console") or [overriding the image](sample-gitlab-runners.md#sample-gitlab-runners-gitlab-ci "sample-gitlab-runners.md#sample-gitlab-runners-gitlab-ci") in your `.gitlab-ci.yml` file.

## What executor does the self-managed runner in CodeBuild run with?

The self-managed runner in CodeBuild runs with the shell executor, where the build runs locally along with the
GitLab runner that is running inside the docker container.

## Can I provide buildspec commands along with the self-managed runner?

Yes, it is possible to add buildspec commands along with self-managed runner. You can provide the buildspec.yml file
in your GitLab repository and use the `buildspec-override:true` tag in the **Tags** section of the job. For more information, see
[Buildspec file name and storage
location](build-spec-ref.md#build-spec-ref-name-storage "build-spec-ref.md#build-spec-ref-name-storage").

## Which regions support using a

CodeBuild-hosted GitLab runner?

CodeBuild-hosted GitLab runners are supported in all CodeBuild regions. For more
information about AWS Regions where CodeBuild is available, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Which platforms support using a

CodeBuild-hosted GitLab runner?

CodeBuild-hosted GitLab runners are supported on both Amazon EC2 and [AWS Lambda](lambda.md "lambda.md") compute. You can use the following platforms:
Amazon Linux 2, Amazon Linux 2023, Ubuntu, and Windows Server Core 2019. For more information,
see [EC2 compute images](ec2-compute-images.md "ec2-compute-images.md") and
[Lambda compute images](lambda-compute-images.md "lambda-compute-images.md").
