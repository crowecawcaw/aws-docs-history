# Managing tags for backups in Accelerate

AMS Accelerate manages the backing up of supported resources. For more information about this service offering, see
[Continuity management in AMS Accelerate](acc-backup.md "acc-backup.md").

AMS Accelerate backup management uses tags to identify which resources should be automatically
backed up (and also provides manual backup capabilities). You can use any tag key:value
combination to associate your resources with backup plans. To opt in to automated backups
using the **ams-default-backup-plan** AWS Backup plan, you must apply the following tag
to your supported resources:

| Key                        | Value |
| -------------------------- | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ams:rt:backup-orchestrator | true  | ###### Note During onboarding, AMS Accelerate tags all resources with **ams:rt:backup-orchestrator-onboarding** with value **true** for short interval, short retention snapshots. This is managed by the **ams-onboarding-backup-plan** backup plan. For more information about AMS Accelerate-managed AWS Backup plans, see [Select an AMS backup plan](acc-backup-select-plan.md "acc-backup-select-plan.md"). |
