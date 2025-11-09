# Example development environment using Cloud9 and CodeCommit

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

This tutorial will guide you through setting up a example development environment for RFDK.

###### Warning

The development environment this creates is intended to serve as a starting point.
This development environment is not suitable for all organizations and security policies.
Please make sure you understand the implications of creating this environment.

Creating this example might result in charges to your AWS account. These include possible charges for services such as Amazon EC2 and CodeCommit. For more information, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") and [AWS CodeCommit Pricing](https://aws.amazon.com/codecommit/pricing/ "https://aws.amazon.com/codecommit/pricing/").

You will:

1. [Step 1: Create an AWS CodeCommit repository](#create-codecommit-repo "#create-codecommit-repo")
2. [Step 2: Create an AWS Cloud9 environment](#create-cloud9-env "#create-cloud9-env")
3. [Step 3: Encrypt Cloud9 EBS volume](#encrypt-cloud9-ebs "#encrypt-cloud9-ebs")
4. [Step 4: Increase storage capacity (optional)](#increase-storage-capacity "#increase-storage-capacity")
5. [Step 5: Configure Cloud9 for use with CodeCommit](#configure-cloud9 "#configure-cloud9")
6. [Step 6: Clone the AWS CodeCommit repository](#clone-codecommit-repo "#clone-codecommit-repo")

## Prerequisites

Before beginning this tutorial, you will need to:

- [Create an AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/ "https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/")
- [Create an IAM user](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") with [least-privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") that has the ability to:
  - **Use AWS CodeCommit** - The `AWSCodeCommitPowerUser`
    [AWS Managed Policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") can serve as a starting point, but it is recommended to use a minimally permissive IAM policy for production environments.
  - **List and resize EBS volumes** - This is granted with the `ec2:DescribeVolumes` and `ec2:ModifyVolume` actions. These can be granted in an inline policy statement.
  - **Deploy your CDK application** - Permissions vary depending on the code in the CDK application, and ultimately the CloudFormation resources you create/update/destroy. The RFDK makes use of CDK’s [grant](../../../cdk/latest/guide/permissions.md#permissions_grants "../../../cdk/latest/guide/permissions.md#permissions_grants") feature which effectively requires administrator access. The `AdministratorAccess` AWS Managed Policy can be used. The credentials for this IAM user should be secured and managed carefully. If these credentials are compromised, your AWS account could be mis-used without limitation.

- [Onboard to CDK](getting-started.md#onboarding-to-cdk "getting-started.md#onboarding-to-cdk")

## Step 1: Create an AWS CodeCommit repository

First, we need a highly-available and secure code repository for managing the source code of our RFDK application.
For this development environment, we will use an [AWS CodeCommit repository](../../../codecommit/latest/userguide/repositories.md "../../../codecommit/latest/userguide/repositories.md").

Follow the AWS CodeCommit’s documentation to [create an AWS CodeCommit repository](../../../codecommit/latest/userguide/how-to-create-repository.md "../../../codecommit/latest/userguide/how-to-create-repository.md").
Take note of the repository name chosen for the remainder of this guide.

## Step 2: Create an AWS Cloud9 environment

Next, we will create an [AWS Cloud9 environment](../../../cloud9/latest/user-guide/environments.md "../../../cloud9/latest/user-guide/environments.md") that we will use for development.
Specifically, we will create an **EC2** Cloud9 environment.
This type of Cloud9 environment means that Cloud9 will manage the lifecycle of the EC2 instance that hosts Cloud9.
The instance is automatically started when opening the Cloud9 IDE and stopped when the IDE is idle or unused to save costs.

Follow the AWS Cloud9 documentation for [Creating an environment](../../../cloud9/latest/user-guide/create-environment-main.md#create-environment-console "../../../cloud9/latest/user-guide/create-environment-main.md#create-environment-console").
Use the following values when creating the Cloud9 environment:

| Cloud 9 Environment Creation Values | Field                                                                                 | Value |
| ----------------------------------- | ------------------------------------------------------------------------------------- | ----- |
| **Name**                            | A desired name for your environment                                                   |
| **Description**                     | An optional description for your environment                                          |
| **Environment type**                | **Create a new no-ingress EC2 instance for environment (access via Systems Manager)** |
| **Instance type**                   | **t3.small**                                                                          |
| **Platform**                        | **Amazon Linux 2**                                                                    |
| **Cost-saving setting**             | **After four hours**                                                                  |

Once you’ve created the environment, the browser will navigate to the Cloud9 IDE for the newly created environment.
The Cloud9 IDE connects to the EC2 instance that hosts the environment and can be used to edit files and create terminal sessions.
Now is a good time to familiarize yourself with the Cloud9 IDE.

One important user interface element is the [**console**](../../../cloud9/latest/user-guide/tour-ide.md#tour-ide-console "../../../cloud9/latest/user-guide/tour-ide.md#tour-ide-console") at the bottom of the screen which will appear as a tab named **bash - "ip-...**.
This panel provides an interactive terminal session where you can run arbitrary shell commands.
You can toggle it being open or closed with the **F6** keyboard shortcut.

By default, Cloud9 EC2 environments come preconfigured with almost all of the required [Prerequisites](getting-started.md#prerequisites "getting-started.md#prerequisites") for working with RFDK, except for the version of NodeJS.
We recommend using the [LTS release]([https://nodejs.org/en/about/releases/](https://nodejs.org/en/about/releases/ "https://nodejs.org/en/about/releases/")) of NodeJS, which can be installed and configured with the following commands:

```
nvm install 14
echo "nvm use 14" >> ~/.bash_profile
```

## Step 3: Encrypt Cloud9 EBS volume

Follow the instructions to [encrypt the EBS volume used by the Cloud9 EC2 instance](../../../cloud9/latest/user-guide/move-environment.md#encrypting-volumes "../../../cloud9/latest/user-guide/move-environment.md#encrypting-volumes").

## Step 4: Increase storage capacity (optional)

###### Note

This step is only required if you plan to stage and build Deadline container images. See
[Deadline Container Images](work-with-rfdk.md#deadline-container-images "work-with-rfdk.md#deadline-container-images") for more details. If you do not have a specific need to build your own container images,
you can skip this step.

By default, AWS Cloud9 creates a 10GB EBS volume for the root file-system of the EC2 instance hosting the Cloud9 environment.
RFDK requires more storage for staging and building the Deadline container images.
Follow the instructions to [Resize an Amazon EBS volume used by an environment](../../../cloud9/latest/user-guide/move-environment.md#move-environment-resize "../../../cloud9/latest/user-guide/move-environment.md#move-environment-resize").
For RFDK development, we recommend a minimum size of **40GB**.

## Step 5: Configure Cloud9 for use with CodeCommit

In this step, we configure git on our Cloud9 environment to use the AWS CLI credential helper.
This uses Cloud9’s managed temporary credentials that are associated with the IAM user connected to the IDE.
To configure this, run the following commands:

```
git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
```

For more details, see [Step 2: Configure the AWS CLI Credential Helper On Your AWS Cloud9 EC2 Development Environment](../../../codecommit/latest/userguide/setting-up-ide-c9.md#setting-up-ide-c9-credentials "../../../codecommit/latest/userguide/setting-up-ide-c9.md#setting-up-ide-c9-credentials") in _Integrate AWS Cloud9 with AWS CodeCommit_ in the _AWS CodeCommit User Guide_.

## Step 6: Clone the AWS CodeCommit repository

In this step, we clone the CodeCommit repo created in [Step 1: Create an AWS CodeCommit repository](#create-codecommit-repo "#create-codecommit-repo") into your Cloud9 environment.

1. From the Cloud9 IDE, ensure the console panel is open. If not, press the **F6** key to toggle it.
2. Run the following commands substituting `my_repo_name` with the CodeCommit repository name created in step 1.

```
# Replace the value on the right-hand side with repository name from step 1
CC_REPO_NAME=`my_repo_name`

```

```
aws codecommit get-repository \
  --repository-name ${CC_REPO_NAME} \
  --query repositoryMetadata.cloneUrlHttp \
  --output text \
  | xargs git clone
```

## Next steps

Now that you have a example RFDK development environment, you are ready to [Build your first RFDK app](first-rfdk-app.md "first-rfdk-app.md").
You can also review the following additional resources:

- [Learn more about git](https://git-scm.com/book/en/v2 "https://git-scm.com/book/en/v2")
- [Read the AWS Cloud9 User Guide](../../../cloud9/latest/user-guide/welcome.md "../../../cloud9/latest/user-guide/welcome.md")
