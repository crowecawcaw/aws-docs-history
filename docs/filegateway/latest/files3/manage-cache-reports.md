# View and manage cache reports for your

S3 File Gateway

Cache reports list files that are currently in the local cache for a specific file
share, according to filters and criteria that you specify. You can view a list of
existing cache reports for a specific file share, check report progress and status, and
delete reports you no longer need using the AWS Storage Gateway API or the Storage Gateway
console.

To manage cache reports using the API, see the following sections in the
_Storage Gateway API Reference_:

- [ListCacheReports](../../../storagegateway/latest/APIReference/API_ListCacheReports.md "../../../storagegateway/latest/APIReference/API_ListCacheReports.md")
- [DescribeCacheReport](../../../storagegateway/latest/APIReference/API_DescribeCacheReport.md "../../../storagegateway/latest/APIReference/API_DescribeCacheReport.md")
- [CancelCacheReport](../../../storagegateway/latest/APIReference/API_CancelCacheReport.md "../../../storagegateway/latest/APIReference/API_CancelCacheReport.md")
- [DeleteCacheReport](../../../storagegateway/latest/APIReference/API_DeleteCacheReport.md "../../../storagegateway/latest/APIReference/API_DeleteCacheReport.md")
  To manage cache reports in the Storage Gateway console, use the following procedure.

###### To manage cache reports using the Storage Gateway console

1.  Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/").
2.  In the navigation pane on the left side of the page, choose **File
    shares**, and then choose the file share for which you want to
    manage cache reports.
3.  On the **Details** page for the file share, choose the
    **Cache reports** tab. This tab lists the existing cache
    reports for the file share, and provides information about status, progress, and
    the object path where the report file is stored in Amazon S3.
4.  Do one of the following:
    - To view additional details for a specific report, such as the report
      ARN and associated tags, choose a report from the **Report
      ID** column.
    - To specify multiple reports to manage simultaneously, select the
      reports using the checkbox column.

5.  To manage one or more reports, choose one of the following from the
    **Actions** drop-down menu:

        * Delete cache report — This deletes the record of the cache
         report from the Storage Gateway database. Delete records for obsolete cache
         reports to make room for new reports. Each file share can have up to 10
         existing cache reports at any time.


        ###### Note

        Deleting the cache report record using this procedure **does not** delete the report file object
         from Amazon S3.
        * Cancel report — This cancels a report that is currently
         in-progress. Cancel an in-progress report if you made a mistake during
         report configuration, or if the report takes an unusually long time to
         complete. Confirm the cancellation when prompted.


        ###### Note

        Completion times can vary significantly depending on the number of
         files in the cache. Typically, most reports complete within 5
         minutes.

    The Storage Gateway console displays a message indicating the result of the
    cancellation or delete action.
