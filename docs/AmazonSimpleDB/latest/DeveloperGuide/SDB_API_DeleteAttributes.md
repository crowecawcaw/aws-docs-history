# DeleteAttributes

## Description

Deletes one or more attributes associated with the item. If all attributes of an item are
deleted, the item is deleted.

###### Note

If you specify `DeleteAttributes` without attributes or values, all
the attributes for the item are deleted.

Unless you specify conditions, the `DeleteAttributes` is an idempotent operation; running it multiple
times on the same item or attribute does _not_ result in an error
response.

Conditional deletes are useful for only deleting items and attributes if specific conditions are met.
If the conditions are met, Amazon SimpleDB performs the delete. Otherwise, the data is not deleted.

When using _eventually consistent_ reads, a
[GetAttributes](SDB_API_GetAttributes.md "SDB_API_GetAttributes.md")
or [Select](SDB_API_Select.md "SDB_API_Select.md") request
(read) immediately after a
[DeleteAttributes](SDB_API_DeleteAttributes.md "SDB_API_DeleteAttributes.md") or
[PutAttributes](SDB_API_PutAttributes.md "SDB_API_PutAttributes.md") request
(write) might not return the updated data. A _consistent read_ always reflects all
writes that received a successful response prior to the read. For more information, see
[Consistency](ConsistencySummary.md "ConsistencySummary.md").

You can perform the expected conditional check on one attribute per operation.

## Request Parameters

| Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Required    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `ItemName`          | The name of the item.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes         |
| `Attribute.X.Name`  | The name of the _attribute_. X can be any positive integer or<br>0. If you specify `DeleteAttributes` without<br>attribute names or values, all the attributes for the item are<br>deleted.<br>Type: String                                                                                                                                                                                                                                                                                                                                           | No          |
| `Attribute.X.Value` | The name of the attribute value (for _multi-valued<br>attributes_). X can be any positive integer or 0. If an<br>attribute value is specified, then the corresponding attribute name<br>is required.<br>Type: String                                                                                                                                                                                                                                                                                                                                  | No          |
| `DomainName`        | The name of the domain in which to perform the operation.<br>Type: String                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes         |
| `Expected.Name`     | Name of the attribute to check.<br>Type: String.<br>Conditions: Must be used with the expected value or expected exists parameter.<br>When used with the expected value parameter, you specify the value to check.<br>When expected exists is set to `true` and it is used with the expected value parameter,<br>it performs similarly to just using the expected value parameter. When expected exists is set to<br>`false`, the operation is performed if the expected attribute is not present.<br>Can only be used with single-valued attributes. | Conditional |
| `Expected.Value`    | Value of the attribute to check.<br>Type: String.<br>Conditions: Must be used with the expected name parameter.<br>Can be used with the expected exists parameter if that parameter is set to `true`.<br>Can only be used with single-valued attributes.                                                                                                                                                                                                                                                                                              | Conditional |
| `Expected.Exists`   | Flag to test the existence of an attribute while performing conditional<br>updates.<br>Type: Boolean.<br>Conditions: Must be used with the expected name parameter. When set to `true`,<br>this must be used with the expected value parameter. When set to `false`, this cannot<br>be used with the expected value parameter.<br>Can only be used with single-valued attributes.                                                                                                                                                                     | Conditional |

## Response Elements

See [Common Response Elements](SDB_API_CommonResponseElements.md "SDB_API_CommonResponseElements.md").

## Special Errors

