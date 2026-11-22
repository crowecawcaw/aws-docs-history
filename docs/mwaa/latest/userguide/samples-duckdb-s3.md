

# Using a DAG to read and write Amazon S3 data with DuckDB

You can use the following code example to write a directed acyclic graph (DAG) that uses DuckDB to generate, check, and summarize sample order data in Amazon S3. The DAG runs on your Amazon MWAA environment's workers and reads and writes files in Amazon S3 as your environment's execution role. The DAG has three tasks:
+ `write_orders` generates a day of sample orders and writes them to Amazon S3 as a gzip-compressed CSV file, in a folder for the run's logical date.
+ `check_orders` reads the day's orders directly from Amazon S3 and counts duplicate order IDs and invalid quantities. You don't need to define a table first.
+ `summarize_orders` writes the day's orders, units, and revenue for each store to Amazon S3 as a Parquet file that you can query with other tools, such as Amazon Athena (Athena).

For more information about the SQL functions that this example uses, such as `read_csv` and `COPY`, see the [DuckDB documentation](https://duckdb.org/docs/) on the DuckDB website.

**Topics**
+ [Version](#samples-duckdb-s3-version)
+ [Prerequisites](#samples-duckdb-s3-prereqs)
+ [Permissions](#samples-duckdb-s3-permissions)
+ [Dependencies](#samples-duckdb-s3-dependencies)
+ [Code example](#samples-duckdb-s3-run)
+ [Clean up resources](#samples-duckdb-cleanup)

## Version
<a name="samples-duckdb-s3-version"></a>

You can use the code example on this page with **Apache Airflow v3.3.1** and later in Python 3.12. For information about using DuckDB in an existing Apache Airflow v3.3.1 environment, see [Version](samples-duckdb.md#samples-duckdb-version).

## Prerequisites
<a name="samples-duckdb-s3-prereqs"></a>

To use the code example on this page, you need the following:
+ An [Amazon MWAA environment](get-started.md) using Apache Airflow v3.3.1 or later.
+ An Amazon S3 bucket for your data.
+ Permission to update your environment's execution role. For more information about the execution role, see [Amazon MWAA execution role](mwaa-create-role.md).

This example uses AWS services that might incur charges, including Amazon S3 storage and request costs for the sample orders and reports that the DAG creates.

## Permissions
<a name="samples-duckdb-s3-permissions"></a>

DuckDB uses your environment's execution role to access Amazon S3. To use the code example on this page, the execution role needs `s3:GetObject`, `s3:PutObject`, `s3:ListBucket`, and `s3:GetBucketLocation` on your data bucket. If your bucket uses an AWS Key Management Service (AWS KMS) key for encryption, the execution role also needs `kms:Decrypt` and `kms:GenerateDataKey` on that key.

**To add DuckDB permissions to the execution role**

1. Open the [AWS Identity and Access Management (IAM) console](https://console.aws.amazon.com/iam/).

1. Choose your environment's execution role, and add the following permissions policy to it. Replace {{amzn-s3-demo-bucket}} with the name of the bucket that stores your data. For more information about the execution role, see [Amazon MWAA execution role](mwaa-create-role.md).

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "DuckDBData",
         "Effect": "Allow",
         "Action": [
           "s3:GetObject",
           "s3:PutObject",
           "s3:ListBucket",
           "s3:GetBucketLocation"
         ],
         "Resource": [
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}",
           "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
         ]
       }
     ]
   }
   ```

   DuckDB needs `s3:ListBucket` to expand wildcard paths, such as `orders/*/*.csv.gz`. If your DAGs only read data, you can remove `s3:PutObject`.

   If the execution role is missing a required permission, the task fails with an HTTP 403 or access denied error. For more information, see [Troubleshooting DuckDB tasks](samples-duckdb.md#samples-duckdb-troubleshooting).

## Dependencies
<a name="samples-duckdb-s3-dependencies"></a>

You don't need additional dependencies to use the code example on this page. Amazon MWAA environments that use Apache Airflow v3.3.1 or later include the DuckDB provider, the `duckdb` library, and the DuckDB extensions for Amazon S3 access.

## Code example
<a name="samples-duckdb-s3-run"></a>

**To run the DuckDB Amazon S3 code example**
**Important**  
This example stores sample data in Amazon S3, so you incur charges for Amazon S3 storage and requests. The sample data is smaller than 1 MB for each DAG run. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/). To avoid ongoing charges, follow the steps in [Clean up resources](#samples-duckdb-cleanup) when you finish.

1. Copy the following Python code example, and save it locally as `duckdb_s3.py`. Replace {{amzn-s3-demo-bucket}} with the name of your bucket.

   ```python
   import pendulum
   
   from airflow.providers.duckdb.operators.duckdb import DuckDBExecuteQueryOperator
   from airflow.sdk import DAG
   
   DATA = "s3://{{amzn-s3-demo-bucket}}/duckdb-sample"
   
   with DAG(
       dag_id="duckdb_s3",
       schedule=None,
       start_date=pendulum.datetime(2026, 1, 1, tz="UTC"),
       catchup=False,
   ):
       # Generate 10,000 sample orders and write them to S3 as gzip-compressed CSV.
       write_orders = DuckDBExecuteQueryOperator(
           task_id="write_orders",
           sql=f"""
               COPY (
                   SELECT i AS order_id,
                          (i % 10) + 1 AS store_id,
                          (i % 5) + 1 AS quantity,
                          round(5 + (i % 50) * 1.5, 2) AS unit_price
                   FROM range(1, 10001) AS t(i)
               ) TO '{DATA}/orders/order_date={{{{ ds }}}}/orders.csv.gz'
                 (FORMAT csv, HEADER true, COMPRESSION gzip)
           """,
       )
   
       # Read the day's orders directly from S3 and check them.
       check_orders = DuckDBExecuteQueryOperator(
           task_id="check_orders",
           sql=f"""
               SELECT count(*) AS orders,
                      count(*) - count(DISTINCT order_id) AS duplicate_order_ids,
                      count(*) FILTER (WHERE quantity <= 0) AS non_positive_quantities
               FROM read_csv('{DATA}/orders/*/*.csv.gz', hive_partitioning = true)
               WHERE order_date = DATE '{{{{ ds }}}}'
           """,
       )
   
       # Write a per-store summary of the day's orders to S3 as Parquet.
       summarize_orders = DuckDBExecuteQueryOperator(
           task_id="summarize_orders",
           sql=f"""
               COPY (
                   SELECT store_id,
                          count(*) AS orders,
                          sum(quantity) AS units,
                          round(sum(quantity * unit_price), 2) AS revenue
                   FROM read_csv('{DATA}/orders/*/*.csv.gz', hive_partitioning = true)
                   WHERE order_date = DATE '{{{{ ds }}}}'
                   GROUP BY store_id
                   ORDER BY store_id
               ) TO '{DATA}/reports/daily_store_sales/order_date={{{{ ds }}}}/sales.parquet'
                 (FORMAT parquet)
           """,
       )
   
       write_orders >> check_orders >> summarize_orders
   ```

   The SQL uses a Python f-string, so the doubled braces (`{{{{ ds }}}}`) render as the Apache Airflow template `{{ ds }}`. Apache Airflow replaces this template with the run's logical date. With `hive_partitioning = true`, DuckDB reads the `order_date` column from the folder names.

   If a query fails, for example because of a missing permission or file, the operator raises an error, and Apache Airflow marks the task as failed. The error appears in the task log, and downstream tasks don't run. To retry failed tasks automatically, set `retries` on the task or in the DAG's `default_args`.

1. Upload `duckdb_s3.py` to the `dags` folder in your environment's Amazon S3 bucket.

1. Open the [Amazon MWAA console](https://console.aws.amazon.com/mwaa/), and choose **Open Airflow UI** for your environment.

1. Trigger the `duckdb_s3` DAG. The run might take a few minutes to complete. If the run fails, check the task log. For troubleshooting information, see [Troubleshooting DuckDB tasks](samples-duckdb.md#samples-duckdb-troubleshooting).

1. Verify the results in the Apache Airflow UI after the run completes.

   1. Choose the `check_orders` task, and then on the **XCom** tab, view the results. The results show 10,000 orders, with no duplicate order IDs and no invalid quantities.

   1. In your data bucket, open the `duckdb-sample/reports/daily_store_sales/` folder, and confirm that it contains the Parquet file that the `summarize_orders` task wrote.

1. 

**Clean up resources**

   When you finish, pause the `duckdb_s3` DAG, delete `duckdb_s3.py` from your `dags` folder, and delete the `duckdb-sample/` folder from your data bucket. If your other DAGs don't need them, remove the `DuckDBData` permissions from the execution role. For detailed steps, see [Clean up resources](#samples-duckdb-cleanup).

## Clean up resources
<a name="samples-duckdb-cleanup"></a>

When you finish with this example, delete the resources that you created to avoid unwanted DAG runs and ongoing Amazon S3 charges. To complete these steps, you need access to your environment's Amazon S3 bucket, your data bucket, and the execution role. For more information about the DAGs folder, see [Adding or updating DAGs](configuring-dag-folder.md).

**To clean up resources**

1. Open the [Amazon MWAA console](https://console.aws.amazon.com/mwaa/), and choose **Open Airflow UI** for your environment.

1. Pause the `duckdb_s3` DAG.

1. Delete `duckdb_s3.py` from the `dags` folder in your environment's Amazon S3 bucket.

1. Delete the `duckdb-sample/` folder, which contains the sample orders and reports, from your data bucket.

1. If your other DAGs don't need them, remove the Amazon S3 permissions that you added to your environment's execution role.