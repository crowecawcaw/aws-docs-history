

# Querying configured tables using the SQL code editor
<a name="use-sql-editor"></a>

As a member who can query, you can build a query manually by writing SQL code in the SQL code editor. The SQL code editor is located in the **Analysis** section of the **Analysis** tab in the AWS Clean Rooms console. 

The SQL code editor is displayed by default. If you want to use the analysis builder to build queries, see [Querying with the analysis builder](query-data-analysis-builder.md). 

**Important**  
If you start writing a SQL query in the code editor and then turn on the **Analysis builder UI**, your query isn't saved.

AWS Clean Rooms supports many SQL commands, functions, and conditions. For more information, see the [AWS Clean Rooms SQL Reference](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference.html). 

**Tip**  
If a scheduled maintenance occurs while a query is running, the query is terminated and rolled back. You must restart the query. 

**To query configured tables using the SQL code editor**

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Run queries**.

1. On the **Analysis** tab, under **Tables**, view the list of tables and their associated analysis rule type (**Aggregation analysis rule**, **List analysis rule**, or **Custom analysis rule**).
**Note**  
If you don’t see the tables that you expect in the list, it might be for the following reasons:  
The tables haven't been [associated](associate-configured-table.md).
The tables don't have an [analysis rule configured](add-analysis-rule.md).

1. (Optional) To view the table's schema and analysis rule controls, expand the table by selecting the plus sign icon (**\+**).

1. Under the **Analysis** section, for **Analysis mode**, select **Write SQL code**.
**Note**  
The **Analysis** section only displays if the member who can receive results and the member who is responsible to pay for query compute costs have joined the collaboration as an active member.

1. Build the query by typing the query into the SQL code editor.

   For more information about supported SQL commands and functions, see the [AWS Clean Rooms SQL Reference.](https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/sql-reference.html) 

   You can also use the following options to build your query.

------
#### [ Use an example query ]

   To use an example query

   1. Select the three vertical dots next to the table.

   1. Under **Insert in editor**, choose **Example query**.
**Note**  
Inserting an **Example query** appends it to the query already in the editor.

      The query example appears. All of the tables listed under **Tables** are included in the query. 

   1. Edit the placeholder values in the query.

------
#### [ Insert column names or functions ]

   To insert a column name or function

   1. Select the three vertical dots next to a column.

   1. Under **Insert in editor**, choose **Column name**.

   1. To manually insert a function that is permitted on a column, 

      1. Select the three vertical dots next to a column.

      1. Select **Insert in editor**.

      1. Select the name of the permitted function (such as INNER JOIN, SUM, SUM DISTINCT, or COUNT).

   1. Press **Ctrl** \+ **Space** to view the table schemas in the code editor.
**Note**  
Members who can query can view and use the partition columns in each configured table association. Ensure the partition column is labeled as a partition column in the AWS Glue table underlying the configured table.

   1. Edit the placeholder values in the query.

------

1. Specify the supported **Worker type** and the **Number of workers**. 

   You can choose the instance type and number of instances (workers) to run your SQL queries. 

   You can select 2 to 128 workers for CR.1X, 2 to 32 workers for CR.4X, and 2 to 16 workers for CR.8X. 

   Use the following table to determine the worker type and number of workers you need for your use case.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/use-sql-editor.html)
**Note**  
Different worker types and number of workers have associated costs. To learn more about the pricing, see [AWS Clean Rooms pricing](https://aws.amazon.com/clean-rooms/pricing/).

1. For **Send results to**, specify who can receive results. 
**Note**  
To receive results, the collaboration member must be configured as a result receiver and must be an active participant in the collaboration (**Status: Active**)

1. (Member who can query only) The **Use your default result settings** checkbox is selected by default. Keep this selected if you want to keep your default result settings.

   If you want to specify different results settings for this query, clear the **Use your default result settings** checkbox, and then choose the following. 

   1. **Result format** (**CSV** or **PARQUET**)

   1. **Result files** (**Single** or **Multiple**)

   1. **Results destination in Amazon S3**

   Each member who can receive results can specify a different **Result format**, **Result files**, and **Results destination in Amazon S3**.

1. To specify **Spark properties**:

   1. Expand **Spark properties**.

   1. Choose **Add Spark properties**.

   1. On the **Spark properties** dialog box, choose a **Property name** from the dropdown list and enter a **Value**.

   The following tables provide a definition for each property.

   For more information about Spark properties, see [Spark Properties](https://spark.apache.org/docs/latest/configuration.html#spark-properties) in the Apache Spark documentation. 
**Note**  
You can configure a maximum of 50 Spark properties. Each property value can be up to 500 characters.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/use-sql-editor.html)    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/use-sql-editor.html)

1. (Optional) For **Compute payer**, select the collaboration member who pays for query compute costs.
**Note**  
If there is only one payer candidate for query compute in the collaboration, it defaults to that payer.

1. Choose **Run**.
**Note**  
You can't run the query if the member who can receive results hasn’t configured the query results settings.

1. View the **Results**. 

   For more information, see [Receiving and using analysis results](receive-query-results.md).

1. Continue to adjust parameters and run your query again, or choose the **\+** button to start a new query in a new tab.

**Note**  
AWS Clean Rooms aims to provide clear error messaging. If an error message doesn't have enough details to help you troubleshoot, contact the account team. Provide them with a description of how the error occurred and the error message (including any identifiers). For more information, see [Troubleshooting AWS Clean Rooms](troubleshooting.md).