# Exporting a snapshot

MemoryDB supports exporting your MemoryDB snapshot to an Amazon Simple Storage Service (Amazon S3) bucket,
which gives you access to it from outside MemoryDB. Exported MemoryDB snapshots are fully-compliant
with Valkey and open-source Redis OSS and can be loaded with the appropriate version or
tooling.
You can export a snapshot using the MemoryDB console, the AWS CLI, or the MemoryDB API.

Exporting a snapshot can be helpful if you need to launch a cluster in another AWS Region.
You can export your data in one AWS Region, copy the .rdb file to the new AWS Region,
and then use that .rdb file to seed the new cluster instead of waiting for the new
cluster to populate through use. For information about seeding a new cluster, see [Seeding a new cluster with an externally created snapshot](snapshots-seeding-redis.md "snapshots-seeding-redis.md").
Another reason you might want to export your cluster's data is to use the .rdb file for offline processing.

###### Important

- The MemoryDB snapshot and the Amazon S3 bucket that you want to copy it to must be in the same AWS Region.

Though snapshots copied to an Amazon S3 bucket are encrypted,
we strongly recommend that you do not grant others access to the Amazon S3 bucket
where you want to store your snapshots.

- Exporting a snapshot to Amazon S3 is not supported for clusters using data tiering. For more information, see [Data tiering](data-tiering.md "data-tiering.md").
  Before you can export a snapshot to an Amazon S3 bucket, you must have an Amazon S3 bucket in the
  same AWS Region as the snapshot. Grant MemoryDB access to the bucket. The first two steps
  show you how to do this.

###### Warning

The following scenarios expose your data in ways that you might not want:

- **When another person has access to the Amazon S3 bucket
  that you exported your snapshot to.**

To control access to your snapshots, only allow access to the Amazon S3 bucket to
those whom you want to access your data. For information about managing
access to an Amazon S3 bucket, see [Managing access](../../../AmazonS3/latest/dev/s3-access-control.md "../../../AmazonS3/latest/dev/s3-access-control.md") in the _Amazon S3 Developer
Guide_.

- **When another person has permissions to use the
  CopySnapshot API operation.**

Users or groups that have permissions to use the `CopySnapshot`
API operation can create their own Amazon S3 buckets and copy snapshots to them. To
control access to your snapshots, use an AWS Identity and Access Management (IAM) policy to control who has the
ability to use the `CopySnapshot` API. For more
information about using IAM to control the use of MemoryDB API
operations, see [Identity and access management in MemoryDB](iam.md "iam.md") in the
_MemoryDB User Guide_.

###### Topics

- [Step 1: Create an Amazon S3 bucket](#snapshots-exporting-create-s3-bucket "#snapshots-exporting-create-s3-bucket")
- [Step 2: Grant MemoryDB access to your
  Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access")
- [Step 3: Export a MemoryDB snapshot](#snapshots-exporting-procedures "#snapshots-exporting-procedures")

## Step 1: Create an Amazon S3 bucket

The following procedure uses the Amazon S3 console to create an Amazon S3 bucket where you
export and store your MemoryDB snapshot.

###### To create an Amazon S3 bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create Bucket**.
3. In **Create a Bucket - Select a Bucket Name and Region**, do the following:
   1. In **Bucket Name**,
      type a name for your Amazon S3 bucket.
   2. From the **Region** list, choose an AWS Region for your Amazon S3 bucket.
      This AWS Region must be the same AWS Region as the MemoryDB snapshot you want to export.
   3. Choose **Create**.

For more information about creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_.

## Step 2: Grant MemoryDB access to your

Amazon S3 bucket

AWS Regions introduced before March 20, 2019, are enabled by default. You can
begin working in these AWS Regions immediately. Regions introduced after March 20,
2019 are disabled by default.
You must enable, or opt in, to these Regions before you can use them, as described
in [Managing AWS
regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md").

### Grant MemoryDB access to your

S3 Bucket in an AWS Region

To create the proper permissions on an Amazon S3 bucket in an AWS Region, take
the following steps.

###### To grant MemoryDB access to an S3 bucket

1.  Sign in to the AWS Management Console and open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  Choose the name of the Amazon S3 bucket that you want to copy the snapshot to.
    This should be the S3 bucket that you created in [Step 1: Create an Amazon S3 bucket](#snapshots-exporting-create-s3-bucket "#snapshots-exporting-create-s3-bucket").
3.  Choose the **Permissions** tab and under **Permissions**, choose **Bucket policy**.
4.  Update the policy to grant MemoryDB required permissions to perform
    operations:

        * Add `[ "Service" : "`region-full-name`.memorydb-snapshot.amazonaws.com" ]` to `Principal`.
        * Add the following permissions required for exporting a snapshot to the Amazon S3 bucket.




        	+ `"s3:PutObject"`
        	+ `"s3:GetObject"`
        	+ `"s3:ListBucket"`
        	+ `"s3:GetBucketAcl"`
        	+ `"s3:ListMultipartUploadParts"`
        	+ `"s3:ListBucketMultipartUploads"`

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
 "Service": "`aws-region`.memorydb-snapshot.amazonaws.com"
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
 "arn:aws:s3:::amzn-s3-demo-bucket",
 "arn:aws:s3:::amzn-s3-demo-bucket/*"
 ]
 }
 ]
}`

```

## Step 3: Export a MemoryDB snapshot

Now you've created your S3 bucket and granted MemoryDB permissions to access it. Change the S3 Object Ownership to _ACLs enabled - Bucket owner preferred_.
Next, you can use the MemoryDB console, the AWS CLI, or the MemoryDB API to export your
snapshot to it. The following assumes that you have the following additional S3
specific IAM permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets",
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject",
 "s3:ListBucket"
 ],
 "Resource": "arn:aws:s3:::*"
 }]
}`

```

