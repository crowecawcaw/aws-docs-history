# ChannelInfo

A structure that encapsulates a signaling channel's metadata and properties.

## Contents

**ChannelARN**

The Amazon Resource Name (ARN) of the signaling channel.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**ChannelName**

The name of the signaling channel.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**ChannelStatus**

Current status of the signaling channel.

Type: String

Valid Values: `CREATING | ACTIVE | UPDATING | DELETING`

Required: No

**ChannelType**

The type of the signaling channel.

Type: String

Valid Values: `SINGLE_MASTER | FULL_MESH`

Required: No

**CreationTime**

The time at which the signaling channel was created.

Type: Timestamp

Required: No

**SingleMasterConfiguration**

A structure that contains the configuration for the `SINGLE_MASTER` channel
type.

Type: [SingleMasterConfiguration](API_SingleMasterConfiguration.md "API_SingleMasterConfiguration.md") object

Required: No

**Version**

The current version of the signaling channel.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ChannelInfo.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ChannelInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ChannelInfo.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ChannelInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ChannelInfo.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ChannelInfo.md")
