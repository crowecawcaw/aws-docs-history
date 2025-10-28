# `AWSSupport-ContainIAMPrincipal`

**Description**

In the event of a security incident or a suspected compromise of an AWS Identity and Access Management (IAM)
User/Role or AWS Identity Center (IDC) user, swift isolation of the affected identity is
crucial while preserving its configuration for investigation. The
`AWSSupport-ContainIAMPrincipal` runbook provides a structured, reversible
approach to contain compromised IAM or IDC identities, effectively blocking their access
to AWS resources and preventing potential spread of the compromise.

This automated process enables investigation without permanent alteration of the
identity's configuration, allowing for restoration of normal access when deemed appropriate.
The containment process maintains the user or role within IAM or the user within IDC,
while effectively isolating it from all network activities. This isolation prevents the
contained identity resource from communicating with resources inside your Amazon Virtual Private Cloud or
accessing internet resources. The containment is designed to be reversible, allowing for
restoration of normal access when deemed appropriate.

**How does it work?**

The `AWSSupport-ContainIAMPrincipal` runbook implements a comprehensive
containment process for IAM users, roles, and Identity Center users. When executed in
`Contain` mode, it first validates all input parameters and performs security
checks on the specified Amazon S3 bucket. It then gathers detailed information about the target
IAM principal and applies appropriate containment measures based on the principal type.
For IAM users, it disables access keys, removes console access, and attaches a deny
policy. For IAM roles, it attaches a deny policy that revokes permissions for sessions
created before containment. For Identity Center users, it removes permission sets, group
memberships, and applies a deny policy. Throughout the process, the runbook backs up the
original configuration to an Amazon S3 bucket for potential restoration. When executed in
`Restore` mode, it attempts to revert the principal to its pre-containment
state using the backed-up configuration. The runbook includes a `DryRun` option
to preview changes without applying them, and provides comprehensive reporting on both
successful operations and failure scenarios.

###### Important

- **Use of Elevated Privileges:** This SSM
  document performs various operations that require elevated privileges, such as
  modifying IAM and IDC identity policies and applying quarantine
  configurations. These actions could potentially lead to a privilege escalation
  or impact other workloads that depend on the targeted identities. You should
  review the permissions granted to the role specified by the
  `AutomationAssumeRole` parameter and ensure they are appropriate
  for the intended use case. You can refer to the following AWS documentation
  for more information on IAM permissions:
  - [Identity and
    Access Management (IAM) Permissions](../../../IAM/latest/UserGuide/access_permissions.md "../../../IAM/latest/UserGuide/access_permissions.md")
  - [AWS Systems Manager Automation Permissions](../../../systems-manager/latest/userguide/automation-permissions.md "../../../systems-manager/latest/userguide/automation-permissions.md")

- **Workload Unavailability Risks:** This Systems Manager
  document performs isolation actions that could potentially cause unavailability
  or disruption to your workloads. When executed during a security event, it will
  restrict access to the affected resource by revoking AWS API permissions from
  the specified IAM and IDC identities, preventing them from making any AWS
  API calls or actions. This could impact any applications or services that depend
  on these identities.
- **Creation of Additional Resources:** The
  automation document may conditionally create additional resources, such as an
  Amazon Simple Storage Service (Amazon S3) bucket and Amazon S3 objects stored in them, depending on the
  execution parameters. These resources will incur additional charges based on
  your AWS usage.
- **Restoration Risks:** If the
  _Action_ parameter is set to `Restore`, this
  SSM document attempts to restore the IAM or IDC identity configuration to
  its original state. However, there is a risk that the restoration process may
  fail, leaving the IAM or IDC identity in an inconsistent state. The document
  provides instructions for manual restoration in case of such failures, but you
  should be prepared to handle potential issues during the restoration
  process.
  It is recommended to review the runbook thoroughly, understand its potential impacts,
  and test it in a non-production environment before executing it in your production
  environment.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainIAMPrincipal "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainIAMPrincipal")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

/

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following permissions to
successfully use the runbook:

