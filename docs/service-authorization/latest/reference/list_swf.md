

# Actions, resources, and condition keys for Amazon Simple Workflow Service
<a name="list_swf"></a>

Amazon Simple Workflow Service (service prefix: `swf`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazonswf/latest/apireference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/swf/swf.json) for this service.

**Topics**
+ [API operations defined by Amazon Simple Workflow Service](#list_swf-operations)
+ [Actions defined by Amazon Simple Workflow Service](#list_swf-actions-as-permissions)
+ [Permission-only actions for Amazon Simple Workflow Service](#list_swf-permission-only-actions)
+ [Resource types defined by Amazon Simple Workflow Service](#list_swf-resources-for-iam-policies)
+ [Condition keys for Amazon Simple Workflow Service](#list_swf-policy-keys)

## API operations defined by Amazon Simple Workflow Service
<a name="list_swf-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_swf-actions-as-permissions).




- **   CountClosedWorkflowExecutions  **
  - **IAM action:**  [swf:CountClosedWorkflowExecutions](#list_swf-action-CountClosedWorkflowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CountOpenWorkflowExecutions  **
  - **IAM action:**  [swf:CountOpenWorkflowExecutions](#list_swf-action-CountOpenWorkflowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CountPendingActivityTasks  **
  - **IAM action:**  [swf:CountPendingActivityTasks](#list_swf-action-CountPendingActivityTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CountPendingDecisionTasks  **
  - **IAM action:**  [swf:CountPendingDecisionTasks](#list_swf-action-CountPendingDecisionTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DeleteActivityType  **
  - **IAM action:**  [swf:DeleteActivityType](#list_swf-action-DeleteActivityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflowType  **
  - **IAM action:**  [swf:DeleteWorkflowType](#list_swf-action-DeleteWorkflowType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeprecateActivityType  **
  - **IAM action:**  [swf:DeprecateActivityType](#list_swf-action-DeprecateActivityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeprecateDomain  **
  - **IAM action:**  [swf:DeprecateDomain](#list_swf-action-DeprecateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeprecateWorkflowType  **
  - **IAM action:**  [swf:DeprecateWorkflowType](#list_swf-action-DeprecateWorkflowType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeActivityType  **
  - **IAM action:**  [swf:DescribeActivityType](#list_swf-action-DescribeActivityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomain  **
  - **IAM action:**  [swf:DescribeDomain](#list_swf-action-DescribeDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkflowExecution  **
  - **IAM action:**  [swf:DescribeWorkflowExecution](#list_swf-action-DescribeWorkflowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeWorkflowType  **
  - **IAM action:**  [swf:DescribeWorkflowType](#list_swf-action-DescribeWorkflowType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowExecutionHistory  **
  - **IAM action:**  [swf:GetWorkflowExecutionHistory](#list_swf-action-GetWorkflowExecutionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListActivityTypes  **
  - **IAM action:**  [swf:ListActivityTypes](#list_swf-action-ListActivityTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClosedWorkflowExecutions  **
  - **IAM action:**  [swf:ListClosedWorkflowExecutions](#list_swf-action-ListClosedWorkflowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomains  **
  - **IAM action:**  [swf:ListDomains](#list_swf-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOpenWorkflowExecutions  **
  - **IAM action:**  [swf:ListOpenWorkflowExecutions](#list_swf-action-ListOpenWorkflowExecutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [swf:ListTagsForResource](#list_swf-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowTypes  **
  - **IAM action:**  [swf:ListWorkflowTypes](#list_swf-action-ListWorkflowTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PollForActivityTask  **
  - **IAM action:**  [swf:PollForActivityTask](#list_swf-action-PollForActivityTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PollForDecisionTask  **
  - **IAM action:**  [swf:PollForDecisionTask](#list_swf-action-PollForDecisionTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RecordActivityTaskHeartbeat  **
  - **IAM action:**  [swf:RecordActivityTaskHeartbeat](#list_swf-action-RecordActivityTaskHeartbeat) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterActivityType  **
  - **IAM action:**  [swf:RegisterActivityType](#list_swf-action-RegisterActivityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterDomain  **
  - **IAM action:**  [swf:RegisterDomain](#list_swf-action-RegisterDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [swf:TagResource](#list_swf-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RegisterWorkflowType  **
  - **IAM action:**  [swf:RegisterWorkflowType](#list_swf-action-RegisterWorkflowType)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** swf.amazonaws.com / **Access level:** Write

- **   RequestCancelWorkflowExecution  **
  - **IAM action:**  [swf:RequestCancelWorkflowExecution](#list_swf-action-RequestCancelWorkflowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RespondActivityTaskCanceled  **
  - **IAM action:**  [swf:RespondActivityTaskCanceled](#list_swf-action-RespondActivityTaskCanceled) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RespondActivityTaskCompleted  **
  - **IAM action:**  [swf:RespondActivityTaskCompleted](#list_swf-action-RespondActivityTaskCompleted) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RespondActivityTaskFailed  **
  - **IAM action:**  [swf:RespondActivityTaskFailed](#list_swf-action-RespondActivityTaskFailed) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RespondDecisionTaskCompleted  **
  - **IAM action:**  [swf:RespondDecisionTaskCompleted](#list_swf-action-RespondDecisionTaskCompleted)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** swf.amazonaws.com / **Access level:** Write

- **   SignalWorkflowExecution  **
  - **IAM action:**  [swf:SignalWorkflowExecution](#list_swf-action-SignalWorkflowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartWorkflowExecution  **
  - **IAM action:**  [swf:StartWorkflowExecution](#list_swf-action-StartWorkflowExecution)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** swf.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [swf:TagResource](#list_swf-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TerminateWorkflowExecution  **
  - **IAM action:**  [swf:TerminateWorkflowExecution](#list_swf-action-TerminateWorkflowExecution) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UndeprecateActivityType  **
  - **IAM action:**  [swf:UndeprecateActivityType](#list_swf-action-UndeprecateActivityType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UndeprecateDomain  **
  - **IAM action:**  [swf:UndeprecateDomain](#list_swf-action-UndeprecateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UndeprecateWorkflowType  **
  - **IAM action:**  [swf:UndeprecateWorkflowType](#list_swf-action-UndeprecateWorkflowType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [swf:UntagResource](#list_swf-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon Simple Workflow Service
<a name="list_swf-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CountClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html)  **
  - **Description:** Grants permission to return the number of closed workflow executions within the given domain that meet the specified filtering criteria
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:tagFilter.tag](#list_swf-swf_tagFilter.tag)<br />[swf:typeFilter.name](#list_swf-swf_typeFilter.name)<br />[swf:typeFilter.version](#list_swf-swf_typeFilter.version)
  - **Access level:** Read

- **   [CountOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountOpenWorkflowExecutions.html)  **
  - **Description:** Grants permission to return the number of open workflow executions within the given domain that meet the specified filtering criteria
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:tagFilter.tag](#list_swf-swf_tagFilter.tag)<br />[swf:typeFilter.name](#list_swf-swf_typeFilter.name)<br />[swf:typeFilter.version](#list_swf-swf_typeFilter.version)
  - **Access level:** Read

- **   [CountPendingActivityTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingActivityTasks.html)  **
  - **Description:** Grants permission to return the estimated number of activity tasks in the specified task list
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:taskList.name](#list_swf-swf_taskList.name)
  - **Access level:** Read

- **   [CountPendingDecisionTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingDecisionTasks.html)  **
  - **Description:** Grants permission to return the estimated number of decision tasks in the specified task list
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:taskList.name](#list_swf-swf_taskList.name)
  - **Access level:** Read

- **   [DeleteActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteActivityType.html)  **
  - **Description:** Grants permission to delete the specified activity type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:activityType.name](#list_swf-swf_activityType.name)<br />[swf:activityType.version](#list_swf-swf_activityType.version)
  - **Access level:** Write

- **   [DeleteWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeleteWorkflowType.html)  **
  - **Description:** Grants permission to delete the specified workflow type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:workflowType.name](#list_swf-swf_workflowType.name)<br />[swf:workflowType.version](#list_swf-swf_workflowType.version)
  - **Access level:** Write

- **   [DeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateActivityType.html)  **
  - **Description:** Grants permission to deprecate the specified activity type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:activityType.name](#list_swf-swf_activityType.name)<br />[swf:activityType.version](#list_swf-swf_activityType.version)
  - **Access level:** Write

- **   [DeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateDomain.html)  **
  - **Description:** Grants permission to deprecate the specified domain
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DeprecateWorkflowType.html)  **
  - **Description:** Grants permission to deprecate the specified workflow type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:workflowType.name](#list_swf-swf_workflowType.name)<br />[swf:workflowType.version](#list_swf-swf_workflowType.version)
  - **Access level:** Write

- **   [DescribeActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html)  **
  - **Description:** Grants permission to return information about the specified activity type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:activityType.name](#list_swf-swf_activityType.name)<br />[swf:activityType.version](#list_swf-swf_activityType.version)
  - **Access level:** Read

- **   [DescribeDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeDomain.html)  **
  - **Description:** Grants permission to return information about the specified domain, including its description and status
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowExecution.html)  **
  - **Description:** Grants permission to return information about the specified workflow execution including its type and some statistics
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html)  **
  - **Description:** Grants permission to return information about the specified workflow type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:workflowType.name](#list_swf-swf_workflowType.name)<br />[swf:workflowType.version](#list_swf-swf_workflowType.version)
  - **Access level:** Read

- **   [GetWorkflowExecutionHistory](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_GetWorkflowExecutionHistory.html)  **
  - **Description:** Grants permission to return the history of the specified workflow execution
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListActivityTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListActivityTypes.html)  **
  - **Description:** Grants permission to return information about all activities registered in the specified domain that match the specified name and registration status
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListClosedWorkflowExecutions.html)  **
  - **Description:** Grants permission to return a list of closed workflow executions in the specified domain that meet the filtering criteria
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:tagFilter.tag](#list_swf-swf_tagFilter.tag)<br />[swf:typeFilter.name](#list_swf-swf_typeFilter.name)<br />[swf:typeFilter.version](#list_swf-swf_typeFilter.version)
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html)  **
  - **Description:** Grants permission to return the list of domains registered in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListOpenWorkflowExecutions.html)  **
  - **Description:** Grants permission to return a list of open workflow executions in the specified domain that meet the filtering criteria
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:tagFilter.tag](#list_swf-swf_tagFilter.tag)<br />[swf:typeFilter.name](#list_swf-swf_typeFilter.name)<br />[swf:typeFilter.version](#list_swf-swf_typeFilter.version)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an AWS SWF resource
  - **Resource types (\*required):** [domain](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflowTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListWorkflowTypes.html)  **
  - **Description:** Grants permission to return information about workflow types in the specified domain
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PollForActivityTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForActivityTask.html)  **
  - **Description:** Grants permission to workers to get an ActivityTask from the specified activity taskList
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:taskList.name](#list_swf-swf_taskList.name)
  - **Access level:** Write

- **   [PollForDecisionTask](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_PollForDecisionTask.html)  **
  - **Description:** Grants permission to deciders to get a DecisionTask from the specified decision taskList
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:taskList.name](#list_swf-swf_taskList.name)
  - **Access level:** Write

- **   [RecordActivityTaskHeartbeat](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RecordActivityTaskHeartbeat.html)  **
  - **Description:** Grants permission to workers to report to the service that the ActivityTask represented by the specified taskToken is still making progress
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterActivityType.html)  **
  - **Description:** Grants permission to register a new activity type along with its configuration settings in the specified domain
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:defaultTaskList.name](#list_swf-swf_defaultTaskList.name)<br />[swf:name](#list_swf-swf_name)<br />[swf:version](#list_swf-swf_version)
  - **Access level:** Write

- **   [RegisterDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterDomain.html)  **
  - **Description:** Grants permission to register a new domain
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_swf-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_swf-aws_TagKeys)
  - **Access level:** Write

- **   [RegisterWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RegisterWorkflowType.html)  **
  - **Description:** Grants permission to register a new workflow type and its configuration settings in the specified domain
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:defaultTaskList.name](#list_swf-swf_defaultTaskList.name)<br />[swf:name](#list_swf-swf_name)<br />[swf:version](#list_swf-swf_version)
  - **Access level:** Write

- **   [RequestCancelWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RequestCancelWorkflowExecution.html)  **
  - **Description:** Grants permission to record a WorkflowExecutionCancelRequested event in the currently running workflow execution identified by the given domain, workflowId, and runId
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RespondActivityTaskCanceled](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCanceled.html)  **
  - **Description:** Grants permission to workers to tell the service that the ActivityTask identified by the taskToken was successfully canceled
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RespondActivityTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskCompleted.html)  **
  - **Description:** Grants permission to workers to tell the service that the ActivityTask identified by the taskToken completed successfully with a result (if provided)
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:activityType.name](#list_swf-swf_activityType.name)<br />[swf:activityType.version](#list_swf-swf_activityType.version)<br />[swf:tagList.member.0](#list_swf-swf_tagList.member.0)<br />[swf:tagList.member.1](#list_swf-swf_tagList.member.1)<br />[swf:tagList.member.2](#list_swf-swf_tagList.member.2)<br />[swf:tagList.member.3](#list_swf-swf_tagList.member.3)<br />[swf:tagList.member.4](#list_swf-swf_tagList.member.4)<br />[swf:taskList.name](#list_swf-swf_taskList.name)<br />[swf:workflowType.name](#list_swf-swf_workflowType.name)<br />[swf:workflowType.version](#list_swf-swf_workflowType.version)
  - **Access level:** Write

- **   [RespondActivityTaskFailed](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondActivityTaskFailed.html)  **
  - **Description:** Grants permission to workers to tell the service that the ActivityTask identified by the taskToken has failed with reason (if specified)
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RespondDecisionTaskCompleted](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_RespondDecisionTaskCompleted.html)  **
  - **Description:** Grants permission to deciders to tell the service that the DecisionTask identified by the taskToken has successfully completed
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SignalWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_SignalWorkflowExecution.html)  **
  - **Description:** Grants permission to record a WorkflowExecutionSignaled event in the workflow execution history and create a decision task for the workflow execution identified by the given domain, workflowId and runId
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_StartWorkflowExecution.html)  **
  - **Description:** Grants permission to start an execution of the workflow type in the specified domain using the provided workflowId and input data
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:tagList.member.0](#list_swf-swf_tagList.member.0)<br />[swf:tagList.member.1](#list_swf-swf_tagList.member.1)<br />[swf:tagList.member.2](#list_swf-swf_tagList.member.2)<br />[swf:tagList.member.3](#list_swf-swf_tagList.member.3)<br />[swf:tagList.member.4](#list_swf-swf_tagList.member.4)<br />[swf:taskList.name](#list_swf-swf_taskList.name)<br />[swf:workflowType.name](#list_swf-swf_workflowType.name)<br />[swf:workflowType.version](#list_swf-swf_workflowType.version)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AWS SWF resource
  - **Resource types (\*required):** [domain](#list_swf-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_swf-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_swf-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TerminateWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_TerminateWorkflowExecution.html)  **
  - **Description:** Grants permission to record a WorkflowExecutionTerminated event and force closure of the workflow execution identified by the given domain, runId, and workflowId
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UndeprecateActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateActivityType.html)  **
  - **Description:** Grants permission to undeprecate a previously deprecated activity type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:activityType.name](#list_swf-swf_activityType.name)<br />[swf:activityType.version](#list_swf-swf_activityType.version)
  - **Access level:** Write

- **   [UndeprecateDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateDomain.html)  **
  - **Description:** Grants permission to undeprecate a previously deprecated domain
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UndeprecateWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UndeprecateWorkflowType.html)  **
  - **Description:** Grants permission to undeprecate a previously deprecated workflow type
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[swf:workflowType.name](#list_swf-swf_workflowType.name)<br />[swf:workflowType.version](#list_swf-swf_workflowType.version)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from an AWS SWF resource
  - **Resource types (\*required):** [domain](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_swf-aws_TagKeys)
  - **Access level:** Tagging, Write



## Permission-only actions for Amazon Simple Workflow Service
<a name="list_swf-permission-only-actions"></a>

The following actions are defined by Amazon Simple Workflow Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CancelTimer](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to cancel a previously started timer and record a TimerCanceled event in the history
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to close the workflow execution and record a WorkflowExecutionCanceled event in the history
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CompleteWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to close the workflow execution and record a WorkflowExecutionCompleted event in the history
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ContinueAsNewWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to close the workflow execution and start a new workflow execution of the same type using the same workflow ID and a unique run Id
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [FailWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to close the workflow execution and record a WorkflowExecutionFailed event in the history
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RecordMarker](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to record a MarkerRecorded event in the history
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RequestCancelActivityTask](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to attempt to cancel a previously scheduled activity task
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RequestCancelExternalWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to request that a request be made to cancel the specified external workflow execution
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ScheduleActivityTask](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to schedule an activity task
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SignalExternalWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to request a signal to be delivered to the specified external workflow execution and records
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartChildWorkflowExecution](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to request that a child workflow execution be started
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTimer](${APIReferenceDocPage}API_Decision.html)  **
  - **Description:** Grants permission to start a timer for a workflow execution
  - **Resource types (\*required):** [domain\*](#list_swf-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Simple Workflow Service
<a name="list_swf-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [domain](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-domains.html)  | arn:${Partition}:swf::${Account}:/domain/${DomainName} | [aws:ResourceTag/${TagKey}](#list_swf-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Simple Workflow Service
<a name="list_swf-policy-keys"></a>

Amazon Simple Workflow Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag of the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag of the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag of the key | ArrayOfString | 
|   [swf:activityType.name](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the name of the activity type | String | 
|   [swf:activityType.version](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the version of the activity type | String | 
|   [swf:defaultTaskList.name](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the name of the default task list | String | 
|   [swf:name](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the name of activities or workflows | String | 
|   [swf:tagFilter.tag](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the value of tagFilter.tag | String | 
|   [swf:tagList.member.0](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the specified tag | String | 
|   [swf:tagList.member.1](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the specified tag | String | 
|   [swf:tagList.member.2](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the specified tag | String | 
|   [swf:tagList.member.3](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the specified tag | String | 
|   [swf:tagList.member.4](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the specified tag | String | 
|   [swf:taskList.name](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the name of the tasklist  | String | 
|   [swf:typeFilter.name](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the name of the type filter | String | 
|   [swf:typeFilter.version](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the version of the type filter | String | 
|   [swf:version](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the version of activities or workflows | String | 
|   [swf:workflowType.name](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the name of the workflow type | String | 
|   [swf:workflowType.version](https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html##swf-dev-iam.api)  | Filters access by the version of the workflow type | String | 