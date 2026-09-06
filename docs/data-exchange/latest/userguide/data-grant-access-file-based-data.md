

# Access an AWS Data Exchange data set containing file-based data
<a name="data-grant-access-file-based-data"></a>

The following topics describe the process of accessing a data set containing file-based data stored as files on AWS Data Exchange. To complete the process, use the AWS Data Exchange console.

After you successfully accept a data grant, you will have access to the data set include in it.

**To view the data sets, revisions, and assets**

1. Open your web browser and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. In the left side navigation pane, under **My data**, choose **Entitled data sets**.

1. Choose a data set.

1. View the **Data set overview**, **Auto-export destinations** (Amazon S3 data sets only), the **Revisions**, and the **Description** of the data set.

## (Optional) Exporting data
<a name="data-grant-access-file-based-data-exporting"></a>

After your data grant is active, you can set up your Amazon S3 bucket to receive assets that you export. You can export the associated assets to Amazon S3 or you can use jobs with a signed URL.

If you want to export or download your data at a later time, including getting new revisions, see [Exporting assets from AWS Data Exchange](exporting-assets.md).

**Important**  
We recommend that you consider Amazon S3 security features when exporting data to Amazon S3. For more information about general guidelines and best practices, see [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) in the *Amazon Simple Storage Service User Guide*.  
For more information about how to export data, see [Exporting assets from AWS Data Exchange](exporting-assets.md) and [Exporting revisions from AWS Data Exchange](exporting-revisions.md).