

# Getting started with connections
<a name="getting-started-connections"></a>

The easiest way to get started with connections is to set up a connection that associates your third-party source repository to your AWS resources. If you wanted to connect your pipeline to an AWS source, such as CodeCommit, you would connect to it as a source action. However, if you have an external repository, you have to create a connection to associate your repository with your pipeline. In this tutorial, you set up a connection with your Bitbucket repository and your pipeline.

In this section, you use connections with: 
+ AWS CodePipeline: In these steps, you create a pipeline with your Bitbucket repository as the pipeline source.
+ [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html): Next, you associate your Bitbucket repository to your feedback and analysis tools in CodeGuru Reviewer.

**Topics**
+ [Prerequisites](#getting-started-connections-prerequisites)
+ [Step 1: Edit your source file](#getting-started-connections-edit)
+ [Step 2: Create your pipeline](#getting-started-connections-pipeline)
+ [Step 3: Associate your repository with CodeGuru Reviewer](#getting-started-connections-analysis)

## Prerequisites
<a name="getting-started-connections-prerequisites"></a>

Before you begin, complete the steps in [Setting up](setting-up.md). You also need a third-party source repository that you want to connect to your AWS services and allow the connection to manage authentication for you. For example, you might want to connect a Bitbucket repository to your AWS services that integrate with source repositories.
+ Create a Bitbucket repository with your Bitbucket account.
+ Have your Bitbucket credentials ready. When you use the AWS Management Console to set up a connection, you are asked to sign in with your Bitbucket credentials. 

## Step 1: Edit your source file
<a name="getting-started-connections-edit"></a>

When you create your Bitbucket repository, a default `README.md` file is included, which you will edit.

1. Log in to your Bitbucket repository and choose **Source**.

1. Choose the `README.md` file and choose **Edit** at the top of the page. Delete the existing text and add the following text.

   ```
   This is a Bitbucket repository!
   ```

1. Choose **Commit**.

   Make sure the `README.md` file is at the root level of your repository.

## Step 2: Create your pipeline
<a name="getting-started-connections-pipeline"></a>

In this section, you create a pipeline with the following actions:
+ A source stage with a connection to your Bitbucket repository and action.
+ A build stage with an AWS CodeBuild build action.

**To create a pipeline with the wizard**

1. Sign in to the CodePipeline console at [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/).

1. On the **Welcome** page, **Getting started** page, or **Pipelines** page, choose **Create pipeline**.

1. In **Step 1: Choose pipeline settings**, in **Pipeline name**, enter **MyBitbucketPipeline**.

1. In **Service role**, choose **New service role**.
**Note**  
If you choose instead to use your existing CodePipeline service role, make sure that you have added the `codeconnections:UseConnection` IAM permission to your service role policy. For instructions for the CodePipeline service role, see [Add permissions to the the CodePipeline service role](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-iam.html#how-to-update-role-new-services).

1. Under **Advanced settings**, leave the defaults. In **Artifact store**, choose **Default location** to use the default artifact store, such as the Amazon S3 artifact bucket designated as the default, for your pipeline in the Region you selected for your pipeline.
**Note**  
This is not the source bucket for your source code. This is the artifact store for your pipeline. A separate artifact store, such as an S3 bucket, is required for each pipeline.

   Choose **Next**.

1. On the **Step 2: Add source stage** page, add a source stage:

   1. In **Source provider**, choose **Bitbucket**.

   1. Under **Connection**, choose **Connect to Bitbucket**.

   1. On the **Connect to Bitbucket** page, in **Connection name**, enter the name for the connection that you want to create. The name helps you identify this connection later.

      Under **Bitbucket apps**, choose **Install a new app**.

   1. On the app installation page, a message shows that the AWS CodeStar app is trying to connect to your Bitbucket account. Choose **Grant access**. After you have authorized the connection, your repositories on Bitbucket are detected, and you can choose to associate one with your AWS resource.

   1. The connection ID for your new installation is displayed. Choose **Complete connection**. You will be returned to the CodePipeline console.

   1. In **Repository name**, choose the name of your Bitbucket repository.

   1. In **Branch name**, choose the branch for your repository.

   1. Make sure the **Start the pipeline on source code change** option is selected.

   1. Under **Output artifact format**, choose one of the following: **CodePipeline default**.
      + Choose **CodePipeline default** to use the default zip format for artifacts in the pipeline.
      + Choose **Full clone** to include Git metadata about the repository for artifacts in the pipeline. This is only supported for CodeBuild actions.

   Choose **Next**.

1. In **Add build stage**, add a build stage:

   1. In **Build provider**, choose **AWS CodeBuild**. Allow **Region** to default to the pipeline Region.

   1. Choose **Create project**.

   1. In **Project name**, enter a name for this build project.

   1. In **Environment image**, choose **Managed image**. For **Operating system**, choose **Ubuntu**.

   1. For **Runtime**, choose **Standard**. For **Image**, choose **aws/codebuild/standard:5.0**.

   1. For **Service role**, choose **New service role**.

   1. Under **Buildspec**, for **Build specifications**, choose **Insert build commands**. Choose **Switch to editor**, and paste the following under **Build commands**:

      ```
      version: 0.2
      
      phases:
        install:
          #If you use the Ubuntu standard image 2.0 or later, you must specify runtime-versions.
          #If you specify runtime-versions and use an image other than Ubuntu standard image 2.0, the build fails.
          runtime-versions:
            nodejs: 12
            # name: version
          #commands:
            # - command
            # - command
        pre_build:
          commands:
            - ls -lt
            - cat README.md
        # build:
          #commands:
            # - command
            # - command
        #post_build:
          #commands:
            # - command
            # - command
      #artifacts:
        #files:
          # - location
          # - location
        #name: $(date +%Y-%m-%d)
        #discard-paths: yes
        #base-directory: location
      #cache:
        #paths:
          # - paths
      ```

   1. Choose **Continue to CodePipeline**. This returns to the CodePipeline console and creates a CodeBuild project that uses your build commands for configuration. The build project uses a service role to manage AWS service permissions. This step might take a couple of minutes.

   1. Choose **Next**.

1. On the **Step 4: Add deploy stage** page, choose **Skip deploy stage**, and then accept the warning message by choosing **Skip** again. Choose **Next**.

1. On **Step 5: Review**, choose **Create pipeline**.

1. When your pipeline is successfully created, a pipeline execution starts.  
![Console screenshot showing successfully completed pipeline with Bitbucket source.](http://docs.aws.amazon.com/dtconsole/latest/userguide/images/pipeline-wizard-bitbucket.png)

1. On your successful build stage, choose **Details**.

   Under **Execution details**, view the CodeBuild build output. The commands output the `README.md` file contents as follows:

   ```
   This is a Bitbucket repository!
   ```  
![Console screenshot showing successfully completed build output example.](http://docs.aws.amazon.com/dtconsole/latest/userguide/images/pipeline-wizard-bitbucket-output.png)

## Step 3: Associate your repository with CodeGuru Reviewer
<a name="getting-started-connections-analysis"></a>

After you create a connection, you can use that connection for all of your AWS resources in the same account. For example, you can use the same Bitbucket connection for a CodePipeline source action in a pipeline and your repository commit analysis in CodeGuru Reviewer.

1. Sign in to the CodeGuru Reviewer console.

1. Under **CodeGuru Reviewer**, choose **Associate repository**.

   The one-page wizard opens.

1. Under **Select source provider**, choose **Bitbucket**.

1. Under **Connect to Bitbucket (with AWS CodeConnections)**, choose the connection you created for your pipeline.

1. Under **Repository location**, choose the name of your Bitbucket repository, and choose **Associate**.

   You can continue to set up code reviews. For more information, see [Connecting to Bitbucket to associate a repository with CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-bitbucket-association.html) in the *Amazon CodeGuru Reviewer User Guide*.