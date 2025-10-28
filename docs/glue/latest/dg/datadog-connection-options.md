# Datadog connection options

The following are connection options for Datadog:

- `ENTITY_NAME`(String) – (Required) Used for Read/Write. The
  name of your Object in Datadog.
- `API_VERSION`(String) – (Required) Used for Read/Write.
  Datadog Rest API version you want to use. `v1` version supports
  `metrics-timeseries` entity whereas, `v2` version
  supports `log-queries` entity.
- `INSTANCE_URL`(String) – (Required) Used for Read. Datadog instance URL. Datadog instance URL varies per region.
- `SELECTED_FIELDS`(List<String>) – Default: empty(SELECT \*). Used for Read. Columns you want to select
  for the object.
- `FILTER_PREDICATE`(String) – Default: empty. Used for Read. It should be in the Spark SQL format.
- `QUERY`(String) – Default: empty. Used for Read. Full Spark SQL query.
