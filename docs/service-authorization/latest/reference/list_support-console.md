

# Actions, resources, and condition keys for AWS Support Console
<a name="list_support-console"></a>

AWS Support Console (service prefix: `support-console`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-console.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awssupport/latest/user/support-console-access-control.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awssupport/latest/user/support-console-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/support-console/support-console.json) for this service.

**Topics**
+ [Actions defined by AWS Support Console](#list_support-console-actions-as-permissions)
+ [Permission-only actions for AWS Support Console](#list_support-console-permission-only-actions)
+ [Resource types defined by AWS Support Console](#list_support-console-resources-for-iam-policies)
+ [Condition keys for AWS Support Console](#list_support-console-policy-keys)

## Actions defined by AWS Support Console
<a name="list_support-console-actions-as-permissions"></a>

AWS Support Console has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Support Console
<a name="list_support-console-permission-only-actions"></a>

The following actions are defined by AWS Support Console but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CheckSubscription](${AuthZDocPage})  | Grants permission to check whether the account has access to given product |  |   | Read | 
|   [CreateCaseDraft](${AuthZDocPage})  | Grants permission to create or update case draft for the given case type |  |   | Write | 
|   [CreateContact](${AuthZDocPage})  | Grants permission to create an authenticated contact for the given contact type |  |   | Write | 
|   [DeleteCaseDraft](${AuthZDocPage})  | Grants permission to delete a case draft for the given case type |  |   | Write | 
|   [DescribeDynamicHelp](${AuthZDocPage})  | Grants permission to get dynamic help resources for given service and category |  |   | Read | 
|   [GetAccountGovCloudEnabled](${AuthZDocPage})  | Grants permission to determines whether the calling account is GovCloud enabled |  |   | Read | 
|   [GetAccountState](${AuthZDocPage})  | Grants permission to get the state of the calling account |  |   | Read | 
|   [GetBanner](${AuthZDocPage})  | Grants permission to get the support banner information |  |   | Read | 
|   [GetCaseDraft](${AuthZDocPage})  | Grants permission to get a case draft for given case type |  |   | Read | 
|   [GetIssueClassificationPredictions](${AuthZDocPage})  | Grants permission to get classification predictions of an issue |  |   | Read | 
|   [GetIssueTextSummary](${AuthZDocPage})  | Grants permission to get a generated text summary of an issue |  |   | Read | 
|   [GetQuestionnaire](${AuthZDocPage})  | Grants permission to get a feedback questionnaire |  |   | Read | 
|   [SaveFeedback](${AuthZDocPage})  | Grants permission to save questionnaire feedback |  |   | Write | 

## Resource types defined by AWS Support Console
<a name="list_support-console-resources-for-iam-policies"></a>

AWS Support Console does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Support Console
<a name="list_support-console-policy-keys"></a>

AWS Support Console has no service-specific condition keys that can be used in the `Condition` element of policy statements.