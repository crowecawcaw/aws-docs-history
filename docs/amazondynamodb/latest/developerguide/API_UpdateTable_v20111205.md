# UpdateTable

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

Updates the provisioned throughput for the given table. Setting the throughput for a table
helps you manage performance and is part of the provisioned throughput feature of DynamoDB.
For more information, see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").

The provisioned throughput values can be upgraded or downgraded based on the maximums
and minimums listed in [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").

The table must be in the `ACTIVE` state for this operation to succeed.
UpdateTable is an asynchronous operation; while executing the operation, the table is in
the `UPDATING` state. While the table is in the
`UPDATING` state, the table still has the provisioned
throughput from before the call. The new provisioned throughput setting is in effect
only when the table returns to the `ACTIVE` state after the
UpdateTable operation.

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.UpdateTable
content-type: application/x-amz-json-1.0

{"TableName":"Table1",
    "ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":15}
}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                     | Required |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `TableName`                                      | The name of the table to update.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `ProvisionedThroughput`                          | New throughput for the specified table, consisting of values for<br>`ReadCapacityUnits` and<br>`WriteCapacityUnits`. See [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").Type: Array                                                                                                                                                                                          | Yes      |
| `ProvisionedThroughput`<br>:`ReadCapacityUnits`  | Sets the minimum number of consistent<br>`ReadCapacityUnits` consumed per second<br>for the specified table before DynamoDB balances the load with<br>other operations.<br>Eventually consistent read operations require less effort than<br>a consistent read operation, so a setting of 50 consistent<br>`ReadCapacityUnits` per second provides<br>100 eventually consistent<br>`ReadCapacityUnits` per second. Type: Number | Yes      |
| `ProvisionedThroughput`<br>:`WriteCapacityUnits` | Sets the minimum number of<br>`WriteCapacityUnits` consumed per<br>second for the specified table before DynamoDB balances the load<br>with other operations. Type: Number                                                                                                                                                                                                                                                      | Yes      |

## Responses

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
Content-Type: application/json
Content-Length: 311
Date: Tue, 12 Jul 2011 21:31:03 GMT

{"TableDescription":
    {"CreationDateTime":1.321657838135E9,
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"AttributeValue1","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"AttributeValue2","AttributeType":"N"}},
    "ProvisionedThroughput":
        {"LastDecreaseDateTime":1.321661704489E9,
        "LastIncreaseDateTime":1.321663607695E9,
        "ReadCapacityUnits":5,
        "WriteCapacityUnits":10},
    "TableName":"Table1",
    "TableStatus":"UPDATING"}}
```

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CreationDateTime`      | Date when the table was created.Type: Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `KeySchema`             | The primary key (simple or composite) structure for the table. A name-value pair for<br>the `HashKeyElement` is required, and a name-value<br>pair for the `RangeKeyElement` is optional (only<br>required for composite primary keys). The maximum hash key size is 2048<br>bytes. The maximum range key size is 1024 bytes. Both limits are<br>enforced separately (i.e. you can have a combined hash + range 2048 +<br>1024 key). For more information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").Type: Map of<br>`HashKeyElement`, or `HashKeyElement` and<br>`RangeKeyElement` for a composite primary key. |
| `ProvisionedThroughput` | Current throughput settings for the specified table, including values for<br>`LastIncreaseDateTime` (if applicable),<br>`LastDecreaseDateTime` (if applicable), Type: Array                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `TableName`             | The name of the updated table.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `TableStatus`           | The current state of the table (`CREATING`,<br>`ACTIVE`, `DELETING`<br>or `UPDATING`), which should be<br>`UPDATING`. Use the [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md") operationto check the<br>status of the table. Type:<br>String                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## Special errors

| Error                       | Description                             |
| --------------------------- | --------------------------------------- |
| `ResourceNotFoundException` | The specified table was not found.      |
| `ResourceInUseException`    | The table is not in the `ACTIVE` state. |

## Examples

### Sample request

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.UpdateTable
content-type: application/x-amz-json-1.0

{"TableName":"comp1",
    "ProvisionedThroughput":{"ReadCapacityUnits":5,"WriteCapacityUnits":15}
}
```

### Sample response

```
HTTP/1.1 200 OK
content-type: application/x-amz-json-1.0
content-length: 390
Date: Sat, 19 Nov 2011 00:46:47 GMT

{"TableDescription":
    {"CreationDateTime":1.321657838135E9,
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"user","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"time","AttributeType":"N"}},
    "ProvisionedThroughput":
        {"LastDecreaseDateTime":1.321661704489E9,
        "LastIncreaseDateTime":1.321663607695E9,
        "ReadCapacityUnits":5,
        "WriteCapacityUnits":10},
    "TableName":"comp1",
    "TableStatus":"UPDATING"}
}
```

## Related actions

- [CreateTable](API_CreateTable_v20111205.md "API_CreateTable_v20111205.md")
- [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md")
- [DeleteTable](API_DeleteTable_v20111205.md "API_DeleteTable_v20111205.md")
