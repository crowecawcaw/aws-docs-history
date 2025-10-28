# Tutorial: Create a pipeline with AWS CloudFormation

StackSets deployment actions

In this tutorial, you use the AWS CodePipeline console to create a pipeline with deployment actions
for creating a stack set and creating stack instances. When the pipeline runs, the template
creates a stack set and also creates and updates the instances where the stack set is
deployed.

###### Important

As part of creating a pipeline, an S3 artifact bucket provided by the customer will be
used by CodePipeline for artifacts. (This is different from the bucket used for an S3 source action.)
If the S3 artifact bucket is in a different account from the account for your pipeline, make
sure that the S3 artifact bucket is owned by AWS accounts that are safe and will be
dependable.

There are two ways to manage permissions for a stack set: self-managed and AWS-managed IAM
roles. This tutorial provides examples with self-managed permissions.

To most effectively use Stacksets in CodePipeline, you should have a clear understanding of the
concepts behind AWS CloudFormation StackSets and how they work. See [StackSets concepts](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md") in the _AWS CloudFormation User Guide_.

###### Topics

- [Prerequisites](#tutorials-stackset-deployment-prereq "#tutorials-stackset-deployment-prereq")
- [Step 1: Upload the sample AWS CloudFormation
  template and parameter file](#tutorials-stackset-deployment-upload "#tutorials-stackset-deployment-upload")
- [Step 2: Create your
  pipeline](#tutorials-stackset-action-pipeline "#tutorials-stackset-action-pipeline")
- [Step 3: View initial
  deployment](#tutorials-stackset-action-initial "#tutorials-stackset-action-initial")
- [Step 4: Add a CloudFormationStackInstances
  action](#tutorials-stacksets-instances "#tutorials-stacksets-instances")
- [Step 5: View stack set resources for your
  deployment](#tutorials-stacksets-view "#tutorials-stacksets-view")
- [Step 6: Make an update to your stack set](#tutorials-stacksets-update "#tutorials-stacksets-update")

## Prerequisites

For stack set operations, you use two different accounts: an administration account and a
target account. You create stack sets in the administrator account. You create individual
stacks that belong to a stack set in the target account.

###### To create an administrator role with your administrator account

- Follow the instructions in [Set up basic permissions for stack set operations](../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md#stacksets-prereqs-accountsetup "../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md#stacksets-prereqs-accountsetup"). Your role must be named
  **`AWSCloudFormationStackSetAdministrationRole`**.

###### To create a service role in the target account

- Create a service role in the target account that trusts the administrator account.
  Follow the instructions in [Set up basic permissions for stack set operations](../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md#stacksets-prereqs-accountsetup "../../../AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.md#stacksets-prereqs-accountsetup"). Your role must be named
  **`AWSCloudFormationStackSetExecutionRole`**.

## Step 1: Upload the sample AWS CloudFormation

template and parameter file

Create a source bucket for your stack set template and parameters files. Download the
sample AWS CloudFormation template file, set up a parameters file, and then zip the files before upload
to your S3 source bucket.

###### Note

Make sure to ZIP the source files before you upload to your S3 source bucket, even if
the only source file is the template.

###### To create an S3 source bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. In **Bucket name**, enter a name for your bucket.

In **Region**, choose the Region where you want to create your
pipeline. Choose **Create bucket**. 4. After the bucket is created, a success banner displays. Choose **Go to bucket
details**. 5. On the **Properties** tab, choose **Versioning**.
Choose **Enable versioning**, and then choose
**Save**.

###### To create the AWS CloudFormation template file

1. Download the following sample template file for generating CloudTrail configuration for
   stack sets: [https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/EnableAWSCloudtrail.yml](https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/EnableAWSCloudtrail.yml "https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/EnableAWSCloudtrail.yml").
2. Save the file as `template.yml`.

###### To create the parameters.txt file

1. Create a file with the parameters for your deployment. Parameters are values that you
   want to update in your stack at runtime. The following sample file updates the template
   parameters for your stack set to enable logging validation and global events.

```
[
  {
    "ParameterKey": "EnableLogFileValidation",
    "ParameterValue": "true"
  },
  {
    "ParameterKey": "IncludeGlobalEvents",
    "ParameterValue": "true"
  }
]
```

2. Save the file as `parameters.txt`.

###### To create the accounts.txt file

1. Create a file with the accounts where you want to create instances, as shown in the
   following sample file.

```
[
    "111111222222","333333444444"
]
```

2. Save the file as `accounts.txt`.

###### To create and upload source files

1. Combine the files into a single ZIP file. Your files should look like this in your ZIP
   file.

```
template.yml
parameters.txt
accounts.txt
```

2. Upload the ZIP file to your S3 bucket. This file is the source artifact created by the
   **Create Pipeline** wizard for your deployment action in CodePipeline.

## Step 2: Create your

pipeline

In this section, you create a pipeline with the following actions:

- A source stage with an S3 source action where the source artifact is your template
  file and any supporting source files.
- A deployment stage with an AWS CloudFormation stack set deployment action that creates the stack
  set.
- A deployment stage with an AWS CloudFormation stack instances deployment action that creates the
  stacks and instances within the target accounts.

###### To create a pipeline with a CloudFormationStackSet action

1. Sign in to the AWS Management Console and open the CodePipeline console at [http://console.aws.amazon.com/codesuite/codepipeline/home](http://console.aws.amazon.com/codesuite/codepipeline/home "http://console.aws.amazon.com/codesuite/codepipeline/home").
2. On the **Welcome** page, **Getting started** page,
   or **Pipelines** page, choose **Create
   pipeline**.
3. On the **Step 1: Choose creation option** page, under
   **Creation options**, choose the **Build custom
   pipeline** option. Choose **Next**.
4. In **Step 2: Choose pipeline settings**, in **Pipeline
   name**, enter `MyStackSetsPipeline`.
5. In **Pipeline type**, choose **V1** for the purposes
   of this tutorial. You can also choose **V2**; however, note that pipeline
   types differ in characteristics and price. For more information, see [Pipeline types](pipeline-types.md "pipeline-types.md").
6. In **Service role**, choose **New service role** to
   allow CodePipeline to create a service role in IAM.
7. In **Artifact store**, leave the defaults.

###### Note

This is not the source bucket for your source code. This is the artifact
store for your pipeline. A separate artifact store, such as an S3 bucket, is required
for each pipeline. When you create or edit a pipeline, you must have an artifact bucket
in the pipeline Region and one artifact bucket per AWS Region where you
are running an action.

For more information, see [Input and output artifacts](welcome-introducing-artifacts.md "welcome-introducing-artifacts.md") and [CodePipeline pipeline structure reference](reference-pipeline-structure.md "reference-pipeline-structure.md").

Choose **Next**. 8. On the **Step 3: Add source stage** page, in **Source
provider**, choose **Amazon S3**. 9. In **Bucket**, enter the S3 source bucket you created for this
tutorial, such as `BucketName`. In **S3 object key**, enter
the file path and file name for your ZIP file, such as
`MyFiles.zip`. 10. Choose **Next**. 11. In **Step 4: Add build stage**, choose **Skip build
stage**, and then accept the warning message by choosing
**Skip** again.

Choose **Next**. 12. In **Step 5: Add test stage**, choose **Skip test
stage**, and then accept the warning message by choosing
**Skip** again.

Choose **Next**. 13. In **Step 6: Add deploy stage**:

    1. In **Deploy provider**, choose **AWS CloudFormation Stack
     Set**.
    2. In **Stack set name**, enter a name for the stack set. This is
     the name of the stack set that the template creates.


    ###### Note

    Make a note of your stack set name. You will use it when you add the second
     StackSets deployment action to your pipeline.
    3. In **Template path**, enter the artifact name and
     file path where you uploaded your template file. For example, enter the following
     using the default source artifact name `SourceArtifact`.



    ```
    SourceArtifact::template.yml
    ```
    4. In **Deployment targets**, enter the artifact name
     and file path where you uploaded your accounts file. For example, enter the following
     using the default source artifact name `SourceArtifact`.



    ```
    SourceArtifact::accounts.txt
    ```
    5. In **Deployment target AWS Regions**, enter one
     Region for deployment of your initial stack instance, such as
     `us-east-1`.
    6. Expand **Deployment options**. In **Parameters**, enter the artifact name and file path where you uploaded
     your parameters file. For example, enter the following using the default source
     artifact name `SourceArtifact`.



    ```
    SourceArtifact::parameters.txt
    ```

    To enter the parameters as a literal input rather than a file path, enter the
     following:



    ```
    ParameterKey=EnableLogFileValidation,ParameterValue=true
    ParameterKey=IncludeGlobalEvents,ParameterValue=true
    ```
    7. In **Capabilities**, choose CAPABILITY\_IAM and
     CAPABILITY\_NAMED\_IAM.
    8. In **Permission model**, choose SELF\_MANAGED.
    9. In **Failure tolerance percentage**, enter
     `20`.
    10. In **Max concurrent percentage**, enter
     `25`.
    11. Choose **Next**.
    12. In **Step 7: Review**, choose **Create
     pipeline**. Your pipeline displays.
    13. Allow your pipeline to run.

## Step 3: View initial

deployment

View the resources and status for your initial deployment. After verifying the deployment
successfully created your stack set, you can add the second action to your
**Deploy** stage.

###### To view the resources

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. Under **Pipelines**, choose your pipeline and choose
   **View**. The diagram shows your pipeline source and deployment
   stages.
3. Choose the AWS CloudFormation action on the **CloudFormationStackSet**
   action in your pipeline. The template, resources, and events for your stack set are shown
   in the AWS CloudFormation console.
4. In the left navigation panel, choose **StackSets**. In the list,
   choose the new stack set.
5. Choose the **Stack instances** tab. Verify that one stack instance
   for each account you provided was created in the us-east-1 Region. Verify that the status
   for each stack instance is `CURRENT`.

## Step 4: Add a CloudFormationStackInstances

action

Create a next action in your pipeline that will allow AWS CloudFormation StackSets to create the
remainingstack instances.

###### To create a next action in your pipeline

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").

Under **Pipelines**, choose your pipeline and choose
**View**. The diagram shows your pipeline source and deployment
stages. 2. Choose to edit the pipeline. The pipeline displays in **Edit** mode. 3. On the **Deploy** stage, choose **Edit**. 4. Under the **AWS CloudFormation Stack Set** deploy action, choose **Add
action group**. 5. On the **Edit action** page, add the action details:

    1. In **Action name**, enter a name for the action.
    2. In **Action provider**, choose **AWS CloudFormation Stack
     Instances**.
    3. Under **Input artifacts**, choose
     **SourceArtifact**.
    4. In **Stack set name**, enter the name for the stack set. This is
     the name of the stack set that you provided in the first action.
    5. In **Deployment targets**, enter the artifact name
     and file path where you uploaded your accounts file. For example, enter the following
     using the default source artifact name `SourceArtifact`.



    ```
    SourceArtifact::accounts.txt
    ```
    6. In **Deployment target AWS Regions**, enter the
     Regions for deployment of your remaining stack instances, such as
     `us-east-2` and `eu-central-1` as follows:



    ```
    us-east2, eu-central-1
    ```
    7. In **Failure tolerance percentage**, enter
     `20`.
    8. In **Max concurrent percentage**, enter
     `25`.
    9. Choose **Save**.
    10. .Manually release a change. Your updated pipeline displays with two actions in the
     Deploy stage.

## Step 5: View stack set resources for your

deployment

You can view the resources and status for your stack set deployment.

###### To view the resources

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. Under **Pipelines**, choose your pipeline and then choose
   **View**. The diagram shows your pipeline source and deployment
   stages.
3. Choose the AWS CloudFormation action on the **`AWS CloudFormation Stack
Instances`** action in your pipeline. The template, resources, and
   events for your stack set are shown in the AWS CloudFormation console.
4. In the left navigation panel, choose **StackSets**. In the list,
   choose your stack set.
5. Choose the **Stack instances** tab. Verify that all remaining stack
   instances for each account you provided were created or updated in the expected Regions.
   Verify that the status for each stack instance is `CURRENT`.

## Step 6: Make an update to your stack set

Make an update to your stack set and deploy the update to instances. In this example, you
also make a change to the deployment targets you want to designate for update. The instances
that are not part of the update move to an outdated status.

1. Open the CodePipeline console at
   [https://console.aws.amazon.com/codepipeline/](https://console.aws.amazon.com/codepipeline/ "https://console.aws.amazon.com/codepipeline/").
2. Under **Pipelines**, choose your pipeline and then choose
   **Edit**. On the **Deploy** stage, choose
   **Edit**.
3. Choose to edit the **AWS CloudFormation Stack Set** action in your
   pipeline. In **Description**, write over the existing
   description with a new description for the stack set.
4. Choose to edit the **AWS CloudFormation Stack Instances** action
   in your pipeline. In **Deployment target AWS Regions**, delete the
   `us-east-2` value that was entered when the action was created.
5. Save the changes. Choose **Release change** to run your
   pipeline.
6. Open your action in AWS CloudFormation. Choose the **StackSet info** tab. In
   **StackSet description**, verify that the new description is
   shown.
7. Choose the **Stack instances** tab. Under
   **Status**, verify that the status for the stack instances in us-east-2
   is `OUTDATED`.
