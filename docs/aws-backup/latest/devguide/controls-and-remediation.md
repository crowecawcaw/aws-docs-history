# Controls and remediation

This page lists the available controls for AWS Backup Audit Manager. You can choose the right
info pane to see a list of controls and jump to a specific control. To quickly compare
controls, see the table in [Choosing your controls](choosing-controls.md "choosing-controls.md"). To
programmatically define controls, see the code snippets in [Creating frameworks using the
AWS Backup API](creating-frameworks-api.md "creating-frameworks-api.md").

You can use up to 50 controls per account per Region. Using the same control in two
different frameworks counts as using two controls of the 50 control limit.

This page lists each control with the following information:

- Description. Values in brackets ("[ ]") are the default parameter
  values.
- The **resource(s)** the control evaluates.
- The **parameters** of the control.
- Occasion when running of control **occurs**.
- The **scope** of the control, as follows:
  - You can specify **Resources by type** by choosing one or more
    AWS Backup-supported services.
  - You specify a **Tagged resources** scope with a single tag key
    and optional value.
  - You can specify a single resource using the **Single
    resource** dropdown list.

- Remediation steps to bring applicable resources into compliance.
  Note that only active resources will be included
  when controls evaluate resources for compliance. For example, an Amazon EC2 instance in a running state
  will be evaluated by the control
  [Last recovery point was created](controls-and-remediation.md#last-recovery-point-created-control "controls-and-remediation.md#last-recovery-point-created-control"). An EC2 instance in a stopped state will not be
  included in the compliance evaluation.

## Backup resources are included in at least one backup plan

**Description**: Evaluates if resources are included in at
least one backup plan.

**Resource**: `AWS Backup: backup selection`

**Parameters**: None

**Occurs**: Automatically every 24 hours

###### Scope:

- Tagged resources
- Resources by type (default)
- Single resource

**Remediation**: Assign the resources to a backup plan.
AWS Backup automatically protects your resources after you assign them to a backup plan. For more
information, see [Assigning resources to a backup
plan](assigning-resources.md "assigning-resources.md").

## Backup plan minimum frequency and minimum retention

**Description**: Evaluates if backup plans contain at least
one backup rule for which the backup frequency is at least [1 day] and retention period is
at least [35 days].

**Resource**: `AWS Backup: backup plans`

###### Parameters:

- Required backup frequency in number of hours or days.
- Required retention period in number of days, weeks, months, or years. We recommend a
  warm storage retention of period of at least one week to enable AWS Backup to take
  incremental backups when possible, avoiding additional charges.

**Occurs**: Configuration changes

###### Scope:

- Tagged resources
- Single resource

**Remediation**: [Update a backup plan](updating-a-backup-plan.md "updating-a-backup-plan.md") to
change either its backup frequency, retention period, or both. Updating your backup plan
changes the retention period for recovery points the plan creates after your update.

## Vaults prevent manual deletion of recovery points

**Description**: Evaluates if backup vaults do not allow
manual deletion of recovery points except by certain IAM roles.

**Resource**: `AWS Backup: backup vaults`

**Parameters**: The Amazon Resource Names (ARNs) of up to
five IAM roles allowed to manually delete recovery points.

**Occurs**: Configuration changes

###### Scope:

- Tagged resources
- Single resource

**Remediation**: Create or modify a resource-based access
policy on a backup vault. For an example policy and instructions on how to set a backup
vault access policy, see [Deny access to delete recovery points in a backup vault](create-a-vault-access-policy.md#deny-access-to-delete-recovery-points "create-a-vault-access-policy.md#deny-access-to-delete-recovery-points").

## Recovery points are encrypted

**Description**: Evaluates if recovery points are
encrypted.

**Resource**: `AWS Backup: recovery points`

**Parameters**: None

**Occurs**: Configuration changes

###### Scope:

- Tagged resources

**Remediation**: Configure encryption for the recovery
points. The way you configure encryption for AWS Backup recovery points differs depending on the
resource type.

You can configure encryption for resource types that support full AWS Backup management in
using AWS Backup. If the resource type does not support full AWS Backup management, you must configure
its backup encryption by following that service's instructions, such as [Amazon EBS
encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the _Amazon Elastic Compute Cloud User Guide_. To see the list of
resource types that support full AWS Backup management, see the "Full AWS Backup management" section
of the [Feature availability by resource](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource")
table.

## Minimum retention established for recovery point

**Description**: Evaluates if recovery point retention
period is at least [35 days].

**Resource**: `AWS Backup: recovery points`

**Parameters**: Required recovery point retention period in
number of days, weeks, months, or years. We recommend a warm storage retention of period of
at least one week to enable AWS Backup to take incremental backups when possible, avoiding
additional charges.

**Occurs**: Configuration changes

###### Scope:

- Tagged resources

**Remediation**: Change the retention periods of your
recovery points. For more information, see [Editing a backup](editing-a-backup.md "editing-a-backup.md").

## Cross-Region backup copy is scheduled

**Description**: Evaluates if a resource is configured to create copies of its backups to another AWS Region.

**Resource**: `AWS Backup: backup selection`

###### Parameters:

- Select the AWS Region(s) where the backup copy should exist (Optional)
- Region

**Occurs**: Automatically every 24 hours

###### Scope:

- Tagged resources
- Resources by type
- Single resource

**Remediation**: [Update a backup plan](updating-a-backup-plan.md "updating-a-backup-plan.md")
to change the AWS Region where backup copy should exist.

## Cross-account backup copy is scheduled

**Description**: Evaluates if a resource is configured to create
copies of its backups to another account. You can add up to 5 accounts for the control to evaluate.
The destination account must be in the same organization as the source account in AWS Organizations.

**Resource**: `AWS Backup: backup selection`

###### Parameters:

- Select the AWS account ID(s) where the backup copy should exist (Optional)
- Account ID

**Occurs**: Automatically every 24 hours

###### Scope:

- Tagged resources
- Resources by type
- Single resource

**Remediation**: [Update a backup plan](updating-a-backup-plan.md "updating-a-backup-plan.md")
to change or add the AWS account ID(s) where the copy should exist.

## Resources are in a backup plan with an AWS Backup Vault Lock

**Description**: Evaluates if a resource has immutable backups stored
in a locked backup vault.

**Resource**: `AWS Backup: backup selection`

###### Parameters:

- Input the minimum and maximum retention days for AWS Backup Vault Lock (optional)
- Minimum retention days
- Maximum retention days

**Occurs**: Automatically every 24 hours

###### Scope:

- Tagged resources
- Resources by type
- Single resource

**Remediation**: [Lock a backup vault](vault-lock.md#lock-backup-vault-cli "vault-lock.md#lock-backup-vault-cli")
to set its name, change either its minimum retention days, maximum retention days, or both.
Can also include `ChangeableForDays` for a vault lock in compliance mode.

## Last recovery point was created

**Description**: This control evaluates if a recovery point
has been created within the specified time frame (in days or hours).

The control is compliant if the resource has had a recovery point created within the
time frame specified. The control is non-compliant if a recovery point was not created
within the number of days or hours specified.

**Resource**: `AWS Backup: recovery points`

###### Parameters:

- Input the specified time frame in whole numbers, either in hours or days.
- Values of `hours` can range from `1` to `744`.
- Value of `days` can range from `1` to `31`.

**Occurs**: Automatically every 24 hours

###### Scope:

- Tagged resources
- Resources by type
- Single resource

**Remediation**:

- [Update a backup plan](updating-a-backup-plan.md "updating-a-backup-plan.md")
  to change the specified time frame of recovery point creation.
- Additionally, you can create an on-demand backup.

## Restore time for resources meet target

**Description**: Evaluates if restoring protected resources
completed within the target restore time.

This control checks if the restore time of a particular resource meets the target
duration. The rule is NON_COMPLIANT if `LatestRestoreExecutionTimeMinutes` of
a resource type is
greater than `maxRestoreTime` in minutes.

###### Parameters:

- `maxRestoreTime` (in minutes)

**Occurs**: Automatically every 24 hours

###### Scope:

- Tagged resources
- Resources by type
- Single resource

###### Note

AWS Backup does not provide any service-level agreements (SLAs) for a restore time.
Restore times can vary based upon system load and capacity, even
for restores containing the same resources.

## Resources in a logically air-gapped vault

**Description**: This control evaluates if resources have at least one
recovery point copied to a logically air-gapped vault within the specified value and time
frame. This control is NON_COMPLIANT if a recovery point has not been copied to a logically
air-gapped vault in the time frame configured for the control.

**Resource**: `AWS Backup: recovery points`

###### Parameters:

- `recoveryPointAgeValue`
- `recoveryPointAgeUnit`

Input the time period. Specify the unit in `days` or `hours`.
Specify a value for that unit. Values of hours can be within `24` to
`2184` inclusive. Values of days can be within `1` to
`91` inclusive.

A minimum value of `7` days or `168` hours is recommended. The
control value should be no more frequent than the copy creation frequency of your backup
plan; otherwise, you may see an unexpected `NON_COMPLIANT` status until your next backup is
copied into a logically air-gapped vault and this control is run.

**Occurs**: Automatically every 24 hours

###### Scope:

- Resources by type
- Single resource
