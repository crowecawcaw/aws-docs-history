# SearchJobBackupsResult

This contains the information about recovery
points returned in results of a search job.

## Contents

**BackupCreationTime**

This is the creation time of the backup (recovery point).

Type: Timestamp

Required: No

**BackupResourceArn**

The Amazon Resource Name (ARN) that uniquely identifies
the backup resources.

Type: String

Required: No

**IndexCreationTime**

This is the creation time of the backup index.

Type: Timestamp

Required: No

**ResourceType**

This is the resource type of the search.

Type: String

Valid Values: `S3 | EBS`

Required: No

**SourceResourceArn**

The Amazon Resource Name (ARN) that uniquely identifies
the source resources.

Type: String

Required: No

**Status**

This is the status of the search job backup result.

Type: String

Valid Values: `RUNNING | COMPLETED | STOPPING | STOPPED | FAILED`

Required: No

**StatusMessage**

This is the status message included with the results.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/SearchJobBackupsResult.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/SearchJobBackupsResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/SearchJobBackupsResult.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/SearchJobBackupsResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/SearchJobBackupsResult.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/SearchJobBackupsResult.md")
