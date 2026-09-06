

# AWS Backup and CloudFormation
<a name="integrate-cloudformation-with-aws-backup"></a>

## In general
<a name="aws-backup-cf-integration-general"></a>

With CloudFormation, you can provision and manage your AWS resources in a safe, repeatable manner using templates that you create. You can use CloudFormation templates and StackSets to manage your backup plans, backup resource selections, and backup vaults. For information about using CloudFormation, see [How Does CloudFormation Work?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.html) in the *AWS CloudFormation User Guide*.

Before you create your CloudFormation template or StackSet, consider the following:
+ Create separate templates for your backup plans and your backup vaults. You can only delete backup vaults that are empty. You can't delete a stack that includes backup vaults if they contain recovery points.
+ Verify you have a service role available before you create your stack. The AWS Backup default service role is created for you the first time you assign resources to a backup plan. If you haven't assigned resources to your backup plan, do so before creating your stack. You can also specify a custom role that you create. For more information about roles, see [IAM service roles](iam-service-roles.md).

## Deploying a backup vault, backup plan, and resource assignment using CloudFormation
<a name="aws-backup-cf-integration-backup-end-to-end"></a>

For a sample CloudFormation template that deploys a backup vault, backup plans, and resource assignment, see [Assign AWS Backup resources through CloudFormation](assigning-resources-cfn.md).

## Deploying backup plans using CloudFormation
<a name="aws-backup-cf-integration-backup-plans"></a>

For sample CloudFormation templates that deploy backup plans, see [CloudFormation templates for backup plans](plan-cfn.md).

## Deploying AWS Backup Audit Manager frameworks and report plans using CloudFormation
<a name="aws-backup-cf-integration-bam"></a>

For sample CloudFormation templates that deploy AWS Backup Audit Manager frameworks and report plans, see [Using AWS Backup Audit Manager with CloudFormation](bam-cfn-integration.md).

## Deploying backup plans across accounts using CloudFormation
<a name="aws-backup-cf-integration-organizations"></a>

You can [ use AWS CloudFormation StackSets across multiple accounts in an AWS Organization](https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/). Sample templates are available in the [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.html).

An excellent starting point and reference is the publication [Automate centralized backup at scale across AWS services using AWS Backup](https://aws.amazon.com/blogs/storage/automate-centralized-backup-at-scale-across-aws-services-using-aws-backup/). With Ibukun Oyewumi and Sabith Venkitachalapathy (Jul. 2021).

## Learning more about CloudFormation
<a name="aws-backup-cf-learn-more"></a>

For information about using CloudFormation with AWS Backup, see [AWS Backup Resource Type Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Backup.html) in the *AWS CloudFormation User Guide*.

For information about controlling access to AWS service resources when using CloudFormation, see [Controlling Access with AWS Identity and Access Management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html) in the *AWS CloudFormation User Guide*.