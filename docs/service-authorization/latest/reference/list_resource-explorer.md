# Actions, resources, and condition keys for Tag Editor

Tag Editor (service prefix: `resource-explorer`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../ARG/latest/userguide.md "../../../ARG/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../ARG/latest/userguide.md "../../../ARG/latest/userguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../ARG/latest/userguide.md "../../../ARG/latest/userguide.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/resource-explorer/resource-explorer.json "https://servicereference.us-east-1.amazonaws.com/v1/resource-explorer/resource-explorer.json") for this service.

###### Topics

- [Actions defined by Tag Editor](#list_resource-explorer-actions-as-permissions "#list_resource-explorer-actions-as-permissions")
- [Permission-only actions for Tag Editor](#list_resource-explorer-permission-only-actions "#list_resource-explorer-permission-only-actions")
- [Resource types defined by Tag Editor](#list_resource-explorer-resources-for-iam-policies "#list_resource-explorer-resources-for-iam-policies")
- [Condition keys for Tag Editor](#list_resource-explorer-policy-keys "#list_resource-explorer-policy-keys")

## Actions defined by Tag Editor

Tag Editor has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for Tag Editor

The following actions are defined by Tag Editor but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                    | Description                                                                           | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [ListResourceTypes](../../../ARG/latest/userguide/gettingstarted-prereqs.md#rg-permissions-te "../../../ARG/latest/userguide/gettingstarted-prereqs.md#rg-permissions-te") | Grants permission to retrieve the resource types currently supported by Tag Editor    |                             |                | List         |
| [ListResources](../../../ARG/latest/userguide/gettingstarted-prereqs.md#rg-permissions-te "../../../ARG/latest/userguide/gettingstarted-prereqs.md#rg-permissions-te")     | Grants permission to retrieve the identifiers of the resources in the AWS account     |                             |                | List         |
| [ListTags](../../../ARG/latest/userguide/gettingstarted-prereqs.md#rg-permissions-te "../../../ARG/latest/userguide/gettingstarted-prereqs.md#rg-permissions-te")          | Grants permission to retrieve the tags attached to the specified resource identifiers |                             |                | Read         |

## Resource types defined by Tag Editor

Tag Editor does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Tag Editor

Tag Editor has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
