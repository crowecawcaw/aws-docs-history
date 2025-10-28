# Tutorial: Use full clone with a CodeCommit pipeline

source

You can choose the full clone option for your CodeCommit source action in CodePipeline. Use this option
to allow CodeBuild to access Git metadata in your pipeline build action.

In this tutorial, you create a pipeline that accesses your CodeCommit repository, uses the full
clone option for source data, and runs a CodeBuild build that clones your repository and performs
Git commands for the repository.

###### Note

CodeBuild actions are the only downstream actions support use of Git metadata available with
the Git clone option. Also, while your pipeline can contain cross-account actions, the CodeCommit
action and the CodeBuild action must be in the same account for the full clone option to
succeed.

###### Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be
used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source action.)
If the S3 artifact bucket is in a different account from the account for your pipeline, make
sure that the S3 artifact bucket is owned by AWS accounts that are safe and will be
dependable.

###### Topics

- [Prerequisites](#tutorials-codecommit-gitclone-prereq "#tutorials-codecommit-gitclone-prereq")
- [Step 1: Create a README file](#tutorials-codecommit-gitclone-file "#tutorials-codecommit-gitclone-file")
- [Step 2: Create your pipeline and
  build project](#tutorials-codecommit-gitclone-pipeline "#tutorials-codecommit-gitclone-pipeline")
- [Step 3: Update the CodeBuild service
  role policy to clone the repository](#tutorials-codecommit-gitclone-rolepolicy "#tutorials-codecommit-gitclone-rolepolicy")
- [Step 4: View repository commands in build
  output](#tutorials-codecommit-gitclone-view "#tutorials-codecommit-gitclone-view")

## Prerequisites

Before you begin, you must create a CodeCommit repository in the same AWS account and Region as
your pipeline.

## Step 1: Create a README file

Use these steps to add a README file to your source repository. The README file provides
an example source file for the CodeBuild downstream action to read.

###### To add a README file

1. Log in to your repository and choose your repository.
2. To create a new file, choose **Add file > Create file**. Name the
   file `README.md`. file and add the following text.

```
This is a CodeCommit repository!
```

3. Choose **Commit changes**.

Make sure the `README.md` file is at the root level of your
repository.

## Step 2: Create your pipeline and

build project

In this section, you create a pipeline with the following actions:

- A source stage with a CodeCommit source action.
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
   name**, enter `MyCodeCommitPipeline`.
5. CodePipeline provides V1 and V2 type pipelines, which differ in characteristics and price.
   The V2 type is the only type you can choose in the console. For more information, see
   [pipeline types](pipeline-types-planning.md "pipeline-types-planning.md"). For information about pricing for CodePipeline, see [Pricing](https://aws.amazon.com/codepipeline/pricing/ "https://aws.amazon.com/codepipeline/pricing/").
6. In **Service role**, do one of the following:
   - Choose **Existing service role**.
   - Choose your existing CodePipeline service role. This role must have the
     `codecommit:GetRepository` IAM permission to your service role policy.
     See [Add
     permissions to the the CodePipeline service role](security-iam.md#how-to-update-role-new-services "security-iam.md#how-to-update-role-new-services").

7. Under **Advanced settings**, leave the defaults. Choose
   **Next**.
8. On the **Step 3: Add source stage** page, do the following:
   1. In **Source provider**, choose
      **CodeCommit**.
   2. In **Repository name**, choose the name of your
      repository.
   3. In **Branch name**, choose your branch name.
   4. Make sure the **Start the pipeline on source code change** option
      is selected.
   5. Under **Output artifact format**, choose **Full
      clone** to enable the Git clone option for the source repository. Only
      actions provided by CodeBuild can use the Git clone option.Choose **Next**.

9. In **Step 4: Add build stage**, do the following:
   1. In **Build provider**, choose **AWS CodeBuild**.
      Allow **Region** to default to the pipeline Region.
   2. Choose **Create project**.
   3. In **Project name**, enter a name for this build project.
   4. In **Environment image**, choose **Managed
      image**. For **Operating system**, choose
      **Ubuntu**.
   5. For **Runtime**, choose **Standard**. For
      **Image**, choose
      **aws/codebuild/standard:5.0**.
   6. For **Service role**, choose **New service
      role**.

   ###### Note

   Note the name of your CodeBuild service role. You will need the role name for the
   final step in this tutorial. 7. Under **Buildspec**, for **Build
   specifications**, choose **Insert build commands**. Choose
   **Switch to editor**, and then under **Build
   commands** paste the following code.

   ```
   version: 0.2

   env:
     git-credential-helper: yes
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
     build:
       commands:
         - git log | head -100
         - git status
         - ls
         - git describe --all
     #post_build:
       #commands:
         # - command
         # - command
   #artifacts:
     #files:
       # - location
     #name: $(date +%Y-%m-%d)
     #discard-paths: yes
     #base-directory: location
   #cache:
     #paths:
       # - paths
   ```

   8. Choose **Continue to CodePipeline**. This returns you to the
      CodePipeline console and creates a CodeBuild project that uses your build commands for
      configuration. The build project uses a service role to manage AWS service
      permissions. This step might take a couple of minutes.
   9. Choose **Next**.

10. In **Step 5: Add test stage**, choose **Skip test
    stage**, and then accept the warning message by choosing
    **Skip** again.

Choose **Next**. 11. On the **Step 6: Add deploy stage** page, choose **Skip
deploy stage**, and then accept the warning message by choosing
**Skip** again. Choose **Next**. 12. On **Step 7: Review**, choose **Create
pipeline**.

## Step 3: Update the CodeBuild service

role policy to clone the repository

The initial pipeline run will fail because you need to update the CodeBuild service role with
permissions to pull from your repository.

Add the `codecommit:GitPull` IAM permission to your service role policy. For
instructions to update the policy in the IAM console, see [Add CodeBuild GitClone permissions for CodeCommit
source actions](troubleshooting.md#codebuild-role-codecommitclone "troubleshooting.md#codebuild-role-codecommitclone").

## Step 4: View repository commands in build

output

###### To view the build output

1. When your service role is successfully updated, choose **Retry** on
   the failed CodeBuild stage.
2. After the pipeline runs successfully, on your successful build stage, choose
   **View details**.

On the details page, choose the **Logs** tab. View the CodeBuild build
output. The commands output the value of the entered variable.

The commands output the `README.md` file contents, list the files
in the directory, clone the repository, view the log, and run `git describe
 --all`.
