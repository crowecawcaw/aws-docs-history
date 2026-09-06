

# Amazon SageMaker Studio Classic
<a name="studio"></a>

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

Amazon SageMaker Studio Classic is a web-based integrated development environment (IDE) for machine learning (ML). Studio Classic lets you build, train, debug, deploy, and monitor your ML models. Studio Classic includes all of the tools you need to take your models from data preparation to experimentation to production with increased productivity. In a single visual interface, you can do the following tasks:
+ Write and run code in Jupyter notebooks
+ Prepare data for machine learning
+ Build and train ML models
+ Deploy the models and monitor the performance of their predictions
+ Track and debug ML experiments
+ Collaborate with other users in real time

For information on the onboarding steps for Studio Classic, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md).

For information about collaborating with other users in real time, see [Collaboration with shared spaces](domain-space.md).

For the AWS Regions supported by Studio Classic, see [Supported Regions and Quotas](regions-quotas.md).

## Amazon SageMaker Studio Classic maintenance phase plan
<a name="studio-deprecation"></a>

The following table gives information about the timeline for when Amazon SageMaker Studio Classic entered its extended maintenance phase.




| Date | Description | 
| --- | --- | 
| 12/31/2024 | Starting December 31st, Studio Classic reaches end of maintenance. At this point, Studio Classic will no longer receive updates and security fixes. All new domains will be created with Amazon SageMaker Studio as the default. | 
| 1/31/2025 | Starting January 31st, users will no longer be able to create new JupyterLab 3 notebooks in Studio Classic. Users will also not be able to restart or update existing notebooks. Users will be able to access existing Studio Classic applications from Studio only to delete or stop existing notebooks. | 

**Note**  
Your existing Studio Classic domain is not automatically migrated to Studio. For information about migrating, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md).

**Topics**
+ [Amazon SageMaker Studio Classic maintenance phase plan](#studio-deprecation)
+ [Amazon SageMaker Studio Classic Features](#studio-features)
+ [Amazon SageMaker Studio Classic UI Overview](studio-ui.md)
+ [Launch Amazon SageMaker Studio Classic](studio-launch.md)
+ [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md)
+ [Use the Amazon SageMaker Studio Classic Launcher](studio-launcher.md)
+ [Use Amazon SageMaker Studio Classic Notebooks](notebooks.md)
+ [Customize Amazon SageMaker Studio Classic](studio-customize.md)
+ [Perform Common Tasks in Amazon SageMaker Studio Classic](studio-tasks.md)
+ [Amazon SageMaker Studio Classic Pricing](studio-pricing.md)
+ [Troubleshooting Amazon SageMaker Studio Classic](studio-troubleshooting.md)

## Amazon SageMaker Studio Classic Features
<a name="studio-features"></a>

Studio Classic includes the following features:
+ [SageMaker Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html)
+ [SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/model-explainability.html)
+ [SageMaker Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
+ [SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio.html)
+ [SageMaker Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html)
+ [SageMaker Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-use-with-studio.html)
+ [SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
+ [Amazon SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-studio.html)
+ [SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
+ [SageMaker Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects.html)
+ [SageMaker Studio Classic Notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks.html)
+ [SageMaker Studio Universal Notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-notebooks-emr-cluster.html)