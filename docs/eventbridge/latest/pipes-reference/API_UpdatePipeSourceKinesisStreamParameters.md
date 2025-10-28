# UpdatePipeSourceKinesisStreamParameters

The parameters for using a Kinesis stream as a source.

## Contents

**BatchSize**

The maximum number of records to include in each batch.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10000.

Required: No

**DeadLetterConfig**

Define the target queue to send dead-letter queue events to.

Type: [DeadLetterConfig](API_DeadLetterConfig.md "API_DeadLetterConfig.md") object

Required: No

**MaximumBatchingWindowInSeconds**

The maximum length of a time to wait for events.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 300.

Required: No

**MaximumRecordAgeInSeconds**

Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite.
When the value is set to infinite, EventBridge never discards old records.

Type: Integer

Valid Range: Minimum value of -1. Maximum value of 604800.

Required: No

**MaximumRetryAttempts**

Discard records after the specified number of retries. The default value is -1, which sets the maximum number of
retries to infinite. When MaximumRetryAttempts is infinite, EventBridge retries failed records until the record expires in the event source.

Type: Integer

Valid Range: Minimum value of -1. Maximum value of 10000.

Required: No

**OnPartialBatchItemFailure**

Define how to handle item process failures. `AUTOMATIC_BISECT` halves each batch and retry each half
until all the records are processed or there is one failed message left in the batch.

Type: String

Valid Values: `AUTOMATIC_BISECT`

Required: No

**ParallelizationFactor**

The number of batches to process concurrently from each shard. The default value is 1.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceKinesisStreamParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/UpdatePipeSourceKinesisStreamParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceKinesisStreamParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/UpdatePipeSourceKinesisStreamParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceKinesisStreamParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/UpdatePipeSourceKinesisStreamParameters.md")
