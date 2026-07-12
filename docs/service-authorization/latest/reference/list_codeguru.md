# Actions, resources, and condition keys for Amazon CodeGuru

Amazon CodeGuru (service prefix: `codeguru`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../codeguru/latest/profiler-ug.md "../../../codeguru/latest/profiler-ug.md").
- View a list of the [API operations available for
  this service](../../../codeguru/latest/profiler-api.md "../../../codeguru/latest/profiler-api.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../codeguru/latest/profiler-ug/security_iam_service-with-iam.md "../../../codeguru/latest/profiler-ug/security_iam_service-with-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/codeguru/codeguru.json "https://servicereference.us-east-1.amazonaws.com/v1/codeguru/codeguru.json") for this service.

###### Topics

- [Actions defined by Amazon CodeGuru](#list_codeguru-actions-as-permissions "#list_codeguru-actions-as-permissions")
- [Permission-only actions for Amazon CodeGuru](#list_codeguru-permission-only-actions "#list_codeguru-permission-only-actions")
- [Resource types defined by Amazon CodeGuru](#list_codeguru-resources-for-iam-policies "#list_codeguru-resources-for-iam-policies")
- [Condition keys for Amazon CodeGuru](#list_codeguru-policy-keys "#list_codeguru-policy-keys")

## Actions defined by Amazon CodeGuru

Amazon CodeGuru has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for Amazon CodeGuru

The following actions are defined by Amazon CodeGuru but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                            | Description                                                                                         | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetCodeGuruFreeTrialSummary](../../../codeguru/latest/profiler-api/API_GetCodeGuruFreeTrialSummary.md "../../../codeguru/latest/profiler-api/API_GetCodeGuruFreeTrialSummary.md") | Grants permission to get free trial summary for the CodeGuru service which includes expiration date |                             |                | Read         |

## Resource types defined by Amazon CodeGuru

Amazon CodeGuru does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Amazon CodeGuru

Amazon CodeGuru has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
