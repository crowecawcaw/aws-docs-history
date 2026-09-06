

# Use `CreateSnapshot` with a CLI
<a name="example_ec2_CreateSnapshot_section"></a>

The following code examples show how to use `CreateSnapshot`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Working with block storage encryption, snapshots, and volume initialization](example_ec2_GettingStarted_022_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To create a snapshot**  
This example command creates a snapshot of the volume with a volume ID of `vol-1234567890abcdef0` and a short description to identify the snapshot.  
Command:  

```
aws ec2 create-snapshot --volume-id {{vol-1234567890abcdef0}} --description {{"This is my root volume snapshot"}}
```
Output:  

```
{
    "Description": "This is my root volume snapshot",
    "Tags": [],
    "Encrypted": false,
    "VolumeId": "vol-1234567890abcdef0",
    "State": "pending",
    "VolumeSize": 8,
    "StartTime": "2018-02-28T21:06:01.000Z",
    "Progress": "",
    "OwnerId": "012345678910",
    "SnapshotId": "snap-066877671789bd71b"
}
```
**To create a snapshot with tags**  
This example command creates a snapshot and applies two tags: purpose=prod and costcenter=123.  
Command:  

```
aws ec2 create-snapshot --volume-id {{vol-1234567890abcdef0}} --description '{{Prod backup}}' --tag-specifications '{{ResourceType=snapshot,Tags=[{Key=purpose,Value=prod},{Key=costcenter,Value=123}]}}'
```
Output:  

```
{
    "Description": "Prod backup",
    "Tags": [
        {
            "Value": "prod",
            "Key": "purpose"
        },
        {
            "Value": "123",
            "Key": "costcenter"
        }
     ],
     "Encrypted": false,
     "VolumeId": "vol-1234567890abcdef0",
     "State": "pending",
     "VolumeSize": 8,
     "StartTime": "2018-02-28T21:06:06.000Z",
     "Progress": "",
     "OwnerId": "012345678910",
     "SnapshotId": "snap-09ed24a70bc19bbe4"
 }
```
+  For API details, see [CreateSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshot.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates a snapshot of the specified volume.**  

```
New-EC2Snapshot -VolumeId vol-12345678 -Description "This is a test"
```
**Output:**  

```
DataEncryptionKeyId :
Description         : This is a test
Encrypted           : False
KmsKeyId            :
OwnerAlias          :
OwnerId             : 123456789012
Progress            :
SnapshotId          : snap-12345678
StartTime           : 12/22/2015 1:28:42 AM
State               : pending
StateMessage        :
Tags                : {}
VolumeId            : vol-12345678
VolumeSize          : 20
```
+  For API details, see [CreateSnapshot](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates a snapshot of the specified volume.**  

```
New-EC2Snapshot -VolumeId vol-12345678 -Description "This is a test"
```
**Output:**  

```
DataEncryptionKeyId :
Description         : This is a test
Encrypted           : False
KmsKeyId            :
OwnerAlias          :
OwnerId             : 123456789012
Progress            :
SnapshotId          : snap-12345678
StartTime           : 12/22/2015 1:28:42 AM
State               : pending
StateMessage        :
Tags                : {}
VolumeId            : vol-12345678
VolumeSize          : 20
```
+  For API details, see [CreateSnapshot](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.