# Tutorial: Use pipeline-level variables

In this tutorial, you will create a pipeline where you add a variable at the pipeline level
and run a CodeBuild build action that outputs your variable value.

###### Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be
used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source action.)
If the S3 artifact bucket is in a different account from the account for your pipeline, make
sure that the S3 artifact bucket is owned by AWS accounts that are safe and will be
dependable.

###### Topics

- [Prerequisites](#tutorials-pipeline-variables-prereq "#tutorials-pipeline-variables-prereq")
- [Step 1: Create your pipeline and build
  project](#tutorials-pipeline-variables-pipeline "#tutorials-pipeline-variables-pipeline")
- [Step 2: Release change and view
  logs](#tutorials-pipeline-variables-view "#tutorials-pipeline-variables-view")

## Prerequisites

Before you begin, you must do the following:

- Create a CodeCommit repository.
- Add a .txt file to the repository.

## Step 1: Create your pipeline and build

project

In this section, you create a pipeline with the following actions:

- A source stage with a connection to your CodeCommit repository.
- A build stage with an AWS CodeBuild build action.

###### To create a pipeline with the wizard

1. Sign in to the CodePipeline console at [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. On the **Welcome** page, **Getting started** page,
   or **Pipelines** page, choose **Create
   pipeline**.
3. On the **Step 1: Choose creation option** page, under
   **Creation options**, choose the **Build custom
   pipeline** option. Choose **Next**.
4. In **Step 2: Choose pipeline settings**, in **Pipeline
   name**, enter `MyVariablesPipeline`.
5. In **Pipeline type**, keep the default selection at
   **V2**. Pipeline types differ in characteristics and price. For more
   information, see [Pipeline types](pipeline-types.md "pipeline-types.md").
6. In **Service role**, choose **New service
   role**.

###### Note

If you choose instead to use your existing CodePipeline service role, make sure that you
have added the `codeconnections:UseConnection` IAM permission to your service
role policy. For instructions for the CodePipeline service role, see [Add permissions
to the the CodePipeline service role](security-iam.md#how-to-update-role-new-services "security-iam.md#how-to-update-role-new-services"). 7. Under **Variables**, choose **Add variable**. In
**Name**, enter `timeout`. In **Default**,
enter 1000. In description, enter the following description:
`Timeout`.

This will create a variable where you can declare the value when the pipeline
execution starts. Variable names must match `[A-Za-z0-9@\-_]+` and can be
anything except an empty string. 8. Under **Advanced settings**, leave the defaults. In
**Artifact store**, choose **Default location** to use
the default artifact store, such as the Amazon S3 artifact bucket designated as the default,
for your pipeline in the Region you selected for your pipeline.

###### Note

This is not the source bucket for your source code. This is the artifact store for
your pipeline. A separate artifact store, such as an S3 bucket, is required for each
pipeline.

Choose **Next**. 9. On the **Step 3: Add source stage** page, add a source stage:

    1. In **Source provider**, choose
     **AWS CodeCommit**.
    2. In **Repository name** and **Branch name**,
     choose the your repository and branch.Choose **Next**.

10. In **Step 4: Add build stage**, add a build stage:
    1.  In **Build provider**, choose **AWS CodeBuild**.
        Allow **Region** to default to the pipeline Region.
    2.  Choose **Create project**.
    3.  In **Project name**, enter a name for this build project.
    4.  In **Environment image**, choose **Managed
        image**. For **Operating system**, choose
        **Ubuntu**.
    5.  For **Runtime**, choose **Standard**. For
        **Image**, choose
        **aws/codebuild/standard:5.0**.
    6.  For **Service role**, choose **New service
        role**.

    ###### Note

    Note the name of your CodeBuild service role. You will need the role name for the
    final step in this tutorial. 7. Under **Buildspec**, for **Build
    specifications**, choose **Insert build commands**. Choose
    **Switch to editor**, and paste the following under **Build
    commands**. In the buildspec, the customer variable
    `$CUSTOM_VAR1` will be used to output the pipeline variable in the build
    log. You will create the `$CUSTOM_VAR1` output variable as an environment
    variable in the following step.

    ```
    version: 0.2
    #env:
      #variables:
         # key: "value"
         # key: "value"
      #parameter-store:
         # key: "value"
         # key: "value"
      #git-credential-helper: yes
    phases:
      install:
        #If you use the Ubuntu standard image 2.0 or later, you must specify runtime-versions.
        #If you specify runtime-versions and use an image other than Ubuntu standard image 2.0, the build fails.
        runtime-versions:
          nodejs: 12
        #commands:
          # - command
          # - command
      #pre_build:
        #commands:
          # - command
          # - command
      build:
        commands:
          - echo $CUSTOM_VAR1
      #post_build:
        #commands:
          # - command
          # - command
    artifacts:
      files:
         - '*'
        # - location
      name: $(date +%Y-%m-%d)
      #discard-paths: yes
      #base-directory: location
    #cache:
      #paths:
        # - paths
    ```

    8.  Choose **Continue to CodePipeline**. This returns to the CodePipeline
        console and creates a CodeBuild project that uses your build commands for configuration.
        The build project uses a service role to manage AWS service permissions. This step
        might take a couple of minutes.
    9.  Under **Environment variables _-
        optional_**, to create an environment variable as an input
        variable for the build action that will be resolved by the pipeline-level variable,
        choose **Add environment variable**. This will create the variable
        specified in the buildspec as `$CUSTOM_VAR1`. In **Name**,
        enter `CUSTOM_VAR1`. In **Value**, enter
        `#{variables.timeout}`. In **Type**, choose
        `Plaintext`.

    The `#{variables.timeout}` value for the environment variable is based
    on the pipeline-level variable namespace `variables` and the pipeline-level
    variable `timeout` created for the pipeline in step 7. 10. Choose **Next**.

11. In **Step 5: Add test stage**, choose **Skip test
    stage**, and then accept the warning message by choosing
    **Skip** again.

Choose **Next**. 12. On the **Step 6: Add deploy stage** page, choose **Skip
deploy stage**, and then accept the warning message by choosing
**Skip** again. Choose **Next**. 13. On **Step 7: Review**, choose **Create
pipeline**.

## Step 2: Release change and view

logs

1. After the pipeline runs successfully, on your successful build stage, choose
   **View details**.

On the details page, choose the **Logs** tab. View the CodeBuild build
output. The commands output the value of the entered variable. 2. In the left-hand nav, choose **History**.

Choose the recent execution, and then choose the **Variables** tab.
View the resolved value for the pipeline variable.
