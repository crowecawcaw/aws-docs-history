# CreateTable

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

The `CreateTable` operation adds a new table to your
account.

The table name must be unique among those associated with the AWS
Account issuing the request, and the AWS region that receives the request (such as
dynamodb.us-west-2.amazonaws.com). Each DynamoDB endpoint is entirely independent. For
example, if you have two tables called "MyTable," one in dynamodb.us-west-2.amazonaws.com
and one in dynamodb.us-west-1.amazonaws.com, they are completely independent and do not
share any data.

The `CreateTable` operation triggers an asynchronous workflow to
begin creating the table. DynamoDB immediately returns the state of the table
(`CREATING`) until the table is in the
`ACTIVE` state. Once the table is in the
`ACTIVE` state, you can perform data plane operations.

Use the [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md") operation to check the status of the table.

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.CreateTable
content-type: application/x-amz-json-1.0

{"TableName":"Table1",
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"AttributeName1","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"AttributeName2","AttributeType":"N"}},
    "ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":10}
}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Required |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `TableName`                                      | The name of the table to create.Allowed<br>characters are a-z, A-Z, 0-9, '\_' (underscore), '-' (dash), and<br>'.' (dot). Names can be between 3 and 255 characters<br>long.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes      |
| `KeySchema`                                      | The primary key (simple or composite) structure for the<br>table. A name-value pair for the<br>`HashKeyElement` is required, and a<br>name-value pair for the `RangeKeyElement`<br>is optional (only required for composite primary keys). For more<br>information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").Primary key element names can be between 1<br>and 255 characters long with no character<br>restrictions.<br>Possible values for the AttributeType are "S" (string), "N"<br>(numeric), or "B" (binary).Type: Map of<br>`HashKeyElement`, or<br>`HashKeyElement` and<br>`RangeKeyElement` for a composite<br>primary key. | Yes      |
| `ProvisionedThroughput`                          | New throughput for the specified table, consisting of values for<br>`ReadCapacityUnits` and<br>`WriteCapacityUnits`. For details, see<br>[DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md"). NoteFor current maximum/minimum values, see [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").Type: Array                                                                                                                                                                                                                                                                                                                                                                      | Yes      |
| `ProvisionedThroughput`:<br>`ReadCapacityUnits`  | Sets the minimum number of consistent<br>`ReadCapacityUnits` consumed per second<br>for the specified table before DynamoDB balances the load with<br>other operations.<br>Eventually consistent read operations require less effort than<br>a consistent read operation, so a setting of 50 consistent<br>`ReadCapacityUnits` per second provides<br>100 eventually consistent<br>`ReadCapacityUnits` per second.<br>Type: Number                                                                                                                                                                                                                                                                                                        | Yes      |
| `ProvisionedThroughput`:<br>`WriteCapacityUnits` | Sets the minimum number of<br>`WriteCapacityUnits` consumed per second<br>for the specified table before DynamoDB balances the load with other<br>operations. Type: Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |

## Responses

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 311
Date: Tue, 12 Jul 2011 21:31:03 GMT

{"TableDescription":
    {"CreationDateTime":1.310506263362E9,
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"AttributeName1","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"AttributeName2","AttributeType":"N"}},
    "ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":10},
    "TableName":"Table1",
    "TableStatus":"CREATING"
    }
}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TableDescription`                               | A container for the table properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `CreationDateTime`                               | Date when the table was created in [UNIX epoch<br>time](http://www.epochconverter.com/ "http://www.epochconverter.com/").Type: Number                                                                                                                                                                                                                                                                                                                                                                                                   |
| `KeySchema`                                      | The primary key (simple or composite) structure for the<br>table. A name-value pair for the<br>`HashKeyElement` is required, and a<br>name-value pair for the `RangeKeyElement`<br>is optional (only required for composite primary keys). For more<br>information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey")<br>.Type: Map of<br>`HashKeyElement`, or<br>`HashKeyElement` and<br>`RangeKeyElement` for a composite<br>primary key. |
| `ProvisionedThroughput`                          | Throughput for the specified table, consisting of values<br>for `ReadCapacityUnits` and<br>`WriteCapacityUnits`. See [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").<br>Type: Array                                                                                                                                                                                                                                                                                                  |
| `ProvisionedThroughput`<br>:`ReadCapacityUnits`  | The minimum number of<br>`ReadCapacityUnits` consumed per second<br>before DynamoDB. balances the load with other<br>operationsType: Number                                                                                                                                                                                                                                                                                                                                                                                             |
| `ProvisionedThroughput`<br>:`WriteCapacityUnits` | The minimum number of<br>`ReadCapacityUnits` consumed per second<br>before `WriteCapacityUnits`. balances the<br>load with other operationsType: Number                                                                                                                                                                                                                                                                                                                                                                                 |
| `TableName`                                      | The name of the created table.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `TableStatus`                                    | The current state of the table<br>(`CREATING`). Once the table is in the<br>`ACTIVE` state, you can put data in<br>it.Use the [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md") API to check<br>the status of the table.Type:<br>String                                                                                                                                                                                                                                                               |

## Special errors

| Error                    | Description                                                                                                                                                                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ResourceInUseException` | Attempt to recreate an already existing table.                                                                                                                                                                                                                                   |
| `LimitExceededException` | The number of simultaneous table requests (cumulative number<br>of tables in the `CREATING`,<br>`DELETING` or<br>`UPDATING` state) exceeds the maximum<br>allowed.NoteFor current maximum/minimum values, see [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").. |

## Examples

The following example creates a table with a composite primary key containing a string
and a number. For examples using the AWS SDK, see [Working with tables and data in DynamoDB](WorkingWithTables.md "WorkingWithTables.md").

### Sample request

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.CreateTable
content-type: application/x-amz-json-1.0


{"TableName":"comp-table",
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"user","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"time","AttributeType":"N"}},
    "ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":10}
}
```

### Sample response

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 311
Date: Tue, 12 Jul 2011 21:31:03 GMT

{"TableDescription":
    {"CreationDateTime":1.310506263362E9,
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"user","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"time","AttributeType":"N"}},
    "ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":10},
    "TableName":"comp-table",
    "TableStatus":"CREATING"
    }
}
```

## Related actions

- [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md")
- [DeleteTable](API_DeleteTable_v20111205.md "API_DeleteTable_v20111205.md")
