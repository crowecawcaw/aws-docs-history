# Tutorial: Deploy to Amazon EC2 instances with

CodePipeline

This tutorial helps you to create a deploy action in CodePipeline that deploys your code to
instances you have configured in Amazon EC2.

###### Note

As part of creating a pipeline in the console, an S3 artifact bucket will be used by
CodePipeline for artifacts. (This is different from the bucket used for an S3 source action.)
If the S3 artifact bucket is in a different account from the account for your pipeline,
make sure that the S3 artifact bucket is owned by AWS accounts that are safe and will
be dependable.

###### Note

The `EC2` deploy action is only available for V2 type pipelines.

## Prerequisites

There are a few resources that you must have in place before you can use this tutorial
to create your CD pipeline. Here are the things you need to get started:

###### Note

All of these resources should be created within the same AWS Region.

- A source control repository (this tutorial uses GitHub) where you will add a
  sample `script.sh` file.
- You must use an existing CodePipeline service role that has been updated with the
  permissions for this action. To update your service role, see [Service role policy
  permissions for the EC2 deploy action](action-reference-EC2Deploy.md#action-reference-EC2Deploy-permissions-action "action-reference-EC2Deploy.md#action-reference-EC2Deploy-permissions-action").

After you have satisfied these prerequisites, you can proceed with the tutorial and
create your CD pipeline.

## Step 1: Create Amazon EC2 Linux

instances

In this step, you create the Amazon EC2 instances where you will deploy a sample
application. As part of this process, create an instance role in IAM, if you have not
already created an instance role in the Region where you want to create
resources.

###### To create an instance role

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).
2. From the console dashboard, choose **Roles**.
3. Choose **Create role**.
4. Under **Select type of trusted entity**, select
   **AWS service**. Under **Choose a use
   case**, select **EC2**. Under **Select
   your use case**, choose **EC2**. Choose
   **Next**.
5. Search for and select the policy named
   **`AmazonSSMManagedEC2InstanceDefaultPolicy`**.
6. Search for and select the policy named
   **`AmazonSSMManagedInstanceCore`**. Choose
   **Next: Tags**.
7. Choose **Next: Review**. Enter a name for the role (for
   example, `EC2InstanceRole`).

###### Note

Make a note of your role name for the next step. You choose this role when
you are creating your instance.

###### Note

You will add permissions to this role to allow access to the S3 artifact
bucket for your pipeline after pipeline creation.

Choose **Create role**.

###### To launch instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the side navigation, choose **Instances**, and select
   **Launch instances** from the top of the page.
3. In **Name**, enter `MyInstances`. This
   assigns the instance a tag **Key** of
   `Name` and a tag **Value** of
   `MyInstances`.
4. Under **Application and OS Images (Amazon Machine Image)**,
   locate the **Amazon Linux** AMI option with the AWS logo, and
   make sure it is selected. (This AMI is described as the Amazon Linux 2 AMI (HVM)
   and is labeled "Free tier eligible".)
5. Under **Instance type**, choose the free tier eligible
   `t2.micro` type as the hardware configuration for your
   instance.
6. Under **Key pair (login)**, choose a key pair or create one.
7. Under **Network settings**, make sure the status is
   **Enable**.
8. Expand **Advanced details**. In **IAM instance
   profile**, choose the IAM role you created in the previous
   procedure (for example, `EC2InstanceRole`).

###### Note

Do not leave the instance role blank as this creates a default role and
does not select the role you created. 9. Under **Summary**, under **Number of
instances**, enter `2`. 10. Choose **Launch instance**. 11. You can view the status of the launch on the **Instances**
page. When you launch an instance, its initial state is `pending`.
After the instance starts, its state changes to `running`, and it
receives a public DNS name. (If the **Public DNS** column is
not displayed, choose the **Show/Hide** icon, and then select
**Public DNS**.)

## Step 2: Add artifact bucket permissions

to the EC2 instance role

You must update the EC2 instance role you created for your instance to allow it access
to your pipeline's artifact bucket.

###### Note

When you create the instance, you create or use an existing EC2 instance role. To
avoid `Access Denied` errors, you must add S3 bucket permissions to the
instance role to give the instance permissions to the CodePipeline artifact bucket. Create
a default role or update your existing role with the `s3:GetObject`
permission scoped down to the artifact bucket for your pipeline's Region.

1. Navigate to your pipeline in the CodePipeline console. Choose
   **Settings**. View the name and location of the artifact
   store for an existing pipeline. Make a note of the artifact bucket Amazon
   Resource Name (ARN) and copy it.
