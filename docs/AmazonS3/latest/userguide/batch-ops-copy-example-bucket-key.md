# Using Batch Operations to enable S3 Bucket Keys for

SSE-KMS

S3 Bucket Keys reduce the cost of server-side encryption with AWS Key Management Service (AWS KMS) (SSE-KMS) by
decreasing request traffic from Amazon S3 to AWS KMS. For more information, see [Reducing the cost of SSE-KMS with Amazon S3 Bucket Keys](bucket-key.md "bucket-key.md") and [Configuring your bucket to use an S3 Bucket Key with
SSE-KMS for new objects](configuring-bucket-key.md "configuring-bucket-key.md"). When you perform a
`CopyObject` operation by using the REST API, AWS SDKs, or AWS CLI, you can enable
or disable an S3 Bucket Key at the object level by adding the
`x-amz-server-side-encryption-bucket-key-enabled` request header with a
`true` or `false` value.

When you configure an S3 Bucket Key for an object by using a `CopyObject`
operation, Amazon S3 updates only the settings for that object. The S3 Bucket Key settings for the
destination bucket don't change. If you submit a `CopyObject` request for an AWS KMS
encrypted object to a bucket that has S3 Bucket Keys enabled, your object level operation will
automatically use S3 Bucket Keys unless you disable the keys in the request header. If you don't
specify an S3 Bucket Key for your object, Amazon S3 applies the S3 Bucket Key settings for the
destination bucket to the object.

To encrypt your existing Amazon S3 objects, you can use S3 Batch Operations. You can use the
Batch Operations **Copy** operation to copy existing unencrypted objects and write
them back to the same bucket as encrypted objects. For more information, see [Encrypting objects with Amazon S3
Batch Operations](https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/ "https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/") on the AWS Storage Blog.

In the following example, you use the Batch Operations **Copy** operation to
enable S3 Bucket Keys on existing objects. For more information, see [Configuring an S3 Bucket Key at the object
level](configuring-bucket-key-object.md "configuring-bucket-key-object.md").

###### Topics

