# Tutorial: Seeding a new node-based cluster with an externally created backup

When you create a new Valkey or Redis OSS node-based cluster, you can seed it with data from a Valkey or Redis OSS .rdb backup file.
Seeding the cluster is useful if you currently manage a Valkey or Redis OSS instance outside of ElastiCache and
want to populate your new ElastiCache for Redis OSS node-based cluster with your existing Valkey or Redis OSS data.

To seed a new Valkey or Redis OSS node-based cluster from a Valkey or Redis OSS backup created within Amazon ElastiCache,
see [Restoring from a backup into a new cache](backups-restoring.md "backups-restoring.md").

When you use a Valkey or Redis OSS .rdb file to seed a new node-based cluster, you can do the
following:

- Upgrade from a nonpartitioned cluster to a Valkey or Redis OSS (cluster mode enabled) node-based cluster.
- Specify a number of shards (called node groups in the API and CLI) in the new
  node-based cluster. This number can be different from the number of shards in the node-based cluster
  that was used to create the backup file.
- Specify a different node type for the new node-based cluster—larger or smaller than
  that used in the cluster that made the backup. If you scale to a smaller node
  type, be sure that the new node type has sufficient memory for your data and
  Valkey or Redis OSS overhead. For more information, see [Ensuring you have enough memory to make a Valkey or Redis OSS snapshot](BestPractices.BGSAVE.md "BestPractices.BGSAVE.md").
- Distribute your keys in the slots of the new Valkey or Redis OSS (cluster mode enabled) cluster differently than in the cluster that was
  used to create the backup file.

###### Note

You can't seed a Valkey or Redis OSS (cluster mode disabled) cluster from an .rdb file created from a Valkey or Redis OSS (cluster mode enabled) cluster.

###### Important

- You must ensure that your Valkey or Redis OSS backup data doesn't exceed the resources
  of the node. For example, you can't upload an .rdb file with 5 GB of Valkey or Redis OSS data to a cache.t3.medium node that has 3.09 GB of memory.

If the backup is too large, the resulting cluster has a status of
`restore-failed`. If this happens, you must delete the
cluster and start over.

