# BuildBatchForDescribeBuildBatchesPublic

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Contents

###### Note

In the following list, the required parameters are described first.

**buildBatchNumber**

Type: Long

Required: No

**buildBatchStatus**

Type: String

Valid Values: `PENDING | SUCCEEDED | FAILED | FAULT | TIMED_OUT | IN_PROGRESS | STOPPED`

Required: No

**endTime**

Type: Timestamp

Required: No

**publicBuildBatchAlias**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `^[0-9a-zA-Z%+=]+:[a-z0-9]{8}(-[a-z0-9]{4}){3}-[a-z0-9]{12}$`

Required: No

**sourceVersion**

Type: String

Length Constraints: Minimum length of 1.

Required: No

**startTime**

Type: Timestamp

Required: No
