# Managing custom authorizers

You can manage your authorizers by using the following APIs.

- [ListAuthorizers](../apireference/API_ListAuthorizers.md "../apireference/API_ListAuthorizers.md"): Show all authorizers in your
  account.
- [DescribeAuthorizer](../apireference/API_DescribeAuthorizer.md "../apireference/API_DescribeAuthorizer.md"): Displays properties of the specified
  authorizer. These values include creation date, last modified date, and
  other attributes.
- [SetDefaultAuthorizer](../apireference/API_SetDefaultAuthorizer.md "../apireference/API_SetDefaultAuthorizer.md"): Specifies the default authorizer for
  your AWS IoT Core data endpoints. AWS IoT Core uses this authorizer if a
  device doesn't pass AWS IoT Core credentials and doesn't specify an
  authorizer. For more information about using AWS IoT Core credentials, see
  [Client authentication](client-authentication.md "client-authentication.md").
- [UpdateAuthorizer](../apireference/API_UpdateAuthorizer.md "../apireference/API_UpdateAuthorizer.md"):  Changes the status, token key name, or
  public keys for the specified authorizer.
- [DeleteAuthorizer](../apireference/API_DeleteAuthorizer.md "../apireference/API_DeleteAuthorizer.md"): Deletes the specified authorizer.

###### Note

You can't update an authorizer's signing requirement. This means that you
can't disable signing in an existing authorizer that requires it. You also
can't require signing in an existing authorizer that doesn't require it.
