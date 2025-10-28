# CentralizationRuleSource

Configuration specifying the source of telemetry data to be centralized.

## Contents

**Regions**

The list of source regions from which telemetry data should be centralized.

Type: Array of strings

Array Members: Minimum number of 1 item.

Length Constraints: Minimum length of 1.

Required: Yes

**Scope**

The organizational scope from which telemetry data should be centralized, specified using
organization id, accounts or organizational unit ids.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

Required: No

**SourceLogsConfiguration**

Log specific configuration for centralization source log groups.

Type: [SourceLogsConfiguration](API_SourceLogsConfiguration.md "API_SourceLogsConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleSource.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/CentralizationRuleSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleSource.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/CentralizationRuleSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleSource.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/CentralizationRuleSource.md")
