

# Test onboarded workloads in Incident Detection and Response
<a name="idr-workloads-testing"></a>

After [Alarm Ingestion](idr-gs-alarm-ingestion.md) completes, AWS Incident Detection and Response enables monitoring for your workload and sends a Go-Live confirmation. Your workload is actively monitored from this point forward.

Alarm testing validates that your onboarded alarms engage AWS Incident Detection and Response as expected, trigger the appropriate runbooks, and any other desired actions, such as auto case creation if you selected it during alarm ingestion.

Testing is optional but strongly recommended. You're responsible for validating your response arrangements before a real incident occurs.

## Testing options
<a name="idr-workloads-testing-options"></a>

AWS Incident Detection and Response offers two testing options.

### Option 1: Scheduled GameDay (recommended)
<a name="idr-workloads-testing-gameday"></a>

A scheduled GameDay is a live end-to-end simulation of what might happen during a real incident. AWS Incident Detection and Response follows your prescribed [runbook](idr-workloads-dev-runbook.md) steps to give you insight into how a real incident might unfold. The GameDay is an opportunity for you to ask questions or refine instructions to improve the engagement.

**To schedule a GameDay, complete the following steps:**

1. [Notify AWS Incident Detection and Response](idr-workloads-change-request.md) with a preferred date and a 1-hour time window, including time zone. Provide at least 48 hours of lead time.

1. Plan resources for the GameDay, including your SRE/Ops team and escalation contacts.

**GameDay schedule:**

1. You and AWS Incident Detection and Response join the call.

1. You disable alarm actions, if applicable.

1. You manually set your alarms to the **ALARM** state using the instructions in [How to test your alarms](#idr-workloads-testing-how-to).

1. AWS Incident Detection and Response confirms receipt of the alarm notification.

1. AWS Incident Detection and Response responds to the alarm and joins the bridge prescribed in your runbook.

1. You and AWS Incident Detection and Response confirm the GameDay outcome.

### Option 2: Offline alarm testing
<a name="idr-workloads-testing-offline"></a>

You can test your alarms independently at any time without scheduling a call. Triggering an alarm engages AWS Incident Detection and Response according to your runbook, just as it would during a real incident.

**To perform offline alarm testing, complete the following steps:**

1. To prevent unintended actions, disable any Amazon CloudWatch alarm actions.

1. Trigger your alarms using the instructions in [How to test your alarms](#idr-workloads-testing-how-to).

1. Within 5 minutes, a support case is created on your behalf and AWS Incident Detection and Response engages you as specified in your runbook.

1. Notify the Incident Manager that you are conducting offline alarm testing.

1. The Incident Manager confirms which alarm state changes were received and validates the response arrangements.

If a support case isn't created within 5 minutes, submit an [incident request](inbound-incident-idr.md) to manually engage AWS Incident Detection and Response for troubleshooting.

## How to test your alarms
<a name="idr-workloads-testing-how-to"></a>

### Amazon CloudWatch alarms
<a name="idr-workloads-testing-cw"></a>

**Note**  
The AWS Identity and Access Management user or role that you use for alarm testing must have `cloudwatch:SetAlarmState` permission.

Use the AWS Command Line Interface or [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html) to manually set your alarm to the **ALARM** state. These commands change the alarm state without impacting your workload.

To prevent unintended actions, for example Amazon EC2 instance restarts, disable any CloudWatch alarm actions before you change the alarm state. You can re-enable CloudWatch alarm actions after testing completes. To learn more about disabling or enabling alarm actions, see [DisableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisableAlarmActions.html) and [EnableAlarmActions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EnableAlarmActions.html) in the *Amazon CloudWatch API Reference*.

**Disable alarm actions:**

```
aws cloudwatch disable-alarm-actions --alarm-names "{{ExampleAlarm}}" --region {{us-east-1}}
```

**Set alarm state to ALARM:**

```
aws cloudwatch set-alarm-state --alarm-name "{{ExampleAlarm}}" --state-value ALARM --state-reason "{{Testing AWS Incident Detection and Response}}" --region {{us-east-1}}
```

**Re-enable alarm actions after testing:**

```
aws cloudwatch enable-alarm-actions --alarm-names "{{ExampleAlarm}}" --region {{us-east-1}}
```

The alarm state reverts to **OK** automatically within a few seconds.

**Composite alarms**

The `set-alarm-state` command doesn't guarantee that composite alarms revert to the **OK** state. As a best practice, verify the state of composite alarms after testing. To manually reset a composite alarm, use the following command:

```
aws cloudwatch set-alarm-state --alarm-name "{{ExampleCompositeAlarm}}" --state-value OK --state-reason "{{Testing AWS Incident Detection and Response}}" --region {{us-east-1}}
```

To learn more about manually changing the state of CloudWatch alarms, see [SetAlarmState](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_SetAlarmState.html) in the *Amazon CloudWatch API Reference*.

To learn more about the permissions required for CloudWatch API operations, see [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html).

### Third-party APM alarms
<a name="idr-workloads-testing-third-party-alarms"></a>

Workloads that use a third-party Application Performance Monitoring (APM) tool, such as Datadog, Splunk, New Relic, or Dynatrace, require different instructions to simulate an alarm.

1. Disable alarm actions in your APM to prevent unintended actions.

1. Modify your alarm threshold or comparison operator to force the alarm into the **ALARM** status. This triggers a payload to AWS Incident Detection and Response.

1. After testing completes, roll back the threshold or comparison operator changes to restore the alarm to **OK** status.

## Key outcomes
<a name="idr-workloads-testing-key-outputs"></a>

After successful testing:
+ Alarm ingestion is confirmed and your alarm configuration is correct.
+ Alarms are received by AWS Incident Detection and Response.
+ A support case is created and your prescribed contacts are notified.
+ AWS Incident Detection and Response engages you by your prescribed conference means.
+ All alarms and support cases generated during testing are resolved.

## Frequently asked questions
<a name="idr-workloads-testing-faq"></a>

**Is alarm testing mandatory?**  
No. Testing is optional but strongly recommended to validate your end-to-end response arrangements before a real incident occurs.

**Will my workload be impacted?**  
No. However, during testing any alarm actions configured on your alarms are triggered unless you disable them. Disable alarm actions before testing to prevent unintended impacts.

**Who is notified during testing?**  
During a scheduled GameDay, all contacts and escalation paths in your runbook are contacted for verification. During offline alarm testing, only the initial contact specified during alarm onboarding is notified.

**Can I reply via email to case updates?**  
No. Email copies of Support case correspondences are sent from a no-reply address. To update a case, use the [AWS Support Center Console](https://console.aws.amazon.com/support/home#/).

**How do I request a GameDay after go-live?**  
Reply to your existing onboarding support case, if it exists, or create a [Request changes to an onboarded workload in Incident Detection and Response](idr-workloads-change-request.md).