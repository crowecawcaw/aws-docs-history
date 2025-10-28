# Use `DescribeSnapshots` with an AWS SDK or CLI

The following code examples show how to use `DescribeSnapshots`.

CLI

**AWS CLI**

**Example 1: To describe a snapshot**

The following `describe-snapshots` example describes the specified snapshot.

```
`aws ec2 describe-snapshots \
 --snapshot-ids `snap-1234567890abcdef0``

```

Output:

```
{
    "Snapshots": [
        {
            "Description": "This is my snapshot",
            "Encrypted": false,
            "VolumeId": "vol-049df61146c4d7901",
            "State": "completed",
            "VolumeSize": 8,
            "StartTime": "2019-02-28T21:28:32.000Z",
            "Progress": "100%",
            "OwnerId": "012345678910",
            "SnapshotId": "snap-01234567890abcdef",
            "Tags": [
                {
                    "Key": "Stack",
                    "Value": "test"
                }
            ]
        }
    ]
}
```

For more information, see [Amazon EBS snapshots](../../../AWSEC2/latest/UserGuide/EBSSnapshots.md "../../../AWSEC2/latest/UserGuide/EBSSnapshots.md") in the _Amazon EC2 User Guide_.

**Example 2: To describe snapshots based on filters**

The following `describe-snapshots` example uses filters to scope the results to snapshots owned by your AWS account that are in the `pending` state. The example uses the `--query` parameter to display only the snapshot IDs and the time the snapshot was started.

```
`aws ec2 describe-snapshots \
 --owner-ids `self` \
 --filters `Name=status,Values=pending` \
 --query `"Snapshots[*].{ID:SnapshotId,Time:StartTime}"``

```

Output:

```
[
    {
        "ID": "snap-1234567890abcdef0",
        "Time": "2019-08-04T12:48:18.000Z"
    },
    {
        "ID": "snap-066877671789bd71b",
        "Time": "2019-08-04T02:45:16.000Z
    },
    ...
]
```

The following `describe-snapshots` example uses filters to scope the results to snapshots created from the specified volume. The example uses the `--query` parameter to display only the snapshot IDs.

```
`aws ec2 describe-snapshots \
 --filters `Name=volume-id,Values=049df61146c4d7901` \
 --query `"Snapshots[*].[SnapshotId]"` \
 --output `text``

```

Output:

```
snap-1234567890abcdef0
snap-08637175a712c3fb9
...
```

For additional examples using filters, see [Listing and filtering your resources](../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI "../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI") in the _Amazon EC2 User Guide_.

**Example 3: To describe snapshots based on tags**

The following `describe-snapshots` example uses tag filters to scope the results to snapshots that have the tag `Stack=Prod`.

```
`aws ec2 describe-snapshots \
 --filters `Name=tag:Stack,Values=prod``

```

For an example of the output for `describe-snapshots`, see Example 1.

For additional examples using tag filters, see [Working with tags](../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI "../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI") in the _Amazon EC2 User Guide_.

**Example 4: To describe snapshots based on age**

The following `describe-snapshots` example uses JMESPath expressions to describe all snapshots created by your AWS account before the specified date. It displays only the snapshot IDs.

```
`aws ec2 describe-snapshots \
 --owner-ids `012345678910` \
 --query `"Snapshots[?(StartTime<='2020-03-31')].[SnapshotId]"``

```

For additional examples using filters, see [Listing and filtering your resources](../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI "../../../AWSEC2/latest/UserGuide/Using_Filtering.md#Filtering_Resources_CLI") in the _Amazon EC2 User Guide_.

**Example 5: To view only archived snapshots**

The following `describe-snapshots` example lists only snapshots that are stored in the archive tier.

```
`aws ec2 describe-snapshots \
 --filters `"Name=storage-tier,Values=archive"``

```

Output:

```
{
    "Snapshots": [
        {
            "Description": "Snap A",
            "Encrypted": false,
            "VolumeId": "vol-01234567890aaaaaa",
            "State": "completed",
            "VolumeSize": 8,
            "StartTime": "2021-09-07T21:00:00.000Z",
            "Progress": "100%",
            "OwnerId": "123456789012",
            "SnapshotId": "snap-01234567890aaaaaa",
            "StorageTier": "archive",
            "Tags": []
        },
    ]
}
```

