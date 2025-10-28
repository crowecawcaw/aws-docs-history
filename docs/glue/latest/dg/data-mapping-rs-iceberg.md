# Data mapping between Amazon Redshift and Apache Iceberg

Redshift and Iceberg support various data types. The following compatibility matrix
outlines the support and limitations when mapping data between these two data systems. Please
refer to [Amazon
Redshift Data Types](../../../redshift/latest/dg/c_Supported_data_types.md "../../../redshift/latest/dg/c_Supported_data_types.md") and [Apache Iceberg Table
Specifications](https://iceberg.apache.org/spec/#primitive-types "https://iceberg.apache.org/spec/#primitive-types") for more details on supported data types in respective data
systems.

| Redshift data type     | Aliases                     | Iceberg data type |
| ---------------------- | --------------------------- | ----------------- |
| SMALLINT               | INT2                        | int               |
| INTEGER                | INT, INT4                   | int               |
| BIGINT                 | INT8                        | long              |
| DECIMAL                | NUMERIC                     | decimal           |
| REAL                   | FLOAT4                      | float             |
| REAL                   | FLOAT4                      | float             |
| DOUBLE PRECISION       | FLOAT8, FLOAT               | double            |
| CHAR                   | CHARACTER, NCHAR            | string            |
| VARCHAR                | CHARACTER VARYING, NVARCHAR | string            |
| BPCHAR                 |                             | string            |
| TEXT                   |                             | string            |
| DATE                   |                             | date              |
| TIME                   | TIME WITHOUT TIMEZONE       | time              |
| TIME                   | TIME WITH TIMEZONE          | not supported     |
| TIMESTAMP              | TIMESTAMP WITHOUT TIMEZONE  | TIMESTAMP         |
| TIMESTAMPZ             | TIMESTAMP WITH TIMEZONE     | TIMESTAMPZ        |
| INTERVAL YEAR TO MONTH |                             | Not supported     |
| INTERVAL DAY TO SECOND |                             | Not supported     |
| BOOLEAN                | BOOL                        | bool              |
| HLLSKETCH              |                             | Not supported     |
| SUPER                  |                             | Not supported     |
| VARBYTE                | VARBINARY, BINARY VARYING   | binary            |
| GEOMETRY               |                             | Not supported     |
| GEOGRAPHY              |                             | Not supported     |
