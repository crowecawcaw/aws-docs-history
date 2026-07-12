# Actions, resources, and condition keys for AWS Identity Store Auth

AWS Identity Store Auth (service prefix: `identitystore-auth`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../singlesignon/latest/userguide.md "../../../singlesignon/latest/userguide.md").
- View a list of the [API operations available for
  this service](../../../singlesignon/latest/userguide.md "../../../singlesignon/latest/userguide.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../singlesignon/latest/userguide/iam-auth-access.md "../../../singlesignon/latest/userguide/iam-auth-access.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/identitystore-auth/identitystore-auth.json "https://servicereference.us-east-1.amazonaws.com/v1/identitystore-auth/identitystore-auth.json") for this service.

###### Topics

- [Actions defined by AWS Identity Store Auth](#list_identitystore-auth-actions-as-permissions "#list_identitystore-auth-actions-as-permissions")
- [Permission-only actions for AWS Identity Store Auth](#list_identitystore-auth-permission-only-actions "#list_identitystore-auth-permission-only-actions")
- [Resource types defined by AWS Identity Store Auth](#list_identitystore-auth-resources-for-iam-policies "#list_identitystore-auth-resources-for-iam-policies")
- [Condition keys for AWS Identity Store Auth](#list_identitystore-auth-policy-keys "#list_identitystore-auth-policy-keys")

## Actions defined by AWS Identity Store Auth

AWS Identity Store Auth has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Identity Store Auth

The following actions are defined by AWS Identity Store Auth but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                           | Description                                                                      | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [BatchDeleteSession](../../../singlesignon/latest/userguide/manage-app-session.md "../../../singlesignon/latest/userguide/manage-app-session.md") | Grants permission to delete a batch of specified sessions                        |                             |                | Write        |
| [BatchGetSession](../../../singlesignon/latest/userguide/manage-app-session.md "../../../singlesignon/latest/userguide/manage-app-session.md")    | Grants permission to return session attributes for a batch of specified sessions |                             |                | Read         |
| [ListSessions](../../../singlesignon/latest/userguide/manage-app-session.md "../../../singlesignon/latest/userguide/manage-app-session.md")       | Grants permission to retrieve a list of active sessions for the specified user   |                             |                | List         |

## Resource types defined by AWS Identity Store Auth

AWS Identity Store Auth does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Identity Store Auth

AWS Identity Store Auth has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