For a complete listing of node types and specifications,
see [Redis OSS node-type specific parameters](ParameterGroups.Engine.md#ParameterGroups.Redis.NodeSpecific "ParameterGroups.Engine.md#ParameterGroups.Redis.NodeSpecific")
and [Amazon ElastiCache product features and details](https://aws.amazon.com/elasticache/details/ "https://aws.amazon.com/elasticache/details/").

- You can encrypt a Valkey or Redis OSS .rdb file with Amazon S3 server-side encryption using
  Amazon S3 managed keys (SSE-S3) or AWS KMS keys (SSE-KMS). If you use SSE-KMS, you must grant
  ElastiCache decrypt permissions on the KMS key and disable Amazon S3 Bucket Keys. For more information,
  see [Grant ElastiCache access to a KMS-encrypted .rdb file](#backups-seeding-redis-kms-encryption "#backups-seeding-redis-kms-encryption"). For general information about
  server-side encryption, see
  [Protecting data using server-side encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md").
  Following, you can find topics that walk you through migrating your cluster from
  outside ElastiCache for Valkey or Redis OSS to ElastiCache for Redis OSS.

###### Migrating to ElastiCache for Redis OSS

- [Step 1: Create a Valkey or Redis OSS backup](#backups-seeding-redis-create-backup "#backups-seeding-redis-create-backup")
- [Step 2: Create an Amazon S3 bucket and folder](#backups-seeding-redis-create-s3-bucket "#backups-seeding-redis-create-s3-bucket")
- [Step 3: Upload your backup to Amazon S3](#backups-seeding-redis-upload "#backups-seeding-redis-upload")
- [Step 4: Grant ElastiCache read access to the .rdb file](#backups-seeding-redis-grant-access "#backups-seeding-redis-grant-access")

###### Migrating from external services to ElastiCache for Redis OSS.

- [Step 1: Create a Valkey or Redis OSS backup](#backups-seeding-redis-create-backup "#backups-seeding-redis-create-backup")
- [Step 2: Create an Amazon S3 bucket and folder](#backups-seeding-redis-create-s3-bucket "#backups-seeding-redis-create-s3-bucket")
- [Step 3: Upload your backup to Amazon S3](#backups-seeding-redis-upload "#backups-seeding-redis-upload")
- [Step 4: Grant ElastiCache read access to the .rdb file](#backups-seeding-redis-grant-access "#backups-seeding-redis-grant-access")

## Step 1: Create a Valkey or Redis OSS backup

###### To create the Valkey or Redis OSS backup to seed your ElastiCache for Redis OSS instance

1. Connect to your existing Valkey or Redis OSS instance.
2. Run either `BGSAVE` or `SAVE` operation to create a backup.
   Note where your .rdb file is located.

`BGSAVE` is asynchronous and does not block other clients while processing.
For more information, see [BGSAVE](https://valkey.io/commands/bgsave "https://valkey.io/commands/bgsave") at the Valkey website.

`SAVE` is synchronous and blocks other processes until finished.
For more information, see [SAVE](https://valkey.io/commands/save "https://valkey.io/commands/save") at the Valkey website.

For additional information on creating a backup, see [Persistence](https://valkey.io/topics/persistence "https://valkey.io/topics/persistence") at the Valkey website.

## Step 2: Create an Amazon S3 bucket and folder

When you have created the backup file, you need to upload it to a folder within an
Amazon S3 bucket. To do that, you must first have an Amazon S3 bucket and folder within that
bucket. If you already have an Amazon S3 bucket and folder with the appropriate
permissions, you can skip to [Step 3: Upload your backup to Amazon S3](#backups-seeding-redis-upload "#backups-seeding-redis-upload").

###### To create an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Follow the instructions for creating an Amazon S3 bucket in [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the
   _Amazon Simple Storage Service User Guide_.

The name of your Amazon S3 bucket must be DNS-compliant. Otherwise, ElastiCache can't
access your backup file. The rules for DNS compliance are:

    * Names must be at least 3 and no more than 63 characters long.
    * Names must be a series of one or more labels separated by a period (.) where each label:




    	+ Starts with a lowercase letter or a number.
    	+ Ends with a lowercase letter or a number.
    	+ Contains only lowercase letters, numbers, and dashes.
    * Names can't be formatted as an IP address (for example, 192.0.2.0).

You must create your Amazon S3 bucket in the same AWS Region
as your new ElastiCache for Redis OSS cluster. This approach makes sure that the
highest data transfer speed when ElastiCache reads your .rdb file from
Amazon S3.

###### Note

To keep your data as secure as possible, make the permissions on your
Amazon S3 bucket as restrictive as you can. At the same time, the permissions still need to allow
the bucket and its contents to be used to seed your new Valkey or Redis OSS cluster.

###### To add a folder to an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the name of the bucket to upload your .rdb file to.
3. Choose **Create folder**.
4. Enter a name for your new folder.
5. Choose **Save**.

Make note of both the bucket name and the folder name.

## Step 3: Upload your backup to Amazon S3

Now, upload the .rdb file that you created in [Step 1: Create a Valkey or Redis OSS backup](#backups-seeding-redis-create-backup "#backups-seeding-redis-create-backup"). You upload it to the Amazon S3
bucket and folder that you created in [Step 2: Create an Amazon S3 bucket and folder](#backups-seeding-redis-create-s3-bucket "#backups-seeding-redis-create-s3-bucket"). For more information
on this task, see [Add an object to a
bucket](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md"). Between steps 2 and 3, choose the name of the folder you created
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
   **Upload** dialog box, and then choose
   **Upload**.

Note the path to your .rdb file. For example, if your bucket name is
`myBucket` and the path is `myFolder/redis.rdb`, enter
`myBucket/myFolder/redis.rdb`. You need this path to seed the new
cluster with the data in this backup.

For additional information, see [Bucket restrictions and limitations](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md")
in the _Amazon Simple Storage Service User Guide_.

## Step 4: Grant ElastiCache read access to the .rdb file

Now, grant ElastiCache read access to your .rdb backup file. You grant ElastiCache access to
your backup file in a different way depending if your bucket is in a default AWS
Region or an opt-in AWS Region.

AWS Regions introduced before March 20, 2019, are enabled by default. You can
begin working in these AWS Regions immediately. Regions introduced after March 20,
2019, such as Asia Pacific (Hong Kong) and Middle East (Bahrain), are disabled by default.
You must enable, or opt in, to these Regions before you can use them, as described
in [Managing AWS

regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in _AWS General Reference_.

Choose your approach depending on your AWS Region:

- For a default Region, use the procedure in [Grant ElastiCache read access to the .rdb file in a default Region](#backups-seeding-redis-default-region "#backups-seeding-redis-default-region").
- For an opt-in Region, use the procedure in [Grant ElastiCache read access to the .rdb file in an opt-in Region](#backups-seeding-opt-in-region "#backups-seeding-opt-in-region").

### Grant ElastiCache read access to the .rdb file in a default Region

AWS Regions introduced before March 20, 2019, are enabled by default. You can
begin working in these AWS Regions immediately. Regions introduced after March 20,
2019, such as Asia Pacific (Hong Kong) and Middle East (Bahrain), are disabled by default.
You must enable, or opt in, to these Regions before you can use them, as described
in [Managing AWS
regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in _AWS General Reference_.

###### To grant ElastiCache read access to the backup file in an AWS Region enabled by default

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the name of the S3 bucket that contains your .rdb file.
3. Choose the **Permissions** tab.
4. Under **Bucket policy**, choose **Edit**.
5. Add a bucket policy that grants ElastiCache the required permissions. The following
   example grants the ElastiCache service principal read access to the bucket and its
   objects. Replace `amzn-s3-demo-bucket` with the name of your
   S3 bucket. Replace `region-full-name` with the AWS Region
   identifier where your cluster is located (for example,
   `us-east-1`).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ElastiCacheSnapshotAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "`region-full-name`.elasticache-snapshot.amazonaws.com"
            },
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",
                "s3:GetBucketAcl"
            ],
            "Resource": [
                "arn:aws:s3:::`amzn-s3-demo-bucket`",
                "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
            ]
        }
    ]
}
```

6. Choose **Save changes**.

### Grant ElastiCache read access to the .rdb file in an opt-in Region

AWS Regions introduced before March 20, 2019, are enabled by default. You can
begin working in these AWS Regions immediately. Regions introduced after March 20,
2019, such as Asia Pacific (Hong Kong) and Middle East (Bahrain), are disabled by default.
You must enable, or opt in, to these Regions before you can use them, as described
in [Managing AWS
regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in _AWS General Reference_.

Now, grant ElastiCache read access to your .rdb backup file.

###### To grant ElastiCache read access to the backup file

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the name of the S3 bucket that contains your .rdb file.
3. Choose the name of the folder that contains your .rdb file.
4. Choose the name of your .rdb backup file. The name of the selected file
   appears above the tabs at the top of the page.
5. Choose the **Permissions** tab.
6. Under **Permissions**, choose **Bucket
   policy** and then choose **Edit**.
7. Update the policy to grant ElastiCache required permissions to perform
   operations:

   - Add `[ "Service" : "`region-full-name`.elasticache-snapshot.amazonaws.com" ]` to `Principal`.
   - Add the following permissions required for exporting a snapshot to the Amazon S3 bucket:

     - `"s3:GetObject"`
     - `"s3:ListBucket"`
     - `"s3:GetBucketAcl"`
       The following is an example of what the updated policy might look like.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ElastiCacheSnapshotExport",
 "Effect": "Allow",
 "Principal": {
 "Service": "`region`.elasticache-snapshot.amazonaws.com"
 },
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:GetBucketAcl",
 "s3:ListMultipartUploadParts",
 "s3:ListBucketMultipartUploads"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 }
 ]
}`

```

8. Choose **Save changes**.

### Grant ElastiCache access to a KMS-encrypted .rdb file

If your Amazon S3 bucket uses AWS KMS server-side encryption (SSE-KMS), you must also
grant ElastiCache permissions on the KMS key so that it can decrypt the .rdb file during the
restore process.

###### To grant ElastiCache decrypt permissions on a KMS key

1. Open the AWS KMS console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. Choose the KMS key that is used to encrypt the Amazon S3 bucket.
3. Under **Key policy**, choose **Edit**.
4. Add the following statement to the key policy to grant ElastiCache decrypt
   permissions:

```
{
    "Sid": "AllowElastiCacheDecrypt",
    "Effect": "Allow",
    "Principal": {
        "Service": "`region-full-name`.elasticache-snapshot.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
    ],
    "Resource": "*"
}
```

Replace `region-full-name` with the AWS Region
identifier where your cluster is located (for example,
`us-west-2`). 5. Choose **Save changes**.

In addition, you must disable Amazon S3 Bucket Keys for the bucket. ElastiCache does not support
reading objects encrypted with Amazon S3 Bucket Keys. To disable this setting, see
[Configuring S3 Bucket
Keys](../../../AmazonS3/latest/userguide/configuring-bucket-key.md "../../../AmazonS3/latest/userguide/configuring-bucket-key.md") in the _Amazon Simple Storage Service User Guide_.

### Seed the ElastiCache cluster with the .rdb file data

Now you are ready to create an ElastiCache cluster and seed it with the data from the .rdb file.
To create the cluster, follow the directions at [Creating a cluster for Valkey or Redis OSS](Clusters.Create.md "Clusters.Create.md")
or [Creating a Valkey or Redis OSS replication group from scratch](Replication.CreatingReplGroup.NoExistingCluster.md "Replication.CreatingReplGroup.NoExistingCluster.md").
Be sure to choose Valkey or Redis OSS as your cluster engine.

The method you use to tell ElastiCache where to find the backup you uploaded to Amazon S3
depends on the method you use to create the cluster:

###### Seed the ElastiCache for Redis OSS cluster or replication group with the .rdb file data

- **Using the ElastiCache console**

When selecting **Cluster settings**, choose **Restore from backups** as your cluster creation method, then choose **Other backups**
as your **Source** in the **Backup source** section. In the **Seed RDB file S3
location** box, type in the Amazon S3 path for the files(s). If you
have multiple .rdb files, type in the path for each file in a comma
separated list. The Amazon S3 path looks something like
``myBucket`/`myFolder`/`myBackupFilename`.rdb`.

- **Using the AWS CLI**

If you use the `create-cache-cluster` or the `create-replication-group` operation,
use the parameter `--snapshot-arns` to specify a fully qualified ARN for each .rdb file.
For example, `arn:aws:s3:::`myBucket`/`myFolder`/`myBackupFilename`.rdb`.
The ARN must resolve to the backup files you stored in Amazon S3.

- **Using the ElastiCache API**

If you use the `CreateCacheCluster` or the `CreateReplicationGroup` ElastiCache API operation,
use the parameter `SnapshotArns` to specify a fully qualified ARN for each .rdb file.
For example, `arn:aws:s3:::`myBucket`/`myFolder`/`myBackupFilename`.rdb`.
The ARN must resolve to the backup files you stored in Amazon S3.

###### Important

When seeding a Valkey or Redis OSS (cluster mode enabled) cluster, you must configure each node group (shard) in the new cluster or replication group. Use the
parameter `--node-group-configuration` (API: `NodeGroupConfiguration`) to do this. For more information, see the following:

- CLI: [create-replication-group](../../../cli/latest/reference/elasticache/create-replication-group.md "../../../cli/latest/reference/elasticache/create-replication-group.md") in the AWS CLI Reference
- API: [CreateReplicationGroup](../APIReference/API_CreateReplicationGroup.md "../APIReference/API_CreateReplicationGroup.md") in the ElastiCache API Reference

During the process of creating your cluster, the data in your Valkey or Redis OSS backup is
written to the cluster. You can monitor the progress by viewing the ElastiCache event
messages. To do this, see the ElastiCache console and choose **Cache
Events**. You can also use the AWS ElastiCache command line interface or
ElastiCache API to obtain event messages. For more information, see [Viewing ElastiCache events](ECEvents.Viewing.md "ECEvents.Viewing.md").
