# Creating a standard export

You can create a standard data export that you can analyze using other processing tools
(Amazon Athena, for example).

###### To create a standard data export

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Data Exports**.
3. Choose **Create export**.
4. On the **Create export** page, under **Export
   type**, choose **Standard data export**.
5. For **Export name**, enter a name for your export.

Export names can have up to 128 characters and must be unique. Valid characters are
a-z, A-Z, 0-9, - (hyphen), and \_ (underscore). 6. Under **Data table configurations**, you can specify the table and
columns to be contained within your export. First, select the table you want to
export.

###### Note

Exporting the Cost optimization recommendations table requires a service-linked
role. For more information, see [Service-linked roles for Data Exports](../../../cost-management/latest/userguide/data-exports-SLR.md "../../../cost-management/latest/userguide/data-exports-SLR.md").

Exporting the Carbon emissions table requires the IAM permission
`sustainability:GetCarbonFootprintSummary` to access the Customer Carbon
Footprint Tool and data.

With the exception of FOCUS 1.0 with AWS columns and Carbon emissions, there are
different table configurations to add data to your export.

    1. For **CUR 2.0**:




    	1. Select **Include resource IDs** to include the IDs of each
    	 individual resource in the export.


    	###### Note

    	Including resource IDs creates individual line items for each of your
    	 resources. This might increase the size of your export significantly, based on
    	 your AWS usage.

    	Selecting resource ID will add a Tag column containing data about users, accounts, cost categories, and
    	 resources when you create a new report. You can deselect the columns to avoid redundant information.
    	2. Select **Split cost allocation data** to include detailed
    	 cost and usage for shared resources (Amazon ECS and Amazon EKS).


    	###### Note

    	Including split cost allocation data creates individual line items for each
    	 of your resources (that is, ECS tasks and Kubernetes pods). This might increase
    	 the size of your Cost and Usage Report significantly, based on your AWS
    	 usage.
    	3. Select **Include Capacity reservation data** to include the Capacity
    	 reservation columns and row-level granularity in the export.


    	###### Note

    	Including Capacity reservation data creates 3 new columns and can split the instance line items, based on your AWS usage.
    	4. Select **Enable manual discount format** to convert your
    	 discounts so that they appear in the Cost and Usage Report in the manual discount
    	 format instead of the standard automated format.


    	###### Note

    	This option only appears if you are on the discount automation
    	 program.
    	5. For **Time granularity**, choose between hourly, daily, or
    	 monthly to have the line items in the export aggregated by that time
    	 granularity.
    2. For **FOCUS 1.0 with AWS columns**, there are no
     table configurations.
    3. For **Carbon emissions**, there are no table
     configurations.
    4. For **Cost optimization recommendations**:




    	1. Select **Include all recommendations** to remove the lowest
    	 savings value recommendation of recommendations that are incompatible with one
    	 another.
    	2. Add **Recommendation filters** if you want certain types of
    	 recommendations to be filtered out before incompatible recommendations are
    	 removed.
    ###### Note

    If you specified these settings in the Cost Optimization Hub console, they will
     be carried over to Data Exports when you choose **Create an
     export** in Cost Optimization Hub.

7. For **Column selection**, select the columns you want to include in
   your export. If unsure, select all columns by selecting the first check box at the top of
   the table. Selecting more columns may increase the file size of your export.
8. Under **Data table delivery options**, for **Data export
   refresh cadence**: .
   - For billing and cost management data exports, the only option available is
     **Daily - export is refreshed up to one time per day**.
   - For carbon emissions data exports, the only option available is \*\*Monthly
   * export is refreshed once per month\*\*. Each update provides the carbon
     emissions data from the previous month (for example, a February update contains January data).

9. For **Compression type and file format**, choose between the
   following for your export:
   - Parquet – Parquet
   - gzip – text/csv

10. For **File versioning**, choose between the following which
    determines whether your export is overwritten with each update:
    - **Overwrite existing data export file**: Each export refresh
      overwrites the previous delivery within the data partition (for example, billing
      periods). Overwriting exports can save on Amazon S3 storage costs.

    ###### Note

    Overwrite is not supported for exports of cost optimization
    recommendations.
    - **Create new data export file**: Each export refresh is written
      to a separate directory, even for deliveries of the same partition (for example,
      billing period). Creating new export versions allows you to track the changes in cost
      and usage data over time.

11. Under **Data export storage settings**, for **S3
    bucket** name, choose **Configure**.
12. In the **Configure S3 bucket** dialog box, do one of the
    following:
    - Select existing bucket.
    - Choose **Create a bucket**, enter an **S3 bucket
      name**, and then choose the **Region** where you want to
      create a new bucket.

13. Review the **Bucket policy**. If you're selecting an existing bucket,
    you need to acknowledge that Data Exports will overwrite you existing S3 bucket policy. The new
    policy will allow both CUR and Data Exports to deliver exports.
14. For **S3 path prefix**, enter a name for the directory that will be
    created in your S3 bucket to store all the export data.
15. Under **Tags**, you can choose to add up to 50 tags in order to
    search and filter your resources or track your AWS costs.

###### Note

Adding tags is optional. 16. Choose **Create** to complete the creation of your export.
