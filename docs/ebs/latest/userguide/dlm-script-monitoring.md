# Monitor Amazon Data Lifecycle Manager pre and post scripts

###### Amazon CloudWatch metrics

Amazon Data Lifecycle Manager publishes the following CloudWatch metrics when pre and post scripts fail and succeed and when VSS
backups fail and succeed.

- `PreScriptStarted`
- `PreScriptCompleted`
- `PreScriptFailed`
- `PostScriptStarted`
- `PostScriptCompleted`
- `PostScriptFailed`
- `VSSBackupStarted`
- `VSSBackupCompleted`
- `VSSBackupFailed`
  For more information, see [Monitor Data Lifecycle Manager policies using CloudWatch](monitor-dlm-cw-metrics.md "monitor-dlm-cw-metrics.md").

###### Amazon EventBridge

Amazon Data Lifecycle Manager emits the following Amazon EventBridge event when a pre or post script is initiated, succeeds, or fails

- `DLM Pre Post Script Notification`
  For more information, see [Monitor Data Lifecycle Manager policies using EventBridge](monitor-cloudwatch-events.md "monitor-cloudwatch-events.md").
