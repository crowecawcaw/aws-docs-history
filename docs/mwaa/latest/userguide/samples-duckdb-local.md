

# Using a DAG to run DuckDB queries in memory
<a name="samples-duckdb-local"></a>

You can use the following code example to write a directed acyclic graph (DAG) that runs DuckDB SQL in memory on your Amazon MWAA environment's workers, without reading from or writing to other AWS services.

The DAG has one task, `summarize_sales`, that uses the DuckDB query operator, `DuckDBExecuteQueryOperator`, to run a list of three SQL statements. The statements create a table, add rows to it, and return a per-store summary. The operator runs the statements in order on the same DuckDB connection and returns the result of the last statement.

**Topics**
+ [Version](#samples-duckdb-local-version)
+ [Prerequisites](#samples-duckdb-local-prereqs)
+ [Permissions](#samples-duckdb-local-permissions)
+ [Dependencies](#samples-duckdb-local-dependencies)
+ [Code example](#samples-duckdb-local-code)

## Version
<a name="samples-duckdb-local-version"></a>

You can use the code example on this page with **Apache Airflow v3.3.1** and later in Python 3.12. For information about using DuckDB in an existing Apache Airflow v3.3.1 environment, see [Version](samples-duckdb.md#samples-duckdb-version).

## Prerequisites
<a name="samples-duckdb-local-prereqs"></a>

To use the code example on this page, you need an [Amazon MWAA environment](get-started.md) using Apache Airflow v3.3.1 or later.

## Permissions
<a name="samples-duckdb-local-permissions"></a>

You don't need additional permissions to use the code example on this page. The DAG doesn't access other AWS services, so it doesn't incur charges beyond your environment's usage.

## Dependencies
<a name="samples-duckdb-local-dependencies"></a>

You don't need additional dependencies to use the code example on this page. Amazon MWAA environments that use Apache Airflow v3.3.1 or later include the DuckDB provider and the `duckdb` library.

## Code example
<a name="samples-duckdb-local-code"></a>

**To run a DuckDB query in memory**

1. Copy the following Python code example, and save it locally as `duckdb_local.py`.

   ```
   import pendulum
   
   from airflow.providers.duckdb.operators.duckdb import DuckDBExecuteQueryOperator
   from airflow.sdk import DAG
   
   with DAG(
       dag_id="duckdb_local",
       schedule=None,
       start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
       catchup=False,
   ):
       summarize_sales = DuckDBExecuteQueryOperator(
           task_id="summarize_sales",
           sql=[
               """
               CREATE TABLE sales (store_id INTEGER, quantity INTEGER, unit_price DECIMAL(10, 2))
               """,
               """
               INSERT INTO sales VALUES
                   (1, 2, 19.99), (1, 1, 5.50), (2, 4, 12.00), (2, 1, 89.00), (3, 3, 7.25)
               """,
               """
               SELECT store_id,
                      count(*) AS orders,
                      sum(quantity) AS units,
                      sum(quantity * unit_price) AS revenue
               FROM sales
               GROUP BY store_id
               ORDER BY store_id
               """,
           ],
       )
   ```

   If a SQL statement fails, the operator raises an error, and Apache Airflow marks the task as failed. The error appears in the task log. To retry failed tasks automatically, set `retries` on the task or in the DAG's `default_args`.

1. Upload `duckdb_local.py` to the `dags` folder in your environment's Amazon S3 bucket. For instructions on uploading DAGs, see [Adding or updating DAGs](configuring-dag-folder.md).

1. Open the [Amazon MWAA console](https://console.aws.amazon.com/mwaa/), and choose **Open Airflow UI** for your environment.

1. Trigger the `duckdb_local` DAG. The run might take a few minutes to complete. If the run fails, check the task log. For troubleshooting information, see [Troubleshooting DuckDB tasks](samples-duckdb.md#samples-duckdb-troubleshooting).

1. When the run completes, choose the `summarize_sales` task, and then view the query results on the **XCom** tab.

   The following table shows the expected results, with one row for each store.


<table>
<thead>
  <tr><th>store_id</th><th>orders</th><th>units</th><th>revenue</th></tr>
</thead>
<tbody>
  <tr><td>1</td><td>2</td><td>3</td><td>45.48</td></tr>
  <tr><td>2</td><td>2</td><td>5</td><td>137.00</td></tr>
  <tr><td>3</td><td>1</td><td>3</td><td>21.75</td></tr>
</tbody>
</table>


1. 

**Clean up resources**

   When you finish, pause the `duckdb_local` DAG, and delete `duckdb_local.py` from the `dags` folder in your environment's Amazon S3 bucket. You don't need to delete the `sales` table. DuckDB deletes the in-memory table when the task ends, so this example doesn't create any other resources.

**Pass data between tasks**  
Downstream tasks often need the results of earlier tasks, such as a file that an earlier task exported. Each task opens its own in-memory DuckDB database, and DuckDB discards the database when the task ends, so tasks can't share data in memory. To pass data between tasks, write it to Amazon S3, as shown in [Using a DAG to read and write Amazon S3 data with DuckDB](samples-duckdb-s3.md).