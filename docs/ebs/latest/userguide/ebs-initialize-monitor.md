

# Monitor the status of Amazon EBS volume initialization
<a name="ebs-initialize-monitor"></a>

When you create a volume, either from a snapshot or from another volume (volume copy), you can monitor the status of the volume initialization to determine whether the initialization process is complete. You can monitor volume initialization using the following options:

**Topics**
+ [AWS CLI, AWS Tools for PowerShell, and Amazon EC2 console](#ebs-initialize-monitor-ec2)
+ [Amazon EventBridge](#ebs-initialize-monitor-ev)

## AWS CLI, AWS Tools for PowerShell, and Amazon EC2 console
<a name="ebs-initialize-monitor-ec2"></a>

You can use the AWS CLI, AWS Tools for PowerShell, and Amazon EC2 console to check the status of the volume initialization at any time after the volume has been created. The following information is provided:
+ **Initialization type** (AWS CLI and AWS Tools for PowerShell only) — Indicates the type of volume initialization used. `default` for fast snapshot restore and default volume initialization, `provisioned-rate` for Amazon EBS Provisioned Rate for Volume Initialization, and `volume-copy` for volume copy initialization.
+ **Estimated time to completion** (AWS CLI and AWS Tools for PowerShell only) — Only for volumes created using an Amazon EBS Provisioned Rate for Volume Initialization. The estimated remaining time, in seconds, for the volume initialization to complete.
+ **Progress** — The progress, as a percentage (0–100), for the volume initialization process. For volumes initialized with fast snapshot restore, the progress moves to 100 percent immediately after creation.
+ **Initialization state** — The overall state of the volume initialization (`initializing` or `completed`). For volumes initialized with fast snapshot restore, the state moves to `completed` immediately after creation.

**Note**  
It can take up to 5 minutes for the volume initialization information to be updated.

Use the following tabs to check the volume initialization status for your volume.

------
#### [ Console ]

**To monitor status of volume initialization**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Volumes**.

1. Select the volume for which to check the volume initialization status.

1. The **Initialization state** field in the grid and **Details** tab provide progress information in the following format: *Initialization state (progress percentage)*. For example, *Initializing (75%)*.

   The possible initialization states include: *Initializing* and *Completed*.

------
#### [ AWS CLI ]

**To monitor status of volume initialization**  
Use the [ describe-volume-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volume-status.html) AWS CLI command to view the initialization status. The output includes `EstimatedTimeToCompleteInSeconds` only for volumes created with an Amazon EBS Provisioned Rate for Volume Initialization.

For example, the following command checks the initialization status for volume `vol-11111111111111111`, which was created with an Amazon EBS Provisioned Rate for Volume Initialization.

```
aws ec2 describe-volume-status --volume-ids {{vol-11111111111111111}}
```

The following is example output.

```
{
    "VolumeStatuses": [
        {
            "Actions": [],
            "AvailabilityZone": "us-east-1a",
            "Events": [],
            "VolumeId": "vol-11111111111111111",
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
                    {
                        "Name": "initialization-state",
                        "Status": "completed"
                    }
                ],
                "Status": "ok"
            },
            "InitializationStatusDetails": {
                "InitializationType": "provisioned-rate",
                "Progress": 75,
                "EstimatedTimeToCompleteInSeconds": 850
            }
        }
    ]
}
```

------
#### [ PowerShell ]

**To monitor status of volume initialization**  
Use the [Get-EC2VolumeStatus](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2VolumeStatus.html) cmdlet to view the initialization status. The output includes `EstimatedTimeToCompleteInSeconds` only for volumes created with an Amazon EBS Provisioned Rate for Volume Initialization.

For example, the following command checks the initialization status for volume `vol-11111111111111111`, which was created with an Amazon EBS Provisioned Rate for Volume Initialization.

```
(Get-EC2VolumeStatus `
    -Region us-east-1 `
    -VolumeId vol-11111111111111111).InitializationStatusDetails |
    Select-Object `
        InitializationType,
        Progress,
        EstimatedTimeToCompleteInSeconds
```

------

## Amazon EventBridge
<a name="ebs-initialize-monitor-ev"></a>

An Amazon EventBridge event is sent to your account within five minutes **after** the volume initialization has completed. You can create rules that trigger programmatic actions in response to these events.

**Note**  
Events are emitted on a best effort basis.
If you delete the volume before initialization completes, or within 5 minutes after initialization completes, you might not receive the event.

For more information about the event, see [EBS volume initialization event](ebs-cloud-watch-events.md#volume-initialization-events).

**To monitor status of volume initialization using EventBridge**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose **Rules**, **Create rule**.

1. For **Step 1**, do the following:

   1. Specify a name and description for the rule.

   1. For **Event bus**, choose the bus to receive the events. If you haven't created a custom event bus, keep **default**, or see [Creating an event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html).

   1. For **Rule type**, keep **Rule with an event pattern**.

   1. Choose **Next**.

1. For **Step 2**, do the following:

   1. For **Event source**, keep **AWS events or EventBridge partner events**.

   1. For **Creation method**, choose **Custom pattern (JSON editor)**.

   1. For **Event pattern**, add the following:

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

      For an example event, see [EBS volume initialization event](ebs-cloud-watch-events.md#volume-initialization-events).

   1. Choose **Next**.

1. For **Step 3**, do the following:

   1. For **Target types**, choose **AWS service**.

   1. For **Select target**, choose **SNS topic**, and for **Topic** select the required topic. If you haven't created any topics, see [Creating a topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html).

   1. For **Permissions**, keep **Use execution role (recommended)** selected.

   1. For **Execution role**, keep **Create a new role for this specific resource** selected and the defauly role name.

   1. Choose **Next**.

1. For **Step 4**, specify tags for the rule if needed, and then choose **Next**.

1. For **Step 5**, review the rule and then choose **Create rule**.