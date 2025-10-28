# Understanding backup plan summary

The backup plan summary feature provides a comprehensive view of your backup plan configuration to help you validate that your backup strategy meets your requirements. The summary includes three key components that address common customer challenges when managing complex backup configurations across multiple AWS services.

## Summary components

Each backup plan summary contains the following information:

- **Next 10 scheduled backup runs**: Shows when your backup rules will execute, including merged rules and proper timezone handling
- **Feature compatibility notes**: Information about which services support point-in-time recovery (PITR) and cold tier storage
  if these are part of your backup plan rule.

## Scheduled backup runs preview

The scheduled runs preview shows up to 10 future backup executions based on your backup plan rules. This preview helps you understand when backups will occur and how multiple rules interact with each other.

### How multiple rules are merged

When you have multiple backup rules in a plan, AWS Backup applies merging logic to determine the final backup behavior:

- **Overlapping backup windows**:
  It is best practice not to have two rules with conflicting rules.
  When two rules would execute at the same time, AWS Backup selects one.
- **PITR and snapshot combinations**: PITR applies to supported resources, while snapshots apply to all resources in the selection
- **Multiple time zones**: Each rule respects its configured timezone for execution scheduling
- **Cross-region copy actions**:
  Copy actions are preserved and displayed with their destination information.
  Note that if a copy rule is attached to a conflicting schedule rule, the
  copy rule will only run if the schedule rule has run.

###### Example Rule merging example

Consider a backup plan with two rules:

- Rule 1: Daily snapshot at 8am PDT, 35-day retention
- Rule 2: Weekly snapshot at 8am PDT, 90-day retention
  When both rules would execute on the same day (such as Sunday),
  the preview shows Rule 2 because it has longer retention (90 days vs 35 days).

### Execution types

The scheduled runs preview displays different execution types based on your rule configuration:

- `CONTINUOUS`: Continuous backups for supported services
- `SNAPSHOTS`: Snapshot (periodic) backups for all resources in the selection
- `CONTINUOUS_AND_SNAPSHOTS`: Point-in-time-restore (PITR) for
  resource types which support it; snapshot (periodic) for all other resource types.

## Feature compatibility validation

The summary includes compatibility reminders to help you understand which AWS services support advanced backup features. This prevents configuration errors and unexpected costs.

### Point-in-time recovery support

When you enable continuous backups in a rule, the summary reminds you that PITR is only supported for:

- Aurora databases
- Amazon RDS databases
- HANA databases
- Amazon S3 buckets

### Cold tier storage support

When you configure cold tier transitions, the summary shows which services support this feature:

- Amazon DynamoDB tables
- Amazon Elastic File System file systems
- HANA databases
- databases
- virtual machines

## Accessing backup plan summaries

You can view backup plan summaries in the AWS Backup console after creating or updating a backup plan. The summary appears in the plan details page and provides immediate feedback about your configuration.

###### To view a backup plan summary

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/").
2. In the navigation pane, choose **Backup plans**.
3. Choose the backup plan you want to review.
4. The backup plan summary appears in the plan details page. Expand
   the summary to see scheduled runs and compatibility notes.

You can also retrieve backup plan information using the AWS CLI:

```
aws backup get-backup-plan --backup-plan-id 012345678
```
