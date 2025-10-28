# Restoring an archived object

Amazon S3 objects in the following storage classes or tiers are archived and are not
accessible in real time:

- The S3 Glacier Flexible Retrieval storage class
- The S3 Glacier Deep Archive storage class
- The S3 Intelligent-Tiering Archive Access tier
- The S3 Intelligent-Tiering Deep Archive Access tier
  Amazon S3 objects that are stored in the S3 Glacier Flexible Retrieval or
  S3 Glacier Deep Archive storage classes are not immediately accessible. To
  access an object in these storage classes, you must restore a temporary copy of the
  object to its S3 bucket for a specified duration (number of days). If you want a
  permanent copy of the object, restore the object, and then create a copy of it in your
  Amazon S3 bucket. Copying restored objects isn't supported in the Amazon S3 console.
  For this type of copy operation, use the
  AWS Command Line Interface (AWS CLI), the AWS SDKs, or the REST API. Unless you make a copy and change
  its storage class, the object will still be stored in the S3 Glacier Flexible Retrieval or
  S3 Glacier Deep Archive storage classes. For information about using these
  storage classes, see [Storage classes for rarely accessed objects](storage-class-intro.md#sc-glacier "storage-class-intro.md#sc-glacier").

To access objects in the S3 Intelligent-Tiering Archive Access and Deep Archive Access
tiers, you must initiate a restore request and wait until the object is moved into the
Frequent Access tier. When you restore an object from the Archive Access tier or
Deep Archive Access tier, the object moves back into the Frequent Access tier. For information
about using these storage classes, see [Storage class for automatically optimizing data with
changing or unknown access patterns](storage-class-intro.md#sc-dynamic-data-access "storage-class-intro.md#sc-dynamic-data-access").

For general information about archived objects, see [Working with archived objects](archived-objects.md "archived-objects.md").

###### Note

- When you restore an archived object from the S3 Glacier Flexible Retrieval or
  S3 Glacier Deep Archive storage classes, you pay for both the archived
  object and the copy that you restored temporarily.
- When you restore an object from S3 Intelligent-Tiering, there are no retrieval
  charges for Standard or Bulk retrievals.
- Subsequent restore requests called on archived objects that have already been
  restored are billed as `GET` requests. For information about pricing, see
  [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Restoring an archived object

You can restore an archived object by using the Amazon S3 console, the Amazon S3
REST API, the AWS SDKs, the AWS Command Line Interface (AWS CLI), or S3 Batch Operations.

###### Restore objects using the Amazon S3 console

Use the following procedure to Restore an object that has been archived to the
S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive storage classes, or the
S3 Intelligent-Tiering Archive Access or Deep Archive Access storage tiers.

###### To restore an archived object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that
   contains the objects that you want to restore.
4. In the **Objects** list, select the object or objects that you want
   to restore, choose **Actions**, and then choose **Initiate
   restore**.
5. If you're restoring from S3 Glacier Flexible Retrieval or
   S3 Glacier Deep Archive, enter the number of days that you want your archived
   data to be accessible in the **Number of days that the restored copy is
   available** box.
6. For **Retrieval tier**, do one of the following:
   - Choose **Bulk retrieval** or **Standard
     retrieval**, and then choose **Initiate restore**.
   - Choose **Expedited retrieval** (available only for
     S3 Glacier Flexible Retrieval or S3 Intelligent-Tiering Archive Access). If you're restoring an object
     in S3 Glacier Flexible Retrieval, you can choose whether to buy provisioned capacity
     for your Expedited retrieval. If you want to purchase provisioned capacity, proceed
     to the next step. If you don't, choose **Initiate restore**.

###### Note

Objects from the S3 Intelligent-Tiering Archive Access and Deep Archive Access tiers are
automatically restored to the Frequent Access tier. 7. (Optional) If you're restoring an object in S3 Glacier Flexible Retrieval and you chose
**Expedited retrieval**, you can choose whether to buy provisioned
capacity. Provisioned capacity is available only for objects in
S3 Glacier Flexible Retrieval. If you already have provisioned capacity, choose
**Initiate restore** to start a provisioned retrieval.

If you have provisioned capacity, all of your Expedited retrievals are served by
your provisioned capacity. For more information, see [Provisioned capacity](restoring-objects-retrieval-options.md#restoring-objects-expedited-capacity "restoring-objects-retrieval-options.md#restoring-objects-expedited-capacity").

    * If you don't have provisioned capacity and you don't want to buy it, choose
     **Initiate restore**.
    * If you don't have provisioned capacity, but you want to buy provisioned capacity
     units (PCUs), choose **Purchase PCUs**. In the **Purchase
     PCUs** dialog box, choose how many PCUs you want to buy, confirm your
     purchase, and then choose **Purchase PCUs**. When you get the
     **Purchase succeeded** message, choose **Initiate
     restore** to start provisioned retrieval.

###### Restore objects from S3 Glacier Flexible Retrieval or

S3 Glacier Deep Archive

The following example uses the `restore-object` command to restore the
object `dir1/example.obj` in the bucket
`amzn-s3-demo-bucket` for 25 days.

```
aws s3api restore-object --bucket `amzn-s3-demo-bucket` --key `dir1/example.obj` --restore-request '{"Days":25,"GlacierJobParameters":{"Tier":"Standard"}}'
```

If the JSON syntax used in the example results in an error on a Windows client, replace
the restore request with the following syntax:

```
--restore-request Days=25,GlacierJobParameters={"Tier"="Standard"}
```

###### Restore objects from S3 Intelligent-Tiering Archive Access and

Deep Archive Access

The following example uses the `restore-object` command to restore the
object `dir1/example.obj` in the bucket
`amzn-s3-demo-bucket` to the Frequent Access tier.

```
aws s3api restore-object --bucket `amzn-s3-demo-bucket` --key `dir1/example.obj` --restore-request '{}'
```

###### Note

Unlike in the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes, restore
requests for S3 Intelligent-Tiering objects don't accept the `Days`
value.

###### Monitor restore status

To monitor the status of your `restore-object` request, use the following
`head-object` command:

```
aws s3api head-object --bucket `amzn-s3-demo-bucket` --key `dir1/example.obj`
```

For more information, see [restore-object](../../../cli/latest/reference/s3api/restore-object.md "../../../cli/latest/reference/s3api/restore-object.md") in the _AWS CLI Command Reference_.

Amazon S3 provides an API operation for you to initiate the restoration of an archived
object. For more information, see [RestoreObject](../API/RESTObjectPOSTrestore.md "../API/RESTObjectPOSTrestore.md") in the _Amazon Simple Storage Service API Reference_.

For examples of how to restore archived objects in S3 Glacier Flexible Retrieval or
S3 Glacier Deep Archive with the AWS SDKs, see [Code examples](../API/s3_example_s3_RestoreObject_section.md "../API/s3_example_s3_RestoreObject_section.md") in the _Amazon S3 API Reference_.

To restore more than one archived object with a single request, you can use
S3 Batch Operations.
You provide S3 Batch Operations with a list of objects to operate on. S3 Batch Operations calls the
respective API operation to perform the specified operation. A single Batch Operations job can perform the
specified operation on billions of objects containing exabytes of data.

To create a Batch Operations job, you must have a manifest that contains only the objects that
you want to restore. You can create a manifest by using S3 Inventory, or you can supply a
CSV file with the necessary information. For more information, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").

Before creating and running S3 Batch Operations jobs, you must grant permissions to Amazon S3 to
perform S3 Batch Operations on your behalf. For the required permissions, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").

###### Note

Batch Operations jobs can operate either on S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive
storage class objects _or_ on S3 Intelligent-Tiering
Archive Access and Deep Archive Access storage tier objects. Batch Operations can't operate on
both types of archived objects in the same job. To restore objects of both types, you
_must_ create separate Batch Operations jobs.

For more information about using Batch Operations to restore archive objects, see [Restore objects with Batch Operations](batch-ops-initiate-restore-object.md "batch-ops-initiate-restore-object.md").

###### To create an S3 Initiate Restore Object Batch Operations job

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Batch Operations**.
3. Choose **Create job**.
4. For **AWS Region**, choose the Region where you want to create
   your job.
5. Under **Manifest format**, choose the type of manifest to
   use.
   - If you choose **S3 inventory report**, enter the path to the
     `manifest.json` object that Amazon S3 generated as part of the
     CSV-formatted inventory report. If you want to use a manifest version other than the
     most recent, enter the version ID for the `manifest.json`
     object.
   - If you choose **CSV**, enter the path to a CSV-formatted
     manifest object. The manifest object must follow the format described in the
     console. If you want to use a version other than the most recent, you can optionally
     include the version ID for the manifest object.

6. Choose **Next**.
7. In the **Operation** section, choose
   **Restore**.
8. In the **Restore** section, for **Restore
   source**, choose either **Glacier Flexible Retrieval or Glacier Deep
   Archive** or **Intelligent-Tiering Archive Access tier or Deep
   Archive Access tier**.

If you chose **Glacier Flexible Retrieval or Glacier Deep
Archive**, enter a number for **Number of days that the restored copy
is available**.

For **Retrieval tier**, choose the tier that you want to
use. 9. Choose **Next**. 10. On the **Configure additional options** page, fill out the
following sections:

    * In the **Additional options** section, provide a description
     for the job and specify a priority number for the job. Higher numbers indicate a
     higher priority. For more information, see [Assigning job priority](batch-ops-job-priority.md "batch-ops-job-priority.md").
    * In the **Completion report** section, select whether Batch Operations
     should create a completion report. For more information about completion reports,
     see [Completion reports](batch-ops-job-status.md#batch-ops-completion-report "batch-ops-job-status.md#batch-ops-completion-report").
    * In the **Permissions** section, you must grant permissions to
     Amazon S3 to perform Batch Operations on your behalf. For the required permissions, see [Granting permissions for Batch Operations](batch-ops-iam-role-policies.md "batch-ops-iam-role-policies.md").
    * (Optional) In the **Job tags** section, add tags in key-value
     pairs. For more information, see [Controlling access and labeling jobs using tags](batch-ops-job-tags.md "batch-ops-job-tags.md").

When you're finished, choose **Next**. 11. On the **Review** page, verify the settings. If you need to make
changes, choose **Previous**. Otherwise, choose **Create
job**.
For more information about Batch Operations, see [Restore objects with Batch Operations](batch-ops-initiate-restore-object.md "batch-ops-initiate-restore-object.md") and [Creating an S3 Batch Operations job](batch-ops-create-job.md "batch-ops-create-job.md").

## Checking the restore status and

expiration date

You can check the status of a restore request or the expiration date by using the Amazon S3
console, Amazon S3 Event Notifications, the AWS CLI, or the Amazon S3 REST API.

###### Note

Objects restored from the S3 Glacier Flexible Retrieval and S3 Glacier Deep Archive storage classes are
stored only for the number of days that you specify. The following procedures
return the expiration date for these copies.

Objects restored from the S3 Intelligent-Tiering Archive Access and Deep Archive Access storage
tiers don't have expiration dates and instead are moved back to the
Frequent Access tier.

###### To check an object's restore status and expiration date in the Amazon S3 console

1.  Open the Amazon S3 console at
    [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2.  In the left navigation pane, choose **General purpose buckets**.
3.  In the buckets list, choose the name of the bucket that contains
    the object that you are restoring.
4.  In the **Objects** list, select the object that you are restoring.
    The object's details page appears.

        * If the restoration isn't finished, at the top of the page, you see a section that
         says **Restoration in progress**.
        * If the restoration is finished, at the top of the page, you see a section that
         says **Restoration complete**. If you're restoring from
         S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive, this section also
         displays the **Restoration expiry date**. Amazon S3 will remove the
         restored copy of your archived object on this date.

    You can be notified of object restoration completion by using the
    `s3:ObjectRestore:Completed` action with the Amazon S3 Event
    Notifications feature. For more information about enabling event
    notifications, see [Enabling notifications by using Amazon SQS, Amazon SNS, and AWS Lambda](how-to-enable-disable-notification-intro.md "how-to-enable-disable-notification-intro.md"). For
    more information about the various `ObjectRestore` event types,
    see [Supported event types for SQS,
    SNS, and Lambda](notification-how-to-event-types-and-destinations.md#supported-notification-event-types "notification-how-to-event-types-and-destinations.md#supported-notification-event-types").

###### Check an object's restore status and expiration date with the AWS CLI

The following example uses the `head-object` command to view metadata
for the object `dir1/example.obj` in
the bucket `amzn-s3-demo-bucket`. When you run this command
on an object being restored Amazon S3 returns if the
restore is ongoing and (if applicable) the expiration date.

```
aws s3api head-object --bucket `amzn-s3-demo-bucket` --key `dir1/example.obj`
```

Expected output (restore ongoing):

```
{
    "Restore": "ongoing-request=\"true\"",
    "LastModified": "2020-06-16T21:55:22+00:00",
    "ContentLength": 405,
    "ETag": "\"b662d79adeb7c8d787ea7eafb9ef6207\"",
    "VersionId": "wbYaE2vtOV0iIBXrOqGAJt3fP1cHB8Wi",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "AES256",
    "Metadata": {},
    "StorageClass": "GLACIER"
}
```

Expected output (restore finished):

```
{
    "Restore": "ongoing-request=\"false\", expiry-date=\"Wed, 12 Aug 2020 00:00:00 GMT\"",
    "LastModified": "2020-06-16T21:55:22+00:00",
    "ContentLength": 405,
    "ETag": "\"b662d79adeb7c8d787ea7eafb9ef6207\"",
    "VersionId": "wbYaE2vtOV0iIBXrOqGAJt3fP1cHB8Wi",
    "ContentType": "binary/octet-stream",
    "ServerSideEncryption": "AES256",
    "Metadata": {},
    "StorageClass": "GLACIER"
}
```

For more information about `head-object`, see [head-object](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/head-object.html") in the _AWS CLI Command
Reference_.

Amazon S3 provides an API operation for you to retrieve object metadata. To check the restoration status and expiration date of an
archived object using the REST API, see [HeadObject](../API/API_HeadObject.md "../API/API_HeadObject.md") in the
_Amazon Simple Storage Service API Reference_.

## Upgrading the speed of an in-progress restore

You can upgrade the speed of your restoration while it is in progress.

###### To upgrade an in-progress restore to a faster tier

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **Buckets** list, choose the name of the bucket that
   contains the objects that you want to restore.
4. In the **Objects** list, select the object that you are
   restoring. The object's details page appears. On the object's details page,
   choose **Upgrade retrieval tier**. For information about
   checking the restoration status of an object, see [Checking the restore status and
   expiration date](#restore-archived-objects-status "#restore-archived-objects-status").
5. Choose the tier that you want to upgrade to, and then choose
   **Initiate restore**.
