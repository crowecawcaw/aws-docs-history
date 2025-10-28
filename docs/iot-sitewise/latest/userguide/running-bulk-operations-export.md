# Run a bulk export job

Bulk export is the action of moving metadata from an AWS IoT SiteWise workspace to an Amazon S3 bucket.

When you perform a bulk export of your AWS IoT SiteWise content to Amazon S3, you can specify filters to limit which specific
asset models and assets you'd like to export.

The filters must be specified in an `iotSiteWiseConfiguration` section within the sources section
of your JSON request.

###### Note

You can include multiple filters in your request. The bulk operation will export asset models and assets
that match any of the filters.

If you don't provide any filters, the bulk operation exports all of your asset models and assets.

###### Example request body with filters

```

{
      "metadataTransferJobId": "your-transfer-job-id",
      "sources": [
       {
        "type": "iotsitewise",
        "iotSiteWiseConfiguration": {
          "filters": [
           {
              "filterByAssetModel": {
                  "assetModelId": "asset model ID"
              }
            },
            {
              "filterByAssetModel": {
                  "assetModelId": "asset model ID",
                  "includeAssets": true
              }
            },
            {
              "filterByAssetModel": {
                  "assetModelId": "asset model ID",
                  "includeOffspring": true
               }
             }
           ]
          }
        }
       ],
       "destination": {
          "type": "s3",
          "s3Configuration": {
            "location": "arn:aws:s3:::amzn-s3-demo-bucket"
          }
      }
}

```

## Export metadata (console)

The following procedure explains the console export action:

###### Create an export job in the AWS IoT SiteWise console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. Choose **Bulk operations New** from the navigation pane.
3. Choose **New export** to start the export process.
4. On the **Export metadata** page:
   - Enter a name for the export job. This is the name used for the exported file in your Amazon S3 bucket.
   - Choose your resources to export, which sets the filters for the job:
     - Export all assets and asset models. Use filters on assets and asset models.
     - Export assets. Filter on your assets.
       - Select the asset to use for the export filter.
       - (Optional) Add the offspring or the associated asset model.

     - Export asset models. Filter on your asset models.
       - Select the asset model to use for the export filter.
       - (Optional) Add the offspring, or the associated asset or both.

     - Choose **Next**.

   - Navigate to the Amazon S3 bucket:
     - Choose **Browse Amazon S3** to view the Amazon S3 bucket and files.
     - Navigate to the Amazon S3 bucket where the file must be placed.
     - Choose **Next**.

   - Review the export job and choose **Export**.

5. The **Bulk operations on SiteWise metadata** page of the AWS IoT SiteWise console displays the newly
   created import job in the **Jobs progress** table.

For the different ways to use filters when exporting metadata, see [Export metadata examples](bulk-operations-export-filter-examples.md "bulk-operations-export-filter-examples.md").

## Export metadata (AWS CLI)

The following procedure explains the AWS CLI export action:

###### Export data from AWS IoT SiteWise to Amazon S3

1. Create a JSON file with your request body. The request body specifies the source and destination for the
   transfer job. The following example shows an example request body:

```

{
    "metadataTransferJobId": "`your-transfer-job-Id`",
    "sources": [{
        "type": "iotsitewise"
    }],
    "destination": {
        "type": "s3",
        "s3Configuration": {
            "location": "arn:aws:s3:::`amzn-s3-demo-bucket`"
        }
    }
}
```

Make sure to specify your Amazon S3 bucket as the destination of the metadata transfer job.

###### Note

This example will export all of your asset models and assets. To limit the export to specific asset
models or assets, you can include filters in your request body. For more information about applying export
filters, see [Export metadata examples](bulk-operations-export-filter-examples.md "bulk-operations-export-filter-examples.md"). 2. Save your request body file to use in the next step. In this example, the file is named
`createMetadataTransferJobExport.json`. 3. Invoke the `CreateMetadataTransferJob` by running the following AWS CLI command:

```

aws iottwinmaker create-metadata-transfer-job --region us-east-1 \
         --cli-input-json file://createMetadataTransferJobExport.json

```

Replace the input JSON file `createMetadataTransferJobExport.json` with your own
transfer file name.
