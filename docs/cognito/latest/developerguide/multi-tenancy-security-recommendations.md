# Multi-tenancy security

recommendations

To help make your application more secure, we recommend the following:

- Validate tenancy in your app with Amazon Verified Permissions. Build policies that examine user
  pool, app client, group, or custom-attribute entitlement before you permit a
  user's request in your application. AWS created Verified Permissions [identity
  sources](../../../verifiedpermissions/latest/userguide/identity-providers.md "../../../verifiedpermissions/latest/userguide/identity-providers.md") with Amazon Cognito user pools in mind. Verified Permissions has [additional guidance](../../../verifiedpermissions/latest/userguide/design-multi-tenancy-considerations.md "../../../verifiedpermissions/latest/userguide/design-multi-tenancy-considerations.md") for multi-tenancy management.
- Use only a verified email address to authorize user access to a tenant based
  on domain match. Do not trust email addresses and phone numbers unless your app
  verifies them, or the external IdP gives a proof of verification. For more
  details on setting these permissions, see [Attribute Permissions and
  Scopes](user-pool-settings-attributes.md#user-pool-settings-attribute- permissions-and-scopes.html "user-pool-settings-attributes.md#user-pool-settings-attribute- permissions-and-scopes.html").
- Use _immutable_, or read-only, custom
  attributes for the user profile attributes that identify tenants. You can only
  set the value of immutable attributes when you create a user or a user signs up
  in your user pool. Also, give app clients read-only access to the
  attributes.
- Use 1:1 mapping between a tenant's external IdP and application client to
  prevent unauthorized cross-tenant access. A user who has been authenticated by
  an external IdP, and who has a valid Amazon Cognito session cookie, can access other
  tenant apps that trust the same IdP.
- When you implement tenant-matching and authorization logic in your
  application, restrict users so that they can't modify the criteria that
  authorize user access to the tenants. Also, if an external IdP is being used for
  federation, restrict tenant identity provider administrators so that they can't
  modify user access.
