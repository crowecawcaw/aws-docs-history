

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# Audit Manager download center
<a name="download-center"></a>



The download center is where you can find and manage all of your downloadable Audit Manager files. When you generate an assessment report or export search results from evidence finder, the files appear in the download center. 

**Contents**
+ [Browsing the download center](#browse-download-center)
+ [Downloading a file](#download-a-file)
+ [Deleting a file](#delete-assessment-report-steps)
+ [Additional resources](#download-center-additional-resources)

## Browsing the download center
<a name="browse-download-center"></a>

Follow these steps to browse your files in the download center.

**To find files in the download center**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Download center**.

1. Choose the **Assessment reports** tab to view the assessment reports that are available to download.
   + This tab shows the assessment reports that you've generated. Assessment reports remain available in the download center until you delete them. 
   + To see the latest status of your assessment report, choose the refresh icon (⟳) to reload the table. Each row in the assessment reports table shows the name of the report, its creation date, and one of the following statuses:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html)

1. Choose the **Exports** tab to view the CSV exports that are available to download.
   + This tab shows the evidence finder search results that you exported in the last seven days. CSV files are removed from the download center after seven days, but they remain available in your [export destination](https://docs.aws.amazon.com/audit-manager/latest/userguide/settings-export-destination.html) S3 bucket. For instructions on how to find an evidence finder CSV export in your S3 destination bucket, see [Viewing your results after you've exported them](exporting-search-results-from-evidence-finder.md#viewing-results-after-export).
   + To see the latest status of your CSV exports, choose the refresh icon (⟳) to reload the table. Each row in the exports table shows the file name, its export date, and one of the following statuses:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/audit-manager/latest/userguide/download-center.html)
**Note**  
Keep in mind that the exports tab might also display CSV files for queries that you ran directly in AWS CloudTrail Lake. This includes queries made in the CloudTrail console or using the CloudTrail API. CloudTrail exports appear on this tab if you queried the Audit Manager event data store, and you chose to save the results to Amazon S3.

## Downloading a file
<a name="download-a-file"></a>

Follow these steps to download a file from the download center.

**To download a file**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Download center**.

1. Choose either the **Assessment reports** tab or the **Exports** tab.

1. Select the file that you want to download, and choose **Download**.

For instructions on how to download a file directly from your S3 destination bucket, see [Downloading an object](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html) in the *Amazon Simple Storage Service (Amazon S3) User Guide*.

## Deleting a file
<a name="delete-assessment-report-steps"></a>

Follow these steps to delete any assessment reports that you no longer need in the download center.

**Note**  
Deleting CSV exports from the download center isn't currently supported. CSV exports are automatically removed from the download center after seven days.

**To delete an assessment report**

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home).

1. In the left navigation pane, choose **Download center**.

1. Choose the **Assessment reports** tab.

1. Select the assessment report that you want to delete, and choose **Delete**.

If you want to delete an assessment report or a CSV export from your S3 destination bucket, we recommend that you complete this task directly in Amazon S3. For instructions, see [Deleting Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html) in the *Amazon Simple Storage Service (Amazon S3) User Guide*.

## Additional resources
<a name="download-center-additional-resources"></a>
+ [Configuring your default export destination for evidence finder](settings-export-destination.md)
+ [Configuring your default assessment report destination](settings-destination.md)
+ [Troubleshooting assessment report issues](assessment-report-issues.md)
+ [ Troubleshooting CSV export issues](https://docs.aws.amazon.com/audit-manager/latest/userguide/evidence-finder-issues.html#csv-exports) 
+ [Downloading an object from Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html)
+ [Deleting Amazon S3 objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html)