- [Considerations for using S3 Batch Operations to
  encrypt objects with S3 Bucket Keys enabled](#bucket-key-ex-things-to-note "#bucket-key-ex-things-to-note")
- [Prerequisites](#bucket-key-ex-prerequisites "#bucket-key-ex-prerequisites")
- [Step 1: Get your list of objects using Amazon S3
  Inventory](#bucket-key-ex-get-list-of-objects "#bucket-key-ex-get-list-of-objects")
- [Step 2: Filter your object
  list with S3 Select](#bucket-key-ex-filter-object-list-with-s3-select "#bucket-key-ex-filter-object-list-with-s3-select")
- [Step 3: Set up and run your S3 Batch Operations
  job](#bucket-key-ex-setup-and-run-job "#bucket-key-ex-setup-and-run-job")

## Considerations for using S3 Batch Operations to

encrypt objects with S3 Bucket Keys enabled

Consider the following issues when you use S3 Batch Operations to encrypt objects with S3 Bucket Keys
enabled:

- You will be charged for S3 Batch Operations jobs, objects, and requests in addition to
  any charges associated with the operation that S3 Batch Operations performs on your behalf,
  including data transfers, requests, and other charges. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing "https://aws.amazon.com/s3/pricing").
- If you use a versioned bucket, each S3 Batch Operations job performed creates new
  encrypted versions of your objects. It also maintains the previous versions without an
  S3 Bucket Key configured. To delete the old versions, set up an S3 Lifecycle expiration
  policy for noncurrent versions as described in [Lifecycle configuration elements](intro-lifecycle-rules.md "intro-lifecycle-rules.md").
- The copy operation creates new objects with new creation dates, which can affect
  lifecycle actions like archiving. If you copy all objects in your bucket, all the new
  copies have identical or similar creation dates. To further identify
  these objects and create different lifecycle rules for various data subsets, consider
  using object tags.

## Prerequisites

Before you configure your objects to use an S3 Bucket Key, review [Changes to note before enabling an S3 Bucket Key](bucket-key.md#bucket-key-changes "bucket-key.md#bucket-key-changes").

To use this example, you must have an AWS account and at least one S3 bucket to hold
your working files and encrypted results. You might also find much of the existing
S3 Batch Operations documentation useful, including the following topics:

- [S3 Batch Operations basics](batch-ops.md#batch-ops-basics "batch-ops.md#batch-ops-basics")
- [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md")
- [Operations supported by S3 Batch Operations](batch-ops-operations.md "batch-ops-operations.md")
- [Managing S3 Batch Operations jobs](batch-ops-managing-jobs.md "batch-ops-managing-jobs.md")

## Step 1: Get your list of objects using Amazon S3

Inventory

To get started, identify the S3 bucket that contains the objects to encrypt, and get a
list of its contents. An Amazon S3 Inventory report is the most convenient and affordable way to do
this. The report provides the list of the objects in a bucket along with their associated
metadata. In this step, the source bucket is the inventoried bucket, and the destination
bucket is the bucket where you store the inventory report file. For more information about
Amazon S3 Inventory source and destination buckets, see [Cataloging and analyzing your data with S3 Inventory](storage-inventory.md "storage-inventory.md").

The easiest way to set up an inventory is by using the AWS Management Console. But you can also use the
REST API, AWS Command Line Interface (AWS CLI), or AWS SDKs. Before following these steps, be sure to sign in
to the console and open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"). If you encounter permission
denied errors, add a bucket policy to your destination bucket. For more information, see [Grant permissions for S3 Inventory
and S3 analytics](example-bucket-policies.md#example-bucket-policies-s3-inventory-1 "example-bucket-policies.md#example-bucket-policies-s3-inventory-1").

###### To get a list of objects using S3 Inventory

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**, and choose a bucket
   that contains objects to encrypt.
3. On the **Management** tab, navigate to the **Inventory
   configurations** section, and choose **Create inventory
   configuration**.
4. Give your new inventory a name, enter the name of the destination S3 bucket, and
   optionally create a destination prefix for Amazon S3 to assign objects in that bucket.
5. For **Output format**, choose **CSV**.
6. (Optional) In the **Additional fields – _optional_** section, choose **Encryption** and
   any other report fields that interest you. Set the frequency for report deliveries to
   **Daily** so that the first report is delivered to your bucket
   sooner.
7. Choose **Create** to save your configuration.

Amazon S3 can take up to 48 hours to deliver the first report, so check back when the first
report arrives. After you receive your first report, proceed to the next step to filter your
S3 Inventory report's contents. If you no longer want to receive inventory reports for this
bucket, delete your S3 Inventory configuration. Otherwise, Amazon S3 continues to deliver reports
on a daily or weekly schedule.

An inventory list isn't a single point-in-time view of all objects. Inventory lists are a
rolling snapshot of bucket items, which are eventually consistent (for example, the list might
not include recently added or deleted objects). Combining S3 Inventory and S3 Batch Operations works
best when you work with static objects, or with an object set that you created two or more
days ago. To work with more recent data, use the [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md")
(`GET` bucket) API operation to build your list of objects manually. If needed,
repeat the process for the next few days or until your inventory report shows the desired
status for all objects.

## Step 2: Filter your object

list with S3 Select

After you receive your S3 Inventory report, you can filter the report’s contents to list
only the objects that aren't encrypted with S3 Bucket Keys enabled. If you want all your bucket’s
objects encrypted with S3 Bucket Keys enabled, you can ignore this step. However, filtering your S3
Inventory report at this stage saves you the time and expense of re-encrypting objects that
you previously encrypted with S3 Bucket Keys enabled.

Although the following steps show how to filter by using [Amazon S3 Select](https://aws.amazon.com/blogs/aws/s3-glacier-select/ "https://aws.amazon.com/blogs/aws/s3-glacier-select/"), you can also use [Amazon Athena](https://aws.amazon.com/athena "https://aws.amazon.com/athena"). To decide which tool to use, look at your
S3 Inventory report’s `manifest.json` file. This file lists the number of
data files that are associated with that report. If the number is large, use Amazon Athena because
it runs across multiple S3 objects, whereas S3 Select works on one object at a time. For more
information about using Amazon S3 and Athena together, see [Querying Amazon S3 Inventory with Amazon Athena](storage-inventory-athena-query.md "storage-inventory-athena-query.md")
and "Using Athena" in the AWS Storage Blog post [Encrypting objects with
Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations "https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations").

###### To filter your S3 Inventory report by using S3 Select

1. Open the `manifest.json` file from your inventory report and look
   at the `fileSchema` section of the JSON. This informs the query that you run on
   the data.

The following JSON is an example `manifest.json` file for a
CSV-formatted inventory on a bucket with versioning enabled. Depending on how you
configured your inventory report, your manifest might look different.

```
  {
    "sourceBucket": "batchoperationsdemo",
    "destinationBucket": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`",
    "version": "2021-05-22",
    "creationTimestamp": "1558656000000",
    "fileFormat": "CSV",
    "fileSchema": "Bucket, Key, VersionId, IsLatest, IsDeleteMarker, BucketKeyStatus",
    "files": [
      {
        "key": "demoinv/batchoperationsdemo/DemoInventory/data/009a40e4-f053-4c16-8c75-6100f8892202.csv.gz",
        "size": 72691,
        "MD5checksum": "c24c831717a099f0ebe4a9d1c5d3935c"
      }
    ]
  }
```

If versioning isn't activated on the bucket, or if you choose to run the report for
the latest versions, the `fileSchema` is `Bucket`, `Key`,
and `BucketKeyStatus`.

If versioning _is_ activated, depending on how you
set up the inventory report, the `fileSchema` might include the following:
`Bucket`, `Key`, `VersionId`, `IsLatest`,
`IsDeleteMarker`, `BucketKeyStatus`. So pay attention to columns
1, 2, 3, and 6 when you run your query.

S3 Batch Operations needs the bucket, key, and version ID as inputs to perform the job, in
addition to the field to search by, which is `BucketKeyStatus`. You don't need
the `VersionID` field, but it helps to specify the `VersionID` field
when you operate on a versioned bucket. For more information, see [Working with objects in a
versioning-enabled bucket](manage-objects-versioned-bucket.md "manage-objects-versioned-bucket.md"). 2. Locate the data files for the inventory report. The `manifest.json`
object lists the data files under **files**. 3. After you locate and select the data file in the S3 console, choose
**Actions**, and then choose **Query with S3
Select**. 4. Keep the preset **CSV**, **Comma**,
and **GZIP** fields selected, and choose
**Next**. 5. To review your inventory report’s format before proceeding, choose **Show file
preview**. 6. Enter the columns to reference in the SQL expression field, and choose **Run
SQL**. The following expression returns columns 1–3 for all objects without an
S3 Bucket Key configured.

`select s._1, s._2, s._3 from s3object s where s._6 = 'DISABLED'`

The following are example results.

```
      batchoperationsdemo,0100059%7Ethumb.jpg,lsrtIxksLu0R0ZkYPL.LhgD5caTYn6vu
      batchoperationsdemo,0100074%7Ethumb.jpg,sd2M60g6Fdazoi6D5kNARIE7KzUibmHR
      batchoperationsdemo,0100075%7Ethumb.jpg,TLYESLnl1mXD5c4BwiOIinqFrktddkoL
      batchoperationsdemo,0200147%7Ethumb.jpg,amufzfMi_fEw0Rs99rxR_HrDFlE.l3Y0
      batchoperationsdemo,0301420%7Ethumb.jpg,9qGU2SEscL.C.c_sK89trmXYIwooABSh
      batchoperationsdemo,0401524%7Ethumb.jpg,ORnEWNuB1QhHrrYAGFsZhbyvEYJ3DUor
      batchoperationsdemo,200907200065HQ%7Ethumb.jpg,d8LgvIVjbDR5mUVwW6pu9ahTfReyn5V4
      batchoperationsdemo,200907200076HQ%7Ethumb.jpg,XUT25d7.gK40u_GmnupdaZg3BVx2jN40
      batchoperationsdemo,201103190002HQ%7Ethumb.jpg,z.2sVRh0myqVi0BuIrngWlsRPQdb7qOS
```

7. Download the results, save them into a CSV format, and upload them to Amazon S3 as your
   list of objects for the S3 Batch Operations job.
8. If you have multiple manifest files, run **Query with S3 Select** on
   those also. Depending on the size of the results, you could combine the lists and run a
   single S3 Batch Operations job or run each list as a separate job. To decide number of jobs to
   run, consider the [price](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/") of running each
   S3 Batch Operations job.

## Step 3: Set up and run your S3 Batch Operations

job

Now that you have your filtered CSV lists of S3 objects, you can begin the S3 Batch Operations
job to encrypt the objects with S3 Bucket Keys enabled.

A _job_ refers collectively to the list (manifest) of
objects provided, the operation performed, and the specified parameters. The easiest way to
encrypt this set of objects with S3 Bucket Keys enabled is by using the **Copy**
operation and specifying the same destination prefix as the objects listed in the manifest. In
an unversioned bucket, this operation overwrites the existing objects. In a bucket with
versioning turned on, this operation creates a newer, encrypted version of the objects.

As part of copying the objects, specify that Amazon S3 should encrypt the objects with SSE-KMS
encryption. This job copies the objects, so all of your objects will show an updated creation
date upon completion, regardless of when you originally added them to Amazon S3. Also specify the
other properties for your set of objects as part of the S3 Batch Operations job, including object
tags and storage class.

###### Substeps

- [Set up your IAM policy](#bucket-key-ex-set-up-iam-policy "#bucket-key-ex-set-up-iam-policy")
- [Set up your Batch Operations IAM role](#bucket-key-ex-set-up-iam-role "#bucket-key-ex-set-up-iam-role")
- [Enable S3 Bucket Keys for an
  existing bucket](#bucket-key-ex-enable-s3-bucket-key-on-a-bucket "#bucket-key-ex-enable-s3-bucket-key-on-a-bucket")
- [Create your Batch Operations job](#bucket-key-ex-create-job "#bucket-key-ex-create-job")
- [Run your Batch Operations job](#bucket-key-ex-run-job "#bucket-key-ex-run-job")

### Set up your IAM policy

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Policy**, and then choose
   **Create policy**.
3. Choose the **JSON** tab. Choose **Edit
   policy** and add the example IAM policy that appears in the following code
   block.

After copying the policy example into your [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), replace the
following:

    1. Replace ```amzn-s3-demo-source-bucket``` with
     the name of your source bucket to copy objects from.
    2. Replace ```amzn-s3-demo-destination-bucket```
     with the name of your destination bucket to copy objects to.
    3. Replace
     ``amzn-s3-demo-manifest-bucket`/`manifest-key``
     with the name of your manifest object.
    4. Replace
     ``amzn-s3-demo-completion-report-bucket`` with
     the name of the bucket where you want to save your completion reports.

JSON

```
 `{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CopyObjectsToEncrypt",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectTagging",
 "s3:PutObjectAcl",
 "s3:PutObjectVersionTagging",
 "s3:PutObjectVersionAcl",
 "s3:GetObject",
 "s3:GetObjectAcl",
 "s3:GetObjectTagging",
 "s3:GetObjectVersion",
 "s3:GetObjectVersionAcl",
 "s3:GetObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-source-bucket/*",
 "arn:aws:s3:::amzn-s3-demo-destination-bucket/*"
 ]
 },
 {
 "Sid": "ReadManifest",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": "arn:aws:s3:::``amzn-s3-demo-manifest-bucket`/`manifest-key``"
 },
 {
 "Sid": "WriteReport",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::`amzn-s3-demo-completion-report-bucket`/*"
 }
 ]
 }`

```

4. Choose **Next: Tags**.
5. Add any tags that you want (optional), and choose **Next:
   Review**.
6. Add a policy name, optionally add a description, and choose **Create
   policy**.
7. Choose **Review policy** and **Save
   changes**.
8. With your S3 Batch Operations policy now complete, the console returns you to the IAM
   **Policies** page. Filter on the policy name, choose the button to the
   left of the policy name, choose **Policy actions**, and choose
   **Attach**.

To attach the newly created policy to an IAM role, select the appropriate users,
groups, or roles in your account and choose **Attach policy**. This
takes you back to the IAM console.

### Set up your Batch Operations IAM role

1. On the [IAM Console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), in the navigation pane, choose **Roles**, and
   then choose **Create role**.
2. Choose **AWS service**, **S3**, and
   **S3 Batch Operations**. Then choose **Next:
   Permissions**.
3. Start entering the name of the IAM **policy** that you just
   created. Select the check box by the policy name when it appears, and choose **Next: Tags**.
4. (Optional) Add tags or keep the key and value fields blank for this exercise. Choose
   **Next: Review**.
5. Enter a role name, and accept the default description or add your own. Choose
   **Create role**.
6. Ensure that the user creating the job has the permissions in the following example.

Replace `account-id` with your AWS account
ID and `IAM-role-name` with the name that you plan
to apply to the IAM role that you will create in the Batch Operations job creation step
later. For more information, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").

```
            {
            "Sid": "AddIamPermissions",
            "Effect": "Allow",
            "Action": [
            "iam:GetRole",
            "iam:PassRole"
            ],
            "Resource": "arn:aws:iam::`account-id`:role/`IAM-role-name`"
            }
```

### Enable S3 Bucket Keys for an

existing bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the **Buckets** list, choose the bucket that you want to turn on
   an S3 Bucket Key for.
3. Choose **Properties**.
4. Under **Default encryption**, choose **Edit**.
5. Under **Encryption type**, you can choose between
   **Amazon S3 managed keys (SSE-S3)** and **AWS Key Management Service key
   (SSE-KMS)**.
6. If you chose **AWS Key Management Service key (SSE-KMS)**, under
   **AWS KMS key**, you can specify the AWS KMS key through one of the
   following options.
   - To choose from a list of available KMS keys, choose **Choose from your
     AWS KMS keys**. From the list of available keys, choose a symmetric encryption KMS key in the same Region as your bucket. Both the AWS managed key
     (`aws/s3`) and your customer managed keys appear in the list.
   - To enter the KMS key ARN, choose **Enter AWS KMS key ARN**, and
     then enter your KMS key ARN in the field that appears.
   - To create a new customer managed key in the AWS KMS console, choose **Create a
     KMS key**.

7. Under **Bucket Key**, choose **Enable**, and then
   choose **Save changes**.

Now that an S3 Bucket Key is enabled at the bucket level, objects that are uploaded,
modified, or copied into this bucket will inherit this encryption configuration by default.
This includes objects that are copied by using Amazon S3 Batch Operations.

### Create your Batch Operations job

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation pane, choose **Batch Operations**, and then choose
   **Create Job**.
3. Choose the **Region** where you store your objects, and choose **CSV** as the manifest type.
4. Enter the path or navigate to the CSV manifest file that you created earlier from S3
   Select (or Athena) results. If your manifest contains version IDs, select that box.
   Choose **Next**.
5. Choose the **Copy** operation, and choose the copy destination
   bucket. You can keep server-side encryption disabled. As long as the bucket destination
   has S3 Bucket Keys enabled, the copy operation applies S3 Bucket Keys at the destination
   bucket.
6. (Optional) Choose a storage class and the other parameters as desired. The
   parameters that you specify in this step apply to all operations performed on the
   objects that are listed in the manifest. Choose **Next**.
7. To configure server-side encryption, follow these steps:
   1. Under **Server-side encryption**, choose one of the
      following:
      - To keep the bucket settings for default server-side encryption of objects
        when storing them in Amazon S3, choose **Do not specify an encryption
        key**. As long as the bucket destination has S3 Bucket Keys enabled, the
        copy operation applies an S3 Bucket Key at the destination bucket.

      ###### Note

      If the bucket policy for the specified destination requires objects to be
      encrypted before storing them in Amazon S3, you must specify an encryption key.
      Otherwise, copying objects to the destination will fail.
      - To encrypt objects before storing them in Amazon S3, choose **Specify an
        encryption key**.

   2. Under **Encryption settings**, if you choose
      **Specify an encryption key**, you must choose either
      **Use destination bucket settings for default encryption** or
      **Override destination bucket settings for default
      encryption**.
   3. If you choose **Override destination bucket settings for default
      encryption**, you must configure the following encryption
      settings.
      1. Under **Encryption type**, you must choose either
         **Amazon S3 managed keys (SSE-S3)** or **AWS Key Management Service key
         (SSE-KMS)**. SSE-S3 uses one of the strongest block
         ciphers—256-bit Advanced Encryption Standard (AES-256) to encrypt each
         object. SSE-KMS provides you with more control over your key. For more
         information, see [Using server-side encryption with Amazon S3 managed keys
         (SSE-S3)](UsingServerSideEncryption.md "UsingServerSideEncryption.md") and [Using server-side encryption with AWS KMS keys
         (SSE-KMS)](UsingKMSEncryption.md "UsingKMSEncryption.md").
      2. If you choose **AWS Key Management Service key (SSE-KMS)**, under
         **AWS KMS key**, you can specify your AWS KMS key
         through one of the following options.
         - To choose from a list of available KMS keys, choose **Choose
           from your AWS KMS keys**, and then choose a symmetric encryption KMS key in the same Region as your bucket. Both the AWS managed key
           (`aws/s3`) and your customer managed keys appear in the list.
         - To enter the KMS key ARN, choose **Enter AWS KMS key
           ARN**, and enter your KMS key ARN in the field that
           appears.
         - To create a new customer managed key in the AWS KMS console, choose **Create
           a KMS key**.

      3. Under **Bucket Key**, choose **Enable**.
         The copy operation applies an S3 Bucket Key at the destination bucket.

8. Give your job a description (or keep the default), set its priority level, choose a
   report type, and specify the **Path to completion report
   destination**.
9. In the **Permissions** section, be sure to choose the Batch Operations
   IAM role that you defined earlier. Choose **Next**.
10. Under **Review**, verify the settings. If you want to make changes,
    choose **Previous**. After confirming the Batch Operations settings, choose
    **Create job**.

For more information, see [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md").

### Run your Batch Operations job

The setup wizard automatically returns you to the S3 Batch Operations section of the Amazon S3
console. Your new job transitions from the **New** state to the
**Preparing** state as S3 begins the process. During the Preparing state,
S3 reads the job’s manifest, checks it for errors, and calculates the number of
objects.

1. Choose the refresh button in the Amazon S3 console to check progress. Depending on the
   size of the manifest, reading can take minutes or hours.
2. After S3 finishes reading the job’s manifest, the job moves to the **Awaiting your confirmation** state. Choose the option button to
   the left of the Job ID, and choose **Run job**.
3. Check the settings for the job, and choose **Run job** in the
   bottom-right corner.

After the job begins running, you can choose the refresh button to check progress
through the console dashboard view or by selecting the specific job. 4. When the job is complete, you can view the **Successful** and
**Failed** object counts to confirm that everything performed as
expected. If you enabled job reports, check your job report for the exact cause of any
failed operations.

You can also perform these steps by using the AWS CLI, AWS SDKs, or Amazon S3 REST API.
For more information about tracking job status and completion reports, see [Tracking job status and completion reports](batch-ops-job-status.md "batch-ops-job-status.md").
