# Using the Amazon WorkSpaces Secure Browser

console

To access the Amazon WorkSpaces Secure Browser console, you must have a minimum set of permissions.
These permissions must allow you to list and view details about the WorkSpaces Secure Browser resources
in your AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console won't function as intended for
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match
the API operation that they're trying to perform.

To ensure that users and roles can still use the WorkSpaces Secure Browser console, also attach the
WorkSpaces Secure Browser `ConsoleAccess` or `ReadOnly` AWS managed policy to
the entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.
