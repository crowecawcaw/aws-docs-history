# Renaming the Delivery Channel

To change the delivery channel name, you must delete it and create a new delivery
channel with your specified name. Before you can delete the delivery channel, you must
temporarily stop the configuration recorder. The AWS Config console does not provide the
option to delete the delivery channel. You must use the AWS CLI, the AWS Config API, or one
of the AWS SDKs.

###### Renaming the delivery channel using the AWS CLI

1. Use the [`stop-configuration-recorder`](../../../cli/latest/reference/configservice/stop-configuration-recorder.md "../../../cli/latest/reference/configservice/stop-configuration-recorder.md") command to stop the
   configuration recorder:

```
$ **aws configservice stop-configuration-recorder --configuration-recorder-name `configRecorderName`**
```

2. Use the [`describe-delivery-channels`](../../../cli/latest/reference/configservice/describe-delivery-channels.md "../../../cli/latest/reference/configservice/describe-delivery-channels.md") command, and take note of
   your delivery channel's attributes:

```
$ **aws configservice describe-delivery-channels**
{
    "DeliveryChannels": [
        {
            "configSnapshotDeliveryProperties": {
                "deliveryFrequency": "Twelve_Hours"
            },
            "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
            "name": "default",
            "s3BucketName": "config-bucket-123456789012"
        }
    ]
}
```

3. Use the [`delete-delivery-channel`](../../../cli/latest/reference/configservice/delete-delivery-channel.md "../../../cli/latest/reference/configservice/delete-delivery-channel.md") command to delete the
   delivery channel:

```
$ **aws configservice delete-delivery-channel --delivery-channel-name `default`**
```

4. Use the [`put-delivery-channel`](../../../cli/latest/reference/configservice/put-delivery-channel.md "../../../cli/latest/reference/configservice/put-delivery-channel.md") command to create a delivery
   channel with the desired name:

```
$ **aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json**
```

The deliveryChannel.json file specifies the delivery channel
attributes:

```
{
    "name": "myCustomDeliveryChannelName",
    "s3BucketName": "config-bucket-123456789012",
    "snsTopicARN": "arn:aws:sns:us-east-2:123456789012:config-topic",
    "configSnapshotDeliveryProperties": {
        "deliveryFrequency": "Twelve_Hours"
    }
}
```

5. Use the `start-configuration-recorder` command to resume
   recording:

```
$ **aws configservice start-configuration-recorder --configuration-recorder-name `configRecorderName`**
```
