# Deploying AWS AppConfig configurations using

CodePipeline

AWS AppConfig is an integrated deploy action for AWS CodePipeline (CodePipeline). CodePipeline is a fully managed
continuous delivery service that helps you automate your release pipelines for fast and
reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy
phases of your release process every time there is a code change, based on the release model
you define. For more information, see [What is
AWS CodePipeline?](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md")

The integration of AWS AppConfig with CodePipeline offers the following benefits:

- Customers who use CodePipeline to manage orchestration now have a lightweight means of
  deploying configuration changes to their applications without having to deploy their
  entire code base.
- Customers who want to use AWS AppConfig to manage configuration deployments but are limited
  because AWS AppConfig does not support their current code or configuration store, now have
  additional options. CodePipeline supports AWS CodeCommit, GitHub, and BitBucket (to name a
  few).

###### Note

AWS AppConfig integration with CodePipeline is only supported in AWS Regions where CodePipeline is [available](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## How integration works

You start by setting up and configuring CodePipeline. This includes adding your configuration
to a CodePipeline-supported code store. Next, you set up your AWS AppConfig environment by performing the
following tasks:

- [Create a namespace and a configuration profile](creating-feature-flags-and-configuration-data.md "creating-feature-flags-and-configuration-data.md")
- [Choose a
  predefined deployment strategy or create your own](appconfig-creating-deployment-strategy.md "appconfig-creating-deployment-strategy.md")

After you complete these tasks, you create a pipeline in CodePipeline that specifies AWS AppConfig as
the _deploy provider_. You can then make a change to your configuration
and upload it to your CodePipeline code store. Uploading the new configuration automatically starts
a new deployment in CodePipeline. After the deployment completes, you can verify your changes. For
information about creating a pipeline that specifies AWS AppConfig as the deploy provider, see
[Tutorial: Create a Pipeline That Uses
AWS AppConfig as a Deployment Provider](../../../codepipeline/latest/userguide/tutorials-AppConfig.md "../../../codepipeline/latest/userguide/tutorials-AppConfig.md") in the _AWS CodePipeline User Guide_.
