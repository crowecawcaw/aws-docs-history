# Creating reports

###### Note

Data Exports enables you to create exports of the Cost and Usage Report (CUR) 2.0. This is the
new and recommended way to receive your detailed cost and usage data from AWS. For more
information, see [Migrating from CUR to CUR 2.0 in Data Exports](dataexports-migrate.md "dataexports-migrate.md").

You can use the **Cost and Usage Reports** page of the Billing and Cost Management console to create
Cost and Usage Reports. You can create up to 10 reports for an individual AWS account.

###### Note

It can take up to 24 hours for AWS to start delivering reports to your Amazon S3 bucket.
After delivery starts, AWS updates the AWS Cost and Usage Reports files at least once a day.

###### To create Cost and Usage Reports

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy Pages**, choose
   **Cost and Usage Reports**.
3. Choose **Create report**.
4. For **Report name**, enter a name for your report.
5. For **Report additional content**, select **Include resource
   IDs** to include the IDs of each individual resource in the report.

###### Note

Including resource IDs creates individual line items for each of your resources.
This might increase the size of your Cost and Usage Reports files significantly, based on your
AWS usage. 6. Select **Split cost allocation data** to include detailed cost and
usage for shared resources (Amazon ECS and Amazon EKS).

###### Note

Including split cost allocation data creates individual line items for each of your
resources (that is, ECS tasks and Kubernetes pods). This might increase the size of your
Cost and Usage Reports files significantly, based on your AWS usage. 7. For **Data refresh settings**, select whether you want the AWS Cost and Usage Reports
to refresh if AWS applies refunds, credits, or support fees to your account after
finalizing your bill. When a report refreshes, a new report is uploaded to Amazon S3. 8. Choose **Next**. 9. For **S3 bucket**, choose **Configure**. 10. In the **Configure S3 bucket** dialog box, do one of the
following:

    * Select an existing bucket.
    * Select **Create a bucket**, enter a bucket name, and then choose
     the Region where you want to create a new bucket.

11. Review the bucket policy, select **The following default policy will be
    applied to your bucket**, and then choose **Save**.
12. For **Report path prefix**, enter the report path prefix that you
    want prepended to the name of your report.
13. For **Time granularity**, choose one of the following:
    - **Hourly** if you want the line items in the report to be
      aggregated by the hour.
    - **Daily** if you want the line items in the report to be
      aggregated by the day.
    - **Monthly** if you want the line items in the report to be
      aggregated by month.

14. For **Report versioning**, choose whether you want each version of
    the report to overwrite the previous version of the report or to be delivered in addition
    to the previous versions.

Overwriting reports can save on Amazon S3 storage costs. Delivering new report versions can
improve auditability of billing data over time. 15. For **Report data integration**, select whether you want to enable
your Cost and Usage Reports to integrate with Amazon Athena, Amazon Redshift, or Quick Suite. The report is compressed in
the following formats:

    * **Athena**: parquet format
    * **Amazon Redshift or Quick Suite**: .gz compression

16. Choose **Next**.
17. After you have reviewed the settings for your report, choose **Review and
    Complete**.
    You can always return to the **Cost and Usage Reports** page in the Billing and Cost Management console to
    see when your reports were last updated.