- s3:GetBucketLocation
- s3:GetBucket
- s3:ListBucket
- s3:GetBucketPublicAccessBlocks
- s3:GetAccountPublicAccessBlocks
- s3:GetBucketPolicyStatus
- s3:GetBucketAcl
- s3:GetObject
- s3:CreateBucket
- s3:PutObject
- iam:GetUser
- iam:GetUserPolicy
- iam:GetRole
- iam:ListUserPolicies
- iam:ListAttachedUserPolicies
- iam:ListAccessKeys
- iam:ListMfaDevices
- iam:ListVirtualMFADevices
- iam:GetLoginProfile
- iam:GetPolicy
- iam:GetRolePolicy
- iam:ListPolicies
- iam:ListAttachedRolePolicies
- iam:ListRolePolicies
- iam:UpdateAccessKey
- iam:CreateAccessKey
- iam:DeleteLoginProfile
- iam:DeleteAccessKey
- iam:PutUserPolicy
- iam:DeleteUserPolicy
- iam:DeactivateMFADevice
- iam:AttachRolePolicy
- iam:AttachUserPolicy
- iam:DeleteRolePolicy
- iam:TagMFADevice
- iam:PutRolePolicy
- iam:TagPolicy
- iam:TagRole
- iam:TagUser
- iam:UntagUser
- iam:UntagRole
- organizations:ListAccounts
- sso:ListPermissionSetsProvisionedToAccount
- sso:GetInlinePolicyForPermissionSet
- sso:ListInstances
- sso-directory:SearchUsers
- sso:ListPermissionSets
- sso:ListAccountAssignments
- sso-directory:DescribeUser
- identitystore:ListUsers
- identitystore:ListGroups
- identitystore:IsMemberInGroups
- identitystore:ListGroupMemberships
- secretsmanager:CreateSecret
- secretsmanager:DeleteSecret
- sso:DeleteAccountAssignment
- sso:PutInlinePolicyToPermissionSet
- sso:CreateAccountAssignment
- sso:DeleteInlinePolicyFromPermissionSet
- sso:TagResource
- sso:UntagResource
- identitystore:DeleteGroupMembership
- identitystore:CreateGroupMembership
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
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:GetBucketPublicAccessBlock",
 "s3:GetBucketPolicyStatus",
 "s3:GetBucketAcl",
 "s3:GetObject",
 "s3:CreateBucket",
 "s3:PutObject"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IAMPermissions",
 "Effect": "Allow",
 "Action": [
 "iam:GetUser",
 "iam:GetUserPolicy",
 "iam:GetRole",
 "iam:ListUserPolicies",
 "iam:ListAttachedUserPolicies",
 "iam:ListAccessKeys",
 "iam:ListMfaDevices",
 "iam:ListVirtualMFADevices",
 "iam:GetLoginProfile",
 "iam:GetPolicy",
 "iam:GetRolePolicy",
 "iam:ListPolicies",
 "iam:ListAttachedRolePolicies",
 "iam:ListRolePolicies",
 "iam:UpdateAccessKey",
 "iam:CreateAccessKey",
 "iam:DeleteLoginProfile",
 "iam:DeleteAccessKey",
 "iam:PutUserPolicy",
 "iam:DeleteUserPolicy",
 "iam:DeactivateMFADevice",
 "iam:AttachRolePolicy",
 "iam:AttachUserPolicy",
 "iam:DeleteRolePolicy",
 "iam:TagMFADevice",
 "iam:PutRolePolicy",
 "iam:TagPolicy",
 "iam:TagRole",
 "iam:TagUser",
 "iam:UntagUser",
 "iam:UntagRole"
 ],
 "Resource": "*"
 },
 {
 "Sid": "OrganizationsPermissions",
 "Effect": "Allow",
 "Action": [
 "organizations:ListAccounts"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SSOPermissions",
 "Effect": "Allow",
 "Action": [
 "sso:ListPermissionSetsProvisionedToAccount",
 "sso:GetInlinePolicyForPermissionSet",
 "sso:ListInstances",
 "sso-directory:SearchUsers",
 "sso:ListPermissionSets",
 "sso:ListAccountAssignments",
 "sso-directory:DescribeUser",
 "sso:DeleteAccountAssignment",
 "sso:PutInlinePolicyToPermissionSet",
 "sso:CreateAccountAssignment",
 "sso:DeleteInlinePolicyFromPermissionSet",
 "sso:TagResource",
 "sso:UntagResource"
 ],
 "Resource": "*"
 },
 {
 "Sid": "IdentityStorePermissions",
 "Effect": "Allow",
 "Action": [
 "identitystore:ListUsers",
 "identitystore:ListGroups",
 "identitystore:IsMemberInGroups",
 "identitystore:ListGroupMemberships",
 "identitystore:DeleteGroupMembership",
 "identitystore:CreateGroupMembership"
 ],
 "Resource": "*"
 },
 {
 "Sid": "SecretsManagerPermissions",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:CreateSecret",
 "secretsmanager:DeleteSecret"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to the [AWSSupport-ContainIAMPrincipal](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainIAMPrincipal/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ContainIAMPrincipal/description") in the AWS Systems Manager console.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Description: (Optional) The Amazon Resource Name (ARN) of the
       AWS Identity and Access Management (IAM) role that allows Systems Manager
       Automation to perform the actions on your behalf. If no role is
       specified, Systems Manager Automation uses the permissions of the user who
       starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **PrincipalType (Required):**
     - Description: (Required) The AWS IAM principal type: IAM
       user, IAM role, or Identity Center user.
     - Type: String
     - Allowed Values: `IAM user|IAM role|Identity Center
user`

   - **PrincipalName (Required):**
     - Description: (Required) The name of the IAM principal. For
       Identity Center users, provide the username.
     - Type: String
     - Allowed Pattern:
       `^[a-zA-Z0-9\\.\\-_\\\\!*'()/+=,@]{1,1024}$`

   - **Action (Required):**
     - Description: (Required) Select `Contain` to isolate the
       target IAM principal or `Restore` to try to restore the
       IAM principal to its original configuration from a previous
       backup.
     - Type: String
     - Allowed Values: `Contain|Restore`

   - **DryRun (Optional):**
     - Description: (Optional) When set to `true`, the
       automation will not make any changes to the target IAM principal,
       instead it will output on what it would have attempted to change,
       detailing out on each step. Default value: `true`.
     - Type: Boolean
     - Allowed Values: `true|false`

   - **ActivateDisabledKeys
     (Conditional):**
     - Description: (Conditional) If the input parameter Action is set to
       `Restore` and the PrincipalType is set to IAM user,
       this option determines if this automation should try to activate the
       associated access keys if deactivated. Please note that the
       integrity of a compromised access key cannot be verified. AWS
       strongly recommends against reactivating a compromised key. Instead,
       it is advisable to generate new keys. Default value:
       `false`.
     - Type: Boolean
     - Allowed Values: `true|false`

   - **BackupS3BucketName (Conditional):**
     - Description: (Conditional) The Amazon Amazon S3 bucket to backup the
       IAM principal configuration when the Action is set to
       `Contain` or to restore the configuration from when
       the Action is `Restore`. Note that if the specified
       Action is `Contain` and the runbook is not able to access
       the bucket or a value is not provided, a new bucket is created in
       your account with the name
       `awssupport-containiamprincipal-<random-string>`.
       If DryRun is set to `true` this parameter is
       required.
     - Type: `AWS::S3::Bucket::Name`

   - **BackupS3KeyName (Conditional):**
     - Description: (Conditional) If Action is set to
       `Restore`, this specifies the Amazon Amazon S3 key the
       automation will use to try to restore the IAM principal
       configuration. The Amazon Amazon S3 key typically follows this format:
       `{year}/{month}/{day}/{hour}/{minute}/{automation_execution_id}.json`.
       The key can be obtained from the output of a previous containment
       automation execution.
     - Type: String
     - Allowed Pattern:
       `^[a-zA-Z0-9\\.\\-_\\\\!*'()/]{0,1024}$`

   - **BackupS3BucketAccess
     (Conditional):**
     - Description: (Conditional) The ARN of the IAM users or roles
       that will be allowed access to the backup Amazon Amazon S3 bucket after
       running the containment actions. This parameter is required when
       Action is `Contain`. The AutomationAssumeRole, or in its
       absence the user under whose context the automation is running is
       automatically added to the list.
     - Type: StringList
     - Allowed Pattern:
       `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::[0-9]{12}:(role|user)\\/[\\w+\\/=,.@-]+$`

   - **TagIdentifier (Optional):**
     - Description: (Optional) Tag the IAM principal with a tag of your
       choice using the following format:
       `Key=<EXAMPLE_KEY>,Value=<EXAMPLE_VALUE>`.
       This option allows you to track the IAM principals that have been
       targeted by this runbook. **Note:** Tag
       keys and values are case-sensitive.
     - Type: String
     - Allowed Pattern:
       `^$|^[Kk][Ee][Yy]=[\\+\\-\\=\\.\\_\\:\\/@a-zA-Z0-9]{1,128},[Vv][Aa][Ll][Uu][Ee]=[\\+\\-\\=\\.\\_\\:\\/@a-zA-Z0-9]{0,128}$`

4. Select Execute.
5. The automation initiates.
6. The document performs the following steps:
   - **ValidateRequiredInputs**

   Validates the required automation input parameters based on the
   `Action` specified.
   - **CheckBackupS3BucketName**

   Checks if the target Amazon Amazon S3 bucket potentially grants
   `read` or `write` public access to its objects. In
   case of containment workflow, a new Amazon Amazon S3 bucket is created if the
   `BackupS3BucketName` bucket doesn't exist.
   - **BranchOnAction**

   Branches the automation based on the value of the specified
   `Action`.
   - **BranchOnPrincipalTypeAndDryRun**

   Branches the automation based on the type of IAM principal (IAM user,
   IAM role, or Identity Center user) and if it is running in
   `DryRun` mode.
   - **BranchOnPrincipalTypeForContain**

   Branches the automation for the `Contain` action based and the
   IAM principal type (IAM user, IAM role, or Identity Center user)
   specified in the input.
   - **GetIAMUser**

   Gets the creation time and username of the target IAM user.
   - **GetIAMUserDetails**

   Gets and stores the configuration of the target IAM user, including
   inline policies, managed policies, access keys, MFA devices, and login
   profile.
   - **UpdateS3KeyForUser**

   Updates the automation 'S3Key' variable from output of the step
   `GetIAMUserDetails`.
   - **GetIAMRole**

   Gets the creation time, role name, and path of the target IAM
   role.
   - **GetIAMRoleDetails**

   Gets and stores the configuration of the target IAM role, including
   inline policies and managed policies attached to the role.
   - **UpdateS3KeyForRole**

   Updates the automation 'S3Key' variable from output of the step
   `GetIAMRoleDetails`.
   - **GetIdentityStoreId**

   Gets the ID of the AWS IAM Identity Center instance associated with
   the AWS account.
   - **GetIDCUser**

   Gets the user ID of the target Identity Center user using the Identity
   Store ID.
   - **GatherIDCUserDetails**

   Gets and stores the configuration of the target Identity Center user,
   including account assignments, associated permission sets, and inline
   policies.
   - **UpdateS3KeyForIDCUser**

   Updates the automation 'S3Key' variable from output of the step
   `GatherIDCUserDetails`.
   - **BranchOnIdentityContain**

   Branches the automation based on the value of `DryRun` and the
   IAM principal type for the `Contain` action.
   - **BranchOnDisableAccessKeys**

   Branches the automation based on whether the IAM user has access keys
   that need to be disabled.
   - **DisableAccessKeys**

   Disables the active IAM user access keys.
   - **BranchOnDisableConsoleAccess**

   Branches based on whether the IAM user has AWS Management Console
   access enabled or not.
   - **DisableConsoleAccess**

   Removes the IAM user's password-based access to the AWS Management
   Console.
   - **AttachInlineDenyPolicyToUser**

   Attaches a deny policy to the IAM user to revoke permissions for older
   session tokens.
   - **AttachInlineDenyPolicyToRole**

   Attaches a deny policy to the IAM role to revoke permissions for older
   session tokens.
   - **RemovePermissionSets**

   Removes permission sets associated with the Identity Center user.
   - **RemoveIDCUserFromIDCGroups**

   Removes the Identity Center user from Identity Center groups.
   - **AttachInlineDenyPolicyToPermissionSet**

   Attaches a deny policy to the permission sets associated with the Identity
   Center user.
   - **BranchOnReactivateKeys**

   Branches the automation based on the `ActivateDisabledKeys`
   parameter during the restore process.
   - **DetachInlineDenyPolicy**

   Removes the deny policy attached to the IAM role during the containment
   process.
   - **DetachInlineDenyPolicyFromPermissionSet**

   Removes the deny policy attached to the permission sets during the
   containment process.
   - **ReportContain**

   Outputs detailed information about the containment actions that would be
   performed when `DryRun` is set to `True`.
   - **ReportRestore**

   Outputs detailed information about the restoration actions that would be
   performed when `DryRun` is set to `True`.
   - **ReportContainFailure**

   Provides comprehensive instructions to manually restore the IAM
   principal's original configuration during a containment workflow failure
   scenario.
   - **ReportRestoreFailure**

   Provides detailed instructions to manually complete the restoration of the
   IAM principal's original configuration during a restore workflow failure
   scenario.

7. After the execution completes, review the Outputs section for the detailed results
   of the execution:
   - **ContainIAMPrincipal.Output**

   Provides detailed information about the containment actions performed when
   Action is set to Contain and DryRun is set to False. Includes information
   about the backup location, applied deny policies, and modified
   configurations.
   - **RestoreIAMPrincipal.Output**

   Provides detailed information about the restoration actions performed when
   Action is set to Restore and DryRun is set to False. Includes information
   about the restored configurations and any issues encountered during
   restoration.
   - **ReportContain.Output**

   Outputs detailed information about the containment actions that would be
   performed when Action is set to Contain and DryRun is set to True. Includes
   a comparison of current and post-containment configurations.
   - **ReportRestore.Output**

   Outputs detailed information about the restoration actions that would be
   performed when Action is set to Restore and DryRun is set to True. Shows the
   current configuration and the original configuration that would be
   restored.
   - **ReportContainFailure.Output**

   Provides comprehensive instructions to manually restore the IAM
   principal's original configuration during a containment workflow failure
   scenario.
   - **ReportRestoreFailure.Output**

   Provides detailed instructions to manually complete the restoration of the
   IAM principal's original configuration during a restore workflow failure
   scenario.

**Outputs**

After the execution completes, review the Outputs section for the detailed results:

- **ContainIAMPrincipal.Output**

Provides detailed information about the containment actions performed when Action
is set to Contain and DryRun is set to False. Includes information about the backup
location, applied deny policies, and modified configurations.

- **RestoreIAMPrincipal.Output**

Provides detailed information about the restoration actions performed when Action
is set to Restore and DryRun is set to False. Includes information about the
restored configurations and any issues encountered during restoration.

- **ReportContain.Output**

Outputs detailed information about the containment actions that would be performed
when Action is set to Contain and DryRun is set to True. Includes a comparison of
current and post-containment configurations.

- **ReportRestore.Output**

Outputs detailed information about the restoration actions that would be performed
when Action is set to Restore and DryRun is set to True. Shows the current
configuration and the original configuration that would be restored.

- **ReportContainFailure.Output**

Provides comprehensive instructions to manually restore the IAM principal's
original configuration during a containment workflow failure scenario.

- **ReportRestoreFailure.Output**

Provides detailed instructions to manually complete the restoration of the IAM
principal's original configuration during a restore workflow failure
scenario.

**References**

Systems Manager Automation

- [Run this
  Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainIAMPrincipal "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ContainIAMPrincipal")
- [Running a simple automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
