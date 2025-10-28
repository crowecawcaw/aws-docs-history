# Remediating exposures for DynamoDB tables

AWS Security Hub can generate exposure findings for DynamoDB tables.

On the Security Hub console, the DynamoDB table involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details.
Programmatically, you can retrieve resource details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

###### Contents

- [Misconfiguration traits in DynamoDB](exposure-ddb-instance.md#misconfiguration "exposure-ddb-instance.md#misconfiguration")
  - [The DynamoDB table has point-in-time recovery disabled](exposure-ddb-instance.md#point-in-time-recovery-disabled "exposure-ddb-instance.md#point-in-time-recovery-disabled")
  - [The DynamoDB table is not covered by a backup plan](exposure-ddb-instance.md#backup-plan "exposure-ddb-instance.md#backup-plan")
  - [The DynamoDB table has deletion protection disabled](exposure-ddb-instance.md#deletion-protection-disabled "exposure-ddb-instance.md#deletion-protection-disabled")

## Misconfiguration traits in DynamoDB

The following describes the misconfiguration traits and remediation steps for DynamoDB tables.

### The DynamoDB table has point-in-time recovery disabled

######

Enable DynamoDB point-in-time recovery

DynamoDB point-in-time recovery provides continuous automated backups for your DynamoDB table data.
For information about how to restore a DynamoDB table to a point in time, see [Restoring a DynamoDB table to a point in time](../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md "../../../amazondynamodb/latest/developerguide/PointInTimeRecovery.md") in the _Amazon DynamoDB User Guide_.

###

The DynamoDB table is not covered by a backup plan

AWS Backup provides a centralized service to configure, manage, and automate backups across AWS services, including DynamoDB.
Without a backup plan, your table lacks scheduled, automated backups with customizable retention periods, creating significant security risks.
An attacker could maliciously corrupt or delete your table data. Without proper backups, you may have no recovery option beyond the Point-in-Time Recovery window (if enabled), potentially resulting in permanent data loss.
Following data protection best practices, we recommend covering your DynamoDB tables with a backup plan.

###### Create a backup plan

Before creating a backup plan, determine an appropriate backup frequency and retention periods for your data.
For information about how to create a backup plan, see [Assign resources to a backup plan](../../../aws-backup/latest/devguide/assigning-resources.md "../../../aws-backup/latest/devguide/assigning-resources.md") in the _Amazon DynamoDB User Guide_.

###

The DynamoDB table has deletion protection disabled

Deletion protection prevents the accidental deletion of DynamoDB tables.
When deletion protection is disabled, DynamoDB tables are vulnerable to unintended deletion through console actions, API calls, CLI commands, or automated processes.
This can expose your AWS environment to data loss, as an unauthorized entity with access to your AWS environment could intentionally delete tables, resulting in service disruption and permanent data loss.
Following data protection best practices, we recommend enabling data protection for DynamoDB tables.

###### Enable deletion protection

If you manage multiple tables, consider using AWS CloudFormation to update table properties in bulk.
You can modify your AWS CloudFormation templates to include `DeletionProtectionEnabled` property and update your stacks.

After completing remediation, verify deletion protection is enabled in the **Additional** info dropdown in the table **Settings** tab.
