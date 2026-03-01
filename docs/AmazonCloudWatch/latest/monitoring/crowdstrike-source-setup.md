# Source configuration for CrowdStrike

## Integrating with CrowdStrike Falcon

CrowdStrike Falcon Data Replicator (FDR) delivers and enriches endpoint, cloud
workload and identity data with the CrowdStrike Security Cloud and world-class
artificial intelligence (AI), enabling your team to derive actionable insights to
improve security operations center (SOC) performance. Amazon CloudWatch Logs enables you to
collect this data in CloudWatch Logs.

## Instructions to setup Amazon S3 and Amazon SQS

Configuring CrowdStrike FDR to send logs to an Amazon S3 bucket involves several steps,
primarily focused on setting up the Amazon S3 bucket, Amazon SQS queue, IAM roles, and then
configuring the Amazon Telemetry Pipeline.

- Ensure CrowdStrike FDR is enabled within your CrowdStrike Falcon
  environment. This typically requires a specific license and may involve
  working with CrowdStrike support.
- Amazon S3 bucket that stores the CrowdStrike logs should reside in the same
  AWS region where the FDR is enabled.
- Configure the Amazon S3 bucket to create event notifications, specifically for
  "Object Create" events. These notifications should be sent to an Amazon SQS
  queue.
- Create an Amazon SQS queue in the same AWS region as your Amazon S3 bucket. This
  queue will receive notifications when new log files are added to the Amazon S3
  bucket.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read data from CrowdStrike FDR, choose
CrowdStrike as the data source. After filling in the required information and you
create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and the CrowdStrike FDR
actions that maps to Detection Findings (2004) and Process Activity (1007).

### Detection Findings

Detection Findings contains the following actions:

- CloudAssociateTreeIdWithRoot
- CustomIOADomainNameDetectionInfoEvent
- TemplateDetectAnalysis

### Process Activity

Process Activity contains the following actions:

- ActiveDirectoryIncomingPsExecExecution2
- AndroidIntentSentIPC
- AssociateTreeIdWithRoot
- AutoRunProcessInfo
- BamRegAppRunTime
- BlockThreadFailed
- BrowserInjectedThread
- CidMigrationConfirmation
- CodeSigningAltered
- CommandHistory
- CreateProcessArgs
- CreateThreadNoStartImage
- CriticalEnvironmentVariableChanged
- CsUmProcessCrashAuxiliaryEvent
- CsUmProcessCrashSummaryEvent
- CustomIOABasicProcessDetectionInfoEvent
- DebuggableFlagTurnedOn
- DebuggedState
- DllInjection
- DocumentProgramInjectedThread
- EarlyExploitPivotDetect
- EndOfProcess
- EnvironmentVariablesChanged
- FalconProcessHandleOpDetectInfo
- FlashThreadCreateProcess
- IdpWatchdogRemediationActionTaken
- InjectedThread
- InjectedThreadFromUnsignedModule
- IPCDetectInfo
- JavaInjectedThread
- KillProcessError
- LsassHandleFromUnsignedModule
- MacKnowledgeActivityEnd
- MacKnowledgeActivityStart
- NamespaceChanged
- PcaAppLaunchEntry
- PcaGeneralDbEntry
- PrivilegedProcessHandle
- PrivilegedProcessHandleFromUnsignedModule
- ProcessActivitySummary
- ProcessBlocked
- ProcessControl
- ProcessDataUsage
- ProcessExecOnPackedExecutable
- ProcessHandleOpDetectInfo
- ProcessHandleOpDowngraded
- ProcessInjection
- ProcessPatternTelemetry
- ProcessRollup
- ProcessRollup2
- ProcessRollup2Stats
- ProcessSelfDeleted
- ProcessSessionCreated
- ProcessSubstituteUser
- ProcessTokenStolen
- ProcessTrace
- ProcessTreeCompositionPatternTelemetry
- PtTelemetry
- PtyCreated
- QueueApcEtw
- ReflectiveDllOpenProcess
- RegisterRawInputDevicesEtw
- RemediationActionKillProcess
- RemediationMonitorKillProcess
- RuntimeEnvironmentVariable
- ScriptControlDotNetMetadata
- ScriptControlErrorEvent
- ServiceStarted
- SessionPatternTelemetry
- SetThreadCtxEtw
- SetWindowsHook
- SetWindowsHookExEtw
- SetWinEventHookEtw
- ShellCommandLineInfo
- SruApplicationTimelineProvider
- SudoCommandAttempt
- SuspectCreateThreadStack
- SuspendProcessError
- SuspiciousPrivilegedProcessHandle
- SuspiciousUserFontLoad
- SuspiciousUserRemoteAPCAttempt
- SyntheticPR2Stats
- SyntheticProcessRollup2
- SyntheticProcessTrace
- SystemTokenStolen
- TerminateProcess
- ThreadBlocked
- UACAxisElevation
- UACCOMElevation
- UACExeElevation
- UACMSIElevation
- UmppcBypassSuspected
- UnexpectedEnvironmentVariable
- UserAssistAppLaunchInfo
- UserSetProcessBreakOnTermination
- WmiCreateProcess
- WmiFilterConsumerBindingEtw

[Show moreShow less](# "#")
