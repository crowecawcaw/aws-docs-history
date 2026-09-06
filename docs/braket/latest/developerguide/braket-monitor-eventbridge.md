

# Monitoring your Braket resources with EventBridge
<a name="braket-monitor-eventbridge"></a>

 Amazon EventBridge monitors status change events in Amazon Braket resources, including quantum tasks and spending limits. Events from Amazon Braket are delivered to EventBridge, almost in real time. You can write rules that indicate which events interest you, including automated actions to take when an event matches a rule. Automatic actions that can be triggered include these:
+ Invoking an AWS Lambda function
+ Activating an AWS Step Functions state machine
+ Notifying an Amazon SNS topic

EventBridge monitors these Amazon Braket status change events:
+ The state of a quantum task changes
+ The amount spent on a spending limit changes

Amazon Braket guarantees delivery of these events. They are delivered at least once, but possibly out of order.

For more information, see the [Events in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html).

**Topics**
+ [Monitor quantum task status with EventBridge](#braket-eventbridge-tasks)
+ [Example Amazon Braket EventBridge event](#braket-eventbridge-examples)
+ [Monitor spending limit changes with EventBridge](#braket-eventbridge-spending-limits)

## Monitor quantum task status with EventBridge
<a name="braket-eventbridge-tasks"></a>

With EventBridge, you can create rules that define actions to take when Amazon Braket sends notification of a status change regarding a Braket quantum task. For example, you can create a rule that sends you an email message each time the status of a quantum task changes.

1. Log in to AWS using an account that has permissions to use EventBridge and Amazon Braket.

1. Open the [Amazon EventBridge console](https://console.aws.amazon.com/events/).

1. Using the following values, create an EventBridge rule:
   + For **Rule type**, choose **Rule with an event pattern**.
   + For **Event source**, choose **Other**.
   + In the **Event pattern** section, choose **Custom patterns (JSON editor)**, and then paste the following event pattern into the text area:

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

     To capture all events from Amazon Braket, exclude the `detail-type` section as shown in the following code:

     ```
     {
       "source": [
         "aws.braket"
       ]
     }
     ```
   + For **Target types**, choose ** AWS service**, and for **Select a target**, choose a target such as an Amazon SNS topic or AWS Lambda function. The target is triggered when a quantum task state change event is received from Amazon Braket.

     For example, use an Amazon Simple Notification Service (SNS) topic to send an email or text message when an event occurs. To do that, first create an Amazon SNS topic using the Amazon SNS console. To learn more, see [Using Amazon SNS for user notifications](https://docs.aws.amazon.com/sns/latest/dg/sns-user-notifications.html).

For details about creating rules, see [Creating Amazon EventBridge rules that react to events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html).

## Example Amazon Braket EventBridge event
<a name="braket-eventbridge-examples"></a>

For information on the fields for an Amazon Braket Quantum Task Status Change event, see [Events in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events.html).

The following attributes appear in the JSON "detail" field.
+  ** `quantumTaskArn` ** (str): The quantum task for which this event was generated.
+  ** `status` ** (Optional[str]): The status to which the quantum task transitioned.
+  ** `deviceArn` ** (str): The device specified by the user for which this quantum task was created.
+  ** shots ** (int): The number of shots requested by the user.
+  ** `outputS3Bucket` ** (str): The output bucket specified by the user.
+  ** `outputS3Directory` ** (str): The output key prefix specified by the user.
+  ** `createdAt` ** (str): The quantum task creation time as an ISO-8601 string.
+  ** `endedAt` ** (Optional[str]): The time at which the quantum task reached a terminal state. This field is present only when the quantum task has transitioned to a terminal state.

The following JSON code shows an example of an Amazon Braket Quantum Task Status Change event.

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

## Monitor spending limit changes with EventBridge
<a name="braket-eventbridge-spending-limits"></a>

To monitor changes to the amount spent on spending limits, use the following event pattern:

```
{
  "source": [
    "aws.braket"
  ],
  "detail-type": [
    "Braket Spending Limit Spend Change"
  ]
}
```

The following attributes appear in the JSON "detail" field for Braket Spending Limit Spend Change events:
+  ** `quantumTaskArn` ** (str): The ARN of the quantum task that caused the change in amount spent.
+  ** `deviceArn` ** (str): The ARN of the device associated with the quantum task.
+  ** `spendingLimit` ** (str): The configured spending limit amount, in US dollars (USD).
+  ** `spendingLimitArn` ** (str): The ARN of the spending limit for which this event was generated.
+  ** `totalSpend` ** (str): The total amount spent against the spending limit.
+  ** `queuedSpend` ** (str): The estimated cost of pending quantum tasks against the spending limit.
+  ** `timePeriod` ** (object): The time period of the spending limit, containing `startAt` and `endAt` timestamps in milliseconds.

The following JSON code shows an example of an Amazon Braket Spending Limit Spend Change event:

```
{
    "version": "0",
    "id": "c1a22f1f-3e86-46ea-87f9-0ca6f2234d83",
    "detail-type": "Braket Spending Limit Spend Change",
    "source": "aws.braket",
    "account": "123456789012",
    "time": "2028-02-29T12:00:00Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:braket:us-west-2:123456789012:spending-limit/b6951b86-8222-45b1-9908-2df6c3ac717d",
        "arn:aws:braket:us-west-2:123456789012:quantum-task/4cf7bd26-0eb7-44bf-bc3b-3d0d0bbdc6a2"
    ],
    "detail": {
        "quantumTaskArn": "arn:aws:braket:us-west-2:123456789012:quantum-task/4cf7bd26-0eb7-44bf-bc3b-3d0d0bbdc6a2",
        "deviceArn": "arn:aws:braket:us-west-2::device/qpu/amazon/example-device",
        "spendingLimit": "10.00",
        "spendingLimitArn": "arn:aws:braket:us-west-2:123456789012:spending-limit/b6951b86-8222-45b1-9908-2df6c3ac717d",
        "totalSpend": "5.00",
        "queuedSpend": "1.00",
        "timePeriod": {
            "startAt": 1764893800000,
            "endAt": 4922726400000
        }
    }
}
```