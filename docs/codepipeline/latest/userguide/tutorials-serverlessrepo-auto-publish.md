# Tutorial: Create a pipeline that

publishes your serverless application to the AWS Serverless Application Repository

You can use AWS CodePipeline to continuously deliver your AWS SAM serverless application to the
AWS Serverless Application Repository.

###### Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be
used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source
action.) If the S3 artifact bucket is in a different account from the account for your
pipeline, make sure that the S3 artifact bucket is owned by AWS accounts that are safe
and will be dependable.

This tutorial shows how to create and configure a pipeline to build your serverless
application that is hosted in GitHub and publish it to the AWS Serverless Application Repository automatically. The pipeline
uses GitHub as the source provider and CodeBuild as the build provider. To publish your
serverless application to the AWS Serverless Application Repository, you deploy an [application](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~aws-serverless-codepipeline-serverlessrepo-publish "https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~aws-serverless-codepipeline-serverlessrepo-publish ") (from the AWS Serverless Application Repository) and associate the Lambda function created by that
application as an Invoke action provider in your pipeline. Then you can continuously deliver
application updates to the AWS Serverless Application Repository, without writing any code.

###### Important

Many of the actions you add to your pipeline in this procedure involve AWS resources that you need to create before you create the pipeline. AWS resources for your source actions must always be created in the same AWS Region
where you create your pipeline. For example, if you create your pipeline in the US East (Ohio)
Region, your CodeCommit repository must be in the US East (Ohio) Region.

You can add cross-region actions when you create your pipeline. AWS resources for cross-region actions must be in the same AWS Region where you plan to execute the action.
For more information, see [Add a cross-Region action in CodePipeline](actions-create-cross-region.md "actions-create-cross-region.md").

## Before you begin

In this tutorial, we assume the following.

- You are familiar with [AWS Serverless Application Model (AWS SAM)](../../../serverless-application-model/latest/developerguide.md "../../../serverless-application-model/latest/developerguide.md") and
  the [AWS Serverless Application Repository](../../../serverlessrepo/latest/devguide.md "../../../serverlessrepo/latest/devguide.md").
- You have a serverless application hosted in GitHub that you have published to
  the AWS Serverless Application Repository using the AWS SAM CLI. To publish an example application to the AWS Serverless Application Repository,
  see [Quick Start:
  Publishing Applications](../../../serverlessrepo/latest/devguide/serverlessrepo-quick-start.md "../../../serverlessrepo/latest/devguide/serverlessrepo-quick-start.md") in the _AWS Serverless Application Repository Developer Guide_.
  To publish your own application to the AWS Serverless Application Repository, see [Publishing Applications Using the AWS SAM CLI](../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md "../../../serverless-application-model/latest/developerguide/serverless-sam-template-publishing-applications.md") in the
  _AWS Serverless Application Model Developer Guide_.

## Step 1: Create a

buildspec.yml file

Create a `buildspec.yml` file with the following contents, and add it to
your serverless application's GitHub repository. Replace
`template.yml` with your application's AWS SAM template and
`bucketname` with the S3 bucket where your packaged
application is stored.

```
version: 0.2
phases:
  install:
    runtime-versions:
        python: 3.8
  build:
    commands:
      - sam package --template-file `template.yml` --s3-bucket `bucketname` --output-template-file packaged-template.yml
artifacts:
  files:
    - packaged-template.yml
```

## Step 2: Create and

configure your pipeline

Follow these steps to create your pipeline in the AWS Region where you want to
publish your serverless application.

1. Sign in to the AWS Management Console and open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. If necessary, switch to the AWS Region where you want to publish your
   serverless application.
3. On the **Welcome** page, **Getting started**
   page, or the **Pipelines** page, choose **Create
   pipeline**.
4. On the **Step 1: Choose creation option** page, under
   **Creation options**, choose the **Build custom
   pipeline** option. Choose **Next**.
5. Choose **Create pipeline**. On the **Step 2: Choose
   pipeline settings** page, in **Pipeline name**,
   enter the name for your pipeline.
6. In **Pipeline type**, choose **V2**. For
   more information, see [Pipeline types](pipeline-types.md "pipeline-types.md"). Choose **Next**.
7. In **Service role**, choose **New service
   role** to allow CodePipeline to create a service role in IAM.
8. Leave the settings under **Advanced settings** at their
   defaults, and then choose **Next**.
9. On the **Step 3: Add source stage** page, in **Source
   provider**, choose **GitHub**.
10. Under **Connection**, choose an existing connection or create
    a new one. To create or manage a connection for your GitHub source action, see
    [GitHub connections](connections-github.md "connections-github.md").
