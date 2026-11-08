

# Working with bulk put items
<a name="BulkPutItems.HowItWorks"></a>

Bulk put items loads data from Amazon Simple Storage Service (Amazon S3) into an existing Amazon DynamoDB table. The writes run on a separate path and consume none of the table's read or write capacity, so your application traffic sees no impact from these bulk put items. Items become available for reading as they're written. [Import from Amazon S3](S3DataImport.HowItWorks.md) creates a new table from data in Amazon S3, while bulk put items writes into a table that already exists.

## How a bulk put items operation works
<a name="BulkPutItems.HowItWorks.Shape"></a>

To start a bulk put items operation, you provide the following:
+ The Amazon S3 location of your input files
+ The target DynamoDB table
+ An Amazon S3 location for the output report
+ (Optional) A performance tier, either `STANDARD` (default) or `ACCELERATED`

DynamoDB reads your S3 objects, writes each item to the table, handles retries and exception cases, and outputs a report to your output Amazon S3 location. The report lists items that were not written and the reason for their failure. Each operation is subject to limits on the number of input objects, the size of each object, and the total input size. For the values, see [Quotas for bulk put items](ServiceQuotas.md#limits-bulk-put-items).

Depending on your requirements, you can choose between two performance tiers. If you do not specify one, the operation uses Standard. For more information, see [Performance tiers](BulkPutItems.Tiers.md).

You can specify a condition expression on each item in the input file. The condition must evaluate to true for the item to be written. Otherwise, the item is skipped. For example, you can use `attribute_not_exists({{pk}})` for insert-only semantics, or a version-attribute guard for conditional overwrites. Condition expressions use the same syntax, operators, and functions as `PutItem`. For the supported operators and functions, see [Condition and filter expressions, operators, and functions in DynamoDB](Expressions.OperatorsAndFunctions.md). Skipped items are reported in your output when you request them. For more information, see [Per-item condition expressions](BulkPutItems.Format.md#BulkPutItems.Format.Conditions). For details on the input file format, see [Amazon S3 input formats for bulk put items](BulkPutItems.Format.md).

When no condition expression is specified on a record, the item is written unconditionally, overwriting any existing item with the same key.

**Topics**
+ [How a bulk put items operation works](#BulkPutItems.HowItWorks.Shape)
+ [Performance tiers](BulkPutItems.Tiers.md)
+ [Input formats](BulkPutItems.Format.md)
+ [Running a bulk put items operation](BulkPutItems.Requesting.md)
+ [Output and reconciliation](BulkPutItems.Output.md)
+ [Considerations and quotas](BulkPutItems.Considerations.md)
+ [Best practices](BulkPutItems.BestPractices.md)