

# Actions, resources, and condition keys for Amazon EventBridge Scheduler
<a name="list_scheduler"></a>

Amazon EventBridge Scheduler (service prefix: `scheduler`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/scheduler/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/scheduler/latest/UserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/scheduler/scheduler.json) for this service.

**Topics**
+ [API operations defined by Amazon EventBridge Scheduler](#list_scheduler-operations)
+ [Actions defined by Amazon EventBridge Scheduler](#list_scheduler-actions-as-permissions)
+ [Resource types defined by Amazon EventBridge Scheduler](#list_scheduler-resources-for-iam-policies)
+ [Condition keys for Amazon EventBridge Scheduler](#list_scheduler-policy-keys)

## API operations defined by Amazon EventBridge Scheduler
<a name="list_scheduler-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_scheduler-actions-as-permissions).




- **   CreateSchedule  **
  - **IAM action:**  [scheduler:CreateSchedule](#list_scheduler-action-CreateSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** scheduler.amazonaws.com / **Access level:** Write

- **   CreateScheduleGroup  **
  - **IAM action:**  [scheduler:CreateScheduleGroup](#list_scheduler-action-CreateScheduleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [scheduler:TagResource](#list_scheduler-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteSchedule  **
  - **IAM action:**  [scheduler:DeleteSchedule](#list_scheduler-action-DeleteSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteScheduleGroup  **
  - **IAM action:**  [scheduler:DeleteSchedule](#list_scheduler-action-DeleteSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [scheduler:DeleteScheduleGroup](#list_scheduler-action-DeleteScheduleGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   GetSchedule  **
  - **IAM action:**  [scheduler:GetSchedule](#list_scheduler-action-GetSchedule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetScheduleGroup  **
  - **IAM action:**  [scheduler:GetScheduleGroup](#list_scheduler-action-GetScheduleGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListScheduleGroups  **
  - **IAM action:**  [scheduler:ListScheduleGroups](#list_scheduler-action-ListScheduleGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchedules  **
  - **IAM action:**  [scheduler:ListSchedules](#list_scheduler-action-ListSchedules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [scheduler:ListTagsForResource](#list_scheduler-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [scheduler:TagResource](#list_scheduler-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [scheduler:UntagResource](#list_scheduler-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateSchedule  **
  - **IAM action:**  [scheduler:UpdateSchedule](#list_scheduler-action-UpdateSchedule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** scheduler.amazonaws.com / **Access level:** Write



## Actions defined by Amazon EventBridge Scheduler
<a name="list_scheduler-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateSchedule.html)  **
  - **Description:** Grants permission to create an Amazon EventBridge Scheduler schedule
  - **Resource types (\*required):** [schedule\*](#list_scheduler-resource-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_CreateScheduleGroup.html)  **
  - **Description:** Grants permission to create an Amazon EventBridge Scheduler schedule group
  - **Resource types (\*required):** [schedule-group\*](#list_scheduler-resource-schedule-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_scheduler-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_scheduler-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeleteSchedule.html)  **
  - **Description:** Grants permission to delete an Amazon EventBridge Scheduler schedule
  - **Resource types (\*required):** [schedule\*](#list_scheduler-resource-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_DeleteScheduleGroup.html)  **
  - **Description:** Grants permission to delete an Amazon EventBridge Scheduler schedule group
  - **Resource types (\*required):** [schedule-group\*](#list_scheduler-resource-schedule-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetSchedule.html)  **
  - **Description:** Grants permission to view details about an Amazon EventBridge Scheduler schedule
  - **Resource types (\*required):** [schedule\*](#list_scheduler-resource-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetScheduleGroup](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_GetScheduleGroup.html)  **
  - **Description:** Grants permission to view details about an Amazon EventBridge Scheduler schedule group
  - **Resource types (\*required):** [schedule-group\*](#list_scheduler-resource-schedule-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListScheduleGroups](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListScheduleGroups.html)  **
  - **Description:** Grants permission to list the Amazon EventBridge Scheduler schedule groups in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchedules](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListSchedules.html)  **
  - **Description:** Grants permission to list the Amazon EventBridge Scheduler schedules in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSchedulesByTarget](https://docs.aws.amazon.com/scheduler/latest/UserGuide/)  **
  - **Description:** Grants permission to list the Amazon EventBridge Scheduler schedules in your account associated with a target
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to lists tag for an Amazon EventBridge Scheduler resource
  - **Resource types (\*required):** [schedule-group](#list_scheduler-resource-schedule-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an Amazon EventBridge Scheduler resource
  - **Resource types (\*required):** [schedule-group\*](#list_scheduler-resource-schedule-group)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_scheduler-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_scheduler-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an Amazon EventBridge Scheduler resource
  - **Resource types (\*required):** [schedule-group\*](#list_scheduler-resource-schedule-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_scheduler-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateSchedule](https://docs.aws.amazon.com/scheduler/latest/APIReference/API_UpdateSchedule.html)  **
  - **Description:** Grants permission to modify an Amazon EventBridge Scheduler schedule
  - **Resource types (\*required):** [schedule\*](#list_scheduler-resource-schedule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon EventBridge Scheduler
<a name="list_scheduler-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [schedule](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule.html)  | arn:${Partition}:scheduler:${Region}:${Account}:schedule/${GroupName}/${ScheduleName} |   | 
|  [schedule-group](https://docs.aws.amazon.com/scheduler/latest/UserGuide/managing-schedule-group.html)  | arn:${Partition}:scheduler:${Region}:${Account}:schedule-group/${GroupName} | [aws:ResourceTag/${TagKey}](#list_scheduler-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon EventBridge Scheduler
<a name="list_scheduler-policy-keys"></a>

Amazon EventBridge Scheduler defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 