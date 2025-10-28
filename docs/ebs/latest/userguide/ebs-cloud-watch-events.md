# Amazon EventBridge events for Amazon EBS

Amazon EBS sends events to Amazon EventBridge for actions performed on volumes and snapshots. With EventBridge,
you can establish rules that trigger programmatic actions in response to these events. For
example, you can create a rule that sends a notification to your email when a snapshot is
enabled for fast snapshot restore.

Events in EventBridge are represented as JSON objects. The fields that are unique to the event are
contained in the "detail" section of the JSON object. The "event" field contains the event name.
The "result" field contains the completed status of the action that triggered the event.
For more information, see [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the _Amazon EventBridge User Guide_.

For more information, see [What Is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the _Amazon EventBridge User Guide_.

###### Events

- [EBS volume events](#volume-events "#volume-events")
- [EBS volume initialization event](#volume-initialization-events "#volume-initialization-events")
- [EBS volume modification events](#volume-modification-events "#volume-modification-events")
- [EBS snapshot events](#snapshot-events "#snapshot-events")
- [EBS Snapshots Archive events](#snapshot-archive-events "#snapshot-archive-events")
- [EBS fast snapshot restore events](#fast-snapshot-restore-events "#fast-snapshot-restore-events")
- [Using AWS Lambda to handle EventBridge events](using_lambda.md "using_lambda.md")

## EBS volume events

Amazon EBS sends events to EventBridge when the following volume events occur.

###### Events

- [createVolume](#create-volume "#create-volume")
- [deleteVolume](#delete-volume "#delete-volume")
- [attachVolume](#attach-fail-key "#attach-fail-key")
- [detachVolume](#detach-volume "#detach-volume")

### Create volume (createVolume)

The `createVolume` event is sent to your AWS account when an action to
create a volume completes. However, it is not saved, logged, or archived. This event
can have a result of either `available` or `failed`. Creation
will fail if an invalid AWS KMS key was provided, as shown in the examples below.

###### Event data

The listing below is an example of a JSON object emitted by EBS for a
successful `createVolume` event.

```
{
   "version": "0",
   "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
   "detail-type": "EBS Volume Notification",
   "source": "aws.ec2",
   "account": "`012345678901`",
   "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
   "region": "`us-east-1`",
   "resources": [
      "arn:aws:ec2:`us-east-1`:`012345678901`:volume/vol-`01234567`"
   ],
   "detail": {
      "result": "available",
      "cause": "",
      "event": "createVolume",
      "request-id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`"
   }
}
```

The listing below is an example of a JSON object emitted by EBS after a failed
`createVolume` event. The cause for the failure was a disabled KMS key.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`",
  "detail-type": "EBS Volume Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`sa-east-1`",
  "resources": [
    "arn:aws:ec2:`sa-east-1`:`0123456789ab`:volume/vol-`01234567`",
  ],
  "detail": {
    "event": "createVolume",
    "result": "failed",
    "cause": "arn:aws:kms:`sa-east-1`:`0123456789ab`:key/`01234567`-`0123`-`0123`-`0123`-`0123456789ab` is disabled.",
    "request-id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`",
  }
}
```

The following is an example of a JSON object that is emitted by EBS after a failed
`createVolume` event. The cause for the failure was a KMS key pending
import.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`",
  "detail-type": "EBS Volume Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`sa-east-1`",
  "resources": [
    "arn:aws:ec2:`sa-east-1`:`0123456789ab`:volume/vol-`01234567`",
  ],
  "detail": {
    "event": "createVolume",
    "result": "failed",
    "cause": "arn:aws:kms:`sa-east-1`:`0123456789ab`:key/`01234567`-`0123`-`0123`-`0123`-`0123456789ab` is pending import.",
    "request-id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`",
  }
}
```

### Delete volume (deleteVolume)

The `deleteVolume` event is sent to your AWS account when an action to
delete a volume completes. However, it is not saved, logged, or archived. This event
has the result `deleted`. If the deletion does not complete, the event is
never sent.

###### Event data

The listing below is an example of a JSON object emitted by EBS for a
successful `deleteVolume` event.

```
{
   "version": "0",
   "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
   "detail-type": "EBS Volume Notification",
   "source": "aws.ec2",
   "account": "`012345678901`",
   "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
   "region": "`us-east-1`",
   "resources": [
      "arn:aws:ec2:`us-east-1`:`012345678901`:volume/vol-`01234567`"
   ],
   "detail": {
      "result": "deleted",
      "cause": "",
      "event": "deleteVolume",
      "request-id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`"
   }
}
```

### Volume attach or reattach (attachVolume, reattachVolume)

The `attachVolume` or `reattachVolume` event is sent to your
AWS account when a volume is attached or reattached to an instance. However, it is
not saved, logged, or archived. If you use a KMS key to encrypt an EBS volume and
the KMS key becomes invalid, EBS will emit an event if that KMS key is later used
to attach or reattach to an instance, as shown in the examples below.

###### Event data

The listing below is an example of a JSON object emitted by EBS after a failed
`attachVolume` event. The cause for the failure was a KMS key
pending deletion.

###### Note

AWS may attempt to reattach to a volume following routine server
maintenance.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`",
  "detail-type": "EBS Volume Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
  "arn:aws:ec2:`us-east-1`:`0123456789ab`:volume/vol-`01234567`",
  "arn:aws:kms:`us-east-1`:`0123456789ab`:key/`01234567`-`0123`-`0123`-`0123`-`0123456789ab`"
  ],
  "detail": {
    "event": "attachVolume",
    "result": "failed",
    "cause": "arn:aws:kms:`us-east-1`:`0123456789ab`:key/`01234567`-`0123`-`0123`-`0123`-`0123456789ab` is pending deletion.",
    "request-id": ""
  }
}
```

The listing below is an example of a JSON object emitted by EBS after a failed
`reattachVolume` event. The cause for the failure was a KMS key
pending deletion.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`",
  "detail-type": "EBS Volume Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
  "arn:aws:ec2:`us-east-1`:`0123456789ab`:volume/vol-`01234567`",
  "arn:aws:kms:`us-east-1`:`0123456789ab`:key/`01234567`-`0123`-`0123`-`0123`-`0123456789ab`"
  ],
  "detail": {
    "event": "reattachVolume",
    "result": "failed",
    "cause": "arn:aws:kms:`us-east-1`:`0123456789ab`:key/`01234567`-`0123`-`0123`-`0123`-`0123456789ab` is pending deletion.",
    "request-id": ""
  }
}
```

### Detach volume (detachVolume)

The `detachVolume` event is sent to your AWS account when a volume
is detached from an Amazon EC2 instance.

###### Event data

The following is an example of a successful `detachVolume` event.

```
{
  "version":"0",
  "id":"`2ec37298-1234-e436-70fc-c96b1example`",
  "detail-type":"AWS API Call via CloudTrail",
  "source":"aws.ec2",
  "account":"`123456789012`",
  "time":"`2024-03-18T16:35:52Z`",
  "region":"`us-east-1`",
  "resources":[],
  "detail":
  {
    "eventVersion":"1.09",
    "userIdentity":
    {
      "type":"IAMUser",
      "principalId":"`AIDAJT12345SQ2EXAMPLE`",
      "arn":"`arn:aws:iam::123456789012:user/administrator"`,
      "accountId":"`123456789012"`,
      "accessKeyId":"`AKIAJ67890A6EXAMPLE"`,
      "userName":"`administrator`"
    },
    "eventTime":"`2024-03-18T16:35:52Z`",
    "eventSource":"ec2.amazonaws.com",
    "eventName":"DetachVolume",
    "awsRegion":"`us-east-1`",
    "sourceIPAddress":"`12.12.123.12`",
    "userAgent":"aws-cli/2.7.12 Python/3.9.11 Windows/10 exe/AMD64 prompt/off command/ec2.detach-volume",
    "requestParameters":
    {
      "volumeId":"`vol-072577c46bexample`",
      "force":false
    },
    "responseElements":
    {
      "requestId":"`1234513a-6292-49ea-83f8-85e95example`",
      "volumeId":"`vol-072577c46bexample`",
      "instanceId":"`i-0217f7eb3dexample`",
      "device":"`/dev/sdb`",
      "status":"detaching",
      "attachTime":`1710776815000`
    },
    "requestID":"`1234513a-6292-49ea-83f8-85e95example`",
    "eventID":"`1234551d-a15a-43eb-9e69-c983aexample`",
    "readOnly":false,
    "eventType":"AwsApiCall",
    "managementEvent":true,
    "recipientAccountId":"`123456789012`",
    "eventCategory":"Management",
    "tlsDetails":
    {
      "tlsVersion":"TLSv1.3",
      "cipherSuite":"TLS_AES_128_GCM_SHA256",
      "clientProvidedHostHeader":"`ec2.us-east-1.amazonaws.com`"
    }
  }
}
```

## EBS volume initialization event

When you create an Amazon EBS volume from a snapshot and use the default volume initialization rate
or an Amazon EBS Provisioned Rate for Volume Initialization, the `initializeVolume` event
is sent to your AWS account within five minutes after volume initialization completes. For more
information, see [Use an Amazon EBS Provisioned Rate for Volume Initialization](initalize-volume.md#volume-initialization-rate "initalize-volume.md#volume-initialization-rate").

The event is **not** sent for volumes created using Fast Snapshot
Restore.

###### Important

`completionTime` reflects when we generated the event. Because the event is
generated within 5 minutes after initialization completes, the `completionTime`
can be up to five minutes after the initialization completed.

The following is an example event.

```
{
   "version": "0",
   "id": "`01234567-0123-0123-0123-012345678901`",
   "detail-type": "EBS Volume Notification",
   "source": "aws.ec2",
   "account": "`012345678901`",
   "time": "`yyyy-mm-ddThh:mm:ssZ`",
   "region": "`us-east-1`",
   "resources": [
      "`arn:aws:ec2:us-east-1:012345678901:volume/vol-01234567890abcdef`"
   ],
   "detail": {
      "event": " initializeVolume",
      "result": "succeeded",
      "completionTime": "`yyyy-mm-ddThh:mm:ssZ`",
      "request-id": "`01234567-0123-0123-0123-0123456789ab`"
   }
}
```

## EBS volume modification events

Amazon EBS sends `modifyVolume` events to EventBridge when a volume is modified.
However, it is not saved, logged, or archived.

```
{
   "version": "0",
   "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
   "detail-type": "EBS Volume Notification",
   "source": "aws.ec2",
   "account": "`012345678901`",
   "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
   "region": "`us-east-1`",
   "resources": [
      "arn:aws:ec2:`us-east-1`:`012345678901`:volume/vol-`03a55cf56513fa1b6`"
   ],
   "detail": {
      "result": "`optimizing`",
      "cause": "",
      "event": "modifyVolume",
      "request-id": "`01234567`-`0123`-`0123`-`0123`-`0123456789ab`"
   }
}
```

## EBS snapshot events

Amazon EBS sends events to EventBridge when the following volume events occur.

###### Events

- [createSnapshot](#create-snapshot-complete "#create-snapshot-complete")
- [createSnapshots](#create-snapshots-complete "#create-snapshots-complete")
- [copySnapshot](#copy-snapshot-complete "#copy-snapshot-complete")
- [shareSnapshot](#snapshot-shared "#snapshot-shared")

### Create snapshot (createSnapshot)

The `createSnapshot` event is sent to your AWS account when an action
to create a snapshot completes. However, it is not saved, logged, or archived. This
event can have a result of either `succeeded` or
`failed`.

###### Event data

The listing below is an example of a JSON object emitted by EBS for a
successful `createSnapshot` event. In the `detail`
section, the `source` field contains the ARN of the source volume.
The `startTime` and `endTime` fields indicate when
creation of the snapshot started and completed.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
     "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`"
  ],
  "detail": {
    "event": "createSnapshot",
    "result": "succeeded",
    "cause": "",
    "request-id": "",
    "snapshot_id": "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`",
    "source": "arn:aws:ec2::`us-west-2`:volume/vol-`01234567`",
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z"  }
}
```

### Create snapshots (createSnapshots)

The `createSnapshots` event is sent to your AWS account when an action
to create a multi-volume snapshot completes. This event can have a result of either
`succeeded` or `failed`.

###### Event data

The listing below is an example of a JSON object emitted by EBS for a
successful `createSnapshots` event. In the `detail`
section, the `source` field contains the ARNs of the source volumes
of the multi-volume snapshot set. The `startTime` and
`endTime` fields indicate when creation of the snapshot started
and completed.

```
{
  "version": "0",
  "id": "`01234567-0123-0123-0123-012345678901`",
  "detail-type": "EBS Multi-Volume Snapshots Completion Status",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-east-1`:snapshot/snap-`01234567`",
    "arn:aws:ec2::`us-east-1`:snapshot/snap-`012345678`"
  ],
  "detail": {
    "event": "createSnapshots",
    "result": "succeeded",
    "cause": "",
    "request-id": "",
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "snapshots": [
      {
        "snapshot_id": "arn:aws:ec2::`us-east-1`:snapshot/snap-`01234567`",
        "source": "arn:aws:ec2::`us-east-1`:volume/vol-`01234567`",
        "status": "completed"
      },
      {
        "snapshot_id": "arn:aws:ec2::`us-east-1`:snapshot/snap-`012345678`",
        "source": "arn:aws:ec2::`us-east-1`:volume/vol-`012345678`",
        "status": "completed"
      }
    ]
  }
}
```

The listing below is an example of a JSON object emitted by EBS after a failed
`createSnapshots` event. The cause for the failure was one or more
snapshots for the multi-volume snapshot set failed to complete. The values of
`snapshot_id` are the ARNs of the failed snapshots. `startTime`
and `endTime` represent when the create-snapshots action started and
ended.

```
{
  "version": "0",
  "id": "`01234567-0123-0123-0123-012345678901`",
  "detail-type": "EBS Multi-Volume Snapshots Completion Status",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy-mm-ddThh:mm:ssZ`",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-east-1`:snapshot/`snap-01234567`",
    "arn:aws:ec2::`us-east-1`:snapshot/`snap-012345678`"
  ],
"detail": {
    "event": "createSnapshots",
    "result": "failed",
    "cause": "Snapshot snap-01234567 is in status error",
   "request-id": "",
    "startTime": "`yyyy-mm-ddThh:mm:ssZ`",
    "endTime": "`yyyy-mm-ddThh:mm:ssZ`",
    "snapshots": [
      {
        "snapshot_id": "arn:aws:ec2::`us-east-1`:snapshot/`snap-01234567`",
        "source": "arn:aws:ec2::`us-east-1`:volume/`vol-01234567`",
        "status": "error"
      },
      {
        "snapshot_id": "arn:aws:ec2::`us-east-1`:snapshot/`snap-012345678`",
        "source": "arn:aws:ec2::`us-east-1`:volume/`vol-012345678`",
        "status": "error"
      }
    ]
  }
}

```

### Copy snapshot (copySnapshot)

The `copySnapshot` event is sent to your AWS account when an action to
copy a snapshot completes. However, it is not saved, logged, or archived. This event
can have a result of either `succeeded` or `failed`.

In the `detail` section, `source` is the ARN of the source
snapshot, and `snapshot_id` is the ARN of the snapshot copy. `startTime`
and `endTime` indicate when the copy operation started and ended.
`incremental` indicates whether the snapshot copy is an incremental snapshot
(`true`), or a full snapshot (`false`). `transferType`
indicates whether the snapshot copy operation was a standard copy operation or a
time-based copy operation. For more information, see [Time-based copies for Amazon EBS snapshots and EBS-backed AMIs](time-based-copies.md "time-based-copies.md").

If you are copying the snapshot across Regions, then the event is emitted in
the destination Region.

###### Scenario 1: Standard snapshot copy operation completes

The following is an example of an event that is sent to your account when a
standard snapshot copy operation completes successfully. Note that `transferType`
is `standard`.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`123456789012`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`"
  ],
  "detail": {
    "event": "copySnapshot",
    "result": "succeeded",
    "cause": "",
    "request-id": "",
    "snapshot_id": "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`",
    "source": "arn:aws:ec2::`eu-west-1`:snapshot/snap-`76543210`",
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "incremental": "true",
    "transferType": "standard"
  }
}
```

###### Scenario 2: Time-based snapshot copy operation completes within completion duration

The following is an example of an event that is sent to your account when a time-based
snapshot copy operation completes within its completion duration. Note that
`transferType` is `time-based` to indicate that it was a
time-based snapshot copy operation. `completionDurationStartTime` indicates
when the completion duration started.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`123456789012`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`"
  ],
  "detail": {
    "event": "copySnapshot",
    "result": "succeeded",
    "cause": "",
    "request-id": "",
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "snapshot_id": "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`",
    "source": "arn:aws:ec2::`eu-west-1`:snapshot/snap-`76543210`",
    "incremental": "true",
    "completionDurationStartTime":"2024-11-16T06:27:33.816Z",
    "transferType": "time-based"
  }
}
```

###### Scenario 3: Time-based snapshot copy operation completes but misses the requested completion duration

When a time-based snapshot copy operation completes, but fails to meet the requested
completion duration, CloudWatch sends two events to your account. The following are examples
of those events.

- The first event is sent to your account as soon as the completion duration is missed, even
  if the copy operation is still in progress. For this event, the `detail-type` is
  `EBS Copy Snapshot Missed Completion Duration`, and `missedCompletionDurationCause`
  provides the reason.

```
{
 "version":"0",
 "id":"`fd90eb95-0938-e02c-cf55-b81363b8ac12`",
 "detail-type":"EBS Copy Snapshot Missed Completion Duration",
 "source":"aws.ec2",
 "account":"`123456789012`",
 "time":"`2024-11-19T18:17:08Z`",
 "region":"`us-east-1`",
 "resources": ["arn:aws:ec2:`us-east-1`:`123456789012`:snapshot/`snap-01234567890abcedf`"],
 "detail":{
   "event":"copySnapshot",
   "missedCompletionDurationCause":"`Snapshot copy was not able to meet the specified completion duration because your snapshot copy operation throughput quota was exceeded.`",
   "snapshot_id":"arn:aws:ec2:`us-east-1`:`123456789012`:snapshot/`snap-01234567890abcedf`",
   "source":"arn:aws:ec2:`us-east-1`:`123456789012`:snapshot/`snap-00987654321fedcba`",
   "startTime": "`Sun Nov 24 22:32:55 UTC 2024`",
   "transferType": "time-based"
   }
}
```

- The second event is sent to your account only once the snapshot is completed. The event includes
  `missedCompletionDurationCause`, which provides the reason.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`123456789012`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`"
  ],
  "detail": {
    "event": "copySnapshot",
    "result": "succeeded",
    "cause": "",
    "request-id": "",
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "snapshot_id": "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`",
    "source": "arn:aws:ec2::`eu-west-1`:snapshot/snap-`76543210`",
    "incremental": "true",
    "completionDurationStartTime":"2024-11-16T06:27:33.816Z",
    "missedCompletionDurationCause":"`Snapshot copy was not able to meet the specified completion duration because your snapshot copy operation throughput quota was exceeded.`",
    "transferType": "time-based"
  }
}
```

###### Scenario 4: Snapshot copy operation fails

The following is an example of an event that is sent to your account when a
snapshot copy operation fails. Note that `result` is `failed`
to indicate that the operation failed.

```
{
  "version": "0",
  "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`123456789012`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`"
  ],
  "detail": {
    "event": "copySnapshot",
    "result": "failed",
    "cause": "Source snapshot ID is not valid",
    "request-id": "",
    "snapshot_id": "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`",
    "source": "arn:aws:ec2::`eu-west-1`:snapshot/snap-`76543210`",
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z"
  }
}
```

### Share snapshot (shareSnapshot)

The `shareSnapshot` event is sent to your AWS account when another
account shares a snapshot with it. However, it is not saved, logged, or archived. The
result is always `succeeded`.

###### Event data

The following is an example of a JSON object emitted by EBS after a completed
`shareSnapshot` event. In the `detail` section, the
value of `source` is the AWS account number of the user that shared
the snapshot with you. `startTime` and `endTime` represent
when the share-snapshot action started and ended. The `shareSnapshot`
event is emitted only when a private snapshot is shared with another user.
Sharing a public snapshot does not trigger the event.

```
{
  "version": "0",
  "id": "`01234567`-`01234`-`0123`-`0123`-`012345678901`",
  "detail-type": "EBS Snapshot Notification",
  "source": "aws.ec2",
  "account": "`012345678901`",
  "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
  "region": "`us-east-1`",
  "resources": [
    "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`"
  ],
  "detail": {
    "event": "shareSnapshot",
    "result": "succeeded",
    "cause": "",
    "request-id": "",
    "snapshot_id": "arn:aws:ec2::`us-west-2`:snapshot/snap-`01234567`",
    "source": `012345678901`,
    "startTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "endTime": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z"
  }
}
```

## EBS Snapshots Archive events

Amazon EBS emits events related to snapshot archiving actions. For more information, see
[Monitor Amazon EBS snapshot archiving using CloudWatch Events](monitor-snapshot-archiving.md "monitor-snapshot-archiving.md").

## EBS fast snapshot restore events

Amazon EBS sends events to EventBridge when the state of fast snapshot restore for a snapshot changes. Events are emitted on a best effort basis.

The following is example data for this event.

```
{
   "version": "0",
   "id": "`01234567`-`0123`-`0123`-`0123`-`012345678901`",
   "detail-type": "EBS Fast Snapshot Restore State-change Notification",
   "source": "aws.ec2",
   "account": "`123456789012`",
   "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
   "region": "`us-east-1`",
   "resources": [
      "arn:aws:ec2:`us-east-1`::snapshot/snap-`03a55cf56513fa1b6`"
   ],
   "detail": {
      "snapshot-id": "snap-`1234567890abcdef0`",
      "state": "`optimizing`",
      "zone": "`us-east-1a`",
      "message": "`Client.UserInitiated - Lifecycle state transition`",
   }
}
```

The possible values for `state` are `enabling`, `optimizing`,
`enabled`, `disabling`, and `disabled`.

The possible values for `message` are as follows:

`Client.InvalidSnapshot.InvalidState - The requested snapshot transitioned to an invalid state (Error)`

A request to enable fast snapshot restore failed and the state transitioned
to `disabling` or `disabled`. Fast snapshot restore
cannot be enabled for this snapshot.

`Client.UserInitiated`

The state successfully transitioned to `enabling` or
`disabling`.

`Client.UserInitiated - Lifecycle state transition`

The state successfully transitioned to `optimizing`,
`enabled`, or `disabled`.

`Server.InsufficientCapacity - There was insufficient capacity available to satisfy the request`

A request to enable fast snapshot restore failed due to insufficient capacity,
and the state transitioned to `disabling` or `disabled`.
Wait and then try again.

`Server.InternalError - An internal error caused the operation to fail`

A request to enable fast snapshot restore failed due to an internal error,
and the state transitioned to `disabling` or `disabled`.
Wait and then try again.

`Client.InvalidSnapshot.InvalidState - The requested snapshot 
 was deleted or access permissions were revoked`

The fast snapshot restore state for the snapshot has transitioned to
`disabling` or `disabled` because the
snapshot was deleted or unshared by the snapshot owner. Fast
snapshot restore cannot be enabled for a snapshot that has been
deleted or is no longer shared with you.
