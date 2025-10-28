# Starting AWS Config with a customer managed configuration recorder using the AWS CLI

You can start AWS Config by creating a customer managed configuration recorder. To create a customer managed configuration recorder with the AWS CLI, use the following commands: [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md"), [`put-delivery-channel`](../../../cli/latest/reference/configservice/put-delivery-channel.md "../../../cli/latest/reference/configservice/put-delivery-channel.md"), and
[`start-configuration-recorder`](../../../cli/latest/reference/configservice/start-configuration-recorder.md "../../../cli/latest/reference/configservice/start-configuration-recorder.md").

- The `put-configuration-recorder` command creates a customer managed configuration recorder.
- The `put-delivery-channel` command creates a delivery channel where AWS Config delivers
  configuration information to an S3 bucket and SNS topic.
- The `start-configuration-recorder` starts the customer managed configuration recorder. The customer managed configuration recorder will begin recording configuration changes for the resource types you specify.

###### Topics

- [Considerations](#gs-cli-subscribe-considerations "#gs-cli-subscribe-considerations")
- [Step 1: Run the put-configuration-recorder](#gs-cli-subscribe-put-configuration-recorder "#gs-cli-subscribe-put-configuration-recorder")
- [Step 2: Run the put-delivery-channel command](#gs-cli-subscribe-put-delivery-channel "#gs-cli-subscribe-put-delivery-channel")
- [Step 3: Run the start-configuration-recorder command](#gs-cli-subscribe-start-configuration-recorder "#gs-cli-subscribe-start-configuration-recorder")

## Considerations

**S3 bucket, SNS topic, and IAM role are required**

To create a customer managed configuration recorder, you need to create an S3 bucket, an SNS topic, and
an IAM role with attached policies as prerequisites. To set up your prerequisites for AWS Config, see [Prerequisites](gs-cli-prereq.md "gs-cli-prereq.md").

**One customer managed configuration recorder per account per Region**

You can have only one customer managed configuration recorder for each AWS account for each AWS Region.

**One delivery channel per account per Region**

You can have only one delivery channel region for each AWS account for each AWS Region.

**Policies and compliance results**

[IAM policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
and [other policies managed in AWS Organizations](../../../organizations/latest/userguide/orgs_manage_policies.md "../../../organizations/latest/userguide/orgs_manage_policies.md")
can impact whether AWS Config
has permissions to record configuration changes for your resources. Additionally, rules directly evaluate the configuration of a resource and rules don't take into account these policies when running evaluations. Make sure that the policies in effect align with how you intend to use AWS Config.

## Step 1: Run the put-configuration-recorder

Use the [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") command to create a customer managed configuration recorder:

This command uses the `--configuration-recorder` and `---recording-group` fields.

```
$ **aws configservice put-configuration-recorder \
--configuration-recorder `file://configurationRecorder.json` \
--recording-group `file://recordingGroup.json`**
```

**The `configuration-recorder` field**

The `configurationRecorder.json` file specifies `name` and `roleArn` as well as the default recording frequency for the configuration recorder (`recordingMode`).
You can also use this field to override the recording frequency for specific resource types.

```
`{
 "name": "`default`",
 "roleARN": "`arn:aws:iam::123456789012:role/config-role`",
 "recordingMode": {
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "recordingModeOverrides": [
 {
 "description": "`Description you provide for the override`",
 "recordingFrequency": `CONTINUOUS` or `DAILY`,
 "resourceTypes": [ `Comma-separated list of resource types to include in the override` ]
 }
 ]
 }
}`
```

**The `recording-group` field**

The `recordingGroup.json` file specifies which resource types are recorded.

```
`{
 "allSupported": `boolean`,
 "exclusionByResourceTypes": {
 "resourceTypes": [ `Comma-separated list of resource types to exclude` ]
 },
 "includeGlobalResourceTypes": `boolean`,
 "recordingStrategy": {
 "useOnly": "`Recording strategy for the configuration recorder`"
 },
 "resourceTypes": [ `Comma-separated list of resource types to include`]
}`
```

For more information about these fields, see [`put-configuration-recorder`](../../../cli/latest/reference/configservice/put-configuration-recorder.md "../../../cli/latest/reference/configservice/put-configuration-recorder.md") in the _AWS CLI Command Reference_.

## Step 2: Run the put-delivery-channel command

Use the [`put-delivery-channel`](../../../cli/latest/reference/configservice/put-delivery-channel.md "../../../cli/latest/reference/configservice/put-delivery-channel.md") command to create a delivery channel:

This command uses the `--delivery-channel` field.

```
$ **aws configservice put-delivery-channel --delivery-channel file://deliveryChannel.json**
```

**The `delivery-channel` field**

The `deliveryChannel.json` file specifies the following:

- The `name` for the delivery channel.
- The `s3BucketName` where AWS Config sends configuration snapshots.
- The `snsTopicARN` where AWS Config sends notifications
- The `configSnapshotDeliveryProperties` which sets how often AWS Config delivers configuration snapshots and how often it invokes evaluations for periodic rules.

```
`{
 "name": "`default`",
 "s3BucketName": "`config-bucket-123456789012`",
 "snsTopicARN": "`arn:aws:sns:us-east-1:123456789012:config-topic`",
 "configSnapshotDeliveryProperties": {
 "deliveryFrequency": "`Twelve_Hours`"
 }
}`
```

For more information about these fields, see [`put-delivery-channel`](../../../cli/latest/reference/configservice/put-delivery-channel.md "../../../cli/latest/reference/configservice/put-delivery-channel.md") in the _AWS CLI Command Reference_.

## Step 3: Run the start-configuration-recorder command

Use the [`start-configuration-recorder`](../../../cli/latest/reference/configservice/start-configuration-recorder.md "../../../cli/latest/reference/configservice/start-configuration-recorder.md")
command to start AWS Config:

```
$ **aws configservice start-configuration-recorder --configuration-recorder-name `configRecorderName`**
```

For more information about these fields, see [`start-configuration-recorder`](../../../cli/latest/reference/configservice/start-configuration-recorder.md "../../../cli/latest/reference/configservice/start-configuration-recorder.md") in the _AWS CLI Command Reference_.
