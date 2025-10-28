Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Importing a virtual machine image to a Snowball Edge device

You can use the AWS CLI and the VM Import/Export service to import a virtual machine (VM) image to the
Snowball Edge device as an Amazon Machine Image (AMI). After importing a VM image, register the image as an AMI
and launch it as an Amazon EC2-compatible instance.

You can add AMIs from Amazon EC2 to the device when creating a job to order a Snowball Edge device. Use this procedure after you have received the Snowball Edge device. For more information, see [Choosing your compute and storage
options](create-job-common.md#compute-storage "create-job-common.md#compute-storage").

You can also use AWS OpsHub to upload the VM image file. For more information, see [Importing an image into your device as an Amazon EC2-compatible AMI](manage-ec2.md#ec2-ami-import "manage-ec2.md#ec2-ami-import") in this guide.

###### Topics

- [Step 1: Prepare the VM image and upload it to the Snowball Edge device](#prepare-image-cli "#prepare-image-cli")
- [Step 2: Set up required permissions on the Snowball Edge](#setup-permission-cli "#setup-permission-cli")
- [Step 3: Import the VM image as a snapshot on the Snowball Edge](#import-snapshot-cli "#import-snapshot-cli")
- [Step 4: Register the snapshot as an AMI on the Snowball Edge](#register-snapshot-cli "#register-snapshot-cli")
- [Step 5: Launch an instance from the AMI on the Snowball Edge](#launch-ami-cli "#launch-ami-cli")
- [Additional AMI actions for a Snowball Edge](#additional-ami-actions "#additional-ami-actions")

## Step 1: Prepare the VM image and upload it to the Snowball Edge device

Prepare the VM image by exporting a VM image from an Amazon EC2 AMI or instance in the AWS Cloud using VM Import/Export or by generating the
VM image locally using your choice of virtualization platform.

To export an Amazon EC2 instance as a VM image using VM Import/Export, see [Exporting an instance as a VM using VM Import/Export](../../../vm-import/latest/userguide/vmexport.md "../../../vm-import/latest/userguide/vmexport.md") in the VM Import/Export User Guide. To export an Amazon EC2 AMI as a VM image using VM Import/Export, see [Exporting a VM
directly from an Amazon Machine Image (AMI)](../../../vm-import/latest/userguide/vmexport_image.md "../../../vm-import/latest/userguide/vmexport_image.md") in the VM Import/Export User Guide.

If generating a VM image from your local environment, ensure the image is configured for use as an AMI on the Snowball Edge device. You may need to configure the following items, depending on your environment.

- Configure and update the operating system.
- Set a hostname.
- Ensure network time protocol (NTP) is configured.
- Include SSH public keys, if necessary. Make local copies of the key pairs. For more information, see [Using SSH to Connect to Your Compute Instances on a Snowball Edge](ssh-ec2-edge.md "ssh-ec2-edge.md").
- Install and configure any software you will use on the Snowball Edge device.

###### Note

Be aware of the following limitations when preparing a disk snapshot for a Snowball Edge device.

- Snowball Edge currently only support importing snapshots that are in
  the RAW image format.
- Snowball Edge currently only support importing snapshots with sizes
  from 1 GB to 1 TB.

### Uploading a VM image to an Amazon S3 bucket on the Snowball Edge device

After preparing a VM image, upload it to an S3 bucket on the Snowball Edge device or cluster. You can use the S3 adapter or Amazon S3 compatible storage on Snowball Edge to upload the snapshot.

###### To upload the virtual machine image using the S3 adapter

- Use the `cp` command to copy the VM image file to a bucket on the device.

```

aws s3 cp `image-path` s3://`S3-bucket-name` --endpoint http://`S3-object-API-endpoint:443` --profile `profile-name`
```

For more information, see [Supported AWS CLI commands](using-adapter-cli.md "using-adapter-cli.md") in this guide.

###### To upload the VM image using Amazon S3 compatible storage on Snowball Edge

- Use the `put-object` command to copy the snapshot file to a bucket on the device.

```

aws s3api put-object --bucket `bucket-name` --key `path-to-snapshot-file` --body `snapshot-file` --endpoint-url `s3api-endpoint-ip` --profile `your-profile`

```

For more information, see [Working with S3 objects on a Snowball Edge device](objects-s3-snow.md "objects-s3-snow.md").

## Step 2: Set up required permissions on the Snowball Edge

For the import to be successful, you must set up permissions for VM Import/Export on the Snowball Edge device, Amazon EC2,
and the user.

###### Note

The service roles and policies that provide these permissions are located on the Snowball Edge device.

### Permissions required for VM Import/Export on a Snowball Edge

Before you can start the import process, you must create an IAM role with a
trust policy that allows VM Import/Export on the Snowball Edge device to assume the role. Additional
permissions are given to the role to allow VM Import/Export on the device to access the image stored in
the S3 bucket on the device.

**Create a trust policy json file**

Following is an example trust policy required to be attached to the role so
that VM Import/Export can access the snapshot that needs to be imported from the S3
bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "Service":"vmie.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

**Create a role with the trust policy json
file**

The role name can be vmimport. You can change it by using the --role-name option
in the command:

```
aws iam create-role --role-name `role-name` --assume-role-policy-document file:///`trust-policy-json-path` --endpoint http://`snowball-ip`:6078 --region snow  --profile `profile-name`
```

The following is an example output from the `create-role` command.

```
{
   "Role":{
      "AssumeRolePolicyDocument":{
         "Version": "2012-10-17",
         "Statement":[
            {
               "Action":"sts:AssumeRole",
               "Effect":"Allow",
               "Principal":{
                  "Service":"vmie.amazonaws.com"
               }
            }
         ]
      },
      "MaxSessionDuration":3600,
      "RoleId":"AROACEMGEZDGNBVGY3TQOJQGEZAAAABQBB6NSGNAAAABPSVLTREPY3FPAFOLKJ3",
      "CreateDate":"2022-04-19T22:17:19.823Z",
      "RoleName":"vmimport",
      "Path":"/",
      "Arn":"arn:aws:iam::123456789012:role/vmimport"
   }
}
```

**Create a policy for the role**

The following example policy has the minimum required permissions to access Amazon S3.
Change the Amazon S3 bucket name to the one which has your images. For a standalone Snowball Edge device, change `snow-id` to your job ID. For a cluster of devices, change `snow-id` to the cluster ID. You also can
use prefixes to further narrow down the location where VM Import/Export can import snapshots from.
Create a policy json file like this.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket"
 ],
 "Resource":[
 "arn:aws:s3:::`import-snapshot-bucket-name`",
 "arn:aws:s3:::`import-snapshot-bucket-name`/*"
 ]
 }
 ]
}`

```

**Create a policy with the policy file:**

```
aws iam create-policy --policy-name `policy-name` --policy-document file:///`policy-json-file-path` --endpoint http://`snowball-ip`:6078 --region snow --profile `profile-name`
```

The following is an output example from the create-policy command.

```
{
   "Policy":{
      "PolicyName":"vmimport-resource-policy",
      "PolicyId":"ANPACEMGEZDGNBVGY3TQOJQGEZAAAABOOEE3IIHAAAABWZJPI2VW4UUTFEDBC2R",
      "Arn":"arn:aws:iam::123456789012:policy/vmimport-resource-policy",
      "Path":"/",
      "DefaultVersionId":"v1",
      "AttachmentCount":0,
      "IsAttachable":true,
      "CreateDate":"2020-07-25T23:27:35.690000+00:00",
      "UpdateDate":"2020-07-25T23:27:35.690000+00:00"
   }
}
```

\***\*Attach the policy to the
role\*\***

Attach a policy to the preceding role and grant permissions to access the required
resources. This allows the local VM Import/Export service to download the snapshot from Amazon S3 on
the device.

```
aws iam attach-role-policy --role-name `role-name` --policy-arn arn:aws:iam::123456789012:policy/`policy-name` --endpoint http://`snowball-ip`:6078 --region snow --profile `profile-name`
```

### Permissions required by the caller on a Snowball Edge

In addition to the role for the Snowball Edge VM Import/Export to assume, you also
must ensure that the user has the permissions that allow them to pass the role to
VMIE. If you use the default root user to perform the import, the root user already
has all the permissions required, so you can skip this step, and go to step 3.

Attach the following two IAM permissions to the user that is doing the
import.

- `pass-role`
- `get-role`

**Create a policy for the role**

The following is an example policy that allows a user to perform the
`get-role` and `pass-role` actions for the IAM role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action": "iam:GetRole",
 "Resource":"*"
 },
 {
 "Sid": "iamPassRole",
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": "arn:aws:iam::*:role/snowball*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": "importexport.amazonaws.com"
 }
 }
 }
 ]
}`

```

