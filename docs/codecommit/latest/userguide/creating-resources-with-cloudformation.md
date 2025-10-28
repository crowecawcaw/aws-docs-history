AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# Creating CodeCommit resources with AWS CloudFormation

AWS CodeCommit is integrated with AWS CloudFormation, a service that helps you to model and set up your
AWS resources so that you can spend less time creating and managing your resources and
infrastructure. You create a template that describes all the AWS resources that you want (such as
repositories), and AWS CloudFormation provisions and configures those resources for
you.

When you use AWS CloudFormation, you can reuse your template to set up your CodeCommit resources
consistently and repeatedly. Describe your resources once, and then provision the same
resources over and over in multiple AWS accounts and Regions.

## CodeCommit and AWS CloudFormation templates

To provision and configure resources for CodeCommit and related services, you must
understand [AWS CloudFormation templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md").
Templates are formatted text files in JSON or YAML. These templates describe the resources
that you want to provision in your AWS CloudFormation stacks. If you're unfamiliar with JSON or YAML, you
can use AWS CloudFormation Designer to help you get started with AWS CloudFormation templates. For more information, see
[What is
AWS CloudFormation Designer?](../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md "../../../AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer.md") in the _AWS CloudFormation User Guide_.

CodeCommit supports creating repositories in AWS CloudFormation Unlike creating repositories from the
console or command line, you can use AWS CloudFormation to create repositories and automatically commit
code to the newly created repository from a specified .zip file in an Amazon S3 bucket. For more
information, including examples of JSON and YAML templates for repositories, see
[AWS::CodeCommit::Repository](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.md").

When you create a CodeCommit repository using AWS CloudFormation, you have the option to commit code to that
repository as part of the creation process as long as the archive is less
than 20 MB by configuring
properties in [AWS:CodeCommit::Repository Code](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.md"). You can specify the Amazon S3 bucket where the code is
stored, and optionally use the [BranchName property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-codecommit-repository-code.md") to specify the name of the default branch that will be created
in the initial commit of that code. These properties are only used in initial repository
creation, and are ignored on stack updates. You cannot use these properties to make additional
commits to a repository, or to change the name of the default branch after the initial commit
is made.

###### Note

On January 19, 2021, AWS changed the name of the default branch in CodeCommit from
_master_ to _main_. This
name change affects the default behavior of CodeCommit when creating the initial commit for
repositories using the CodeCommit console, the CodeCommit APIs, the AWS SDKs, and the
AWS CLI. Repositories created with AWS CloudFormation or the AWS CDK with an initial commit
of code as part of creation align with this change beginning March 4, 2021. This change does
not affect existing repositories or branches. Customers who use local Git clients to create
their initial commits have a default branch name that follows the configuration of those Git
clients. For more information, see [Working with
branches](branches.md "branches.md"), [Create a
commit](how-to-create-commit.md "how-to-create-commit.md"), and [Change branch
settings](how-to-change-branch.md "how-to-change-branch.md").

You can also create templates that create related resources, such as [notification rules](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codestarnotifications-notificationrule.md") for repositories, [AWS CodeBuild build
projects](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.md"), [AWS CodeDeploy
applications](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.md"), and [AWS CodePipeline
pipelines](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.md").

## Template examples

The following examples create a CodeCommit repository named
`MyDemoRepo`. The newly created repository is populated with code stored
in an Amazon S3 bucket named `MySourceCodeBucket` and placed in a branch
named `development`, which is the default branch for the repository.

###### Note

The name of the Amazon S3 bucket that contains the ZIP file with the content that will be
committed to the new repository can be specified using an ARN or the name of the bucket in the
Amazon Web Services account. The Amazon S3 object key is as defined in the [Amazon S3 Developer Guide](../../../AmazonS3/latest/dev/Introduction.md#BasicsKeys "../../../AmazonS3/latest/dev/Introduction.md#BasicsKeys").

**JSON**:

```
{
    "MyRepo": {
        "Type": "AWS::CodeCommit::Repository",
        "Properties": {
            "RepositoryName": "`MyDemoRepo`",
            "RepositoryDescription": "`This is a repository for my project with code from MySourceCodeBucket.`",
            "Code": {
                "BranchName": "`development`",
                "S3": {
                    "Bucket": "`MySourceCodeBucket`",
                    "Key": "`MyKey`",
                    "ObjectVersion": "`1`"
                }
            }
        }
    }
}
```

**YAML**:

```
MyRepo:
  Type: AWS::CodeCommit::Repository
  Properties:
    RepositoryName: `MyDemoRepo`
    RepositoryDescription: `This is a repository for my project with code from MySourceCodeBucket.`
    Code:
      BranchName: `development`
      S3:
        Bucket: `MySourceCodeBucket`,
        Key: `MyKey`,
        ObjectVersion: `1`
```

For more examples, see [AWS::CodeCommit::Repository](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codecommit-repository.md").

## AWS CloudFormation, CodeCommit, and the AWS Cloud Development Kit (AWS CDK)

Repositories created using the AWS CDK use AWS CloudFormation functionality in their creation.
Understanding how AWS CloudFormation templates work with CodeCommit resources can help you create and manage your
AWS CDK code. For more information about the AWS CDK, see the [AWS Cloud Development Kit (AWS CDK) Developer Guide](../../../cdk/latest/guide/home.md "../../../cdk/latest/guide/home.md") and the [AWS CDK API Reference.](../../../cdk/api/v2/docs/aws-cdk-lib.md "../../../cdk/api/v2/docs/aws-cdk-lib.md")

The following AWS CDK Typescript example creates a CodeCommit repository named
`MyDemoRepo`. The newly created repository is populated with code
stored in an Amazon S3 bucket named `MySourceCodeBucket` and placed in a
branch named `development`, which is the default branch for the
repository.

```
import * as cdk from '@aws-cdk/core';
import codecommit = require('@aws-cdk/aws-codecommit');
export class CdkCodecommitStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // The code creates a CodeCommit repository with a default branch name development
      new codecommit.CfnRepository(this, 'MyRepoResource', {
            repositoryName: "MyDemoRepo",
            code: {
              "branchName": "development",
              "s3": {
                "bucket": "MySourceCodeBucket",
                "key": "MyKey"
              }
            },
        }
     );
  }
}
```

## Learn more about AWS CloudFormation

To learn more about AWS CloudFormation, see the following resources:

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/")
- [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")
- [AWS CloudFormation Command
  Line Interface User Guide](../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md "../../../cloudformation-cli/latest/userguide/what-is-cloudformation-cli.md")
