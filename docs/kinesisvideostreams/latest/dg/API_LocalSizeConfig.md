# LocalSizeConfig

The configuration details that include the maximum size of the media
(`MaxLocalMediaSizeInMB`) that you want to
store for a stream on the Edge Agent, as well as the strategy that should be used (`StrategyOnFullSize`) when a stream's
maximum size has been reached.

## Contents

**MaxLocalMediaSizeInMB**

The overall maximum size of the media that you want to store for a stream on the Edge Agent.

Type: Integer

Valid Range: Minimum value of 64. Maximum value of 2000000.

Required: No

**StrategyOnFullSize**

The strategy to perform when a stream’s `MaxLocalMediaSizeInMB` limit is reached.

Type: String

Valid Values: `DELETE_OLDEST_MEDIA | DENY_NEW_MEDIA`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/LocalSizeConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/LocalSizeConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/LocalSizeConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/LocalSizeConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/LocalSizeConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/LocalSizeConfig.md")
