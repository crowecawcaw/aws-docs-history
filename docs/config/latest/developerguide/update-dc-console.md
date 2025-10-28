# Updating the Delivery Channel

When you update the delivery channel, you can set the following options:

- The Amazon S3 bucket where AWS Config sends configuration snapshots and configuration
  history files.
- How often AWS Config delivers configuration snapshots to your Amazon S3 bucket.
- The Amazon SNS topic to which AWS Config sends notifications about configuration
  changes.
  You can use the AWS Config console to set the Amazon S3 bucket and the Amazon SNS topic for
  your delivery channel. For steps to manage these settings, see [Setting Up AWS Config with the Console](gs-console.md "gs-console.md").

The console does not provide options to rename the delivery channel, set the
frequency for configuration snapshots, or delete the delivery channel. To do
these tasks, you must use the AWS CLI, the AWS Config API, or one of the AWS
SDKs.

The following code examples show how to use `PutDeliveryChannel`.

CLI

**AWS CLI**

**To create a delivery channel**

The following command provides the settings for the delivery channel as JSON code:

```
`aws configservice put-delivery-channel --delivery-channel `file://deliveryChannel.json``

```

The `deliveryChannel.json` file specifies the delivery channel attributes:

```
{
    "name": "default",
    "s3BucketName": "config-bucket-123456789012",
    "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic",
    "configSnapshotDeliveryProperties": {
        "deliveryFrequency": "Twelve_Hours"
    }
}
```

This example sets the following attributes:

`name` - The name of the delivery channel. By default, AWS Config assigns the name `default` to a new delivery channel.You cannot update the delivery channel name with the `put-delivery-channel` command. For the steps to change the name, see Renaming the Delivery Channel.`s3BucketName` - The name of the Amazon S3 bucket to which AWS Config delivers configuration snapshots and configuration history files.If you specify a bucket that belongs to another AWS account, that bucket must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon S3 Bucket.

`snsTopicARN` - The Amazon Resource Name (ARN) of the Amazon SNS topic to which AWS Config sends notifications about configuration changes.If you choose a topic from another account, the topic must have policies that grant access permissions to AWS Config. For more information, see Permissions for the Amazon SNS Topic.

`configSnapshotDeliveryProperties` - Contains the `deliveryFrequency` attribute, which sets how often AWS Config delivers configuration snapshots and how often it invokes evaluations for periodic Config rules.

If the command succeeds, AWS Config returns no output. To verify the settings of your delivery channel, run the describe-delivery-channels command.

- For API details, see
  [PutDeliveryChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-delivery-channel.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-delivery-channel.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example changes the deliveryFrequency property of an existing delivery channel.**

```
Write-CFGDeliveryChannel -ConfigSnapshotDeliveryProperties_DeliveryFrequency TwentyFour_Hours -DeliveryChannelName default -DeliveryChannel_S3BucketName amzn-s3-demo-bucket -DeliveryChannel_S3KeyPrefix my

```

- For API details, see
  [PutDeliveryChannel](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example changes the deliveryFrequency property of an existing delivery channel.**

```
Write-CFGDeliveryChannel -ConfigSnapshotDeliveryProperties_DeliveryFrequency TwentyFour_Hours -DeliveryChannelName default -DeliveryChannel_S3BucketName amzn-s3-demo-bucket -DeliveryChannel_S3KeyPrefix my

```

- For API details, see
  [PutDeliveryChannel](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

(Optional) You can use the [`describe-delivery-channels`](../../../cli/latest/reference/configservice/describe-delivery-channels.md "../../../cli/latest/reference/configservice/describe-delivery-channels.md")
command to verify that the delivery channel settings are updated:

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

The following code examples show how to use `DescribeDeliveryChannels`.

CLI

**AWS CLI**

**To get details about the delivery channel**

The following command returns details about the delivery channel:

```
`aws configservice describe-delivery-channels`

```

Output:

```
{
    "DeliveryChannels": [
        {
            "snsTopicARN": "arn:aws:sns:us-east-1:123456789012:config-topic",
            "name": "default",
            "s3BucketName": "config-bucket-123456789012"
        }
    ]
}
```

- For API details, see
  [DescribeDeliveryChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-delivery-channels.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example retrieves the delivery channel for the region and displays details.**

```
Get-CFGDeliveryChannel -Region eu-west-1 | Select-Object Name, S3BucketName, S3KeyPrefix, @{N="DeliveryFrequency";E={$_.ConfigSnapshotDeliveryProperties.DeliveryFrequency}}

```

**Output:**

```
Name    S3BucketName               S3KeyPrefix DeliveryFrequency
----    ------------               ----------- -----------------
default config-bucket-NA my          TwentyFour_Hours
```

- For API details, see
  [DescribeDeliveryChannels](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example retrieves the delivery channel for the region and displays details.**

```
Get-CFGDeliveryChannel -Region eu-west-1 | Select-Object Name, S3BucketName, S3KeyPrefix, @{N="DeliveryFrequency";E={$_.ConfigSnapshotDeliveryProperties.DeliveryFrequency}}

```

**Output:**

```
Name    S3BucketName               S3KeyPrefix DeliveryFrequency
----    ------------               ----------- -----------------
default config-bucket-NA my          TwentyFour_Hours
```

- For API details, see
  [DescribeDeliveryChannels](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.
