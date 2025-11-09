# `AWSSupport-TroubleshootCloudWatchAlarm`

**Description**

The `AWSSupport-TroubleshootCloudWatchAlarm` runbook helps identify and
troubleshoot issues with misconfigured or problematic Amazon CloudWatch (CloudWatch) Alarms. It leverages
public AWS APIs and known alarm evaluation logic to detect delayed or missing datapoints
in the monitored metrics, which can lead to missed or delayed alarm actions. This runbook
provides a structured approach to investigate and resolve Amazon CloudWatch (CloudWatch) Alarm-related
problems.

**How does it work?**

The runbook `AWSSupport-TroubleshootCloudWatchAlarm` performs the following
steps:

- Verifies the Amazon CloudWatch (CloudWatch) alarm details and the value of the
  `AlarmTriggerTimestamp` parameter to check if it's within 2,592,000
  seconds (30 days).
- Checks if an alarm is based on a Metric or Metric Math or is an Anomaly Detector
  Alarm.
- Checks if an alarm is in insufficient data sate.
- Checks if the metric(s) used in the alarm matches with `ListMetrics`
  value.
- Verifies if a metric was missing datapoint(s) at a given timestamp.
- Gets the most recent history for a given timestamp.
- Checks if an alarm did not trigger due to a delayed or missed metric(s).
- Checks if an alarm's enabled action(s) was/were delivered.
- Generates a troubleshooting report combining all diagnostic results.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCloudWatchAlarm "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-TroubleshootCloudWatchAlarm")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `cloudwatch:DescribeAlarms`
- `cloudwatch:DescribeAlarmHistory`
- `cloudwatch:DescribeAnomalyDetectors`
- `cloudwatch:GetMetricData`
- `cloudwatch:GetMetricStatistics`
- `cloudwatch:ListMetrics`

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:DescribeAlarms",
 "cloudwatch:DescribeAlarmHistory",
 "cloudwatch:DescribeAnomalyDetectors",
 "cloudwatch:GetMetricData",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:ListMetrics"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-TroubleshootCloudWatchAlarm`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAlarm/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAlarm/description") in Systems Manager under
   Documents.
2. Select Execute automation.
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Optional):**
     - Type: `String`
     - Description: (Optional) The Amazon Resource Name (ARN) of the
       AWS AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform
       the actions on your behalf. If no role is specified, Systems Manager
       Automation uses the permissions of the user who starts this
       runbook.

   - **CloudWatchMetricAlarmName
     (Required):**
     - Type: `String`
     - Description: (Required) The name of the Amazon CloudWatch (CloudWatch) metric
       Alarm to troubleshoot.
     - Allowed Pattern: `^[a-zA-Z0-9.:;,\\-_&()
]{1,255}$`

   - **AlarmTriggerTimestamp (Required):**
     - Type: `String`
     - Description: (Required) The UTC timestamp when the Alarm issue
       occurred. This information is crucial for troubleshooting the issue
       and understanding the context in which it happened. The timestamp
       value should be a time within the last 30 days from today and in the
       format `YYYY-MM-DDTHH:mm:ssZ`. Example:
       `2024-10-29T09:04:00Z`
     - Allowed Pattern:
       `^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2}):(\\d{2})Z$`

