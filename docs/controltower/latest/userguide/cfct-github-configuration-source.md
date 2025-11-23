# Set up GitHub as the configuration source

This section tells you how to deploy Customizations for AWS Control Tower (CfCT) with GitHub as a source. The process has three main steps:

- Prepare a GitHub repository
- Create the GitHub code connection
- Deploy the CloudFormation stack

## Prepare a GitHub repository

Create a repository within your GitHub account, the default name used in the template is `custom-control-tower-configuration`. Consider making the target repository _private_. You'll define your customizations in a `yaml` file called `manifest.yaml` in the [deployment folder](https://github.com/aws-solutions/aws-control-tower-customizations/tree/main/deployment "https://github.com/aws-solutions/aws-control-tower-customizations/tree/main/deployment") of the CfCT repository.

The [_CfCT customization guide_](cfct-customizations-dev-guide.md "cfct-customizations-dev-guide.md") provides detailed guidance on creating a `manifest.yaml` to configure your customizations.

## Create the GitHub conection

From your **Developer Tools --Connections** instance for Github, perform the following steps:

1. Select **Create connection** and choose GitHub as the provider
2. Choose **Create a GitHub App connection**, and in the **Connection name** field, enter **GitHub CfCT**, or any name you choose
3. Select **Connect to GitHub** and then choose **Install a new app**
4. Select the GitHub User or Organization for your repository
5. Under **Repository access**, choose **Only select repositories**, then select the repository you created earlier, and **Save** your work.
6. Note the Code Connections ARN - you'll need it when deploying the CloudFormation stack.

## Deploy the CloudFormation stack

- Download the `custom-control-tower-initiation.template` file from the repository.
- Create a new CloudFormation stack, using the `custom-control-tower-initiation.template` file.
- Under **AWS CodePipeline Source**, choose **GitHub (via Code Connection)**.
- Under **GitHub Setup**, specify these fields:
  - For **ARN of the Code Connection**, provide the Code Connection ARN
  - for **GitHub User or Organization**, provide the name of the GitHub user or organization under which you created the repository
  - For **GitHub Repository Name**, enter the repository name (defaults to `custom-control-tower-configuration`)
  - For **GitHub Branch Name**, enter the branch name (defaults to `main`)
