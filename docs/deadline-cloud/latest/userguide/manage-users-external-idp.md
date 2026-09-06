

# Manage users with an external identity provider
<a name="manage-users-external-idp"></a>

If your IAM Identity Center is connected to an external identity provider (IdP) such as Okta or Microsoft Entra ID, users must be created and managed in that external system. The Deadline Cloud console cannot create new users when an external IdP is configured.

After users are created in your external IdP and synchronized to IAM Identity Center, you can assign them permissions to Deadline Cloud resources. See [Assign permissions to users and groups](assign-permissions-procedure.md) for information about assigning permissions at the farm, queue, and fleet level.

For information about managing your external identity provider configuration, see [Manage your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html) in the IAM Identity Center User Guide.