# AWS billing and usage reports for CloudFront

AWS provides two usage reports for CloudFront:


* The AWS billing report is a high-level view of all activity for AWS services
 that you're using, including CloudFront.
* The AWS usage report is a summary of activity for a specific service, aggregated
 by hour, day, or month. It also includes usage charts that provide a graphical
 representation of your CloudFront usage.
###### Note

Like other AWS services, CloudFront charges you for only what you use. For more
 information, see [CloudFront
 pricing](https://aws.amazon.com/cloudfront/pricing/ "https://aws.amazon.com/cloudfront/pricing/").

###### Topics

* [View the AWS billing report for CloudFront](#billing-report "#billing-report")
* [View the AWS usage report for CloudFront](#usage-report "#usage-report")
* [Interpret your AWS bill and usage
 reports for CloudFront](billing-and-usage-interpreting.md "billing-and-usage-interpreting.md")

## View the AWS billing report for CloudFront


You can view a summary of your AWS usage and charges, listed by service, on the
 **Bills** page in the AWS Billing and Cost Management console.


###### To view the AWS billing report

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
 [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Bills**.
3. Choose a **Billing period** (for example, August
 2023).
4. On the **Charges by service** tab, choose
 **CloudFront**, and then expand **Global** or
 the AWS Region name.
5. To download a detailed billing report in CSV format, choose **Download
 all to CSV**.

For more information about your AWS bill, see [Viewing your
 bill](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/getting-viewing-bill.html "https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/getting-viewing-bill.html") in the *AWS Billing User Guide*.


The billing report includes the following values that apply to CloudFront:



* **ProductCode** –
 `AmazonCloudFront`
* **UsageType** – One of the following
 values:




	+ A code that identifies the type of data transfer
	+ `Invalidations`
	+ `Executions-CloudFrontFunctions`
	+ `KeyValueStore-APIOperations`
	+ `KeyValueStore-EdgeReads`
	+ `RealTimeLog-KinesisDataStream`
	+ `SSL-Cert-Custom`
* **ItemDescription** – A description of the
 billing rate for the **UsageType**.
* **UsageStart Date** and **UsageEndDate** – The day that the usage applies to, in
 Coordinated Universal Time (UTC).
* **UsageQuantity** – One of the following
 values: 




	+ The number of requests during the specified time period
	+ The amount of data transferred in gigabytes
	+ The number of objects invalidated
	+ The sum of the prorated months that you had SSL certificates
	 associated with enabled CloudFront distributions. For example, if you have one
	 certificate associated with an enabled distribution for an entire month
	 and another certificate associated with an enabled distribution for half
	 of the month, this value will be 1.5.

## View the AWS usage report for CloudFront


AWS provides a CloudFront usage report that is more detailed than the billing report but
 less detailed than CloudFront access logs. The usage report provides aggregate usage data by
 hour, day, or month, and it lists operations by region and usage type, such as data
 transferred out of the Australia region.


###### To view the AWS usage report

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
 [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Explorer**.
3. On the **New cost and usage report** page, in the **Report parameters** pane, choose a date range and granularity for the report.
4. Under **Filters**, **Service**, select **CloudFront**.
5. Select the **Usage type**.
6. Under **Cost and usage breakdown**, choose **Download as CSV**.

For more information about the AWS usage report, see [AWS Usage
 Report](https://docs.aws.amazon.com/cur/latest/userguide/usage-report.html "https://docs.aws.amazon.com/cur/latest/userguide/usage-report.html") in the *AWS Data Exports User Guide*. 


The CloudFront usage report includes the following values:



* **Service** –
 `AmazonCloudFront`
* **Operation** – HTTP method. Values
 include `DELETE`, `GET`, `HEAD`,
 `OPTIONS`, `PATCH`, `POST`, and
 `PUT`.
* **UsageType** – One of the following
 values:




	+ A code that identifies the type of data transfer
	+ `Invalidations`
	+ `Executions-CloudFrontFunctions`
	+ `KeyValueStore-APIOperations`
	+ `KeyValueStore-EdgeReads`
	+ `RealTimeLog-KinesisDataStream`
	+ `SSL-Cert-Custom`
* **Resource** – Either the ID of the CloudFront
 distribution associated with the usage or the certificate ID of an SSL
 certificate that you have associated with a CloudFront distribution.
* **StartTime/EndTime** – The day that the
 usage applies to, in Coordinated Universal Time (UTC).
* **UsageValue** – 1) The number of requests
 during the specified time period or 2)the amount of data transferred in
 bytes.

If you’re using Amazon S3 as the origin for CloudFront, consider running the usage report for
 Amazon S3, too. However, if you use Amazon S3 for purposes other than as an origin for your CloudFront
 distributions, it might not be clear what portion applies to your CloudFront usage.


###### Tip

For detailed information about every request that CloudFront receives for your objects,
 turn on CloudFront access logs for your distribution. For more information, see [Standard logging (access logs)](AccessLogs.md "AccessLogs.md").


For more information about understanding the CloudFront charges and usage types on your
 reports, see [Interpret your AWS bill and usage
 reports for CloudFront](billing-and-usage-interpreting.md "billing-and-usage-interpreting.md").
