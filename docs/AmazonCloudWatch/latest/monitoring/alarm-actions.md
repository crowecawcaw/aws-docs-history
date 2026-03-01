# Alarm actions

You can specify what actions an alarm takes when it changes state between the OK, ALARM, and INSUFFICIENT_DATA states.

Most actions can be set for the transition into each of the three states. Except for Auto Scaling actions, the actions happen only on state transitions, and are not performed again if the condition persists for hours or days.

The following are supported as alarm actions:

- Notify one or more subscribers by using an Amazon Simple Notification Service topic. Subscribers can be applications as well as persons.
- Invoke a Lambda function. This is the easiest way for you to automate custom actions on alarm state changes.
- Alarms based on EC2 metrics can also perform EC2 actions, such as stopping, terminating, rebooting, or recovering an EC2 instance.
- Alarms can perform actions to scale an Auto Scaling group.
- Alarms can create OpsItems in Systems Manager Ops Center or create incidents in AWS Systems Manager Incident Manager. These actions are performed only when the alarm goes into ALARM state.
- An alarm can start an investigation when it goes into ALARM state.
  Alarms also emit events to Amazon EventBridge when they change state, and you can set up Amazon EventBridge to trigger other actions for these state changes.

## Alarm actions and notifications

The following table shows the actions executed for alarms along with
their behavior for multiple time series (or contributors) alarms:

| Action Type                                    | Multiple Time Series Alarm support | More Information                                                                                                                                                                                                                                         |
| ---------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SNS notifications                              | Contributor Level                  | [Amazon SNS event destinations](../../../sns/latest/dg/sns-event-destinations.md "../../../sns/latest/dg/sns-event-destinations.md")                                                                                                                     |
| EC2 actions (stop, terminate, reboot, recover) | Not supported                      | [Stop, terminate, reboot, or recover an EC2 instance](UsingAlarmActions.md "UsingAlarmActions.md")                                                                                                                                                       |
| Auto Scaling actions                           | Not supported                      | [Step and simple<br>scaling policies for Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/as-scaling-simple-step.md "../../../autoscaling/ec2/userguide/as-scaling-simple-step.md")                                                           |
| Systems Manager OpsItem creation               | Alarm Level                        | [Configure CloudWatch alarms to create OpsItems](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md")          |
| Systems Manager Incident Manager incidents     | Alarm Level                        | [Creating incidents automatically with CloudWatch alarms](../../../incident-manager/latest/userguide/incident-creation.md#incident-tracking-auto-alarms "../../../incident-manager/latest/userguide/incident-creation.md#incident-tracking-auto-alarms") |
| Lambda function invocation                     | Contributor Level                  | [Invoke a Lambda function from an alarm](alarms-and-actions-Lambda.md "alarms-and-actions-Lambda.md")                                                                                                                                                    |
| CloudWatch investigations investigation        | Alarm Level                        | [Start a CloudWatch investigations from an alarm](Start-Investigation-Alarm.md "Start-Investigation-Alarm.md")                                                                                                                                           |

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

Multiple time series Metrics Insights Alarm SNS notification for Contributor example:

```
{
  "AlarmName": "DynamoDBInsightsAlarm",
  "NewStateValue": "ALARM",
  "NewStateReason": "Threshold Crossed: 1 datapoint was less than the threshold (1.0). The most recent datapoint which crossed the threshold: [0.0 (01/12/25 13:34:00)].",
  "StateChangeTime": "2025-12-01T13:42:04.919+0000",
  "OldStateValue": "OK",
  "AlarmContributorId": "6d442278dba546f6",
  "AlarmContributorAttributes": {
    "TableName": "example-dynamodb-table-name"
  }
  // Additional information...
}

```

## Muting Alarm Actions

Alarm mute rules allow you to automatically mute alarm actions during predefined time windows, such as maintenance periods or operational events. CloudWatch continues monitoring alarm states while preventing unwanted notifications. For more information, see [Alarm Mute Rules](alarm-mute-rules.md "alarm-mute-rules.md").

###### Mute rules vs. disabling alarm actions

Alarm mute rules temporarily mute actions during scheduled time windows and automatically unmute when the window ends. In contrast, the `DisableAlarmActions` API permanently disables alarm actions until you manually call `EnableAlarmActions`. The `EnableAlarmActions` API does not unmute alarms that are muted by active mute rules.

###### Note

Muting an alarm does not stop CloudWatch from sending alarm events for alarm create, update, delete, and state changes to Amazon EventBridge.