\***\*Create a policy with the policy
file:\*\***

```
aws iam create-policy --policy-name `policy-name` --policy-document file:///`policy-json-file-path` --endpoint http://`snowball-ip`:6078 --region snow --profile `profile-name`
```

The following is an output example from the create-policy command.

```
{
   "Policy":{
      "PolicyName":"caller-policy",
      "PolicyId":"ANPACEMGEZDGNBVGY3TQOJQGEZAAAABOOOTUOE3AAAAAAPPBEUM7Q7ARPUE53C6R",
      "Arn":"arn:aws:iam::123456789012:policy/caller-policy",
      "Path":"/",
      "DefaultVersionId":"v1",
      "AttachmentCount":0,
      "IsAttachable":true,
      "CreateDate":"2020-07-30T00:58:25.309000+00:00",
      "UpdateDate":"2020-07-30T00:58:25.309000+00:00"
   }
}
```

After the policy has been generated, attach the policy to the IAM users that will
call the Amazon EC2 API or CLI operation to import the snapshot.

```
aws iam attach-user-policy --user-name `your-user-name` --policy-arn arn:aws:iam::123456789012:policy/`policy-name` --endpoint http://`snowball-ip`:6078 --region snow --profile `profile-name`
```

### Permissions Required to call Amazon EC2 APIs on a Snowball Edge

