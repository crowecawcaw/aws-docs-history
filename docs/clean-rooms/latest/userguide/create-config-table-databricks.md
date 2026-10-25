

# Creating a configured table – Databricks data source
<a name="create-config-table-databricks"></a>

In this procedure, the [member](glossary.md#glossary-member) does the following tasks: 
+ Configures an existing Databricks table, shared through Delta Sharing, for use in AWS Clean Rooms. (This step can be done before or after joining a collaboration, unless using Cryptographic Computing for Clean Rooms.)
+ Names the [configured table](glossary.md#glossary-configured-table) and chooses which columns to use in the collaboration.

The following procedure assumes that:
+ The collaboration member has already [prepared their Databricks data](prepare-data-databricks.md) by creating a Delta Sharing share and recipient and a service role that AWS Clean Rooms can assume.

**To create a configured table – Databricks data source**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Tables**.

1. In the upper right corner, choose **Configure new table**.

1. For **Data source**, under **Third-party clouds and data sources**, choose **Databricks**. 

1. For **Databricks connection details**, enter the following information about the Delta Sharing share that you prepared:
   + The **Workspace URL** for your Databricks workspace.
   + The **Delta Sharing endpoint** URL for your recipient.
   + The **Share name**, **Schema name**, and **Table name** that you want to bring into the collaboration.
**Note**  
AWS Clean Rooms supports Databricks external tables that are backed by data in Amazon S3.

1. For **Databricks table and schema details**, enter the **Column name** for each column that you want to be visible to query runners. AWS Clean Rooms infers the schema automatically, so you don't enter data types.

1. For **Columns allowed in collaborations**, choose an option based on your goal. 


<table>
<thead>
  <tr><th>Your goal</th><th>Recommended option</th></tr>
</thead>
<tbody>
  <tr><td>Allow all columns for use in AWS Clean Rooms (subject to analysis rules)</td><td><b>All columns</b></td></tr>
  <tr><td>Allow one or more of the columns that you entered</td><td><b>Custom list</b></td></tr>
</tbody>
</table>


1. For **Configured table details**, 

   1. Enter a **Name** for the configured table.

      You can use the default name or rename this table.

   1. Enter a **Description** of the table. 

      The description helps differentiate between other configured tables with similar names.

   1. If you want to enable **Tags** for the configured table resource, choose **Add new tag** and then enter the **Key** and **Value** pair. 

1. Choose **Configure new table**. 

Now that you have created a configured table, you are ready to: 
+ [Add an analysis rule to the configured table](add-analysis-rule.md)
+ [Associate the configured table to a collaboration](associate-configured-table.md)