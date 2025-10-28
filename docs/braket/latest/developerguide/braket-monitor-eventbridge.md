# Monitoring your quantum tasks with EventBridge

Amazon EventBridge monitors status change events in Amazon Braket quantum tasks. Events from Amazon Braket are delivered to EventBridge,
almost in real time. You can write rules that indicate which events interest you, including automated actions to take
when an event matches a rule. Automatic actions that can be triggered include these:

- Invoking an AWS Lambda function
- Activating an AWS Step Functions state machine
- Notifying an Amazon SNS topic
  EventBridge monitors these Amazon Braket status change events:

- The state of qauntum task changes
  Amazon Braket guarantees delivery of quantum task status change events. These events are delivered at least once, but possibly out of order.

For more information, see the [Events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

###### In this section:

- [Monitor quantum task status with EventBridge](#braket-eventbridge-tasks "#braket-eventbridge-tasks")
- [Example Amazon Braket EventBridge event](#braket-eventbridge-examples "#braket-eventbridge-examples")

## Monitor quantum task status with EventBridge

With EventBridge, you can create rules that define actions to take when Amazon Braket sends notification of a status
change regarding a Braket quantum task. For example, you can create a rule that sends you an email message each time
the status of a quantum task changes.

1. Log in to AWS using an account that has permissions to use EventBridge and Amazon
   Braket.
2. Open the [Amazon EventBridge console](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
3. Using the following values, create an EventBridge rule:
   - For **Rule type**, choose **Rule with an event pattern**.
   - For **Event source**, choose **Other**.
   - In the **Event pattern** section, choose **Custom patterns (JSON editor)**, and then paste the following event pattern into the text area:

   ```
   {
     "source": [
       "aws.braket"
     ],
     "detail-type": [
       "Braket Task State Change"
     ]
   }
   ```

   To capture all events from Amazon
   Braket, exclude the `detail-type` section as shown in the following code:

   ```
   {
     "source": [
       "aws.braket"
     ]
   }
   ```

   - For **Target types**, choose **AWS service**, and for **Select a target**, choose a target such as an Amazon SNS topic or AWS Lambda function. The target is triggered when a quantum task state change event is received from Amazon
     Braket.

   For example, use an Amazon Simple Notification Service (SNS) topic to send an email or text message when an event occurs. To do that, first create an Amazon SNS topic using the Amazon SNS console. To learn more, see [Using Amazon SNS for user notifications](../../../sns/latest/dg/sns-user-notifications.md "../../../sns/latest/dg/sns-user-notifications.md").

For details about creating rules, see [Creating Amazon EventBridge rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

## Example Amazon Braket EventBridge event

For information on the fields for an Amazon Braket Quantum Task Status Change event,
see [Events in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

The following attributes appear in the JSON "detail" field.

- **`quantumTaskArn`** (str): The quantum task for which this event was generated.
- **`status`** (Optional[str]): The status to which the quantum task transitioned.
- **`deviceArn`** (str): The device specified by the user for which this quantum task was created.
- **shots** (int): The number of shots requested by the user.
- **`outputS3Bucket`** (str): The output bucket specified by the user.
- **`outputS3Directory`** (str): The output key prefix specified by the user.
- **`createdAt`** (str): The quantum task creation time as an ISO-8601 string.
- **`endedAt`** (Optional[str]): The time at which the quantum task reached a terminal state. This field is present only when the quantum task has transitioned to a terminal state.

The following JSON code shows an example of an Amazon
Braket Quantum Task Status Change event.

```
{
    "version":"0",
    "id":"6101452d-8caf-062b-6dbc-ceb5421334c5",
    "detail-type":"Braket Task State Change",
    "source":"aws.braket",
    "account":"012345678901",
    "time":"2021-10-28T01:17:45Z",
    "region":"us-east-1",
    "resources":[
        "arn:aws:braket:us-east-1:012345678901:quantum-task/834b21ed-77a7-4b36-a90c-c776afc9a71e"
    ],
    "detail":{
        "quantumTaskArn":"arn:aws:braket:us-east-1:012345678901:quantum-task/834b21ed-77a7-4b36-a90c-c776afc9a71e",
        "status":"COMPLETED",
        "deviceArn":"arn:aws:braket:::device/quantum-simulator/amazon/sv1",
        "shots":"100",
        "outputS3Bucket":"amazon-braket-0260a8bc871e",
        "outputS3Directory":"sns-testing/834b21ed-77a7-4b36-a90c-c776afc9a71e",
        "createdAt":"2021-10-28T01:17:42.898Z",
        "eventName":"MODIFY",
        "endedAt":"2021-10-28T01:17:44.735Z"
      }
}
```
