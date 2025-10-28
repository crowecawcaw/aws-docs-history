# Built-in functions in Amazon Keyspaces

Amazon Keyspaces (for Apache Cassandra) supports a variety of built-in functions that you can use in Cassandra Query
Language (CQL) statements.

###### Topics

- [Scalar functions](#cql.functions.scalar "#cql.functions.scalar")

## Scalar functions

A _scalar function_ performs a calculation on a single value
and returns the result as a single value. Amazon Keyspaces supports the following scalar
functions.

| Function           | Description                                                                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `blobAsType`       | Returns a value of the specified data type.                                                                      |
| `cast`             | Converts one native data type into another native data type.                                                     |
| `currentDate`      | Returns the current date/time as a date.                                                                         |
| `currentTime`      | Returns the current date/time as a time.                                                                         |
| `currentTimestamp` | Returns the current date/time as a timestamp.                                                                    |
| `currentTimeUUID`  | Returns the current date/time as a `timeuuid`.                                                                   |
| `fromJson`         | Converts the JSON string into the selected column's data type.                                                   |
| `maxTimeuuid`      | Returns the largest possible `timeuuid` for timestamp or date string.                                            |
| `minTimeuuid`      | Returns the smallest possible `timeuuid` for timestamp or date string.                                           |
| `now`              | Returns a new unique `timeuuid`.                                                                                 |
| `toDate`           | Converts either a `timeuuid` or a timestamp to a date type.                                                      |
| `toJson`           | Returns the column value of the selected column in JSON format.                                                  |
| `token`            | Returns the hash value of the partition key.                                                                     |
| `toTimestamp`      | Converts either a `timeuuid` or a date to a timestamp.                                                           |
| `TTL`              | Returns the expiration time in seconds for a column.                                                             |
| `typeAsBlob`       | Converts the specified data type into a `blob`.                                                                  |
| `toUnixTimestamp`  | Converts either a `timeuuid` or a timestamp into a `bigInt`.                                                     |
| `uuid`             | Returns a random version 4 UUID.                                                                                 |
| `writetime`        | Returns the timestamp of the value of the specified column.                                                      |
| `dateOf`           | _(Deprecated)_ Extracts the timestamp of a `timeuuid`, and returns the value as a date.                          |
| `unixTimestampOf`  | _(Deprecated)_ Extracts the timestamp of a `timeuuid`, and returns the value as a raw, 64-bit integer timestamp. |
