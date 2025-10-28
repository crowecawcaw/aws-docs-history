# Monitor EC2 Fast Launch

This section covers how to monitor the Amazon EC2 Windows Server AMIs in your
account that have EC2 Fast Launch enabled.

## Monitor EC2 Fast Launch state changes with EventBridge

When the state changes for a Windows AMI with EC2 Fast Launch enabled, Amazon EC2 generates an
`EC2 Fast Launch State-change Notification` event. Then Amazon EC2 sends the
state change event to Amazon EventBridge (formerly known as Amazon CloudWatch Events).

You can create EventBridge rules that trigger one or more actions in response to the
state change event. For example, you can create an EventBridge rule that detects when EC2 Fast Launch
is enabled and performs the following actions:

- Sends a message to an Amazon SNS topic that notifies its subscribers.
- Invokes a Lambda function that performs some action.
- Sends the state change data to Amazon Data Firehose for analytics.

For more information, see [Creating Amazon EventBridge rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md")
in the _Amazon EventBridge User Guide_.

###### State change events

The EC2 Fast Launch feature emits JSON formatted state change events on a
best-effort basis. Amazon EC2 sends the events to EventBridge in near real time. This section
describes the event fields and shows an example of the event format.

**`EC2 Fast Launch State-change Notification`**

**imageId**

Identifies the AMI with the EC2 Fast Launch state change.

**resourceType**

The type of resource to use for pre-provisioning. Supported value: `snapshot`.
The default value is `snapshot`.

**state**

The current state of the EC2 Fast Launch feature for the specified AMI.
Valid values include the following:

- **enabling** – You've enabled the
  EC2 Fast Launch feature for the AMI, and Amazon EC2 has started
  creating snapshots for the pre-provisioning process.
- **enabling-failed** – Something went
  wrong that caused the pre-provisioning process to fail the first time that
  you enabled the EC2 Fast Launch for an AMI. This can
  happen anytime during the pre-provisioning process.
- **enabled** – The
  EC2 Fast Launch feature is enabled. The state changes to
  `enabled` as soon as Amazon EC2 creates the first pre-provisioned
  snapshot for a newly enabled EC2 Fast Launch AMI. If the AMI was
  already enabled and goes through pre-provisioning again, the state change
  happens right away.
- **enabled-failed** – This state
  applies only if this is not the first time your EC2 Fast Launch AMI goes
  through the pre-provisioning process. This can happen if the
  EC2 Fast Launch feature is disabled and then later enabled again,
  or if there is a configuration change or other error after pre-provisioning
  is completed for the first time.
- **disabling** – The AMI owner has turned
  off the EC2 Fast Launch feature for the AMI, and Amazon EC2 has started
  the clean up process.
- **disabled** – The
  EC2 Fast Launch feature is disabled. The state changes to
  `disabled` as soon as Amazon EC2 completes the clean up process.
- **disabling-failed** – Something
  went wrong that caused the clean up process to fail. This means that some
  pre-provisioned snapshots may still remain in the account.

**stateTransitionReason**

The reason that the state changed for the EC2 Fast Launch AMI.

###### Note

All fields in this event message are required.

The following example shows a newly enabled EC2 Fast Launch AMI that has launched
the first instance to start the pre-provisioning process. At this point, the state is
`enabling`. After Amazon EC2 creates the first pre-provisioned snapshot, the
state changes to `enabled`.

```
{
	"version": "0",
	"id": "01234567-0123-0123-0123-012345678901",
	"detail-type": "EC2 Fast Launch State-change Notification",
	"source": "aws.ec2",
	"account": "123456789012",
	"time": "2022-08-31T20:30:12Z",
	"region": "us-east-1",
	"resources": [
		"arn:aws:ec2:us-east-1:123456789012:image/ami-123456789012"
	],
	"detail": {
		"imageId": "ami-123456789012",
		"resourceType": "snapshot",
		"state": "enabling",
		"stateTransitionReason": "Client.UserInitiated"
	}
}
```

## Monitor EC2 Fast Launch metrics with CloudWatch

Amazon EC2 AMIs with EC2 Fast Launch enabled send metrics to Amazon CloudWatch. You can use the AWS Management Console, the AWS CLI,
or an API to list the metrics that EC2 Fast Launch sends to CloudWatch. The `AWS/EC2`
namespace includes the following EC2 Fast Launch metrics:

| Metric                                  | Description                                                                                                                                                 |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NumberOfAvailableFastLaunchSnapshots    | The number of pre-provisioned snapshots available per EC2 Fast Launch enabled AMI.                                                                          |
| NumberOfInstancesFastLaunched           | The number of instances per EC2 Fast Launch enabled AMI that were launched from pre-provisioned snapshots.                                                  |
| NumberOfInstancesNotFastLaunched        | The number of instances per EC2 Fast Launch enabled AMI that resulted in a cold boot due to the lack of available pre-provisioned snapshots at launch time. |
| FastLaunchSnapshotUsedToRefillStartTime | The timestamp when Amazon EC2 launched a new image from a EC2 Fast Launch enabled AMI to create another snapshot after an existing snapshot was used.       |
| FastLaunchSnapshotCreationTime          | Measures the time it took for Amazon EC2 to launch an instance and create a snapshot for a EC2 Fast Launch enabled AMI.                                     |
