

# Actions, resources, and condition keys for AWS Diagnostic tools
<a name="list_ts"></a>

AWS Diagnostic tools (service prefix: `ts`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/diagnostic-tools/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ts/latest/diagnostic-tools/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ts/ts.json) for this service.

**Topics**
+ [Actions defined by AWS Diagnostic tools](#list_ts-actions-as-permissions)
+ [Resource types defined by AWS Diagnostic tools](#list_ts-resources-for-iam-policies)
+ [Condition keys for AWS Diagnostic tools](#list_ts-policy-keys)

## Actions defined by AWS Diagnostic tools
<a name="list_ts-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetExecution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetExecution.html)  **
  - **Description:** Grants permission to get details about specific execution within AWS Diagnostic tools
  - **Resource types (\*required):** [execution\*](#list_ts-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetExecutionOutput](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetExecutionOutput.html)  **
  - **Description:** Grants permission to get details about specific execution output within AWS Diagnostic tools
  - **Resource types (\*required):** [execution\*](#list_ts-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTool](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_GetTool.html)  **
  - **Description:** Grants permission to get details about specific tool within AWS Diagnostic tools
  - **Resource types (\*required):** [tool\*](#list_ts-resource-tool)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListExecutions](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListExecutions.html)  **
  - **Description:** Grants permission to list all available execution within AWS Diagnostic tools
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an AWS Diagnostic tools resource
  - **Resource types (\*required):** [execution\*](#list_ts-resource-execution)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ts-aws_TagKeys)
  - **Access level:** Read

- **   [ListTools](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_ListTools.html)  **
  - **Description:** Grants permission to list all available tools within AWS Diagnostic tools
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartExecution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_StartExecution.html)  **
  - **Description:** Grants permission to start an execution workflow of specific tool within AWS Diagnostic tools
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ts-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_ts-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AWS Diagnostic tools resource
  - **Resource types (\*required):** [execution\*](#list_ts-resource-execution)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an AWS Diagnostic tools resource
  - **Resource types (\*required):** [execution\*](#list_ts-resource-execution)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ts-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Diagnostic tools
<a name="list_ts-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [execution](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Execution.html)  | arn:${Partition}:ts::${Account}:execution/${UserId}/${ToolId}/${ExecutionId} | [aws:ResourceTag/${TagKey}](#list_ts-aws_ResourceTag___TagKey_) | 
|  [tool](https://docs.aws.amazon.com/diagnostic-tools/latest/APIReference/API_Tool.html)  | arn:${Partition}:ts::aws:tool/${ToolId} |   | 

## Condition keys for AWS Diagnostic tools
<a name="list_ts-policy-keys"></a>

AWS Diagnostic tools defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 