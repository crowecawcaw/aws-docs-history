# Exporting assets to a signed URL as a subscriber

(console)

As a subscriber to AWS Data Exchange data products, you can use the AWS Data Exchange console to export AWS Data Exchange
assets to destinations other than S3 buckets using the following instructions.

###### To export an asset to a signed URL as a subscriber (console)

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange "https://console.aws.amazon.com/dataexchange").
2. In the left side navigation pane, for **My subscriptions**,
   choose **Entitled data**.
3. In **Entitled data**, choose the product that has the revision
   you want to export.
4. In **Entitled data sets**, choose the data set.
5. On the **Revisions** tab, choose the revision.
6. From the **Assets** tab, select the check box next to the assets
   that you want to export.
7. Select **Export actions** and then choose **Download
   selected assets**.

A job is started to export your asset. After the job is finished, the
**State** field in the **Jobs** section is updated
to **Completed**.
