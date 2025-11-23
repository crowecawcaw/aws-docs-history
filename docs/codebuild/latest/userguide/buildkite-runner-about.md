# About the CodeBuild-hosted Buildkite runner

The following are some common questions about the CodeBuild-hosted Buildkite
runner.

## When should I include the image

and instance overrides in the label?

You can include the image and instance overrides in the label in order to specify
different build environment for each of your Buildkite jobs. This can be done
without the need to create multiple CodeBuild projects or webhooks. For example, this is
useful when you need to use a [matrix for Buildkite jobs](https://buildkite.com/docs/pipelines/configure/workflows/build-matrix "https://buildkite.com/docs/pipelines/configure/workflows/build-matrix").

```
agents:
  queue: "myQueue"
steps:
  - command: "echo \"Hello World\""
    agents:
      project: "codebuild-myProject"
      image: "{{matrix.os}}"
      instance-size: "{{matrix.size}}"
    matrix:
      setup:
        os:
          - "arm-3.0"
          - "al2-5.0"
        size:
          - "small"
          - "large"
```

## Can CodeBuild create webhooks

within Buildkite automatically?

Currently, Buildkite requires that all webhooks are created manually using their
console. You can follow the tutorial at [Tutorial: Configure a CodeBuild-hosted Buildkite
runner](sample-runner-buildkite.md "sample-runner-buildkite.md") to create a Buildkite webhook manually
in the Buildkite console.

## Can I use CloudFormation to create

Buildkite webhooks?

CloudFormation is not currently supported for Buildkite runner webhooks, as Buildkite
requires webhooks to be created manually using their console.

## Which regions support using a

CodeBuild-hosted Buildkite runner?

CodeBuild-hosted Buildkite runners are supported in all CodeBuild regions. For more
information about AWS Regions where CodeBuild is available, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").
