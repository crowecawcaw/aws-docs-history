# Verifying that AWS Config is Successfully Started with the AWS CLI

After you have started AWS Config, you can use AWS CLI commands to check that the AWS Config is running
and that AWS Config has created a configuration recorder and a delivery channel. You can also confirm
that AWS Config has started recording and delivering configurations to the delivery channel.

###### Topics

- [Step 1: Check that a delivery channel is Created](#gs-cli-verify-channel "#gs-cli-verify-channel")
- [Step 2: Check that a configuration recorder is
  Created](#gs-cli-verify-recorder "#gs-cli-verify-recorder")
- [Step 3: Check that AWS Config has started recording](#gs-cli-verify-config-recording "#gs-cli-verify-config-recording")

## Step 1: Check that a delivery channel is Created

Use the [`describe-delivery-channels`](../../../cli/latest/reference/configservice/describe-delivery-channels.md "../../../cli/latest/reference/configservice/describe-delivery-channels.md") command to check that your Amazon S3
bucket and Amazon SNS topic is configured.

You can use the `--delivery-channel-names` field to specify a list of delivery channel. If a delivery channel is not specified, this command returns the details of all delivery channels associated with the account.

```
$ **aws configservice describe-delivery-channels**
{
    "DeliveryChannels": [
        {
            "snsTopicARN": "arn:aws:sns:us-west-2:0123456789012:my-config-topic",
            "name": "my-delivery-channel",
            "s3BucketName": "my-config-bucket"
        }
    ]
}
```

## Step 2: Check that a configuration recorder is

Created

Use the [`describe-configuration-recorders`](../../../cli/latest/reference/configservice/describe-configuration-recorders.md "../../../cli/latest/reference/configservice/describe-configuration-recorders.md") command to check that a
configuration recorder is created.

You can use the `arn` and `configuration-recorder-names` fields to specify a list of configuration recorders. If a configuration recorder is not specified, this command returns the details of all configuration recorders associated with the account.

```
$ **aws configservice describe-configuration-recorders**
{
    "ConfigurationRecorders": [
        {
            "roleARN": "arn:aws:iam::012345678912:role/myConfigRole",
            "name": "default"
        }
    ]
}
```

## Step 3: Check that AWS Config has started recording

Use the [`describe-configuration-recorder-status`](../../../cli/latest/reference/configservice/describe-configuration-recorder-status.md "../../../cli/latest/reference/configservice/describe-configuration-recorder-status.md") command to check that the configuration recorder is successfully recording the resource types in scope.

You can use the `arn` and `configuration-recorder-names` fields to specify a list of configuration recorders. If a configuration recorder is not specified, this command returns the details of all configuration recorders associated with the account.

```
$ **aws configservice describe-configuration-recorder-status**
{
    "ConfigurationRecordersStatus": [
        {
            "name": "default",
            "lastStatus": "SUCCESS",
            "lastStopTime": 1414511624.914,
            "lastStartTime": 1414708460.276,
            "recording": true,
            "lastStatusChangeTime": 1414816537.148,
            "lastErrorMessage": "NA",
            "lastErrorCode": "400"
        }
    ]
}
```

The `true` value in the `recording` field confirms that the
configuration recorder has started recording configurations. AWS Config
records the time in UTC. The output is displayed as a Unix timestamp.
