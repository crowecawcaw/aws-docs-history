# Creating a Legacy CUR export

You can create a data export of your legacy Cost and Usage Report (CUR). This workflow
uses the legacy `cur` APIs and doesn't allow you to use SQL to define your export
contents. CUR 2.0 with its additional columns and SQL access is only available as a standard
data export.

###### To create a legacy data export

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Data Exports**.
3. Choose **Create**.
4. On the **Create** page, under **Export type**,
   choose **Legacy CUR export**.
5. For **Export name**, enter a name for your export.
6. Under **Export content**, select the data to include in your CUR
   export.
   - For **Additional export content**, select **Include
     resource IDs** to include the IDs of each individual resource in the
     export.

   ###### Note

   Including resource IDs creates individual line items for each of your resources.
   This might increase the size of your export significantly, based on your AWS
   usage.
   - Select **Split cost allocation data** to include detailed cost
     and usage for shared resources (Amazon ECS and Amazon EKS).

   ###### Note

   Including split cost allocation data creates individual line items for each of
   your resources (that is, ECS tasks and Kubernetes pods). This might increase the
   size of your Cost and Usage Report significantly, based on your AWS usage.
   - Select **Enable manual discount format** to convert your
     discounts so that they appear in the Cost and Usage Report in the manual discount
     format instead of the standard automated format.

   ###### Note

   This is only available for customers on Discount Automation.

7. Under **Data table delivery options**, for **Time
   granularity**, choose one of the following:
   - **Hourly** if you want the line items in the export to be
     aggregated by the hour.
   - **Daily** if you want the line items in the export to be
     aggregated by the day.
   - **Monthly** if you want the line items in the export to be
     aggregated by month.

8. For **Report versioning**, choose between the following:
   - **Create new report version**: Each report refresh will be
     written to a separate directory, even for deliveries of the same billing period.
     Choose this to improve the ability to audit your exports over time.
   - **Overwrite existing report**: Each report refresh will overwrite
     the previous delivery within the same billing period. Deliveries of new billing
     periods be delivered as new files and directories. Choose this to save on Amazon S3
     storage costs.

9. For **Report data integration**, choose whether you want to enable
   your Cost and Usage Reports to integrate with Amazon Athena, Amazon Redshift, or Amazon
   QuickSight. The report is compressed in the following formats:
   - **Amazon Athena**: Selects the delivery options optimal for
     Amazon Athena which are Parquet file format and overwrite existing report. Also
     delivers a script that can be used to set up the integration.
   - **Amazon Redshift**: Selects the delivery option optimal for
     Amazon Redshift which is gzip/csv file format. Also delivers a script that can be used
     to set up the integration.
   - **Amazon QuickSight**: Selects the delivery option optimal for
     Amazon QuickSight which is gzip/csv file format.

10. For **Compression type and file format**, choose between the
    following:
    - Parquet – Parquet
    - gzip – text/csv
    - zip – text/csv

11. Under **Data export storage settings**, for **S3
    bucket** name, choose **Configure**.
12. In the **Configure S3 bucket** dialog box, do one of the
    following:
    - Select existing bucket.
    - Choose **Create a bucket**, enter an **S3 bucket
      name**, and then choose the **Region** where you want to
      create a new bucket.

13. Review the **Bucket policy**, and then choose **Create
    bucket**.
14. For **S3 path prefix**, enter the S3 path prefix that you want
    prepended to the name of your export.
15. Under **Tags**, you can choose to add up to 50 tags in order to
    search and filter your resources or track your AWS costs.

###### Note

Adding tags is optional. 16. Choose **Create report**.
