# Exporting a backup

Amazon ElastiCache supports exporting your ElastiCache for Redis OSS backup to an Amazon Simple Storage Service (Amazon S3) bucket,
which gives you access to it from outside ElastiCache.
You can export a backup using the ElastiCache console, the AWS CLI, or the ElastiCache API.

Exporting a backup can be helpful if you need to launch a cluster in another AWS Region.
You can export your data in one AWS Region, copy the .rdb file to the new AWS Region,
and then use that .rdb file to seed the new cache instead of waiting for the new
cluster to populate through use. For information about seeding a new cluster, see [Tutorial: Seeding a new node-based cluster with an externally created backup](backups-seeding-redis.md "backups-seeding-redis.md").
Another reason you might want to export your cache's data is to use the .rdb file for offline processing.

###### Important

- The ElastiCache backup and the Amazon S3 bucket that you want to copy it to must be in the same AWS Region.

Though backups copied to an Amazon S3 bucket are encrypted,
we strongly recommend that you do not grant others access to the Amazon S3 bucket
where you want to store your backups.

- Exporting a backup to Amazon S3 is not supported for clusters using data tiering. For more information, see [Data tiering in ElastiCache](data-tiering.md "data-tiering.md").
- Exporting a backup is available for: node-based Valkey clusters, node-based Redis OSS clusters, and Valkey, Memcached, and Redis OSS serverless caches. Exporting a backup is not available for node-based Memcached clusters.
  Before you can export a backup to an Amazon S3 bucket, you must have an Amazon S3 bucket in the
  same AWS Region as the backup. Grant ElastiCache access to the bucket. The first two steps
  show you how to do this.

## Create an Amazon S3 bucket

The following steps use the Amazon S3 console to create an Amazon S3 bucket where you
export and store your ElastiCache backup.

###### To create an Amazon S3 bucket

1.  Sign in to the AWS Management Console and open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  Choose **Create Bucket**.
3.  In **Create a Bucket - Select a Bucket Name and Region**, do the following:
    1. In **Bucket Name**,
       type a name for your Amazon S3 bucket.

    The name of your Amazon S3 bucket must be DNS-compliant. Otherwise, ElastiCache can't
    access your backup file. The rules for DNS compliance are:

        * Names must be at least 3 and no more than 63 characters long.
        * Names must be a series of one or more labels separated by a period (.) where each label:




        	+ Starts with a lowercase letter or a number.
        	+ Ends with a lowercase letter or a number.
        	+ Contains only lowercase letters, numbers, and dashes.
        * Names can't be formatted as an IP address (for example, 192.0.2.0).

    2. From the **Region** list, choose an AWS Region for your Amazon S3 bucket.
       This AWS Region must be the same AWS Region as the ElastiCache backup you want to export.
    3. Choose **Create**.

For more information about creating an Amazon S3 bucket, see [Creating a bucket](../../../AmazonS3/latest/userguide/CreatingaBucket.md "../../../AmazonS3/latest/userguide/CreatingaBucket.md") in the _Amazon Simple Storage Service User Guide_.

## Grant ElastiCache access to your Amazon S3 bucket

For ElastiCache to be able to copy a snapshot to an Amazon S3 bucket, you must update your IAM bucket policy to grant ElastiCache access to the
bucket.

###### Warning

Even though backups copied to an Amazon S3 bucket are encrypted, your data can be
accessed by anyone with access to your Amazon S3 bucket. Therefore, we strongly
recommend that you set up IAM policies to prevent unauthorized access to this
Amazon S3 bucket. For more information, see [Managing
access](../../../AmazonS3/latest/userguide/s3-access-control.md "../../../AmazonS3/latest/userguide/s3-access-control.md") in the _Amazon S3 User Guide_.

To create the proper permissions on an Amazon S3 bucket, take the steps described following.

###### To grant ElastiCache access to an S3 bucket

1.  Sign in to the AWS Management Console and open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  Choose the name of the Amazon S3 bucket that you want to copy the backup to.
    This should be the S3 bucket that you created in [Create an Amazon S3 bucket](#backups-exporting-create-s3-bucket "#backups-exporting-create-s3-bucket").
3.  Choose the **Permissions** tab and under **Permissions**, choose **Access control list (ACL)** and then choose **Edit**.
4.  Add grantee Canonical Id `540804c33a284a299d2547575ce1010f2312ef3da9b3a053c8bc45bf233e4353` with the following options:
    - **Objects: List, Write**
    - **Bucket ACL: Read, Write**

    ###### Note

        + For the PDT GovCloud Region, the Canonical Id is `40fa568277ad703bd160f66ae4f83fc9dfdfd06c2f1b5060ca22442ac3ef8be6`.
        + For the OSU GovCloud Region, the Canonical Id is `c54286759d2a83da9c480405349819c993557275cf37d820d514b42da6893f5c`.

5.  Choose **Save**.

## Export an ElastiCache backup

Now you've created your S3 bucket and granted ElastiCache permissions to access it.
Next, you can use the ElastiCache console, the AWS CLI, or the ElastiCache API to export your
snapshot to it.

The following is an example of what the updated policy might look like.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy15397346",
 "Statement": [
 {
 "Sid": "Stmt15399484",
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::hkg-elasticache-backup",
 "arn:aws:s3:::hkg-elasticache-backup/*"
 ]
 }
 ]
}`

```

