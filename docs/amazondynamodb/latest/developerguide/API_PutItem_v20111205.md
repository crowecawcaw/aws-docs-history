# PutItem

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

Creates a new item, or replaces an old item with a new item (including all the attributes).
If an item already exists in the specified table with the same primary key, the new item
completely replaces the existing item. You can perform a conditional put (insert a new
item if one with the specified primary key doesn't exist), or replace an existing item
if it has certain attribute values.

Attribute values may not be null; string and binary type attributes must have lengths
greater than zero; and set type attributes must not be empty. Requests with empty values
will be rejected with a `ValidationException`.

###### Note

To ensure that a new item does not replace an existing item, use a conditional put
operation with `Exists` set to `false` for
the primary key attribute, or attributes.

For more information about using `PutItem`, see [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md").

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.PutItem
content-type: application/x-amz-json-1.0

{"TableName":"Table1",
    "Item":{
        "AttributeName1":{"S":"AttributeValue1"},
        "AttributeName2":{"N":"AttributeValue2"},
        "AttributeName5":{"B":"dmFsdWU="}
    },
    "Expected":{"AttributeName3":{"Value": {"S":"AttributeValue"}, "Exists":Boolean}},
    "ReturnValues":"ReturnValuesConstant"}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Required |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `TableName`                                      | The name of the table to contain the item.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes      |
| `Item`                                           | A map of the attributes for the item, and must include the primary key values that<br>define the item. Other attribute name-value pairs can be provided for<br>the item. For more information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").Type: Map of attribute<br>names to attribute values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes      |
| `Expected`                                       | Designates an attribute for a conditional put. The `Expected`<br>parameter allows you to provide an attribute name, and whether<br>or not DynamoDB should check to see if the attribute value already<br>exists; or if the attribute value exists and has a particular<br>value before changing it.Type: Map of an attribute<br>names to an attribute value, and whether it exists.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No       |
| `Expected:AttributeName`                         | The name of the attribute for the conditional put.Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No       |
| `Expected:AttributeName: ExpectedAttributeValue` | Use this parameter to specify whether or not a value already exists for the attribute<br>name-value pair. The following JSON notation replaces the<br>item if the "Color" attribute doesn't already exist for that<br>item:<br>`<br>"Expected" :<br>{"Color":{"Exists":false}}<br>`<br>The<br>following JSON notation checks to see if the attribute with name<br>"Color" has an existing value of "Yellow" before replacing the<br>item:<br>`<br>"Expected" :<br>{"Color":{"Exists":true,{"Value":{"S":"Yellow"}}}<br>`<br>By<br>default, if you use the `Expected`<br>parameter and provide a `Value`, DynamoDB<br>assumes the attribute exists and has a current value to be<br>replaced. So you don't have to specify<br>`{"Exists":true}`, because it is implied. You can<br>shorten the request to:<br>`<br>"Expected" :<br>{"Color":{"Value":{"S":"Yellow"}}}<br>`<br>NoteIf you specify `{"Exists":true}` without an<br>attribute value to check, DynamoDB returns an error. | No       |
| `ReturnValues`                                   | Use this parameter if you want to get the attribute name-value pairs<br>before they were updated with the `PutItem`<br>request. Possible parameter values are `NONE`<br>(default) or `ALL_OLD`. If<br>`ALL_OLD` is specified, and<br>`PutItem` overwrote an attribute name-value<br>pair, the content of the old item is returned. If this parameter is not<br>provided or is `NONE`, nothing is returned.Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No       |

## Responses

### Syntax

The following syntax example assumes the request specified a
`ReturnValues` parameter of `ALL_OLD`;
otherwise, the response has only the `ConsumedCapacityUnits`
element.

```
HTTP/1.1 200
x-amzn-RequestId: 8966d095-71e9-11e0-a498-71d736f27375
content-type: application/x-amz-json-1.0
content-length: 85

{"Attributes":
	{"AttributeName3":{"S":"AttributeValue3"},
	"AttributeName2":{"SS":"AttributeValue2"},
	"AttributeName1":{"SS":"AttributeValue1"},
	},
"ConsumedCapacityUnits":1
}
```

| Name                    | Description                                                                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Attributes`            | Attribute values before the put operation, but only if the<br>`ReturnValues` parameter is specified<br>as `ALL_OLD` in the request.Type: Map of attribute name-value pairs.                                                                                                             |
| `ConsumedCapacityUnits` | The number of write capacity units consumed by the operation. This value shows the number<br>applied toward your provisioned throughput. For more information<br>see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").<br>Type: Number |

## Special errors

| Error                             | Description                                                          |
| --------------------------------- | -------------------------------------------------------------------- |
| `ConditionalCheckFailedException` | Conditional check failed. An expected attribute value was not found. |
| `ResourceNotFoundException`       | The specified item or attribute was not found.                       |

## Examples

For examples using the AWS SDK, see [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md").

### Sample request

```
// This header is abbreviated. For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.PutItem
content-type: application/x-amz-json-1.0

{"TableName":"comp5",
	"Item":
		{"time":{"N":"300"},
		"feeling":{"S":"not surprised"},
		"user":{"S":"Riley"}
		},
	"Expected":
		{"feeling":{"Value":{"S":"surprised"},"Exists":true}}
	"ReturnValues":"ALL_OLD"
}
```

### Sample response

```
HTTP/1.1 200
x-amzn-RequestId: 8952fa74-71e9-11e0-a498-71d736f27375
content-type: application/x-amz-json-1.0
content-length: 84

{"Attributes":
	{"feeling":{"S":"surprised"},
	"time":{"N":"300"},
	"user":{"S":"Riley"}},
"ConsumedCapacityUnits":1
}
```

## Related actions

- [UpdateItem](API_UpdateItem_v20111205.md "API_UpdateItem_v20111205.md")
- [DeleteItem](API_DeleteItem_v20111205.md "API_DeleteItem_v20111205.md")
- [GetItem](API_GetItem_v20111205.md "API_GetItem_v20111205.md")
- [BatchGetItem](API_BatchGetItem_v20111205.md "API_BatchGetItem_v20111205.md")
