# About the CodeBuild-hosted GitHub Actions

runner

The following are some common questions about the CodeBuild-hosted GitHub Actions
runner.

## When should I include the image and

instance overrides in the label?

You can include the image and instance overrides in the label in order to specify
different build environment for each of your GitHub Actions workflow jobs. This can
be done without the need to create multiple CodeBuild projects or webhooks. For example,
this is useful when you need to use a [matrix for your workflow jobs](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs "https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs").

```
name: Hello World
on: [push]
jobs:
  Hello-World-Job:
    runs-on:
      - codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
        image:${{ matrix.os }}
        instance-size:${{ matrix.size }}
    strategy:
      matrix:
        include:
          - os: arm-3.0
            size: small
          - os: linux-5.0
            size: large
    steps:
      - run: echo "Hello World!"
```

###### Note

Quotation marks might be required if `runs-on` has multiple labels
containing GitHub Actions context.

## Can I use AWS CloudFormation for this feature?

Yes, you can include a filter group in your AWS CloudFormation template that specifies a GitHub
Actions workflow job event filter in your project webhook.

```
Triggers:
  Webhook: true
  FilterGroups:
    - - Type: EVENT
        Pattern: WORKFLOW_JOB_QUEUED
```

For more information, see [Filter GitHub webhook events (AWS CloudFormation)](github-webhook-events-cfn.md "github-webhook-events-cfn.md").

If you need help setting up project credentials in your AWS CloudFormation template, see [AWS::CodeBuild::SourceCredential](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.md") in the
_AWS CloudFormation User Guide_ for more information.

## How can I mask secrets when using this

feature?

By default, secrets that are printed in the log is not masked. If you would like
to mask your secrets, you can use the following syntax:
`::add-mask::`value``. The following is
an example of how you can use this syntax in your YAML:

```
name: Secret Job
on: [push]
jobs:
  Secret-Job:
    runs-on: codebuild-myProject-${{ github.run_id }}-${{ github.run_attempt }}
    env:
      SECRET_NAME: "secret-name"
    steps:
      - run: echo "::add-mask::$SECRET_NAME"
```

For more information, see [Masking a value in a log](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#masking-a-value-in-a-log "https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#masking-a-value-in-a-log") on GitHub.

## Can I receive GitHub Actions webhook events from multiple repositories within a single project?

CodeBuild supports organization and global level webhooks, which receive events from a specified organization or enterprise.
For more information, see [GitHub global and organization
webhooks](github-global-organization-webhook.md "github-global-organization-webhook.md").

## Which regions support using a

CodeBuild-hosted GitHub Actions runner?

CodeBuild-hosted GitHub Actions runners are supported in all CodeBuild regions. For more
information about AWS Regions where CodeBuild is available, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Which platforms support using a

CodeBuild-hosted GitHub Actions runner?

CodeBuild-hosted GitHub Actions runners are supported on both Amazon EC2 and [AWS Lambda](lambda.md "lambda.md") compute. You can use the following platforms:
Amazon Linux 2, Amazon Linux 2023, Ubuntu, and Windows Server Core 2019. For more information,
see [EC2 compute images](ec2-compute-images.md "ec2-compute-images.md") and
[Lambda compute images](lambda-compute-images.md "lambda-compute-images.md").
