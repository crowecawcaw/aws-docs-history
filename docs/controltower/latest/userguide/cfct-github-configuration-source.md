

# Set up GitHub as the configuration source
<a name="cfct-github-configuration-source"></a>

This section tells you how to deploy Customizations for AWS Control Tower (CfCT) with GitHub as a source. The process has three main steps:
+ Prepare a GitHub repository
+ Create the GitHub code connection
+ Deploy the CloudFormation stack

## Prepare a GitHub repository
<a name="prepare-github-cfct-source"></a>

 Create a repository within your GitHub account, the default name used in the template is `custom-control-tower-configuration`. Consider making the target repository *private*. You'll define your customizations in a `yaml` file called `manifest.yaml` in the [ deployment folder](https://github.com/aws-solutions/aws-control-tower-customizations/tree/main/deployment) of the CfCT repository.

The [*CfCT customization guide*](https://docs.aws.amazon.com/controltower/latest/userguide/cfct-customizations-dev-guide.html) provides detailed guidance on creating a `manifest.yaml` to configure your customizations. 

## Create the GitHub conection
<a name="create-github-cfct-connection"></a>

From your **Developer Tools --Connections** instance for Github, perform the following steps:

1. Select **Create connection** and choose GitHub as the provider

1. Choose **Create a GitHub App connection**, and in the **Connection name** field, enter **GitHub CfCT**, or any name you choose

1. Select **Connect to GitHub** and then choose **Install a new app**

1. Select the GitHub User or Organization for your repository

1. Under **Repository access**, choose **Only select repositories**, then select the repository you created earlier, and **Save** your work.

1. Note the Code Connections ARN - you'll need it when deploying the CloudFormation stack.

## Deploy the CloudFormation stack
<a name="deploy-github-cfct-stack"></a>
+ Download the `custom-control-tower-initiation.template` file from the repository.
+ Create a new CloudFormation stack, using the `custom-control-tower-initiation.template` file.
+ Under **AWS CodePipeline Source**, choose **GitHub (via Code Connection)**.
+ Under **GitHub Setup**, specify these fields: 
  + For **ARN of the Code Connection**, provide the Code Connection ARN
  + for **GitHub User or Organization**, provide the name of the GitHub user or organization under which you created the repository
  + For **GitHub Repository Name**, enter the repository name (defaults to `custom-control-tower-configuration`)
  + For **GitHub Branch Name**, enter the branch name (defaults to `main`)