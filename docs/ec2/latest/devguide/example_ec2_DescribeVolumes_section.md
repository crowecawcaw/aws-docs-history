# Use `DescribeVolumes` with a CLI

The following code examples show how to use `DescribeVolumes`.

CLI

**AWS CLI**

**Example 1: To describe a volume**

The following `describe-volumes` example describes the specified volumes in the current Region.

```
`aws ec2 describe-volumes \
 --volume-ids `vol-049df61146c4d7901` `vol-1234567890abcdef0``

```

Output:

```
{
    "Volumes": [
        {
            "AvailabilityZone": "us-east-1a",
            "Attachments": [
                {
                    "AttachTime": "2013-12-18T22:35:00.000Z",
                    "InstanceId": "i-1234567890abcdef0",
                    "VolumeId": "vol-049df61146c4d7901",
                    "State": "attached",
                    "DeleteOnTermination": true,
                    "Device": "/dev/sda1"
                }
            ],
            "Encrypted": true,
            "KmsKeyId": "arn:aws:kms:us-east-2a:123456789012:key/8c5b2c63-b9bc-45a3-a87a-5513eEXAMPLE,
            "VolumeType": "gp2",
            "VolumeId": "vol-049df61146c4d7901",
            "State": "in-use",
            "Iops": 100,
            "SnapshotId": "snap-1234567890abcdef0",
            "CreateTime": "2019-12-18T22:35:00.084Z",
            "Size": 8
        },
        {
            "AvailabilityZone": "us-east-1a",
            "Attachments": [],
            "Encrypted": false,
            "VolumeType": "gp2",
            "VolumeId": "vol-1234567890abcdef0",
            "State": "available",
            "Iops": 300,
            "SnapshotId": "",
            "CreateTime": "2020-02-27T00:02:41.791Z",
            "Size": 100
        }
    ]
}
```

**Example 2: To describe volumes that are attached to a specific instance**

The following `describe-volumes` example describes all volumes that are both attached to the specified instance and set to delete when the instance terminates.

```
`aws ec2 describe-volumes \
 --region `us-east-1` \
 --filters `Name=attachment.instance-id,Values=i-1234567890abcdef0` `Name=attachment.delete-on-termination,Values=true``

```

For an example of the output for `describe-volumes`, see Example 1.

**Example 3: To describe available volumes in a specific Availability Zone**

The following `describe-volumes` example describes all volumes that have a status of `available` and are in the specified Availability Zone.

```
`aws ec2 describe-volumes \
 --filters `Name=status,Values=available` `Name=availability-zone,Values=us-east-1a``

```

For an example of the output for `describe-volumes`, see Example 1.

**Example 4: To describe volumes based on tags**

The following `describe-volumes` example describes all volumes that have the tag key `Name` and a value that begins with `Test`. The output is then filtered with a query that displays only the tags and IDs of the volumes.

```
`aws ec2 describe-volumes \
 --filters `Name=tag:Name,Values=Test*` \
 --query `"Volumes[*].{ID:VolumeId,Tag:Tags}"``

```

Output:

```
[
    {
       "Tag": [
           {
               "Value": "Test2",
               "Key": "Name"
           }
       ],
       "ID": "vol-1234567890abcdef0"
   },
   {
       "Tag": [
           {
               "Value": "Test1",
               "Key": "Name"
           }
       ],
       "ID": "vol-049df61146c4d7901"
    }
]
```

For additional examples using tag filters, see [Working with tags](../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI "../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI") in the _Amazon EC2 User Guide_.

- For API details, see
  [DescribeVolumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified EBS volume.**

```
Get-EC2Volume -VolumeId vol-12345678

```

**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2c
CreateTime       : 7/17/2015 4:35:19 PM
Encrypted        : False
Iops             : 90
KmsKeyId         :
Size             : 30
SnapshotId       : snap-12345678
State            : in-use
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : standard
```

**Example 2: This example describes your EBS volumes that have the status 'available'.**

```
Get-EC2Volume -Filter @{ Name="status"; Values="available" }

```

**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2c
CreateTime       : 12/21/2015 2:31:29 PM
Encrypted        : False
Iops             : 60
KmsKeyId         :
Size             : 20
SnapshotId       : snap-12345678
State            : available
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : gp2
...
```

**Example 3: This example describes all your EBS volumes.**

```
Get-EC2Volume

```

- For API details, see
  [DescribeVolumes](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified EBS volume.**

```
Get-EC2Volume -VolumeId vol-12345678

```

**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2c
CreateTime       : 7/17/2015 4:35:19 PM
Encrypted        : False
Iops             : 90
KmsKeyId         :
Size             : 30
SnapshotId       : snap-12345678
State            : in-use
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : standard
```

**Example 2: This example describes your EBS volumes that have the status 'available'.**

```
Get-EC2Volume -Filter @{ Name="status"; Values="available" }

```

**Output:**

```
Attachments      : {}
AvailabilityZone : us-west-2c
CreateTime       : 12/21/2015 2:31:29 PM
Encrypted        : False
Iops             : 60
KmsKeyId         :
Size             : 20
SnapshotId       : snap-12345678
State            : available
Tags             : {}
VolumeId         : vol-12345678
VolumeType       : gp2
...
```

**Example 3: This example describes all your EBS volumes.**

```
Get-EC2Volume

```

- For API details, see
  [DescribeVolumes](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
