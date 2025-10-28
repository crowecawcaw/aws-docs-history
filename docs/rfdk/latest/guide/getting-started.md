# Getting started with the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

This topic introduces you to important RFDK concepts and describes how to install and configure the RFDK.

###### Topics in this chapter include:

- [Prerequisites](#prerequisites "#prerequisites")
- [Onboarding to CDK](#onboarding-to-cdk "#onboarding-to-cdk")
- [Example development environment using Cloud9 and CodeCommit](example-dev-env.md "example-dev-env.md")
- [Your first RFDK app](first-rfdk-app.md "first-rfdk-app.md")

## Prerequisites

RFDK applications are written for the AWS CDK toolkit, so you first need to fulfill the [AWS CDK prerequisites](../../../cdk/latest/guide/getting_started.md#getting_started_prerequisites "../../../cdk/latest/guide/getting_started.md#getting_started_prerequisites"). This includes:

- Installing Node.js
- Providing AWS credentials and region (optionally installing AWS CLI)
- Installing the programming language of your choice
- Installing the AWS CDK Toolkit

###### Important

The CDK and the RFDK both require Node.js to be installed, no matter the language you work in. The [minimal supported version of Node.js for RFDK](https://github.com/aws/aws-rfdk#render-farm-deployment-kit-on-aws-rfdk "https://github.com/aws/aws-rfdk#render-farm-deployment-kit-on-aws-rfdk") may differ from the [version required for CDK](https://github.com/aws/aws-cdk#aws-cloud-development-kit-aws-cdk "https://github.com/aws/aws-cdk#aws-cloud-development-kit-aws-cdk"), so you need to use the greater of them.

Similarly, RFDK currently supports applications written in Python and TypeScript. If using Python, the [minimal supported version of Python for RFDK](https://github.com/aws/aws-rfdk#render-farm-deployment-kit-on-aws-rfdk "https://github.com/aws/aws-rfdk#render-farm-deployment-kit-on-aws-rfdk") may differ from the [version required for CDK](https://github.com/aws/aws-cdk#aws-cloud-development-kit-aws-cdk "https://github.com/aws/aws-cdk#aws-cloud-development-kit-aws-cdk"), so you need to use the greater of them.

RFDK provides [Docker](https://docs.docker.com/get-started/overview/ "https://docs.docker.com/get-started/overview/") recipes for building container images for the RFDK server components such as the Deadline Render Queue and
Deadline Usage Based Licensing.
You will need to [install Docker](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") if you plan to use these components. RFDK requires _Docker 17.05_ or later.
We also provide a [walkthrough for setting up a example development environment](example-dev-env.md "example-dev-env.md") with all the necessary prerequisites installed.

## Onboarding to CDK

We recommend that you learn the CDK and the CDK deployment workflow with [getting started with the AWS CDK](../../../cdk/latest/guide/getting_started.md "../../../cdk/latest/guide/getting_started.md").
If you want to have a more in-depth tour that includes setting up your development environment and learning how to work with the CDK, then we recommend the official
[CDK Workshop](https://cdkworkshop.com/ "https://cdkworkshop.com/").

You need to bootstrap your account using the CDK toolkit before you can deploy a CDK application into an AWS region. This needs to be done one time for each region
that you want to deploy into using your account. Learn more about how to bootstrap your account from the official CDK documentation on
[bootstrapping your AWS environment](../../../cdk/latest/guide/cli.md#cli-bootstrap "../../../cdk/latest/guide/cli.md#cli-bootstrap").
