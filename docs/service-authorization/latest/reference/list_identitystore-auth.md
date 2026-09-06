

# Actions, resources, and condition keys for AWS Identity Store Auth
<a name="list_identitystore-auth"></a>

AWS Identity Store Auth (service prefix: `identitystore-auth`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/singlesignon/latest/userguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/iam-auth-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/identitystore-auth/identitystore-auth.json) for this service.

**Topics**
+ [Actions defined by AWS Identity Store Auth](#list_identitystore-auth-actions-as-permissions)
+ [Permission-only actions for AWS Identity Store Auth](#list_identitystore-auth-permission-only-actions)
+ [Resource types defined by AWS Identity Store Auth](#list_identitystore-auth-resources-for-iam-policies)
+ [Condition keys for AWS Identity Store Auth](#list_identitystore-auth-policy-keys)

## Actions defined by AWS Identity Store Auth
<a name="list_identitystore-auth-actions-as-permissions"></a>

AWS Identity Store Auth has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Identity Store Auth
<a name="list_identitystore-auth-permission-only-actions"></a>

The following actions are defined by AWS Identity Store Auth but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [BatchDeleteSession](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-app-session.html)  | Grants permission to delete a batch of specified sessions |  |   | Write | 
|   [BatchGetSession](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-app-session.html)  | Grants permission to return session attributes for a batch of specified sessions |  |   | Read | 
|   [ListSessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-app-session.html)  | Grants permission to retrieve a list of active sessions for the specified user |  |   | List | 

## Resource types defined by AWS Identity Store Auth
<a name="list_identitystore-auth-resources-for-iam-policies"></a>

AWS Identity Store Auth does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Identity Store Auth
<a name="list_identitystore-auth-policy-keys"></a>

AWS Identity Store Auth has no service-specific condition keys that can be used in the `Condition` element of policy statements.