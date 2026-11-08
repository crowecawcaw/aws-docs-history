

# Best practices for bulk put items in DynamoDB
<a name="BulkPutItems.BestPractices"></a>

The following are the best practices for using bulk put items.

## Split your input across multiple similarly sized S3 objects
<a name="BulkPutItems.BestPractices.SplitInput"></a>

DynamoDB reads and processes S3 objects in parallel, so a set of similarly sized objects completes faster than one large object or a mix of very large and very small objects. Each operation supports up to 50,000 S3 objects, and each object can be up to 5 GB. If your dataset has more than 50,000 objects, consolidate them into fewer, larger objects.

## Stay within the size limit for your performance tier
<a name="BulkPutItems.BestPractices.SizeLimit"></a>

Each performance tier has its own limit on the total input size of one operation. To load a dataset larger than the limit, split it into multiple operations, or use the Accelerated performance tier if your table supports it. For the limits, see [Quotas for bulk put items](ServiceQuotas.md#limits-bulk-put-items).

## Distribute writes evenly across the key space
<a name="BulkPutItems.BestPractices.DistributeKeys"></a>

Bulk put items performs best when your data has high-cardinality partition keys that are spread evenly across the key space. If an S3 object holds items sorted by partition key, consecutive writes target the same partition, which creates a rolling hot partition and slows the operation. Randomize the order of sorted data before you start the operation. For more information, see [Distributing write activity efficiently during data upload in DynamoDB](bp-partition-key-data-upload.md).

## Validate your input before you start
<a name="BulkPutItems.BestPractices.ValidateInput"></a>

Run a validation pass on a sample of your files before you submit a large operation, because a single record that DynamoDB cannot parse stops it reading the rest of that object, and can end the whole operation `FAILED`. For the conditions that stop an object, see [Validation errors that stop an object](BulkPutItems.Format.md#BulkPutItems.Format.ValidationErrors).

## Use condition expressions to protect existing data
<a name="BulkPutItems.BestPractices.Conditions"></a>

If you must not overwrite existing or newer data, add an insert-only condition or a version guard to every record, including keys that your application writes while the operation runs. For the syntax and examples, see [Per-item condition expressions](BulkPutItems.Format.md#BulkPutItems.Format.Conditions) and [Concurrent writes to the same keys](BulkPutItems.Considerations.md#BulkPutItems.Considerations.ConcurrentWrites).

## Do not modify S3 objects during an active operation
<a name="BulkPutItems.BestPractices.NoModification"></a>

Keep your source S3 objects unchanged while an operation is in progress. Modifying an input object can cause the operation to fail with failure code `ObjectModifiedInS3DuringImport`. Wait for the operation to finish before you change the source files, and restart it with a stable version of the objects if you see this error.

## Use a client token when you retry a start request
<a name="BulkPutItems.BestPractices.ClientToken"></a>

Pass a [ClientToken](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-ClientToken) with [StartBulkPutItems](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html) whenever you might retry the request, so that a retry returns the existing operation instead of starting a second one. For how the token works, see [Starting a bulk put items operation](BulkPutItems.Requesting.md#BulkPutItems.Requesting.Start).

## Protect downstream stream consumers
<a name="BulkPutItems.BestPractices.Streams"></a>

On a table with DynamoDB Streams or a Kinesis data stream enabled, every bulk write produces a stream record at the operation write rate. Consumers sized for normal traffic can fall behind. DynamoDB Streams retains records for 24 hours. Set [MaxWriteRequestUnits](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_StartBulkPutItems.html#DDB-StartBulkPutItems-request-MaxWriteRequestUnits) to cap the bulk put items write rate at a level your consumers can sustain.

Do not set `MaxWriteRequestUnits` lower than you need. A low cap slows the operation, so a large operation might not finish within the maximum processing time and ends `FAILED` with failure code `Timeout`, leaving the remaining items unwritten. Choose the highest rate your consumers can sustain. For more information, see [Status values](BulkPutItems.Requesting.md#BulkPutItems.Requesting.Describe.Status).