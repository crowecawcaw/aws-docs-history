

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Tutorial: Upload artifacts to Amazon S3
<a name="build-deploy"></a>

In this tutorial, you learn how to upload artifacts to an Amazon S3 bucket using an Amazon CodeCatalyst [workflow](workflows-concepts.md#workflows-concepts-workflows) that includes a couple of [build actions](workflows-concepts.md#workflows-concepts-actions). These actions run in series when the workflow starts. The first build action generates two files, `Hello.txt` and `Goodbye.txt`, and bundles them into a build artifact. The second build action uploads the artifact to Amazon S3. You'll configure the workflow to run every time you push a commit to your source repository.

**Topics**
+ [Prerequisites](#build-deploy-tut-prereqs)
+ [Step 1: Create an AWS role](#build-deploy-tut-role)
+ [Step 2: Create an Amazon S3 bucket](#build-deploy-tut-artifact)
+ [Step 3: Create a source repository](#deploy-tut-lambda-cfn-source)
+ [Step 4: Create a workflow](#build-deploy-tut-workflow.title)
+ [Step 5: Verify the results](#build-deploy.s3.verify)
+ [Clean up](#deploy-tut-lambda-cfn-clean-up)

## Prerequisites
<a name="build-deploy-tut-prereqs"></a>

Before you begin, you need the following:
+ You need a CodeCatalyst **space** with a connected AWS account. For more information, see [Creating a space](spaces-create.md).
+ In your space, you need an empty project called:

  ```
  codecatalyst-artifact-project
  ```

  Use the **Start from scratch** option to create this project.

  For more information, see [Creating an empty project in Amazon CodeCatalyst](projects-create.md#projects-create-empty).
+ In your project, you need a CodeCatalyst **environment** called:

  ```
  codecatalyst-artifact-environment
  ```

  Configure this environment as follows:
  + Choose any type, such as **Development**.
  + Connect your AWS account to it.
  + For the **Default IAM role**, choose any role. You'll specify a different role later.

  For more information, see [Deploying into AWS accounts and VPCs](deploy-environments.md).

## Step 1: Create an AWS role
<a name="build-deploy-tut-role"></a>

In this step, you create an AWS IAM role which you will later assign to the build action in your workflow. This role grants the CodeCatalyst build action permission to access your AWS account and write to Amazon S3 where your artifact will be stored. The role is called the **Build role**.

**Note**  
If you already have a build role that you created for another tutorial, you can use it for this tutorial too. Just make sure it has the permissions and trust policy shown in the following procedure.

For more information on IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *AWS AWS Identity and Access Management User Guide*.

**To create a build role**

1. Create a policy for the role, as follows:

   1. Sign in to AWS.

   1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

   1. In the navigation pane, choose **Policies**.

   1. Choose **Create policy**.

   1. Choose the **JSON** tab.

   1. Delete the existing code.

   1. Paste the following code:

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Sid": "VisualEditor0",
                  "Effect": "Allow",
                  "Action": [
                      "s3:PutObject",
                      "s3:ListBucket"
                  ],
                  "Resource": "*"
              }
          ]
      }
      ```

------
**Note**  
The first time the role is used to run workflow actions, use the wildcard in the resource policy statement and then scope down the policy with the resource name after it is available.  

      ```
      "Resource": "*"
      ```

   1. Choose **Next: Tags**.

   1. Choose **Next: Review**.

   1. In **Name**, enter:

      ```
      codecatalyst-s3-build-policy
      ```

   1. Choose **Create policy**.

      You have now created a permissions policy.

1. Create the build role, as follows:

   1. In the navigation pane, choose **Roles**, and then choose **Create role**.

   1. Choose **Custom trust policy**.

   1. Delete the existing custom trust policy.

   1. Add the following custom trust policy:

   1. Choose **Next**.

   1. In **Permissions policies**, search for `codecatalyst-s3-build-policy` and select its check box.

   1. Choose **Next**.

   1. For **Role name**, enter:

      ```
      codecatalyst-s3-build-role
      ```

   1. For **Role description**, enter:

      ```
      CodeCatalyst build role
      ```

   1. Choose **Create role**.

   You have now created a build role with a trust policy and permissions policy.

## Step 2: Create an Amazon S3 bucket
<a name="build-deploy-tut-artifact"></a>

In this step, you create an Amazon S3 bucket where the `Hello.txt` and `Goodbye.txt` artifacts will be uploaded.

**To create an Amazon S3 bucket**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. In the main pane, choose **Create bucket**.

1. For **Bucket name**, enter:

   ```
   codecatalyst-artifact-bucket
   ```

1. For **AWS Region**, choose a Region. This tutorial assumes you chose **US West (Oregon) us-west-2**. For information about Regions supported by Amazon S3, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *AWS General Reference*.

1. At the bottom of the page, choose **Create bucket**.

1. Copy the name of the bucket you just created, for example:

   ```
   codecatalyst-artifact-bucket
   ```

You have now created a bucket called **codecatalyst-artifact-bucket** in the US West (Oregon) us-west-2 Region.

## Step 3: Create a source repository
<a name="deploy-tut-lambda-cfn-source"></a>

In this step, you create a source repository in CodeCatalyst. This repository is used to store the tutorial's workflow definition file. 

For more information on source repositories, see [Creating a source repository](source-repositories-create.md).

**To create a source repository**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Navigate to your project, `codecatalyst-artifact-project`.

1. In the navigation pane, choose **Code**, and then choose **Source repositories**. 

1. Choose **Add repository**, and then choose **Create repository**.

1. In **Repository name**, enter:

   ```
   codecatalyst-artifact-source-repository
   ```

1. Choose **Create**.

You have now created a repository called `codecatalyst-artifact-source-repository`.

## Step 4: Create a workflow
<a name="build-deploy-tut-workflow.title"></a>

In this step, you create a workflow that consists of the following building blocks that run sequentially:
+ A trigger – This trigger starts the workflow run automatically when you push a change to your source repository. For more information on triggers, see [Starting a workflow run automatically using triggers](workflows-add-trigger.md).
+ A build action called `GenerateFiles` – On trigger, the `GenerateFiles` action creates two files, `Hello.txt` and `Goodbye.txt`, and packages them into an output artifact called `codecatalystArtifact`.
+ Another build action called `Upload` – On completion of the `GenerateFiles` action, the `Upload` action runs the AWS CLI command `aws s3 sync` to upload the files in the `codecatalystArtifact` and in your source repository to your Amazon S3 bucket. The AWS CLI comes pre-installed and pre-configured on the CodeCatalyst compute platform, so you don't need to install or configure it.

  For more information on the pre-packaged software on the CodeCatalyst compute platform, see [Specifying runtime environment images](build-images.md). For more information on the AWS CLI's `aws s3 sync` command, see [sync](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html) in the *AWS CLI Command Reference*.

For more information on the build action, see [Building with workflows](build-workflow-actions.md).

**To create a workflow**

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose **Create workflow**.

1. Delete the YAML sample code.

1. Add the following YAML code:
**Note**  
In the YAML code that follows, you can omit the `Connections:` section if you want. If you omit this section, you must ensure that the role specified in the **Default IAM role** field in your environment includes the permissions and trust policies described in [Step 1: Create an AWS role](#build-deploy-tut-role). For more information about setting up an environment with a default IAM role, see [Creating an environment](deploy-environments-creating-environment.md).

   ```
   Name: codecatalyst-artifact-workflow
   SchemaVersion: 1.0
   
   Triggers:
     - Type: Push
       Branches:
         - main   
   Actions:
     GenerateFiles:
       Identifier: aws/build@v1
       Configuration: 
         Steps:
           # Create the output files.
           - Run: echo "Hello, World!" > "Hello.txt"
           - Run: echo "Goodbye!" > "Goodbye.txt"
       Outputs:
         Artifacts:
           - Name: codecatalystArtifact
             Files:
               - "**/*"
     Upload:
       Identifier: aws/build@v1
       DependsOn: 
         - GenerateFiles
       Environment:
         Name: {{codecatalyst-artifact-environment}}
         Connections:
           - Name: {{codecatalyst-account-connection}}
             Role: {{codecatalyst-s3-build-role}}
       Inputs:
         Artifacts:
           - codecatalystArtifact
       Configuration: 
         Steps:
           # Upload the output artifact to the S3 bucket.
           - Run: aws s3 sync . s3://{{codecatalyst-artifact-bucket}}
   ```

   In the code above, replace:
   + {{codecatalyst-artifact-environment}} with the name of the environment you created in [Prerequisites](#build-deploy-tut-prereqs).
   + {{codecatalyst-account-connection}} with the name of the account connection you created in [Prerequisites](#build-deploy-tut-prereqs).
   + {{codecatalyst-s3-build-role}} with the name of the build role that you created in [Step 1: Create an AWS role](#build-deploy-tut-role).
   + {{codecatalyst-artifact-bucket}} with the name of the Amazon S3 you created in [Step 2: Create an Amazon S3 bucket](#build-deploy-tut-artifact).

   For information about the properties in this file, see the [Build and test actions YAML](build-action-ref.md).

1. (Optional) Choose **Validate** to make sure the YAML code is valid before committing.

1. Choose **Commit**.

1. On the **Commit workflow** dialog box, enter the following:

   1. For **Workflow file name**, leave the default, `codecatalyst-artifact-workflow`.

   1. For **Commit message**, enter:

      ```
      add initial workflow file
      ```

   1. For **Repository**, choose **codecatalyst-artifact-source-repository**.

   1. For **Branch name**, choose **main**.

   1. Choose **Commit**.

   You have now created a workflow. A workflow run starts automatically because of the trigger defined at the top of the workflow. Specifically, when you committed (and pushed) the `codecatalyst-artifact-workflow.yaml` file to your source repository, the trigger started the workflow run.

**To view the workflow run in progress**

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.

1. Choose the workflow you just created: `codecatalyst-artifact-workflow`.

1. Choose **GenerateFiles** to see the first build action progress.

1. Choose **Upload** to see the second build action progress.

1. When the **Upload** action finishes, do the following:
   + If the workflow run succeeded, go to the next procedure.
   + If the workflow run failed, choose **Logs** to troubleshoot the issue.

## Step 5: Verify the results
<a name="build-deploy.s3.verify"></a>

After the workflow runs, go to the Amazon S3 service and look in your {{codecatalyst-artifact-bucket}} bucket. It should now include the following files and folders:

```
.
|— .aws/
|— .git/
|Goodbye.txt
|Hello.txt
|REAME.md
```

The `Goodbye.txt` and `Hello.txt` files were uploaded because they were part of the `codecatalystArtifact` artifact. The `.aws/`, `.git/`, and `README.md` files were uploaded because they were in your source repository.

## Clean up
<a name="deploy-tut-lambda-cfn-clean-up"></a>

Clean up in CodeCatalyst and AWS to avoid being charged for these services.

**To clean up in CodeCatalyst**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/).

1. Delete the `codecatalyst-artifact-source-repository` source repository.

1. Delete the `codecatalyst-artifact-workflow` workflow.

**To clean up in AWS**

1. Clean up in Amazon S3, as follows:

   1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

   1. Delete the files in the `codecatalyst-artifact-bucket` bucket.

   1. Delete the `codecatalyst-artifact-bucket` bucket.

1. Clean up in IAM, as follows:

   1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

   1. Delete the `codecatalyst-s3-build-policy`.

   1. Delete the `codecatalyst-s3-build-role`.