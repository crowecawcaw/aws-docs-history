

# Data formats and type mapping
<a name="aurora-analytics-type-mapping"></a>

When you create a foreign table, the extension maps data types from Parquet or Iceberg to PostgreSQL data types. This section describes how Aurora PostgreSQL performs type mapping and which PostgreSQL data types are supported.

**Topics**
+ [Automatic data type mapping](#aurora-analytics-type-mapping-automatic)
+ [Types not supported for automatic schema inference](#aurora-analytics-type-mapping-unsupported-inference)
+ [Data types for foreign table columns](#aurora-analytics-type-mapping-column-types)

## Automatic data type mapping
<a name="aurora-analytics-type-mapping-automatic"></a>

When you create a foreign table without specifying column definitions (using empty parentheses), Aurora PostgreSQL automatically infers column names and data types from the remote data source.

The following table shows how source types that exist in both Parquet and Iceberg are inferred.


**Type inference for Parquet and Iceberg source types**  

| Parquet type | Iceberg type | PostgreSQL type | 
| --- | --- | --- | 
| BOOLEAN | boolean | boolean | 
| INT32 | int | integer | 
| INT64 | long | bigint | 
| FLOAT | float | real | 
| DOUBLE | double | double precision | 
| DECIMAL(p,s) | decimal(p,s) | numeric(p,s) | 
| BYTE\_ARRAY | binary | bytea | 
| FIXED\_LEN\_BYTE\_ARRAY | fixed(L) | bytea | 
| STRING (UTF-8) | string | text | 
| UUID | uuid | uuid | 
| DATE | date | date | 
| TIME (millis/micros, isAdjustedToUTC = false) | time | time | 
| TIMESTAMP (micros/millis, isAdjustedToUTC = false) | timestamp | timestamp | 
| TIMESTAMP (nanos, isAdjustedToUTC = false) | timestamp\_ns | timestamp | 
| TIMESTAMP (micros/millis, isAdjustedToUTC = true) | timestamptz | timestamptz | 
| TIMESTAMP (nanos, isAdjustedToUTC = true) | timestamptz\_ns | timestamptz | 

The following additional Parquet types have no Iceberg equivalent and are inferred as shown.


**Type inference for Parquet-only source types**  

| Parquet type | PostgreSQL type | 
| --- | --- | 
| INT\_8 (1-byte int) | smallint | 
| INT16 | smallint | 
| UNSIGNED INT8 | smallint | 
| UNSIGNED INT16 | integer | 
| UNSIGNED INT32 | bigint | 
| UNSIGNED INT64 | numeric(20,0) | 
| ENUM (logical) | varchar | 
| JSON | json | 
| TIME (millis/micros, isAdjustedToUTC = true) | timetz | 
| Legacy timestamp (nanosecond) | timestamp | 
| INTERVAL | interval | 
| BIT | varbit | 

## Types not supported for automatic schema inference
<a name="aurora-analytics-type-mapping-unsupported-inference"></a>

The following remote source types cannot be inferred automatically. When you create a foreign table with an empty column list and the source contains one of these types, `CREATE FOREIGN TABLE` returns an error:
+ `STRUCT`
+ `MAP`
+ `LIST`
+ `GEOMETRY`
+ `GEOGRAPHY`

You can handle these columns in two ways:
+ **Skip them**: Set `aurora_analytics.skip_unsupported_columns` to `true` so automatic schema inference skips the unsupported columns and creates the foreign table with the remaining columns. A notice is emitted for each skipped column.
+ **Define them manually**: Specify the column list explicitly and declare the struct, map, or nested-list columns as `json` (or `varchar` for a native text representation). Aurora PostgreSQL then returns the data in standard JSON format.

```
CREATE FOREIGN TABLE my_table (
    id integer,
    name text,
    struct_col json,
    map_col json,
    list_of_struct json
)
SERVER aurora_analytics_server
OPTIONS (location 's3://my-bucket/data/', format 'parquet');
```

## Data types for foreign table columns
<a name="aurora-analytics-type-mapping-column-types"></a>

All PostgreSQL data types work in foreign table queries (in expressions, results, and joins) just as they do in any PostgreSQL query. The following sections are about a narrower question: which types you can define a foreign table column as, and which the analytical engine can read a Parquet or Iceberg column into. A type that is not supported here cannot be used as a foreign-table column type, but you can still use that type freely elsewhere in the same query.

### Fully supported types
<a name="aurora-analytics-type-mapping-fully-supported"></a>

The following PostgreSQL data types are fully supported as foreign table column types: `BOOLEAN`, `BYTEA`, `INTEGER`, `SMALLINT`, `BIGINT`, `REAL`, `DOUBLE PRECISION`, `TEXT`, `JSON`, `DATE`, and `UUID`.

### Partially supported types
<a name="aurora-analytics-type-mapping-partially-supported"></a>

The following PostgreSQL data types are supported with limitations.


**Partially supported foreign table column types**  

| PostgreSQL type | Limitation | 
| --- | --- | 
| VARCHAR, BPCHAR | — | 
| NUMERIC, DECIMAL | Precision (P) and Scale (S) must be explicitly defined. P must be between 1 and 38. S must be between 0 and P. | 
| TIME, TIMETZ | Only maximum precision (6) is supported. | 
| TIMESTAMP, TIMESTAMPTZ | Only maximum precision (6) is supported. | 
| BIT, VARBIT | Length constraints are not supported (for example, BIT(n) or VARBIT(n)). | 
| INTERVAL | Only maximum precision (6) is supported. Special values inf, -inf, and NaN are not supported. | 

### Types not supported for foreign table columns
<a name="aurora-analytics-type-mapping-not-supported"></a>

The following PostgreSQL data types cannot be used as foreign table column types. If a foreign table column is defined as one of these types (or a source column maps to one during schema inference), `CREATE FOREIGN TABLE` returns an error. You can still use these types elsewhere in a query (for example, building a `JSONB` value in the `SELECT` list or filtering with an array) because the restriction is on the column definition, not on query usage.


**Unsupported foreign table column types**  

| PostgreSQL type | Notes | 
| --- | --- | 
| JSONB | — | 
| SMALLSERIAL, SERIAL, BIGSERIAL | — | 
| Array types | For example, INTEGER[], TEXT[]. | 
| ENUM | — | 
| INET, CIDR, MACADDR, MACADDR8 | — | 
| MONEY | — | 
| Range types | For example, INT4RANGE, TSRANGE, DATERANGE. | 
| Geometric types | For example, POINT, LINE, POLYGON, CIRCLE. | 
| TSVECTOR, TSQUERY | — | 
| XML | — | 

**Note**  
When Aurora PostgreSQL automatically infers a foreign table's schema and the source contains columns it cannot map, it errors by default. Set the `aurora_analytics.skip_unsupported_columns` parameter to `true` to skip those columns instead and create the foreign table with the remaining supported columns.