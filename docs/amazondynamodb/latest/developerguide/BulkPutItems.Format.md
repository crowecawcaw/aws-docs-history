

# Amazon S3 input formats for bulk put items
<a name="BulkPutItems.Format"></a>

DynamoDB bulk put items reads input data from Amazon S3 in two formats: DynamoDB JSON and Amazon Ion. You can supply a single Amazon S3 object or multiple objects under the same [Amazon S3 key prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html).

Each input file can optionally contain per-item condition expressions that control whether items are written to the table. The following sections describe the supported formats, compression options, and the condition expression model.

**Topics**
+ [Supported formats and compression](#BulkPutItems.Format.Supported)
+ [DynamoDB JSON](#BulkPutItems.Format.DDBJson)
+ [Amazon Ion](#BulkPutItems.Format.Ion)
+ [Source data layout in Amazon S3](#BulkPutItems.Format.SourceData)
+ [Per-item condition expressions](#BulkPutItems.Format.Conditions)
+ [Condition failure reporting](#BulkPutItems.Format.Reporting)
+ [Validation errors that stop an object](#BulkPutItems.Format.ValidationErrors)

## Supported formats and compression
<a name="BulkPutItems.Format.Supported"></a>

Specify the input format when you call [StartBulkPutItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html) by setting the [InputFormat](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-InputFormat) field in [InputS3Configuration](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html), the request parameter that describes where your input is stored in Amazon S3 and how it is formatted. For all request parameters, see [Starting a bulk put items operation](BulkPutItems.Requesting.md#BulkPutItems.Requesting.Start).


| Format | Description | 
| --- | --- | 
| `DYNAMODB_JSON` | DynamoDB marshalled JSON. One JSON object per line ([JSON Lines](https://jsonlines.org/) format). Each line contains an `Item` field and optional condition fields. | 
| `ION` | Amazon Ion text format. Each record is an Ion struct containing an `Item` field and optional condition fields, delimited by newlines. | 

Set the [InputCompressionType](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-InputCompressionType) field to indicate how your Amazon S3 objects are compressed.


| Compression type | Description | 
| --- | --- | 
| `GZIP` | Objects are GZIP-compressed. | 
| `ZSTD` | Objects are Zstandard-compressed. | 
| `NONE` | Objects are uncompressed. | 

## DynamoDB JSON
<a name="BulkPutItems.Format.DDBJson"></a>

A file in DynamoDB JSON format consists of one JSON object per line ([JSON Lines](https://jsonlines.org/) format). Each line contains an `Item` field in DynamoDB marshalled JSON and optional condition fields. Do not use newlines within a single record. For how the condition fields work, see [Per-item condition expressions](#BulkPutItems.Format.Conditions).

**Unconditional put (default behavior)**

When you omit condition fields, each item overwrites any existing item with the same primary key:

```
{"Item":{"id":{"S":"item-1"},"name":{"S":"Widget A"},"price":{"N":"9.99"}}}
{"Item":{"id":{"S":"item-2"},"name":{"S":"Widget B"},"price":{"N":"14.99"}}}
{"Item":{"id":{"S":"item-3"},"name":{"S":"Widget C"},"price":{"N":"4.99"}}}
```

**Simple condition — insert only**

Add `attribute_not_exists({{pk}})` to prevent overwrites. Replace {{pk}} with the name of your partition key attribute:

```
{"Item":{"id":{"S":"item-1"},"name":{"S":"Widget A"},"price":{"N":"9.99"}},"ConditionExpression":"attribute_not_exists(id)"}
{"Item":{"id":{"S":"item-2"},"name":{"S":"Widget B"},"price":{"N":"14.99"}},"ConditionExpression":"attribute_not_exists(id)"}
```

**Named expression with substitution tokens**

Use `ExpressionAttributeNames` and `ExpressionAttributeValues` when your condition references reserved words or substitutes attribute values:

```
{"Item":{"id":{"S":"item-2"},"status":{"S":"ACTIVE"},"version":{"N":"3"}},"ConditionExpression":"#s = :v","ExpressionAttributeNames":{"#s":"status"},"ExpressionAttributeValues":{":v":{"S":"ACTIVE"}}}
{"Item":{"id":{"S":"item-5"},"status":{"S":"PENDING"},"version":{"N":"2"}},"ConditionExpression":"#ver < :newver","ExpressionAttributeNames":{"#ver":"version"},"ExpressionAttributeValues":{":newver":{"N":"2"}}}
```

In the first record, the item is written only if the existing item's `status` attribute equals `ACTIVE`. In the second record, the item is written only if the existing item's `version` is less than `2`.

**Mixed conditions in a single file**

Different records in the same file can carry different conditions, or no condition at all:

```
{"Item":{"id":{"S":"new-1"},"data":{"S":"hello"}},"ConditionExpression":"attribute_not_exists(id)"}
{"Item":{"id":{"S":"existing-1"},"data":{"S":"updated"}},"ConditionExpression":"#v = :expected","ExpressionAttributeNames":{"#v":"version"},"ExpressionAttributeValues":{":expected":{"N":"5"}}}
{"Item":{"id":{"S":"overwrite-1"},"data":{"S":"replaced"}}}
```

In this example, the first record uses insert-only semantics. The second record uses a version guard. The third record overwrites unconditionally because it has no condition.

## Amazon Ion
<a name="BulkPutItems.Format.Ion"></a>

[Amazon Ion](https://amzn.github.io/ion-docs/) is a richly typed, self-describing, hierarchical data serialization format. When you use Ion format for bulk put items, the Ion datatypes are mapped to DynamoDB datatypes in the target table.

Each record is an Ion struct containing an `Item` field and optional condition fields, delimited by newlines. Each line begins with an Ion version marker.

**Unconditional put**

**Note**  
In the following example, items are formatted on multiple lines to improve readability. In actual input files, each record is on a single line.

```
$ion_1_0
{
  Item:{
    id:"order-001",
    amount:99.95,
    status:"PENDING"
  }
}
$ion_1_0
{
  Item:{
    id:"order-002",
    amount:149.00,
    status:"SHIPPED"
  }
}
```

**With per-item condition expression**

```
$ion_1_0
{
  Item:{
    id:"order-001",
    amount:99.95,
    status:"PENDING"
  },
  ConditionExpression:"attribute_not_exists(id)"
}
$ion_1_0
{
  Item:{
    id:"order-002",
    amount:149.00,
    status:"SHIPPED"
  },
  ConditionExpression:"#s = :v",
  ExpressionAttributeNames:{"#s":"status"},
  ExpressionAttributeValues:{":v":"ACTIVE"}
}
```

The following table shows how Ion datatypes map to DynamoDB datatypes.


| Ion data type | DynamoDB representation | 
| --- | --- | 
| `string` | `String (S)` | 
| `bool` | `Boolean (BOOL)` | 
| `decimal` | `Number (N)` | 
| `blob` | `Binary (B)` | 
| `list` (with annotation `$dynamodb_SS`, `$dynamodb_NS`, or `$dynamodb_BS`) | `Set (SS, NS, BS)` | 
| `list` | `List (L)` | 
| `struct` | `Map (M)` | 

## Source data layout in Amazon S3
<a name="BulkPutItems.Format.SourceData"></a>

You can supply your input as a single Amazon S3 object or as multiple objects stored under the same S3 key prefix. When you set the [S3KeyPrefix](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_InputS3Configuration.html#DDB-Type-InputS3Configuration-S3KeyPrefix) field in `InputS3Configuration`, DynamoDB reads all objects under that S3 key prefix. For guidance on how to split your input, see [Best practices for bulk put items in DynamoDB](BulkPutItems.BestPractices.md).

**Note**  
All objects under the specified S3 key prefix must use the same format and the same compression type. You cannot mix DynamoDB JSON and Ion objects, or mix compressed and uncompressed objects, in a single bulk put items operation.

## Per-item condition expressions
<a name="BulkPutItems.Format.Conditions"></a>

Condition expressions for bulk put items are specified *per item, inside the input file*. They use the same syntax as condition expressions for the PutItem operation. For the full syntax, see [DynamoDB condition expression CLI example](Expressions.ConditionExpressions.md). For the supported operators and functions, see [Condition and filter expressions, operators, and functions in DynamoDB](Expressions.OperatorsAndFunctions.md).

Each record in your input file contains the following fields:
+ `Item` (required) — The item to write, in DynamoDB marshalled JSON or Ion format.
+ `ConditionExpression` (optional) — A condition expression that must evaluate to true for the item to be written.
+ `ExpressionAttributeNames` (optional) — A map of substitution tokens for attribute names in the condition expression.
+ `ExpressionAttributeValues` (optional) — A map of substitution tokens for attribute values in the condition expression.

### Condition evaluation behavior
<a name="BulkPutItems.Format.Conditions.Behaviour"></a>

The following table describes how DynamoDB evaluates condition expressions during a bulk put items operation.


| Scenario | Behavior | 
| --- | --- | 
| No condition on a record | The item is written unconditionally, overwriting any existing item with the same primary key. | 
| `attribute_not_exists({{pk}})` | Insert-only semantics for that record. The item is written only if no item with the same primary key already exists in the table. | 
| Per-item version guard | You can specify a condition that checks a version attribute, for example `#v = :expected`. This enables safe cross-Region migration and incremental synchronization use cases. To write both brand-new items and newer versions, use `attribute_not_exists(#v) OR #v < :new`. | 
| Condition not met | The item is skipped. DynamoDB reports the skipped item only if you request the `CONDITION_CHECK_FAILURE` output type. For more information, see [Condition failure reporting](#BulkPutItems.Format.Reporting). | 

**Important**  
Items that fail a condition check are still billed. For details, see [Billing for reports and failed items](BulkPutItems.Output.md#BulkPutItems.Output.Billing).

### To achieve semantics of inserting new items only
<a name="BulkPutItems.Format.Conditions.InsertOnly"></a>

Because conditions are per-item, you must include a `ConditionExpression` on every record if you want put-if-not-exists behavior across the entire file. The following example shows a DynamoDB JSON input file where every record carries `attribute_not_exists(id)` to prevent overwrites:

```
{"Item":{"id":{"S":"order-001"},"amount":{"N":"99.95"},"status":{"S":"PENDING"}},"ConditionExpression":"attribute_not_exists(id)"}
{"Item":{"id":{"S":"order-002"},"amount":{"N":"149.00"},"status":{"S":"SHIPPED"}},"ConditionExpression":"attribute_not_exists(id)"}
{"Item":{"id":{"S":"order-003"},"amount":{"N":"25.50"},"status":{"S":"DELIVERED"}},"ConditionExpression":"attribute_not_exists(id)"}
```

If you generate input files from an ETL pipeline, add the `ConditionExpression` field to your record template. If you have existing files without conditions, reprocess them to inject the condition before you start the operation.

## Condition failure reporting
<a name="BulkPutItems.Format.Reporting"></a>

When you configure your output Amazon S3 location, include `CONDITION_CHECK_FAILURE` in the [OutputType](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OutputS3Configuration.html#DDB-Type-OutputS3Configuration-OutputType) list. DynamoDB outputs records for items that did not satisfy their condition expression to your output Amazon S3 bucket. You can parse these output files to identify which items were skipped and take corrective action. When your input uses condition expressions, request `CONDITION_CHECK_FAILURE` so skipped items are reported, because without it DynamoDB keeps no record or count of them.

A retried or resumed operation can report a condition-check conflict for an item the operation itself wrote earlier. To tell this apart from a conflict with pre-existing data, compare the existing image in the report with the item you supplied. If they are equal, the operation wrote that item and the conflict is expected.

Items reported here were not written on the attempt that produced the record. They are still billed. For more information, see [Billing for reports and failed items](BulkPutItems.Output.md#BulkPutItems.Output.Billing). To reconcile the results of a bulk put items operation, use the Amazon S3 output files together with the [DescribeBulkOperation](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeBulkOperation.html) counts. For the full workflow, see [Reconciling results](BulkPutItems.Output.md#BulkPutItems.Output.Reconciliation).

## Validation errors that stop an object
<a name="BulkPutItems.Format.ValidationErrors"></a>

Some errors prevent DynamoDB from locating the next record boundary. These errors include malformed or truncated JSON or Ion, invalid record structure, a missing or duplicate `Item` field, an unknown top-level field, invalid DynamoDB values, invalid UTF-8, input that reaches the parser's nesting limit, a record that exceeds the parser's read limit, decompression errors, a compression mismatch, and some Amazon S3 object-read errors. A record may contain only these top-level fields: `Item`, `ConditionExpression`, `ExpressionAttributeNames`, and `ExpressionAttributeValues`.

When one of these errors occurs, DynamoDB produces one error result and stops reading that Amazon S3 object. Other input objects can continue. If you requested `ERROR` output, the report row contains `itemLocation.inputSourceArn` and `errorMessages`, but it does not contain `itemLocation.itemIndex`. A validation error that applies to one complete record includes `itemIndex` and does not stop the rest of the object.

The completion manifest marks the object `PARTIALLY_PROCESSED` and lists completed records in `processedRanges`. If DynamoDB cannot confirm that it read all stored input bytes, the operation ends `FAILED` with failure code `ValidationException`. If DynamoDB read all stored bytes before detecting the error, the operation can end `COMPLETED_WITH_ERRORS` with [ProcessedInputBytes](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-ProcessedInputBytes) equal to [TotalInputBytes](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BulkOperationDescription.html#DDB-Type-BulkOperationDescription-TotalInputBytes). Use the final status, `ERROR` report, and completion manifest together to identify records to correct or resubmit. DynamoDB doesn't bill records that validation rejects as table writes. For more information, see [Billing for reports and failed items](BulkPutItems.Output.md#BulkPutItems.Output.Billing).