To import a snapshot, the IAM user must have the
`ec2:ImportSnapshot` permissions. If restricting access to the user
is not required, you can use the `ec2:*` permissions to grant full Amazon EC2
access. The following are the permissions that can be granted or restricted for
Amazon EC2 on your device. Create a policy file with the content shown:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "ec2:ImportSnapshot",
 "ec2:DescribeImportSnapshotTasks",
 "ec2:CancelImportTask",
 "ec2:DescribeSnapshots",
 "ec2:DeleteSnapshot",
 "ec2:RegisterImage",
 "ec2:DescribeImages",
 "ec2:DeregisterImage"
 ],
 "Resource":"*"
 }
 ]
}`

```

**Create a policy with the policy file:**

```
aws iam create-policy --policy-name `policy-name` --policy-document file:///`policy-json-file-path` --endpoint http://`snowball-ip`:6078 --region snow --profile `profile-name`
```

The following is an output example from the create-policy command.

```
{
    "Policy":
        {
            "PolicyName": "ec2-import.json",
            "PolicyId": "ANPACEMGEZDGNBVGY3TQOJQGEZAAAABQBGPDQC5AAAAATYN62UNBFYTF5WVCSCZS",
            "Arn": "arn:aws:iam::123456789012:policy/ec2-import.json",
            "Path": "/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 0,
            "IsAttachable": true,
            "CreateDate": "2022-04-21T16:25:53.504000+00:00",
            "UpdateDate": "2022-04-21T16:25:53.504000+00:00"
        }
}
```

After the policy has been generated, attach the policy to the IAM users that
will call the Amazon EC2 API or CLI operation to import the snapshot.

```
aws iam attach-user-policy --user-name `your-user-name` --policy-arn arn:aws:iam::123456789012:policy/`policy-name` --endpoint http://`snowball-ip`:6078 --region snow --profile `profile-name`
```

## Step 3: Import the VM image as a snapshot on the Snowball Edge

The next step is to import the VM image as a snapshot on the device. The value
of the `S3Bucket` parameter is the name of the bucket which contains the VM image. The value of the `S3Key` parameter is the path to the VM image file
in this bucket.

