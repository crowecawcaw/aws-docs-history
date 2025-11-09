# ListTables

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

Returns an array of all the tables associated with the current account and endpoint.

Each DynamoDB endpoint is entirely independent. For example, if you have two tables
called "MyTable," one in dynamodb.us-west-2.amazonaws.com and one in
dynamodb.us-east-1.amazonaws.com, they are completely independent and do not share any
data. The ListTables operation returns all of the table names associated
with the account making the request, for the endpoint that receives the request.

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.ListTables
content-type: application/x-amz-json-1.0

{"ExclusiveStartTableName":"Table1","Limit":3}
```

The ListTables operation, by default, requests all of the table names associated
with the account making the request, for the endpoint that receives the
request.

| Name                      | Description                                                                                                                                                                                                              | Required |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `Limit`                   | A number of maximum table names to return.<br>Type: Integer                                                                                                                                                              | No       |
| `ExclusiveStartTableName` | The name of the table that starts the list. If you already ran a ListTables operation and<br>received an `LastEvaluatedTableName` value<br>in the response, use that value here to continue the<br>list.<br>Type: String | No       |

## Responses

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: S1LEK2DPQP8OJNHVHL8OU2M7KRVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 81
Date: Fri, 21 Oct 2011 20:35:38 GMT

{"TableNames":["Table1","Table2","Table3"], "LastEvaluatedTableName":"Table3"}
```

| Name                     | Description                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TableNames`             | The names of the tables associated with the current account<br>at the current endpoint.<br>Type: Array                                                                                                                                                                                                                                                                 |
| `LastEvaluatedTableName` | The name of the last table in the current list, only if some tables for the account and<br>endpoint have not been returned. This value does not exist in a<br>response if all table names are already returned. Use this value<br>as the `ExclusiveStartTableName` in a new<br>request to continue the list until all the table names are<br>returned.<br>Type: String |

## Special errors

No errors are specific to this operation.

## Examples

The following examples show an HTTP POST request and response using the ListTables
operation.

### Sample request

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.ListTables
content-type: application/x-amz-json-1.0

{"ExclusiveStartTableName":"comp2","Limit":3}
```

### Sample response

```
HTTP/1.1 200 OK
x-amzn-RequestId: S1LEK2DPQP8OJNHVHL8OU2M7KRVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 81
Date: Fri, 21 Oct 2011 20:35:38 GMT

{"LastEvaluatedTableName":"comp5","TableNames":["comp3","comp4","comp5"]}
```

## Related actions

- [DescribeTables](API_DescribeTables_v20111205.md "API_DescribeTables_v20111205.md")
- [CreateTable](API_CreateTable_v20111205.md "API_CreateTable_v20111205.md")
- [DeleteTable](API_DeleteTable_v20111205.md "API_DeleteTable_v20111205.md")
