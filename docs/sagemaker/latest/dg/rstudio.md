# RStudio on Amazon SageMaker AI

RStudio is an integrated development environment for R, with a console, syntax-highlighting
editor that supports direct code execution, and tools for plotting, history, debugging and
workspace management. Amazon SageMaker AI supports RStudio as a fully-managed integrated development
environment (IDE) integrated with Amazon SageMaker AI domain through Posit Workbench. RStudio allows
customers to create data science insights using an R environment. With RStudio integration, you
can launch an RStudio environment in the domain to run your RStudio workflows on SageMaker AI
resources. For more information about Posit Workbench, see the [Posit website](https://posit.co/products/enterprise/workbench/ "https://posit.co/products/enterprise/workbench/"). This page gives
information about important RStudio concepts.

SageMaker AI integrates RStudio through the creation of a RStudioServerPro app.

The following are supported by RStudio on SageMaker AI.

- R developers use the RStudio IDE interface with popular developer tools from the R
  ecosystem. Users can launch new RStudio sessions, write R code, install dependencies from
  RStudio Package Manager, and publish Shiny apps using RStudio Connect.
- R developers can quickly scale underlying compute resources to run large scale data
  processing and statistical analysis.
- Platform administrators can set up user identities, authorization, networking,
  storage, and security for their data science teams through AWS IAM Identity Center and AWS Identity and Access Management
  integration. This includes connection to private Amazon Virtual Private Cloud (Amazon VPC) resources and
  internet-free mode with AWS PrivateLink.
- Integration with AWS License Manager.
  For information on the onboarding steps to create a domain with RStudio enabled,
  see [Amazon SageMaker AI domain overview](gs-studio-onboard.md "gs-studio-onboard.md").

## Region availability

The following table gives information about the AWS Regions that RStudio on SageMaker AI is supported in.

| Region name               | Region         |
| ------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| US East (Ohio)            | us-east-2      |
| US East (N. Virginia)     | us-east-1      |
| US West (N. California)   | us-west-1      |
| US West (Oregon)          | us-west-2      |
| Asia Pacific (Mumbai)     | ap-south-1     |
| Asia Pacific (Seoul)      | ap-northeast-2 |
| Asia Pacific (Singapore)  | ap-southeast-1 |
| Asia Pacific (Sydney)     | ap-southeast-2 |
| Asia Pacific (Tokyo)      | ap-northeast-1 |
| Canada (Central)          | ca-central-1   |
| Europe (Frankfurt)        | eu-central-1   |
| Europe (Ireland)          | eu-west-1      |
| Europe (London)           | eu-west-2      |
| Europe (Paris)            | eu-west-3      |
| Europe (Stockholm)        | eu-north-1     |
| South America (São Paulo) | sa-east-1      | ## RStudio components <br>• _RStudioServerPro_: The RStudioServerPro app is a multiuser app that is a shared resource among all user profiles in the domain. Once an RStudio app is created in a domain, the admin can give permissions to users in the domain. <br>• _RStudio user_: RStudio users are users within the domain that are authorized to use the RStudio license. <br>• _RStudio admin_: An RStudio on Amazon SageMaker AI admin can access the RStudio administrative dashboard. RStudio on Amazon SageMaker AI admins differ from "stock" Posit Workbench admins because they do not have root access to the instance running the RStudioServerPro app and can't modify the RStudio configuration file. <br>• _RStudio Server_: The RStudio Server instance is responsible for serving the RStudio UI to all authorized Users. This instance is launched on an Amazon SageMaker AI instance. <br>• _RSession_: An RSession is a browser-based interface to the RStudio IDE running on an Amazon SageMaker AI instance. Users can create and interact with their RStudio projects through the RSession. <br>• _RSessionGateway_: The RSessionGateway app is used to support an RSession. <br>• _RStudio administrative dashboard_: This dashboard gives information on the RStudio users in the Amazon SageMaker AI domain and their sessions. This dashboard can only be accessed by users that have RStudio admin authorization. ## Differences from Posit Workbench RStudio on Amazon SageMaker AI has some significant differences from [Posit Workbench](https://posit.co/products/enterprise/workbench/ "https://posit.co/products/enterprise/workbench/"). <br>• When using RStudio on SageMaker AI, users don’t have access to the RStudio configuration files. Amazon SageMaker AI manages the configuration file and sets defaults. You can modify the RStudio Connect and RStudio Package Manager URLs when creating your RStudio-enabled Amazon SageMaker AI domain. <br>• Project sharing, realtime collaboration, and Job Launcher are not currently supported when using RStudio on Amazon SageMaker AI. <br>• When using RStudio on SageMaker AI, the RStudio IDE runs on Amazon SageMaker AI instances for on-demand containerized compute resources. <br>• RStudio on SageMaker AI only supports the RStudio IDE and does not support other IDEs supported by a Posit Workbench installation. <br>• RStudio on SageMaker AI only supports the RStudio version specified in [RStudio Versioning](rstudio-version.md "rstudio-version.md"). |
