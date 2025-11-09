# Select an AMS backup plan

AMS provides three different backup plans with a fourth backup plan to minimize cost during onboarding. To select an AMS backup plan for each supported resource, tag the resource with the plan’s associated tag. As you onboard
to Accelerate, AMS will work with you to identify the backup plan that best fits your needs.

###### Important

Do not edit your AMS default backup plans as your changes might be lost. Instead, create new plans for your custom configurations. For more information, see
[Creating a backup plan](../../../aws-backup/latest/devguide/creating-a-backup-plan.md "../../../aws-backup/latest/devguide/creating-a-backup-plan.md").

## Default AMS backup plan

AWS Backup continuous backup is not enabled for this backup plan; for details, see [Restoring to a specified time using point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md").

TAG key: `ams:rt:backup-orchestrator`

TAG value: `true`

| Default AMS backup plan | Start Time                 | Retention |
| ----------------------- | -------------------------- | --------- |
| hourly backup           | N/A                        | N/A       |
| daily backup            | daily 4:00 UTC             | 7 days    |
| weekly backup           | Saturday, 2:00 UTC         | 4 weeks   |
| monthly backup          | 1st of the month, 2:00 UTC | 26 weeks  |
| yearly backup           | Jan 1st, 2:00 UTC          | 2 years   |

## Enhanced backup plan

AWS Backup continuous backup is enabled with maximum retention (31
days) on supported resources; for details, see [Restoring to a specified time
using point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") and [Supported services and applications for point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services "../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services").

TAG key: `ams:rt:backup-orchestrator-enhanced`

TAG value: `true`

| Enhanced backup plan | Start Time                 | Retention   |
| -------------------- | -------------------------- | ----------- |
| hourly backup        | N/A                        | N/A         |
| daily backup         | daily 4:00 UTC             | **31 days** |
| weekly backup        | Saturday, 2:00 UTC         | **6 weeks** |
| monthly backup       | 1st of the month, 2:00 UTC | 26 weeks    |
| yearly backup        | Jan 1st, 2:00 UTC          | 2 years     |

## Data Sensitive backup plan

AWS Backup continuous backup is enabled with maximum retention (31 days) on supported
resources; for details, see [Restoring to a specified time
using point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") and [Supported services and applications for point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services "../../../aws-backup/latest/devguide/point-in-time-recovery.md#point-in-time-recovery-supported-services").

TAG key: `ams:rt:backup-orchestrator-data-sensitive`

TAG value: `true`

| Data Sensitive backup plan | Start Time                 | Retention   |
| -------------------------- | -------------------------- | ----------- |
| hourly backup              | every hour                 | **7 days**  |
| daily backup               | daily 4:00 UTC             | **31 days** |
| weekly backup              | Saturday, 2:00 UTC         | **6 weeks** |
| monthly backup             | 1st of the month, 2:00 UTC | 26 weeks    |
| yearly backup              | Jan 1st, 2:00 UTC          | 2 years     |

## AMS Accelerate onboarding backup plan

AWS Backup continuous backup is not enabled for this backup plan; for details, see
[Restoring to a specified time using point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md").

TAG key: `ams:rt:backup-orchestrator-onboarding`

TAG value: `true`

| AMS Accelerate onboarding backup plan | Start Time | Retention   |
| ------------------------------------- | ---------- | ----------- |
| hourly backup                         | every hour | **2 weeks** |
| daily backup                          | N/A        | N/A         |
| weekly backup                         | N/A        | N/A         |
| monthly backup                        | N/A        | N/A         |
| yearly backup                         | N/A        | N/A         |

**Related AWS Backup Topics**

- [Creating a backup plan](../../../aws-backup/latest/devguide/creating-a-backup-plan.md "../../../aws-backup/latest/devguide/creating-a-backup-plan.md")
- [Point-in-time restore (PITR)](../../../aws-backup/latest/devguide/point-in-time-recovery.md "../../../aws-backup/latest/devguide/point-in-time-recovery.md") enables continuous backups
  of supported resources and allows you to select a specific time for your recovery. For a list of supported resources, see
  [Feature availability by resource](../../../aws-backup/latest/devguide/whatisbackup.md#features-by-resource "../../../aws-backup/latest/devguide/whatisbackup.md#features-by-resource").
