# Create a cache report for your S3 File Gateway

S3 File Gateway can generate a report of the metadata for files that are currently in the
local upload cache for a specific file share. You can apply filters and additional
criteria that determine which specific types of cached files appear in the report. You
can use this report to help identify and resolve gateway issues. For example, if you
have files failing upload from your gateway to Amazon S3, you can generate a report that
lists the specific files that are failing to upload, and the reasons for upload failure.
The report is a CSV file containing a list of files which match the set of filter
parameters you specify. The output file is stored as an Amazon S3 object in a bucket location
that you specify when you configure the report. To create a cache report using the
AWS Storage Gateway API, see [StartCacheReport](../../../storagegateway/latest/APIReference/API_StartCacheReport.md "../../../storagegateway/latest/APIReference/API_StartCacheReport.md") in the _Storage Gateway API Reference_. To
create a cache report in the Storage Gateway console, use the following procedure.

**Prerequisites**

- Your gateway must have `s3:PutObject` and
  `s3:AbortMultipartUpload` permissions for the Amazon S3 bucket where
  you want to store the cache report.
- No other cache reports can currently be in-progress for the file share.
- There must be fewer than 10 existing cache reports for the file share.
- The gateway must be online and connected to AWS.
- The gateway root disk must have at least 20GB of free space.

###### To create a cache report using the Storage Gateway console

1. Open the Storage Gateway console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/").
2. In the navigation pane on the left side of the page, choose **File
   shares**, and then choose the file share for which you want to
   create a cache report.
3. From the **Actions** drop-down menu, choose**Create
   cache report**.
4. For **Amazon S3 location**, enter the Amazon S3 bucket and prefix of
   the location where you want to save the completed cache report CSV file object
   in Amazon S3. To select the bucket and prefix from your existing Amazon S3 storage, choose
   **Browse S3**.
5. For **IAM role**, do one of the following to specify an
   IAM role that grants your File Gateway permissions to generate and store your
   cache report:
   - To specify an existing IAM role, choose a role from the drop-down
     list.
   - To manually create a new IAM role, choose **Create a
     role**, then create the new role using the IAM
     console.

###### Note

The IAM role you specify must have the following permissions to write
objects to the report bucket **Amazon S3 location**, and to stop
multipart uploads to the report bucket:

    * `s3:PutObject`
    * `s3:AbortMultipartUpload`The role must also allow the `storagegateway.amazonaws.com`

service to assume the role using the `sts:AssumeRole`
action. 6. For **Report filter**, do one of the following to determine
which files will be included in the cache report:

    * To include all cached files that are currently failing upload to Amazon S3,
     choose **All files failing to upload**.
    * To include only those files that fail upload to Amazon S3 for a specific
     reason, choose **Specific upload failure reasons
     only**. Then, for **Failure reasons**, select
     one or more of the following reasons:




    	+ Inaccessible storage class — The gateway can't access
    	 the Amazon S3 storage class where the object is stored. For more
    	 information, see [Error: InaccessibleStorageClass](troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-inaccessiblestorageclass "troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-inaccessiblestorageclass").
    	+ Invalid object state — The state of the file on the
    	 gateway doesn't match its state in Amazon S3. For more information,
    	 see [Error: InvalidObjectState](troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-invalidobjectstate "troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-invalidobjectstate").
    	+ Object missing — The object has been deleted or moved
    	 in Amazon S3. For more information, see [Error: ObjectMissing](troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-objectmissing "troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-objectmissing").
    	+ S3 Access Denied — The Amazon S3 bucket access IAM role
    	 doesn't allow the gateway to perform the upload operation. For
    	 more information, see [Error: S3AccessDenied](troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-s3accessdenied "troubleshooting-file-gateway-issues.md#troubleshoot-logging-errors-s3accessdenied").

###### Note

The **Files Failing Upload** flag is reset
every 24 hours and during gateway reboot. If this report captures the files
after the reset, but before they become flagged again, they will not be
reported as **Files Failing Upload**. 7. For **Use a VPC endpoint to connect to S3?**, do one of the
following to specify how your gateway will connect to the Amazon S3 bucket:

    * To connect directly without using Amazon VPC, choose **Connect
     directly to the bucket**.
    * To browse a list of existing Amazon VPC endpoints, choose **Choose
     a VPC endpoint**, and then specify an endpoint from the
     **VPC endpoints** drop-down list that
     appears.
    * To specify an existing Amazon VPC endpoint by its DNS name, choose
     **Input a VPC endpoint DNS name**, and then enter
     the DNS name in the **VPC endpoint DNS name** field
     that appears.

###### Note

If your file share uses a VPC endpoint to connect to Amazon S3 for normal
operations, we recommend using the same VPC when you configure your cache
report. Cache report creation will fail if the gateway can't connect to the
Amazon S3 bucket for any reason, including invalid VPC configuration. 8. (Optional) Under **Tags - optional**, choose **Add
new tag**, then enter a **Key** and
**Value** for your cache report.

A tag is a case-sensitive key-value pair that helps you categorize your
Storage Gateway resources. Adding tags can make filtering and searching for your cache
report easier. You can repeat this step to add up to 50 tags. 9. Choose **Create report** when finished.

Storage Gateway begins generating the report. You can check progress and view status
on the **Cache reports** tab of the details page for the file
share.
