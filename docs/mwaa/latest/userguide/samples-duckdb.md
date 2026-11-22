

# Using DuckDB with Amazon MWAA

Amazon Managed Workflows for Apache Airflow (Amazon MWAA) environments that use Apache Airflow v3.3.1 and later include native DuckDB support. With DuckDB, the tasks in your directed acyclic graphs (DAGs) can run SQL without installing packages, creating connections, or managing credentials. DuckDB is an in-process SQL engine that runs inside an Apache Airflow task on your environment's workers, so you don't need a separate database server or cluster. Use DuckDB for checks, summaries, and transformations on data that your pipelines produce, such as CSV, JSON, and Parquet files in Amazon S3.

This topic describes how DuckDB works in an Amazon MWAA environment. The following code examples show how to write DAGs that run DuckDB queries in memory, and that read and write data in Amazon S3. Each code example includes its own prerequisites, permissions, and cleanup steps.

**Topics**
+ [Version](#samples-duckdb-version)
+ [Prerequisites](#samples-duckdb-prereqs)
+ [How DuckDB connects in Amazon MWAA](#samples-duckdb-how)
+ [Using DuckDB with Apache Airflow v2.11 through v3.2](#samples-duckdb-earlier-versions)
+ [Customize DuckDB in your environment](#samples-duckdb-customize)
+ [Troubleshooting DuckDB tasks](#samples-duckdb-troubleshooting)
+ [Next steps](#samples-duckdb-next-steps)
+ [Related resources](#samples-duckdb-resources)
+ [Using a DAG to run DuckDB queries in memory](samples-duckdb-local.md)
+ [Using a DAG to read and write Amazon S3 data with DuckDB](samples-duckdb-s3.md)

## Version
<a name="samples-duckdb-version"></a>

Native DuckDB support is available in Amazon MWAA environments that use **Apache Airflow v3.3.1** and later. Earlier Apache Airflow versions don't include the DuckDB provider. To use DuckDB with an earlier version, see [Using DuckDB with Apache Airflow v2.11 through v3.2](#samples-duckdb-earlier-versions). You can use the code examples on this page with Apache Airflow v3.3.1 in Python 3.12.

If your Apache Airflow v3.3.1 environment was created before DuckDB support was available, update your environment to apply the latest Amazon MWAA image. Don't change any environment settings. The update can take some time to complete.

## Prerequisites
<a name="samples-duckdb-prereqs"></a>

To use the code examples for DuckDB, you need an [Amazon MWAA environment](get-started.md) using Apache Airflow v3.3.1 or later. Each example lists any additional prerequisites, such as Amazon S3 permissions.

## How DuckDB connects in Amazon MWAA
<a name="samples-duckdb-how"></a>

Amazon MWAA environments that use Apache Airflow v3.3.1 or later include DuckDB by default, so you don't need to add packages to your `requirements.txt` file. The current Apache Airflow v3.3.1 image includes DuckDB version 2.0.0, version 0.2.0 of the Apache Airflow DuckDB provider, and version 9.38.0 of the Apache Airflow Amazon provider (`apache-airflow-providers-amazon`). The Amazon provider adds the `duckdb_aws` connection type that the `duckdb_default` connection uses. This connection type requires version 9.38.0 or later of the Amazon provider. To check the DuckDB version that your tasks use, run `SELECT version();` in a DuckDB task.

When a DuckDB task doesn't name a connection, the DuckDB query operator, `DuckDBExecuteQueryOperator`, uses the `duckdb_default` connection. Amazon MWAA creates this connection for you when you create or update your environment. With this connection, DuckDB does the following:
+ Reads and writes Amazon S3 data as your environment's execution role, the same IAM role that your other tasks use. You don't need to add access keys to Apache Airflow or to your SQL.
+ Uses the Amazon S3 support that's included in the Amazon MWAA image, so your environment doesn't need internet access to download it. This applies only to the default DuckDB version. If you install a different DuckDB version, DuckDB downloads its Amazon S3 support the first time a task uses it, even if your tasks use the `duckdb_default` connection. For more information, see [Customize DuckDB in your environment](#samples-duckdb-customize).
+ Runs in memory, so each task starts with an empty database. To share data between tasks, write it to Amazon S3.

The `duckdb_default` connection appears in the Apache Airflow UI under **Admin**, **Connections**. You can edit or delete it.

Amazon MWAA doesn't overwrite an existing `duckdb_default` connection. If you delete the connection, Amazon MWAA creates it again the next time you update your environment. For more information about connections, see [Managing connections to Apache Airflow](manage-connections.md).

## Using DuckDB with Apache Airflow v2.11 through v3.2
<a name="samples-duckdb-earlier-versions"></a>

Amazon MWAA environments that use Apache Airflow v3.2 or earlier don't include DuckDB, and Amazon MWAA doesn't create the `duckdb_default` connection for them. You can add DuckDB to environments that use Apache Airflow v2.11 through v3.2. The Apache Airflow DuckDB provider requires Apache Airflow v2.11 or later, so you can't use it with Apache Airflow v2.10 or earlier. To use DuckDB in an environment that uses Apache Airflow v2.11 through v3.2, do the following:

1. Add `apache-airflow-providers-duckdb` and `duckdb` to your `requirements.txt` file. Choose versions that support your Apache Airflow version. For more information about `requirements.txt`, see [Installing Python dependencies](working-dags-dependencies.md).

1. To read and write Amazon S3 data, set up Amazon S3 access in your SQL before your queries. The following statements load the DuckDB extensions for Amazon S3 and use your environment's execution role for credentials.

   ```sql
   INSTALL httpfs;
   LOAD httpfs;
   INSTALL aws;
   LOAD aws;
   CREATE SECRET (TYPE s3, PROVIDER credential_chain);
   ```

DuckDB downloads these extensions from `extensions.duckdb.org` the first time a task uses them. If your environment doesn't have internet access, provide the extensions yourself, as described in [Customize DuckDB in your environment](#samples-duckdb-customize).

## Customize DuckDB in your environment
<a name="samples-duckdb-customize"></a>

You can change how DuckDB works in your environment in the following ways:
+ **Use a different AWS identity for some tasks** – Create a connection with the `duckdb_aws` connection type, and pass its ID to the operator as `conn_id`. In the connection's `extra` field, set `aws_conn_id` to an AWS connection, such as one that assumes a role in another account.
+ **Change the default connection** – Edit `duckdb_default` in the Apache Airflow UI. For example, set DuckDB options such as `memory_limit` or `threads` in the connection's `extra` field.
+ **Use a different DuckDB or provider version** – Add the version that you want to your `requirements.txt` file. If you change the version of the Amazon provider, `apache-airflow-providers-amazon`, use version 9.38.0 or later. Earlier versions don't include the `duckdb_aws` connection type that the `duckdb_default` connection uses. If your environment doesn't have internet access, also provide the matching DuckDB extensions. DuckDB looks for extensions in a folder for each DuckDB version and platform, `~/.duckdb/extensions/{{version}}/{{platform}}/`. For example, for DuckDB 1.5.6, use a [startup script](using-startup-script.md) to copy `httpfs.duckdb_extension` and `aws.duckdb_extension` from Amazon S3 to `~/.duckdb/extensions/v1.5.6/linux_amd64/`. For more information about `requirements.txt`, see [Installing Python dependencies](working-dags-dependencies.md).

**Note**  
The Amazon MWAA image includes DuckDB extensions that match the default DuckDB version. If you install a different version, DuckDB downloads matching extensions from `extensions.duckdb.org` the first time a task uses them. This download might add time to the first task run.

## Troubleshooting DuckDB tasks
<a name="samples-duckdb-troubleshooting"></a>

If a DuckDB task fails, check the task's log in the Apache Airflow UI for missing permissions, incorrect paths, missing extensions, or memory limits. The following entries describe how to resolve each of these common causes, so that your DAGs can complete successfully.

Resolve HTTP 403 or access denied errors from Amazon S3  
Verify that your environment's execution role has the permissions in [Permissions](samples-duckdb-s3.md#samples-duckdb-s3-permissions) for the Amazon S3 code example for the bucket and prefix in your SQL. If the bucket uses AWS KMS keys for encryption, also verify the AWS KMS permissions.  
If the role has the required permissions, verify that the task uses a connection with the `duckdb_aws` connection type. A connection with the `duckdb` connection type doesn't create a secret for Amazon S3 access, so Amazon S3 denies the request. Check the connection that you pass as `conn_id`, or the `duckdb_default` connection if the task doesn't specify one.  
The `duckdb_aws` connection type requires version 9.38.0 or later of the Amazon provider, `apache-airflow-providers-amazon`. If your `requirements.txt` file installs an earlier version, remove that requirement or change it to version 9.38.0 or later.

Fix wildcard paths that find no files  
Verify that the execution role has `s3:ListBucket` on the bucket. DuckDB lists the objects in your bucket to expand paths such as `orders/*/*.csv.gz`. Also verify that the path in your SQL matches where you store your files. If an earlier task writes the files, verify that the earlier task succeeded.

Resolve DuckDB extension installation or loading failures  
Check whether you installed a DuckDB version other than the default one, DuckDB 2.0.0, in your `requirements.txt` file. If your environment doesn't have internet access, DuckDB can't download extensions for that version. Remove the version from your `requirements.txt` file to use the default version and the extensions in the Amazon MWAA image. Alternatively, provide the extensions yourself as described in [Customize DuckDB in your environment](#samples-duckdb-customize).

Reduce memory use for DuckDB tasks  
Reduce the data that each query reads, because DuckDB runs on the worker and shares its memory with other tasks. For example, filter on a partition column such as `order_date`. You can also set `memory_limit` in the connection's `extra` field, or use a larger [Configuring the Amazon MWAA environment class](environment-class.md). For queries over large datasets, consider using Athena instead.

## Next steps
<a name="samples-duckdb-next-steps"></a>
+ Run DuckDB tasks when another DAG updates your data, without changing that DAG. To do this, add an `outlets` asset to the task that writes the data. Then use that asset as the `schedule` for your DuckDB DAG. For more information, see [Asset-aware scheduling](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/asset-scheduling.html) in the Apache Airflow documentation.
+ Query JSON and Parquet files in Amazon S3 by using the DuckDB `read_json` and `read_parquet` functions in your DAGs.
+ Share results with other teams and BI tools by querying the Parquet files that DuckDB writes to Amazon S3 with Athena.

## Related resources
<a name="samples-duckdb-resources"></a>
+ [DuckDB documentation](https://duckdb.org/docs/) on the DuckDB website
+ [What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) in the *Amazon Athena User Guide*
+ [Amazon MWAA execution role](mwaa-create-role.md)