4. Select Execute.
5. The automation initiates.
6. The document performs the following steps:
   - **`VerifyRunbookInputs`**

   Verifies the Amazon CloudWatch (CloudWatch) alarm details and the value of the
   `AlarmTriggerTimestamp` parameter to check if it's within
   2,592,000 seconds (30 days).
   - **`UpdateSSMDocumentInputChecksVariable`**

   Updates the variable `SSMDocumentInputChecks` with value
   `SSMDocumentInputChecks` from
   `VerifyRunbookInputs` step.
   - **`BranchOnAlarmIsVerified`**

   Branches on Runbook's inputs verification
   `AlarmTriggerTimestamp` and
   `CloudWatchAlarmName`.
   - **`CheckMetricAlarmType`**

   Checks if an alarm is based on a Metric or Metric Math or is an Anomaly
   Detector Alarm.
   - **`CheckAlarmInInsufficientDataState`**

   Checks if an alarm is in insufficient data sate.
   - **`UpdateInsufficientDataChecksVariable`**

   Updates the variable `InsufficientDataChecks` with value
   `InsufficientDataChecks` from
   `CheckAlarmInInsufficientDataState` step.
   - **`BranchOnAlarmHasInsufficientData`**

   Branches on the `AlarmHasInsufficientData` value from
   `CheckAlarmInInsufficientDataState` step, the default step is
   `CheckMetricMismatch`.
   - **`CheckMetricMismatch`**

   Checks if the metric(s) used in the alarm matches with
   `ListMetrics` value.
   - **`UpdateMetricMismatchChecksVariable`**

   Updates the variable `MetricMismatchChecks` with value
   `MetricMismatchChecks` from `CheckMetricMismatch`
   step.
   - **`BranchOnMetricsMatched`**

   Branches on the `MetricsMatched` value from
   `CheckMetricMismatch` step, the default step is
   `CheckMissingDatapoint`.
   - **`CheckMissingDatapoint`**

   Verifies if a metric was missing datapoint(s) at a given timestamp.
   - **`UpdateMetricMissingDatapointsChecksVariable`**

   Updates the variable `MetricMissingDatapointsChecks` with value
   `MetricMissingDatapointsChecks` from
   `CheckMissingDatapoint` step.
   - **`BranchOnMetricMissingDatapoint`**

   Branches on the `MetricMissingDatapoint` value from
   `CheckMissingDatapoint` step, the default step is
   `GetAlarmHistoryDetails`.
   - **`GetAlarmHistoryDetails`**

   Gets the most recent history for a given timestamp.
   - **`UpdateAlarmHistoryChecksVariable`**

   Updates the variable `AlarmHistoryChecks` with value
   `AlarmHistoryChecks` from `GetAlarmHistoryDetails`
   step.
   - **`BranchOnAlarmHistoryFound`**

   Branches on the `AlarmHistoryFound` value from
   `GetAlarmHistoryDetails` step, the default step is
   `CheckDelayedMetric`.
   - **`CheckDelayedMetric`**

   Checks if an alarm did not trigger due to a delayed or missed
   metric(s).
   - **`UpdateDelayedMetricChecksVariable`**

   Updates the variable `DelayedMetricChecks` with value
   `DelayedMetricChecks` from `CheckDelayedMetric`
   step.
   - **`BranchOnMetricDelayedAndDatapointsMeetThreshold`**

   Branches on the `MetricDelayed` and
   `DatapointsMeetThreshold` values from
   `CheckDelayedMetric` step, the default step is
   `GenerateReport`.
   - **`CheckActionDelivered`**

   Checks if an alarm's enabled action(s) was/were delivered.
   - **`UpdateActionDeliveredChecksVariable`**

   Updates the variable `ActionDeliveredChecks` with output
   `ActionDeliveredChecks` from
   `CheckActionDelivered` step.
   - **`GenerateReport`**

   Compiles the output of the previous steps and outputs a report.

7. After the execution completes, review the Outputs section for the detailed results
   of the execution:
   - **GenerateReport.Report**

   A report of the provided Amazon CloudWatch (CloudWatch) metric Alarm.

```

                ------------------------------------------------------------------------------------------
                |                     AWS CloudWatch Alarm Troubleshooting Results                       |
                ------------------------------------------------------------------------------------------
                |     Alarm Name                        -               Demo-Alarm                       |
                |     Timestamp                         -               2025-03-04T06:31:00Z             |
                ------------------------------------------------------------------------------------------
                |     ✅ No Issue(s) Found                                                               |
                ------------------------------------------------------------------------------------------



                ==========================================================================================
                1. Validating SSM Document input parameters:
                ==========================================================================================
                ✅ [PASSED]: Found a metric alarm with name Demo-Alarm


                ==========================================================================================
                2. Checking alarm's data state:
                ==========================================================================================
                ✅ [PASSED]: The alarm is not in INSUFFICIENT_DATA state, alarm's state is: ALARM


                ==========================================================================================
                3. Checking if the alarm experienced metric mismatches:
                ==========================================================================================
                ✅ [PASSED]: Metric matches with the configured metric for Alarm.


                ==========================================================================================
                4. Checking if the alarm's metric(s) experienced missing datapoint(s):
                ==========================================================================================
                ✅ [PASSED]: Metric has datapoints


                ==========================================================================================
                5. Retrieving alarm's history for timestamp 2025-03-04T06:31:00Z:
                ==========================================================================================
                ✅ [PASSED]: Found most recent alarm history item for the provided timestamp: '2025-03-04T06:31:00Z'


                ==========================================================================================
                6. Checking if the alarm experienced metric delays or the alarm's datapoint(s) did not meet the configured threshold:
                ==========================================================================================
                ✅ [PASSED]: CloudWatch alarm did not experience any delayed metric


                ==========================================================================================
                7. Checking if the alarm has actions enabled and if action(s) were delivered:
                ==========================================================================================
                ✅ [PASSED]: Successfully executed action arn:aws:sns:us-east-1:12345678910:Demo_Alarms_Topic


                ------------------------------------------------------------------------------------------

                ✅ All the checks have passed for CloudWatch alarm, Demo-Alarm, the alarm's configuration is correct.

```

**References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAlarm/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-TroubleshootCloudWatchAlarm/description")
- [Run an
  automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an
  Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation
  Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
