# Actions, resources, and condition keys for AWS Diagnostic tools

AWS Diagnostic tools (service prefix: `ts`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../diagnostic-tools.md "../../../diagnostic-tools.md").
- View a list of the [API operations available for
  this service](../../../diagnostic-tools/latest/APIReference.md "../../../diagnostic-tools/latest/APIReference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../ts/latest/diagnostic-tools/security-iam.md "../../../ts/latest/diagnostic-tools/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/ts/ts.json "https://servicereference.us-east-1.amazonaws.com/v1/ts/ts.json") for this service.

###### Topics

- [Actions defined by AWS Diagnostic tools](#list_ts-actions-as-permissions "#list_ts-actions-as-permissions")
- [Resource types defined by AWS Diagnostic tools](#list_ts-resources-for-iam-policies "#list_ts-resources-for-iam-policies")
- [Condition keys for AWS Diagnostic tools](#list_ts-policy-keys "#list_ts-policy-keys")

## Actions defined by AWS Diagnostic tools

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                    | Description                                                                                   | Resource types (\*required)                                              | Condition keys                                                                                                                                                                                                                                                          | Access level   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| [GetExecution](../../../diagnostic-tools/latest/APIReference/API_GetExecution.md "../../../diagnostic-tools/latest/APIReference/API_GetExecution.md")                      | Grants permission to get details about specific execution within AWS Diagnostic tools         | [execution\*](#list_ts-resource-execution "#list_ts-resource-execution") | [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_ "#list_ts-aws_ResourceTag___TagKey_")                                                                                                                                                                    | Read           |
| [GetExecutionOutput](../../../diagnostic-tools/latest/APIReference/API_GetExecutionOutput.md "../../../diagnostic-tools/latest/APIReference/API_GetExecutionOutput.md")    | Grants permission to get details about specific execution output within AWS Diagnostic tools  | [execution\*](#list_ts-resource-execution "#list_ts-resource-execution") | [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_ "#list_ts-aws_ResourceTag___TagKey_")                                                                                                                                                                    | Read           |
| [GetTool](../../../diagnostic-tools/latest/APIReference/API_GetTool.md "../../../diagnostic-tools/latest/APIReference/API_GetTool.md")                                     | Grants permission to get details about specific tool within AWS Diagnostic tools              | [tool\*](#list_ts-resource-tool "#list_ts-resource-tool")                |                                                                                                                                                                                                                                                                         | Read           |
| [ListExecutions](../../../diagnostic-tools/latest/APIReference/API_ListExecutions.md "../../../diagnostic-tools/latest/APIReference/API_ListExecutions.md")                | Grants permission to list all available execution within AWS Diagnostic tools                 |                                                                          |                                                                                                                                                                                                                                                                         | List           |
| [ListTagsForResource](../../../diagnostic-tools/latest/APIReference/API_ListTagsForResource.md "../../../diagnostic-tools/latest/APIReference/API_ListTagsForResource.md") | Grants permission to list the tags for an AWS Diagnostic tools resource                       | [execution\*](#list_ts-resource-execution "#list_ts-resource-execution") | [aws:RequestTag/${TagKey}](#list_ts-aws_RequestTag___TagKey_ "#list_ts-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_ "#list_ts-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_ts-aws_TagKeys "#list_ts-aws_TagKeys") | Read           |
| [ListTools](../../../diagnostic-tools/latest/APIReference/API_ListTools.md "../../../diagnostic-tools/latest/APIReference/API_ListTools.md")                               | Grants permission to list all available tools within AWS Diagnostic tools                     |                                                                          |                                                                                                                                                                                                                                                                         | List           |
| [StartExecution](../../../diagnostic-tools/latest/APIReference/API_StartExecution.md "../../../diagnostic-tools/latest/APIReference/API_StartExecution.md")                | Grants permission to start an execution workflow of specific tool within AWS Diagnostic tools |                                                                          | [aws:RequestTag/${TagKey}](#list_ts-aws_RequestTag___TagKey_ "#list_ts-aws_RequestTag___TagKey_")<br>[aws:TagKeys](#list_ts-aws_TagKeys "#list_ts-aws_TagKeys")                                                                                                         | Write          |
| [TagResource](../../../diagnostic-tools/latest/APIReference/API_TagResource.md "../../../diagnostic-tools/latest/APIReference/API_TagResource.md")                         | Grants permission to tag an AWS Diagnostic tools resource                                     | [execution\*](#list_ts-resource-execution "#list_ts-resource-execution") | [aws:RequestTag/${TagKey}](#list_ts-aws_RequestTag___TagKey_ "#list_ts-aws_RequestTag___TagKey_")<br>[aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_ "#list_ts-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_ts-aws_TagKeys "#list_ts-aws_TagKeys") | Tagging, Write |
| [UntagResource](../../../diagnostic-tools/latest/APIReference/API_UntagResource.md "../../../diagnostic-tools/latest/APIReference/API_UntagResource.md")                   | Grants permission to untag an AWS Diagnostic tools resource                                   | [execution\*](#list_ts-resource-execution "#list_ts-resource-execution") | [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_ "#list_ts-aws_ResourceTag___TagKey_")<br>[aws:TagKeys](#list_ts-aws_TagKeys "#list_ts-aws_TagKeys")                                                                                                      | Tagging, Write |

## Resource types defined by AWS Diagnostic tools

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                               | ARN                                                                          | Condition keys                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [execution](../../../diagnostic-tools/latest/APIReference/API_Execution.md "../../../diagnostic-tools/latest/APIReference/API_Execution.md") | arn:${Partition}:ts::${Account}:execution/${UserId}/${ToolId}/${ExecutionId} | [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_ "#list_ts-aws_ResourceTag___TagKey_") |
| [tool](../../../diagnostic-tools/latest/APIReference/API_Tool.md "../../../diagnostic-tools/latest/APIReference/API_Tool.md")                | arn:${Partition}:ts::aws:tool/${ToolId}                                      |                                                                                                      |

## Condition keys for AWS Diagnostic tools

AWS Diagnostic tools defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                             | Description                                                      | Type          |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------- |
| [aws:RequestTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag")    | Filters access by the allowed set of values for each of the tags | String        |
| [aws:ResourceTag/${TagKey}](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") | Filters access by tag-value associated with the resource         | String        |
| [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys")                       | Filters access by the presence of mandatory tags in the request  | ArrayOfString |
