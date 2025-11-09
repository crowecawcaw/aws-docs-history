# BatchGetItem

###### Important

**`This section refers to API version 2011-12-05,
 which is deprecated and should not be used for new
 applications.`**

**For documentation on the current low-level API, see the
[Amazon DynamoDB API Reference](../APIReference.md "../APIReference.md").**

## Description

The `BatchGetItem` operation returns the attributes for multiple
items from multiple tables using their primary keys. The maximum number of items that
can be retrieved for a single operation is 100. Also, the number of items retrieved is
constrained by a 1 MB size limit. If the response size limit is exceeded or a partial
result is returned because the table’s provisioned throughput is exceeded, or because of
an internal processing failure, DynamoDB returns an `UnprocessedKeys`
value so you can retry the operation starting with the next item to get. DynamoDB
automatically adjusts the number of items returned per page to enforce this limit. For
example, even if you ask to retrieve 100 items, but each individual item is 50 KB in
size, the system returns 20 items and an appropriate
`UnprocessedKeys` value so you can get the next page of
results. If desired, your application can include its own logic to assemble the pages of
results into one set.

If no items could be processed because of insufficient provisioned throughput on each
of the tables involved in the request, DynamoDB returns a `ProvisionedThroughputExceededException` error.

###### Note

By default, `BatchGetItem` performs eventually consistent
reads on every table in the request. You can set the
`ConsistentRead` parameter to `true`,
on a per-table basis, if you want consistent reads instead.

`BatchGetItem` fetches items in parallel to minimize
response latencies.

When designing your application, keep in mind that DynamoDB does not guarantee how
attributes are ordered in the returned response. Include the primary key values in
the `AttributesToGet` for the items in your request to help
parse the response by item.

If the requested items do not exist, nothing is returned in the response for
those items. Requests for non-existent items consume the minimum read capacity units
according to the type of read. For more information, see [DynamoDB item sizes and formats](CapacityUnitCalculations.md "CapacityUnitCalculations.md").

## Requests

### Syntax

```
// This header is abbreviated. For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.BatchGetItem
content-type: application/x-amz-json-1.0

{"RequestItems":
    {"Table1":
        {"Keys":
            [{"HashKeyElement": {"S":"KeyValue1"}, "RangeKeyElement":{"N":"KeyValue2"}},
            {"HashKeyElement": {"S":"KeyValue3"}, "RangeKeyElement":{"N":"KeyValue4"}},
            {"HashKeyElement": {"S":"KeyValue5"}, "RangeKeyElement":{"N":"KeyValue6"}}],
        "AttributesToGet":["AttributeName1", "AttributeName2", "AttributeName3"]},
    "Table2":
        {"Keys":
            [{"HashKeyElement": {"S":"KeyValue4"}},
            {"HashKeyElement": {"S":"KeyValue5"}}],
        "AttributesToGet": ["AttributeName4", "AttributeName5", "AttributeName6"]
        }
    }
}
```

