# ReportOverrides

The level of detail included in each aspect of your DataSync
[task
report](task-reports.md "task-reports.md").

## Contents

**Deleted**

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location. This only applies if you [configure your
task](configure-metadata.md "configure-metadata.md") to delete data in the destination that isn't in the source.

Type: [ReportOverride](API_ReportOverride.md "API_ReportOverride.md") object

Required: No

**Skipped**

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.

Type: [ReportOverride](API_ReportOverride.md "API_ReportOverride.md") object

Required: No

**Transferred**

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.

Type: [ReportOverride](API_ReportOverride.md "API_ReportOverride.md") object

Required: No

**Verified**

Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify at the end of your transfer.

Type: [ReportOverride](API_ReportOverride.md "API_ReportOverride.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ReportOverrides.md "../../../goto/SdkForCpp/datasync-2018-11-09/ReportOverrides.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportOverrides.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportOverrides.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportOverrides.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportOverrides.md")
