# Onboarding AWS Backup in Accelerate

To configure backups, you need to create backup policies called _backup plans_. A backup plan specifies which AWS resources
to back up, how frequently they need to be backed up, and the backup retention period. We recommend evaluating your organization's continuity, security, and
compliance requirements to determine what backup plans you need.

**Opt-in**

- Ensure that AWS Backup is enabled for each account, Region, and resource type by following the steps here:

[Getting Started 1: Service Opt-in](../../../aws-backup/latest/devguide/service-opt-in.md "../../../aws-backup/latest/devguide/service-opt-in.md").

Optionally,
[Getting started 2: Create on on-demand backup](../../../aws-backup/latest/devguide/create-on-demand-backup.md "../../../aws-backup/latest/devguide/create-on-demand-backup.md").
**Choose a backup plan**

- To choose a backup plan, see [Select an AMS backup plan](acc-backup-select-plan.md "acc-backup-select-plan.md").
  **Add resources**

Resources are not associated with a backup plan by default. They need to be added to a backup plan.

- To add resources to a backup plan, see [Tag your resources to apply AMS backup plans](acc-backup-assign-plan-resources.md "acc-backup-assign-plan-resources.md").
- To enable backup on all resources using tags, see [Managing tags for backups in Accelerate](acc-tag-req-backup.md "acc-tag-req-backup.md").
