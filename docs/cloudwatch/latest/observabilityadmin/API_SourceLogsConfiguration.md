# SourceLogsConfiguration

Configuration for selecting and handling source log groups for centralization.

## Contents

**EncryptedLogGroupStrategy**

A strategy determining whether to centralize source log groups that are encrypted with
customer managed KMS keys (CMK). ALLOW will consider CMK encrypted source log groups for
centralization while SKIP will skip CMK encrypted source log groups from
centralization.

Type: String

Valid Values: `ALLOW | SKIP`

Required: Yes

**LogGroupSelectionCriteria**

The selection criteria that specifies which source log groups to centralize. The selection
criteria uses the same format as OAM link filters.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/SourceLogsConfiguration.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/SourceLogsConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/SourceLogsConfiguration.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/SourceLogsConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/SourceLogsConfiguration.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/SourceLogsConfiguration.md")
