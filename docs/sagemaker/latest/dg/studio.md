# Amazon SageMaker Studio Classic

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

Amazon SageMaker Studio Classic is a web-based integrated development environment (IDE) for machine learning
(ML). Studio Classic lets you build, train, debug, deploy, and monitor your ML models. Studio Classic
includes all of the tools you need to take your models from data preparation to experimentation
to production with increased productivity. In a single visual interface, you can do the
following tasks:

- Write and run code in Jupyter notebooks
- Prepare data for machine learning
- Build and train ML models
- Deploy the models and monitor the performance of their predictions
- Track and debug ML experiments
- Collaborate with other users in real time
  For information on the onboarding steps for Studio Classic, see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

For information about collaborating with other users in real time, see [Collaboration with shared spaces](domain-space.md "domain-space.md").

For the AWS Regions supported by Studio Classic, see
[Supported Regions and Quotas](regions-quotas.md "regions-quotas.md").

## Amazon SageMaker Studio Classic maintenance phase plan

The following table gives information about the timeline for when Amazon SageMaker Studio Classic entered its extended maintenance phase.

| Date       | Description                                                                                                                                                                                                                                                                                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 12/31/2024 | Starting December 31st, Studio Classic reaches end of maintenance. At this point, Studio Classic will no longer receive updates and security fixes. All new domains will be created with Amazon SageMaker Studio as the default.                                                                          |
| 1/31/2025  | Starting January 31st, users will no longer be able to create new JupyterLab 3 notebooks in Studio Classic. Users will also not be able to restart or update existing notebooks. Users will be able to access existing Studio Classic applications from Studio only to delete or stop existing notebooks. | ###### Note Your existing Studio Classic domain is not automatically migrated to Studio. For information about migrating, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md"). ###### Topics <br>• [Amazon SageMaker Studio Classic Features](#studio-features "#studio-features") <br>• [Amazon SageMaker Studio Classic UI Overview](studio-ui.md "studio-ui.md") <br>• [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md") <br>• [JupyterLab Versioning in Amazon SageMaker Studio Classic](studio-jl.md "studio-jl.md") <br>• [Use the Amazon SageMaker Studio Classic Launcher](studio-launcher.md "studio-launcher.md") <br>• [Use Amazon SageMaker Studio Classic Notebooks](notebooks.md "notebooks.md") <br>• [Customize Amazon SageMaker Studio Classic](studio-customize.md "studio-customize.md") <br>• [Perform Common Tasks in Amazon SageMaker Studio Classic](studio-tasks.md "studio-tasks.md") <br>• [Amazon SageMaker Studio Classic Pricing](studio-pricing.md "studio-pricing.md") <br>• [Troubleshooting Amazon SageMaker Studio Classic](studio-troubleshooting.md "studio-troubleshooting.md") ## Amazon SageMaker Studio Classic Features Studio Classic includes the following features: <br>• [SageMaker Autopilot](autopilot-automate-model-development.md "autopilot-automate-model-development.md") <br>• [SageMaker Clarify](model-explainability.md "model-explainability.md") <br>• [SageMaker Data Wrangler](data-wrangler.md "data-wrangler.md") <br>• [SageMaker Debugger](debugger-on-studio.md "debugger-on-studio.md") <br>• [SageMaker Experiments](experiments.md "experiments.md") <br>• [SageMaker Feature Store](feature-store-use-with-studio.md "feature-store-use-with-studio.md") <br>• [SageMaker JumpStart](studio-jumpstart.md "studio-jumpstart.md") <br>• [Amazon SageMaker Pipelines](pipelines-studio.md "pipelines-studio.md") <br>• [SageMaker Model Registry](model-registry.md "model-registry.md") <br>• [SageMaker Projects](sagemaker-projects.md "sagemaker-projects.md") <br>• [SageMaker Studio Classic Notebooks](notebooks.md "notebooks.md") <br>• [SageMaker Studio Universal Notebook](studio-notebooks-emr-cluster.md "studio-notebooks-emr-cluster.md") |