The following process uses the MemoryDB console to export a snapshot to an Amazon S3 bucket
so that you can access it from outside MemoryDB.
The Amazon S3 bucket must be in the same AWS Region as the MemoryDB snapshot.

###### To export a MemoryDB snapshot to an Amazon S3 bucket

1.  Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2.  To see a list of your snapshots,
    from the left navigation pane choose **Snapshots**.
3.  From the list of snapshots, choose the radio button to the left of the name of the snapshot you want to export.
4.  Choose **Copy**.
5.  In **Create a Copy of the Backup?**, do the following:
    1. In **New snapshot name** box,
       type a name for your new snapshot.

    The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

    MemoryDB adds a shard identifier and `.rdb` to the
    value that you enter here. For example, if you enter `my-exported-snapshot`,
    MemoryDB creates `my-exported-snapshot-0001.rdb`. 2. From the **Target S3 Location** list,
    choose the name of the Amazon S3 bucket that you want to copy your snapshot to (the bucket that you created in [Step 1: Create an Amazon S3 bucket](#snapshots-exporting-create-s3-bucket "#snapshots-exporting-create-s3-bucket")).

    The **Target S3 Location** must be an Amazon S3 bucket
    in the snapshot's AWS Region with the following permissions for the export process to succeed.

        * Object access – **Read** and **Write**.
        * Permissions access – **Read**.

    For more information, see [Step 2: Grant MemoryDB access to your
    Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access"). 3. Choose **Copy**.

###### Note

If your S3 bucket does not have the permissions needed for MemoryDB to export a snapshot to it, you
receive one of the following error messages. Return to [Step 2: Grant MemoryDB access to your
Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access") to add the permissions
specified and retry exporting your snapshot.

- MemoryDB has not been granted READ permissions %s on the S3 Bucket.

**Solution:**
Add Read permissions on the bucket.

- MemoryDB has not been granted WRITE permissions %s on the S3 Bucket.

**Solution:**
Add Write permissions on the bucket.

- MemoryDB has not been granted READ_ACP permissions %s on the S3 Bucket.

**Solution:**
Add **Read** for Permissions access on the bucket.
If you want to copy your snapshot to another AWS Region, use Amazon S3 to copy it. For more information, see [Copying objects](../../../AmazonS3/latest/userguide/copy-object.md "../../../AmazonS3/latest/userguide/copy-object.md") in the _Amazon Simple Storage Service User Guide_.

Export the snapshot to an Amazon S3 bucket using the `copy-snapshot` CLI operation with
the following parameters:

###### Parameters

- `--source-snapshot-name` –
  Name of the snapshot to be copied.
- `--target-snapshot-name` –
  Name of the snapshot's copy.

The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

MemoryDB adds a shard identifier and `.rdb` to the
value you enter here. For example, if you enter `my-exported-snapshot`,
MemoryDB creates `my-exported-snapshot-0001.rdb`.

- `--target-bucket` –
  Name of the Amazon S3 bucket where you want to export the snapshot.
  A copy of the snapshot is made in the specified bucket.

The `--target-bucket` must be an Amazon S3 bucket
in the snapshot's AWS Region with the following permissions for the export process to succeed.

    + Object access – **Read** and **Write**.
    + Permissions access – **Read**.

For more information, see [Step 2: Grant MemoryDB access to your
Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access").
The following operation copies a snapshot to amzn-s3-demo-bucket.

For Linux, macOS, or Unix:

```
aws memorydb copy-snapshot \
    --source-snapshot-name `automatic.my-primary-2021-06-27-03-15` \
    --target-snapshot-name `my-exported-snapshot` \
    --target-bucket `amzn-s3-demo-bucket`
```

For Windows:

```
aws memorydb copy-snapshot ^
    --source-snapshot-name `automatic.my-primary-2021-06-27-03-15` ^
    --target-snapshot-name `my-exported-snapshot` ^
    --target-bucket `amzn-s3-demo-bucket`
```

###### Note

If your S3 bucket does not have the permissions needed for MemoryDB to export a snapshot to it, you
receive one of the following error messages. Return to [Step 2: Grant MemoryDB access to your
Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access") to add the permissions
specified and retry exporting your snapshot.

- MemoryDB has not been granted READ permissions %s on the S3 Bucket.

**Solution:**
Add Read permissions on the bucket.

- MemoryDB has not been granted WRITE permissions %s on the S3 Bucket.

**Solution:**
Add Write permissions on the bucket.

- MemoryDB has not been granted READ_ACP permissions %s on the S3 Bucket.

**Solution:**
Add **Read** for Permissions access on the bucket.
For more information, see `copy-snapshot` in the _AWS CLI Command Reference_.

If you want to copy your snapshot to another AWS Region, use Amazon S3 copy. For more information,
see [Copying objects](../../../AmazonS3/latest/userguide/copy-object.md "../../../AmazonS3/latest/userguide/copy-object.md") in the _Amazon Simple Storage Service User Guide_.

Export the snapshot to an Amazon S3 bucket using the `CopySnapshot` API operation with
these parameters.

###### Parameters

- `SourceSnapshotName` –
  Name of the snapshot to be copied.
- `TargetSnapshotName` –
  Name of the snapshot's copy.

The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

MemoryDB adds a shard identifier and `.rdb` to the value
that you enter here. For example, if you enter
`my-exported-snapshot`, you get
`my-exported-snapshot-0001.rdb`.

- `TargetBucket` –
  Name of the Amazon S3 bucket where you want to export the snapshot.
  A copy of the snapshot is made in the specified bucket.

The `TargetBucket` must be an Amazon S3 bucket
in the snapshot's AWS Region with the following permissions for the export process to succeed.

    + Object access – **Read** and **Write**.
    + Permissions access – **Read**.

For more information, see [Step 2: Grant MemoryDB access to your
Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access").
The following example makes a copy of an automatic snapshot to the Amazon S3 bucket `amzn-s3-demo-bucket`.

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=CopySnapshot
    &SourceSnapshotName=automatic.my-primary-2021-06-27-03-15
    &TargetBucket=&example-s3-bucket;
    &TargetSnapshotName=my-snapshot-copy
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210801T220302Z
    &Version=2021-01-01
    &X-Amz-Algorithm=Amazon4-HMAC-SHA256
    &X-Amz-Date=20210801T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20210801T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```

###### Note

If your S3 bucket does not have the permissions needed for MemoryDB to export a snapshot to it, you
receive one of the following error messages. Return to [Step 2: Grant MemoryDB access to your
Amazon S3 bucket](#snapshots-exporting-grant-access "#snapshots-exporting-grant-access") to add the permissions
specified and retry exporting your snapshot.

- MemoryDB has not been granted READ permissions %s on the S3 Bucket.

**Solution:**
Add Read permissions on the bucket.

- MemoryDB has not been granted WRITE permissions %s on the S3 Bucket.

**Solution:**
Add Write permissions on the bucket.

- MemoryDB has not been granted READ_ACP permissions %s on the S3 Bucket.

**Solution:**
Add **Read** for Permissions access on the bucket.
For more information, see [CopySnapshot](../APIReference/API_CopySnapshot.md "../APIReference/API_CopySnapshot.md").

If you want to copy your snapshot to another AWS Region, use Amazon S3 copy to copy the exported snapshot
to the Amazon S3 bucket in another AWS Region. For more information, see [Copying objects](../../../AmazonS3/latest/userguide/copy-object.md "../../../AmazonS3/latest/userguide/copy-object.md") in the _Amazon Simple Storage Service User Guide_.
