# TaskFilter

You can use API filters to narrow down the list of resources returned by
`ListTasks`. For example, to retrieve all tasks on a source location, you can use
`ListTasks` with filter name `LocationId` and `Operator
 Equals` with the ARN for the location.

For more information, see [filtering DataSync
resources](query-resources.md "query-resources.md").

## Contents

**Name**

The name of the filter being used. Each API call supports a list of filters that are
available for it. For example, `LocationId` for `ListTasks`.

Type: String

Valid Values: `LocationId | CreationTime`

Required: Yes

**Operator**

The operator that is used to compare filter values (for example, `Equals` or
`Contains`).

Type: String

Valid Values: `Equals | NotEquals | In | LessThanOrEqual | LessThan | GreaterThanOrEqual | GreaterThan | Contains | NotContains | BeginsWith`

Required: Yes

**Values**

The values that you want to filter for. For example, you might want to display only tasks
for a specific destination location.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^[0-9a-zA-Z_\ \-\:\*\.\\/\?-]*$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskFilter.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskFilter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskFilter.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskFilter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskFilter.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskFilter.md")
