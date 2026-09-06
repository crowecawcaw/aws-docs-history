

# Exporting AWS Data Exchange asset revisions to an S3 bucket as a subscriber (console)
<a name="export-rev-s3-console-sub"></a>

As a subscriber to AWS Data Exchange data products, you can use the AWS Data Exchange console to export AWS Data Exchange assets to an S3 bucket using the following instructions.

**To export a revision to an S3 bucket as a subscriber (console)**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, for **My subscriptions**, choose **Entitled data**.

1. In **Entitled data**, choose the product that has the revision you want to export.

1. In **Entitled data sets**, choose the data set.

1. On the **Revisions** tab, select the revision, and then choose **Export to Amazon S3**.

1. In **Export revision to Amazon S3**, select a destination option, Amazon S3 bucket folder destination, configure encryption options, and then choose **Export**.

   A job is started to export your revision. After the job is finished, the **State** field in the **Jobs** section is updated to **Completed**.