| Name                      | Description                                                                                                                                                                                                                                                   | Required |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `RequestItems`            | A container of the table name and corresponding items to get by primary key. While<br>requesting items, each table name can be invoked only once per<br>operation.Type: String Default:<br>None                                                               | Yes      |
| `Table`                   | The name of the table containing the items to get. The<br>entry is simply a string specifying an existing table with no<br>label.<br>Type: String<br>Default: None                                                                                            | Yes      |
| `Table`:`Keys`            | The primary key values that define the items in the<br>specified table. For more information about primary keys, see<br>[Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey").<br>Type: Keys | Yes      |
| `Table`:`AttributesToGet` | Array of Attribute names within the specified table. If<br>attribute names are not specified then all attributes will be<br>returned. If some attributes are not found, they will not appear<br>in the result.<br>Type: Array                                 | No       |
| `Table`:`ConsistentRead`  | If set to `true`, then a consistent read is issued, otherwise<br>eventually consistent is used.<br>Type: Boolean                                                                                                                                              | No       |

## Responses

### Syntax

```
HTTP/1.1 200
x-amzn-RequestId: 8966d095-71e9-11e0-a498-71d736f27375
content-type: application/x-amz-json-1.0
content-length: 855

{"Responses":
    {"Table1":
        {"Items":
        [{"AttributeName1": {"S":"AttributeValue"},
        "AttributeName2": {"N":"AttributeValue"},
        "AttributeName3": {"SS":["AttributeValue", "AttributeValue", "AttributeValue"]}
        },
        {"AttributeName1": {"S": "AttributeValue"},
        "AttributeName2": {"S": "AttributeValue"},
        "AttributeName3": {"NS": ["AttributeValue", "AttributeValue", "AttributeValue"]}
        }],
    "ConsumedCapacityUnits":1},
    "Table2":
        {"Items":
        [{"AttributeName1": {"S":"AttributeValue"},
        "AttributeName2": {"N":"AttributeValue"},
        "AttributeName3": {"SS":["AttributeValue", "AttributeValue", "AttributeValue"]}
        },
        {"AttributeName1": {"S": "AttributeValue"},
        "AttributeName2": {"S": "AttributeValue"},
        "AttributeName3": {"NS": ["AttributeValue", "AttributeValue","AttributeValue"]}
        }],
    "ConsumedCapacityUnits":1}
    },
    "UnprocessedKeys":
        {"Table3":
        {"Keys":
            [{"HashKeyElement": {"S":"KeyValue1"}, "RangeKeyElement":{"N":"KeyValue2"}},
            {"HashKeyElement": {"S":"KeyValue3"}, "RangeKeyElement":{"N":"KeyValue4"}},
            {"HashKeyElement": {"S":"KeyValue5"}, "RangeKeyElement":{"N":"KeyValue6"}}],
        "AttributesToGet":["AttributeName1", "AttributeName2", "AttributeName3"]}
        }
}
```

| Name                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Responses`                                         | Table names and the respective item attributes<br>from the tables.Type: Map                                                                                                                                                                                                                                                                                                                                                      |
| `Table`                                             | The name of the table containing the items. The entry is<br>simply a string specifying the table with no label.Type: String                                                                                                                                                                                                                                                                                                      |
| `Items`                                             | Container for the attribute names and values meeting the operation parameters.Type: Map of attribute names to and their data types and values.                                                                                                                                                                                                                                                                                   |
| `ConsumedCapacityUnits`                             | The number of read capacity units consumed, for each table. This value shows the number<br>applied toward your provisioned throughput. Requests for<br>non-existent items consume the minimum read capacity units,<br>depending on the type of read. For more information see [DynamoDB provisioned capacity mode](provisioned-capacity-mode.md "provisioned-capacity-mode.md").<br>Type: Number                                 |
| `UnprocessedKeys`                                   | Contains an array of tables and their respective keys that were<br>not processed with the current response, possibly due to reaching a<br>limit on the response size. The<br>`UnprocessedKeys` value is in the same form<br>as a `RequestItems` parameter (so the value can<br>be provided directly to a subsequent<br>`BatchGetItem` operation). For more<br>information, see the above `RequestItems`<br>parameter.Type: Array |
| `UnprocessedKeys`:<br>`Table`: `Keys`               | The primary key attribute values that define the items and the attributes associated with<br>the items. For more information about primary keys, see [Primary key](HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey "HowItWorks.md#HowItWorks.CoreComponents.PrimaryKey")<br>.Type: Array of attribute name-value pairs.                                                                                                       |
| `UnprocessedKeys`:<br>`Table`:<br>`AttributesToGet` | Attribute names within the specified table. If<br>attribute names are not specified then all attributes will be<br>returned. If some attributes are not found, they will not appear<br>in the result. Type: Array of attribute names.                                                                                                                                                                                            |
| `UnprocessedKeys`:<br>`Table`:<br>`ConsistentRead`  | If set to `true`, then a consistent read is used<br>for the specified table, otherwise an eventually consistent read<br>is used. Type: Boolean.                                                                                                                                                                                                                                                                                  |

## Special errors

| Error                                    | Description                                                    |
| ---------------------------------------- | -------------------------------------------------------------- |
| `ProvisionedThroughputExceededException` | Your maximum allowed provisioned throughput has been exceeded. |

## Examples

The following examples show an HTTP POST request and response using the BatchGetItem
operation. For examples using the AWS SDK, see [Working with items and attributes in DynamoDB](WorkingWithItems.md "WorkingWithItems.md").

### Sample request

The following sample requests attributes from two different tables.

```
// This header is abbreviated.
// For a sample of a complete header, see DynamoDB low-level API.
POST / HTTP/1.1
x-amz-target: DynamoDB_20111205.BatchGetItem
content-type: application/x-amz-json-1.0
content-length: 409

{"RequestItems":
    {"comp1":
        {"Keys":
            [{"HashKeyElement":{"S":"Casey"},"RangeKeyElement":{"N":"1319509152"}},
            {"HashKeyElement":{"S":"Dave"},"RangeKeyElement":{"N":"1319509155"}},
            {"HashKeyElement":{"S":"Riley"},"RangeKeyElement":{"N":"1319509158"}}],
        "AttributesToGet":["user","status"]},
    "comp2":
        {"Keys":
            [{"HashKeyElement":{"S":"Julie"}},{"HashKeyElement":{"S":"Mingus"}}],
        "AttributesToGet":["user","friends"]}
    }
}
```

### Sample response

The following sample is the response.

```
HTTP/1.1 200 OK
x-amzn-RequestId: GTPQVRM4VJS792J1UFJTKUBVV4KQNSO5AEMVJF66Q9ASUAAJG
content-type: application/x-amz-json-1.0
content-length: 373
Date: Fri, 02 Sep 2011 23:07:39 GMT

{"Responses":
    {"comp1":
        {"Items":
            [{"status":{"S":"online"},"user":{"S":"Casey"}},
            {"status":{"S":"working"},"user":{"S":"Riley"}},
            {"status":{"S":"running"},"user":{"S":"Dave"}}],
        "ConsumedCapacityUnits":1.5},
    "comp2":
        {"Items":
            [{"friends":{"SS":["Elisabeth", "Peter"]},"user":{"S":"Mingus"}},
            {"friends":{"SS":["Dave", "Peter"]},"user":{"S":"Julie"}}],
        "ConsumedCapacityUnits":1}
    },
    "UnprocessedKeys":{}
}
```
