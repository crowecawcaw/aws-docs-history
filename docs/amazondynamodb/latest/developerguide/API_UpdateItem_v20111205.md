# UpdateItem

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

Edits an existing item's attributes. You can perform a conditional update (insert a new
attribute name-value pair if it doesn't exist, or replace an existing name-value pair if
it has certain expected attribute values).

###### Note

You cannot update the primary key attributes using UpdateItem. Instead, delete the item and
use PutItem to create a new item with new attributes.

The UpdateItem operation includes an `Action` parameter, which defines
how to perform the update. You can put, delete, or add attribute values.

Attribute values may not be null; string and binary type attributes must have lengths
greater than zero; and set type attributes must not be empty. Requests with empty values
will be rejected with a `ValidationException`.

If an existing item has the specified primary key:

- PUT— Adds the specified attribute. If the attribute
  exists, it is replaced by the new value.
- DELETE— If no value is specified, this removes the
  attribute and its value. If a set of values is specified, then the values in the
  specified set are removed from the old set. So if the attribute value contains
  [a,b,c] and the delete action contains [a,c], then the final attribute value is [b].
  The type of the specified value must match the existing value type. Specifying an
  empty set is not valid.
- ADD— Only use the add action for numbers or if the target
  attribute is a set (including string sets). ADD does not work if the target
  attribute is a single string value or a scalar binary value. The specified value
  is added to a numeric value (incrementing or decrementing the existing numeric
  value) or added as an additional value in a string set. If a set of values is
  specified, the values are added to the existing set. For example if the original
  set is [1,2] and supplied value is [3], then after the add operation the set is
  [1,2,3], not [4,5]. An error occurs if an Add action is specified for a set
  attribute and the attribute type specified does not match the existing set type.

If you use ADD for an attribute that does not exist, the attribute and its
values are added to the item.

If no item matches the specified primary key:

- PUT— Creates a new item with specified primary key. Then
  adds the specified attribute.
- DELETE— Nothing happens.
- ADD— Creates an item with supplied primary key and number
  (or set of numbers) for the attribute value. Not valid for a string or a binary
  type.

###### Note

If you use `ADD` to increment or decrement a number value for an item that doesn't
exist before the update, DynamoDB uses `0` as the initial value. Also, if
you update an item using `ADD` to increment or decrement a number value
for an attribute that doesn't exist before the update (but the item does) DynamoDB uses
`0` as the initial value. For example, you use `ADD` to
add `+3` to an attribute that did not exist before the update. DynamoDB uses
`0` for the initial value, and the value after the update is
`3`.

