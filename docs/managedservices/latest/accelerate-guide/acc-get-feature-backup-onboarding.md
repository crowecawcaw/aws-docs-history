

# Onboarding AWS Backup in Accelerate
<a name="acc-get-feature-backup-onboarding"></a>

To configure backups, you need to create backup policies called *backup plans*. A backup plan specifies which AWS resources to back up, how frequently they need to be backed up, and the backup retention period. We recommend evaluating your organization's continuity, security, and compliance requirements to determine what backup plans you need. 

**Opt-in**
+ Ensure that AWS Backup is enabled for each account, Region, and resource type by following the steps here:

  [Getting Started 1: Service Opt-in](https://docs.aws.amazon.com/aws-backup/latest/devguide/service-opt-in.html).

  Optionally, [Getting started 2: Create on on-demand backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/create-on-demand-backup.html).

**Choose a backup plan**
+ To choose a backup plan, see [Select an AMS backup plan](acc-backup-select-plan.md).

**Add resources**

Resources are not associated with a backup plan by default. They need to be added to a backup plan.
+ To add resources to a backup plan, see [Tag your resources to apply AMS backup plans](acc-backup-assign-plan-resources.md).
+ To enable backup on all resources using tags, see [Managing tags for backups in Accelerate](acc-tag-req-backup.md).