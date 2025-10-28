# How AMI store and restore works

To store and restore an AMI using S3, you use the following APIs:

- `CreateStoreImageTask` – Stores the AMI in an S3 bucket
- `DescribeStoreImageTasks` – Provides the progress of the AMI store
  task
- `CreateRestoreImageTask` – Restores the AMI from an S3 bucket

###### How the APIs work

- [CreateStoreImageTask](#CreateStoreImageTask "#CreateStoreImageTask")
- [DescribeStoreImageTasks](#DescribeStoreImageTasks "#DescribeStoreImageTasks")
- [CreateRestoreImageTask](#CreateRestoreImageTask "#CreateRestoreImageTask")
- [File paths](#file-paths-in-s3 "#file-paths-in-s3")

## CreateStoreImageTask

The `CreateStoreImageTask` API stores an AMI as a single object in an S3
bucket.

The API creates a task that reads all of the data from the AMI and its snapshots, and then
uses an [S3 multipart upload](../../../AmazonS3/latest/userguide/mpuoverview.md "../../../AmazonS3/latest/userguide/mpuoverview.md") to store the data in an S3 object. The API takes
all of the components of the AMI, including most of the non-Region-specific AMI
metadata, and all the EBS snapshots contained in the AMI, and packs them into a
single object in S3. The data is compressed as part of the upload process to reduce
the amount of space used in S3, so the object in S3 might be smaller than the sum of
the sizes of the snapshots in the AMI.

If there are AMI and snapshot tags visible to the account calling this API, they are
preserved.

The object in S3 has the same ID as the AMI, but with a `.bin` extension. The
following data is also stored as S3 metadata tags on the S3 object: AMI name, AMI
description, AMI registration date, AMI owner account, and a timestamp for the store
operation.

The time it takes to complete the task depends on the size of the AMI. It also depends on
how many other tasks are in progress because tasks are queued. You can track the
progress of the task by calling the `DescribeStoreImageTasks` API.

The sum of the sizes of all the AMIs in progress is limited to 1,200 GB of EBS snapshot
data per account. Further task creation will be rejected until the tasks in progress
are less than the limit. For example, if an AMI with 200 GB of snapshot data and
another AMI with 400 GB of snapshot data are currently being stored, another request
will be accepted, because the total in progress is 600 GB, which is less than the
limit. But if a single AMI with 1,200 GB of snapshot data is currently being stored,
further tasks are rejected until the task is completed.

## DescribeStoreImageTasks

The `DescribeStoreImageTasks` API describes the
progress of the AMI store tasks. You can describe tasks for specified AMIs. If you
don't specify AMIs, you get a paginated list of all of the store image tasks that
have been processed in the last 31 days.

For each AMI task, the response indicates if the task is `InProgress`,
`Completed`, or `Failed`. For tasks
`InProgress`, the response shows an estimated progress as a
percentage.

Tasks are listed in reverse chronological order.

Currently, only tasks from the previous month can be viewed.

## CreateRestoreImageTask

The `CreateRestoreImageTask` API starts a task that
restores an AMI from an S3 object that was previously created by using a
`CreateStoreImageTask` request.

The restore task can be performed in the same or a different Region in which the store task
was performed.

The S3 bucket from which the AMI object will be restored must be in the same
Region in which the restore task is requested. The AMI will be restored in this
Region.

The AMI is restored with its metadata, such as the name, description, and block device
mappings corresponding to the values of the stored AMI. The name must be unique for
AMIs in the Region for this account. If you do not provide a name, the new AMI gets
the same name as the original AMI. The AMI gets a new AMI ID that is generated at
the time of the restore process.

The time it takes to complete the AMI restoration task depends on the size of the AMI. It
also depends on how many other tasks are in progress because tasks are queued. You
can view the progress of the task by describing the AMI ([describe-images](../../../cli/latest/reference/ec2/describe-images.md "../../../cli/latest/reference/ec2/describe-images.md")) or
its EBS snapshots ([describe-snapshots](../../../cli/latest/reference/ec2/describe-snapshots.md "../../../cli/latest/reference/ec2/describe-snapshots.md")). If the task fails, the AMI and snapshots are moved
to a failed state.

The sum of the sizes of all of the AMIs in progress is limited to 600 GB (based on the size
after restoration) of EBS snapshot data per account. Further task creation will be
rejected until the tasks in progress are less than the limit.

## File paths

You can use file paths when storing and restoring AMIs, in the following way:

- When storing an AMI in S3, the file path can be added to the bucket name. Internally, the
  system separates the path from the bucket name, and then adds the path to the
  object key that is generated to store the AMI. The full object path is shown in
  the response from the API call.
- When restoring the AMI, because an object key parameter is available, the path can be added
  to the beginning of the object key value.

###### Example: Bucket name with appended file path

When you store the AMI, specify the file path after the bucket name.

```
`amzn-s3-demo-bucket/path1/path2`
```

The following is the resulting object key.

```
`path1/path2/ami-0abcdef1234567890`.bin
```

When you restore the AMI, you specify both the bucket name and the object
key. For examples, see [Create a store image task](work-with-ami-store-restore.md#create-store-image-task "work-with-ami-store-restore.md#create-store-image-task").