For more information, see [View archived snapshots](../../../AWSEC2/latest/UserGuide/working-with-snapshot-archiving.md#view-archived-snapshot "../../../AWSEC2/latest/UserGuide/working-with-snapshot-archiving.md#view-archived-snapshot") in the _Amazon Elastic Compute Cloud User Guide_.

- For API details, see
  [DescribeSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshots.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshots.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified snapshot.**

```
Get-EC2Snapshot -SnapshotId snap-12345678

```

**Output:**

```
DataEncryptionKeyId :
Description         : Created by CreateImage(i-1a2b3c4d) for ami-12345678 from vol-12345678
Encrypted           : False
KmsKeyId            :
OwnerAlias          :
OwnerId             : 123456789012
Progress            : 100%
SnapshotId          : snap-12345678
StartTime           : 10/23/2014 6:01:28 AM
State               : completed
StateMessage        :
Tags                : {}
VolumeId            : vol-12345678
VolumeSize          : 8
```

**Example 2: This example describes the snapshots that have a 'Name' tag.**

```
Get-EC2Snapshot | ? { $_.Tags.Count -gt 0 -and $_.Tags.Key -eq "Name" }

```

**Example 3: This example describes the snapshots that have a 'Name' tag with the value 'TestValue'.**

```
Get-EC2Snapshot | ? { $_.Tags.Count -gt 0 -and $_.Tags.Key -eq "Name" -and $_.Tags.Value -eq "TestValue" }

```

**Example 4: This example describes all your snapshots.**

```
Get-EC2Snapshot -Owner self

```

- For API details, see
  [DescribeSnapshots](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified snapshot.**

```
Get-EC2Snapshot -SnapshotId snap-12345678

```

**Output:**

```
DataEncryptionKeyId :
Description         : Created by CreateImage(i-1a2b3c4d) for ami-12345678 from vol-12345678
Encrypted           : False
KmsKeyId            :
OwnerAlias          :
OwnerId             : 123456789012
Progress            : 100%
SnapshotId          : snap-12345678
StartTime           : 10/23/2014 6:01:28 AM
State               : completed
StateMessage        :
Tags                : {}
VolumeId            : vol-12345678
VolumeSize          : 8
```

**Example 2: This example describes the snapshots that have a 'Name' tag.**

```
Get-EC2Snapshot | ? { $_.Tags.Count -gt 0 -and $_.Tags.Key -eq "Name" }

```

**Example 3: This example describes the snapshots that have a 'Name' tag with the value 'TestValue'.**

```
Get-EC2Snapshot | ? { $_.Tags.Count -gt 0 -and $_.Tags.Key -eq "Name" -and $_.Tags.Value -eq "TestValue" }

```

**Example 4: This example describes all your snapshots.**

```
Get-EC2Snapshot -Owner self

```

- For API details, see
  [DescribeSnapshots](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ebs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ebs#code-examples").

Shows the state of a snapshot.

```
async fn show_state(client: &Client, id: &str) -> Result<(), Error> {
    let resp = client
        .describe_snapshots()
        .filters(Filter::builder().name("snapshot-id").values(id).build())
        .send()
        .await?;

    println!(
        "State: {}",
        resp.snapshots().first().unwrap().state().unwrap().as_ref()
    );

    Ok(())
}


```

```
async fn show_snapshots(client: &Client) -> Result<(), Error> {
    // "self" represents your account ID.
    // You can list the snapshots for any account by replacing
    // "self" with that account ID.
    let resp = client.describe_snapshots().owner_ids("self").send().await?;
    let snapshots = resp.snapshots();
    let length = snapshots.len();

    for snapshot in snapshots {
        println!(
            "ID:          {}",
            snapshot.snapshot_id().unwrap_or_default()
        );
        println!(
            "Description: {}",
            snapshot.description().unwrap_or_default()
        );
        println!("State:       {}", snapshot.state().unwrap().as_ref());
        println!();
    }

    println!();
    println!("Found {} snapshot(s)", length);
    println!();

    Ok(())
}


```

- For API details, see
  [DescribeSnapshots](https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_snapshots "https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_snapshots")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