```
aws ec2 import-snapshot --disk-container "Format=RAW,UserBucket={S3Bucket=`bucket-name`,S3Key=`image-file`}" --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

For more information, see [import-snapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-snapshot.html") in the AWS CLI Command Reference.

This command doesn't support the following switches.

- [--client-data `value`]
- [--client-token `value`]
- [--dry-run]
- [--no-dry-run]
- [--encrypted]
- [--no-encrypted]
- [--kms-key-id `value`]
- [--tag-specifications `value`]

###### Example output of `import-snapshot` command

```
{
   "ImportTaskId":"s.import-snap-1234567890abc",
   "SnapshotTaskDetail":{
      "DiskImageSize":2.0,
      "Encrypted":false,
      "Format":"RAW",
      "Progress":"3",
      "Status":"active",
      "StatusMessage":"pending",
      "UserBucket":{
         "S3Bucket":"bucket",
         "S3Key":"vmimport/image01"
      }
   }
}
```

###### Note

Snowball Edge currently only allow one active import job to run at a
time, per device. To start a new import task, either wait for the current task
to finish, or choose another available node in a cluster. You can also choose to
cancel the current import if you want. To prevent delays, don't reboot the
Snowball Edge device while the import is in progress. If you reboot the
device, the import will fail, and progress will be deleted when the device
becomes accessible. To check the status of your snapshot import task status, use
the following command:

```
aws ec2 describe-import-snapshot-tasks --import-task-ids `id` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

## Step 4: Register the snapshot as an AMI on the Snowball Edge

When the snapshot import to the device is successful, you can register it using
the `register-image` command.

###### Note

You can only register an AMI when all of its snapshots are available.

