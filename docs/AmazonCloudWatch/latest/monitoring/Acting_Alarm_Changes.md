# Acting on alarm changes

CloudWatch can notify users on two types of alarm changes: when an alarm changes state, and when
the configuration of an alarm gets updated.

When an alarm evaluates, it might change from one state to another, such as ALARM or OK.
For Metrics Insights alarms that monitor multiple time series, each time series (contributor)
can only be in ALARM or OK state, never in INSUFFICIENT_DATA state. This is because a time
series only exists when data is present.

## Alarm actions and notifications

The following table shows which actions are executed at the alarm level versus the
contributor level for Metrics Insights alarms:

| Action Type                                    | Alarm Level | Contributor Level | More Information                                                                                                                                                                                                                                         |
| ---------------------------------------------- | ----------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SNS notifications                              | Yes         | Yes               | [Amazon SNS event destinations](../../../sns/latest/dg/sns-event-destinations.md "../../../sns/latest/dg/sns-event-destinations.md")                                                                                                                     |
| EC2 actions (stop, terminate, reboot, recover) | No          | Yes               | [Create alarms to stop, terminate, reboot, or recover an EC2<br>instance](UsingAlarmActions.md "UsingAlarmActions.md")                                                                                                                                   |
| Auto Scaling actions                           | Yes         | No                | [Step and simple<br>scaling policies for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/as-scaling-simple-step.md "../../../autoscaling/ec2/userguide/as-scaling-simple-step.md")                                                           |
| Systems Manager OpsItem creation               | Yes         | Yes               | [Configure CloudWatch alarms to create OpsItems](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md")          |
| Systems Manager Incident Manager incidents     | Yes         | No                | [Creating incidents automatically with CloudWatch alarms](../../../incident-manager/latest/userguide/incident-creation.md#incident-tracking-auto-alarms "../../../incident-manager/latest/userguide/incident-creation.md#incident-tracking-auto-alarms") |
| Lambda function invocation                     | Yes         | Yes               | [Invoke a Lambda function from an alarm](alarms-and-actions-Lambda.md "alarms-and-actions-Lambda.md")                                                                                                                                                    |
| CloudWatch investigations investigation        | Yes         | No                | [Start a CloudWatch investigations from an alarm](Start-Investigation-Alarm.md "Start-Investigation-Alarm.md")                                                                                                                                           |

The content of alarm notifications differs between single-metric alarms and multi-time
series alarms:

- Single-metric alarms include both a state reason and detailed state reason data,
  showing the specific datapoints that caused the state change.
- Multi-time series alarms provide a simplified state reason for each contributor,
  without the detailed state reason data block.

###### Example Notification Content Examples

Single-metric alarm notification includes detailed data:

```
{
  "stateReason": "Threshold Crossed: 3 out of the last 3 datapoints [32.6 (03/07/25 08:29:00), 33.8 (03/07/25 08:24:00), 41.0 (03/07/25 08:19:00)] were greater than the threshold (31.0)...",
  "stateReasonData": {
    "version": "1.0",
    "queryDate": "2025-07-03T08:34:06.300+0000",
    "startDate": "2025-07-03T08:19:00.000+0000",
    "statistic": "Average",
    "period": 300,
    "recentDatapoints": [41, 33.8, 32.6],
    "threshold": 31,
    "evaluatedDatapoints": [
      {
        "timestamp": "2025-07-03T08:29:00.000+0000",
        "sampleCount": 5,
        "value": 32.6
      }
      // Additional datapoints...
    ]
  }
}
```

Multi-time series alarm notification includes simplified reason:

```
{
  "stateReason": "Threshold Crossed: 3 datapoints were greater than the threshold (0.0). The most recent datapoints which crossed the threshold: [32.6 (03/07/25 08:29:00)]."
}
```

Additionally, CloudWatch sends events to Amazon EventBridge whenever alarms change state, and when alarms
are created, deleted, or updated. You can write EventBridge rules to take actions or be notified when
EventBridge receives these events.

###### Topics

- [Notifying users on alarm changes](Notify_Users_Alarm_Changes.md "Notify_Users_Alarm_Changes.md")
- [Invoke a Lambda function from an alarm](alarms-and-actions-Lambda.md "alarms-and-actions-Lambda.md")
- [Start a CloudWatch investigations from an alarm](Start-Investigation-Alarm.md "Start-Investigation-Alarm.md")
- [Alarm events and EventBridge](cloudwatch-and-eventbridge.md "cloudwatch-and-eventbridge.md")