2. Navigate to the IAM console and choose **Roles**. Choose the
   instance role you created in Step 1 of this tutorial.
3. On the **Permissions** tab, choose **Add inline
   policy**.
4. Add the following JSON to the policy document, replacing the value in the
   `Resource` field with the bucket ARN.

```
{
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::`BucketName`"
}
```

5. Choose **Update**.

## Step 3: Add a script file to your

repository

Paste this sample text to create your `script.sh` file for the
post-script step in the deployment.

```

echo "Hello World!"
```

###### To add a `script.sh` file to your source repository

1. Open a text editor and then copy and paste the file above into a new
   file.
2. Commit and push your `script.sh` file to your source
   repository.
   1. Add the file.

   ```
   `git add .`
   ```

   2. Commit the change.

   ```
   `git commit -m "Adding script.sh."`
   ```

   3. Push the commit.

   ````
   `git push`
   ```Make a note of the path in your repository.
   ````

```
/MyDemoRepo/test/script.sh
```

## Step 4: Creating your pipeline

Use the CodePipeline wizard to create your pipeline stages and connect your source
repository.

###### To create your pipeline

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. On the **Welcome** page, **Getting started**
   page, or the **Pipelines** page, choose **Create
   pipeline**.
3. On the **Step 1: Choose creation option** page, under
   **Creation options**, choose the **Build custom
   pipeline** option. Choose **Next**.
4. In **Step 2: Choose pipeline settings**, in
   **Pipeline name**, enter
   `MyPipeline`.
5. CodePipeline provides V1 and V2 type pipelines, which differ in characteristics and
   price. The V2 type is the only type you can choose in the console. For more
   information, see [pipeline types](pipeline-types-planning.md "pipeline-types-planning.md"). For information about pricing for CodePipeline, see [Pricing](https://aws.amazon.com/codepipeline/pricing/ "https://aws.amazon.com/codepipeline/pricing/").
6. In **Service role**, choose **Use existing service
   role**, and then choose the CodePipeline service role that has been
   updated with the required permissions for this action. To configure your CodePipeline
   service role for this action, see [Service role policy
   permissions for the EC2 deploy action](action-reference-EC2Deploy.md#action-reference-EC2Deploy-permissions-action "action-reference-EC2Deploy.md#action-reference-EC2Deploy-permissions-action").
7. Leave the settings under **Advanced settings** at their
   defaults, and then choose **Next**.
8. On the **Step 3: Add source stage** page, add a source
   stage:
   1. In **Source provider**, choose **GitHub (via
      GitHub App)**.
   2. Under **Connection**, choose an existing connection
      or create a new one. To create or manage a connection for your GitHub
      source action, see [GitHub connections](connections-github.md "connections-github.md").
   3. In **Repository name**, choose the name of your
      GitHub repository.Choose **Next**.

9. On the **Step 4: Add build stage** page, choose
   **Skip**.
10. On the **Step 5: Add deploy stage** page, choose
    **EC2**.

![Add an EC2 deploy action to your pipeline.](images/ec2deploy-action.png)

    1. For **Target directory**, enter the directory on the
     instance that you want to deploy to, such as
     `/home/ec2-user/testhelloworld`.


    ###### Note

    Specify the deployment directory that you want the action to use
     on the instance. The action will automate creating the specified
     directory on the instance as part of the deployment.
    2. For **PostScript**, enter the path and file name for
     your script, such as `test/script.sh`.
    3. Choose **Next**.

11. On the **Step 6: Review** page, review your pipeline
    configuration and choose **Create pipeline** to create the
    pipeline.

![A console diagram showing a successful pipeline run with the deploy action added to your pipeline.](images/ec2deploy-pipeline.png) 12. After the pipeline runs successfully, choose **View details**
to view the logs on the action to view the managed compute action output.

![View logs for the Amazon EC2 deploy action in your pipeline.](images/ec2deploy-logs.png)

![View the second page of logs for the Amazon EC2 deploy action in your pipeline.](images/ec2deploy-logs2.png)

## Step 5: Test Your Pipeline

Your pipeline should have everything for running an end-to-end native AWS continuous
deployment. Now, test its functionality by pushing a code change to your source
repository.

###### To test your pipeline

1. Make a code change to your configured source repository, commit, and push the
   change.
2. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
3. Choose your pipeline from the list.
4. Watch the pipeline progress through its stages. Your pipeline should complete
   and your action deploys the script on your instances.
5. For more troubleshooting information, see [EC2 Deploy action fails with an error message
   No such file](troubleshooting.md#troubleshooting-ec2-deploy "troubleshooting.md#troubleshooting-ec2-deploy").
