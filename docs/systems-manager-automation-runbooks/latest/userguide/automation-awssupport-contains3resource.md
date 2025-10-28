# `AWSSupport-ContainS3Resource`

**Description**

The `AWSSupport-ContainS3Resource` runbook provides an automated solution for
the procedure outlined in the article [Support Automation Workflow (SAW)
Runbook: Contain a compromised AWS Amazon S3 Bucket](https://repost.aws/articles/ARhGc0hDqKRIKAVCbmF1GmuQ "https://repost.aws/articles/ARhGc0hDqKRIKAVCbmF1GmuQ")

###### Important

- This runbook performs various operations that require elevated privileges,
  such as modifying Amazon S3 bucket policies, tags, and public access configurations.
  These actions could potentially lead to privilege escalation or impact other
  workloads that depend on the targeted Amazon S3 bucket. You should review the
  permissions granted to the role specified by the
  `AutomationAssumeRole` parameter and ensure they are appropriate
  for the intended use case. You can refer to the following AWS documentation
  for more information on IAM permissions: [`Identity and
 Access Management (IAM) Permissions`](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md")
  [`AWS AWS Systems Manager Automation Permissions`](../../../systems-manager/latest/userguide/automation-setup-iam.md "../../../systems-manager/latest/userguide/automation-setup-iam.md").
- This runbook performs mutative actions that could potentially cause
  unavailability or disruption to your workloads. Specifically, the
  `Contain` action blocks all access to the specified Amazon S3 bucket,
  except for the roles specified in the `SecureRoles` parameter. This
  could impact any applications or services that rely on the targeted Amazon S3
  bucket.
- During the `Contain` action, this runbook may create an additional
  Amazon S3 bucket (specified by the `BackupS3BucketName` parameter) to
  store the backup of the original bucket's configuration, if it does not already
  exist.
- If the `Action` parameter is set to `Restore`, this
  runbook attempts to restore the Amazon S3 bucket's configuration to its original
  state based on the backup stored in the `BackupS3BucketName` bucket.
  However, there is a risk that the restoration process may fail, leaving the Amazon S3
  bucket in an inconsistent state. The runbook provides instructions for manual
  restoration in case of such failures, but you should be prepared to handle
  potential issues during the restoration process.
  It is recommended to review the runbook thoroughly, understand its potential impacts,
  and test it in a non-production environment before executing it in your production
  environment.

**How does it work?**

This runbook operates differently based on the resource type and action:

- For Amazon S3 General Purpose Bucket `Containment`: The automation blocks
  public access to the bucket, disables ACL configuration, enforces Bucket Owner
  Object ownership, and puts a restrictive bucket policy denying all Amazon S3 actions to
  the bucket except for allow listed IAM Roles.
- For Amazon S3 General Purpose Object `Containment`: The automation blocks
  Public Access to bucket, disables ACL configuration, enforces Bucket Owner Object
  ownership, and puts a restrictive bucket policy denying all Amazon S3 actions on the
  object except for allow listed IAM Roles.
- For Amazon S3 Directory Bucket `Containment`: The automation puts a
  restrictive bucket policy denying all Amazon S3 actions to the bucket except for allow
  listed IAM Roles.
- For Amazon S3 General Purpose Bucket `Restore`: The automation restores the
  Block Public Access configuration, Bucket ACL configuration, Bucket Owner Object
  ownership and Bucket Policy to the initial configuration prior to
  containment.
- For Amazon S3 General Purpose Object `Restore`: The automation restores the
  Block Public Access configuration, Bucket ACL configuration, Object ACL
  Configuration, Bucket Owner Object ownership and Bucket Policy to the initial
  configuration prior to containment.
- For Amazon S3 Directory Bucket `Restore`: The automation restores the bucket
  policy to the initial configuration prior to containment.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainS3Resource "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainS3Resource")

**Document Type**

Automation

**Owner**

Amazon

**Platform**

/

**Required IAM Permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the
runbook successfully.

- s3:CreateBucket
- s3:DeleteBucketPolicy
- s3:DeleteObjectTagging
- s3:GetAccountPublicAccessBlock
- s3:GetBucketAcl
- s3:GetBucketLocation
- s3:GetBucketOwnershipControls
- s3:GetBucketPolicy
- s3:GetBucketPolicyStatus
- s3:GetBucketTagging
- s3:GetEncryptionConfiguration
- s3:GetObject
- s3:GetObjectAcl
- s3:GetObjectTagging
- s3:GetReplicationConfiguration
- s3:ListBucket
- s3:PutAccountPublicAccessBlock
- s3:PutBucketACL
- s3:PutBucketOwnershipControls
- s3:PutBucketPolicy
- s3:PutBucketPublicAccessBlock
- s3:PutBucketTagging
- s3:PutBucketVersioning
- s3:PutObject
- s3:PutObjectAcl
- s3express:CreateSession
- s3express:DeleteBucketPolicy
- s3express:GetBucketPolicy
- s3express:PutBucketPolicy
- ssm:DescribeAutomationExecutions
  Here is an example of an IAM policy that grants the necessary permissions for the
  `AutomationAssumeRole`:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3Permissions",
 "Effect": "Allow",
 "Action": [
 "s3:CreateBucket",
 "s3:DeleteBucketPolicy",
 "s3:DeleteObjectTagging",
 "s3:GetAccountPublicAccessBlock",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation",
 "s3:GetBucketOwnershipControls",
 "s3:GetBucketPolicy",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketTagging",
 "s3:GetEncryptionConfiguration",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:GetReplicationConfiguration",
 "s3:ListBucket",
 "s3:PutAccountPublicAccessBlock",
 "s3:PutBucketACL",
 "s3:PutBucketOwnershipControls",
 "s3:PutBucketPolicy",
 "s3:PutBucketPublicAccessBlock",
 "s3:PutBucketTagging",
 "s3:PutBucketVersioning",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3ExpressPermissions",
 "Effect": "Allow",
 "Action": [
 "s3express:CreateSession",
 "s3express:DeleteBucketPolicy",
 "s3express:GetBucketPolicy",
 "s3express:PutBucketPolicy"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSMPermissions",
 "Effect": "Allow",
 "Action": [
 "ssm:DescribeAutomationExecutions"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Instructions**

Follow these steps to configure the automation:

1.  Navigate to [`AWSSupport-ContainS3Resource`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainS3Resource/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainS3Resource/description") in Systems Manager under
    Documents.
2.  Select Execute automation.
3.  For the input parameters, enter the following:
    - **BucketName (Required):**
      - Description: (Required) The name of the Amazon S3 bucket.
      - Type: `AWS::S3::Bucket::Name`

    - **Action (Required):**
      - Description: (Required) Select `Contain` to isolate the
        Amazon S3 resource or `Restore` to try to restore the resource
        configuration to its original state from a previous backup.
      - Type: String
      - Allowed Values: `Contain|Restore`

    - **DryRun (Optional):**
      - Description: (Optional) When set to true, the automation will not
        make any changes to the target Amazon S3 resource, instead it will output
        what it would have attempted to change. Default value: true.
      - Type: Boolean
      - Allowed Values: `true|false`

    - **BucketKeyName (Optional):**
      - Description: (Optional) The key of the Amazon S3 object you want to
        contain or restore. Used during object level containment.
      - Type: String
      - Allowed Pattern:
        `^[a-zA-Z0-9\\.\\-_\\\\!*'()/]{0,1024}$`

    - **BucketRestrictAccess
      (Conditional):**
      - Description: (Conditional) The ARN of the IAM users or roles
        that will be allowed access to the target Amazon S3 resource after
        running the containment actions. This parameter is required when
        `Action` is set to `Contain`.
      - Type: StringList
      - Allowed Pattern:
        `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::[0-9]{12}:(role|user)\\/[\\w+\\/=,.@-]+$`

    - **TagIdentifier (Optional):**
      - Description: (Optional) A tag in the format
        Key=BatchId,Value=78925 that will be added to the resources created
        or modified by this runbook during the containment workflow.
      - Type: String
      - Allowed Pattern:
        `^$|^[Kk][Ee][Yy]=[\\+\\-\\=\\.\\_\\:\\/@a-zA-Z0-9]{1,128},[Vv][Aa][Ll][Uu][Ee]=[\\+\\-\\=\\.\\_\\:\\/@a-zA-Z0-9]{0,128}$`

    - **BackupS3BucketName (Conditional):**
      - Description: (Conditional) The Amazon S3 bucket to backup the target
        resource configuration when the `Action` is set to
        `Contain` or to restore the configuration from when
        the `Action` is set to `Restore`.
      - Type: `AWS::S3::Bucket::Name`

    - **BackupS3KeyName (Conditional):**
      - Description: (Conditional) If `Action` is set to
        `Restore`, this specifies the Amazon S3 key the automation
        will use to try to restore the target resource configuration.
      - Type: String
      - Allowed Pattern:
        `^[a-zA-Z0-9\\.\\-_\\\\!*'()/]{0,1024}$`

    - **BackupS3BucketAccess
      (Conditional):**
      - Description: (Conditional) The ARN of the IAM users or roles
        that will be allowed access to the backup Amazon S3 bucket after running
        the containment actions. This parameter is required when
        `Action` is `Contain`.
      - Type: StringList
      - Allowed Pattern:
        `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::[0-9]{12}:(role|user)\\/[\\w+\\/=,.@-]+$`

    - **AutomationAssumeRole (Optional):**
      - Description: (Optional) The Amazon Resource Name (ARN) of the
        IAM role that allows Systems Manager Automation to perform the actions on
        your behalf.
      - Type: `AWS::IAM::Role::Arn`

4.  Select Execute.
5.  The automation initiates.
6.  The document performs the following steps:
    - **validateRequiredInputs**

    Validates the required automation input parameters based on the Action
    specified.
    - **assertBucketExists**

    Checks if the target Amazon S3 bucket exists and is accessible.
    - **backupBucketPreChecks**

    Checks if the backup Amazon S3 bucket potentially grants public read or write
    access to its objects.
    - **backupTargetBucketMetadata**

    Describes the current configuration of the target Amazon S3 bucket and uploads
    the backup to the specified backup Amazon S3 bucket.
    - **containBucket**

    Performs bucket level operations to contain the target Amazon S3 bucket.
    - **BranchOnActionAndMode**

    Branches the automation based on the input parameters Action and
    DryRun.
    - **RestoreInstanceConfiguration**

    Restores the Amazon S3 bucket configuration from the backup.
    - **containFinalOutput**

    Consolidates containment activity in readable format.
    - **ReportContain**

    Outputs dry run details for the containment actions.
    - **ReportRestore**

    Outputs dry run details for the restoring actions.
    - **ReportRestoreFailure**

    Provides instructions to restore the Amazon S3 bucket original configuration
    during a restore workflow failure scenario.
    - **ReportContainmentFailure**

    Provides instructions to restore the Amazon S3 bucket original configuration
    during a containment workflow failure scenario.
    - **FinalOutput**

    Outputs the details of the containment actions.

7.  After the execution completes, review the Outputs section for the detailed results
    of the execution:

        * **ContainFinalOutput.Output**


        Outputs the details of the containment actions performed by this runbook
         when `DryRun` is set to False.
        * **RestoreFinalOutput.Output**


        Outputs the details of the restore actions performed by this runbook when
         `DryRun` is set to False.
        * **ContainS3ResourceDryRun.Output**


        Outputs the details of the containment actions performed by this runbook
         when `DryRun` is set to True.
        * **RestoreS3ResourceDryRun.Output**


        Outputs the details of the restore actions performed by this runbook when
         `DryRun` is set to True.
        * **ReportContainmentFailure.Output**


        Provides instructions to restore the target Amazon S3 resource original
         configuration during a containment workflow failure scenario.
        * **ReportRestoreFailure.Output**


        Provides instructions to restore the target Amazon S3 resource original
         configuration during a restore workflow failure scenario.

    **References**

Systems Manager Automation

- [Run
  this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainS3Resource/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainS3Resource/description")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
