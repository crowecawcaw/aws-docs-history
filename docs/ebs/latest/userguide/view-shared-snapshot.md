# Use Amazon EBS snapshots that are shared with you

###### To use a shared unencrypted snapshot

Locate the shared snapshot by ID or description. You can use this snapshot as
you would any other snapshot that you own in your account. For example, you can
create a volume from the snapshot or copy it to a different Region.

###### To use a shared encrypted snapshot

Locate the shared snapshot by ID or description. Create a copy of the shared
snapshot in your account, and encrypt the copy with a KMS key that you own. You
can then use the copy to create volumes or you can copy it to different Regions.

Console

###### To view snapshot permissions

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**.
3. Select the snapshot.
4. If the filter is **Owned by me**, the snapshot is owned by
   this account. If the filter is **Private snapshots**, the
   snapshot is either owned by this account or shared specifically with this
   account. Select a snapshot and on the **Details** tab, check whether
   **Owner** specifies this account or a different account.

AWS CLI

###### To view snapshot permissions

Use the [describe-snapshot-attribute](../../../cli/latest/reference/ec2/describe-snapshot-attribute.md "../../../cli/latest/reference/ec2/describe-snapshot-attribute.md")
command to get the snapshot permissions of the specified snapshot.

```
aws ec2 describe-snapshot-attribute \
    --snapshot-id `snap-0abcdef1234567890` \
    --attribute createVolumePermission
```

The following is example output.

```
{
    "SnapshotId": "snap-0abcdef1234567890",
    "CreateVolumePermissions": [
        {
            "UserId": "111122223333"
        }
    ]
}
```

PowerShell

###### To view snapshot permissions

Use the [Get-EC2SnapshotAttribute](../../../powershell/latest/reference/items/Get-EC2SnapshotAttribute.md "../../../powershell/latest/reference/items/Get-EC2SnapshotAttribute.md")
cmdlet.

```
(Get-EC2SnapshotAttribute `
    -SnapshotId `snap-0abcdef1234567890` `
    -Attribute createVolumePermission).CreateVolumePermissions
```

The following is example output.

```
Group UserId
----- ------
      111122223333
```
