# Run a bulk import job

Bulk import is the action of moving metadata into an AWS IoT SiteWise workspace. For example, bulk import can move
metadata from a local file, or a file in an Amazon S3 bucket, to an AWS IoT SiteWise workspace.

## Step 1: Prepare the file to import

Download the AWS IoT SiteWise native format file to import assets and the asset models. See [AWS IoT SiteWise metadata transfer job schema](bulk-operations-schema.md "bulk-operations-schema.md") for more details.

## Step 2: Upload the prepared file to Amazon S3

Upload the file to Amazon S3. See [Uploading a file to Amazon S3](../../../AmazonS3/latest/userguide/GetStartedWithS3.md#uploading-an-object-bucket "../../../AmazonS3/latest/userguide/GetStartedWithS3.md#uploading-an-object-bucket") in the
_Amazon Simple Storage Service User Guide_ for details.

## Import metadata (console)

You can use the AWS IoT SiteWise console to bulk import metadata. Follow [Step 1: Prepare the file to import](#preparing-import-file "#preparing-import-file") and [Step 2: Upload the prepared file to Amazon S3](#uploading-import-file "#uploading-import-file") to prepare a file that is ready to be imported.

###### Import data from Amazon S3 to AWS IoT SiteWise console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. Choose **Bulk operations New** from the navigation pane.
3. Choose **New import** to start the import process.
4. On the **Import metadata** page:
   - Choose **Browse Amazon S3** to view the Amazon S3 bucket and files.
   - Navigate to the Amazon S3 bucket that contains the prepared import file.
   - Select the file to import.
   - Review the selected file, and choose **Import**.

5. The **Bulk operations on SiteWise metadata** page of the AWS IoT SiteWise console displays the newly
   created import job in the **Jobs progress** table.

## Import metadata (AWS CLI)

To perform an import action, use the following procedure:

###### Import data from Amazon S3 to AWS CLI

1. Create a metadata file that specifies the resources you want to import, following the [AWS IoT SiteWise metadata transfer job schema](bulk-operations-schema.md "bulk-operations-schema.md"). Store this file in your Amazon S3
   bucket.

For examples of metadata files to import, see [Import metadata examples](bulk-operations-import-metadata-example.md "bulk-operations-import-metadata-example.md"). 2. Now create a JSON file with the request body. The request body specifies the source and destination for
the transfer job. This file is separate from the file from the previous step. Make sure to specify your Amazon S3
bucket as a source and `iotsitewise` as the destination.

The following example shows the request body:

```
{
      "metadataTransferJobId": "`your-transfer-job-Id`",
      "sources": [{
          "type": "s3",
          "s3Configuration": {
              "location": "arn:aws:s3:::`amzn-s3-demo-bucket`/your_import_metadata.json"
          }
      }],
      "destination": {
          "type": "iotsitewise"
      }
  }
```

3. Invoke the `CreateMetadataTransferJob` by running the following AWS CLI command. In this
   example, the request body file from the previous step is named
   `createMetadataTransferJobExport.json`.

```
aws iottwinmaker create-metadata-transfer-job --region us-east-1 \
  --cli-input-json file://createMetadataTransferJobImport.json
```

This will create a metadata transfer job, and begin the process of the transferring your selected
resources.
