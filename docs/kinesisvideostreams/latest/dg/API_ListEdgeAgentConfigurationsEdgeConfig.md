# ListEdgeAgentConfigurationsEdgeConfig

A description of a single stream's edge configuration.

## Contents

**CreationTime**

The timestamp when the stream first created the edge config.

Type: Timestamp

Required: No

**EdgeConfig**

A description of the stream's edge configuration that will be used to sync
with the Edge Agent IoT Greengrass component. The Edge Agent component will run
on an IoT Hub Device setup at your premise.

Type: [EdgeConfig](API_EdgeConfig.md "API_EdgeConfig.md") object

Required: No

**FailedStatusDetails**

A description of the generated failure status.

Type: String

Required: No

**LastUpdatedTime**

The timestamp when the stream last updated the edge config.

Type: Timestamp

Required: No

**StreamARN**

The Amazon Resource Name (ARN) of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: No

**StreamName**

The name of the stream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

**SyncStatus**

The current sync status of the stream's edge configuration.

Type: String

Valid Values: `SYNCING | ACKNOWLEDGED | IN_SYNC | SYNC_FAILED | DELETING | DELETE_FAILED | DELETING_ACKNOWLEDGED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/ListEdgeAgentConfigurationsEdgeConfig.md")