For opt-in Regions, the following is an example of what the updated IAM policy for the S3 bucket might look like. (This examples uses the Asia Pacific (Hong Kong) Region.)

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Policy15397346",
 "Statement": [
 {
 "Sid": "Stmt15399483",
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::hkg-elasticache-backup",
 "arn:aws:s3:::hkg-elasticache-backup/*"
 ]
 },
 {
 "Sid": "Stmt15399484",
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::hkg-elasticache-backup",
 "arn:aws:s3:::hkg-elasticache-backup/*"
 ]
 }
 ]
}`

```

The following steps use the ElastiCache console to export a backup to an Amazon S3 bucket
so that you can access it from outside ElastiCache.
The Amazon S3 bucket must be in the same AWS Region as the ElastiCache backup.

###### To export an ElastiCache backup to an Amazon S3 bucket

1.  Sign in to the AWS Management Console and open the ElastiCache console at
    [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2.  To see a list of your backups,
    from the left navigation pane choose **Backups**.
3.  From the list of backups, choose the box to the left of the name of the backup you want to export.
4.  Choose **Copy**.
5.  In **Create a Copy of the Backup?**, do the following:
    1. In **New backup name** box,
       type a name for your new backup.

    The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

    ElastiCache adds an instance identifier and `.rdb` to the
    value that you enter here. For example, if you enter `my-exported-backup`,
    ElastiCache creates `my-exported-backup-0001.rdb`. 2. From the **Target S3 Location** list,
    choose the name of the Amazon S3 bucket that you want to copy your backup to (the bucket that you created in [Create an Amazon S3 bucket](#backups-exporting-create-s3-bucket "#backups-exporting-create-s3-bucket")).

    The **Target S3 Location** must be an Amazon S3 bucket
    in the backup's AWS Region with the following permissions for the export process to succeed.

        * Object access – **Read** and **Write**.
        * Permissions access – **Read**.

    For more information, see [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access "#backups-exporting-grant-access"). 3. Choose **Copy**.

###### Note

If your S3 bucket does not have the permissions needed for ElastiCache to export a backup to it, you
receive one of the following error messages. Return to [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access "#backups-exporting-grant-access") to add the permissions
specified and retry exporting your backup.

- ElastiCache has not been granted READ permissions %s on the S3 Bucket.

**Solution:**
Add Read permissions on the bucket.

- ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.

**Solution:**
Add Write permissions on the bucket.

- ElastiCache has not been granted READ_ACP permissions %s on the S3 Bucket.

**Solution:**
Add **Read** for Permissions access on the bucket.
If you want to copy your backup to another AWS Region, use Amazon S3 to copy it. For more information, see [Copying an object](../../../AmazonS3/latest/userguide/MakingaCopyofanObject.md "../../../AmazonS3/latest/userguide/MakingaCopyofanObject.md") in the _Amazon Simple Storage Service User Guide_.

**Exporting a backup of a serverless cache**

Export the backup to an Amazon S3 bucket using the `export-serverless-cache-snapshot` CLI operation with
the following parameters:

###### Parameters

- `--serverless-cache-snapshot-name` –
  Name of the backup to be copied.
- `--s3-bucket-name` –

Name of the Amazon S3 bucket where you want to export the backup.
A copy of the backup is made in the specified bucket.

The `--s3-bucket-name` must be an Amazon S3 bucket in the backup's AWS Region
with the following permissions for the export process to succeed.

    + Object access – **Read** and **Write**.
    + Permissions access – **Read**.

The following operation copies a backup to my-s3-bucket.

For Linux, macOS, or Unix:

```
aws elasticache export-serverless-cache-snapshot \
    --serverless-cache-snapshot-name `automatic.my-redis-2023-11-27` \
    --s3-bucket-name `my-s3-bucket`
```

For Windows:

```
aws elasticache export-serverless-cache-snapshot ^
    --serverless-cache-snapshot-name `automatic.my-redis-2023-11-27` ^
    --s3-bucket-name `my-s3-bucket`
```

**Exporting a backup of a node-based cluster**

Export the backup to an Amazon S3 bucket using the `copy-snapshot` CLI operation with
the following parameters:

###### Parameters

- `--source-snapshot-name` –
  Name of the backup to be copied.
- `--target-snapshot-name` –
  Name of the backup's copy.

The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

ElastiCache adds an instance identifier and `.rdb` to the
value you enter here. For example, if you enter `my-exported-backup`,
ElastiCache creates `my-exported-backup-0001.rdb`.

- `--target-bucket` –
  Name of the Amazon S3 bucket where you want to export the backup.
  A copy of the backup is made in the specified bucket.

The `--target-bucket` must be an Amazon S3 bucket
in the backup's AWS Region with the following permissions for the export process to succeed.

    + Object access – **Read** and **Write**.
    + Permissions access – **Read**.

For more information, see [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access "#backups-exporting-grant-access").
The following operation copies a backup to my-s3-bucket.

For Linux, macOS, or Unix:

```
aws elasticache copy-snapshot \
    --source-snapshot-name `automatic.my-redis-primary-2016-06-27-03-15` \
    --target-snapshot-name `my-exported-backup` \
    --target-bucket `my-s3-bucket`
```

For Windows:

```
aws elasticache copy-snapshot ^
    --source-snapshot-name `automatic.my-redis-primary-2016-06-27-03-15` ^
    --target-snapshot-name `my-exported-backup` ^
    --target-bucket `my-s3-bucket`
```
