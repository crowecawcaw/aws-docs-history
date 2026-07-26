# Actions, resources, and condition keys for AWS Support Plans

AWS Support Plans (service prefix: `supportplans`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awssupport/latest/user.md "../../../awssupport/latest/user.md").
- View a list of the [API operations available for
  this service](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awssupport/latest/user/security.md "../../../awssupport/latest/user/security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/supportplans/supportplans.json "https://servicereference.us-east-1.amazonaws.com/v1/supportplans/supportplans.json") for this service.

###### Topics

- [Actions defined by AWS Support Plans](#list_supportplans-actions-as-permissions "#list_supportplans-actions-as-permissions")
- [Permission-only actions for AWS Support Plans](#list_supportplans-permission-only-actions "#list_supportplans-permission-only-actions")
- [Resource types defined by AWS Support Plans](#list_supportplans-resources-for-iam-policies "#list_supportplans-resources-for-iam-policies")
- [Condition keys for AWS Support Plans](#list_supportplans-policy-keys "#list_supportplans-policy-keys")

## Actions defined by AWS Support Plans

AWS Support Plans has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Support Plans

The following actions are defined by AWS Support Plans but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                | Description                                                                               | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [AcceptSupportAgreement](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")        | Grants permission to accept a support agreement for this AWS account                      |                             |                | Write        |
| [CancelSupportAgreement](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")        | Grants permission to cancel a support agreement for this AWS account                      |                             |                | Write        |
| [CreateSupportAgreement](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")        | Grants permission to create a support agreement for this AWS account                      |                             |                | Write        |
| [CreateSupportPlanSchedule](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")     | Grants permission to create support plan schedules for this AWS account                   |                             |                | Write        |
| [GetSupportAgreement](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")           | Grants permission to view details about a support agreement for this AWS account          |                             |                | Read         |
| [GetSupportPlan](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")                | Grants permission to view details about the current support plan for this AWS account     |                             |                | Read         |
| [GetSupportPlanUpdateStatus](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")    | Grants permission to view details about the status for a request to update a support plan |                             |                | Read         |
| [ListSupportAgreementRevisions](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md") | Grants permission to list support agreement revisions for this AWS account                |                             |                | List         |
| [ListSupportAgreements](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")         | Grants permission to list support agreements for this AWS account                         |                             |                | List         |
| [ListSupportPlanModifiers](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")      | Grants permission to view a list of all support plan modifiers for this account           |                             |                | List         |
| [RejectSupportAgreement](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")        | Grants permission to reject a support agreement for this AWS account                      |                             |                | Write        |
| [StartSupportPlanUpdate](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")        | Grants permission to update the support plan for this AWS account                         |                             |                | Write        |
| [UpdateSupportAgreement](../../../awssupport/latest/user/security-support-plans.md "../../../awssupport/latest/user/security-support-plans.md")        | Grants permission to update a support agreement for this AWS account                      |                             |                | Write        |

## Resource types defined by AWS Support Plans

AWS Support Plans does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Support Plans

AWS Support Plans has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
