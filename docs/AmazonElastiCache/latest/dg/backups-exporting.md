

# Exporting a backup
<a name="backups-exporting"></a>

Amazon ElastiCache supports exporting your ElastiCache for Redis OSS backup to an Amazon Simple Storage Service (Amazon S3) bucket, which gives you access to it from outside ElastiCache. You can export a backup using the ElastiCache console, the AWS CLI, or the ElastiCache API.

Exporting a backup can be helpful if you need to launch a cluster in another AWS Region. You can export your data in one AWS Region, copy the .rdb file to the new AWS Region, and then use that .rdb file to seed the new cache instead of waiting for the new cluster to populate through use. For information about seeding a new cluster, see [Tutorial: Seeding a new node-based cluster with an externally created backup](backups-seeding-redis.md). Another reason you might want to export your cache's data is to use the .rdb file for offline processing.

**Important**  
 The ElastiCache backup and the Amazon S3 bucket that you want to copy it to must be in the same AWS Region.  
Though backups copied to an Amazon S3 bucket are encrypted, we strongly recommend that you do not grant others access to the Amazon S3 bucket where you want to store your backups.
Exporting a backup to Amazon S3 is not supported for clusters using data tiering. For more information, see [Data tiering in ElastiCache](data-tiering.md).
Exporting a backup is available for: node-based Valkey clusters, node-based Redis OSS clusters, and Valkey, Memcached, and Redis OSS serverless caches. Exporting a backup is not available for node-based Memcached clusters.

Before you can export a backup to an Amazon S3 bucket, you must have an Amazon S3 bucket in the same AWS Region as the backup. Grant ElastiCache access to the bucket. The first two steps show you how to do this.

## Create an Amazon S3 bucket
<a name="backups-exporting-create-s3-bucket"></a>

The following steps use the Amazon S3 console to create an Amazon S3 bucket where you export and store your ElastiCache backup.

**To create an Amazon S3 bucket**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose **Create Bucket**.

1. In **Create a Bucket - Select a Bucket Name and Region**, do the following:

   1. In **Bucket Name**, type a name for your Amazon S3 bucket.

      The name of your Amazon S3 bucket must be DNS-compliant. Otherwise, ElastiCache can't access your backup file. The rules for DNS compliance are:
      + Names must be at least 3 and no more than 63 characters long.
      + Names must be a series of one or more labels separated by a period (.) where each label:
        + Starts with a lowercase letter or a number.
        + Ends with a lowercase letter or a number.
        + Contains only lowercase letters, numbers, and dashes.
      + Names can't be formatted as an IP address (for example, 192.0.2.0).

   1. From the **Region** list, choose an AWS Region for your Amazon S3 bucket. This AWS Region must be the same AWS Region as the ElastiCache backup you want to export.

   1. Choose **Create**.

For more information about creating an Amazon S3 bucket, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingaBucket.html) in the *Amazon Simple Storage Service User Guide*. 

## Grant ElastiCache access to your Amazon S3 bucket
<a name="backups-exporting-grant-access"></a>

ElastiCache requires access to your Amazon S3 bucket to copy a snapshot to it. We recommend granting access by using an Amazon S3 bucket policy rather than access control lists (ACLs).

**Warning**  
Even though backups copied to an Amazon S3 bucket are encrypted, your data can be accessed by anyone with access to your Amazon S3 bucket. Therefore, we strongly recommend that you set up IAM policies to prevent unauthorized access to this Amazon S3 bucket. For more information, see [Managing access](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User Guide*.

Add the following bucket policy to your Amazon S3 bucket. Replace `{{amzn-s3-demo-bucket}}` with the name of your Amazon S3 bucket and `{{region}}` with the AWS Region of your bucket (for example, `us-east-1`).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ElastiCacheSnapshotExport",
            "Effect": "Allow",
            "Principal": {
                "Service": "{{region}}.elasticache-snapshot.amazonaws.com"
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
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        }
    ]
}
```

------

**To add the bucket policy using the Amazon S3 console**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the name of the Amazon S3 bucket that you want to copy the backup to. This should be the S3 bucket that you created in [Create an Amazon S3 bucket](#backups-exporting-create-s3-bucket).

1. Choose the **Permissions** tab.

1. Under **Bucket policy**, choose **Edit**.

1. Paste the bucket policy into the policy editor. Replace the `{{region}}` and `{{amzn-s3-demo-bucket}}` placeholders with your values.

1. Choose **Save changes**.

For more information about migrating from ACLs to bucket policies, see [Grant Amazon ElastiCache (Redis OSS) access to your S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-ownership-migrating-acls-prerequisites.html#object-ownership-elasticache-redis) in the *Amazon S3 User Guide*.

## Required IAM permissions for the caller
<a name="backups-exporting-caller-iam"></a>

To call the export operation, you must have permissions to call `elasticache:CopySnapshot` and to access the target Amazon S3 bucket. You can call this operation using the ElastiCache console, the AWS CLI, or the ElastiCache API `CopySnapshot` operation. These IAM permissions are separate from the Amazon S3 bucket policy that grants the ElastiCache service access to the bucket. For information about the bucket policy, see [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access).

The following IAM policy shows the minimum permissions that you need. Replace `{{amzn-s3-demo-bucket}}` with the name of your target Amazon S3 bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ElastiCacheCopySnapshot",
            "Effect": "Allow",
            "Action": "elasticache:CopySnapshot",
            "Resource": "*"
        },
        {
            "Sid": "S3BucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObject",
                "s3:ListBucket",
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
                "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
            ]
        },
        {
            "Sid": "S3GlobalAccess",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "arn:aws:s3:::*"
        }
    ]
}
```

