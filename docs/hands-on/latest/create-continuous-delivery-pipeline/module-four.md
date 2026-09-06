

# Module 4: Create Delivery Pipeline
<a name="module-four"></a>


|  |  | 
| --- |--- |
| **Time to complete** | 10 minutes  | 
| **Services used** | [AWS CodePipeline](https://aws.amazon.com/codepipeline/?e=gs2020&p=cicd-four)  | 

## Overview
<a name="overview"></a>

In this module, you will use AWS CodePipeline to set up a continuous delivery pipeline with source, build, and deploy stages. The pipeline will detect changes in the code stored in your GitHub repository, build the source code using AWS CodeBuild, and then deploy your application to AWS Elastic Beanstalk. 

## What you will accomplish
<a name="what-you-will-accomplish"></a>

In this module, you will: 
+ Set up a continuous delivery pipeline on AWS CodePipeline 
+ Configure a source stage using your GitHub repo 
+ Configure a build stage using AWS CodeBuild 
+ Configure a deploy stage using your AWS Elastic Beanstalk application 
+ Deploy the application hosted on GitHub to Elastic Beanstalk through a pipeline 

## Key concepts
<a name="key-concepts"></a>

**Continuous delivery**—Software development practice that allows developers to release software more quickly by automating the build, test, and deploy processes. 

**Pipeline**—Workflow model that describes how software changes go through the release process. Each pipeline is made up of a series of stages. 

**Stage**—Logical division of a pipeline, where actions are performed. A stage might be a build stage, where the source code is built and tests are run. It can also be a deployment stage, where code is deployed to runtime environments. 

**Action**—Set of tasks performed in a stage of the pipeline. For example, a source action can start a pipeline when source code is updated, and a deploy action can deploy code to a compute service like AWS Elastic Beanstalk. 

## Implementation
<a name="implementation"></a>

### Step 1: Create a new pipeline
<a name="create-a-new-pipeline"></a>

1. In a browser window, open the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/start). 

1. Choose the orange **Create pipeline** button. A new screen will open up so you can set up the pipeline. 

1. In the **Pipeline name** field, enter **Pipeline-DevOpsGettingStarted.** 

1. Confirm that **New service role** is selected. 

1. Choose the orange **Next** button. 

### Step 2: Configure the source stage
<a name="configure-the-source-stage"></a>

1. Select **GitHub version 1** from the **Source provider** dropdown menu. 

1. Choose the white **Connect to GitHub** button. A new browser tab will open asking you to give AWS CodePipeline access to your GitHub repo. 

1. Choose the green **Authorize aws-codesuite** button. Next, you will see a green box with the message **You have successfully configured the action with the provider.** 

1. From the **Repository** dropdown, select the repo you created in Module 1. 

1. Select **main** from the **branch** dropdown menu. 

1. Confirm that **GitHub webhooks** is selected. 

1. Choose the orange **Next** button. 

### Step 3: Configure the build stage
<a name="configure-the-build-stage"></a>

1. From the **Build provider** dropdown menu, select **AWS CodeBuild.** 

1. Under **Region** confirm that the **US West (Oregon)** Region is selected. 

1. Select **Build-DevOpsGettingStarted** under **Project name.** 

1. Choose the orange **Next** button. 

### Step 4: Configure the deploy stage
<a name="configure-the-deploy-stage"></a>

1. Select **AWS Elastic Beanstalk** from the **Deploy provider** dropdown menu. 

1. Under **Region,** confirm that the **US West (Oregon)** Region is selected. 

1. Select the field under **Application name** and confirm you can see the app **DevOpsGettingStarted** created in Module 2. 

1. Select **DevOpsGettingStarted-env** from the **Environment name** textbox. 

1. Choose the orange **Next** button. You will now see a page where you can review the pipeline configuration. 

1. Choose the orange **Create pipeline** button. 

### Step 5: Watch first pipeline execution
<a name="watch-first-pipeline-execution"></a>

While watching the pipeline execution, you will see a page with a green bar at the top. This page shows all the steps defined for the pipeline and, after a few minutes, each will change from blue to green. 

1. Once the **Deploy** stage has switched to green and it says **Succeeded,** choose **AWS Elastic Beanstalk.** A new tab listing your AWS Elastic Beanstalk environments will open. 

1. Select the URL in the **Devopsgettingstarted-env** row. You should see a webpage with a white background and the text you included in your GitHub commit in Module 1. 

#### Application architecture
<a name="application-architecture"></a>

Here's what our architecture looks like now: 

We have created a continuous delivery pipeline on AWS CodePipeline with three stages: source, build, and deploy. The source code from the GitHub repo created in [Module 1: Set Up Git Repo](module-one.md) is part of the source stage. That source code is then built by AWS CodeBuild in the build stage. Finally, the built code is deployed to the AWS Elastic Beanstalk environment created in [Module 3: Create Build Project](module-three.md). 

![Diagram illustrating a DevOps pipeline using a Git repository as the source, AWS CodePipeline for orchestration, AWS CodeBuild for building the application, and AWS Elastic Beanstalk for deployment.](http://docs.aws.amazon.com/hands-on/latest/create-continuous-delivery-pipeline/images/devops-git-codebuild-elastic-beanstalk.png)
