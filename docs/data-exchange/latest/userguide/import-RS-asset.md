# Importing AWS Data Exchange assets from an AWS Data Exchange datashare for

Amazon Redshift

When you import assets using AWS Data Exchange datashare for Amazon Redshift, you can begin querying,
analyzing, and operationalizing third-party Amazon Redshift tables after subscribing.

## Importing assets from an AWS Data Exchange datashare for Amazon Redshift

(AWS SDKs)

###### To import assets from an AWS Data Exchange datashare for Amazon Redshift (AWS SDKs)

1. Create a `CreateJob` request of type
   `IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES`.
2. Include the following in the request:
   - `AssetSources`
     - `DataShareArn`

   - `DataSetID`
   - `RevisionID`

3. Start the `CreateJob` request with a `StartJob` operation
   that requires the `JobId` returned in step 1.
4. (Optional) Poll the `GetJob` operation to wait for the job to
   complete.
5. (Optional) Update the assets' name property after they are created.

## Importing assets from an AWS Data Exchange datashare for

Amazon Redshift (console)

###### To import an asset from an ADE datashare (for Amazon Redshift console)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, for **Publish data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose the data set that has the asset
   you want to update.
4. On the **Revisions** tab, choose **Create
   revision** to open the **Create revision** page.
   1. For **Revision settings**, provide an optional comment for
      your revision that describes the purpose of the revision.
   2. For **Add tags – optional**, add tags associated with the
      resource.
   3. Choose **Create**.

   Your new revision is created.

5. For the **AWS Data Exchange datashares for Amazon Redshift** section, choose
   **Add datashares**.
6. On the **Add AWS Data Exchange datashare to revision** page, select the
   datashare or datashares that you want to add.
7. Choose **Add datashare(s)**.

A job is started to import your assets into your data set. After the job is
finished, the **State** field in the **Jobs** section
is updated to **Completed**.