**Important**  
The `s3:ListAllMyBuckets` action is an account-level operation. Its `Resource` element must be `"*"` or `"arn:aws:s3:::*"`. Scoping this action to a specific bucket ARN makes it ineffective and causes the error: "Elasticache was unable to validate the authenticated user has access on the S3 bucket." For more information, see [Amazon S3 actions related to accounts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html#using-with-s3-policy-actions-related-to-accounts) in the *Amazon S3 User Guide*.

## Export an ElastiCache backup
<a name="backups-exporting-procedures"></a>

Now you've created your S3 bucket and granted ElastiCache permissions to access it. Next, you can use the ElastiCache console, the AWS CLI, or the ElastiCache API to export your snapshot to it. 

### Exporting an ElastiCache backup (Console)
<a name="backups-exporting-CON"></a>

The following steps use the ElastiCache console to export a backup to an Amazon S3 bucket so that you can access it from outside ElastiCache. The Amazon S3 bucket must be in the same AWS Region as the ElastiCache backup.

**To export an ElastiCache backup to an Amazon S3 bucket**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. To see a list of your backups, from the left navigation pane choose **Backups**.

1. From the list of backups, choose the box to the left of the name of the backup you want to export. 

1. Choose **Export**.

1. In **Export Backup**, do the following: 

   1. In **New backup name** box, type a name for your new backup.

      The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

      ElastiCache adds an instance identifier and `.rdb` to the value that you enter here. For example, if you enter `my-exported-backup`, ElastiCache creates `my-exported-backup-0001.rdb`.

   1. From the **Target S3 Location** list, choose the name of the Amazon S3 bucket that you want to copy your backup to (the bucket that you created in [Create an Amazon S3 bucket](#backups-exporting-create-s3-bucket)).

      The **Target S3 Location** must be an Amazon S3 bucket in the backup's AWS Region with the following permissions for the export process to succeed.
      + Object access – **Read** and **Write**.
      + Permissions access – **Read**.

      For more information, see [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access). 

   1. Choose **Copy**.

**Note**  
If your S3 bucket does not have the permissions needed for ElastiCache to export a backup to it, you receive one of the following error messages. Return to [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access) to add the permissions specified and retry exporting your backup.  
ElastiCache has not been granted READ permissions %s on the S3 Bucket.  
**Solution:** Add Read permissions on the bucket.
ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.  
**Solution:** Add Write permissions on the bucket.
ElastiCache has not been granted READ\_ACP permissions %s on the S3 Bucket.  
**Solution:** Add **Read** for Permissions access on the bucket.

If you want to copy your backup to another AWS Region, use Amazon S3 to copy it. For more information, see [Copying an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MakingaCopyofanObject.html) in the *Amazon Simple Storage Service User Guide*.

### Exporting an ElastiCache serverless backup (AWS CLI)
<a name="backups-exporting-CLI"></a>

**Exporting a backup of a serverless cache**

Export the backup to an Amazon S3 bucket using the `export-serverless-cache-snapshot` CLI operation with the following parameters:

**Parameters**
+ `--serverless-cache-snapshot-name` – Name of the backup to be copied.
+ `--s3-bucket-name` – Name of the Amazon S3 bucket where you want to export the backup. A copy of the backup is made in the specified bucket.

  The `--s3-bucket-name` must be an Amazon S3 bucket in the backup's AWS Region with the following permissions for the export process to succeed.
  + Object access – **Read** and **Write**.
  + Permissions access – **Read**.

The following operation copies a backup to my-s3-bucket.

For Linux, macOS, or Unix:

```
aws elasticache export-serverless-cache-snapshot \
    --serverless-cache-snapshot-name {{automatic.my-redis-2023-11-27}} \
    --s3-bucket-name {{my-s3-bucket}}
```

For Windows:

```
aws elasticache export-serverless-cache-snapshot ^
    --serverless-cache-snapshot-name {{automatic.my-redis-2023-11-27}} ^
    --s3-bucket-name {{my-s3-bucket}}
```

### Exporting a node-based ElastiCache cluster backup (AWS CLI)
<a name="backups-exporting-self-designed-CON"></a>

**Exporting a backup of a node-based cluster**

Export the backup to an Amazon S3 bucket using the `copy-snapshot` CLI operation with the following parameters:

**Parameters**
+ `--source-snapshot-name` – Name of the backup to be copied.
+ `--target-snapshot-name` – Name of the backup's copy.

  The name must be between 1 and 1,000 characters and able to be UTF-8 encoded.

  ElastiCache adds an instance identifier and `.rdb` to the value you enter here. For example, if you enter `my-exported-backup`, ElastiCache creates `my-exported-backup-0001.rdb`.
+ `--target-bucket` – Name of the Amazon S3 bucket where you want to export the backup. A copy of the backup is made in the specified bucket.

  The `--target-bucket` must be an Amazon S3 bucket in the backup's AWS Region with the following permissions for the export process to succeed.
  + Object access – **Read** and **Write**.
  + Permissions access – **Read**.

  For more information, see [Grant ElastiCache access to your Amazon S3 bucket](#backups-exporting-grant-access).

The following operation copies a backup to my-s3-bucket.

For Linux, macOS, or Unix:

```
aws elasticache copy-snapshot \
    --source-snapshot-name {{automatic.my-redis-primary-2016-06-27-03-15}} \
    --target-snapshot-name {{my-exported-backup}} \
    --target-bucket {{my-s3-bucket}}
```

For Windows:

```
aws elasticache copy-snapshot ^
    --source-snapshot-name {{automatic.my-redis-primary-2016-06-27-03-15}} ^
    --target-snapshot-name {{my-exported-backup}} ^
    --target-bucket {{my-s3-bucket}}
```