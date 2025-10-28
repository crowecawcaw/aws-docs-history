# Use `CreateVolume` with a CLI

The following code examples show how to use `CreateVolume`.

CLI

**AWS CLI**

**To create an empty General Purpose SSD (gp2) volume**

The following `create-volume` example creates an 80 GiB General Purpose SSD (gp2) volume in the specified Availability Zone. Note that the current Region must be `us-east-1`, or you can add the `--region` parameter to specify the Region for the command.

```
`aws ec2 create-volume \
 --volume-type `gp2` \
 --size `80` \
 --availability-zone `us-east-1a``

```

Output:

```
{
    "AvailabilityZone": "us-east-1a",
    "Tags": [],
    "Encrypted": false,
    "VolumeType": "gp2",
    "VolumeId": "vol-1234567890abcdef0",
    "State": "creating",
    "Iops": 240,
    "SnapshotId": "",
    "CreateTime": "YYYY-MM-DDTHH:MM:SS.000Z",
    "Size": 80
}
```

If you do not specify a volume type, the default volume type is `gp2`.

```
`aws ec2 create-volume \
 --size `80` \
 --availability-zone `us-east-1a``

```

**Example 2: To create a Provisioned IOPS SSD (io1) volume from a snapshot**

The following `create-volume` example creates a Provisioned IOPS SSD (io1) volume with 1000 provisioned IOPS in the specified Availability Zone using the specified snapshot.

```
`aws ec2 create-volume \
 --volume-type `io1` \
 --iops `1000` \
 --snapshot-id `snap-066877671789bd71b` \
 --availability-zone `us-east-1a``

```

Output:

```
{
    "AvailabilityZone": "us-east-1a",
    "Tags": [],
    "Encrypted": false,
    "VolumeType": "io1",
    "VolumeId": "vol-1234567890abcdef0",
    "State": "creating",
    "Iops": 1000,
    "SnapshotId": "snap-066877671789bd71b",
    "CreateTime": "YYYY-MM-DDTHH:MM:SS.000Z",
    "Size": 500
}
```

**Example 3: To create an encrypted volume**

The following `create-volume` example creates an encrypted volume using the default CMK for EBS encryption. If encryption by default is disabled, you must specify the `--encrypted` parameter as follows.

```
`aws ec2 create-volume \
 --size `80` \
 --encrypted \
 --availability-zone `us-east-1a``

```

Output:

```
{
    "AvailabilityZone": "us-east-1a",
    "Tags": [],
    "Encrypted": true,
    "VolumeType": "gp2",
    "VolumeId": "vol-1234567890abcdef0",
    "State": "creating",
    "Iops": 240,
    "SnapshotId": "",
    "CreateTime": "YYYY-MM-DDTHH:MM:SS.000Z",
    "Size": 80
}
```

If encryption by default is enabled, the following example command creates an encrypted volume, even without the `--encrypted` parameter.

```
`aws ec2 create-volume \
 --size `80` \
 --availability-zone `us-east-1a``

```

If you use the `--kms-key-id` parameter to specify a customer managed CMK, you must specify the `--encrypted` parameter even if encryption by default is enabled.

```
`aws ec2 create-volume \
 --volume-type `gp2` \
 --size `80` \
 --encrypted \
 --kms-key-id `0ea3fef3-80a7-4778-9d8c-1c0c6EXAMPLE` \
 --availability-zone `us-east-1a``

```

**Example 4: To create a volume with tags**

The following `create-volume` example creates a volume and adds two tags.

```
`aws ec2 create-volume \
 --availability-zone `us-east-1a` \
 --volume-type `gp2` \
 --size `80` \
 --tag-specifications '`ResourceType=volume,Tags=[{Key=purpose,Value=production},{Key=cost-center,Value=cc123}]`'`

```

- For API details, see
  [CreateVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-volume.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-volume.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates the specified volume.**

```
New-EC2Volume -Size 50 -AvailabilityZone us-west-2a -VolumeType gp2

```

**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2a
CreateTime       : 12/22/2015 1:42:07 AM
Encrypted        : False
Iops             : 150
KmsKeyId         :
Size             : 50
SnapshotId       :
State            : creating
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : gp2
```

**Example 2: This example request creates a volume and applies a tag with a key of stack and a value of production.**

```
$tag = @{ Key="stack"; Value="production" }

$tagspec = new-object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "volume"
$tagspec.Tags.Add($tag)

New-EC2Volume -Size 80 -AvailabilityZone "us-west-2a" -TagSpecification $tagspec

```

- For API details, see
  [CreateVolume](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates the specified volume.**

```
New-EC2Volume -Size 50 -AvailabilityZone us-west-2a -VolumeType gp2

```

**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2a
CreateTime       : 12/22/2015 1:42:07 AM
Encrypted        : False
Iops             : 150
KmsKeyId         :
Size             : 50
SnapshotId       :
State            : creating
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : gp2
```

**Example 2: This example request creates a volume and applies a tag with a key of stack and a value of production.**

```
$tag = @{ Key="stack"; Value="production" }

$tagspec = new-object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "volume"
$tagspec.Tags.Add($tag)

New-EC2Volume -Size 80 -AvailabilityZone "us-west-2a" -TagSpecification $tagspec

```

- For API details, see
  [CreateVolume](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
