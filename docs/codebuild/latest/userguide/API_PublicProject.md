# PublicProject

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Contents

###### Note

In the following list, the required parameters are described first.

**artifacts**

Type: [PublicProjectArtifacts](API_PublicProjectArtifacts.md "API_PublicProjectArtifacts.md") object

Required: No

**buildBatchConfig**

Type: [PublicProjectBuildBatchConfig](API_PublicProjectBuildBatchConfig.md "API_PublicProjectBuildBatchConfig.md") object

Required: No

**concurrentBuildLimit**

Type: Integer

Required: No

**description**

Type: String

Length Constraints: Minimum length of 0. Maximum length of 255.

Required: No

**environment**

Type: [PublicProjectEnvironment](API_PublicProjectEnvironment.md "API_PublicProjectEnvironment.md") object

Required: No

**name**

Type: String

Length Constraints: Minimum length of 2. Maximum length of 150.

Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{1,254}`

Required: No

**queuedTimeoutInMinutes**

Type: Integer

Valid Range: Minimum value of 5. Maximum value of 480.

Required: No

**secondaryArtifacts**

Type: Array of [PublicProjectArtifacts](API_PublicProjectArtifacts.md "API_PublicProjectArtifacts.md") objects

Array Members: Minimum number of 0 items. Maximum number of 12 items.

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

**timeoutInMinutes**

Type: Integer

Valid Range: Minimum value of 5. Maximum value of 480.

Required: No

**webhook**

Type: [PublicWebhook](API_PublicWebhook.md "API_PublicWebhook.md") object

Required: No
