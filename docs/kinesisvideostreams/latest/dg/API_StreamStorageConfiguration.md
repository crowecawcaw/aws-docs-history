# StreamStorageConfiguration

The configuration for stream storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.

## Contents

**DefaultStorageTier**

The default storage tier for the stream data. This setting determines the storage class used for stream data, affecting both performance characteristics and storage costs.

Available storage tiers:

- `HOT` - Optimized for frequent access with the lowest latency and highest performance. Ideal for real-time applications and frequently accessed data.
- `WARM` - Balanced performance and cost for moderately accessed data. Suitable for data that is accessed regularly but not continuously.

Type: String

Valid Values: `HOT | WARM`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/StreamStorageConfiguration.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/StreamStorageConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/StreamStorageConfiguration.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/StreamStorageConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/StreamStorageConfiguration.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/StreamStorageConfiguration.md")
