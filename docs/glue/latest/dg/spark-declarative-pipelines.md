

# Spark Declarative Pipelines
<a name="spark-declarative-pipelines"></a>

Spark Declarative Pipelines (SDP) is a declarative framework for building batch and streaming data pipelines in AWS Glue 6.0. With SDP, you define what your data should look like using SQL or Python, and the framework automatically determines the execution plan, resolves dependencies between datasets, and runs independent branches in parallel.

SDP simplifies pipeline development by eliminating imperative boilerplate code for reading, writing, catalog registration, and execution ordering. You focus on business transformations while the framework handles the pipeline infrastructure.

SDP is available in AWS Glue version 6.0 and later.

## SDP concepts
<a name="spark-declarative-pipelines-concepts"></a>

A pipeline consists of a YAML manifest file (`spark-pipeline.yml`) and one or more SQL or Python transformation files. SDP automatically:
+ Resolves dependencies by inferring the DAG from table references
+ Determines execution order without manual orchestration
+ Runs independent branches in parallel for maximum throughput
+ Manages incremental state for streaming tables through checkpoints
+ Registers output tables in the catalog upon materialization

### Dataset types
<a name="spark-declarative-pipelines-dataset-types"></a>

Three dataset types are available in SDP:

Streaming table  
Processes only new data since the last run. Maintains state across job executions using checkpoints. Use streaming tables for ingestion, event streams, IoT data, change data capture, and append-only sources.

Materialized view  
Fully recomputes the dataset on every run. The output always reflects the current state of source data. Use materialized views for aggregations, joins, summary analytics, and reports.

Temporary view  
Session-scoped and not persisted or cataloged. Use temporary views for intermediate transformations and staging logic.

**Important**  
Materialized views always perform a full recompute in the current version. They do not support incremental refresh. Use streaming tables for incremental workloads.

## Prerequisites
<a name="spark-declarative-pipelines-prerequisites"></a>

To use SDP, you need the following:
+ AWS Glue version 6.0
+ An Amazon S3 location for pipeline storage (checkpoints, metadata)
+ For Data Catalog integration (optional): set `--enable-glue-datacatalog` to `true`. Alternatively, you can configure catalog settings directly through Spark configuration.
+ For persistent table storage: either set `spark.sql.warehouse.dir` to an Amazon S3 path, or set the `database:` field in the pipeline YAML and ensure the AWS Glue database has a `LocationUri` configured to an Amazon S3 path
+ For cross-run incremental processing with streaming tables, a streaming table's data and checkpoint state must persist on Amazon S3. For example, Hive or AWS Glue-managed (non-Iceberg) tables require the database `LocationUri` to be set to an Amazon S3 path, while Apache Iceberg tables manage their table metadata themselves.

**Important**  
If you use the `database:` field in your pipeline YAML for Hive or AWS Glue-managed (non-Iceberg) tables, the corresponding AWS Glue database must have its `LocationUri` set to an Amazon S3 path. The `LocationUri` is what places managed streaming tables (and their `_spark_metadata` log) on Amazon S3, which is what enables persistent, cross-run incremental processing for those tables. Iceberg tables that use the Data Catalog with `catalog-impl=GlueCatalog` (Option 1) do not require a database `LocationUri`. Create or update the database with an explicit Amazon S3 location:  

```
aws glue create-database --database-input '{
  "Name":"my_pipeline_db",
  "LocationUri":"s3://my-bucket/warehouse/my_pipeline_db"
}'
```

## Creating a pipeline
<a name="spark-declarative-pipelines-creating"></a>

To create an SDP pipeline, complete the following steps.

### Step 1: Create the pipeline YAML
<a name="spark-declarative-pipelines-step1-yaml"></a>

Create a file named `spark-pipeline.yml`:

```
name: my_analytics_pipeline
catalog: spark_catalog
database: analytics_db
storage: s3://my-bucket/pipeline-storage/
libraries:
  - glob:
      include: transformations/**
configuration:
  spark.sql.shuffle.partitions: "4"
```

