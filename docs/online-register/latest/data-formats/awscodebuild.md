

# Data retrieval APIs for AWS CodeBuild
<a name="awscodebuild"></a>

AWS CodeBuild provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="codebuild-BatchGetBuildBatches"></a>[BatchGetBuildBatches](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetBuildBatches.html) | Get information about one or more build batches | Read | 
| <a name="codebuild-BatchGetBuilds"></a>[BatchGetBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetBuilds.html) | Get information about one or more builds | Read | 
| <a name="codebuild-BatchGetCommandExecutions"></a>[BatchGetCommandExecutions](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetCommandExecutions.html) | Get information about one or more command executions | Read | 
| <a name="codebuild-BatchGetFleets"></a>[BatchGetFleets](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetFleets.html) | Return an array of the Fleet objects specified by the input parameter | Read | 
| <a name="codebuild-BatchGetProjects"></a>[BatchGetProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetProjects.html) | Get information about one or more build projects | Read | 
| <a name="codebuild-BatchGetReportGroups"></a>[BatchGetReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReportGroups.html) | Return an array of ReportGroup objects that are specified by the input reportGroupArns parameter | Read | 
| <a name="codebuild-BatchGetReports"></a>[BatchGetReports](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetReports.html) | Return an array of the Report objects specified by the input reportArns parameter | Read | 
| <a name="codebuild-BatchGetSandboxes"></a>[BatchGetSandboxes](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_BatchGetSandboxes.html) | Get information about one or more sandboxes | Read | 
| <a name="codebuild-DescribeCodeCoverages"></a>[DescribeCodeCoverages](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeCodeCoverages.html) | Return an array of CodeCoverage objects | Read | 
| <a name="codebuild-DescribeTestCases"></a>[DescribeTestCases](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeTestCases.html) | Return an array of TestCase objects | Read | 
| <a name="codebuild-GetReportGroupTrend"></a>[GetReportGroupTrend](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetReportGroupTrend.html) | Analyze and accumulate test report values for the test reports in the specified report group | Read | 
| <a name="codebuild-GetResourcePolicy"></a>[GetResourcePolicy](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_GetResourcePolicy.html) | Return a resource policy for the specified project or report group | Read | 
| <a name="codebuild-ListBuildBatches"></a>[ListBuildBatches](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatches.html) | Get a list of build batch IDs, with each build batch ID representing a single build batch | List | 
| <a name="codebuild-ListBuildBatchesForProject"></a>[ListBuildBatchesForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildBatchesForProject.html) | Get a list of build batch IDs for the specified build project, with each build batch ID representing a single build batch | List | 
| <a name="codebuild-ListBuilds"></a>[ListBuilds](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuilds.html) | Get a list of build IDs, with each build ID representing a single build | List | 
| <a name="codebuild-ListBuildsForProject"></a>[ListBuildsForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListBuildsForProject.html) | Get a list of build IDs for the specified build project, with each build ID representing a single build | List | 
| <a name="codebuild-ListCommandExecutionsForSandbox"></a>[ListCommandExecutionsForSandbox](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCommandExecutionsForSandbox.html) | Get a list of command execution IDs for the specified sandbox, with each command execution ID representing a single command execution | List | 
| <a name="codebuild-ListConnectedOAuthAccounts"></a>[ListConnectedOAuthAccounts](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies) | List connected third-party OAuth providers. Only used in the AWS CodeBuild console | List | 
| <a name="codebuild-ListCuratedEnvironmentImages"></a>[ListCuratedEnvironmentImages](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListCuratedEnvironmentImages.html) | Get information about Docker images that are managed by AWS CodeBuild | List | 
| <a name="codebuild-ListFleets"></a>[ListFleets](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListFleets.html) | Get a list of compute fleet ARNs, with each compute fleet ARN representing a single fleet | List | 
| <a name="codebuild-ListProjects"></a>[ListProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListProjects.html) | Get a list of build project names, with each build project name representing a single build project | List | 
| <a name="codebuild-ListReportGroups"></a>[ListReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportGroups.html) | Return a list of report group ARNs. Each report group ARN represents one report group | List | 
| <a name="codebuild-ListReports"></a>[ListReports](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReports.html) | Return a list of report ARNs. Each report ARN representing one report | List | 
| <a name="codebuild-ListReportsForReportGroup"></a>[ListReportsForReportGroup](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListReportsForReportGroup.html) | Return a list of report ARNs that belong to the specified report group. Each report ARN represents one report | List | 
| <a name="codebuild-ListRepositories"></a>[ListRepositories](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html#console-policies) | List source code repositories from a connected third-party OAuth provider. Only used in the AWS CodeBuild console | List | 
| <a name="codebuild-ListSandboxes"></a>[ListSandboxes](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxes.html) | Get a list of sandbox IDs, with each sandbox ID representing a single sandbox | List | 
| <a name="codebuild-ListSandboxesForProject"></a>[ListSandboxesForProject](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSandboxesForProject.html) | Get a list of sandbox IDs for the specified sandbox project, with each sandbox ID representing a single sandbox | List | 
| <a name="codebuild-ListSharedProjects"></a>[ListSharedProjects](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSharedProjects.html) | Return a list of project ARNs that have been shared with the requester. Each project ARN represents one project | List | 
| <a name="codebuild-ListSharedReportGroups"></a>[ListSharedReportGroups](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSharedReportGroups.html) | Return a list of report group ARNs that have been shared with the requester. Each report group ARN represents one report group | List | 
| <a name="codebuild-ListSourceCredentials"></a>[ListSourceCredentials](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ListSourceCredentials.html) | Return a list of SourceCredentialsInfo objects | List | 