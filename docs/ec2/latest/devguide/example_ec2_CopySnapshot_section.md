# Use `CopySnapshot` with a CLI

The following code examples show how to use `CopySnapshot`.

CLI

**AWS CLI**

**Example 1: To copy a snapshot to another Region**

The following `copy-snapshot` example command copies the specified snapshot from the `us-west-2` Region to the `us-east-1` Region and adds a short description.

```
`aws ec2 copy-snapshot \
 --region `us-east-1` \
 --source-region `us-west-2` \
 --source-snapshot-id `snap-066877671789bd71b` \
 --description '`This is my copied snapshot.`'`

```

Output:

```
{
    "SnapshotId": "snap-066877671789bd71b"
}
```

**Example 2: To copy an unencrypted snapshot and encrypt the new snapshot**

The following `copy-snapshot` command copies the specified unencrypted snapshot from the `us-west-2` Region to the current Region and encrypts the new snapshot using the specified KMS key.

```
`aws ec2 copy-snapshot \
 --source-region `us-west-2` \
 --source-snapshot-id `snap-066877671789bd71b` \
 --encrypted \
 --kms-key-id `alias/my-kms-key``

```

Output:

```
{
    "SnapshotId": "snap-066877671789bd71b"
}
```

For more information, see [Copy an Amazon EBS snapshot](../../../ebs/latest/userguide/ebs-copy-snapshot.md "../../../ebs/latest/userguide/ebs-copy-snapshot.md") in the _Amazon EBS User Guide_.

- For API details, see
  [CopySnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-snapshot.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example copies the specified snapshot from the EU (Ireland) region to the US West (Oregon) region.**

```
Copy-EC2Snapshot -SourceRegion eu-west-1 -SourceSnapshotId snap-12345678 -Region us-west-2

```

**Example 2: If you set a default region and omit the Region parameter, the default destination region is the default region.**

```
Set-DefaultAWSRegion us-west-2
Copy-EC2Snapshot -SourceRegion eu-west-1 -SourceSnapshotId snap-12345678

```

- For API details, see
  [CopySnapshot](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example copies the specified snapshot from the EU (Ireland) region to the US West (Oregon) region.**

```
Copy-EC2Snapshot -SourceRegion eu-west-1 -SourceSnapshotId snap-12345678 -Region us-west-2

```

**Example 2: If you set a default region and omit the Region parameter, the default destination region is the default region.**

```
Set-DefaultAWSRegion us-west-2
Copy-EC2Snapshot -SourceRegion eu-west-1 -SourceSnapshotId snap-12345678

```

- For API details, see
  [CopySnapshot](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
