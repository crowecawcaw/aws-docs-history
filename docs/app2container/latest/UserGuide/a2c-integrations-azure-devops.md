AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Set up CI/CD pipelines with

Microsoft Azure DevOps

Azure DevOps is a continuous delivery platform, orchestrator, and cloud provider from Microsoft.
App2Container integrates with Azure DevOps Services to automate the build and deployment process that
updates your application container images in Amazon ECR. For more information about Azure DevOps,
see [What
is Azure DevOps?](https://docs.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops "https://docs.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops") in the Microsoft documentation.

###### Contents

- [Prerequisites](#integrations-azure-devops-prereq "#integrations-azure-devops-prereq")
- [Azure DevOps integration for App2Container
  workflow](#integrations-azure-devops-workflow "#integrations-azure-devops-workflow")
  These directions cover IAM users. For information that covers IAM Roles Anywhere, see
  [External pipeline deployments to AWS using IAM Roles Anywhere](https://aws.amazon.com/blogs/security/enable-external-pipeline-deployments-to-aws-cloud-by-using-iam-roles-anywhere/ "https://aws.amazon.com/blogs/security/enable-external-pipeline-deployments-to-aws-cloud-by-using-iam-roles-anywhere/").

## Prerequisites

To configure Azure DevOps pipeline integration for your application container from App2Container,
your application must meet the following criteria.

- You must have a Microsoft Azure account with the following organization and project
  structure:
  - An organization that Azure DevOps services can use for your pipeline. To learn more about
    how to set up an organization for your Microsoft Azure account, see the
    [Create an organization](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/create-organization?view=azure-devops "https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/create-organization?view=azure-devops") page on the
    _Azure DevOps Services_ documentation website.
  - A project that Azure DevOps services can use for your pipeline. The project establishes a
    repository where your pipeline stores artifacts for your application.
    For more information, see [Create a project in Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops "https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops") on the
    _Azure DevOps Services_ documentation website.
  - An agent pool that contains Microsoft-hosted agents. Microsoft provides a predefined
    agent pool called **Azure Pipelines** that
    contains Microsoft-hosted agents. When you create your agent pool,
    choose the **Azure Pipelines** default agent pool. For
    more information, see [Create and manage agent pools](https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues?view=azure-devops "https://docs.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues?view=azure-devops") on the
    _Azure DevOps Services_ documentation website.

- To access AWS resources for your application from your Azure DevOps pipeline,
  install the AWS Toolkit for Azure DevOps extension into your Azure DevOps account .
  - Search for `AWS toolkit for Azure DevOps` in the [Azure DevOps
    section of the Visual Studio Marketplace](https://marketplace.visualstudio.com/azuredevops "https://marketplace.visualstudio.com/azuredevops").
  - Choose the **AWS toolkit for Azure DevOps** extension
    from the results.
  - Choose **Get it free** If prompted, sign in to your
    Azure DevOps account.
  - To install the extension into your Azure DevOps account, choose
    **Install**.

- Azure DevOps pipelines need permission to perform pipeline actions that access or update
  AWS resources. To grant access for Azure DevOps, attach or embed the policy
  resources and actions shown in the **IAM policy for Azure DevOps**
  example in the [IAM policy examples](iam-a2c.md#example-iam-policies "iam-a2c.md#example-iam-policies"). For more information on how
  to set up your IAM resources for App2Container, see [Create IAM resources for general use](iam-a2c.md#iam-user-containerize "iam-a2c.md#iam-user-containerize").
- After you've installed the AWS Toolkit for Azure DevOps and set up the IAM user and policy that Azure DevOps uses
  to interact with AWS services, you can set up an AWS service connection
  under your Azure project settings, as follows:

      1. Sign in to your Azure DevOps account organization, and select your
       project.
      2. In the lower left of your browser window, choose **Project settings**.
       This opens the **Project Settings** menu.
      3. In the **Pipelines** section of the menu, choose **Service
       connections**.
      4. Choose **New service connection**. This displays a
       list of services that you can connect to.
      5. To open the **New AWS service connection** form, choose
       **AWS** from the list, and then choose **Next**.
       If there is a long list of service connections, you might need to scroll down.
      6. Enter the following information in the form:



      ###### Required



      	+ **Access Key ID** – The access key ID for the IAM user that
      	 Azure DevOps uses to access AWS services for pipeline
      	 actions.
      	+ **Secret Access Key** – The secret access key for the IAM
      	 user that Azure DevOps uses to access AWS services for pipeline
      	 actions.
      	+ **Service connection name** – The name
      	 of the service connection for your project
      	+ **Grant access permission to all pipelines**
      	 – Select this check box to ensure that all of your
      	 pipelines have permission to access AWS services.
      You can fill in one or more of the optional fields, if needed,
       depending on how you set up your security in IAM.
      7. Choose **Save** to save your settings and close the
       form.

  For more information, see [Manage service connections](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops "https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops") on the _Azure DevOps Services_ documentation website.

- When App2Container runs Azure DevOps pipelines, it authenticates with a
  Microsoft Azure Personal Access Token (PAT). To learn more about how to create a PAT and save it as a
  secret in AWS Secrets Manager, see [Create secrets for Microsoft Azure DevOps
  pipelines](manage-secrets.md#azure-devops-secrets "manage-secrets.md#azure-devops-secrets").

## Azure DevOps integration for App2Container

workflow

Applications follow all of the standard App2Container workflow steps through deployment.
Azure DevOps integration happens in the pipeline step. To set up integration with Microsoft Azure DevOps
pipelines, to refresh components for your application container, configure the
`pipeline.json` file as follows.

Before you run the **generate pipeline** command, review the
`pipeline.json` file that the **generate
app-deployment** command created. Configure the parameters for your
Azure DevOps pipeline as follows:

- Set the flags to activate Azure DevOps deployment.
  Configure exactly one source repository, and one type of pipeline. In each section, set one
  Boolean value `enabled` flag to `true`, and all others to `false`.
  - sourceInfo
    - CodeCommit – enabled: **false**
    - ExistingGitRepo – enabled: **false**
    - AzureRepo – enabled: **true**

  - pipelineInfo
    - CodePipeline – enabled: **false**
    - Jenkins – enabled: **false**
    - AzureDevOps – enabled: **true**

- In the `AzureRepo` object of the `sourceInfo` section, set the
  following additional parameters, or leave the default values that App2Container
  creates:
  - repositoryName (string, required) –
    The name of the Azure Repos Git repository that you want to use
    or create.
  - branch (string, required) – The name
    of the code branch in the Azure Repos Git repository where App2Container commits
    pipeline resources.

- In the `Azure DevOps` object of the `pipelineInfo` section, set the
  following additional parameters, or leave the default values that App2Container
  creates:
  - organizationName (string, required) –
    The name of the organization that you set up under your Microsoft Azure account
    for Azure DevOps.
  - projectName (string, required) –
    The name of the project that you set up under your Microsoft Azure account for
    Azure DevOps.
  - serviceCredName (string, required) – The
    name of the service credentials that Azure DevOps uses to connect to AWS.
  - agentPoolName (string, required) – The
    name of the agent pool with the Microsoft-hosted agents that your pipeline uses to
    build and deploy updated container images for your application.
  - personalAccessTokenARN (string, required) – The
    ARN that identifies the Secrets Manager secret where you store your Microsoft Azure Personal Access Token (PAT).

### Validation

When you run the **generate pipeline** command, App2Container performs
the following validation to ensure the success of your pipeline deployment:

###### File validation

App2Container ensures that the Azure DevOps sections in the `pipeline.json`
file are complete, and that all required properties pass validation.

- Checks that `AzureRepo` is the only source repository that
  you have activated in the `sourceInfo` section of the
  `pipeline.json` file, and that this section
  contains all required properties.
- Checks that `AzureDevOps` is the only pipeline that you have
  activated in the `pipelineInfo` section of the
  `pipeline.json` file, and that this section
  contains all required properties.

###### Deployment validation

Before creating a pipeline, you must have deployed your containerized
application to run on Amazon ECS, Amazon EKS, or App Runner. App2Container verifies that your application
container is running in the environment you've configured before it proceeds.

###### Microsoft-hosted agent validation

App2Container verifies that all of the following prerequisites are installed on the
Microsoft-hosted agent:

- Git
- Docker engine
- AWS CLI
- `kubectl` (only for Amazon EKS container pipelines)

###### Azure account tools and settings

App2Container verifies that the Microsoft Azure account has the tools and settings it needs
to interact with AWS for Azure DevOps pipeline deployments, as follows:

- The AWS Toolkit for Microsoft Azure DevOps is installed in the Azure DevOps account
- The Azure DevOps service connection is configured for
  AWS
- The Microsoft Azure Agent Pool exists

### Output

The **generate pipeline** command generates the following artifacts for
Azure DevOps pipelines. If you don't use the `--deploy` option with the
**generate pipeline** command, you can edit the artifacts that App2Container
added to your Azure Repos Git repository to create your pipeline from the
Azure DevOps interface.

Amazon ECS

###### Scripts to install and validate prerequisites on the Microsoft-hosted agent

- `install-pre-req-aws.sh`
  – Installs AWS CLI on the Microsoft-hosted agent.
- `install-pre-req-docker.sh`
  – Installs the Docker engine on the Microsoft-hosted agent.
- `install-pre-req-git.sh`
  – Installs Git on the Microsoft-hosted agent.
- `pre-requisite-validation.sh`
  – Checks the Microsoft-hosted agent for prerequisites,
  and installs any that are missing.

###### Note

Scripts for Windows platforms use the .ps1 file extension.

###### Pipeline resources (in usage order)

- `pre-requisites.yml`
  – Sets up a pipeline stage that runs scripts to check
  the Microsoft-hosted agent and install any prerequisites that are missing.
- `pipeline.json` –
  Contains configurable settings for your pipeline..
- `image-build.yml` –
  Builds the application container image and uploads it to Amazon ECR.
- `beta-ecs-release.yaml`
  – Updates the Amazon ECS clusters for your beta
  environment, if you have defined that stage.
- `prod-ecs-release.yaml`
  – Updates the Amazon ECS clusters for your prod
  environment, if you have defined that stage.

###### Note

App2Container supports two stages for your pipelines: beta and prod. You must have
at least one stage defined, or you can have both.

Amazon EKS

###### Scripts to install and validate prerequisites on the

Microsoft-hosted agent

- `install-pre-req-aws.sh`
  – Installs AWS CLI on the Microsoft-hosted agent.
- `install-pre-req-docker.sh`
  – Installs the Docker engine on the Microsoft-hosted agent.
- `install-pre-req-git.sh`
  – Installs Git on the Microsoft-hosted agent.
- `install-pre-req-kubectl.sh`
  – Installs kubectl on the Microsoft-hosted
  agent.
- A
  `pre-requisite-validation.sh`
  file – Checks the Microsoft-hosted agent for prerequisites,
  and installs any that are missing.

###### Note

Scripts for Windows platforms use the .ps1 file extension.

###### Pipeline resources (in usage order)

- `pre-requisites.yml`
  – Sets up a pipeline stage that runs scripts to check
  the Microsoft-hosted agent and install any prerequisites that are missing.
- `pipeline.json` –
  Contains configurable settings for your pipeline.
- `image-build.yml` –
  Builds the application container image and uploads it to Amazon ECR.
- `beta-eks-release.yaml`
  – Updates the Amazon EKS clusters for your beta
  environment, if you have defined that stage.
- `prod-eks-release.yaml`
  – Updates the Amazon EKS clusters for your prod
  environment, if you have defined that stage.

###### Note

App2Container supports two stages for your pipelines: beta and prod. You must have
at least one stage defined, or you can have both.

App Runner

###### Scripts to install and validate prerequisites on the

Microsoft-hosted agent

- `install-pre-req-aws.sh`
  – Installs AWS CLI on the Microsoft-hosted agent.
- `install-pre-req-docker.sh`
  – Installs the Docker engine on the Microsoft-hosted agent.
- `install-pre-req-git.sh`
  – Installs Git on the Microsoft-hosted agent.
- `pre-requisite-validation.sh`
  – Checks the Microsoft-hosted agent for prerequisites,
  and installs any that are missing.

###### Note

Scripts for Windows platforms use the .ps1 file extension.

###### Pipeline resources (in usage order)

- `pre-requisites.yml` –
  Sets up a pipeline stage that runs scripts to check
  the Microsoft-hosted agent and install any prerequisites that are missing.
- `pipeline.json` –
  Contains configurable settings for your pipeline.
- `image-build.yml` –
  Builds the application container image and uploads it to Amazon ECR.

###### Note

If your Azure Repos Git repository doesn't already exist, App2Container creates
it.

If you run the **generate pipeline** command with the
`--deploy` option, App2Container creates the pipeline in Azure DevOps, and
starts the pipeline build.
