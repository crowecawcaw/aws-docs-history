

# Actions, resources, and condition keys for Amazon CodeGuru Profiler
<a name="list_codeguruprofiler"></a>

Amazon CodeGuru Profiler (service prefix: `codeguru-profiler`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/codeguru/latest/profiler-api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/codeguru-profiler/codeguru-profiler.json) for this service.

**Topics**
+ [API operations defined by Amazon CodeGuru Profiler](#list_codeguruprofiler-operations)
+ [Actions defined by Amazon CodeGuru Profiler](#list_codeguruprofiler-actions-as-permissions)
+ [Resource types defined by Amazon CodeGuru Profiler](#list_codeguruprofiler-resources-for-iam-policies)
+ [Condition keys for Amazon CodeGuru Profiler](#list_codeguruprofiler-policy-keys)

## API operations defined by Amazon CodeGuru Profiler
<a name="list_codeguruprofiler-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_codeguruprofiler-actions-as-permissions).




- **   AddNotificationChannels  **
  - **IAM action:**  [codeguru-profiler:AddNotificationChannels](#list_codeguruprofiler-action-AddNotificationChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetFrameMetricData  **
  - **IAM action:**  [codeguru-profiler:BatchGetFrameMetricData](#list_codeguruprofiler-action-BatchGetFrameMetricData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ConfigureAgent  **
  - **IAM action:**  [codeguru-profiler:ConfigureAgent](#list_codeguruprofiler-action-ConfigureAgent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProfilingGroup  **
  - **IAM action:**  [codeguru-profiler:CreateProfilingGroup](#list_codeguruprofiler-action-CreateProfilingGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [codeguru-profiler:TagResource](#list_codeguruprofiler-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteProfilingGroup  **
  - **IAM action:**  [codeguru-profiler:DeleteProfilingGroup](#list_codeguruprofiler-action-DeleteProfilingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeProfilingGroup  **
  - **IAM action:**  [codeguru-profiler:DescribeProfilingGroup](#list_codeguruprofiler-action-DescribeProfilingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsReportAccountSummary  **
  - **IAM action:**  [codeguru-profiler:GetFindingsReportAccountSummary](#list_codeguruprofiler-action-GetFindingsReportAccountSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotificationConfiguration  **
  - **IAM action:**  [codeguru-profiler:GetNotificationConfiguration](#list_codeguruprofiler-action-GetNotificationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **IAM action:**  [codeguru-profiler:GetPolicy](#list_codeguruprofiler-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfile  **
  - **IAM action:**  [codeguru-profiler:GetProfile](#list_codeguruprofiler-action-GetProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRecommendations  **
  - **IAM action:**  [codeguru-profiler:GetRecommendations](#list_codeguruprofiler-action-GetRecommendations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFindingsReports  **
  - **IAM action:**  [codeguru-profiler:ListFindingsReports](#list_codeguruprofiler-action-ListFindingsReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfileTimes  **
  - **IAM action:**  [codeguru-profiler:ListProfileTimes](#list_codeguruprofiler-action-ListProfileTimes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfilingGroups  **
  - **IAM action:**  [codeguru-profiler:ListProfilingGroups](#list_codeguruprofiler-action-ListProfilingGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [codeguru-profiler:ListTagsForResource](#list_codeguruprofiler-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PostAgentProfile  **
  - **IAM action:**  [codeguru-profiler:PostAgentProfile](#list_codeguruprofiler-action-PostAgentProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutPermission  **
  - **IAM action:**  [codeguru-profiler:PutPermission](#list_codeguruprofiler-action-PutPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RemoveNotificationChannel  **
  - **IAM action:**  [codeguru-profiler:RemoveNotificationChannel](#list_codeguruprofiler-action-RemoveNotificationChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemovePermission  **
  - **IAM action:**  [codeguru-profiler:RemovePermission](#list_codeguruprofiler-action-RemovePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SubmitFeedback  **
  - **IAM action:**  [codeguru-profiler:SubmitFeedback](#list_codeguruprofiler-action-SubmitFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [codeguru-profiler:TagResource](#list_codeguruprofiler-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [codeguru-profiler:UntagResource](#list_codeguruprofiler-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateProfilingGroup  **
  - **IAM action:**  [codeguru-profiler:UpdateProfilingGroup](#list_codeguruprofiler-action-UpdateProfilingGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon CodeGuru Profiler
<a name="list_codeguruprofiler-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddNotificationChannels](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AddNotificationChannels.html)  **
  - **Description:** Grants permission to add up to 2 topic ARNs of existing AWS SNS topics to publish notifications
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchGetFrameMetricData](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_BatchGetFrameMetricData.html)  **
  - **Description:** Grants permission to get the frame metric data for a Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ConfigureAgent](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html)  **
  - **Description:** Grants permission to register with the orchestration service and retrieve profiling configuration information, used by agents
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_CreateProfilingGroup.html)  **
  - **Description:** Grants permission to create a profiling group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeguruprofiler-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_codeguruprofiler-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_DeleteProfilingGroup.html)  **
  - **Description:** Grants permission to delete a profiling group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_DescribeProfilingGroup.html)  **
  - **Description:** Grants permission to describe a profiling group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingsReportAccountSummary](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetFindingsReportAccountSummary.html)  **
  - **Description:** Grants permission to get a summary of recent recommendations for each profiling group in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetNotificationConfiguration](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetNotificationConfiguration.html)  **
  - **Description:** Grants permission to get the notification configuration
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetPolicy.html)  **
  - **Description:** Grants permission to get the resource policy associated with the specified Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfile](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html)  **
  - **Description:** Grants permission to get aggregated profiles for a specific profiling group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommendations](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetRecommendations.html)  **
  - **Description:** Grants permission to get recommendations
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFindingsReports](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListFindingsReports.html)  **
  - **Description:** Grants permission to list the available recommendations reports for a specific profiling group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfileTimes](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html)  **
  - **Description:** Grants permission to list the start times of the available aggregated profiles for a specific profiling group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProfilingGroups](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfilingGroups.html)  **
  - **Description:** Grants permission to list profiling groups in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PostAgentProfile](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html)  **
  - **Description:** Grants permission to submit a profile collected by an agent belonging to a specific profiling group for aggregation
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutPermission](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PutPermission.html)  **
  - **Description:** Grants permission to update the list of principals allowed for an action group in the resource policy associated with the specified Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RemoveNotificationChannel](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_RemoveNotificationChannel.html)  **
  - **Description:** Grants permission to delete an already configured SNStopic arn from the notification configuration
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemovePermission](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_RemovePermission.html)  **
  - **Description:** Grants permission to remove the permission of specified Action Group from the resource policy associated with the specified Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SubmitFeedback](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_SubmitFeedback.html)  **
  - **Description:** Grants permission to submit user feedback for useful or non useful anomaly
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_TagResource.html)  **
  - **Description:** Grants permission to add or overwrite tags to a Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_codeguruprofiler-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguruprofiler-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a Profiling Group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_codeguruprofiler-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_UpdateProfilingGroup.html)  **
  - **Description:** Grants permission to update a specific profiling group
  - **Resource types (\*required):** [ProfilingGroup\*](#list_codeguruprofiler-resource-ProfilingGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon CodeGuru Profiler
<a name="list_codeguruprofiler-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ProfilingGroup](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-profiling-groups.html)  | arn:${Partition}:codeguru-profiler:${Region}:${Account}:profilingGroup/${ProfilingGroupName} | [aws:ResourceTag/${TagKey}](#list_codeguruprofiler-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon CodeGuru Profiler
<a name="list_codeguruprofiler-policy-keys"></a>

Amazon CodeGuru Profiler defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 