# Actions, resources, and condition keys for Application Discovery Arsenal

Application Discovery Arsenal (service prefix: `arsenal`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../application-discovery/latest/userguide.md "../../../application-discovery/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../application-discovery/latest/userguide.md "../../../application-discovery/latest/userguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../application-discovery/latest/userguide/setting-up.md#setting-up-user-policy "../../../application-discovery/latest/userguide/setting-up.md#setting-up-user-policy") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/arsenal/arsenal.json "https://servicereference.us-east-1.amazonaws.com/v1/arsenal/arsenal.json") for this service.

###### Topics

- [Actions defined by Application Discovery Arsenal](#list_arsenal-actions-as-permissions "#list_arsenal-actions-as-permissions")
- [Permission-only actions for Application Discovery Arsenal](#list_arsenal-permission-only-actions "#list_arsenal-permission-only-actions")
- [Resource types defined by Application Discovery Arsenal](#list_arsenal-resources-for-iam-policies "#list_arsenal-resources-for-iam-policies")
- [Condition keys for Application Discovery Arsenal](#list_arsenal-policy-keys "#list_arsenal-policy-keys")

## Actions defined by Application Discovery Arsenal

Application Discovery Arsenal has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for Application Discovery Arsenal

The following actions are defined by Application Discovery Arsenal but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                  | Description                                                                                     | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [RegisterOnPremisesAgent](../../../application-discovery/latest/userguide/setting-up.md "../../../application-discovery/latest/userguide/setting-up.md") | Grants permission to register AWS provided data collectors to the Application Discovery Service |                             |                | Write        |

## Resource types defined by Application Discovery Arsenal

Application Discovery Arsenal does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for Application Discovery Arsenal

Application Discovery Arsenal has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
