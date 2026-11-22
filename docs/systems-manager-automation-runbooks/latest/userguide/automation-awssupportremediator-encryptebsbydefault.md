

# `AWSSupportRemediator-EncryptEbsByDefault`

**Description**

Enables Amazon Elastic Block Store (Amazon EBS) encryption by default for the AWS account in the current AWS Region.

This automation remediates findings identified by AWS Well-Architected Agent. It remediates findings from AWS Security Hub CSPM control [EBS default encryption should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-7).

If Amazon EBS encryption by default is already enabled in the current AWS Region, the automation completes successfully without making changes.

When Amazon EBS encryption by default is enabled, Amazon EBS encrypts new volumes and snapshot copies in the Region. Amazon EBS uses the default AWS Key Management Service (AWS KMS) key unless you specify a different AWS KMS key at creation time. This setting applies at the account and Region level and does not modify existing Amazon EBS volumes or snapshots.

After you enable this setting, the launching AWS Identity and Access Management (IAM) principal must have specific permissions on the AWS KMS key. These permissions are `kms:CreateGrant`, `kms:Decrypt`, `kms:DescribeKey`, `kms:GenerateDataKeyWithoutPlaintext`, and `kms:ReEncrypt*`. Without these permissions, new Amazon Elastic Compute Cloud (Amazon EC2) instance launches and Amazon EBS volume attachments fail. The AWS managed `alias/aws/ebs` key automatically grants these permissions for most service-linked roles. This primarily affects accounts using a customer managed AWS KMS key as the default. For more information, see [Amazon EBS encryption by default](https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html).

To revert this change, call the `ec2:DisableEbsEncryptionByDefault` API manually. Disabling the setting does not remove encryption from Amazon EBS volumes or snapshots that Amazon EBS already encrypted under this setting.

**Important considerations**  
You are responsible for reviewing automation actions before they run.
This automation might cause stack drift if the resource is part of an AWS CloudFormation stack.
Access to `AWSSupportRemediator-*` runbooks requires an active Business Support\+, Enterprise Support, or Unified Operations Support plan. For more information, see [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) on the AWS website.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `ec2:EnableEbsEncryptionByDefault`
+ `ec2:GetEbsEncryptionByDefault`

**Document Steps**

1. **validateEbsEncryption** - Checks the current Amazon EBS encryption by default configuration for the account in the current Region and decides whether to enable it.

1. **branchOnChangeRequired** - Branches on whether to enable Amazon EBS encryption by default.

1. **enableEBSEncryption** - Enables Amazon EBS encryption by default for the account in the current Region.

**Outputs**
+ validateEbsEncryption.ChangeRequired: Whether to enable Amazon EBS encryption by default.
+ validateEbsEncryption.ValidationMessage: Information about the validation result.
+ validateEbsEncryption.EbsEncryptionByDefault: The initial Amazon EBS encryption by default status before any changes.
+ enableEBSEncryption.EbsEncryptionByDefault: The final Amazon EBS encryption by default status when the `enableEBSEncryption` step runs.