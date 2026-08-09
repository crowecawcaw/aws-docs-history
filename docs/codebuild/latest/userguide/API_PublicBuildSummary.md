# PublicBuildSummary

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Contents

###### Note

In the following list, the required parameters are described first.

**buildStatus**

Type: String

Required: No

**primaryArtifact**

Represents a resolved build artifact. A resolved artifact is an artifact that is built and
deployed to the destination, such as Amazon S3.

Type: [ResolvedArtifact](../APIReference/API_ResolvedArtifact.md "../APIReference/API_ResolvedArtifact.md") object

Required: No

**publicBuildAlias**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:\p{XDigit}{8}(-\p{XDigit}{4}){3}-\p{XDigit}{12}$`

Required: No

**requestedOn**

Type: Timestamp

Required: No

**secondaryArtifacts**

Type: Array of [ResolvedArtifact](../APIReference/API_ResolvedArtifact.md "../APIReference/API_ResolvedArtifact.md") objects

Required: No
