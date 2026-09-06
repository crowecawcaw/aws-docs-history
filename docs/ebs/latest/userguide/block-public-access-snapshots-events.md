

# Monitor block public access for Amazon EBS snapshots using EventBridge
<a name="block-public-access-snapshots-events"></a>

Amazon EBS emits events related to block public access for snapshots. You can use AWS Lambda and Amazon EventBridge to handle event notifications programmatically. Events are emitted on a best effort basis. For more information, see the [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The following events are emitted:
+ Enable block public access for snapshots in block all sharing mode

  ```
  {
    "version": "0",
    "id": "{{01234567-0123-0123-0123-012345678901}}",
    "detail-type": "EBS Snapshot Block Public Access Enabled",
    "source": "aws.ec2",
    "account": "{{123456789012}}",
    "time": "{{2019-05-31T21:49:54Z}}",
    "region": "{{us-east-1}}",
    "detail": { 
      "SnapshotBlockPublicAccessState": "block-all-sharing",
      "message": "Block Public Access was successfully enabled in 'block-all-sharing' mode"
    }
  }
  ```
+ Enable block public access for snapshots in block new sharing mode

  ```
  {
    "version": "0",
    "id": "{{01234567-0123-0123-0123-012345678901}}",
    "detail-type": "EBS Snapshot Block Public Access Enabled",
    "source": "aws.ec2",
    "account": "{{123456789012}}",
    "time": "{{2019-05-31T21:49:54Z}}",
    "region": "{{us-east-1}}",
    "detail": { 
      "SnapshotBlockPublicAccessState": "block-new-sharing",
      "message": "Block Public Access was successfully enabled in 'block-new-sharing' mode"
    }
  }
  ```
+ Disable block public access for snapshots

  ```
  {
    "version": "0",
    "id": "{{01234567-0123-0123-0123-012345678901}}",
    "detail-type": "EBS Snapshot Block Public Access Disabled",
    "source": "aws.ec2",
    "account": "{{123456789012}}",
    "time": "{{2019-05-31T21:49:54Z}}",
    "region": "{{us-east-1}}",
    "detail": { 
      "SnapshotBlockPublicAccessState": "unblocked",
      "message": "Block Public Access was successfully disabled"
    }
  }
  ```