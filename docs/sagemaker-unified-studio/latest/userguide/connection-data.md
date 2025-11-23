# Connection data

To retrieve all properties of a `Connection`, you can access the
`data` field to get a `ConnectionData` object.
`ConnectionData` fields can be accessed using the dot notation
(e.g. `conn_data.top_level_field`). For retrieving further nested
data within `ConnectionData`, you can access it as a dictionary. For
example: `conn_data.top_level_field["nested_field"]`.

```

conn_data: ConnectionData = proj_redshift_conn.data
red_temp_dir = conn_data.redshiftTempDir
lineage_sync = conn_data.lineageSync
lineage_job_id = lineage_sync["lineageJobId"]
spark_conn = proj.connection("my_spark_glue_connection_name")
id = spark_conn.id
env_id = spark_conn.environment_id
glue_conn = spark_conn.data.glue_connection_name
workers = spark_conn.data.number_of_workers
glue_version = spark_conn.data.glue_version
# Fetching tracking server ARN and tracking server name from an MLFlow connection
ml_flow_conn = proj.connection('<my_ml_flow_connection_name>')
tracking_server_arn = ml_flow_conn.data.tracking_server_arn
tracking_server_name = ml_flow_conn.data.tracking_server_name

```