11. In **Repository**, choose your GitHub source
    repository.
12. In **Branch**, choose your GitHub branch.
13. Leave the remaining defaults for the source action. Choose
    **Next**.
14. On the **Step 4: Add build stage** page, add a build
    stage:
    1. In **Build provider**, choose
       **AWS CodeBuild**. For **Region**, use
       the pipeline Region.
    2. Choose **Create project**.
    3. In **Project name**, enter a name for this build
       project.
    4. In **Environment image**, choose **Managed
       image**. For **Operating system**, choose
       **Ubuntu**.
    5. For **Runtime** and **Runtime
       version**, choose the runtime and version required for your
       serverless application.
    6. For **Service role**, choose **New service
       role**.
    7. For **Build specifications**, choose **Use a
       buildspec file**.
    8. Choose **Continue to CodePipeline**. This opens the
       CodePipeline console and creates a CodeBuild project that uses the
       `buildspec.yml` in your repository for
       configuration. The build project uses a service role to manage
       AWS service permissions. This step might take a couple of
       minutes.
    9. Choose **Next**.

15. In **Step 5: Add test stage**, choose **Skip test
    stage**, and then accept the warning message by choosing
    **Skip** again.

Choose **Next**. 16. On the **Step 6: Add deploy stage** page, choose
**Skip deploy stage**, and then accept the warning message
by choosing **Skip** again. Choose
**Next**. 17. On **Step 7: Review**, choose **Create
pipeline**. You should see a diagram that shows the stages. 18. Grant the CodeBuild service role permission to access the S3 bucket where your
packaged application is stored.

    1. In the **Build** stage of your new pipeline, choose
     **CodeBuild**.
    2. Choose the **Build details** tab.
    3. In **Environment**, choose the CodeBuild service role to
     open the IAM console.
    4. Expand the selection for `CodeBuildBasePolicy`, and choose
     **Edit policy**.
    5. Choose **JSON**.
    6. Add a new policy statement with the following contents. The statement
     allows CodeBuild to put objects into the S3 bucket where your packaged
     application is stored. Replace `bucketname`
     with the name of your S3 bucket.



    ```
            {
                "Effect": "Allow",
                "Resource": [
                    "arn:aws:s3:::`bucketname`/*"
                ],
                "Action": [
                    "s3:PutObject"
                ]
            }
    ```
    7. Choose **Review policy**.
    8. Choose **Save changes**.

## Step 3: Deploy the publish

application

Follow these steps to deploy the application that contains the Lambda function that
performs the publish to the AWS Serverless Application Repository. This application is **aws-serverless-codepipeline-serverlessrepo-publish**.

###### Note

You must deploy the application to the same AWS Region as your pipeline.

1. Go to the [application](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~aws-serverless-codepipeline-serverlessrepo-publish "https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:077246666028:applications~aws-serverless-codepipeline-serverlessrepo-publish ") page, and choose **Deploy**.
2. Select **I acknowledge that this app creates custom IAM
   roles**.
3. Choose **Deploy**.
4. Choose **View CloudFormation Stack** to open the CloudFormation console.
5. Expand the **Resources** section. You see
   **ServerlessRepoPublish**, which is of the type
   **AWS::Lambda::Function**. Make a note of the physical ID
   of this resource for the next step. You use this physical ID when you create the
   new publish action in CodePipeline.

## Step 4: Create the publish

action

Follow these steps to create the publish action in your pipeline.

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. In the left navigation section, choose the pipeline that you want to
   edit.
3. Choose **Edit**.
4. After the last stage of your current pipeline, choose **+ Add
   stage**. In **Stage name** enter a name, such as
   `Publish`, and choose **Add
   stage**.
5. In the new stage, choose **+ Add action group**.
6. Enter an action name. From **Action provider**, in
   **Invoke**, choose **AWS Lambda**.
7. From **Input artifacts**, choose
   **BuildArtifact**.
8. From **Function name**, choose the physical ID of the Lambda
   function that you noted in the previous step.
9. Choose **Save** for the action.
10. Choose **Done** for the stage.
11. In the upper right, choose **Save**.
12. To verify your pipeline, make a change to your application in GitHub. For
    example, change the application's description in the `Metadata`
    section of your AWS SAM template file. Commit the change and push it to your
    GitHub branch. This triggers your pipeline to run. When the pipeline is
    complete, check that your application has been updated with your change in the
    [AWS Serverless Application Repository](https://console.aws.amazon.com/serverlessrepo/home "https://console.aws.amazon.com/serverlessrepo/home").
