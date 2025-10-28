# Importing AWS Data Exchange assets from an S3 bucket

When you import assets from Amazon S3 to AWS Data Exchange, the AWS Identity and Access Management (IAM) permissions you use
must include the ability to write to the AWS Data Exchange service S3 buckets and to read from the S3
bucket where your assets are stored. You can import from any S3 bucket that you have
permission to access, regardless of ownership. For more information, see [Amazon S3 permissions](access-control.md#additional-s3-permissions "access-control.md#additional-s3-permissions").

You can import up to 100 assets in a single job.

###### Topics

- [Importing assets from an S3 bucket (AWS
  SDKs)](#import-assets-s3-prog "#import-assets-s3-prog")
- [Importing assets from an S3 bucket
  (console)](#import-assets-via-console "#import-assets-via-console")

## Importing assets from an S3 bucket (AWS

SDKs)

###### To import assets from an Amazon S3 bucket (AWS SDKs)

1. Create a `CreateJob` request of type
   `IMPORT_ASSETS_FROM_S3`.
2. Include the following in the request:
   - `AssetSources`
     - `Bucket`
     - `Key`

   - `DataSetID`
   - `RevisionID`

3. Start the `CreateJob` request with a `StartJob` operation
   that requires the `JobId` returned in step 1.
4. (Optional) Update the assets' name property after they are created.

## Importing assets from an S3 bucket

(console)

###### To import an asset from an S3 bucket (console)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, for **Publish data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose the data set that has the revision
   you want to update.
4. On the **Revisions** tab, choose **Create
   revision** to open the **Create revision** page.
   1. For **Revision settings**, provide an optional comment for
      your revision that describes the purpose of the revision.
   2. For **Add tags – optional**, add tags associated with the
      resource.
   3. Choose **Create**.

   Your new revision is created.

5. For the **Jobs** section, choose **Import from
   Amazon S3**.
6. Follow the prompts in the **Import from Amazon S3** window, and then
   choose **Import assets**.

A job is started to import your asset into your data set. After the job is
finished, the **State** field in the **Jobs** section
is updated to **Completed**.
