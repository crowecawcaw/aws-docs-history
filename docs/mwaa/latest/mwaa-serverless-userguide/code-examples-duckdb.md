

# Using DuckDB in Amazon MWAA Serverless workflows
<a name="code-examples-duckdb"></a>

Run DuckDB SQL in Amazon MWAA Serverless workflows with `DuckDBExecuteQueryOperator`. DuckDB is an in-process SQL engine that runs inside a workflow task, so you avoid the cost and operational overhead of running a separate database server. Use DuckDB for data checks, summaries, and transformations on CSV, JSON, and Parquet files in Amazon S3.

With Amazon MWAA Serverless, you can use DuckDB without a code package, a connection definition, or access keys. The following examples are YAML workflow definitions that you upload to Amazon S3 and run with the AWS CLI.

**Topics**
+ [Understanding how DuckDB works in Amazon MWAA Serverless](#code-examples-duckdb-how)
+ [Prerequisites](#code-examples-duckdb-prereqs)
+ [Querying data in memory with DuckDB](#code-examples-duckdb-memory)
+ [Reading and writing Amazon S3 data with DuckDB](#code-examples-duckdb-s3)
+ [Running the DuckDB examples](#code-examples-duckdb-run)
+ [Resolving DuckDB permission, file path, and table errors](#code-examples-duckdb-troubleshooting)
+ [Clean up resources](#code-examples-duckdb-cleanup)

## Understanding how DuckDB works in Amazon MWAA Serverless
<a name="code-examples-duckdb-how"></a>

The Amazon MWAA Serverless execution environment includes the DuckDB library, the Apache Airflow DuckDB provider, and the Apache Airflow Amazon provider. For information about the versions, see [Pre-installed packages](custom-code-operators.md#operators-python-bash-preinstalled).

To run DuckDB SQL, set a task's `operator` key to the following class path:

```
airflow.providers.duckdb.operators.duckdb.DuckDBExecuteQueryOperator
```

The operator takes the following task keys:
+ `sql` – A SQL statement, or a list of statements that run in order. For one statement, the operator returns the result rows. For a list, the operator returns one result for each statement.
+ (Optional) `hook_params` – DuckDB settings to apply when the task connects, such as `threads` and `memory_limit`.
+ (Optional) `conn_id` – The connection to use. The default is `duckdb_default`.

For information about all operator parameters, see [DuckDB operator reference](https://airflow.apache.org/docs/apache-airflow-providers-duckdb/stable/_api/airflow/providers/duckdb/operators/duckdb/index.html#airflow.providers.duckdb.operators.duckdb.DuckDBExecuteQueryOperator) in the Apache Airflow DuckDB provider documentation.

Amazon MWAA Serverless provides the `duckdb_default` connection to every task. This connection has the `duckdb_aws` connection type. With this connection, you can do the following:
+ Read and write Amazon S3 data with your workflow execution role credentials, without adding access keys to your SQL.
+ Run queries in an in-memory database that starts empty for each task, because the connection doesn't name a database file. To share data between tasks, write it to Amazon S3.

To change the default connection for every task, set `AIRFLOW_CONN_DUCKDB_DEFAULT` in `Environment.Variables`. For more information, see [Default connections](connections.md#connections-defaults).

## Prerequisites
<a name="code-examples-duckdb-prereqs"></a>

To run the examples on this page, you need the following:
+ An Amazon S3 bucket for your workflow definitions. For more information, see [Create an Amazon S3 bucket for Amazon MWAA Serverless](mwaas-s3-bucket.md).
+ A workflow execution role that can read your workflow definitions. For more information, see [Execution roles](get-started-execution-role.md).
+ The AWS CLI, configured with permissions to create and run Amazon MWAA Serverless workflows.

The example that reads and writes Amazon S3 data also needs permissions on your data bucket. For information about the policy, see [Reading and writing Amazon S3 data with DuckDB](#code-examples-duckdb-s3).

## Querying data in memory with DuckDB
<a name="code-examples-duckdb-memory"></a>

The following YAML workflow definition has one task that runs two statements. The first statement creates a table of 1,000 sample orders. The second statement counts the orders and units for each store. The `hook_params` key limits DuckDB to 2 threads and 512 MB of memory for this task.

Save the following YAML workflow definition as `duckdb_in_memory.yaml`:

```
duckdb_in_memory:
  default_args:
    retries: 0
  schedule: null
  tasks:
    summarize_orders:
      operator: airflow.providers.duckdb.operators.duckdb.DuckDBExecuteQueryOperator
      hook_params:
        threads: 2
        memory_limit: "512 MB"
      sql:
        - |
          CREATE TABLE orders AS
          SELECT i AS order_id,
                 (i % 10) + 1 AS store_id,
                 (i % 5) + 1 AS quantity
          FROM range(1, 1001) AS t(i)
        - |
          SELECT store_id,
                 count(*) AS orders,
                 sum(quantity) AS units
          FROM orders
          GROUP BY store_id
          ORDER BY store_id
```

This example doesn't access Amazon S3, so it needs no extra permissions. To run it, follow the steps in Running the DuckDB examples, later on this page. When the run succeeds, `RunDetail.RunState` is `SUCCESS`.

The operator returns one result for each statement. Apache Airflow stores these results in XCom. XCom is the Apache Airflow feature that tasks use to pass small amounts of data to each other. Return small results only, because XCom data counts toward a quota. For more information about quotas, see [Quotas for Amazon MWAA Serverless](mwaa-serverless-quotas.md).

## Reading and writing Amazon S3 data with DuckDB
<a name="code-examples-duckdb-s3"></a>

The following YAML workflow definition has one task that runs two statements:

1. The first statement writes 10,000 sample orders to Amazon S3 as a CSV file.

1. The second statement reads the CSV file from Amazon S3. It then writes the orders, units, and revenue for each store as a Parquet file.

**Important**  
This example stores sample data in Amazon S3, which incurs storage and request charges. To avoid ongoing charges, delete `orders.csv` and `store_sales.parquet` when you finish by running the following AWS CLI command. For all cleanup steps, see [Clean up resources](#code-examples-duckdb-cleanup).  

```
aws s3 rm s3://{{amzn-s3-demo-bucket}}/duckdb-sample/ --recursive
```

Before you run the example, add a policy to your workflow execution role. For instructions on adding a policy, see [Update an execution role](get-started-execution-role.md#execution-role-update). In the following JSON policy, replace `{{amzn-s3-demo-bucket}}` with the name of your data bucket:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DuckDBDataBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket",
        "s3:GetBucketLocation"
      ],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
    },
    {
      "Sid": "DuckDBDataObjects",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/duckdb-sample/*"
    }
  ]
}
```

If your bucket uses an AWS KMS key for encryption, the role also needs `kms:Decrypt` and `kms:GenerateDataKey` on that key.

In the following YAML workflow definition, replace `{{amzn-s3-demo-bucket}}` with the name of your data bucket. Then save the definition as `duckdb_s3.yaml`:

```
duckdb_s3:
  default_args:
    retries: 0
  schedule: null
  tasks:
    write_and_summarize_orders:
      operator: airflow.providers.duckdb.operators.duckdb.DuckDBExecuteQueryOperator
      sql:
        - |
          COPY (
              SELECT i AS order_id,
                     (i % 10) + 1 AS store_id,
                     (i % 5) + 1 AS quantity,
                     round(5 + (i % 50) * 1.5, 2) AS unit_price
              FROM range(1, 10001) AS t(i)
          ) TO 's3://{{amzn-s3-demo-bucket}}/duckdb-sample/orders.csv' (FORMAT csv, HEADER true)
        - |
          COPY (
              SELECT store_id,
                     count(*) AS orders,
                     sum(quantity) AS units,
                     round(sum(quantity * unit_price), 2) AS revenue
              FROM read_csv('s3://{{amzn-s3-demo-bucket}}/duckdb-sample/orders.csv')
              GROUP BY store_id
              ORDER BY store_id
          ) TO 's3://{{amzn-s3-demo-bucket}}/duckdb-sample/store_sales.parquet' (FORMAT parquet)
```

To run the example, follow the steps in the following section. After the run succeeds, list the output files with the following AWS CLI command:

```
aws s3 ls s3://{{amzn-s3-demo-bucket}}/duckdb-sample/
```

The output lists `orders.csv` and `store_sales.parquet`.

When you finish, delete the sample data with the following AWS CLI command. For all cleanup steps, see [Clean up resources](#code-examples-duckdb-cleanup).

```
aws s3 rm s3://{{amzn-s3-demo-bucket}}/duckdb-sample/ --recursive
```

## Running the DuckDB examples
<a name="code-examples-duckdb-run"></a>

Use the following steps to run either example. Replace `{{duckdb_s3.yaml}}` with the name of the file that you saved. Replace `{{amzn-s3-demo-bucket1}}` with the name of your workflow definitions bucket. Replace the role ARN, account ID, and `{{us-east-1}}` with your own values.

**To run a DuckDB example**

1. Open a terminal where the AWS CLI is configured with permissions to create and run Amazon MWAA Serverless workflows.

1. Upload the workflow definition to your workflow definitions bucket.

   ```
   aws s3 cp {{duckdb_s3.yaml}} s3://{{amzn-s3-demo-bucket1}}/dags/{{duckdb_s3.yaml}}
   ```

1. Create the workflow. You don't need the `--code` parameter because DuckDB is pre-installed.

   ```
   aws mwaa-serverless create-workflow \
       --name {{duckdb-s3}} \
       --definition-s3-location '{"Bucket": "{{amzn-s3-demo-bucket1}}", "ObjectKey": "dags/{{duckdb_s3.yaml}}"}' \
       --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
       --region {{us-east-1}}
   ```

   The command returns a `WorkflowArn`. Use it in the following steps.

1. Start a workflow run. The run can take a few minutes.

   ```
   aws mwaa-serverless start-workflow-run \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/duckdb-s3-a1b2c3d4e5}} \
       --region {{us-east-1}}
   ```

1. Check the run status. Replace `{{run-id}}` with the `RunId` that `start-workflow-run` returns.

   ```
   aws mwaa-serverless get-workflow-run \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/duckdb-s3-a1b2c3d4e5}} \
       --run-id {{run-id}} \
       --region {{us-east-1}}
   ```

   When `RunDetail.RunState` is `SUCCESS`, the run has finished. If the value is `FAILED`, check the task log. For information about task logs, see [Viewing task logs](custom-code-operators.md#operators-python-bash-troubleshooting-logs).

## Resolving DuckDB permission, file path, and table errors
<a name="code-examples-duckdb-troubleshooting"></a>

DuckDB tasks commonly fail because of missing Amazon S3 permissions, file paths that don't match your data, or tables that a different task created. If a DuckDB task fails, the error appears in the task log. The following list describes these errors and how to fix them:

DuckDB task fails with an HTTP 403 or access denied error from Amazon S3  
Verify that your workflow execution role has the permissions in [Reading and writing Amazon S3 data with DuckDB](#code-examples-duckdb-s3) for the bucket in your SQL. If the bucket uses an AWS KMS key, also verify the `kms:Decrypt` and `kms:GenerateDataKey` permissions.  
If you set `conn_id` or override `duckdb_default`, verify that the connection type is `duckdb_aws`. A connection with the `duckdb` connection type doesn't use your execution role credentials for Amazon S3.

DuckDB task finds no files at an Amazon S3 path  
Verify that the path in your SQL matches where you store your files. If your SQL uses a wildcard path, for example a path that ends in `*.csv`, the execution role also needs `s3:ListBucket` on the bucket.

DuckDB task reports that a table doesn't exist  
Each task starts with an empty in-memory database. Create the table in the same task that queries it, or write the data to Amazon S3 and read it in a later task.

## Clean up resources
<a name="code-examples-duckdb-cleanup"></a>

This procedure removes the workflows, workflow definitions, sample data, and permissions that you created for the examples.

**Important**  
To avoid ongoing charges, delete the resources that you created when you finish with the examples.

**To clean up resources**

1. Open a terminal where the AWS CLI is configured for the account that you used to run the examples.

1. The following AWS CLI command deletes a workflow. Run it for each workflow that you created. Replace the workflow ARN with the `WorkflowArn` that `create-workflow` returned.

   ```
   aws mwaa-serverless delete-workflow \
       --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/duckdb-s3-a1b2c3d4e5}} \
       --region {{us-east-1}}
   ```

1. The following AWS CLI commands delete the workflow definitions from your workflow definitions bucket. Replace `{{amzn-s3-demo-bucket1}}` with the name of your workflow definitions bucket.

   ```
   aws s3 rm s3://{{amzn-s3-demo-bucket1}}/dags/duckdb_in_memory.yaml
   aws s3 rm s3://{{amzn-s3-demo-bucket1}}/dags/duckdb_s3.yaml
   ```

1. The following AWS CLI command deletes the sample data from your data bucket. Replace `{{amzn-s3-demo-bucket}}` with the name of your data bucket.

   ```
   aws s3 rm s3://{{amzn-s3-demo-bucket}}/duckdb-sample/ --recursive
   ```

1. If your other workflows don't need it, remove the `DuckDBDataBucket` and `DuckDBDataObjects` policy statements from your workflow execution role.