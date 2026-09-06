

# Module 5: Finalize Pipeline and Test
<a name="module-five"></a>


|  |  | 
| --- |--- |
| **AWS experience** | Beginner  | 
| **Time to complete** | 5 minutes  | 
| **Services used** | [AWS CodePipeline](https://aws.amazon.com/codepipeline/)  | 

## Overview
<a name="overview"></a>

In this module, you will use [AWS CodePipeline](https://aws.amazon.com/codepipeline/) to add a review stage to your continuous delivery pipeline. 

As part of this process, you can add an approval action to a stage at the point where you want the pipeline execution to stop so someone can manually approve or reject the action. Manual approvals are useful to have someone else review a change before deployment. If the action is approved, the pipeline execution resumes. If the action is rejected—or if no one approves or rejects the action within seven days—the result is the same as the action failing, and the pipeline execution does not continue. 

## What you will accomplish
<a name="what-you-will-accomplish"></a>

In this module, you will: 
+ Add a review stage to your pipeline 
+ Manually approve a change before it is deployed 

## Key concepts
<a name="key-concepts"></a>

**Approval action—**Type of pipeline action that stops the pipeline execution until someone approves or rejects it. 

**Pipeline execution—**Set of changes, such as a merged commit, released by a pipeline. Pipeline executions traverse the pipeline stages in order. Each pipeline stage can only process one execution at a time. To do this, a stage is locked while it processes an execution. 

**Failed execution—**If an execution fails, it stops and does not completely traverse the pipeline. The pipeline status changes to **Failed** and the stage that was processing the execution is unlocked. A failed execution can be retried or replaced by a more recent execution. 

## Implementation
<a name="implementation"></a>

### Step 1: Create review stage in pipeline
<a name="create-review-stage-in-pipeline"></a>

1. Open the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/pipelines). 

1. You should see the pipeline we created in Module 4, which was called **Pipeline-DevOpsGettingStarted.** Select this pipeline. 

1. Choose the white **Edit** button near the top of the page. 

1. Choose the white** Add stage** button between the **Build** and **Deploy** stages. 

1. In the **Stage name** field, enter **Review.** 

1. Choose the orange **Add stage** button. 

1. In the **Review** stage, choose the white **Add action group** button. 

1. Under **Action name,** enter **Manual\_Review.** 

1. From the **Action provider** dropdown, select **Manual approval.** 

1. Confirm that the optional fields have been left blank. 

1. Choose the orange **Done** button. 

1. Choose the orange **Save** button at the top of the page. 

1. Choose the orange **Save** button to confirm the changes. You will now see your pipeline with four stages: **Source, Build, Review,** and **Deploy.** 

### Step 2: Push a new commit to your repo
<a name="push-a-new-commit-to-your-repo"></a>

1. In your favorite code editor, open the **app.js** file from Module 1. 

1. Change the message in Line 5. 

1. Save the file. 

1. Open your preferred Git client. 

1. Navigate to the folder created in Module 1. 

1. Commit the change with the following commands: 

   ```
   git add app.js
   git commit -m "Full pipeline test"
   ```

1. Push the local changes to the remote repo hosted on GitHub with the following command: 

   ```
   git push
   ```

### Step 3: Monitor the pipeline and manually approve the change
<a name="monitor-the-pipeline-and-manually-approve-the-change"></a>

1. Navigate to the [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/pipelines). 

1. Select the pipeline named **Pipeline-DevOpsGettingStarted.** You should see the **Source** and **Build** stages switch from blue to green. 

1. When the **Review** stage switches to blue, choose the white **Review** button. 

1. Write an approval comment in the **Comments** textbox. 

1. Choose the orange **Approve** button. 

1. Wait for the **Review** and **Deploy** stages to switch to green. 

1. Select the **AWS Elastic Beanstalk** link in the **Deploy** stage. A new tab listing your Elastic Beanstalk environments will open. 

1. Select the URL in the **Devopsgettingstarted-env** row. You should see a webpage with a white background and the text you had in your most recent GitHub commit. 

## Congratulations\!
<a name="congratulations"></a>

You successfully built a continuous delivery pipeline on AWS\! As a great next step, dive deeper into specific AWS technologies and take your application to the next level. 

## Application architecture
<a name="application-architecture"></a>

With all modules now completed, here is the architecture of what you built: 

We have used AWS CodePipeline to add a review stage with manual approval to our continuous delivery pipeline. Now, our code changes will have to be reviewed and approved before they are deployed to AWS Elastic Beanstalk. 

![A diagram showing a CI/CD deployment workflow using AWS CodePipeline. The flow starts with users pushing source code to a Git repository, which triggers the CodePipeline in AWS Cloud. The pipeline includes steps for source (Git repository), build (AWS CodeBuild), manual approval (review), and deployment to AWS Elastic Beanstalk.](http://docs.aws.amazon.com/hands-on/latest/create-continuous-delivery-pipeline/images/diagram-deployment-workflow-using-acplong.png)


## Clean up resources
<a name="clean-up-resources"></a>

### (Optional) Delete AWS Elastic Beanstalk application
<a name="optional-delete-aws-elastic-beanstalk-application"></a>

1. In a new browser window, open the [AWS Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk/home#/applications). 

1. In the left navigation menu, click on **Applications.** You should see the **DevOpsGettingStarted** application listed under **All applications**. 

1. Select the radio button next to **DevOpsGettingStarted.** 

1. Click the **Actions** at the top of the page. 

1. In the dropdown menu, select **Delete application**. 

1. Type **DevOpsGettingStarted** in the text box to confirm deletion. 

1. Click **Delete**. 

### (Optional) Delete pipeline in AWS CodePipeline
<a name="optional-delete-pipeline-in-aws-codepipeline"></a>

1. In a new browser window, open the [AWS CodePipeline Console](https://console.aws.amazon.com/codesuite/codepipeline/pipelines). 

1. Select the **radio button** next to **Pipeline-DevOpsGettingStarted.** 

1. Click **Delete pipeline** at the top of the page. 

1. Type **delete** in the text box to confirm deletion. 

1. Click **Delete**. 

### (Optional) Delete pipeline resources from Amazon S3 bucket
<a name="optional-delete-pipeline-resources-from-amazon-s3-bucket"></a>

1. In a new browser window, open the [Amazon S3 Console](https://s3.console.aws.amazon.com/s3/home). 

1. You should see a bucket named **codepipeline-us-west-2** followed by your AWS account number. Click on this bucket. Inside this bucket, you should see a folder named **Pipeline-DevOpsGettingStarted**. 

1. Select the checkbox next to the **Pipeline-DevOpsGettingStarted** folder. 

1. Click **Actions** from the dropdown menu. 

1. In the dropdown menu, select **Delete**. 

1. Click **Delete**. 

### (Optional) Delete build project in AWS CodeBuild
<a name="optional-delete-build-project-in-aws-codebuild"></a>

1. In a new browser window, open the [AWS CodeBuild Console](https://console.aws.amazon.com/codesuite/codebuild/projects). 

1. In the left navigation, click **Build projects** under **Build**. You should see the **Build-DevOpsGettingStarted** build project listed under **Build project**. 

1. Select the radio button next to **Build-DevOpsGettingStarted.** 

1. Click **Delete build project** at the top of the page. 

1. Type **delete** in the text box to confirm deletion. 

1. Click **Delete**. 