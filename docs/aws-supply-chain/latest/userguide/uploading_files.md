# Uploading files for the first time

You can use the AWS Supply Chain Auto-association feature to upload your raw data and automatically associate your raw data with AWS Supply Chain data model. You can also view the _required_
columns and tables for each AWS Supply Chain module within the AWS Supply Chain web application.

For a brief demonstration of how auto-association works, watch the following video:

###### Note

You can only upload CSV files to Amazon S3 when you are using Auto-association.

After the source columns from your dataset are associated with the destination columns, AWS Supply Chain will automatically generate the SQL recipe.

###### Note

AWS Supply Chain uses Amazon Bedrock for Auto-association, which it's not supported in all
the &AWS Regions that AWS Supply Chain is available in. Hence,
AWS Supply Chain will call Amazon Bedrock endpoint from the closest available
region, Europe (Ireland) Region – Europe (Frankfurt) and Asia Pacific (Sydney) Region
– US West (Oregon).

###### Note

Auto-association using the Large Language Models (LLM) is only supported when data is ingested through Amazon S3.

1. On the AWS Supply Chain dashboard, on the left navigation pane, choose **Data
   Lake** and then choose the **Data Ingestion** tab.

The **Data Ingestion** page appears. 2. Choose **Add New Source**.

The **Select your data source** page appears. 3. On the **Select your data source** page, choose **Upload files**. 4. Choose **Continue**.

![Uploading your source files](images/data_lake.png) 5. On the **Which capabilities do you want to run** page, choose the
AWS Supply Chain modules that you want to use. You can choose more than one
module. 6. Under **Upload your source files** section, add a suffix to the **Source system name**. For example, oracle_test. 7. To upload your source dataset, choose **files** or drag and drop files.

The source tables with the name and status are displayed. 8. Choose **Upload to S3**. The _upload status_ will change to display the status. 9. Under **Review data requirements**, review all the required data entities and
columns for the selected AWS Supply Chain feature. All of the required
primary and foreign keys are displayed. 10. Choose **Continue**. 11. Under **Manage your source tables**, the following source tables and the
columns listed will be auto associated and imported into data lake.

Choose **Delete table** to delete any of the source tables before importing into data lake.

![Managing your source files](images/data_lake1.png) 12. Choose **Accept all and Continue**.

A message on auto-associating your tables to AWS Supply Chain data lake is displayed.

![Managing destination flows](images/data_lake3.png) 13. Under **Manage Destination Flows**, you can review each auto-associated table.

By default, **Auto-Association** is enabled and the source columns are auto-associated with the destination columns. To update the auto-associated columns, you can update the SQL recipe to create your custom recipe. 14. Under **Source Columns**, all of the unassociated source columns are listed.
Drag and drop the unassociated columns to the **Destination
Columns** on the right. 15. Follow the preceding step for each auto-associated table. 16. Choose **Submit**. 17. Choose **Exit and Review Destination Flows**.