For more information about using this operation, see [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md").

## Requests

### Syntax

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.UpdateItem
content-type: application/x-amz-json-1.0

{"TableName":"Table1",
    "Key":
        {"HashKeyElement":{"S":"AttributeValue1"},
        "RangeKeyElement":{"N":"AttributeValue2"}},
    "AttributeUpdates":{"AttributeName3":{"Value":{"S":"AttributeValue3_New"},"Action":"PUT"}},
    "Expected":{"AttributeName3":{"Value":{"S":"AttributeValue3_Current"}}},
    "ReturnValues":"ReturnValuesConstant"
}
```

| Name                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Required |
| ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `TableName`                                      | The name of the table containing the item to update.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes      |
| `Key`                                            | The primary key that defines the item. For more information about primary keys, see<br>[Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").Type: Map of `HashKeyElement`<br>to its value and `RangeKeyElement` to its<br>value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Yes      |
| `AttributeUpdates`                               | Map of attribute name to the new value and action for the update. The attribute names<br>specify the attributes to modify, and cannot contain any primary key<br>attributes.Type: Map of attribute name, value, and an<br>action for the attribute update.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |          |
| `AttributeUpdates`:`Action`                      | Specifies how to perform the update. Possible values: `PUT` (default),<br>`ADD` or `DELETE`. The<br>semantics are explained in the UpdateItem description.Type: StringDefault: `PUT`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No       |
| `Expected`                                       | Designates an attribute for a conditional update. The `Expected`<br>parameter allows you to provide an attribute name, and whether<br>or not DynamoDB should check to see if the attribute value already<br>exists; or if the attribute value exists and has a particular<br>value before changing it.Type: Map of attribute names.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No       |
| `Expected:AttributeName`                         | The name of the attribute for the conditional put.Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No       |
| `Expected:AttributeName: ExpectedAttributeValue` | Use this parameter to specify whether or not a value already exists for the attribute<br>name-value pair. The following JSON notation updates the<br>item if the "Color" attribute doesn't already exist for that<br>item:<br>`<br>"Expected" :<br>{"Color":{"Exists":false}}<br>`<br>The<br>following JSON notation checks to see if the attribute with name<br>"Color" has an existing value of "Yellow" before updating the<br>item:<br>`<br>"Expected" :<br>{"Color":{"Exists":true},{"Value":{"S":"Yellow"}}}<br>`<br>By<br>default, if you use the `Expected`<br>parameter and provide a `Value`, DynamoDB<br>assumes the attribute exists and has a current value to be<br>replaced. So you don't have to specify<br>`{"Exists":true}`, because it is implied. You can<br>shorten the request to:<br>`<br>"Expected" :<br>{"Color":{"Value":{"S":"Yellow"}}}<br>`<br>NoteIf you specify `{"Exists":true}` without an<br>attribute value to check, DynamoDB returns an error. | No       |
| `ReturnValues`                                   | Use this parameter if you want to get the attribute name-value pairs before they were<br>updated with the `UpdateItem` request. Possible<br>parameter values are `NONE` (default) or<br>`ALL_OLD`, `UPDATED_OLD`,<br>`ALL_NEW` or<br>`UPDATED_NEW`. If `ALL_OLD` is<br>specified, and `UpdateItem` overwrote an attribute<br>name-value pair, the content of the old item is returned. If this<br>parameter is not provided or is `NONE`, nothing is<br>returned. If `ALL_NEW` is specified, then all the<br>attributes of the new version of the item are returned. If<br>`UPDATED_NEW` is specified, then the new<br>versions of only the updated attributes are returned.Type: String                                                                                                                                                                                                                                                                                            | No       |

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
content-length: 140

{"Attributes":{
	"AttributeName1":{"S":"AttributeValue1"},
	"AttributeName2":{"S":"AttributeValue2"},
	"AttributeName3":{"S":"AttributeValue3"},
	"AttributeName5":{"B":"dmFsdWU="}
	},
"ConsumedCapacityUnits":1
}
```

| Name                    | Description                                                                                                                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Attributes`            | A map of attribute name-value pairs, but only if the<br>`ReturnValues` parameter is specified as<br>something other than `NONE` in the request.Type: Map of attribute name-value pairs.                                                                                                 |
| `ConsumedCapacityUnits` | The number of write capacity units consumed by the operation. This value shows the number<br>applied toward your provisioned throughput. For more information<br>see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").<br>Type: Number |

## Special errors

| Error                             | Description                                                                                                  |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `ConditionalCheckFailedException` | Conditional check failed. Attribute ("+ name +") value is ("+ value +") but was<br>expected ("+ expValue +") |
| `ResourceNotFoundExceptions`      | The specified item or attribute was not found.                                                               |

## Examples

For examples using the AWS SDK, see [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md").

### Sample request

```
// This header is abbreviated. For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.UpdateItem
content-type: application/x-amz-json-1.0

{"TableName":"comp5",
    "Key":
        {"HashKeyElement":{"S":"Julie"},"RangeKeyElement":{"N":"1307654350"}},
    "AttributeUpdates":
        {"status":{"Value":{"S":"online"},
        "Action":"PUT"}},
    "Expected":{"status":{"Value":{"S":"offline"}}},
    "ReturnValues":"ALL_NEW"
}
```

### Sample response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 5IMHO7F01Q9P7Q6QMKMMI3R3QRVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 121
Date: Fri, 26 Aug 2011 21:05:00 GMT

{"Attributes":
    {"friends":{"SS":["Lynda, Aaron"]},
    "status":{"S":"online"},
    "time":{"N":"1307654350"},
    "user":{"S":"Julie"}},
"ConsumedCapacityUnits":1
}
```

## Related actions

- [PutItem](API_PutItem_v20111205.md "API_PutItem_v20111205.md")
- [DeleteItem](API_DeleteItem_v20111205.md "API_DeleteItem_v20111205.md")
