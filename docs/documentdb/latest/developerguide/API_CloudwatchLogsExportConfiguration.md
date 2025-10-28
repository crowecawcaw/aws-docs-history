# CloudwatchLogsExportConfiguration

The configuration setting for the log types to be enabled for export to Amazon
CloudWatch Logs for a specific instance or cluster.

The `EnableLogTypes` and `DisableLogTypes` arrays determine
which logs are exported (or not exported) to CloudWatch Logs. The values within these
arrays depend on the engine that is being used.

## Contents

###### Note

In the following list, the required parameters are described first.

**DisableLogTypes.member.N**

The list of log types to disable.

Type: Array of strings

Required: No

**EnableLogTypes.member.N**

The list of log types to enable.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/CloudwatchLogsExportConfiguration.md "../../../goto/SdkForCpp/docdb-2014-10-31/CloudwatchLogsExportConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/CloudwatchLogsExportConfiguration.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/CloudwatchLogsExportConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/CloudwatchLogsExportConfiguration.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/CloudwatchLogsExportConfiguration.md")
