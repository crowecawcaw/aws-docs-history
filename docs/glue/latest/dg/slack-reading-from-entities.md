# Reading from Slack entities

**Prerequisites**

- A Slack object you would like to read from.

**Supported entities**

| Entity        | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| conversations | Yes             | Yes            | No                | Yes                | Yes                   |

**Example**

```
slack_read = glueContext.create_dynamic_frame.from_options(
    connection_type="slack",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "conversations/C058W38R5J8"
    }
)
```

**Slack entity and field details**

| Entity        | Field             | Data Type | Supported Operators                                                                         |
| ------------- | ----------------- | --------- | ------------------------------------------------------------------------------------------- |
| conversations | attachments       | List      | NA                                                                                          |
| conversations | bot_id            | String    | NA                                                                                          |
| conversations | blocks            | List      | NA                                                                                          |
| conversations | client_msg_id     | String    | NA                                                                                          |
| conversations | is_starred        | Boolean   | NA                                                                                          |
| conversations | last_read         | String    | NA                                                                                          |
| conversations | latest_reply      | String    | NA                                                                                          |
| conversations | reactions         | List      | NA                                                                                          |
| conversations | replies           | List      | NA                                                                                          |
| conversations | reply_count       | Integer   | NA                                                                                          |
| conversations | reply_users       | List      | NA                                                                                          |
| conversations | reply_users_count | Integer   | NA                                                                                          |
| conversations | subscribed        | Boolean   | NA                                                                                          |
| conversations | subtype           | String    | NA                                                                                          |
| conversations | text              | String    | NA                                                                                          |
| conversations | team              | String    | NA                                                                                          |
| conversations | thread_ts         | String    | NA                                                                                          |
| conversations | ts                | String    | EQUAL_TO, BETWEEN, LESS_THAN, LESS_THAN_OR_EQUAL_TO, GREATER_THAN, GREATER_THAN_OR_EQUAL_TO |
| conversations | type              | String    | NA                                                                                          |
| conversations | user              | String    | NA                                                                                          |
| conversations | inviter           | String    | NA                                                                                          |
| conversations | root              | Struct    | NA                                                                                          |
| conversations | is_locked         | Boolean   | NA                                                                                          |
| conversations | files             | List      | NA                                                                                          |
| conversations | room              | Struct    | NA                                                                                          |
| conversations | upload            | Boolean   | NA                                                                                          |
| conversations | display_as_bot    | Boolean   | NA                                                                                          |
| conversations | channel           | String    | NA                                                                                          |
| conversations | no_notifications  | Boolean   | NA                                                                                          |
| conversations | permalink         | String    | NA                                                                                          |
| conversations | pinned_to         | List      | NA                                                                                          |
| conversations | pinned_info       | Struct    | NA                                                                                          |
| conversations | edited            | Struct    | NA                                                                                          |
| conversations | app_id            | String    | NA                                                                                          |
| conversations | bot_profile       | Struct    | NA                                                                                          |
| conversations | metadata          | Struct    | NA                                                                                          |

**Partitioning queries**

Additional spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`,
`NUM_PARTITIONS` can be provided if you want to utilize concurrency in Spark. With these parameters,
the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by spark
tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition query.
- `LOWER_BOUND`: an inclusive lower bound value of the chosen partition field.

For date, we accept the Spark date format used in Spark SQL queries.
Example of valid value: `"2024-07-01T00:00:00.000Z"`.

- `UPPER_BOUND`: an exclusive upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: number of partitions.

Entity wise partitioning field support details are captured in below table.

| Entity Name   | Partitioning Field | Data Type |
| ------------- | ------------------ | --------- |
| conversations | ts                 | String    |

**Example**

```
slack_read = glueContext.create_dynamic_frame.from_options(
    connection_type="slack",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "conversations/C058W38R5J8",
        "PARTITION_FIELD": "ts"
        "LOWER_BOUND": "2022-12-01T00:00:00.000Z"
        "UPPER_BOUND": "2024-09-23T15:00:00.000Z"
        "NUM_PARTITIONS": "2"
    }
)
```
