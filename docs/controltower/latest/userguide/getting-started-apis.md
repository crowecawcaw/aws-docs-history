# Get started with AWS Control Tower using APIs

This getting started procedure is intended for AWS Control Tower administrators. This procedure requires some prerequisites and
includes two main steps.

In this procedure, you will use APIs from AWS Control Tower and other AWS services to configure and launch a landing zone.
These APIs allow you to create a AWS Control Tower environment programatically, either
[through the AWS CloudFormation console](lz-apis-cfn.md "lz-apis-cfn.md"), or through the AWS CLI.

Before you launch your AWS Control Tower landing zone, perform these prerequisite tasks:

- Determine the most appropriate home Region.
  For more information, see [Administrative tips for landing zone setup](tips-for-admin-setup.md "tips-for-admin-setup.md") .
- Review [Prerequisite: Automated pre-launch checks for
  your management account](getting-started-prereqs.md "getting-started-prereqs.md") to
  learn about the automated pre-launch checks that make sure your management
  account is ready for changes that establish your landing zone.

###### Topics

- [Expectations for landing zone configuration with APIs](getting-started-expectations-api.md "getting-started-expectations-api.md")
- [Step 1: Configure your landing zone](lz-api-prereques.md "lz-api-prereques.md")
- [Step 2: Launch your landing zone](lz-api-launch.md "lz-api-launch.md")
- [Identify your landing zone](lz-api-list.md "lz-api-list.md")
- [Update your landing zone](lz-api-update.md "lz-api-update.md")
- [Reset the landing zone to resolve drift](lz-api-reset.md "lz-api-reset.md")
- [View the details of your landing zone manifest file](lz-manifest-file.md "lz-manifest-file.md")
- [View the status of your landing zone operations](lz-api-examples-short.md "lz-api-examples-short.md")
- [Examples: Set up an AWS Control Tower landing zone with APIs only](walkthrough-api-setup.md "walkthrough-api-setup.md")
- [Landing zone schemas](landing-zone-schemas.md "landing-zone-schemas.md")
- [Launch a landing zone using AWS CloudFormation](lz-apis-cfn.md "lz-apis-cfn.md")
