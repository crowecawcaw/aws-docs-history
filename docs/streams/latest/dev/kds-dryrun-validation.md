

# Test your permissions and request inputs with dry run
<a name="kds-dryrun-validation"></a>

You can use the `DryRun` parameter with Kinesis Data Streams data plane APIs to verify that you have the required permissions and that your request parameters are valid. This validation occurs before you run the operation on an Amazon Kinesis Data Streams resource. When you set `DryRun` to true, Kinesis Data Streams validates that you have the required IAM permissions to access your stream, checks your request parameters, and confirms that the target resource exists. It performs these checks without running the operation or reading or writing any data.

If all checks pass, the API returns HTTP 400 with a `DryRunOperationException`, confirming that the request would have succeeded without the `DryRun` parameter. If any check fails, the API returns the same error that the actual operation would return (for example, `AccessDeniedException`). You can receive the following exceptions, among others:
+ `DryRunOperationException` – The request would have succeeded without the `DryRun` parameter.
+ `AccessDeniedException` – The caller does not have the required IAM permissions for the API action.
+ `ResourceNotFoundException` – The specified stream or consumer does not exist.
+ `ValidationException` – One or more request parameters are invalid (for example, missing required fields, malformed ARN).
+ `InvalidArgumentException` – A parameter value is out of range or not supported (for example, invalid ShardIteratorType, future timestamp).

Requests with `DryRun` enabled are subject to a dedicated throttle limit of 1 transaction per second (TPS) per stream, separate from the stream's normal per-shard throughput limits. This limit is shared across all supported dry-run APIs (`PutRecord`, `PutRecords`, `GetRecords`, `GetShardIterator`, and `SubscribeToShard`) on the same stream. If you exceed this limit, the API returns a `ThrottlingException`.

There is no additional charge for using the `DryRun` parameter. Requests with `DryRun` enabled are billed the same as the equivalent request with `DryRun` disabled. For example, for `PutRecord` and `PutRecords`, you are charged based on the input payload size in Provisioned mode. Any charges for the stream and shard-hours continue to apply. For more information about pricing, see [Amazon Kinesis Data Streams pricing](https://aws.amazon.com/kinesis/data-streams/pricing/).

**Note**  
The `DryRun` parameter validates IAM permissions for the Kinesis Data Streams API actions. It does not validate AWS Key Management Service key permissions for encrypted streams. If your stream uses server-side encryption with a customer managed AWS KMS key, you must separately verify that your producers have `kms:GenerateDataKey` permission and your consumers have `kms:Decrypt` permission on the AWS KMS key. To validate AWS KMS permissions, see [Testing your permissions](https://docs.aws.amazon.com/kms/latest/developerguide/) in the AWS Key Management Service Developer Guide.

## Supported APIs
<a name="kds-dryrun-validation-supported-apis"></a>

The `DryRun` parameter is supported for the following APIs:
+ [`PutRecord`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html)
+ [`PutRecords`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecords.html)
+ [`GetRecords`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetRecords.html)
+ [`GetShardIterator`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html)
+ [`SubscribeToShard`](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_SubscribeToShard.html)

## AWS CloudTrail logging
<a name="kds-dryrun-validation-cloudtrail"></a>

If you enable data events in AWS CloudTrail, AWS CloudTrail logs data plane API calls that use the `DryRun` parameter set to true. The corresponding CloudTrail event includes the `DryRun` parameter in the request, and the errorCode field shows `DryRunOperationException` for successful validations.

## Using dry run with the AWS CLI
<a name="kds-dryrun-validation-cli"></a>

Specify the `--dry-run` flag in your AWS CLI commands.

Example: Testing PutRecord permissions

```
aws kinesis put-record \
    --stream-name <your-stream-name> \
    --data <your-data-payload> \
    --partition-key <your-partition-key> \
    --dry-run
```

If the request would have succeeded, the response includes the following message: `DryRunOperation validation succeeded while calling PutRecord operation.: Request would have succeeded, but DryRun flag is set.`

## Using dry run with AWS SDKs
<a name="kds-dryrun-validation-sdk"></a>

### Python (Boto3)
<a name="kds-dryrun-validation-sdk-python"></a>

```
import boto3
from botocore.exceptions import ClientError

kinesis = boto3.client('kinesis')

try:
    kinesis.put_record(
        StreamName='my-stream',
        Data=b'test-data',
        PartitionKey='my-partition-key',
        DryRun=True
    )
except ClientError as e:
    if e.response['Error']['Code'] == 'DryRunOperationException':
        print('SUCCESS: Request would have succeeded')
    else:
        print(f'FAILURE: {e.response["Error"]["Code"]}')
```

### Java (AWS SDK for Java 2.x)
<a name="kds-dryrun-validation-sdk-java"></a>

```
PutRecordRequest request = PutRecordRequest.builder()
    .streamName("my-stream")
    .data(SdkBytes.fromUtf8String("test-data"))
    .partitionKey("my-partition-key")
    .dryRun(true)
    .build();

try {
    kinesisClient.putRecord(request);
} catch (DryRunOperationException e) {
    System.out.println("SUCCESS: " + e.getMessage());
} catch (AccessDeniedException e) {
    System.out.println("FAILURE: " + e.getMessage());
}
```