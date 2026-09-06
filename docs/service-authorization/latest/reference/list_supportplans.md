

# Actions, resources, and condition keys for AWS Support Plans
<a name="list_supportplans"></a>

AWS Support Plans (service prefix: `supportplans`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awssupport/latest/user/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awssupport/latest/user/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/supportplans/supportplans.json) for this service.

**Topics**
+ [Actions defined by AWS Support Plans](#list_supportplans-actions-as-permissions)
+ [Permission-only actions for AWS Support Plans](#list_supportplans-permission-only-actions)
+ [Resource types defined by AWS Support Plans](#list_supportplans-resources-for-iam-policies)
+ [Condition keys for AWS Support Plans](#list_supportplans-policy-keys)

## Actions defined by AWS Support Plans
<a name="list_supportplans-actions-as-permissions"></a>

AWS Support Plans has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Support Plans
<a name="list_supportplans-permission-only-actions"></a>

The following actions are defined by AWS Support Plans but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcceptSupportAgreement](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to accept a support agreement for this AWS account |  |   | Write | 
|   [CancelSupportAgreement](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to cancel a support agreement for this AWS account |  |   | Write | 
|   [CreateSupportAgreement](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to create a support agreement for this AWS account |  |   | Write | 
|   [CreateSupportPlanSchedule](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to create support plan schedules for this AWS account |  |   | Write | 
|   [GetSupportAgreement](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to view details about a support agreement for this AWS account |  |   | Read | 
|   [GetSupportPlan](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to view details about the current support plan for this AWS account |  |   | Read | 
|   [GetSupportPlanUpdateStatus](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to view details about the status for a request to update a support plan |  |   | Read | 
|   [ListSupportAgreementRevisions](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to list support agreement revisions for this AWS account |  |   | List | 
|   [ListSupportAgreements](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to list support agreements for this AWS account |  |   | List | 
|   [ListSupportPlanModifiers](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to view a list of all support plan modifiers for this account |  |   | List | 
|   [RejectSupportAgreement](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to reject a support agreement for this AWS account |  |   | Write | 
|   [StartSupportPlanUpdate](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to update the support plan for this AWS account |  |   | Write | 
|   [UpdateSupportAgreement](https://docs.aws.amazon.com/awssupport/latest/user/security-support-plans.html)  | Grants permission to update a support agreement for this AWS account |  |   | Write | 

## Resource types defined by AWS Support Plans
<a name="list_supportplans-resources-for-iam-policies"></a>

AWS Support Plans does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Support Plans
<a name="list_supportplans-policy-keys"></a>

AWS Support Plans has no service-specific condition keys that can be used in the `Condition` element of policy statements.