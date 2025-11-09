# Query

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

A `Query` operation gets the values of one or more items and their
attributes by primary key (`Query` is only available for
hash-and-range primary key tables). You must provide a specific
`HashKeyValue`, and can narrow the scope of the query using
comparison operators on the `RangeKeyValue` of the primary key. Use
the `ScanIndexForward` parameter to get results in forward or
reverse order by range key.

Queries that do not return results consume the minimum read capacity units according to the
type of read.

###### Note

If the total number of items meeting the query parameters exceeds the 1MB limit, the
query stops and results are returned to the user with a
`LastEvaluatedKey` to continue the query in a subsequent
operation. Unlike a Scan operation, a Query operation never returns an empty result
set _and_ a `LastEvaluatedKey`. The
`LastEvaluatedKey` is only provided if the results exceed
1MB, or if you have used the `Limit` parameter.

The result can be set for a consistent read using the
`ConsistentRead` parameter.

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.Query
content-type: application/x-amz-json-1.0

{"TableName":"Table1",
	"Limit":2,
	"ConsistentRead":true,
	"HashKeyValue":{"S":"AttributeValue1":},
	"RangeKeyCondition": {"AttributeValueList":[{"N":"AttributeValue2"}],"ComparisonOperator":"GT"}
	"ScanIndexForward":true,
	"ExclusiveStartKey":{
		"HashKeyElement":{"S":"AttributeName1"},
		"RangeKeyElement":{"N":"AttributeName2"}
	},
    "AttributesToGet":["AttributeName1", "AttributeName2", "AttributeName3"]},
}
```

| Name                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Required |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `TableName`                                   | The name of the table containing the requested items.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes      |
| `AttributesToGet`                             | Array of Attribute names. If attribute names are not specified then all attributes will<br>be returned. If some attributes are not found, they will not appear in<br>the result.Type: Array                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No       |
| `Limit`                                       | The maximum number of items to return (not necessarily the number of matching items). If<br>DynamoDB processes the number of items up to the limit while<br>querying the table, it stops the query and returns the matching<br>values up to that point, and a<br>`LastEvaluatedKey` to apply in a<br>subsequent operation to continue the query. Also, if the result<br>set size exceeds 1MB before DynamoDB hits this limit, it stops the<br>query and returns the matching values, and a<br>`LastEvaluatedKey` to apply in a<br>subsequent operation to continue the query.Type: Number                                                                                                                                                                                          | No       |
| `ConsistentRead`                              | If set to `true`, then a consistent read is<br>issued, otherwise eventually consistent is used.Type: Boolean                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No       |
| `Count`                                       | If set to `true`, DynamoDB returns a total number of items that match the query<br>parameters, instead of a list of the matching items and their<br>attributes. You can apply the `Limit`<br>parameter to count-only queries.<br>Do not set `Count` to `true` while providing a list<br>of `AttributesToGet`; otherwise, DynamoDB<br>returns a validation error. For more information, see [Counting the items in the results](Query.md#Query.Count "Query.md#Query.Count").Type: Boolean                                                                                                                                                                                                                                                                                          | No       |
| `HashKeyValue`                                | Attribute value of the hash component of the composite primary key.Type: String, Number, or Binary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes      |
| `RangeKeyCondition`                           | A container for the attribute values and comparison operators to use for the query. A query<br>request does not require a<br>`RangeKeyCondition`. If you provide<br>only the `HashKeyValue`, DynamoDB returns all<br>items with the specified hash key element value.Type: Map                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No       |
| `RangeKeyCondition`:​<br>`AttributeValueList` | The attribute values to evaluate for the query parameters. The<br>`AttributeValueList` contains one<br>attribute value, unless a `BETWEEN`<br>comparison is specified. For the `BETWEEN`<br>comparison, the `AttributeValueList`<br>contains two attribute values. Type: A map of `AttributeValue` to a<br>`ComparisonOperator`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   | No       |
| `RangeKeyCondition`:​<br>`ComparisonOperator` | The criteria for evaluating the provided attributes, such as equals, greater-than, etc.<br>The following are valid comparison operators for a Query operation.<br>NoteString value comparisons for greater than, equals, or less than are based on ASCII<br>character code values. For example, `a` is<br>greater than `A`, and `aa` is greater<br>than `B`. For a list of code values, see [http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters](http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters "http://en.wikipedia.org/wiki/ASCII#ASCII_printable_characters").<br>For Binary, DynamoDB treats each byte of the binary data as unsigned when it<br>compares binary values, for example when evaluating query<br>expressions.<br>Type: String or Binary | No       |
|                                               | `EQ` : Equal.<br>For `EQ`, `AttributeValueList`<br>can contain only one `AttributeValue` of<br>type String, Number, or Binary (not a set). If an item contains<br>an `AttributeValue` of a different type<br>than the one specified in the request, the value does not match.<br>For example, `{"S":"6"}` does not equal<br>`{"N":"6"}`. Also, `{"N":"6"}` does<br>not equal `{"NS":["6", "2", "1"]}`.                                                                                                                                                                                                                                                                                                                                                                             |          |
|                                               | `LE` : Less than or equal.<br>For `LE`, `AttributeValueList`<br>can contain only one `AttributeValue` of<br>type String, Number, or Binary (not a set). If an item contains<br>an `AttributeValue` of a different type<br>than the one specified in the request, the value does not match.<br>For example, `{"S":"6"}` does not equal<br>`{"N":"6"}`. Also, `{"N":"6"}` does<br>not compare to `{"NS":["6", "2", "1"]}`.                                                                                                                                                                                                                                                                                                                                                           |          |
|                                               | `LT` : Less than.<br>For `LT`, `AttributeValueList`<br>can contain only one `AttributeValue` of<br>type String, Number, or Binary (not a set). If an item contains<br>an `AttributeValue` of a different type<br>than the one specified in the request, the value does not match.<br>For example, `{"S":"6"}` does not equal<br>`{"N":"6"}`. Also, `{"N":"6"}` does<br>not compare to `{"NS":["6", "2", "1"]}`.                                                                                                                                                                                                                                                                                                                                                                    |          |
|                                               | `GE` : Greater than or equal.<br>For `GE`, `AttributeValueList`<br>can contain only one `AttributeValue` of<br>type String, Number, or Binary (not a set). If an item contains<br>an `AttributeValue` of a different type<br>than the one specified in the request, the value does not match.<br>For example, `{"S":"6"}` does not equal<br>`{"N":"6"}`. Also, `{"N":"6"}` does<br>not compare to `{"NS":["6", "2", "1"]}`.                                                                                                                                                                                                                                                                                                                                                        |          |
|                                               | `GT` : Greater than.<br>For `GT`, `AttributeValueList`<br>can contain only one `AttributeValue` of<br>type String, Number, or Binary (not a set). If an item contains<br>an `AttributeValue` of a different type<br>than the one specified in the request, the value does not match.<br>For example, `{"S":"6"}` does not equal<br>`{"N":"6"}`. Also, `{"N":"6"}` does<br>not compare to `{"NS":["6", "2", "1"]}`.                                                                                                                                                                                                                                                                                                                                                                 |          |
|                                               | `BEGINS_WITH` : checks for a prefix.<br>For `BEGINS_WITH`,<br>`AttributeValueList` can contain only<br>one `AttributeValue` of type String or<br>Binary (not a Number or a set). The target attribute of the<br>comparison must be a String or Binary (not a Number or a<br>set).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |          |
|                                               | `BETWEEN` : Greater than, or equal to, the first value and less than, or<br>equal to, the second value.<br>For `BETWEEN`,<br>`AttributeValueList` must contain two<br>`AttributeValue` elements of the same<br>type, either String, Number, or Binary (not a set). A target<br>attribute matches if the target value is greater than, or equal<br>to, the first element and less than, or equal to, the second<br>element. If an item contains an<br>`AttributeValue` of a different type<br>than the one specified in the request, the value does not match.<br>For example, `{"S":"6"}` does not compare to<br>`{"N":"6"}`. Also, `{"N":"6"}` does<br>not compare to `{"NS":["6", "2", "1"]}`.                                                                                   |          |
| `ScanIndexForward`                            | Specifies ascending or descending traversal of the index. DynamoDB returns results reflecting<br>the requested order determined by the range key: If the data<br>type is Number, the results are returned in numeric order;<br>otherwise, the traversal is based on ASCII character code<br>values.Type:<br>BooleanDefault is `true` (ascending).                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `ExclusiveStartKey`                           | Primary key of the item from which to continue an earlier query. An earlier query might<br>provide this value as the `LastEvaluatedKey` if<br>that query operation was interrupted before completing the query; either<br>because of the result set size or the `Limit`<br>parameter. The `LastEvaluatedKey` can be passed<br>back in a new query request to continue the operation from that<br>point.Type: `HashKeyElement`, or `HashKeyElement` and<br>`RangeKeyElement` for a composite<br>primary key.                                                                                                                                                                                                                                                                        | No       |

## Responses

### Syntax

```
HTTP/1.1 200
x-amzn-RequestId: 8966d095-71e9-11e0-a498-71d736f27375
content-type: application/x-amz-json-1.0
content-length: 308

