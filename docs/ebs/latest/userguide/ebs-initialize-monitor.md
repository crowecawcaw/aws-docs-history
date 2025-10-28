# Monitor the status of Amazon EBS volume initialization

When you create a volume, either from a snapshot or from another volume (volume copy), you
can monitor the status of the volume initialization to determine whether the initialization
process is complete. You can monitor volume initialization using the following options:

###### Topics

- [AWS CLI and Amazon EC2 console](#ebs-initialize-monitor-ec2 "#ebs-initialize-monitor-ec2")
- [Amazon EventBridge](#ebs-initialize-monitor-ev "#ebs-initialize-monitor-ev")

## AWS CLI and Amazon EC2 console

You can use the AWS CLI and Amazon EC2 console to check the status of the volume initialization
at any time after the volume has been created. The following information is provided:

- **Initialization type** (AWS CLI only) — Indicates
  the type of volume initialization used. `default` for fast snapshot restore and
  default volume initialization, `provisioned-rate` for Amazon EBS Provisioned Rate for Volume Initialization, and
  `volume-copy` for volume copy initialization.
- **Estimated time to completion** (AWS CLI only) —
  Only for volumes created using a Amazon EBS Provisioned Rate for Volume Initialization. The estimated remaining time, in seconds,
  for the volume initialization to complete.
- **Progress** — The progress, as a percentage (0-100),
  for the volume initialization process. For volumes initialized with fast snapshot restore,
  the progress moves to 100 percent immediately after creation.
- **Initialization state** — The overall state of the
  volume initialization (`initializing` or `completed`). For volumes
  initialized with fast snapshot restore, the state moves to `completed` immediately
  after creation.

###### Note

It can take up to 5 minutes for the volume initialization information to be updated.

Console

###### To monitor status of volume initialization

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume for which to check the volume initialization status.
4. The **Initialization state** field in the grid and **Details**
   tab provide progress information in the following format: _Initialization state (progress
   percentage)_. For example, _Initializing (75%)_.

The possible initialization states include: _Initializing_ and
_Completed_.

AWS CLI

###### To monitor status of volume initialization

Use the [describe-volume-status](../../../cli/latest/reference/ec2/describe-volume-status.md "../../../cli/latest/reference/ec2/describe-volume-status.md") AWS CLI command to view the initialization status.
`EstimatedTimeToCompleteInSeconds` is returned only for volumes created with an
Amazon EBS Provisioned Rate for Volume Initialization.

For example, the following command checks the initialization status for volume
`vol-11111111111111111`, which was created with an Amazon EBS Provisioned Rate for Volume Initialization.

```
aws ec2 describe-volume-status --volume-id `vol-01111111111111111`
```

The following is example output.

```
{
    "VolumeStatuses": [
        {
            "Actions": [],
            "AvailabilityZone": "us-east-1a",
            "Events": [],
            "VolumeID": "vol-11111111111111111",
            "VolumeStatus": {
                "Details": [
                    {
                        "Name": "io-enabled",
                        "Status": "passed"
                    },
                    {
                        "Name": "io-performance",
                        "Status": "not-applicable"
                    },
                    **{
 "Name": "initialization-state",
 "Status": "completed"
 }**
                ],
                "Status": "ok"
            },
            **"InitializationStatusDetails": {
 "InitializationType": "provisioned-rate",
 "Progress": 75,
 "EstimatedTimeToCompleteInSeconds": 850
 }**
        }
    ]
}
```

## Amazon EventBridge

An Amazon EventBridge event is sent to your account within five minutes **after**
the volume initialization has completed. You can create rules that trigger programmatic actions in response
to these events.

###### Note

- Events are emitted on a best effort basis.
- If you delete the volume before initialization completes, or within 5 minutes
  after initialization completes, you might not receive the event.

For more information about the event, see [EBS volume initialization event](ebs-cloud-watch-events.md#volume-initialization-events "ebs-cloud-watch-events.md#volume-initialization-events").

###### To monitor status of volume initialization using EventBridge

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Choose **Rules**, **Create rule**.
3. For **Step 1**, do the following:
   1. Specify a name and description for the rule.
   2. For **Event bus**, choose the bus to receive the events. If you haven't
      created a custom event bus, keep **default**, or see [Creating an event bus](../../../eventbridge/latest/userguide/eb-create-event-bus.md "../../../eventbridge/latest/userguide/eb-create-event-bus.md").
   3. For **Rule type**, keep **Rule with an
      event pattern**.
   4. Choose **Next**.

4. For **Step 2**, do the following:
   1. For **Event source**, keep **AWS events or EventBridge partner events**.
   2. For **Creation method**, choose **Custom pattern (JSON editor)**.
   3. For **Event pattern**, add the following:

   ```
   {
       "detail-type": ["EBS Volume Notification"],
       "source": ["aws.ec2"],
       "detail": {
           "event": ["initializeVolume"],
           "result": ["succeeded"]
       }
   }
   ```

   For an example event, see [EBS volume initialization event](ebs-cloud-watch-events.md#volume-initialization-events "ebs-cloud-watch-events.md#volume-initialization-events"). 4. Choose **Next**.

5. For **Step 3**, do the following:
   1. For **Target types**, choose **AWS service**.
   2. For **Select target**, choose **SNS topic**, and for
      **Topic** select the required topic. If you haven't created any topics, see
      [Creating a topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md").
   3. For **Permissions**, keep **Use execution role (recommended)** selected.
   4. For **Execution role**, keep **Create a new role for this
      specific resource** selected and the defauly role name.
   5. Choose **Next**.

6. For **Step 4**, specify tags for the rule if needed, and then choose
   **Next**.
7. For **Step 5**, review the rule and then choose **Create rule**.
