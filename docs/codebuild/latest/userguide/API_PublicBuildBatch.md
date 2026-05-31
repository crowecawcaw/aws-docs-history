# PublicBuildBatch

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Contents

###### Note

In the following list, the required parameters are described first.

**artifacts**

Type: [PublicBuildArtifacts](API_PublicBuildArtifacts.md "API_PublicBuildArtifacts.md") object

Required: No

**buildBatchConfig**

Type: [PublicProjectBuildBatchConfig](API_PublicProjectBuildBatchConfig.md "API_PublicProjectBuildBatchConfig.md") object

Required: No

**buildBatchNumber**

Type: Long

Required: No

**buildBatchStatus**

Type: String

Valid Values: `PENDING | SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`

Required: No

**buildGroups**

Type: Array of [PublicBuildGroup](API_PublicBuildGroup.md "API_PublicBuildGroup.md") objects

Required: No

**buildTimeoutInMinutes**

Type: Integer

Required: No

**complete**

Type: Boolean

Required: No

**currentPhase**

Type: String

Required: No

**endTime**

Type: Timestamp

Required: No

**environment**

Type: [PublicProjectEnvironment](API_PublicProjectEnvironment.md "API_PublicProjectEnvironment.md") object

Required: No

**id**

Type: String

Length Constraints: Minimum length of 1.

Required: No

**initiator**

Type: String

Required: No

**logsStatus**

Type: [PublicLogsStatus](API_PublicLogsStatus.md "API_PublicLogsStatus.md") object

Required: No

**phases**

Type: Array of [BuildBatchPhase](../APIReference/API_BuildBatchPhase.md "../APIReference/API_BuildBatchPhase.md") objects

Required: No

**projectName**

Type: String

Length Constraints: Minimum length of 1.

Required: No

**publicBuildBatchAlias**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$`

Required: No

**queuedTimeoutInMinutes**

Type: Integer

Required: No

**resolvedSourceVersion**

Type: String

Length Constraints: Minimum length of 1.

Required: No

**secondaryArtifacts**

Type: Array of [PublicBuildArtifacts](API_PublicBuildArtifacts.md "API_PublicBuildArtifacts.md") objects

Required: No

**secondarySources**

Type: Array of [PublicProjectSource](API_PublicProjectSource.md "API_PublicProjectSource.md") objects

Array Members: Minimum number of 0 items. Maximum number of 12 items.

Required: No

**secondarySourceVersions**

Type: Array of [ProjectSourceVersion](../APIReference/API_ProjectSourceVersion.md "../APIReference/API_ProjectSourceVersion.md") objects

Array Members: Minimum number of 0 items. Maximum number of 12 items.

Required: No

**source**

Type: [PublicProjectSource](API_PublicProjectSource.md "API_PublicProjectSource.md") object

Required: No

**sourceVersion**

Type: String

Length Constraints: Minimum length of 1.

Required: No

**startTime**

Type: Timestamp

Required: No
