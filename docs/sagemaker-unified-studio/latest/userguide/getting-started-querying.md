# Get started with the query editor in

Amazon SageMaker Unified Studio

You can use the query editor to perform analysis using SQL.
The query editor tool provides a place to write and run queries, view results,
and share your work with your team.

## Prerequisites

Before you get started with the query editor, you must access Amazon SageMaker Unified Studio
and create a project with the **SQL analytics** project profile.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.

For more information, see [Access Amazon SageMaker Unified Studio](getting-started-access-the-portal.md "getting-started-access-the-portal.md"). 2. Create a project with a **SQL analytics** project profile. This project profile sets up your project
with access to Amazon Redshift Serverless and Amazon Athena resources.
For more information, see [Create a new project](create-new-project.md "create-new-project.md").

## Query sample data using Amazon Athena in Amazon SageMaker Unified Studio

After you create a project, you can use the query editor to write and run queries.

1. Navigate to the project you created in the top center menu of the Amazon SageMaker Unified Studio home page.
2. Expand the **Build** menu in the top navigation bar, then choose **Query editor**.
3. Create a new querybook tab. A querybook is a kind of SQL notebook where you can
   draw from multiple engines to design and visualize data analytics solutions.
4. Select a data source for your queries by using the menu in the upper-right corner of the querybook.
   1. Under **Connections**, choose **Athena (Lakehouse)** to connect to your Lakehouse resources.
   2. Under **Catalogs**, choose **AwsDataCatalog**.
   3. Under **Databases**, choose the name of the AWS Glue database. This database was created for use when the project was created.

5. Choose **Choose** to connect to the database and query engine.
6. Copy the following SQL query into the querybook cell to create a table in the database.

```

CREATE TABLE mkt_sls_table AS
SELECT 146776932 AS ord_num, 23 AS sales_qty_sld, 23.4 AS wholesale_cost, 45.0 as lst_pr, 43.0 as sell_pr, 2.0 as disnt, 12 as ship_mode,13 as warehouse_id, 23 as item_id, 34 as ctlg_page, 232 as ship_cust_id, 4556 as bill_cust_id
UNION ALL SELECT 46776931, 24, 24.4, 46, 44, 1, 14, 15, 24, 35, 222, 4551
UNION ALL SELECT 46777394, 42, 43.4, 60, 50, 10, 30, 20, 27, 43, 241, 4565
UNION ALL SELECT 46777831, 33, 40.4, 51, 46, 15, 16, 26, 33, 40, 234, 4563
UNION ALL SELECT 46779160, 29, 26.4, 50, 61, 8, 31, 15, 36, 40, 242, 4562
UNION ALL SELECT 46778595, 43, 28.4, 49, 47, 7, 28, 22, 27, 43, 224, 4555
UNION ALL SELECT 46779482, 34, 33.4, 64, 44, 10, 17, 27, 43, 52, 222, 4556
UNION ALL SELECT 46779650, 39, 37.4, 51, 62, 13, 31, 25, 31, 52, 224, 4551
UNION ALL SELECT 46780524, 33, 40.4, 60, 53, 18, 32, 31, 31, 39, 232, 4563
UNION ALL SELECT 46780634, 39, 35.4, 46, 44, 16, 33, 19, 31, 52, 242, 4557
UNION ALL SELECT 46781887, 24, 30.4, 54, 62, 13, 18, 29, 24, 52, 223, 4561

```

7. Choose the **Run cell** icon.
   ![The chart icon used in the Amazon SageMaker Unified Studio query editor.](images/qev2/qev2-run.png)

When the query finishes running, a **Result** tab appears below the cell to display the outcome. 8. Refresh the **Data explorer** navigation pane, and view the table you created in the **Lakehouse** section. 9. Choose **Add SQL** to add another cell to the querybook. Then enter the following script:

```

select * from mkt_sls_table limit 10

```

10. Choose the **Run cell** icon.

In the **Results** tab, the first ten rows of the table you created are displayed. 11. Choose **Add SQL** to add another cell to the querybook. Then enter the following script:

```

select item_id, sales_qty_sld
from mkt_sls_table
where sales_qty_sld > 30

```

12. Choose the **Run cell** icon.

In the **Results** tab, only data that fulfills the specified requirements is displayed. 13. In the **Results** tab, choose the **Chart view** icon.
![The chart icon used in the Amazon SageMaker Unified Studio query editor.](images/qev2/qev2-chart.png)

This opens up a chart view with a line graph as a default. 14. Set up the chart to display a pie chart.

    1. For **Type**, choose **Pie**.
    2. For **Values**, choose **sales\_qty\_sold**.
    3. For **Labels**, choose **item\_id**.This displays a pie chart so you can visualize results.

After you've finished querying the data, you can choose to view the queries in your query history
and save them to share with other project members.

- For more information about reviewing query history, see [Review query history](query-history.md "query-history.md").
- For more information about other operations you can do with the query editor, such as using generative AI to create SQL queries,
  see [SQL analytics](sql-query.md "sql-query.md").
