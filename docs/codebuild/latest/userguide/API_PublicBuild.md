# PublicBuild

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Contents

###### Note

In the following list, the required parameters are described first.

**artifacts**

Type: [PublicBuildArtifacts](API_PublicBuildArtifacts.md "API_PublicBuildArtifacts.md") object

Required: No

**buildComplete**

Type: Boolean

Required: No

**buildNumber**

Type: Long

Required: No

**buildStatus**

Type: String

Valid Values: `PENDING | SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`

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

Type: Array of [BuildPhase](../APIReference/API_BuildPhase.md "../APIReference/API_BuildPhase.md") objects

Required: No

**projectName**

Type: String

Length Constraints: Minimum length of 1.

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

**timeoutInMinutes**

Type: Integer

Required: No
