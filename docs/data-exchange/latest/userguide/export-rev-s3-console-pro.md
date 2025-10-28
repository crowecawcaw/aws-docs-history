# Exporting AWS Data Exchange asset revisions to an S3 bucket

as a provider (console)

As a provider of AWS Data Exchange data products, you can use the AWS Data Exchange console to export AWS Data Exchange
assets to an S3 bucket using the following instructions.

###### To export a revision to an S3 bucket as a provider (console)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, for **Publish data**, choose
   **Owned data sets**.
3. In **Owned data sets**, choose the product that has the revision
   you want to export.
4. Navigate to the **Products** tab to make sure that the data set is
   associated with a published product.
5. On the **Revisions** tab, choose the revision.
6. For the **Imported assets** section, select the check box next to
   the asset name.
7. Select **Export actions** and then choose **Export selected
   assets to Amazon S3**.
8. Follow the prompts in the **Export to Amazon S3** window and then choose
   **Export**.

A job is started to export your asset. After the job is finished, the
**State** field in the **Jobs** section is updated to
**Completed**.
