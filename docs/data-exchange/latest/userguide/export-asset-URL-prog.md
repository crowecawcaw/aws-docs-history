# Exporting AWS Data Exchange assets to a signed URL (AWS

SDKs)

You can use the AWS SDKs to export AWS Data Exchange assets to destinations other than S3
buckets.

###### To export assets to a signed URL (AWS SDKs)

1. Create a `CreateJob` request of type
   `EXPORT_ASSET_TO_SIGNED_URL`.
2. Include the following in the request:
   - `AssetID`
   - `DataSetID`
   - `RevisionID`

3. Start the `CreateJob` request with a `StartJob` operation
   that requires the `JobId` returned in step 1.
4. (Optional) Update the assets' name property after they are created.
5. The response details include the `SignedUrl` that you can use to import
   your file.

###### Note

The signed URL expires one
minute
after it's created.
