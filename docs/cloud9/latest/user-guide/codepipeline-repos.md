AWS Cloud9 is no longer available to new customers. Existing customers of
AWS Cloud9 can continue to use the service as normal.
[Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "https://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")

# Working with AWS CodePipeline in the AWS Cloud9 IDE

You can use the AWS Cloud9 Integrated Development Environment (IDE) to work with source code in repositories that are
compatible with AWS CodePipeline.

CodePipeline is a continuous delivery service you can use to model, visualize, and automate the
steps required to release your software and ongoing changes you make to it. You can use CodePipeline
to quickly model and configure the different stages of a software release process. For more
information, see the [AWS CodePipeline User Guide](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md").

###### Note

Completing these procedures might result in charges to your AWS account. These include
possible charges for services such as Amazon EC2, CodePipeline, Amazon S3, and AWS services supported by
CodePipeline. For more information, see [Amazon EC2
Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/"), [AWS CodePipeline
Pricing](https://aws.amazon.com/codepipeline/pricing/ "https://aws.amazon.com/codepipeline/pricing/"), [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/"), and
[Cloud Services Pricing](https://aws.amazon.com/pricing/services/ "https://aws.amazon.com/pricing/services/").

- [Step 1: Create or Identify Your
  Source Code Repository](#codepipeline-repos-create-source-code "#codepipeline-repos-create-source-code")
- [Step 2: Create an AWS Cloud9
  Development Environment, Connect It to the Code Repository, and Upload Your
  Code](#codepipeline-repos-connect-to-repo "#codepipeline-repos-connect-to-repo")
- [Step 3: Prepare to Work with AWS CodePipeline](#codepipeline-repos-setup "#codepipeline-repos-setup")
- [Step 4: Create a Pipeline in AWS CodePipeline](#codepipeline-repos-create-pipeline "#codepipeline-repos-create-pipeline")

## Step 1: Create or identify your source

code repository

In this step, you create or identify a source code repository that is compatible with
CodePipeline.

Later in this topic, you upload your software's source code to that repository. CodePipeline
will build, test, and deploy the uploaded source code in that repository by using related
pipelines that you also create.

Your source code repository must be one of the following repository types that CodePipeline
supports:

- **AWS CodeCommit**. If you already have a repository in
  CodeCommit that you want to use, skip ahead to [Step 2: Create an AWS Cloud9
  Development Environment, Connect It to the Code Repository, and Upload Your
  Code](#codepipeline-repos-connect-to-repo "#codepipeline-repos-connect-to-repo"). Otherwise, to use CodeCommit, follow these instructions in the _AWS CodeCommit Sample_ in this order, and then
  return to this topic:
  - [Step 1: Set Up Your IAM Group
    with Required Access Permissions](sample-codecommit.md#sample-codecommit-permissions "sample-codecommit.md#sample-codecommit-permissions")
  - [Step 2: Create a Repository in
    AWS CodeCommit](sample-codecommit.md#sample-codecommit-create-repo "sample-codecommit.md#sample-codecommit-create-repo")

- **Amazon S3**. If you already have a bucket in Amazon S3 that
  you want to use, skip ahead to [Step 2: Create an AWS Cloud9 Development Environment, Connect It to the Code
  Repository, and Upload Your Code](#codepipeline-repos-connect-to-repo "#codepipeline-repos-connect-to-repo"). Otherwise, to use Amazon S3, follow these
  instructions in the _Amazon Simple Storage Service User Guide_ in this order, and then
  return to this topic:
  - [Sign Up
    for Amazon S3](../../../AmazonS3/latest/gsg/SigningUpforS3.md "../../../AmazonS3/latest/gsg/SigningUpforS3.md")
  - [Create a
    Bucket](../../../AmazonS3/latest/userguide/creating-bucket.md "../../../AmazonS3/latest/userguide/creating-bucket.md")

- **GitHub**. If you already have a repository in GitHub,
  you can clone it and create a local copy on your development environment using the
  [Git panel](source-control-gitpanel.md "source-control-gitpanel.md") interface. If you don't yet have an account or repository set up on
  GitHub, refer to the [relevant documentation](https://docs.github.com/en/github "https://docs.github.com/en/github") for instructions.

## Step 2: Create an AWS Cloud9 Development Environment,

connect it to the code repository, and upload your code

In this step, you create an AWS Cloud9 development environment in the AWS Cloud9 console. You then connect the environment
to the repository that CodePipeline will use. Finally, you use the AWS Cloud9 IDE for the environment to
upload your source code to the repository.

To create the environment, follow the instructions in [Creating an Environment](create-environment.md "create-environment.md"), and then return to this topic. (If you already have an
environment, you can use it. You don't need to create a new one.)

To connect the environment to the repository, and then upload your source code to the
repository if it isn't already there, use one of the following sets of instructions. The
set you choose depends on the type of repository that stores the source code.

| **Repository type** | **Instructions**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CodeCommit          | Follow these instructions in the _AWS CodeCommit Sample_:<br>• [Step 3: Connect Your<br>Environment to the Remote Repository](sample-codecommit.md#sample-codecommit-connect-repo "sample-codecommit.md#sample-codecommit-connect-repo")<br>• [Step 4: Clone the Remote<br>Repository into Your Environment](sample-codecommit.md#sample-codecommit-clone-repo "sample-codecommit.md#sample-codecommit-clone-repo")<br>• [Step 5: Add Files to the<br>Repository](sample-codecommit.md#sample-codecommit-add-files "sample-codecommit.md#sample-codecommit-add-files"), substituting your own source code for this<br>step |
| Amazon S3           | • Install and configure the AWS CLI or AWS CloudShell in the environment, as<br>described in the [AWS CLI and AWS CloudShell<br>Sample](sample-aws-cli.md "sample-aws-cli.md").<br>• To upload your source code to the bucket, use the AWS CLI or the<br>AWS CloudShell in the environment to run the [aws s3<br>cp](../../../cli/latest/reference/s3/cp.md "../../../cli/latest/reference/s3/cp.md") command. (For the AWS CloudShell, you can remove<br>`aws` from the command.)                                                                                                                                         |
| GitHub              | You can clone a repository hosted on GitHub and interact with by using<br>the [Git panel](source-control-gitpanel.md "source-control-gitpanel.md")<br>interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

After you connect the environment to the repository, whenever you push source code changes
from the AWS Cloud9 IDE to the repository, CodePipeline automatically sends those changes through
related pipelines to be built, tested, and deployed. You create a related pipeline later in
this topic.

## Step 3: Prepare to work with AWS CodePipeline

In this step, you attach a specific AWS managed policy to the IAM group you created or
identified in [Team Setup](setup.md "setup.md"). This enables the group's users to
begin creating and working with pipelines in CodePipeline.

If you have used CodePipeline before, skip ahead to [Step 4: Create a Pipeline in AWS CodePipeline](#codepipeline-repos-create-pipeline "#codepipeline-repos-create-pipeline").

For this step, follow these instructions in [Step 3: Use an IAM Managed Policy to Assign AWS CodePipeline; Permissions to the IAM
User](../../../codepipeline/latest/userguide/getting-started-codepipeline.md#assign-permissions "../../../codepipeline/latest/userguide/getting-started-codepipeline.md#assign-permissions") in the _AWS CodePipeline User Guide_, and then return to this
topic.

## Step 4: Create a pipeline in

AWS CodePipeline

In this step, you create a pipeline in CodePipeline that uses the repository you created or
identified earlier in this topic.

For this step, follow the instructions in [Create a
Pipeline in AWS CodePipeline](../../../codepipeline/latest/userguide/pipelines-create.md "../../../codepipeline/latest/userguide/pipelines-create.md") in the
_AWS CodePipeline User Guide_.

After you create the pipeline, CodePipeline sends the current version of the source code in the
repository through the pipeline to be built, tested, and deployed. Then, whenever you push
source code changes from the AWS Cloud9 IDE to the repository, CodePipeline automatically sends those
changes through the pipeline to be built, tested, and deployed.

To view the pipeline, follow the instructions in [View Pipeline
Details and History in AWS CodePipeline](../../../codepipeline/latest/userguide/pipelines-view.md "../../../codepipeline/latest/userguide/pipelines-view.md") in the
_AWS CodePipeline User Guide_.
