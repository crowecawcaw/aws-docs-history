# AWS usage reports for Amazon S3

When you download a usage report, you can choose to aggregate usage data by hour, day, or
 month. The Amazon S3 usage report lists operations by usage type and AWS Region. For more
 detailed reports about your Amazon S3 storage usage, download dynamically generated AWS
 usage reports. You can choose which usage type, operation, and time period to include.
 You can also choose how the data is aggregated. For more information about usage
 reports, see [AWS Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/usage-report.html "https://docs.aws.amazon.com/cur/latest/userguide/usage-report.html")in the *AWS Data Exports User
 Guide*.

The Amazon S3 usage report includes the following information:


* Service – Amazon S3
* Operation – The operation performed on
 your bucket or object. For a detailed explanation of Amazon S3 operations, see [Tracking Operations in Your
 Usage Reports](aws-usage-report-understand.md#aws-usage-report-understand-operations "aws-usage-report-understand.md#aws-usage-report-understand-operations").
* UsageType – One of the following
 values:




	+ A code that identifies the type of storage
	+ A code that identifies the type of request
	+ A code that identifies the type of retrieval
	+ A code that identifies the type of data transfer
	+ A code that identifies early deletions from S3 Intelligent-Tiering, S3 Standard-IA, S3 One
	 Zone-Infrequent Access (S3 One Zone-IA), S3 Glacier Flexible Retrieval, or
	 S3 Glacier Deep Archive storage
	+ `StorageObjectCount` – The count of objects stored
	 within a given bucket
For a detailed explanation of Amazon S3 usage types, see [Understanding your AWS billing and usage
 reports for Amazon S3](aws-usage-report-understand.md "aws-usage-report-understand.md").
* Resource – The name of the bucket or table 
 associated with the listed usage.
* StartTime – Start time of the day that
 the usage applies to, in Coordinated Universal Time (UTC).
* EndTime – End time of the day that the
 usage applies to, in Coordinated Universal Time (UTC).
* UsageValue – One of the following volume
 values. The typical unit of measurement for data is gigabytes (GB). However,
 depending on the service and the report, terabytes (TB) might appear
 instead.




	+ The number of requests during the specified time period
	+ The amount of data transferred
	+ The amount of data stored in a given hour
	+ The amount of data associated with restorations from S3 Standard-IA, S3 One Zone-IA,
	 S3 Glacier Flexible Retrieval, or S3 Glacier Deep Archive
	 storage
###### Tip

For detailed information about every request that Amazon S3 receives for your objects,
 turn on server access logging for your buckets. For more information, see [Logging requests with server access logging](ServerLogs.md "ServerLogs.md"). 

You can download a usage report as an XML or a
 comma-separated values (CSV) file. The following is an example CSV usage report opened
 in a spreadsheet application.


![A CSV usage report in a spreadsheet application.](../../../images/AmazonS3/latest/userguide/images/s3-usage-report.png)
For more information, see [Understanding your AWS billing and usage
 reports for Amazon S3](aws-usage-report-understand.md "aws-usage-report-understand.md").


## Downloading the AWS Usage Report


You can download a usage report as an XML or a CSV file.


###### To download the usage report

1. Sign in to the AWS Management Console and open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the title bar, choose your username or account ID, and then choose
 **Billing and Cost Management**.
3. In the navigation pane, choose **Legacy Pages** and choose **Cost and usage
 reports**.
4. Under AWS Usage Report, choose **Create a Usage
 Report**.
5. On the **Download usage report** page, choose the
 following settings:




	* **Services** – Choose
	 **Amazon Simple Storage Service**.
	* **Usage Types**
	 – For a detailed explanation of Amazon S3 usage types, see [Understanding your AWS billing and usage
	 reports for Amazon S3](aws-usage-report-understand.md "aws-usage-report-understand.md").
	* **Operation**
	 – For a detailed explanation of Amazon S3 operations, see [Tracking Operations in Your
	 Usage Reports](aws-usage-report-understand.md#aws-usage-report-understand-operations "aws-usage-report-understand.md#aws-usage-report-understand-operations").
	* **Time Period**
	 – The time period that you want the report to cover.
	* **Report
	 Granularity** – Whether you want the
	 report to include subtotals by the hour, by the day, or by the
	 month.
6. Choose **Download**, choose the download format
 (**XML Report** or **CSV Report**),
 and then follow the prompts to open or save the report.

## More info



* [Understanding your AWS billing and usage
 reports for Amazon S3](aws-usage-report-understand.md "aws-usage-report-understand.md")
* [AWS Billing reports for Amazon S3](aws-billing-reports.md "aws-billing-reports.md")
