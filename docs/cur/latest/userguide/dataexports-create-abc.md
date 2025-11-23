# Configuring Cost and Usage Reports 2.0 using AWS Billing Conductor

With AWS Billing Conductor, you can create pro forma AWS Cost and Usage Report (AWS CUR) 2.0 for each billing group. These pro forma reports use the same file format, granularity, and columns as the standard AWS CUR 2.0, providing the most comprehensive cost and usage data available for a given time period.

For more information about AWS Billing Conductor, see the [AWS Billing Conductor User Guide](../../../billingconductor/latest/userguide/what-is-billingconductor.md "../../../billingconductor/latest/userguide/what-is-billingconductor.md").

###### Topics

- [Comparing standard and AWS Billing Conductor Cost and Usage Reports](#dataexports-standard-ABC "#dataexports-standard-ABC")
- [Creating pro forma Cost and Usage Reports for a billing group](#dataexports-abc-cur "#dataexports-abc-cur")

## Comparing standard and AWS Billing Conductor Cost and Usage Reports

There are a few differences between the standard Cost and Usage Reports and pro forma AWS CUR created using the AWS Billing Conductor configuration.

**Account coverage**

- Standard AWS CUR – Includes cost and usage data for all accounts in your consolidated billing family
- Pro forma AWS CUR – Includes only accounts that belong to the specific billing group at the time of report generation

**Invoice handling**

- Standard AWS CUR – Populates the invoice column after AWS generates an invoice
- Pro forma AWS CUR – Does not populate the invoice column because AWS does not generate or issue invoices based on pro forma billing data

## Creating pro forma Cost and Usage Reports for a billing group

Use the following steps to generate a pro forma AWS CUR for a billing group.

###### To create pro forma Cost and Usage Reports for a billing group

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Data Exports**.
3. Choose **Create**.
4. In the **Export details** section, choose **Standard data export**.
5. For **Export name**, enter a name for your export.
6. Under **Data table content settings**, choose **CUR 2.0**.
7. Under **Data table configurations**, choose **Include resource IDs** to include the IDs of each individual resources in the report.

**Split cost allocation data** is disabled when pro forma data export is enabled. 8. Choose **Next**. 9. For **S3 bucket**, choose **Configure**. 10. In the **Configure S3 Bucket** dialog box, do one of the following:

    * Choose an existing bucket from the drop down list and choose **Next**.
    * Enter a bucket name and the AWS Region where you want to create a new bucket and choose **Next**.

11. Review the **Bucket policy**, select **I have confirmed that this policy is correct**, and choose **Save**.
12. For **S3 path prefix**, enter the S3 path prefix that you want
    prepended to the name of your export.
13. For **Time granularity**, choose one of the following:
    - **Hourly** if you want the line items in the report to be aggregated by the hour.
    - **Daily** if you want the line items in the report to be aggregated by the day.
    - **Monthly** if you want the line items in the report to be aggregated by the month.

14. For **Report versioning**, choose whether you want each version of the report to overwrite the previous version of the report, or to be delivered in addition to the previous versions.

Overwriting reports can save on Amazon S3 storage costs. Delivering new report versions can improve auditability of billing data over time. 15. Choose **Next**. 16. After you have reviewed the settings for your report, choose **Review and Complete**.
