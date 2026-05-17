# Alarm testing (Gameday)

The last step in the AWS Incident Detection and Response onboarding process is to perform a Gameday for your new workload. After Alarm Ingestion steps, AWS Incident Detection and Response confirms a date and time of your choosing to start your Gameday.

Your Gameday serves two main purposes:

- **Functional Validation:** Confirms that AWS Incident Detection and Response can correctly receive your alarm events. And, functional validation confirms that your alarm events trigger the desired actions, such as automatic support case creation if you selected it during alarm ingestion.
- **Simulation:** The Gameday is an end to end simulation of what might happen during a real incident. AWS Incident Detection and Response gives you insight into how a real incident might unfold. The Gameday is an opportunity for you to ask questions or refine instructions to improve the engagement.
  During the alarm test, AWS Incident Detection and Response works with you to remediate any issues identified.

## CloudWatch Alarm testing

During the Gameday, Amazon CloudWatch alarms are tested by manually changing the alarm to the **Alarm** state using the AWS Command Line Interface. You can also access the AWS CLI from AWS CloudShell. AWS Incident Detection and Response provides you with a list of AWS CLI commands for you to use during testing.

Example AWS CLI command to set an alarm state:

```
aws cloudwatch set-alarm-state --alarm-name "`ExampleAlarm`" --state-value ALARM --state-reason "`Testing AWS Incident Detection and Response`" --region `us-east-1`
```

###### Note

The AWS Identity and Access Management user or role that you use for alarm testing must have `cloudwatch:SetAlarmState` permission.

To learn more about manually changing the state of CloudWatch alarms, see [SetAlarmState](../../../AmazonCloudWatch/latest/APIReference/API_SetAlarmState.md "../../../AmazonCloudWatch/latest/APIReference/API_SetAlarmState.md").

To learn more about the permissions required for CloudWatch API operations, see [Amazon CloudWatch permissions reference](../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md "../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md").

## Third party APM alarms testing

Workloads that utilize a third party Application Performance Monitoring (APM) tool, such as Datadog, Splunk, New Relic, or Dynatrace, require different instructions to simulate an alarm. At the start of the Gameday, AWS Incident Detection and Response requests that you temporarily change your alarm thresholds or comparison operators to force the alarm into the **ALARM** status. This status triggers a payload to AWS Incident Detection and Response.

## The Gameday validates the following points

- Alarm ingestion is successful and your alarm configuration is correct.
- Alarms are successfully created and received by AWS Incident Detection and Response.
- A support case is created for your incident and your prescribed runbook contacts are notified.
- AWS Incident Detection and Response can engage with you by your defined conference bridge method.
