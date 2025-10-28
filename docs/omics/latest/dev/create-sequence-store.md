AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Creating a HealthOmics sequence store

HealthOmics sequence stores support storage of genomic files in the unaligned formats of `FASTQ` (gzip-only)
and `uBAM`. It also supports the aligned formats of `BAM` and `CRAM`.

Imported files are stored as read sets. You can add tags to read sets and use IAM policies to control access
to read sets. Aligned read sets require a reference genome to align genomic sequences, but it's optional for
unaligned read sets.

To store read sets, you first create a sequence store. When you create a sequence store, you can specify an
optional Amazon S3 bucket as a fallback location and the location where S3 access logs are stored. The fallback
location is used for storing any files that fail to create a read set during a direct upload. Fallback locations are
available for sequence stores created after May 15, 2023. You specify the fallback location when you create the
sequence store.

You can specify up to five read set tag keys. When you create or update a read set with a tag key that matches one of these keys,
the read set tags are propagated to the corresponding Amazon S3 object.
System tags created by HealthOmics are propagated by default.

###### Topics

- [Creating a sequence store using the console](#console-create-sequence-store "#console-create-sequence-store")
- [Creating a sequence store using the CLI](#api-create-sequence-store "#api-create-sequence-store")
- [Updating a sequence store](#update-sequence-store "#update-sequence-store")
- [Updating read set tags for a sequence store](#sequence-store-manage-tags "#sequence-store-manage-tags")
- [Importing genomic files](#import-genomic-files "#import-genomic-files")

## Creating a sequence store using the console

###### To create a sequence store

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Sequence stores**.
3. On the **Create sequence store** page, provide the
   following information
   - **Sequence store name** - A unique name for
     this store.
   - **Description** (optional) - A description of
     this sequence store.

4. For **Fallback location in S3**, specify an Amazon S3 location. HealthOmics uses the fallback
   location for storing any files that fail to create a read set during a direct upload.
   You need to grant the HealthOmics service write access to the Amazon S3 fallback location.
   For an example policy, see [Configure a fallback location](synchronous-uploads.md#synchronous-uploads-fallback "synchronous-uploads.md#synchronous-uploads-fallback").

Fallback locations aren't available for sequence stores created before May 16, 2023. 5. (Optional) For **Read set tag keys for S3 propagation**, you can enter up to five
read set keys to propagate from a read set to the underlying S3 Objects. By propagating tags from a read set
to the S3 object, you can grant S3 access permissions based on tags and/or end users to see the propagated
tags through the Amazon S3 getObjectTagging API operation.

    1. Enter one key value in the text box. The console creates a new text box to add the next key.
    2. (Optional) Choose **Remove** to remove all the keys.

6. Under **Data Encryption**, select whether you want
   data encryption to be owned and managed by AWS or to use a customer managed CMK.
7. (Optional) Under **S3 Data access**, select whether to create a new role and
   policy to access the sequence store through Amazon S3.
8. (Optional) For **S3 access logging**, select `Enabled` if you want Amazon S3
   to collect access log records.

For **Access logging location in S3**, specify an Amazon S3 location to store the logs. This
field is visible only if you enabled S3 access logging. 9. **Tags** (optional) - Provide up to 50 tags for this sequence store. These tags are
separate from read set tags that are set during read set import/tag update

After you create the store, it's ready for [Importing genomic files](#import-genomic-files "#import-genomic-files").

## Creating a sequence store using the CLI

In the following example, replace `sequence store name` with the
name you chose for your sequence store.

```
aws omics create-sequence-store --name ``sequence store name`` --fallback-location "s3://amzn-s3-demo-bucket"
```

You receive the following response in JSON, which includes the ID number for your
newly created sequence store.

```
{
    "id": "3936421177",
    "arn": "arn:aws:omics:us-west-2:111122223333:sequenceStore/3936421177",
    "name": "sequence_store_example_name",
    "creationTime": "2022-07-13T20:09:26.038Z"
    "fallbackLocation" : "s3://amzn-s3-demo-bucket"
}
```

You can also view all sequence stores associated with your account by using the
**list-sequence-stores** command, as shown in the following.

```
aws omics list-sequence-stores
```

You receive the following response.

```
{
    "sequenceStores": [
        {
            "arn": "arn:aws:omics:us-west-2:111122223333:sequenceStore/3936421177",
            "id": "3936421177",
            "name": "MySequenceStore",
            "creationTime": "2022-07-13T20:09:26.038Z",
            "updatedTime": "2024-09-13T04:11:31.242Z",
            "fallbackLocation" : "s3://amzn-s3-demo-bucket",
            "status": "Active"
        }
    ]
}
```

You can use **get-sequence-store** to learn more about a sequence store by using its ID, as
shown in the following example:

```
aws omics get-sequence-store --id ``sequence store ID``
```

You receive the following response:

```
{
  "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/sequencestoreID",
  "creationTime": "2024-01-12T04:45:29.857Z",
  "updatedTime": "2024-09-13T04:11:31.242Z",
  "description": null,
  "fallbackLocation": null,
  "id": "2015356892",
  "name": "MySequenceStore",
  "s3Access": {
      "s3AccessPointArn": "arn:aws:s3:us-west-2:123456789012:accesspoint/592761533288-2015356892",
      "s3Uri": "s3://592761533288-2015356892-ajdpi90jdas90a79fh9a8ja98jdfa9jf98-s3alias/592761533288/sequenceStore/2015356892/",
      "accessLogLocation": "s3://IAD-seq-store-log/2015356892/"
  },
  "sseConfig": {
      "keyArn": "arn:aws:kms:us-west-2:123456789012:key/eb2b30f5-635d-4b6d-b0f9-d3889fe0e648",
      "type": "KMS"
  },
  "status": "Active",
  "statusMessage": null,
  "setTagsToSync": ["withdrawn","protocol"],
}
```

After creation, several store parameters can also be updated. This can be done through the Console or
the API `updateSequenceStore` operation.

## Updating a sequence store

To update a sequence store, follow these steps:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Sequence stores**.
3. Choose the sequence store to update.
4. In the **Details** panel, choose **Edit**.
5. On the **Edit details** page, you can update the
   following fields:
   - **Sequence store name** - A unique name for
     this store.
   - **Description** - A description of
     this sequence store.
   - **Fallback location in S3**, specify an Amazon S3 location.
     HealthOmics uses the fallback location for storing any files that fail to create a read set during a direct upload.
   - **Read set tag keys for S3 propagation**
     you can enter up to five read set keys to propagate to Amazon S3.
   - (Optional) For **S3 access logging**, select `Enabled` if you want Amazon S3 to
     collect access log records.

   For **Access logging location in S3**, specify an Amazon S3 location to store the logs.
   This field is visible only if you enabled S3 access logging.
   - **Tags** (optional) - Provide up to 50 tags
     for this sequence store.

## Updating read set tags for a sequence store

To update read set tags or other fields for a sequence store, follow these steps:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Sequence stores**.
3. Choose the sequence store that you want to update.
4. Choose the **Details** tab.
5. Choose **Edit**.
6. Add new read set tags or delete existing tags, as required.
7. Update the name, description, fallback location, or S3 data access, as required.
8. Choose **Save changes**.

## Importing genomic files

To import genomic files to a sequence store, follow these steps:

###### To import a genomics file

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose
   choose **Sequence stores**.
3. On the **Sequence stores** page, choose the sequence
   store that you want to import your files into.
4. On the individual sequence store page, choose **Import
   genomic files**.
5. On the **Specify import details** page, provide the
   following information
   - **IAM role** - The IAM role that can access
     the genomic files on Amazon S3.
   - **Reference genome** - The reference genome
     for this genomics data.

6. On the **Specify import manifest** page, specify the
   following information **Manifest file**. The manifest
   file is a JSON or YAML file that describes essential information of your
   genomics data. For information about the manifest file, see [Importing read sets into a HealthOmics sequence store](import-sequence-store.md "import-sequence-store.md").
7. Click **Create import job**.
