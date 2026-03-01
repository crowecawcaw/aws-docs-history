# Supported column data types

This section describes the supported data types for non-partition and partition
columns.

## Supported non-partition column data types

For non-partition columns, all data types that Athena supports except
`CHAR` are supported (`CHAR` is not supported in the Delta
Lake protocol itself). Supported data types include:

```
boolean
tinyint
smallint
integer
bigint
double
float
decimal
varchar
string
binary
date
timestamp
array
map
struct
```

## Supported partition column data types

For partition columns, Athena supports tables with the following data types:

```
boolean
integer
smallint
tinyint
bigint
decimal
float
double
date
timestamp
varchar
```

For more information about the data types in Athena, see [Data types in Amazon Athena](data-types.md "data-types.md").
