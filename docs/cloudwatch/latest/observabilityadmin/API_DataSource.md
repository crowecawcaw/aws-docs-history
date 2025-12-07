# DataSource

Information about a data source associated with the telemetry pipeline. For CloudWatch Logs sources,
this includes both a name and type extracted from the log event metadata. For third-party
sources (such as S3), this includes only a name, with the type field left empty.

## Contents

**Name**

The name of the data source. For CloudWatch Logs sources, this corresponds to the
`data_source_name` from the log event metadata. For third-party sources, this is
either the configured `data_source_name` or defaults to the plugin name if not
specified.

Type: String

Required: No

**Type**

The type of the data source. For CloudWatch Logs sources, this corresponds to the
`data_source_type` from the log event metadata. For third-party sources, this
field is empty.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/DataSource.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/DataSource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/DataSource.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/DataSource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/DataSource.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/DataSource.md")
