# Manage users with an external identity provider

If your IAM Identity Center is connected to an external identity provider (IdP) such as Okta
or Microsoft Entra ID, users must be created and managed in that external system.
The Deadline Cloud console cannot create new users when an external IdP is configured.

After users are created in your external IdP and synchronized to IAM Identity Center, you can assign them
permissions to Deadline Cloud resources. See [Understanding access levels](manage-users-by-farm.md "manage-users-by-farm.md") for information about
assigning permissions at the farm, queue, and fleet level.

For information about managing your external identity provider configuration, see [Manage
your identity source](../../../singlesignon/latest/userguide/manage-your-identity-source.md "../../../singlesignon/latest/userguide/manage-your-identity-source.md") in the IAM Identity Center User Guide.
