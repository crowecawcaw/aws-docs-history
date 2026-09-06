

# Querying with the analysis builder
<a name="query-data-analysis-builder"></a>

You can use the analysis builder to build queries without having to write SQL code. With the analysis builder, you can build a query for a collaboration that has:
+ A single table that uses the [aggregation analysis rule](analysis-rules-aggregation.md) with no JOIN required
+ Two tables (one from each member) that both use the [aggregation analysis rule](glossary.md#glossary-agg-analysis-rule)
+ Two tables (one from each member) that both use the [list analysis rule](glossary.md#glossary-list-analysis-rule)
+ Two tables (one from each member) that both use the aggregation analysis rule and two tables (one from each member) that both use the list analysis rule

If you want to manually write SQL queries, see [Querying configured tables using the SQL code editor](use-sql-editor.md).

The analysis builder appears as the **Analysis builder UI** option in the **Analysis** section of the **Analysis** tab in the AWS Clean Rooms console. 

**Important**  
If you turn on the **Analysis builder UI**, start building a query in the analysis builder, and then turn off the **Analysis builder UI**, your query isn't saved.

**Tip**  
If a scheduled maintenance occurs while a query is running, the query is terminated and rolled back. You must restart the query. 

The following topics explain how to use the analysis builder.

**Topics**
+ [Use the analysis builder to query a single table (aggregation)](#use-analysis-builder-one-table)
+ [Use the analysis builder to query two tables (aggregation or list)](#use-analysis-builder-two-tables)

## Use the analysis builder to query a single table (aggregation)
<a name="use-analysis-builder-one-table"></a>

This procedure demonstrates how to use the **Analysis builder UI** in the AWS Clean Rooms console to build a query. The query is for a collaboration that has a single table that uses the [aggregation analysis rule](analysis-rules-aggregation.md) with no JOIN required.

**To use the analysis builder to query a single table**

Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Run queries**.

1. On the **Analysis** tab, under **Tables**, view the table and its associated analysis rule type. (The analysis rule type should be the **Aggregation analysis rule**.)
**Note**  
If you don’t see the table you expect, it might be for the following reasons:  
The table hasn't been [associated](associate-configured-table.md).
The table doesn't have an [analysis rule configured](add-analysis-rule.md).

1. Under the **Analysis** section, turn on **Analysis builder UI**.

1. Build a query.

   If you want to see all of the aggregation metrics, skip to step 9.

   1. For **Choose metrics**, review the aggregate metrics that have been preselected by default and remove any metric if needed.

   1. (Optional) For **Add segments – optional**, choose one or more parameters.
**Note**  
**Add segments – optional** is only displayed if dimensions are specified for the table.

   1. (Optional) For **Add filters – optional**, choose **Add filter**, and then choose a **Parameter**, operator, and **Value**. 

      To add more filters, choose **Add another filter**. 

      To remove a filter, choose **Remove**.
**Note**  
ORDER BY isn't supported for aggregation queries.  
Only the AND operator is supported in filters.

   1. (Optional) For **Add description – optional**, enter a description to help identify the query in the list of queries.

1. Expand **Preview SQL code**.

   1. View the SQL code that's generated from the analysis builder.

   1. To copy the SQL code, choose **Copy**.

   1. To edit the SQL code, choose **Edit in SQL code editor**.

1. (Optional) For **Compute payer**, select the collaboration member who pays for query compute costs.
**Note**  
If there is only one payer candidate for query compute in the collaboration, it defaults to that payer.

1. Choose **Run**.
**Note**  
You can't run the query if the member who can receive results hasn’t configured the query results settings.

1. Continue to adjust parameters and run your query again, or choose the **\+** button to start a new query in a new tab.

**Note**  
AWS Clean Rooms aims to provide clear error messaging. If an error message doesn't have enough details to help you troubleshoot, contact the account team. Provide them with a description of how the error occurred and the error message (including any identifiers). For more information, see [Troubleshooting AWS Clean Rooms](troubleshooting.md).

## Use the analysis builder to query two tables (aggregation or list)
<a name="use-analysis-builder-two-tables"></a>

This procedure describes how to use the analysis builder in the AWS Clean Rooms console to build a query for a collaboration that has:
+ Two tables (one from each member) that both use the [aggregation analysis rule](analysis-rules-aggregation.md)
+ Two tables (one from each member) that both use the [list analysis rule](analysis-rules-list.md)
+ Two tables (one from each member) that both use the aggregation analysis rule and two tables (one from each member) that both use the list analysis rule

**To use the analysis builder to query two tables**

Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home).

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration that has **Your member abilities** status of **Run queries**..

1. On the **Analysis** tab, under **Tables**, view the two tables and their associated analysis rule type (**Aggregation analysis rule** or **List analysis rule**).
**Note**  
If you don’t see the tables you expect in the list, it might be for the following reasons:  
The tables haven't been [associated](associate-configured-table.md).
The tables don't have an [analysis rule configured](add-analysis-rule.md).

1. Under the **Analysis** section, turn on **Analysis builder UI**.

1. Build a query.

   If the collaboration contains two tables that use the **Aggregation analysis rule** and two tables that use the **List analysis rule**, first choose **Aggregation** or **List**, and then follow the prompts based on the selected analysis rule.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/query-data-analysis-builder.html)

1. Expand **Preview SQL code**.

   1. View the SQL code that's generated from the analysis builder.

   1. To copy the SQL code, choose **Copy**.

   1. To edit the SQL code, choose **Edit in SQL code editor**.

1. (Optional) For **Compute payer**, select the collaboration member who pays for query compute costs.
**Note**  
If there is only one payer candidate for query compute in the collaboration, it defaults to that payer.

1. Choose **Run**.
**Note**  
You can't run the query if the member who can receive results hasn’t configured the query results settings

1. Continue to adjust parameters and run your query again, or choose the **\+** button to start a new query in a new tab.

**Note**  
AWS Clean Rooms aims to provide clear error messaging. If an error message doesn't have enough details to help you troubleshoot, contact the account team. Provide them with a description of how the error occurred and the error message (including any identifiers). For more information, see [Troubleshooting AWS Clean Rooms](troubleshooting.md).