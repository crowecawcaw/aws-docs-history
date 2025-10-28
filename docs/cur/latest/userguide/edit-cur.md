# Editing your Cost and Usage Reports configuration

You can use the **Cost and Usage Reports** page in the Billing and Cost Management console to edit
Cost and Usage Reports.

###### Note

Report names can't be edited. If you chose **Overwrite** for
**Report versioning**, you're unable to edit the report name, whether the
report includes resource IDs, time granularity, or the report versioning. If you delete a
report set to **Overwrite** and create a new report with the same name,
Amazon S3 bucket, and path prefix, your data could corrupt and become inaccurate.

###### To edit Cost and Usage Reports

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy Pages**, choose
   **Cost and Usage Reports**.
3. Select the report that you want to edit and choose **Edit
   report**.
4. (Versioned reports only) For **Report additional content**, select
   **Include resource IDs** to include the IDs of each individual resource
   in the report.

###### Note

Including resource IDs creates individual line items for each of your resources.
This might increase the size of your Cost and Usage Reports files significantly, based on your
AWS usage. 5. Select **Split cost allocation data** to include detailed cost and
usage for shared resources (Amazon ECS and Amazon EKS).

###### Note

Including split cost allocation data creates individual line items for each of your
resources (that is, ECS tasks and Kubernetes pods). This might increase the size of your
Cost and Usage Reports files significantly, based on your AWS usage. 6. For **Data refresh settings**, select whether you want the AWS Cost and Usage Reports
to refresh if AWS applies refunds, credits, or support fees to your account after
finalizing your bill. When a report refreshes, a new report is uploaded to Amazon S3. 7. Choose **Next**. 8. For **S3 bucket**, enter the name of the Amazon S3 bucket where you want
the reports delivered. 9. Choose **Verify**.

###### Note

The bucket must have appropriate permissions to be valid. For more information on
adding permissions to the bucket, see [Setting Bucket and Object Access Permissions](../../../AmazonS3/latest/userguide/set-permissions.md "../../../AmazonS3/latest/userguide/set-permissions.md") in the _[Amazon Simple Storage Service User Guide](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")_. 10. For **Report path prefix**, enter the report path prefix that you
want prepended to the name of your report. 11. (Versioned reports only) For **Time granularity**, choose one of the
following:

    * **Hourly**: If you want the line items in the report to be
     aggregated by the hour.
    * **Daily**: If you want the line items in the report to be
     aggregated by the day.
    * **Monthly** if you want the line items in the report to be
     aggregated by month.

12. (Versioned reports only) For **Report versioning**, choose whether
    you want each version of the report to overwrite the previous version of the report, or to
    be delivered in addition to the previous versions.
13. For **Report data integration**, select whether you want to enable
    your AWS CUR to integrate with Amazon Athena, Amazon Redshift, or Quick Suite. The report is compressed in the
    following formats:
    - **Athena**: Parquet format
    - **Amazon Redshift or Quick Suite**: .gz compression

14. Choose **Save**.
