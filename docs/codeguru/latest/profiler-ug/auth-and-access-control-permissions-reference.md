# Amazon CodeGuru Profiler permissions

reference

You can use AWS-wide condition keys in your CodeGuru Profiler policies to express conditions. For
a list, see the [IAM JSON Policy Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the
_IAM User Guide_.

You specify the actions in the policy's `Action` field. To specify an
action, use the `codeguru-profiler:` prefix followed by the API operation name (for
example, `codeguru-profiler:CreateProfilingGroup` and
`codeguru-profiler:GetFindingsReport`). To specify multiple actions in a single
statement, separate them with commas (for example, `"Action": [
 "codeguru-profiler:CreateProfilingGroup", "codeguru-profiler:GetFindingsReport" ]`).

**Using wildcard characters**

You specify an ARN, with or without a wildcard character (\*), as the resource value in
the policy's `Resource` field. You can use a wildcard to specify multiple
actions or resources. For example, `codeguru-profiler:*` specifies all CodeGuru Profiler actions
and `codeguru-profiler:Get*` specifies all CodeGuru Profiler actions that begin with the word
`Get`. The following example refers to all profiling groups with names that
begin with `my`.

```
arn:aws:codeguru-profiler:us-east-2:123456789012:profilingGroup/my*
```

You can use the following table as a reference when you are setting up [authenticating with identities in CodeGuru Profiler](security_iam_authentication.md "security_iam_authentication.md") and writing permissions policies that
you can attach to an IAM identity (identity-based policies).

CodeGuru Profiler API operations and required
permissions for actions| CodeGuru Profiler API operations | Required permissions (API actions) | Resources |
| --- | --- | --- |
| `ConfigureAgent` | `codeguru-profiler:ConfigureAgent` Required for an agent to register with an orchestration service and retrieve profiling configuration information. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `CreateProfilingGroup` | `codeguru-profiler:CreateProfilingGroup` Required to create a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `DeleteProfilingGroup` | `codeguru-profiler:DeleteProfilingGroup` Required to delete a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `DescribeProfilingGroup` | `codeguru-profiler:DescribeProfilingGroup` Required to get information about a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `GetFindingsReport` | `codeguru-profiler:GetFindingsReport` Required to get a recommendations report. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `GetFindingsReportAccountSummary` | `codeguru-profiler:GetFindingsReportAccountSummary` Required to get a summary of recent recommendations for each profiling group in an AWS account. | `*` |
| `GetPolicy` | `codeguru-profiler:GetPolicy` Required to get the resource policy that is associated with a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `GetProfile` | `codeguru-profiler:GetProfile` Required to get aggregated profiles for one profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `GetRecommendations` | `codeguru-profiler:GetRecommendations` Required to get recommendations. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `ListFindingsReports` | `codeguru-profiler:ListFindingsReports` Required to list recommendations reports for one profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `ListProfileTimes` | `codeguru-profiler:ListProfileTimes` Required to list the start times of profiles for one profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `ListProfilingGroups` | `codeguru-profiler:ListProfilingGroups` Required to list the profiling groups in one AWS account. | `*` |
| `PostAgentProfile` | `codeguru-profiler:PostAgentProfile` Required to submit a profile for aggregation. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `PutPermission` | `codeguru-profiler:PutPermission` Required to update the list of principals for an action group in the resource policy of a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `RemovePermission` | `codeguru-profiler:RemovePermission` Required to remove the permission of an action group from the resource policy of a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
| `UpdateProfilingGroup` | `codeguru-profiler:UpdateProfilingGroup` Required to update a profiling group. | `arn:aws:codeguru-profiler:`region-ID`:`account-ID`:profilingGroup/`profiling-group-name`` |
