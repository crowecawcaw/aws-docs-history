# AWS Backup and AWS CloudFormation

## In general

With AWS CloudFormation, you can provision and manage your AWS resources in a safe, repeatable manner
using templates that you create. You can use AWS CloudFormation templates and StackSets to manage your
backup plans, backup resource selections, and backup vaults. For information about using
AWS CloudFormation, see [How Does AWS CloudFormation
Work?](../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.md "../../../AWSCloudFormation/latest/UserGuide/cfn-whatis-howdoesitwork.md") in the _AWS CloudFormation User Guide_.

Before you create your AWS CloudFormation template or StackSet, consider the following:

- Create separate templates for your backup plans and your backup vaults. You can only
  delete backup vaults that are empty. You can't delete a stack that includes backup vaults
  if they contain recovery points.
- Verify you have a service role available before you create your stack. The AWS Backup
  default service role is created for you the first time you assign resources to a backup
  plan. If you haven't assigned resources to your backup plan, do so before creating your
  stack. You can also specify a custom role that you create. For more information about
  roles, see [IAM service roles](iam-service-roles.md "iam-service-roles.md").

## Deploying a backup vault, backup

plan, and resource assignment using AWS CloudFormation

For a sample AWS CloudFormation template that deploys a backup vault, backup plans, and resource
assignment, see [Assign AWS Backup resources through AWS CloudFormation](assigning-resources-cfn.md "assigning-resources-cfn.md").

## Deploying backup plans using AWS CloudFormation

For sample AWS CloudFormation templates that deploy backup plans, see [AWS CloudFormation templates for backup plans](plan-cfn.md "plan-cfn.md").

## Deploying AWS Backup Audit Manager frameworks and

report plans using AWS CloudFormation

For sample AWS CloudFormation templates that deploy AWS Backup Audit Manager frameworks and report plans,
see [Using AWS Backup Audit Manager with AWS CloudFormation](bam-cfn-integration.md "bam-cfn-integration.md").

## Deploying backup plans across accounts using AWS CloudFormation

You can [use AWS CloudFormation StackSets across multiple accounts in an AWS Organization](https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/ "https://aws.amazon.com/blogs/aws/new-use-aws-cloudformation-stacksets-for-multiple-accounts-in-an-aws-organization/"). Sample
templates are available in the [AWS CloudFormation User
Guide](../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md "../../../AWSCloudFormation/latest/UserGuide/stacksets-sampletemplates.md").

An excellent starting point and reference is the publication [Automate centralized backup at scale across AWS services using AWS Backup](https://aws.amazon.com/blogs/storage/automate-centralized-backup-at-scale-across-aws-services-using-aws-backup/ "https://aws.amazon.com/blogs/storage/automate-centralized-backup-at-scale-across-aws-services-using-aws-backup/"). With Ibukun
Oyewumi and Sabith Venkitachalapathy (Jul. 2021).

## Learning more about AWS CloudFormation

For information about using AWS CloudFormation with AWS Backup, see [AWS Backup Resource Type Reference](../../../AWSCloudFormation/latest/UserGuide/AWS_Backup.md "../../../AWSCloudFormation/latest/UserGuide/AWS_Backup.md") in the
_AWS CloudFormation User Guide_.

For information about controlling access to AWS service resources when using AWS CloudFormation, see
[Controlling Access with AWS Identity and Access Management](../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md "../../../AWSCloudFormation/latest/UserGuide/using-iam-template.md")
in the _AWS CloudFormation User Guide_.
