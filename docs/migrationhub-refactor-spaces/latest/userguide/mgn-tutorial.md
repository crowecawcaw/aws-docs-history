

AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform).

# Tutorial: Using Refactor Spaces with AWS Application Migration Service
<a name="mgn-tutorial"></a>

This tutorial shows how to automatically create a refactor environment and route traffic to your application after migrating an application using AWS Application Migration Service (AWS MGN), so that you can continue modernizing as soon as you've migrated an application. The AWS Migration Hub Refactor Spaces (Refactor Spaces) post-launch action in AWS MGN creates a Refactor Spaces environment, an application, a service, and a default route. 

You can use a Refactor Spaces environment to quickly launch new features in AWS Lambda (Lambda), Amazon Elastic Container Service (Amazon ECS), or Amazon Elastic Kubernetes Service (Amazon EKS), or you can safely and incrementally move traffic to new services without modifying the existing application. For more information, see [What is AWS Migration Hub Refactor Spaces?](what-is-mhub-refactor-spaces.md) and [Enable Refactor Spaces](https://docs.aws.amazon.com/mgn/latest/ug/predefined-post-launch-actions.html#predefined-enable-refactor-space) in the *AWS MGN User Guide*.

For a quick overview of a complete migration workflow, see [Migration workflow](https://docs.aws.amazon.com/mgn/latest/ug/migration-workflow-gs.html) in the *AWS MGN User Guide*.

## Prerequisites
<a name="prerequisites"></a>

To do this tutorial, you need the following prerequisites:
+ An AWS account. If you don't have an AWS account, see [Getting started: Are you a first-time AWS user?](https://docs.aws.amazon.com/accounts/latest/reference/welcome-first-time-user.html).
+ Familiarity with AWS MGN. For an introduction, see [What Is AWS Application Migration Service?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html).
+ Familiarity with Refactor Spaces. For an introduction, see [What is AWS Migration Hub Refactor Spaces?](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/what-is-mhub-refactor-spaces.html) 

## Step 1: Set up AWS MGN
<a name="init-mgn-config-template"></a>

To use AWS MGN, you must first set it up in the AWS Region in which you plan to use it.

1. Open the AWS MGN console at [https://console.aws.amazon.com/mgn/home](https://console.aws.amazon.com/mgn/home).

1. Choose the Region that you want to work in.

1. Choose the **Get started** button that appears in the following image.  
![AWS Transform MGN page with "Start migrating" box and "Get started" button.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/mgn-get-started.png)

1. If this is your first time using AWS MGN in the Region you chose, you will see the following screen. Choose the **Set up service** button.  
![Service initialization page with View roles, Cancel, and Set up service buttons.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/set-up-mgn.png)

For more information, see [Initializing AWS MGN via the console](https://docs.aws.amazon.com/mgn/latest/ug/mandatory-setup.html).

## Step 2: Create an IAM role
<a name="create-iam-role"></a>

In this step you create a service role that the automation script of the MGN post-launch action will need to assume.

1. Open the IAM console at [https://console.aws.amazon.com/iam](https://console.aws.amazon.com/iam).

1. In the left navigation pane, choose **Roles**.

1. Choose **Create role**.

1. Under **Use cases for other AWS services:**, choose **Systems Manager** from the dropdown list.

1. Below the dropdown list, choose the ****Systems Manager** option.**

1. Choose **Next**.

1. In the search field, enter **Refactor**, and then press the **Enter** key.

1. Choose the following two policies: **AWSMigrationHubRefactorSpacesFullAccess** and **AWSMigrationHubRefactorSpaces-SSMAutomationPolicy**.

1. Choose **Next**.

1. For the role name, enter **RefactorSpacesSSMTutorialRole**.

1. Choose **Create role**.

1. When you see a success message like the one in the following image, choose **View role**.  
![IAM Roles page showing success message for role creation with "View role" option.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/role-created.png)

1. Choose **Add permissions**, then choose **Create inline policy**.

1. Choose the **JSON** button that appears in the following image.  
![Policy editor interface showing service selection and JSON toggle button highlighted.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/json-policy.png)

1. Replace the JSON in the policy editor with the first block of JSON in the following section: [Extra required permissions for Refactor Spaces](https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess).

1. Choose **Next**.

1. For the policy name, enter **RefactorSpacesExtraRequiredPermissions**.

1. Choose **Create policy**.

1. Copy the ARN that you see in the summary section of the role and save it because you need it to configure the post-launch action.

## Step 3: Configure the launch and post-launch templates
<a name="enable-ssm-integ"></a>

In this step, you enable post-launch actions (if you haven't used them in this Region before) and you configure the Refactor Spaces post-launch action.

**Configure the launch template to transfer server tags**

1. In the left navigation pane, choose **Launch template**.

1. Choose **Edit**.

1. Turn on **Transfer server tags**.

1. Choose **Save template**.

Now you must enable post-launch actions. If you've already enabled post-launch actions in this Region, skip the following procedure and go to the procedure for configuring the Refactor Spaces post-launch action.

**Enable post-launch actions**

1. In the left navigation pane, choose **Post-launch template**.

1. Choose the edit button that appears in the following image.  
![Post-launch template interface showing settings for configuring actions after server launch in AWS.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/enable-post-launch-actions.png)

1. Turn on **Install the Systems Manager agent and allow executing actions on launched servers**, as shown in the following image.  
![Post-launch actions section with toggle enabled for installing Systems Manager agent.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/install-ssm.png)

1. Choose **Save template**.

**Configure the Refactor Spaces post-launch action**

1. In the left navigation pane, choose **Post-launch template**.

1. In the **Actions** section, choose the action with the title **Enable Refactor Spaces**.

1. In the **Actions** section, choose the **Edit** button that appears in the following image.  
![Actions section with Edit button highlighted among other options.](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/images/edit-post-launch-actions.png)

1. Specify the following values in the form:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/mgn-tutorial.html)

1. Choose **Save action**.

## Step 4: Create an EC2 instance to use as a source server
<a name="create-ec2-instance"></a>

1. Open the EC2 console at [https://console.aws.amazon.com/ec2](https://console.aws.amazon.com/ec2).

1. Choose **Launch instance**.

1. For the name field, enter **RefactorSpacesSSMTutorialEC2Instance**.

1. Under **Amazon Machine Image (AMI)**, choose **Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type**.

1. Under the **Key pair (login)**, choose an existing key pair or choose **Create new key pair**. You need a key pair to connect to the EC2 instance. For information on how to connect to an EC2 instance, see [Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect.html) in the Amazon Elastic Compute Cloud User Guide for Linux Instances.

1. Create an IAM role and attach to it the [AWSApplicationMigrationAgentInstallationPolicy](https://docs.aws.amazon.com/mgn/latest/ug/security-iam-awsmanpol-AWSApplicationMigrationAgentInstallationPolicy.html) policy.

## Step 5: Add a source server and launch a test instance
<a name="add-source-server-launch-test-instance"></a>

1. Open the AWS MGN console at [https://console.aws.amazon.com/mgn/home](https://console.aws.amazon.com/mgn/home).

1. Follow the instructions in [Linux](https://docs.aws.amazon.com/mgn/latest/ug/linux-agent.html) in the AWS MGN User Guide to install the AWS Replication Agent on the EC2 instance that you created in the previous section.

1. In the left navigation pane of the MGN console, choose **Source servers**.

1. At the bottom of the screen, under **Source server name**, choose the name of the source server that you created for this tutorial. This action takes you to the source server's details page.

1. Choose the **Tags** tab.

1. Choose **Manage tags**, and then choose **Add new tag**.

1. For the key, enter **refactor-spaces:ssm:optin**. For the value, enter **true**.

1. Choose **Save**.

1. While still on the source server details page, choose **Test and cutover**, then choose **Launch test instances**.

1.  After the test instance is launched, navigate to the **Refactor Spaces Environments** page. Choose **RefactorSpacesSSMTutorialEnvironment**, and then choose the application named **RefactorSpacesSSMTutorialApplication**.

1. On the application's page, the Proxy table contains the proxy URL. This URL becomes the migrated application's new front door and traffic is now routed to the migrated Amazon EC2 instance. Services and routes can be added to move traffic away from the migrated application to new microservices. 

    **Note:** When migrating, you can hide the proxy's URL using Amazon API Gateway custom domains before cutting over to your new front door. 

You have launched a test instance and a Refactor Spaces environment that includes the new application proxy URL, a default route that points to your migrated application, and the infrastructure necessary to incrementally route traffic to new services.

For more information on launching test instances, see [Launching a test instance](https://docs.aws.amazon.com/mgn/latest/ug/launching-test-gs.html) in the AWS MGN User Guide.

After testing, when you are ready for cutover, see [Launching a cutover instance](https://docs.aws.amazon.com/mgn/latest/ug/launch-cutover-gs.html) in the AWS MGN User Guide.

## Related resources
<a name="related-resources"></a>
+ For information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the AWS Identity and Access Management User Guide.
+ For more information about EC2 instances, see [What is Amazon EC2?](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) in the Amazon Elastic Compute Cloud User Guide for Linux Instances.