| Error                          | Description                                                                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `AttributeDoesNotExist`        | Attribute ("+ name + ") does not exist.                                                                                       |
| `ConditionalCheckFailed`       | Conditional check failed. Attribute (" + name + ") value exists.                                                              |
| `ConditionalCheckFailed`       | Conditional check failed. Attribute ("+ name +") value is ("+ value +") but was<br>expected ("+ expValue +").                 |
| `ExistsAndExpectedValue`       | `Expected.Exists=false` and<br>`Expected.Value` cannot be specified<br>together.                                              |
| `IncompleteExpectedExpression` | If `Expected.Exists=true` or unspecified, then<br>`Expected.Value` has to be specified.                                       |
| `InvalidParameterValue`        | Value (" + value + ") for parameter `Expected.Exists` is<br>invalid. `Expected.Exists` should be either<br>`true` or `false`. |
| `InvalidParameterValue`        | Value (" + value + ") for parameter `Name` is invalid.The empty<br>string is an illegal attribute name.                       |
| `InvalidParameterValue`        | Value (" + value + ") for parameter `Name` is invalid. Value<br>exceeds maximum length of 1024.                               |
| `InvalidParameterValue`        | Value (" + value + ") for parameter `Value` is invalid.<br>Value exceeds maximum length of 1024.                              |
| `InvalidParameterValue`        | Value (" + value + ") for parameter `Item` is invalid.<br>Value exceeds max length of 1024.                                   |
| `InvalidWSDLVersion`           | Parameter (" + parameterName +") is only supported in WSDL version 2009-04-15 or<br>beyond. Please upgrade to new version.    |
| `MissingParameter`             | The request must contain the parameter<br>`DomainName`.                                                                       |
| `MissingParameter`             | The request must contain the parameter<br>`ItemName`.                                                                         |
| `MissingParameter`             | The request must contain the attribute `Name`, if an attribute<br>`Value` is specified.                                       |
| `MultipleExistsConditions`     | Only one `Exists` condition can be specified.                                                                                 |
| `MultipleExpectedNames`        | Only one `Expected.Name` can be specified.                                                                                    |
| `MultipleExpectedValues`       | Only one `Expected.Value` can be specified.                                                                                   |
| `MultiValuedAttribute`         | Attribute (" + name + ") is multi-valued. Conditional check can only be performed on<br>a single-valued attribute.            |
| `NoSuchDomain`                 | The specified domain does not exist.                                                                                          |

## Examples

### Sample Request

In this example, the Jumbo Fez has sold out in several colors. The following deletes the
`red`, `brick`, and `garnet` values from the
`color` attribute of the `JumboFez` item.

```

https://sdb.amazonaws.com/
?Action=DeleteAttributes
&Attribute.1.Name=color
&Attribute.1.Value=red
&Attribute.2.Name=color
&Attribute.2.Value=brick
&Attribute.3.Name=color
&Attribute.3.Value=garnet
&AWSAccessKeyId=[valid access key id]
&DomainName=MyDomain
&ItemName=JumboFez
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

### Sample Response

```

**<DeleteAttributesResponse">**
  **<ResponseMetadata>**
    **<RequestId>**05ae667c-cfac-41a8-ab37-a9c897c4c3ca**</RequestId>**
    **<BoxUsage>**0.0000219907**</BoxUsage>**
  **</ResponseMetadata>**
**</DeleteAttributesResponse>**

```

### Sample Request

In this example, the Micro Fez has sold out. The following deletes the Micro Fez if the
quantity reaches 0

###### Note

For more examples of conditional operations, see
[Conditionally Putting and Deleting Data](ConditionalPutDelete.md "ConditionalPutDelete.md").

```

https://sdb.amazonaws.com/
?Action=DeleteAttributes
&ItemName=MicroFez
&Expected.Name=quantity
&Expected.Value=0
&SignatureVersion=2
&SignatureMethod=HmacSHA256
&Timestamp=2010-01-25T15%3A03%3A07-07%3A00
&Version=2009-04-15
&Signature=[valid signature]

```

### Sample Response

```

**<DeleteAttributesResponse>**
  **<ResponseMetadata>**
    **<RequestId>**05ae667c-cfac-41a8-ab37-a9c897c4c3ca**</RequestId>**
    **<BoxUsage>**0.0000219907**</BoxUsage>**
  **</ResponseMetadata>**
**</DeleteAttributesResponse>**

```

## Related Actions

- [BatchDeleteAttributes](SDB_API_BatchDeleteAttributes.md "SDB_API_BatchDeleteAttributes.md")
- [GetAttributes](SDB_API_GetAttributes.md "SDB_API_GetAttributes.md")
- [PutAttributes](SDB_API_PutAttributes.md "SDB_API_PutAttributes.md")
