# Analyzing SQL Server execution plans using the Performance Insights dashboard for Amazon RDS

When analyzing DB load on a SQL Server Database, you might want to know which plans are contributing the most to DB load.
You can determine which plans are contributing the most to DB load by using the plan capture feature of Performance Insights.

###### To analyze SQL Server execution plans using the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Performance Insights**.
3. Choose a SQL Server DB instance. The Performance Insights dashboard is displayed for that
   DB instance.
4. In the **Database load (DB load)** section, choose **Plans**
   next to **Slice by**.

The Average active sessions chart shows the plans used by your top SQL statements. The plan hash values appear to
the right of the color-coded squares. Each hash value uniquely identifies a plan.

![Slice by plans](images/pi-slice-by-plans-sqlserver.png) 5. Scroll down to the **Top SQL** tab.

In the following example, the top SQL digest has three plans.
The presence of a question mark in the SQL statement indicates that the statement is a digest.
To view the full SQL statement, choose a value in the **SQL statements** column.

![Choose a digest plan](images/top-sql-plans-unselected-sqlserver.png) 6. Choose the digest to expand it into its component statements.

In the following example, the `SELECT` statement is a digest query. The component queries in the digest
use three different execution plans. The colors assigned to the plans correspond to the database load chart.

![Choose a digest plan](images/pi-digest-plan-sqlserver.png) 7. Scroll down and choose two **Plans** to compare from **Plans for digest
query** list.

You can view either one or two plans for a query at a time. The following screenshot
compares two plans in the digest. In the following example, 40% of the average
active sessions running this digest query are using the plan on the left, whereas
28% are using the plan on the right.

![Compare the plans side by side](images/pi-compare-plan-sqlserver.png)

In the previous example, the plans differ in an important way. Step 2 in the plan on the left uses an table scan, whereas the plan
on the right uses a clustered index scan. For a table with a large number of rows, a query retrieving a single row is almost
always faster with a clustered index scan. 8. (Optional) Choose the **Settings** icon on the Plan Details table to customize the visibility and order of columns.
The following screenshot shows the Plan Details table with the **Output list** column as the second column.

![Customize the visibility and order of columns in the Plan Details table](images/pi-plan-fields-sql-server.png) 9. (Optional) Choose **Copy** to copy the plan to the clipboard, or **Download** to
save the plan to your hard drive.

###### Note

Performance Insights displays estimated execution plans using a hierarchical tree table.
The table includes the partial execution information for each statement.
For more information about the columns in the Plan Details table, see [SET SHOWPLAN_ALL](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-showplan-all-transact-sql "https://learn.microsoft.com/en-us/sql/t-sql/statements/set-showplan-all-transact-sql") in the SQL Server documentation.
To display the full execution information for an estimated execution plan, choose **Download** to download the plan and then upload the plan to SQL Server Management Studio.
For more information about displaying an estimated execution plan using SQL Server Management Studio, see [Display an Estimated Execution Plan](https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-the-estimated-execution-plan "https://learn.microsoft.com/en-us/sql/relational-databases/performance/display-the-estimated-execution-plan") in the SQL Server documentation.
