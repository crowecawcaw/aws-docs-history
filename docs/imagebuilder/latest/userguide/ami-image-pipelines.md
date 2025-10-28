# Create and update AMI image pipelines

You can set up, configure, and manage AMI image pipelines from the Image Builder
console, through the Image Builder API, SDKs or the AWS CLI. In the console, you can use the
**Create image pipeline** console wizard to guide you through
the following steps.

- Specify pipeline details such as name, description, and resource tags.
- Configure pipeline schedule and logging defaults. For scheduled pipeline
  execution, you can set the number of consecutive failures that are allowed
  before Image Builder disables the pipeline.
- Select an AMI image recipe that includes a base image from quick-start
  Amazon managed images, images that you created or that were shared with you,
  or images that you subscribe to through the AWS Marketplace.
  The recipe also includes components that perform the following tasks on
  the EC2 instances that Image Builder uses to build your image:
  - Add and remove software
  - Customize settings and scripts
  - Run selected tests

- Specify workflows to configure image build and test steps that your
  pipeline runs.
- Define infrastructure configuration for your pipeline with default
  settings or settings that you configure yourself. Configuration includes
  the instance type and key pair to use for your image, security and network
  settings, log storage and troubleshooting settings, and SNS notifications.

This is an _optional_ step. Image Builder uses default settings
for your infrastructure configuration if you don't define the configuration
yourself.

- Define distribution settings to deliver your images to destination AWS
  Regions and accounts. You can specify a KMS key for encryption, configure
  AMI sharing or license configuration, or configure a launch template for
  the AMIs you distribute.

This is an _optional_ step. If you don't define the
configuration yourself, Image Builder uses default naming for your output AMI, and
distributes the AMI to the source Region. The source Region is the Region
where you run the pipeline.
For more information and a step-by-step tutorial about using the
**Create image pipeline** console wizard with default
values where provided, see [Tutorial: Create an image
pipeline with output AMI from the Image Builder console wizard](start-build-image-pipeline.md "start-build-image-pipeline.md").

###### Contents

- [Create an AMI image
  pipeline from the AWS CLI](cli-create-image-pipeline.md "cli-create-image-pipeline.md")
- [Update AMI image pipelines from the console](update-image-pipeline-console.md "update-image-pipeline-console.md")
- [Update AMI image pipelines from the AWS CLI](cli-update-image-pipeline.md "cli-update-image-pipeline.md")
