# PipeSourceSelfManagedKafkaParameters

The parameters for using a self-managed Apache Kafka stream as a source.

A _self managed_ cluster refers to any Apache Kafka cluster not hosted by AWS.
This includes both clusters you manage yourself, as well as those hosted by a third-party
provider, such as [Confluent
Cloud](https://www.confluent.io/ "https://www.confluent.io/"), [CloudKarafka](https://www.cloudkarafka.com/ "https://www.cloudkarafka.com/"), or [Redpanda](https://redpanda.com/ "https://redpanda.com/"). For more information, see [Apache Kafka streams as a source](../userguide/eb-pipes-kafka.md "../userguide/eb-pipes-kafka.md") in the _Amazon EventBridge User Guide_.

## Contents

**TopicName**

The name of the topic that the pipe will read from.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 249.

Pattern: `[^.]([a-zA-Z0-9\-_.]+)`

Required: Yes

**AdditionalBootstrapServers**

An array of server URLs.

Type: Array of strings

Array Members: Minimum number of 0 items. Maximum number of 2 items.

Length Constraints: Minimum length of 1. Maximum length of 300.

Pattern: `(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}`

Required: No

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

Type: [SelfManagedKafkaAccessConfigurationCredentials](API_SelfManagedKafkaAccessConfigurationCredentials.md "API_SelfManagedKafkaAccessConfigurationCredentials.md") object

**Note:** This object is a Union. Only one member of this object can be specified or returned.

Required: No

**MaximumBatchingWindowInSeconds**

The maximum length of a time to wait for events.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 300.

Required: No

**ServerRootCaCertificate**

The ARN of the Secrets Manager secret used for certification.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?):(\d{12}):secret:.+)`

Required: No

**StartingPosition**

The position in a stream from which to start reading.

Type: String

Valid Values: `TRIM_HORIZON | LATEST`

Required: No

**Vpc**

This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.

Type: [SelfManagedKafkaAccessConfigurationVpc](API_SelfManagedKafkaAccessConfigurationVpc.md "API_SelfManagedKafkaAccessConfigurationVpc.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeSourceSelfManagedKafkaParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeSourceSelfManagedKafkaParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeSourceSelfManagedKafkaParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeSourceSelfManagedKafkaParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeSourceSelfManagedKafkaParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeSourceSelfManagedKafkaParameters.md")
