# WAFLoggingParameters

Configuration parameters for WAF logging, including redacted fields and logging filters.

## Contents

**LoggingFilter**

A filter configuration that determines which WAF log records to include or exclude.

Type: [LoggingFilter](API_LoggingFilter.md "API_LoggingFilter.md") object

Required: No

**LogType**

The type of WAF logs to collect (currently supports WAF_LOGS).

Type: String

Valid Values: `WAF_LOGS`

Required: No

**RedactedFields**

The fields to redact from WAF logs to protect sensitive information.

Type: Array of [FieldToMatch](API_FieldToMatch.md "API_FieldToMatch.md") objects

Array Members: Minimum number of 0 items. Maximum number of 100 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/WAFLoggingParameters.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/WAFLoggingParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/WAFLoggingParameters.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/WAFLoggingParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/WAFLoggingParameters.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/WAFLoggingParameters.md")
