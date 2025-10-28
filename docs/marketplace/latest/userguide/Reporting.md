# Seller reports in AWS Marketplace

###### Important

On August 30, 2024, AWS Marketplace will discontinue several reports and data sets:

- The Marketplace legacy comma separated (csv) Seller reports
- The Commerce Analytics Service (CAS) API
- Associated email notifications
  Check the report pages for impacted reports, or check with you AWS administrator who was
  issued communication on 5/30/2024 if you have questions.

AWS Marketplace provides reports that include information about product usage, buyers, billing, and
payment information. Reports are available to all registered AWS Marketplace sellers.

Here are some key points about report generation:

- Reports are generated daily, weekly, or monthly, depending on the report.
- Reports are generated at 00:00 UTC and cover through 24:00 UTC of the previous day.
- Reports are generated as .csv files.
- You can configure Amazon SNS to notify you when data is delivered to your encrypted Amazon S3
  bucket. After you configure notifications, AWS sends notifications to the email address
  that is associated with the AWS account that you registered with on AWS Marketplace.

For information on how to configure notifications, see [Getting started with
Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the _Amazon Simple Notification Service Developer Guide._

To cancel getting notification emails, contact the [AWS Marketplace Seller Operations](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/") team.

- To learn about each report, you can download [sample reports](https://s3.amazonaws.com/awsmp-loadforms/AWS+Marketplace+-+Seller+Reporting+Examples.zip "https://s3.amazonaws.com/awsmp-loadforms/AWS+Marketplace+-+Seller+Reporting+Examples.zip").

## Accessing reports

AWS Marketplace provides two ways to configure your reports:

- Using an API interface. The [Accessing product and customer data with the
  AWS Marketplace Commerce Analytics Service](commerce-analytics-service.md "commerce-analytics-service.md") enables you to automatically access the
  data in your reports through an API interface. You can automate ingesting your information
  and download a portion of a report instead of the whole report. The service returns data
  asynchronously to a file in Amazon Simple Storage Service rather than directly as with a traditional
  API. The data is delivered in a machine-readable format so that you can import or
  incorporate the data into your systems.
- Using the reports dashboard in the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/reports/ "https://aws.amazon.com/marketplace/management/reports/"). This dashboard
  provides reports for previous reporting periods.

You can control access to reports by using AWS Identity and Access Management (IAM) permissions.

## Available AWS Marketplace seller reports

The following reports are available in AWS Marketplace:

- [Daily business report](daily-business-report.md "daily-business-report.md")
- [Daily customer subscriber report](daily-customer-subscriber-report.md "daily-customer-subscriber-report.md")
- [Disbursement report](monthly-disbursement-report.md "monthly-disbursement-report.md")
- [Monthly billed revenue report](monthly-billed-revenue-report.md "monthly-billed-revenue-report.md")
- [Sales compensation report](sales-compensation-report.md "sales-compensation-report.md")
