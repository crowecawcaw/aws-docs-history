AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Tutorial: Setting up the Rocket Software (formerly Micro Focus) build for the

BankDemo sample application

AWS Mainframe Modernization provides you with the ability to set up builds and continuous integration/continuous delivery (CI/CD) pipelines for your migrated applications.
These builds and pipelines use AWS CodeBuild, AWS CodeCommit, and AWS CodePipeline to provide these capabilities.
CodeBuild is a fully managed build service that compiles your source code, runs unit tests, and produces artifacts that are ready to deploy.
CodeCommit is a version control service that enables you to privately store and manage Git reponsitories in the AWS Cloud.
CodePipeline is a continuous delivery service that enables you to model, visualize, and automate the steps required to release your software.

This tutorial demonstrates how to use AWS CodeBuild to compile the BankDemo sample application
source code from Amazon S3 and then export the compiled code back to Amazon S3.

AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs
tests, and produces software packages that are ready to deploy. With CodeBuild, you can use
prepackaged build environments, or you can create custom build environments that use your own
build tools. This demo scenario uses the second option. It consists of a CodeBuild build environment
that uses a pre-packaged Docker image.

###### Important

Before you start your mainframe modernization project, we recommend that you learn about
the [AWS
Migration Acceleration Program (MAP) for Mainframe](https://aws.amazon.com/migration-acceleration-program/mainframe/ "https://aws.amazon.com/migration-acceleration-program/mainframe/") or contact [AWS mainframe specialists](mailto: mainframe@amazon.com "mailto: mainframe@amazon.com") to learn about the
steps required to modernize a mainframe application.

###### Topics

- [Prerequisites](#tutorial-build-mf-prerequisites "#tutorial-build-mf-prerequisites")
- [Step 1: Share the build assets with AWS
  account](#tutorial-build-mf-assets "#tutorial-build-mf-assets")
- [Step 2: Create Amazon S3 buckets](#tutorial-build-mf-s3 "#tutorial-build-mf-s3")
- [Step 3: Create the build spec file](#tutorial-build-mf-spec "#tutorial-build-mf-spec")
- [Step 4: Upload the source files](#tutorial-build-mf-upload "#tutorial-build-mf-upload")
- [Step 5: Create IAM policies](#tutorial-build-mf-IAM-policy "#tutorial-build-mf-IAM-policy")
- [Step 6: Create an IAM role](#tutorial-build-mf-IAM-role "#tutorial-build-mf-IAM-role")
- [Step 7: Attach the IAM policies to the IAM
  role](#tutorial-build-mf-attach "#tutorial-build-mf-attach")
- [Step 8: Create the CodeBuild project](#tutorial-build-mf-create-project "#tutorial-build-mf-create-project")
- [Step 9: Start the build](#tutorial-build-mf-start "#tutorial-build-mf-start")
- [Step 10: Download output artifacts](#tutorial-build-mf-download-output "#tutorial-build-mf-download-output")
- [Clean up resources](#tutorial-build-mf-clean "#tutorial-build-mf-clean")

## Prerequisites

Before you start this tutorial, complete the following prerequisites.

- Download the [BankDemo sample
  application](https://d3lkpej5ajcpac.cloudfront.net/demo/mf/BANKDEMO-build.zip "https://d3lkpej5ajcpac.cloudfront.net/demo/mf/BANKDEMO-build.zip") and unzip it to a folder. The source folder contains COBOL programs
  and Copybooks, and definitions. It also contains a JCL
  folder for reference, although you do not need to build JCL. The folder also contains the
  meta files required for the build.
- In the AWS Mainframe Modernization console, choose **Tools** . In **Analysis,
  development, and build assets**, choose **Share assets with my AWS
  account**.

## Step 1: Share the build assets with AWS

account

In this step, you ensure that you share the build assets with your AWS account,
especially in the Region where assets are being used.

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/m2/home?region=us-west-2#/").
2. In the left navigation, choose **Tools**.
3. In **Analysis, development, and build assets**, choose
   **Share assets with my AWS account**.

###### Important

You need to do this step once in every AWS Region where you intend to do
builds.

## Step 2: Create Amazon S3 buckets

In this step, you create two Amazon S3 buckets. The first is an input bucket to hold the source
code, and the other is an output bucket to hold the build output. For more information, see
[Creating, configuring, and working with Amazon S3 buckets](../../../AmazonS3/latest/userguide/creating-buckets-s3.md "../../../AmazonS3/latest/userguide/creating-buckets-s3.md") in the
_Amazon S3 User Guide_.

1. To create the input bucket, log in to the Amazon S3 console and choose **Create
   bucket**.
2. In **General configuration**, provide a name for the bucket and
   specify the AWS Region where you want to create the bucket. An example name is
   `codebuild-regionId-accountId-input-bucket`, where `regionId` is
   the AWS Region of the bucket ,and `accountId` is your AWS account
   ID.

###### Note

If you are creating the bucket in a different AWS Region from US East (N. Virginia),
specify the `LocationConstraint` parameter. For more information, see [Create
Bucket](../../../AmazonS3/latest/API/API_CreateBucket.md "../../../AmazonS3/latest/API/API_CreateBucket.md") in the _Amazon Simple Storage Service API Reference_. 3. Retain all other settings and choose **Create bucket**. 4. Repeat steps 1-3 to create the output bucket. An example name is
`codebuild-regionId-accountId-output-bucket`, where `regionId` is
the AWS Region of the bucket and `accountId` is your AWS account ID.

Whatever names you choose for these buckets, be sure to use them throughout this
tutorial.

## Step 3: Create the build spec file

In this step, you create a build spec file,. This file provides build commands and related
settings, in YAML format, for CodeBuild to run the build. For more information, see [Build
specification reference for CodeBuild](../../../codebuild/latest/userguide/build-spec-ref.md "../../../codebuild/latest/userguide/build-spec-ref.md") in the
_AWS CodeBuild User Guide_.

1. Create a file named `buildspec.yml` in the directory that you
   unzipped as a prerequisite.
2. Add the following content to the file and save. No changes are required for this
   file.

```
version: 0.2
env:
  exported-variables:
    - CODEBUILD_BUILD_ID
    - CODEBUILD_BUILD_ARN
phases:
  install:
    runtime-versions:
      python: 3.7
  pre_build:
    commands:
      - echo Installing source dependencies...
      - ls -lR $CODEBUILD_SRC_DIR/source
  build:
    commands:
      - echo Build started on `date`
      - /start-build.sh -Dbasedir=$CODEBUILD_SRC_DIR/source -Dloaddir=$CODEBUILD_SRC_DIR/target
  post_build:
    commands:
      - ls -lR $CODEBUILD_SRC_DIR/target
      - echo Build completed on `date`
artifacts:
  files:
    - $CODEBUILD_SRC_DIR/target/**
```

Here `CODEBUILD_BUILD_ID`, `CODEBUILD_BUILD_ARN`,
`$CODEBUILD_SRC_DIR/source`, and `$CODEBUILD_SRC_DIR/target` are
environment variables available within CodeBuild. For more information, see [Environment variables in build environments](../../../codebuild/latest/userguide/build-env-ref-env-vars.md "../../../codebuild/latest/userguide/build-env-ref-env-vars.md").

At this point, your directory should look like this.

````
(root directory name)
|-- build.xml
|-- buildspec.yml
|-- LICENSE.txt
|-- source
|... etc. ``` 3. Zip the contents of the folder to a file named `BankDemo.zip`.. For this tutorial, you can't zip the folder. Instead, zip the contents of the folder to the file `BankDemo.zip`. ## Step 4: Upload the source files In this step, you upload the source code for the BankDemo sample application to your Amazon S3 input bucket. 1. Log in to the Amazon S3 console and choose **Buckets** in the left navigation pane. Then choose the input bucket you created previously. 2. Under **Objects**, choose **Upload**. 3. In the **Files and folders** section, choose **Add Files**. 4. Navigate to and choose your `BankDemo.zip` file. 5. Choose **Upload**. ## Step 5: Create IAM policies In this step, you create two [IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md"). One policy grants permissions for AWS Mainframe Modernization to access and use the Docker image that contains the Rocket Software build tools. This policy is not customized for customers. The other policy grants permissions for AWS Mainframe Modernization to interact with the input and output buckets, and with the [Amazon CloudWatch logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md") that CodeBuild generates. To learn about creating an IAM policy, see [Editing IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the *IAM User Guide*. ###### To create a policy for accessing Docker images 1. In the IAM console, copy the following policy document and paste it into the policy editor. JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "ecr:GetAuthorizationToken" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "ecr:BatchCheckLayerAvailability", "ecr:GetDownloadUrlForLayer", "ecr:BatchGetImage" ], "Resource": "arn:aws:ecr:*:673918848628:repository/m2-enterprise-build-tools" }, { "Effect": "Allow", "Action": [ "s3:PutObject" ], "Resource": "arn:aws:s3:::aws-m2-repo-*-<region>-prod" } ] }` ``` 2. Provide a name for the policy, for example, `m2CodeBuildPolicy`. ###### To create a policy that allows AWS Mainframe Modernization to interact with buckets and logs 1. In the IAM console, copy the following policy document and paste it into the policy editor. Make sure to update `regionId` to the AWS Region, and `accountId` to your AWS account. 2. Provide a name for the policy, for example, `BankdemoCodeBuildRolePolicy`. ## Step 6: Create an IAM role In this step, you create a new [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") that allows CodeBuild to interact with AWS resources for you, after you associate the IAM policies that you previously created with this new IAM role. For information about creating a service role, see [Creating a Role to Delegate Permissions to an AWS Service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the *IAM User Guide*,. 1. Log in to the IAM console and choose **Roles** in the left navigation pane. 2. Choose **Create role**. 3. Under **Trusted entity type**, choose **AWS service**. 4. Under **Use cases for other AWS services**, choose **CodeBuild**, and then choose **CodeBuild** again. 5. Choose **Next**. 6. On the **Add permissions** page, choose **Next**. You assign a policy to the role later. 7. Under **Role details**, provide a name for the role, for example, `BankdemoCodeBuildServiceRole`. 8. Under **Select trusted entities**, verify that the policy document looks like the following: JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "codebuild.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }` ``` 9. Choose **Create role**. ## Step 7: Attach the IAM policies to the IAM role In this step, you attach the two IAM policies you previously created to the `BankdemoCodeBuildServiceRole` IAM role. 1. Log in to the IAM console and choose **Roles** in the left navigation pane. 2. In **Roles**, choose the role you created previously, for example, `BankdemoCodeBuildServiceRole`. 3. In **Permissions policies**, choose **Add permissions**, and then **Attach policies**. 4. In **Other permissions policies**, choose the policies that you created previously, for example, `m2CodeBuildPolicy` and `BankdemoCodeBuildRolePolicy`. 5. Choose **Attach policies.** ## Step 8: Create the CodeBuild project In this step, you create the CodeBuild project. 1. Log in to the CodeBuild console and choose **Create build project**. 2. In the **Project configuration** section, provide a name for the project, for example, `codebuild-bankdemo-project`. 3. In the **Source** section, for **Source provider**, choose **Amazon S3**, and then choose the input bucket you created previously, for example, `codebuild-regionId-accountId-input-bucket`. 4. In the **S3 object key or S3 folder** field, enter the name of the zip file that you uploaded to the S3 bucket. In this case, the file name is `bankdemo.zip`. 5. In the **Environment** section, choose **Custom image**. 6. In the **Environment type** field, choose **Linux**. 7. Under **Image registry**, choose **Other registry**. 8. In the **External registry URL** field, <br>• For Rocket Software v9: Enter `673918848628.dkr.ecr.us-west-1.amazonaws.com/m2-enterprise-build-tools:9.0.7.R1`. If you're using a different AWS Region with Rocket Software v9, you can also specify `673918848628.dkr.ecr.<m2-region>.amazonaws.com/m2-enterprise-build-tools:9.0.7.R1`, where <m2-region> is an AWS Region in which AWS Mainframe Modernization service is available (for example, `eu-west-3`). <br>• For Rocket Software v8: Enter `673918848628.dkr.ecr.us-west-2.amazonaws.com/m2-enterprise-build-tools:8.0.9.R1` <br>• For Rocket Software v7: Enter `673918848628.dkr.ecr.us-west-2.amazonaws.com/m2-enterprise-build-tools:7.0.R10` 9. Under **Service role**, choose **Existing service role**, and in the **Role ARN** field, choose the service role you created previously; for example, `BankdemoCodeBuildServiceRole`. 10. In the **Buildspec** section, choose **Use a buildspec file**. 11. In the **Artifacts** section, under **Type**, choose **Amazon S3**, and then choose your output bucket, for example, `codebuild-regionId-accountId-output-bucket`. 12. In the **Name** field, enter the name of a folder in the bucket that you want to contain the build output artifacts, for example, `bankdemo-output.zip`. 13. Under **Artifacts packaging**, choose **Zip**. 14. Choose **Create build project**. ## Step 9: Start the build In this step, you start the build. 1. Log in to the CodeBuild console. 2. In the left navigation pane, choose **Build projects**. 3. Choose the build project that you created previously, for example, `codebuild-bankdemo-project`. 4. Choose **Start build**. This command starts the build. The build runs asynchronously. The output of the command is a JSON that includes the attribute id. This attribute idis a reference to the CodeBuild build id of the build that you just started. You can view the status of the build in the CodeBuild console. You can also see detailed logs about the build execution in the console. For more information, see [View detailed build information](../../../codebuild/latest/userguide/getting-started-build-log-console.md "../../../codebuild/latest/userguide/getting-started-build-log-console.md") in the *AWS CodeBuild User Guide*. When the current phase is COMPLETED, it means that your build finished successfully, and your compiled artifacts are ready on Amazon S3. ## Step 10: Download output artifacts In this step, you download the output artifacts from Amazon S3. The Rocket Software build tool can create several different executable types. In this tutorial, it generates shared objects. 1. Log in to the Amazon S3 console. 2. In the **Buckets** role="bold"> section, choose the name of your output bucket, for example, `codebuild-regionId-accountId-output-bucket`. 3. Choose **Download** role="bold">. 4. Unzip the downloaded file. Navigate to the target folder to see the build artifacts. These include the `.so` Linux shared objects. ## Clean up resources If you no longer need the resources that you created for this tutorial, delete them to avoid additional charges. To do so, complete the following steps: <br>• Delete the S3 buckets that you created for this tutorial. For more information, see [Deleting a bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md") in the *Amazon Simple Storage Service User Guide*. <br>• Delete the IAM policies that you created for this tutorial. For more information, see [Deleting IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-delete.md "../../../IAM/latest/UserGuide/access_policies_manage-delete.md") in the *IAM User Guide*. <br>• Delete the IAM role that you created for this tutorial. For more information, see [Deleting roles or instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the *IAM User Guide*. <br>• Delete the CodeBuild project that you created for this tutorial. For more information, see [Delete a build project in CodeBuild](../../../codebuild/latest/userguide/delete-project.md "../../../codebuild/latest/userguide/delete-project.md") in the *AWS CodeBuild User Guide*.
````
