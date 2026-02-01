# `AWSSupport-ShareEncryptedAMIOrEBSSnapshot`

**Description**

This runbook automates the process of sharing encrypted Amazon Machine Images or Amazon Elastic Block Store snapshots with other Amazon Web Services accounts. This runbook handles the complex requirements for cross-account sharing of encrypted resources, including AWS Key Management Service key policy modifications and resource permission updates.

This automation performs the steps outlined in the AWS Security Blog article [How to share encrypted AMIs across accounts to launch encrypted Amazon Elastic Compute Cloud instances](https://aws.amazon.com/blogs/security/how-to-share-encrypted-amis-across-accounts-to-launch-encrypted-ec2-instances/ "https://aws.amazon.com/blogs/security/how-to-share-encrypted-amis-across-accounts-to-launch-encrypted-ec2-instances/").

###### Important Considerations

- **This runbook will modify your resources**: The runbook will add cross-account permissions to your AWS KMS Customer Managed Key (CMK) policy and grant AMI launch permissions or Amazon EBS snapshot create volume permissions to the destination account.
- **Additional costs may apply**: When copying resources (different region or AWS managed key encryption), additional costs will be incurred for the new AMI or Amazon EBS snapshot and any cross-region data transfer.
- **Please verify the destination account ID**: Double-check the destination account ID as this runbook cannot validate account existence.
- **Automatic rollback with manual verification**: This runbook attempts to automatically roll back changes if it fails. However, if the rollback itself fails, please verify that no extra AMI/Snapshot copies were left in your account, resource LaunchPermission/CreateVolumePermission attributes do not include unintended accounts, and AWS KMS key policy is in its original state.

**How does it work?**

The runbook performs the following high-level steps:

- Validates the input resource existence, state, and encryption configuration
- Checks current resource sharing permissions with the destination account
- Analyzes AWS KMS key policy and creates a comprehensive preview of all required changes
- Requests approval from designated principals before making any changes
- Executes approved changes including resource copying (if needed), permission updates, and AWS KMS key policy modifications
- Provides a comprehensive execution report with rollback information if needed

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ShareEncryptedAMIOrEBSSnapshot "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ShareEncryptedAMIOrEBSSnapshot")

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

The AutomationAssumeRole parameter requires the following actions:

- ec2:DescribeImages
- ec2:DescribeSnapshots
- ec2:DescribeImageAttribute
- ec2:DescribeSnapshotAttribute
- ec2:ModifyImageAttribute
- ec2:ModifySnapshotAttribute
- ec2:CopyImage
- ec2:CopySnapshot
- ec2:DeregisterImage
- ec2:DeleteSnapshot
- kms:DescribeKey
- kms:GetKeyPolicy
- kms:PutKeyPolicy
- kms:CreateGrant
- kms:GenerateDataKey\*
- kms:ReEncrypt\*
- kms:Decrypt
- accessanalyzer:CheckAccessNotGranted

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-ShareEncryptedAMIOrEBSSnapshot`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ShareEncryptedAMIOrEBSSnapshot/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ShareEncryptedAMIOrEBSSnapshot/description") in Systems Manager under Documents.
2. Select Execute automation.
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**

   The Amazon Resource Name of the AWS AWS Identity and Access Management role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
   - **Approvers (Required):**

   The list of AWS authenticated principals who are able to either approve or reject the action. The maximum number of approvers is 10. You can specify principals by using any of the following formats: user name, user ARN, IAM role ARN, or IAM assume role ARN.
   - **ResourceId (Required):**

   AMI or Amazon EBS Snapshot ID to be shared (e.g., ami-123456789012 or snap-123456789012).
   - **DestinationAccountId (Required):**

   The 12-digit AWS account ID where the resource will be shared.
   - **CustomerManagedKeyId (Optional):**

   AWS KMS CMK ID to re-encrypt the resource. Required if the resource is encrypted with AWS managed key or when DestinationRegion is specified for cross-region copying. For cross-region copying, this key must exist in the destination region.
   - **DestinationRegion (Optional):**

   The AWS region where the resource will be copied. The default value is the current region. If a different region is specified, the resource will be copied to the destination region using the AWS KMS CMK specified in the CustomerManagedKeyId parameter.

4. Select Execute.
5. The automation initiates.
6. The document performs the following steps:
   - **`ValidateResources`**:

   Validates input resource existence, state, encryption configuration, and determines required changes for sharing.
   - **`BranchOnResourcePermission`**:

   Branches the workflow based on whether resource sharing permission need to be checked.
   - **`CheckResourcePermission`**:

   Checks if the target account has required sharing permission for the resource.
   - **`AnalyzeChanges`**:

   Analyzes AWS KMS key policy and creates comprehensive preview of all required changes.
   - **`BranchOnChanges`**:

   Branches the workflow based on whether changes require approval.
   - **`GetApproval`**:

   Waits for the approval of designated AWS IAM principals to proceed with required changes.
   - **`ExecuteChanges`**:

   Executes approved changes with rollback on failure.
   - **`Results`**:

   Generates a comprehensive execution report summarizing all actions taken during the encrypted AMI or snapshot sharing process.

7. After completed, review the Outputs section for the detailed results of the execution.

**Required AWS AWS Identity and Access Management Policy for Destination Account**

The IAM role or user in the destination account must configure the following IAM permissions to launch encrypted Amazon EC2 instances from the shared encrypted AMI or to create volumes from the shared encrypted Amazon EBS snapshot:

```

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "kms:DescribeKey",
                    "kms:ReEncrypt*",
                    "kms:CreateGrant",
                    "kms:Decrypt"
                ],
                "Resource": [
                    "arn:aws:kms:<region>:<account-id>:key/<key-id>"
                ]
            }
        ]
    }

```

**References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ShareEncryptedAMIOrEBSSnapshot/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ShareEncryptedAMIOrEBSSnapshot/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
- [Share a AWS KMS key](../../../ebs/latest/userguide/share-kms-key.md "../../../ebs/latest/userguide/share-kms-key.md")
