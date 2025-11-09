# DeleteItem

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

Deletes a single item in a table by primary key. You can perform a conditional delete
operation that deletes the item if it exists, or if it has an expected attribute
value.

###### Note

If you specify `DeleteItem` without attributes or values, all
the attributes for the item are deleted.

Unless you specify conditions, the `DeleteItem` is an idempotent operation; running it multiple
times on the same item or attribute does _not_ result in an error
response.

Conditional deletes are useful for only deleting items and attributes if specific
conditions are met. If the conditions are met, DynamoDB performs the delete. Otherwise,
the item is not deleted.

You can perform the expected conditional check on one attribute per operation.

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.DeleteItem
content-type: application/x-amz-json-1.0

{"TableName":"Table1",
    "Key":
        {"HashKeyElement":{"S":"AttributeValue1"},"RangeKeyElement":{"N":"AttributeValue2"}},
    "Expected":{"AttributeName3":{"Value":{"S":"AttributeValue3"}}},
    "ReturnValues":"ALL_OLD"}
}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Required |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `TableName`                                      | The name of the table containing the item to delete.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes      |
| `Key`                                            | The primary key that defines the item. For more information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").Type: Map of `HashKeyElement`<br>to its value and `RangeKeyElement` to its<br>value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes      |
| `Expected`                                       | Designates an attribute for a conditional delete. The `Expected`<br>parameter allows you to provide an attribute name, and whether or not<br>DynamoDB should check to see if the attribute has a particular value before<br>deleting it.Type: Map of attribute names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No       |
| `Expected:AttributeName`                         | The name of the attribute for the conditional put.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No       |
| `Expected:AttributeName: ExpectedAttributeValue` | Use this parameter to specify whether or not a value already exists for the attribute<br>name-value pair. The following JSON notation deletes the<br>item if the "Color" attribute doesn't exist for that<br>item:<br>`<br>"Expected" :<br>{"Color":{"Exists":false}}<br>`<br>The<br>following JSON notation checks to see if the attribute with name<br>"Color" has an existing value of "Yellow" before deleting the<br>item:<br>`<br>"Expected" :<br>{"Color":{"Exists":true},{"Value":{"S":"Yellow"}}}<br>`<br>By<br>default, if you use the `Expected`<br>parameter and provide a `Value`, DynamoDB<br>assumes the attribute exists and has a current value to be<br>replaced. So you don't have to specify<br>`{"Exists":true}`, because it is implied. You can<br>shorten the request to:<br>`<br>"Expected" :<br>{"Color":{"Value":{"S":"Yellow"}}}<br>`<br>NoteIf you specify `{"Exists":true}` without an<br>attribute value to check, DynamoDB returns an error. | No       |
| `ReturnValues`                                   | Use this parameter if you want to get the attribute name-value pairs before they were<br>deleted. Possible parameter values are `NONE`<br>(default) or `ALL_OLD`. If<br>`ALL_OLD` is specified, the content of the old<br>item is returned. If this parameter is not provided or is<br>`NONE`, nothing is returned.Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No       |

## Responses

### Syntax

```
HTTP/1.1 200 OK
x-amzn-RequestId: CSOC7TJPLR0OOKIRLGOHVAICUFVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 353
Date: Tue, 12 Jul 2011 21:31:03 GMT

{"Attributes":
    {"AttributeName3":{"SS":["AttributeValue3","AttributeValue4","AttributeValue5"]},
    "AttributeName2":{"S":"AttributeValue2"},
    "AttributeName1":{"N":"AttributeValue1"}
    },
"ConsumedCapacityUnits":1
}
```

| Name                    | Description                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Attributes`            | If the `ReturnValues` parameter is provided as<br>`ALL_OLD` in the request, DynamoDB returns an<br>array of attribute name-value pairs (essentially, the deleted item).<br>Otherwise, the response contains an empty set. Type: Array of attribute name-value pairs.                                                                                            |
| `ConsumedCapacityUnits` | The number of write capacity units consumed by the operation. This value shows the number<br>applied toward your provisioned throughput. Delete requests on<br>non-existent items consume 1 write capacity unit. For more<br>information see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").<br>Type: Number |

## Special errors

| Error                             | Description                                                          |
| --------------------------------- | -------------------------------------------------------------------- |
| `ConditionalCheckFailedException` | Conditional check failed. An expected attribute value was not found. |

## Examples

### Sample request

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.DeleteItem
content-type: application/x-amz-json-1.0

{"TableName":"comp-table",
    "Key":
        {"HashKeyElement":{"S":"Mingus"},"RangeKeyElement":{"N":"200"}},
    "Expected":
        {"status":{"Value":{"S":"shopping"}}},
    "ReturnValues":"ALL_OLD"
}
```

### Sample response

```
HTTP/1.1 200 OK
x-amzn-RequestId: U9809LI6BBFJA5N2R0TB0P017JVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 353
Date: Tue, 12 Jul 2011 22:31:23 GMT

{"Attributes":
    {"friends":{"SS":["Dooley","Ben","Daisy"]},
    "status":{"S":"shopping"},
    "time":{"N":"200"},
    "user":{"S":"Mingus"}
    },
"ConsumedCapacityUnits":1
}
```

## Related actions

- [PutItem](API_PutItem_v20111205.md "API_PutItem_v20111205.md")
