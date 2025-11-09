# DeleteTable

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

The `DeleteTable` operation deletes a table and all of its items. After a
`DeleteTable` request, the specified table is in the
`DELETING` state until DynamoDB completes the deletion. If the
table is in the `ACTIVE` state, you can delete it. If a table is in
`CREATING` or `UPDATING` states, then
DynamoDB returns a `ResourceInUseException` error. If the specified table does
not exist, DynamoDB returns a `ResourceNotFoundException`. If table is already
in the `DELETING` state, no error is returned.

###### Note

DynamoDB might continue to accept data plane operation requests, such as
`GetItem` and `PutItem`, on a table in the
`DELETING` state until the table deletion is
complete.

Tables are unique among those associated with the AWS Account issuing the request, and
the AWS region that receives the request (such as dynamodb.us-west-1.amazonaws.com).
Each DynamoDB endpoint is entirely independent. For example, if you have two
tables called "MyTable," one in dynamodb.us-west-2.amazonaws.com and one in
dynamodb.us-west-1.amazonaws.com, they are completely independent and do not share any
data; deleting one does not delete the other.

Use the [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md")
operation to check the status of the table.

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.DeleteTable
content-type: application/x-amz-json-1.0

{"TableName":"Table1"}
```

| Name        | Description                                      | Required |
| ----------- | ------------------------------------------------ | -------- |
| `TableName` | The name of the table to delete.<br>Type: String | Yes      |

## Responses

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4HONCKIVH1BFUDQ1U68CTG3N27VV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 311
Date: Sun, 14 Aug 2011 22:56:22 GMT

{"TableDescription":
    {"CreationDateTime":1.313362508446E9,
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"user","AttributeType":"S"},
        "RangeKeyElement":{"AttributeName":"time","AttributeType":"N"}},
    "ProvisionedThroughput":{"ReadCapacityUnits":10,"WriteCapacityUnits":10},
    "TableName":"Table1",
    "TableStatus":"DELETING"
    }
}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TableDescription`                               | A container for the table properties.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `CreationDateTime`                               | Date when the table was created.Type: Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `KeySchema`                                      | The primary key (simple or composite) structure for the table. A name-value pair for the<br>`HashKeyElement` is required, and a<br>name-value pair for the `RangeKeyElement`<br>is optional (only required for composite primary keys). For more<br>information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").Type: Map of<br>`HashKeyElement`, or `HashKeyElement` and<br>`RangeKeyElement` for a composite primary key. |
| `ProvisionedThroughput`                          | Throughput for the specified table, consisting of values for<br>`ReadCapacityUnits` and<br>`WriteCapacityUnits`. See [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").                                                                                                                                                                                                                                                                                                    |
| `ProvisionedThroughput`:<br>`ReadCapacityUnits`  | The minimum number of<br>`ReadCapacityUnits` consumed per second<br>for the specified table before DynamoDB balances the load with<br>other operations. Type: Number                                                                                                                                                                                                                                                                                                                                                       |
| `ProvisionedThroughput`:<br>`WriteCapacityUnits` | The minimum number of `WriteCapacityUnits` consumed per second for the<br>specified table before DynamoDB balances the load with other<br>operations.Type: Number                                                                                                                                                                                                                                                                                                                                                          |
| `TableName`                                      | The name of the deleted table.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `TableStatus`                                    | The current state of the table (`DELETING`). Once the table is<br>deleted, subsequent requests for the table return `resource<br>not found`. Use the [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md") operation to check the status<br>of the table. Type: String                                                                                                                                                                                                                       |

## Special errors

| Error                    | Description                                                         |
| ------------------------ | ------------------------------------------------------------------- |
| `ResourceInUseException` | Table is in state `CREATING` or `UPDATING`<br>and can't be deleted. |

## Examples

### Sample request

```
// This header is abbreviated. For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.DeleteTable
content-type: application/x-amz-json-1.0
content-length: 40

{"TableName":"favorite-movies-table"}
```

### Sample response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 4HONCKIVH1BFUDQ1U68CTG3N27VV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 160
Date: Sun, 14 Aug 2011 17:20:03 GMT

{"TableDescription":
    {"CreationDateTime":1.313362508446E9,
    "KeySchema":
        {"HashKeyElement":{"AttributeName":"name","AttributeType":"S"}},
    "TableName":"favorite-movies-table",
    "TableStatus":"DELETING"
}
```

## Related actions

- [CreateTable](API_CreateTable_v20111205.md "API_CreateTable_v20111205.md")
- [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md")
