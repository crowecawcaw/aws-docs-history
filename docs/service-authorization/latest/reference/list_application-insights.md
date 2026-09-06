

# Actions, resources, and condition keys for Amazon CloudWatch Application Insights
<a name="list_application-insights"></a>

Amazon CloudWatch Application Insights (service prefix: `applicationinsights`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/applicationinsights/applicationinsights.json) for this service.

**Topics**
+ [Actions defined by Amazon CloudWatch Application Insights](#list_application-insights-actions-as-permissions)
+ [Permission-only actions for Amazon CloudWatch Application Insights](#list_application-insights-permission-only-actions)
+ [Resource types defined by Amazon CloudWatch Application Insights](#list_application-insights-resources-for-iam-policies)
+ [Condition keys for Amazon CloudWatch Application Insights](#list_application-insights-policy-keys)

## Actions defined by Amazon CloudWatch Application Insights
<a name="list_application-insights-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AddWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_AddWorkload.html)  | Grants permission to add a workload |  |   | Write | 
|   [CreateApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateApplication.html)  | Grants permission to create an application from a resource group |  |   | Write | 
|   [CreateComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateComponent.html)  | Grants permission to create a component from a group of resources |  |   | Write | 
|   [CreateLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_CreateLogPattern.html)  | Grants permission to create log a pattern |  |   | Write | 
|   [DeleteApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteApplication.html)  | Grants permission to delete an application |  |   | Write | 
|   [DeleteComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteComponent.html)  | Grants permission to delete a component |  |   | Write | 
|   [DeleteLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DeleteLogPattern.html)  | Grants permission to delete a log pattern |  |   | Write | 
|   [DescribeApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeApplication.html)  | Grants permission to describe an application |  |   | Read | 
|   [DescribeComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponent.html)  | Grants permission to describe a component |  |   | Read | 
|   [DescribeComponentConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfiguration.html)  | Grants permission to describe a component's configuration |  |   | Read | 
|   [DescribeComponentConfigurationRecommendation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeComponentConfigurationRecommendation.html)  | Grants permission to describe the recommended application component configuration |  |   | Read | 
|   [DescribeLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeLogPattern.html)  | Grants permission to describe a log pattern |  |   | Read | 
|   [DescribeObservation](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeObservation.html)  | Grants permission to describe an observation |  |   | Read | 
|   [DescribeProblem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblem.html)  | Grants permission to describe a problem |  |   | Read | 
|   [DescribeProblemObservations](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeProblemObservations.html)  | Grants permission to describe the observation in a problem |  |   | Read | 
|   [DescribeWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_DescribeWorkload.html)  | Grants permission to describe a workload |  |   | Read | 
|   [ListApplications](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListApplications.html)  | Grants permission to list all applications |  |   | List | 
|   [ListComponents](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListComponents.html)  | Grants permission to list an application's components |  |   | List | 
|   [ListConfigurationHistory](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListConfigurationHistory.html)  | Grants permission to list configuration history |  |   | List | 
|   [ListLogPatternSets](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatternSets.html)  | Grants permission to list log pattern sets for an application |  |   | List | 
|   [ListLogPatterns](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListLogPatterns.html)  | Grants permission to list log patterns |  |   | List | 
|   [ListProblems](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListProblems.html)  | Grants permission to list the problems in an application |  |   | List | 
|   [ListTagsForResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListTagsForResource.html)  | Grants permission to list tags for the resource |  |   | Read | 
|   [ListWorkloads](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_ListWorkloads.html)  | Grants permission to list workloads |  |   | List | 
|   [RemoveWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_RemoveWorkload.html)  | Grants permission to remove a workload |  |   | Write | 
|   [TagResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_TagResource.html)  | Grants permission to tag a resource |  | [aws:RequestTag/${TagKey}](#list_application-insights-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_application-insights-aws_TagKeys) | Tagging, Write | 
|   [UntagResource](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UntagResource.html)  | Grants permission to untag a resource |  | [aws:TagKeys](#list_application-insights-aws_TagKeys) | Tagging, Write | 
|   [UpdateApplication](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateApplication.html)  | Grants permission to update an application |  |   | Write | 
|   [UpdateComponent](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponent.html)  | Grants permission to update a component |  |   | Write | 
|   [UpdateComponentConfiguration](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateComponentConfiguration.html)  | Grants permission to update a component's configuration |  |   | Write | 
|   [UpdateLogPattern](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateLogPattern.html)  | Grants permission to update a log pattern |  |   | Write | 
|   [UpdateProblem](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateProblem.html)  | Grants permission to update a problem |  |   | Write | 
|   [UpdateWorkload](https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_UpdateWorkload.html)  | Grants permission to update a workload |  |   | Write | 

## Permission-only actions for Amazon CloudWatch Application Insights
<a name="list_application-insights-permission-only-actions"></a>

The following actions are defined by Amazon CloudWatch Application Insights but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [Link](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.html#CloudWatch-Unified-Cross-Account-Setup-permissions)  | Grants permission to share Application Insights resources with a monitoring account |  |   | Write | 

## Resource types defined by Amazon CloudWatch Application Insights
<a name="list_application-insights-resources-for-iam-policies"></a>

Amazon CloudWatch Application Insights does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for Amazon CloudWatch Application Insights
<a name="list_application-insights-policy-keys"></a>

Amazon CloudWatch Application Insights defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by a list of tag keys that are allowed in the request | ArrayOfString | 