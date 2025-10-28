# Reading from Salesforce

**Prerequisite**

A Salesforce sObject you would like to read from. You will need the object name such as `Account` or `Case` or `Opportunity`.

**Example**:

```
salesforce_read = glueContext.create_dynamic_frame.from_options(
    connection_type="salesforce",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Account",
        "API_VERSION": "v60.0"
    }
)
```

## Partitioning queries

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For Date or Timestamp fields, the connector accepts the Spark timestamp format used in Spark SQL queries.

Examples of valid values:

```
"TIMESTAMP \"1707256978123\""
"TIMESTAMP '2018-01-01 00:00:00.000 UTC'"
"TIMESTAMP \"2018-01-01 00:00:00 Pacific/Tahiti\""
"TIMESTAMP \"2018-01-01 00:00:00\""
"TIMESTAMP \"-123456789\" Pacific/Tahiti"
"TIMESTAMP \"1702600882\""
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.
- `TRANSFER_MODE`: supports two modes: `SYNC` and `ASYNC`. Default is `SYNC`.
  When set to `ASYNC`, Bulk API 2.0 Query will be utilized for processing.

Example:

```
salesforce_read = glueContext.create_dynamic_frame.from_options(
    connection_type="salesforce",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "Account",
        "API_VERSION": "v60.0",
        "PARTITION_FIELD": "SystemModstamp",
        "LOWER_BOUND": "TIMESTAMP '2021-01-01 00:00:00 Pacific/Tahiti'",
        "UPPER_BOUND": "TIMESTAMP '2023-01-10 00:00:00 Pacific/Tahiti'",
        "NUM_PARTITIONS": "10",
        "TRANSFER_MODE": "ASYNC"
    }
)
```

## FILTER_PREDICATE option

**FILTER_PREDICATE**: It is an optional parameter. This option is used for query filter.

Examples of **FILTER_PREDICATE**:

```
     Case 1: FILTER_PREDICATE with single criterion
     Examples:
       LastModifiedDate >= TIMESTAMP '2025-04-01 00:00:00 Pacific/Tahiti'
       LastModifiedDate <= TIMESTAMP "2025-04-01 00:00:00"
       LastModifiedDate >= TIMESTAMP '2018-01-01 00:00:00.000 UTC'
       LastModifiedDate <= TIMESTAMP "-123456789 Pacific/Tahiti"
       LastModifiedDate <= TIMESTAMP "1702600882"

     Case 2: FILTER_PREDICATE with multiple criteria
     Examples:
       LastModifiedDate >= TIMESTAMP '2025-04-01 00:00:00 Pacific/Tahiti' AND Id = "0012w00001CotGiAAJ"
       LastModifiedDate >= TIMESTAMP "1702600882" AND Id = "001gL000002i26MQAQ"

     Case 3: FILTER_PREDICATE single criterion with LIMIT
     Examples:
       LastModifiedDate >= TIMESTAMP "1702600882" LIMIT 2

     Case 4: FILTER_PREDICATE with LIMIT
     Examples:
       LIMIT 2
```
