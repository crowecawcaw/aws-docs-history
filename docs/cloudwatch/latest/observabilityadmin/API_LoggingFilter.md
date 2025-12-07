# LoggingFilter

Configuration that determines which WAF log records to keep or drop based on specified
conditions.

## Contents

**DefaultBehavior**

The default action (KEEP or DROP) for log records that don't match any filter conditions.

Type: String

Valid Values: `KEEP | DROP`

Required: No

**Filters**

A list of filter conditions that determine log record handling behavior.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/LoggingFilter.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/LoggingFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/LoggingFilter.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/LoggingFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/LoggingFilter.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/LoggingFilter.md")
