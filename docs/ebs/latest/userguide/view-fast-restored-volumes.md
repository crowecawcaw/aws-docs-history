# View Amazon EBS volumes restored using fast snapshot restore

When you create a volume from a snapshot that is enabled for fast snapshot restore in
the Availability Zone for the volume, it is restored using fast snapshot restore.

AWS CLI

###### To view volumes that were created from a snapshot that is enabled for fast snapshot restore

Use the [describe-volumes](../../../cli/latest/reference/ec2/describe-volumes.md "../../../cli/latest/reference/ec2/describe-volumes.md") command.

```
aws ec2 describe-volumes --filters Name=fast-restored,Values=true
```

The following is example output.

```
{
    "Volumes": [
        {
            "Attachments": [],
            "AvailabilityZone": "us-east-2a",
            "CreateTime": "2020-01-26T00:34:11.093Z",
            "Encrypted": true,
            "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/8c5b2c63-b9bc-45a3-a87a-5513e232e843",
            "Size": 20,
            "SnapshotId": "snap-0abcdef1234567890",
            "State": "available",
            "VolumeId": "vol-01234567890abcdef",
            "Iops": 100,
            "VolumeType": "gp2",
            "FastRestored": true
        }
    ]
}
```

PowerShell

###### To view volumes that were created from a snapshot that is enabled for fast snapshot restore

Use the [Get-EC2Volume](../../../powershell/latest/reference/items/Get-EC2Volume.md "../../../powershell/latest/reference/items/Get-EC2Volume.md") cmdlet.

```
Get-EC2Volume -Filter @{Name="fast-restored"; Values="true"}
```
