# Seeding a new cluster with an externally created snapshot

When you create a new MemoryDB cluster, you can seed it with data from a Valkey or Redis OSS .rdb snapshot file.

To seed a new MemoryDB cluster from a MemoryDB snapshot or ElastiCache (Redis OSS) snapshot,
see [Restoring from a snapshot](snapshots-restoring.md "snapshots-restoring.md").

When you use a .rdb file to seed a new MemoryDB cluster, you can do the
following:

- Specify a number of shards in the new
  cluster. This number can be different from the number of shards in the cluster
  that was used to create the snapshot file.
- Specify a different node type for the new cluster—larger or smaller than
  that used in the cluster that made the snapshot. If you scale to a smaller node
  type, be sure that the new node type has sufficient memory for your data and engine overhead.

###### Important

- You must ensure that your snapshot data doesn't exceed the resources
  of the node.

If the snapshot is too large, the resulting cluster has a status of
`restore-failed`. If this happens, you must delete the
cluster and start over.

For a complete listing of node types and specifications,
see [MemoryDB node-type specific parameters](parametergroups.md#parametergroups.redis.nodespecific "parametergroups.md#parametergroups.redis.nodespecific").

- You can encrypt a .rdb file with Amazon S3 server-side encryption (SSE-S3) only. For more information, see
  [Protecting data using server-side encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md").

## Step 1: Create a snapshot on an external cluster

###### To create the snapshot to seed your MemoryDB cluster

1. Connect to your existing Valkey or Redis OSS instance.
2. Run either the `BGSAVE` or `SAVE` operation to create a snapshot.
   Note where your .rdb file is located.

`BGSAVE` is asynchronous and does not block other clients while processing.
For more information, see [BGSAVE](http://valkey.io/commands/bgsave "http://valkey.io/commands/bgsave").

`SAVE` is synchronous and blocks other processes until finished.
For more information, see [SAVE](http://valkey.io/commands/save "http://valkey.io/commands/save").

For additional information on creating a snapshot, see [persistence](http://valkey.io/topics/persistence "http://valkey.io/topics/persistence").

## Step 2: Create an Amazon S3 bucket and folder

When you have created the snapshot file, you need to upload it to a folder within an
Amazon S3 bucket. To do that, you must first have an Amazon S3 bucket and folder within that
bucket. If you already have an Amazon S3 bucket and folder with the appropriate
permissions, you can skip to [Step 3: Upload your snapshot to Amazon S3](#snapshots-seeding-upload "#snapshots-seeding-upload").

###### To create an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Follow the instructions for creating an Amazon S3 bucket in [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the
   _Amazon Simple Storage Service User Guide_.

The name of your Amazon S3 bucket must be DNS-compliant. Otherwise, MemoryDB can't
access your backup file. The rules for DNS compliance are:

    * Names must be at least 3 and no more than 63 characters long.
    * Names must be a series of one or more labels separated by a period (.) where each label:




    	+ Starts with a lowercase letter or a number.
    	+ Ends with a lowercase letter or a number.
    	+ Contains only lowercase letters, numbers, and dashes.
    * Names can't be formatted as an IP address (for example, 192.0.2.0).

We strongly recommend that you create your Amazon S3 bucket in the same AWS Region
as your new MemoryDB cluster. This approach makes sure that the
highest data transfer speed when MemoryDB reads your .rdb file from
Amazon S3.

###### Note

To keep your data as secure as possible, make the permissions on your
Amazon S3 bucket as restrictive as you can. At the same time, the permissions still need to allow
the bucket and its contents to be used to seed your new MemoryDB
cluster.

###### To add a folder to an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the name of the bucket to upload your .rdb file to.
3. Choose **Create folder**.
4. Enter a name for your new folder.
5. Choose **Save**.

Make note of both the bucket name and the folder name.

## Step 3: Upload your snapshot to Amazon S3

Now, upload the .rdb file that you created in [Step 1: Create a snapshot on an external cluster](#snapshots-seeding-create-snapshot "#snapshots-seeding-create-snapshot"). You upload it to the Amazon S3
bucket and folder that you created in [Step 2: Create an Amazon S3 bucket and folder](#snapshots-seeding-create-s3-bucket "#snapshots-seeding-create-s3-bucket"). For more information
on this task, see [Uploading objects](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md"). Between steps 2 and 3, choose the name of the folder you created
.

###### To upload your .rdb file to an Amazon S3 folder

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the name of the Amazon S3 bucket you created in Step 2.
3. Choose the name of the folder you created in Step 2.
4. Choose **Upload**.
5. Choose **Add files**.
6. Browse to find the file or files you want to upload, then choose the file
   or files. To choose multiple files, hold down the Ctrl key while choosing
   each file name.
7. Choose **Open**.
8. Confirm the correct file or files are listed in the
   **Upload** page, and then choose
   **Upload**.

Note the path to your .rdb file. For example, if your bucket name is
`amzn-s3-demo-bucket` and the path is `myFolder/redis.rdb`, enter
`amzn-s3-demo-bucket/myFolder/redis.rdb`. You need this path to seed the new
cluster with the data in this snapshot.

For additional information, see [Bucket naming rules](../../../AmazonS3/latest/userguide/bucketnamingrules.md "../../../AmazonS3/latest/userguide/bucketnamingrules.md")
in the _Amazon Simple Storage Service User Guide_.

## Step 4: Grant MemoryDB read access to the .rdb file

AWS Regions introduced before March 20, 2019, are enabled by default. You can
begin working in these AWS Regions immediately. Regions introduced after March 20,
2019 are disabled by default. You must enable, or opt in, to these Regions before you can use them, as described
in [Managing AWS
regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md").

### Grant MemoryDB read access to the .rdb file

###### To grant MemoryDB read access to the snapshot file

1.  Sign in to the AWS Management Console and open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  Choose the name of the S3 bucket that contains your .rdb file.
3.  Choose the name of the folder that contains your .rdb file.
4.  Choose the name of your .rdb snapshot file. The name of the selected file
    appears above the tabs at the top of the page.
5.  Choose the **Permissions** tab.
6.  Under **Permissions**, choose **Bucket
    policy** and then choose **Edit**.
7.  Update the policy to grant MemoryDB required permissions to perform
    operations:

        * Add `[ "Service" : "`region-full-name`.memorydb-snapshot.amazonaws.com" ]` to `Principal`.
        * Add the following permissions required for exporting a snapshot to the Amazon S3 bucket:




        	+ `"s3:GetObject"`
        	+ `"s3:ListBucket"`
        	+ `"s3:GetBucketAcl"`

    The following is an example of what the updated policy might look
    like.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy15397346",
 "Statement": [
 {
 "Sid": "Stmt15399483",
 "Effect": "Allow",
 "Principal": {
 "Service": "us-east-1.memorydb-snapshot.amazonaws.com"
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket",
 "s3:GetBucketAcl"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/snapshot1.rdb",
 "arn:aws:s3:::amzn-s3-demo-bucket/snapshot2.rdb"
 ]
 }
 ]
}`

```

8. Choose **Save**.

## Step 5: Seed the MemoryDB cluster with the .rdb file data

Now you are ready to create a MemoryDB cluster and seed it with the data from the .rdb file.
To create the cluster, follow the directions at [Creating a MemoryDB cluster](getting-started.md#clusters.create "getting-started.md#clusters.create").

The method you use to tell MemoryDB where to find the snapshot you uploaded to Amazon S3
depends on the method you use to create the cluster:

###### Seed the MemoryDB cluster with the .rdb file data

- **Using the MemoryDB console**

After you choose the engine, expand the **Advanced settings** section and locate **Import data to
cluster**. In the **Seed RDB file S3
location** box, type in the Amazon S3 path for the files(s). If you
have multiple .rdb files, type in the path for each file in a comma
separated list. The Amazon S3 path looks something like
``amzn-s3-demo-bucket`/`myFolder`/`myBackupFilename`.rdb`.

- **Using the AWS CLI**

If you use the `create-cluster` or the `create-cluster` operation,
use the parameter `--snapshot-arns` to specify a fully qualified ARN for each .rdb file.
For example, `arn:aws:s3:::`amzn-s3-demo-bucket`/`myFolder`/`myBackupFilename`.rdb`.
The ARN must resolve to the snapshot files you stored in Amazon S3.

- **Using the MemoryDB API**

If you use the `CreateCluster` or the `CreateCluster` MemoryDB API operation,
use the parameter `SnapshotArns` to specify a fully qualified ARN for each .rdb file.
For example, `arn:aws:s3:::`amzn-s3-demo-bucket`/`myFolder`/`myBackupFilename`.rdb`.
The ARN must resolve to the snapshot files you stored in Amazon S3.

During the process of creating your cluster, the data in your snapshot is
written to the cluster. You can monitor the progress by viewing the MemoryDB event
messages. To do this, see the MemoryDB console and choose **Events**. You can also use the AWS MemoryDB command line interface or
MemoryDB API to obtain event messages.