For more information, see [register-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html") in the AWS CLI Command Reference.

###### Example of the `register-image` command

```
aws ec2 register-image \
--name `ami-01` \
--description `my-ami-01` \
--block-device-mappings "[{\"DeviceName\": \"/dev/sda1\",\"Ebs\":{\"Encrypted\":false,\"DeleteOnTermination\":true,\"SnapshotId\":\"`snapshot-id`\",\"VolumeSize\":30}}]" \
--root-device-name /dev/sda1 \
--endpoint http://`snowball-ip`:8008 \
--region snow \
--profile `profile-name`

```

Following is an example of block device mapping JSON. For more information, see the
[block-device-mapping parameter of register-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html") in the AWS CLI Command Reference.

```
[
    {
        "DeviceName": "/dev/sda",
        "Ebs":
            {
                "Encrypted": false,
                "DeleteOnTermination": true,
                "SnapshotId": "`snapshot-id`",
                "VolumeSize": 30
            }
    }
]
```

###### Example of the `register-image` command

```
{
    "ImageId": "s.ami-8de47d2e397937318"
 }
```

## Step 5: Launch an instance from the AMI on the Snowball Edge

To launch an instance, see [run-instances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html") in the AWS CLI Command Reference.

The value of the `image-id` parameter is the value of the `ImageId` name as the output of the `register-image` command.

```
aws ec2 run-instances --image-id `image-id` --instance-type `instance-type` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

```
{
   "Instances":[
      {
         "SourceDestCheck":false,
         "CpuOptions":{
            "CoreCount":1,
            "ThreadsPerCore":2
         },
         "InstanceId":"s.i-12345a73123456d1",
         "EnaSupport":false,
         "ImageId":"s.ami-1234567890abcdefg",
         "State":{
            "Code":0,
            "Name":"pending"
         },
         "EbsOptimized":false,
         "SecurityGroups":[
            {
               "GroupName":"default",
               "GroupId":"s.sg-1234567890abc"
            }
         ],
         "RootDeviceName":"/dev/sda1",
         "AmiLaunchIndex":0,
         "InstanceType":"sbe-c.large"
      }
   ],
   "ReservationId":"s.r-1234567890abc"
}
```

###### Note

You can also use AWS OpsHub to launch the instance. For more information, see [Launching an Amazon EC2-compatible instance](manage-ec2.md#launch-instance "manage-ec2.md#launch-instance") in this guide.

## Additional AMI actions for a Snowball Edge

You can use additional AWS CLI commands to monitor snapshot import status, get details on snapshots that have been imported, canceling importing a snapshot, and deleting or deregistering snapshots after they have been imported.

### Monitoring snapshot import status on a Snowball Edge

To see the current state of the import progress, you can run the Amazon EC2
`describe-import-snapshot-tasks` command. This command supports
pagination and filtering on the `task-state`.

###### Example of the `describe-import-snapshot-tasks` command

```
aws ec2 describe-import-snapshot-tasks --import-task-ids `id` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

###### Example of `describe-import-snapshot-tasks` command output

```
{
        "ImportSnapshotTasks": [
            {
                "ImportTaskId": "s.import-snap-8f6bfd7fc9ead9aca",
                "SnapshotTaskDetail": {
                    "Description": "Created by AWS-Snowball-VMImport service for s.import-snap-8f6bfd7fc9ead9aca",
                    "DiskImageSize": 8.0,
                    "Encrypted": false,
                    "Format": "RAW",
                    "Progress": "3",
                    "SnapshotId": "s.snap-848a22d7518ad442b",
                    "Status": "active",
                    "StatusMessage": "pending",
                    "UserBucket": {
                        "S3Bucket": "bucket1",
                        "S3Key": "image1"
                    }
                }
            }
        ]
 }
```

###### Note

This command only shows output for tasks that have successfully completed or been marked as
deleted within the last 7 days. Filtering only supports
`Name=task-state`, `Values=active | deleting | deleted |
 completed`

This command doesn't support the following parameters.

- [--dry-run]
- [--no-dry-run]

### Canceling an import task on a Snowball Edge

To cancel an import task, run the `cancel-import-task` command.

###### Example of the `cancel-import-task` command

```
aws ec2 cancel-import-task --import-task-id `import-task-id` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

###### Example of `cancel-import-task` command output

```
{
        "ImportTaskId": "s.import-snap-8234ef2a01cc3b0c6",
        "PreviousState": "active",
        "State": "deleting"
}
```

###### Note

Only tasks that are not in a completed state can be canceled.

This command doesn't support the following parameters.

- [--dry-run]
- [--no-dry-run]

### Describing snapshots on a Snowball Edge

After a snapshot is imported, you can use this command to describe it. To filter
the snapshots, you can pass in `snapshot-ids` with the snapshot ID from
the previous import task response. This command supports pagination and filter on
`volume-id`, `status`, and `start-time`.

###### Example of `describe-snapshots` command

```
aws ec2 describe-snapshots --snapshot-ids `snapshot-id` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

###### Example of `describe-snapshots` command output

```
{
    "Snapshots": [
        {
            "Description": "Created by AWS-Snowball-VMImport service for s.import-snap-8f6bfd7fc9ead9aca",
            "Encrypted": false,
            "OwnerId": "123456789012",
            "SnapshotId": "s.snap-848a22d7518ad442b",
            "StartTime": "2020-07-30T04:31:05.032000+00:00",
            "State": "completed",
            "VolumeSize": 8
        }
    ]
 }
```

This command doesn't support the following parameters.

- [--restorable-by-user-ids `value`]
- [--dry-run]
- [--no-dry-run]

### Deleting a snapshot from a Snowball Edge device

To remove snapshots that you own and you no longer need, you can use the
`delete-snapshot` command.

###### Example of the `delete-snapshot` command

```
aws ec2 delete-snapshot --snapshot-id `snapshot-id` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

###### Note

Snowball Edge does not support deleting snapshots that are in a **PENDING**
state or if it is designated as a root device for an AMI.

This command doesn't support the following parameters.

- [--dry-run]
- [--no-dry-run]

### Deregistering an AMI on a Snowball Edge

To deregister AMIs that you no longer need, you can run the
`deregister-image` command. Deregistering an AMI that is in the
**Pending** state is not currently supported.

###### Example of the `deregister-image` command

```
aws ec2 deregister-image --image-id `image-id` --endpoint http://`snowball-ip`:8008 --region snow --profile `profile-name`
```

This command doesn't support the following parameters.

- [--dry-run]
- [--no-dry-run]
