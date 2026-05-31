# PublicProjectSource

###### Note

This API element is not contained in the AWS CLI or AWS SDKs.

## Contents

###### Note

In the following list, the required parameters are described first.

**type**

Type: String

Valid Values: `NO_SOURCE | CODECOMMIT | CODEPIPELINE | GITHUB | S3 | BITBUCKET | GITHUB_ENTERPRISE | GITLAB | GITLAB_SELF_MANAGED`

Required: Yes

**buildspec**

Type: String

Required: No

**gitCloneDepth**

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**gitSubmodulesConfig**

Information about the Git submodules configuration for an AWS CodeBuild build project.

Type: [GitSubmodulesConfig](../APIReference/API_GitSubmodulesConfig.md "../APIReference/API_GitSubmodulesConfig.md") object

Required: No

**location**

Type: String

Required: No

**sourceIdentifier**

Type: String

Required: No
