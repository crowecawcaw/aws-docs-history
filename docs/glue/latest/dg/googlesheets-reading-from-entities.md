# Reading from Google Sheets entities

**Prerequisites**

- A Google SpreadSheet that you would like to read from. You will need the SpreadSheet ID and tabName of the spreadsheet.

**Google Sheets Entity and Field Details:**

| Entity      | Data Type | Supported Operators           |
| ----------- | --------- | ----------------------------- |
| Spreadsheet | String    | N/A (filter is not supported) |

**Example**

```
googleSheets_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googlesheets",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "{SpreadSheetID}#{SheetTabName}",
        "API_VERSION": "v4"
    }
```

**Partitioning queries**

For Record Base Partitioning only, `NUM_PARTITIONS` can be provided as additional spark options if you
want to utilize concurrency in Spark. With this parameter, the original query would be split into
`NUM_PARTITIONS` number of sub-queries that can be executed by spark tasks concurrently.

**Example with `NUM_PARTITIONS`**

```
googlesheets_read = glueContext.create_dynamic_frame.from_options(
    connection_type="googlesheets",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "{SpreadSheetID}#{SheetTabName}",
        "API_VERSION": "v4",
        "NUM_PARTITIONS": "10"
    }
```
