# PipeSourceManagedStreamingKafkaParameters

The parameters for using an MSK stream as a source.

## Contents

**TopicName**

The name of the topic that the pipe will read from.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 249.

Pattern: `[^.]([a-zA-Z0-9\-_.]+)`

Required: Yes

**BatchSize**

The maximum number of records to include in each batch.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 10000.

Required: No

**ConsumerGroupID**

The name of the destination queue to consume.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 200.

Pattern: `[a-zA-Z0-9-\/*:_+=.@-]*`

Required: No

**Credentials**

The credentials needed to access the resource.

Type: [MSKAccessCredentials](API_MSKAccessCredentials.md "API_MSKAccessCredentials.md") object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

**MaximumBatchingWindowInSeconds**

The maximum length of a time to wait for events.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 300.

Required: No

**StartingPosition**

The position in a stream from which to start reading.

Type: String

Valid Values: `TRIM_HORIZON | LATEST`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeSourceManagedStreamingKafkaParameters.md")
