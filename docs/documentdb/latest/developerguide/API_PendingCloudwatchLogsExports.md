# PendingCloudwatchLogsExports

A list of the log types whose configuration is still pending. These log types are in
the process of being activated or deactivated.

## Contents

###### Note

In the following list, the required parameters are described first.

**LogTypesToDisable.member.N**

Log types that are in the process of being enabled. After they are enabled, these log
types are exported to Amazon CloudWatch Logs.

Type: Array of strings

Required: No

**LogTypesToEnable.member.N**

Log types that are in the process of being deactivated. After they are deactivated,
these log types aren't exported to CloudWatch Logs.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/PendingCloudwatchLogsExports.md "../../../goto/SdkForCpp/docdb-2014-10-31/PendingCloudwatchLogsExports.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/PendingCloudwatchLogsExports.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/PendingCloudwatchLogsExports.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/PendingCloudwatchLogsExports.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/PendingCloudwatchLogsExports.md")
