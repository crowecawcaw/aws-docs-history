

# Data retrieval APIs for Amazon Simple Workflow Service
<a name="amazonsimpleworkflowservice"></a>

Amazon Simple Workflow Service provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="swf-CountClosedWorkflowExecutions"></a>[CountClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountClosedWorkflowExecutions.html) | Return the number of closed workflow executions within the given domain that meet the specified filtering criteria | Read | 
| <a name="swf-CountOpenWorkflowExecutions"></a>[CountOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountOpenWorkflowExecutions.html) | Return the number of open workflow executions within the given domain that meet the specified filtering criteria | Read | 
| <a name="swf-CountPendingActivityTasks"></a>[CountPendingActivityTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingActivityTasks.html) | Return the estimated number of activity tasks in the specified task list | Read | 
| <a name="swf-CountPendingDecisionTasks"></a>[CountPendingDecisionTasks](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_CountPendingDecisionTasks.html) | Return the estimated number of decision tasks in the specified task list | Read | 
| <a name="swf-DescribeActivityType"></a>[DescribeActivityType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeActivityType.html) | Return information about the specified activity type | Read | 
| <a name="swf-DescribeDomain"></a>[DescribeDomain](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeDomain.html) | Return information about the specified domain, including its description and status | Read | 
| <a name="swf-DescribeWorkflowExecution"></a>[DescribeWorkflowExecution](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowExecution.html) | Return information about the specified workflow execution including its type and some statistics | Read | 
| <a name="swf-DescribeWorkflowType"></a>[DescribeWorkflowType](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_DescribeWorkflowType.html) | Return information about the specified workflow type | Read | 
| <a name="swf-GetWorkflowExecutionHistory"></a>[GetWorkflowExecutionHistory](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_GetWorkflowExecutionHistory.html) | Return the history of the specified workflow execution | Read | 
| <a name="swf-ListActivityTypes"></a>[ListActivityTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListActivityTypes.html) | Return information about all activities registered in the specified domain that match the specified name and registration status | List | 
| <a name="swf-ListClosedWorkflowExecutions"></a>[ListClosedWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListClosedWorkflowExecutions.html) | Return a list of closed workflow executions in the specified domain that meet the filtering criteria | List | 
| <a name="swf-ListDomains"></a>[ListDomains](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListDomains.html) | Return the list of domains registered in the account | List | 
| <a name="swf-ListOpenWorkflowExecutions"></a>[ListOpenWorkflowExecutions](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListOpenWorkflowExecutions.html) | Return a list of open workflow executions in the specified domain that meet the filtering criteria | List | 
| <a name="swf-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListTagsForResource.html) | List tags for an AWS SWF resource | List | 
| <a name="swf-ListWorkflowTypes"></a>[ListWorkflowTypes](https://docs.aws.amazon.com/amazonswf/latest/apireference/API_ListWorkflowTypes.html) | Return information about workflow types in the specified domain | List | 