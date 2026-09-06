

# Exporting AWS Data Exchange assets to an S3 bucket (AWS SDKs)
<a name="export-assets-s3-prog"></a>

You can use the AWS SDKs to export AWS Data Exchange assets to an S3 bucket using the following instructions.

**To export assets to an S3 bucket (AWS SDKs)**

1. Create a `CreateJob` request of type `EXPORT_ASSETS_TO_S3`.

1. Include the following in the request:
   + `AssetDestinations`
     + `AssetID`
     + `Bucket`
     + `Key`
   + `DataSetID`
   + `Encryption`
     + `KmsKeyArn`
     + `Type`
   + `RevisionID`

1. Start the `CreateJob` request with a `StartJob` operation that requires the `JobId` returned in step 1.

1. (Optional) Update the assets' name property after they are created.

**Note**  
For information about exporting an entire revision as a single job, see [Exporting revisions from AWS Data Exchange](exporting-revisions.md).