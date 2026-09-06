# Explore Image Builder sample projects on GitHub

The EC2 Image Builder team maintains the [Image Builder
samples repository](https://github.com/aws-samples/amazon-ec2-image-builder-samples "https://github.com/aws-samples/amazon-ec2-image-builder-samples") on GitHub. The repository contains complete,
deployable sample projects that show how to implement common use cases with
infrastructure as code. Samples are available as AWS CloudFormation (CloudFormation) templates,
AWS Cloud Development Kit (AWS CDK) applications, Terraform modules, and
AWS Task Orchestrator and Executor (AWSTOE) component documents.

Each sample is self-contained, with its own README that covers prerequisites,
deployment steps, how the sample works, testing, and cleanup. The tutorials in
this chapter show you the image building process from the console. The sample
projects show you the same concepts expressed as code that you can deploy,
inspect, and adapt.

The repository includes samples for the following areas:

- **Getting started** – The smallest
  complete image pipeline, provided as both a CloudFormation template and an AWS CDK
  application in the `quick-start` sample.
- **Use-case kits** – Complete
  pipelines for common scenarios, such as a golden AMI pipeline with
  scheduled patching and Auto Scaling group refresh. Other kits cover
  cross-account AMI distribution, private VPC builds, lifecycle cleanup
  policies, and container base image pipelines that publish to
  Amazon Elastic Container Registry.
- **Image workflows** – Custom
  workflow samples that add human approval gates to the build and
  distribution stages, and integrate AWS Step Functions for out-of-band AMI
  validation.
- **Platform coverage** – Golden
  image pipelines for Windows Server, macOS, and Linux.
- **Components and debugging** –
  AWSTOE component patterns such as reboot-and-resume and build-time
  secrets. Also includes a script that tests component documents locally.
  A debugging walkthrough diagnoses a build that fails on purpose.
  For the full list of samples, see the index in the [repository README](https://github.com/aws-samples/amazon-ec2-image-builder-samples#readme "https://github.com/aws-samples/amazon-ec2-image-builder-samples#readme") on GitHub. The samples are licensed under MIT-0,
  and the team reviews issues and pull requests on a best-effort basis.