{"Count":2,"Items":[{
    "AttributeName1":{"S":"AttributeValue1"},
    "AttributeName2":{"N":"AttributeValue2"},
    "AttributeName3":{"S":"AttributeValue3"}
    },{
    "AttributeName1":{"S":"AttributeValue3"},
    "AttributeName2":{"N":"AttributeValue4"},
    "AttributeName3":{"S":"AttributeValue3"},
    "AttributeName5":{"B":"dmFsdWU="}
}],
    "LastEvaluatedKey":{"HashKeyElement":{"AttributeValue3":"S"},
                        "RangeKeyElement":{"AttributeValue4":"N"}
     },
     "ConsumedCapacityUnits":1
}
```

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Items`                 | Item attributes meeting the query parameters.Type: Map of attribute names to and their data types and values.                                                                                                                                                                                                                                                                                                                      |
| `Count`                 | Number of items in the response. For more information, see<br>[Counting the items in the results](Query.md#Query.Count "Query.md#Query.Count").<br>Type: Number                                                                                                                                                                                                                                                                    |
| `LastEvaluatedKey`      | Primary key of the item where the query operation stopped, inclusive of the previous<br>result set. Use this value to start a new operation excluding this value<br>in the new request.The `LastEvaluatedKey`<br>is `null` when the entire query result set is<br>complete (i.e. the operation processed the “last page”).<br>Type: `HashKeyElement`, or `HashKeyElement` and<br>`RangeKeyElement` for a composite<br>primary key. |
| `ConsumedCapacityUnits` | The number of read capacity units consumed by the operation. This value shows the number<br>applied toward your provisioned throughput. For more information<br>see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").<br>Type: Number                                                                                                                                             |

## Special errors

| Error                       | Description                        |
| --------------------------- | ---------------------------------- |
| `ResourceNotFoundException` | The specified table was not found. |

## Examples

For examples using the AWS SDK, see [Querying tables in DynamoDB](Query.md "Query.md").

### Sample request

```

// This header is abbreviated. For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.Query
content-type: application/x-amz-json-1.0

{"TableName":"1-hash-rangetable",
	"Limit":2,
	"HashKeyValue":{"S":"John"},
	"ScanIndexForward":false,
	"ExclusiveStartKey":{
		"HashKeyElement":{"S":"John"},
		"RangeKeyElement":{"S":"The Matrix"}
	}
}
```

### Sample response

```

HTTP/1.1 200
x-amzn-RequestId: 3647e778-71eb-11e0-a498-71d736f27375
content-type: application/x-amz-json-1.0
content-length: 308

{"Count":2,"Items":[{
	"fans":{"SS":["Jody","Jake"]},
	"name":{"S":"John"},
	"rating":{"S":"***"},
	"title":{"S":"The End"}
	},{
	"fans":{"SS":["Jody","Jake"]},
	"name":{"S":"John"},
	"rating":{"S":"***"},
	"title":{"S":"The Beatles"}
	}],
	"LastEvaluatedKey":{"HashKeyElement":{"S":"John"},"RangeKeyElement":{"S":"The Beatles"}},
"ConsumedCapacityUnits":1
}
```

### Sample request

```
// This header is abbreviated. For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.Query
content-type: application/x-amz-json-1.0

{"TableName":"1-hash-rangetable",
	"Limit":2,
	"HashKeyValue":{"S":"Airplane"},
	"RangeKeyCondition":{"AttributeValueList":[{"N":"1980"}],"ComparisonOperator":"EQ"},
	"ScanIndexForward":false}
```

### Sample response

```
HTTP/1.1 200
x-amzn-RequestId: 8b9ee1ad-774c-11e0-9172-d954e38f553a
content-type: application/x-amz-json-1.0
content-length: 119

{"Count":1,"Items":[{
	"fans":{"SS":["Dave","Aaron"]},
	"name":{"S":"Airplane"},
	"rating":{"S":"***"},
	"year":{"N":"1980"}
	}],
"ConsumedCapacityUnits":1
}
```

## Related actions

- [Scan](API_Scan_v20111205.md "API_Scan_v20111205.md")