The following table describes the pipeline YAML fields.


| Field | Required | Description | 
| --- | --- | --- | 
| name | Yes | A name for your pipeline. | 
| catalog | No | The catalog to use. Defaults to spark\_catalog. | 
| database | No | The AWS Glue database for output tables. For LocationUri requirements, see [Prerequisites](#spark-declarative-pipelines-prerequisites). | 
| storage | Yes | An Amazon S3 path for pipeline checkpoints and metadata. | 
| libraries | Yes | Glob patterns for transformation files to include. | 
| configuration | No | Spark configuration properties. | 

### Step 2: Write transformations
<a name="spark-declarative-pipelines-step2-transformations"></a>

Create transformation files in a `transformations/` directory. You can use SQL, Python, or both in the same pipeline.

**SQL example** (`transformations/silver.sql`):

```
CREATE MATERIALIZED VIEW silver_sales AS
SELECT *, UPPER(region) as clean_region
FROM bronze_sales
WHERE amount > 0;

CREATE MATERIALIZED VIEW gold_summary AS
SELECT clean_region, COUNT(*) as order_count, SUM(amount) as total_revenue
FROM silver_sales
GROUP BY clean_region;
```

**Python example** (`transformations/bronze.py`):

```
from pyspark import pipelines as dp
from pyspark.sql import DataFrame, SparkSession

spark = SparkSession.active()

@dp.materialized_view(comment="Raw sales data from S3")
def bronze_sales() -> DataFrame:
    return spark.read.format("csv").option("header", "true") \
        .option("inferSchema", "true") \
        .load("s3://source-bucket/raw-data/sales/")
```

**Python streaming table example** (`transformations/events.py`):

```
from pyspark import pipelines as dp
from pyspark.sql import DataFrame, SparkSession

spark = SparkSession.active()

dp.create_streaming_table(
    "streaming_events",
    comment="Incremental event ingestion",
    schema="event_id STRING, event_type STRING, timestamp LONG, payload STRING"
)

@dp.append_flow(target="streaming_events")
def ingest_events() -> DataFrame:
    return (
        spark.readStream.format("json")
        .schema("event_id STRING, event_type STRING, timestamp LONG, payload STRING")
        .load("s3://source-bucket/events/")
    )
```

**Note**  
For streaming tables in Python, use `dp.create_streaming_table()` combined with `@dp.append_flow(target=...)`.

### Step 3: Upload to Amazon S3
<a name="spark-declarative-pipelines-step3-upload"></a>

Upload your pipeline files to Amazon S3 as either:
+ A `.zip` file containing `spark-pipeline.yml` and the `transformations/` directory
+ An Amazon S3 prefix (directory) containing the same structure

### Step 4: Create and run the AWS Glue job
<a name="spark-declarative-pipelines-step4-create-job"></a>

Create a AWS Glue job with the following parameters:
+ `--enable-spark-declarative-pipeline`: `true` (required; activates SDP mode)
+ `ScriptLocation`: pipeline definition zip or an Amazon S3 prefix (required for SDP pipeline)
+ `--enable-glue-datacatalog`: `true` (optional; registers tables in Data Catalog)

The following example creates an SDP job using the AWS CLI:

```
aws glue create-job \
  --name my-sdp-pipeline \
  --role arn:aws:iam::123456789012:role/MyGlueRole \
  --glue-version 6.0 \
  --worker-type G.1X --number-of-workers 2 \
  --command '{"Name":"glueetl","ScriptLocation":"s3://my-bucket/pipelines/my_pipeline.zip"}' \
  --default-arguments '{
      "--enable-spark-declarative-pipeline": "true",
      "--enable-glue-datacatalog": "true"
  }'
```

## Running pipelines
<a name="spark-declarative-pipelines-running"></a>

You run SDP pipelines using `StartJobRun`. You can control execution behavior with job arguments passed at run time.

### Run modes
<a name="spark-declarative-pipelines-run-modes"></a>

Pass the following arguments to `StartJobRun` to control pipeline execution:

`--conf spark.glue.sdp.jobMode`  
Controls the execution mode:  
+ `RUN` (default): Executes the pipeline normally.
+ `VALIDATE`: Performs a dry run that checks YAML syntax, dependency resolution, and SQL/Python compilation without writing any data.

`--conf spark.glue.sdp.runMode`  
Controls which datasets are refreshed:    
Default (no run-mode flag)  
Runs all datasets. Materialized views fully recompute; streaming tables process only new data since the last checkpoint.  
`--refresh <dataset>`  
Refreshes only the specified dataset. Streaming tables process new data incrementally; materialized views fully recompute.  
`--full-refresh <dataset>`  
Resets and recomputes only the specified dataset. For streaming tables, this resets the checkpoint and reprocesses all data.  
`--full-refresh-all`  
Resets and recomputes all datasets.

## Using Iceberg tables with SDP
<a name="spark-declarative-pipelines-iceberg"></a>

Apache Iceberg is the recommended table format for streaming tables that require durable, cross-run incremental processing, because it does not depend on the file-based `_spark_metadata` log used by Hive or AWS Glue-managed tables. You can configure Iceberg with SDP in two ways, depending on whether you want your output tables registered in the Data Catalog.

### Option 1: Iceberg with the Data Catalog (recommended)
<a name="spark-declarative-pipelines-iceberg-glue-catalog"></a>

Use this option when you want your Iceberg tables registered in the Data Catalog (with `table_type=ICEBERG`) so that they are queryable from other engines such as , Amazon Redshift, and Amazon EMR. Table data and metadata are stored in Amazon S3, and cross-run incremental state is preserved. Add the following to the `configuration` section of your `spark-pipeline.yml`:

```
configuration:
  spark.sql.catalog.glue_catalog: "org.apache.iceberg.spark.SparkCatalog"
  spark.sql.catalog.glue_catalog.catalog-impl: "org.apache.iceberg.aws.glue.GlueCatalog"
  spark.sql.catalog.glue_catalog.io-impl: "org.apache.iceberg.aws.s3.S3FileIO"
  spark.sql.catalog.glue_catalog.warehouse: "s3://my-bucket/iceberg-warehouse"
```

In your pipeline YAML, set `catalog: glue_catalog` and set `database:` to a AWS Glue database. When you create the AWS Glue job, set `--enable-spark-declarative-pipeline` to `true`. Do not set `--enable-glue-datacatalog` for Iceberg tables.

**Note**  
The Iceberg catalog uses its own `warehouse` location for table data and metadata. When you use this option, you do not need to set `spark.sql.warehouse.dir` or a database `LocationUri` for the Iceberg tables themselves.

### Option 2: Iceberg with a file-based (Hadoop) catalog
<a name="spark-declarative-pipelines-iceberg-hadoop-catalog"></a>

Use this option when you do not need Data Catalog registration. Iceberg metadata is file-based in Amazon S3, and the tables are **not** registered in the Data Catalog. Add the following to the `configuration` section of your `spark-pipeline.yml`:

```
configuration:
  spark.sql.catalog.spark_catalog: "org.apache.iceberg.spark.SparkSessionCatalog"
  spark.sql.catalog.spark_catalog.type: "hadoop"
  spark.sql.catalog.spark_catalog.warehouse: "s3://my-bucket/iceberg-warehouse"
```

**Note**  
Note the following about this option:  
Tables created with this option are not registered in the Data Catalog, so they are not queryable from query engines such as .
This option uses its own `warehouse` location for table storage.

Use Option 1 if you need your tables registered in the Data Catalog and queryable from other engines. Use Option 2 only if you do not need Data Catalog registration.

**Note**  
The `--enable-glue-datacatalog` job parameter wires the Spark Hive metastore to the Data Catalog for Hive (non-Iceberg) tables. For Iceberg tables, `catalog-impl=GlueCatalog` registers tables directly in the Data Catalog through the AWS SDK, so you do not set `--enable-glue-datacatalog` for Iceberg. Do not configure Iceberg with the default `SparkSessionCatalog` (`type: hive`) together with `--enable-glue-datacatalog` in an attempt to register Iceberg tables in the Data Catalog: on AWS Glue 6.0, this combination fails.

With Iceberg configured, you get the following benefits:
+ Streaming tables maintain checkpoint state in Amazon S3 across job runs
+ Each run creates new data files and Iceberg snapshots
+ Subsequent runs resume from the last committed offset
+ Full table history is preserved through Iceberg's snapshot mechanism

You can also read incrementally from an Iceberg table as a streaming source. In a medallion architecture, a downstream streaming table can consume only the new rows that are committed to an upstream Iceberg table on each run. The following example reads incrementally from an Iceberg `bronze` table into a `silver` streaming table:

```
from pyspark import pipelines as dp
from pyspark.sql import SparkSession

spark = SparkSession.active()

dp.create_streaming_table(
    "silver",
    comment="Incremental silver layer built from the bronze Iceberg table"
)

@dp.append_flow(target="silver")
def from_bronze():
    # Incremental read from the Iceberg bronze table; each run processes only new rows.
    return spark.readStream.table("bronze")
```

## Considerations and limitations
<a name="spark-declarative-pipelines-considerations"></a>

Consider the following when you use SDP:
+ **Materialized views always fully recompute**. Incremental refresh is not supported. Use streaming tables for incremental workloads.
+ **Streaming table Python API**. Use `dp.create_streaming_table()` with `@dp.append_flow(target=...)`.
+ **Cross-run incremental processing for streaming tables**. Streaming tables support cross-run incremental processing only when their data and checkpoint state persist on Amazon S3. Hive or AWS Glue-managed (non-Iceberg) tables require the database `LocationUri` to be set to an Amazon S3 path, while Apache Iceberg tables manage their table metadata themselves.
+ **Database LocationUri required for Hive or AWS Glue-managed (non-Iceberg) tables**. Iceberg tables that use the Data Catalog with `catalog-impl=GlueCatalog` do not require one. For details, see [Prerequisites](#spark-declarative-pipelines-prerequisites).
+ **Data quality expectations**. Inline data quality annotations are not supported in the current SDP framework.
+ **Avoid `withColumn` in downstream query functions**. When a downstream dataset (such as a materialized view) reads from an upstream pipeline dataset using `spark.table(...)` and applies `.withColumn(...)`, SDP might fail to detect the dependency between the datasets on the second and subsequent runs. This causes the downstream to read stale data from the previous run (one-run lag). To avoid this issue, express derived columns inside `.select(...)` instead of using `.withColumn(...)`. Also avoid any operation that forces plan resolution (such as `.schema` or `.collect`) inside query functions.
+ **No migration tooling**. Automated migration from other pipeline frameworks is not supported. Migrate tables incrementally; SDP can read from existing catalog tables.
+ **Scheduling**. SDP jobs use the same scheduling mechanisms as other AWS Glue jobs (AWS Glue Triggers, Amazon EventBridge, Apache Airflow).

## Migrating from imperative scripts to SDP
<a name="spark-declarative-pipelines-migrating"></a>

You can migrate existing imperative Spark scripts to SDP incrementally:

1. Start with one table by converting a single `spark.sql(...).write.saveAsTable(...)` call into a `CREATE MATERIALIZED VIEW` SQL statement.

1. Add tables incrementally. SDP handles mixed dependencies. SDP tables can read from existing catalog tables that are not part of the pipeline.

1. Run both patterns in parallel during transition. SDP jobs and imperative jobs can coexist.

SDP can reference any table accessible through the SparkSession, including existing Data Catalog tables, external tables, and cross-database references.