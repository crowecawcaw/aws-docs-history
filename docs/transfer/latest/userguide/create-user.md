# Managing users for server endpoints

In the following sections, you can find information about how to add users using AWS Transfer Family,
AWS Directory Service for Microsoft Active Directory or a custom identity provider.

As part of each user's properties, you also store that user's Secure Shell (SSH)
public key. Doing so is required for key-based authentication. The private key is stored
locally on your user's computer. When your user sends an authentication request to your
server by using a client, your server first confirms that the user has access to the
associated SSH private key. The server then successfully authenticates the user.

###### Note

For automated deployment and management of users with multiple SSH keys, see [Transfer Family Terraform modules](terraform.md "terraform.md").

In addition, you specify a user's home directory, or landing directory, and assign an
AWS Identity and Access Management (IAM) role to the user. Optionally, you can provide a session policy to limit
user access only to the home directory of your Amazon S3 bucket.

###### Important

AWS Transfer Family blocks usernames that are 1 or 2 characters long from authenticating to SFTP
servers. Additionally, we also block the `root`user name.

The reason behind this is due to the large volume of malicious login attempts by
password scanners.

## Amazon EFS vs. Amazon S3

Characteristics of each storage option:

- To limit access: Amazon S3 supports session policies; Amazon EFS supports POSIX user,
  group, and secondary group IDs
- Both support public/private keys
- Both support home directories
- Both support logical directories

###### Note

For Amazon S3, most of the support for logical directories is via API/CLI. You
can use the **Restricted** check box in the console to lock
down a user to their home directory, but you cannot specify a virtual
directory structure.

## Logical directories

If you are specifying logical directory values for your user, the parameter you use
depends on the type of user.

- For service-managed users, provide logical directory values in `HomeDirectoryMappings`.
- For custom identity provider users, provide logical directory values in `HomeDirectoryDetails`.

AWS Transfer Family supports specifying a HomeDirectory value when using the LOGICAL
HomeDirectoryType. This applies to Service Managed users, Active Directory access, and
Custom Identity Provider implementations where the HomeDirectoryDetails are provided in
the response.

###### Important

When specifying a HomeDirectory with LOGICAL HomeDirectoryType, the value must map
to one of your logical directory mappings. The service validates this during both
user creation and updates to prevent configurations that would not work.

### Default behavior

By default, if left unspecified, the HomeDirectory is set to "/" for LOGICAL mode.
This behavior is unchanged and remains compatible with existing user
definitions.

- Make sure to map your HomeDirectory to an _Entry_ and
  not a _Target_. For more details, see [Rules for using logical directories](logical-dir-mappings.md#logical-dir-rules "logical-dir-mappings.md#logical-dir-rules").
- For details on how a virtual directory is structured see [Virtual directory structure](implement-log-dirs.md#virtual-dirs "implement-log-dirs.md#virtual-dirs").

### Custom Identity Provider

considerations

When using a Custom Identity Provider, you can now specify a HomeDirectory in the
response while using LOGICAL HomeDirectoryType. The TestIdentityProvider API call
will produce correct results when the Custom IDP specifies a HomeDirectory in
LOGICAL mode.

Example Custom IDP response with HomeDirectory and LOGICAL
HomeDirectoryType:

```
{
  "Role": "arn:aws:iam::123456789012:role/transfer-user-role",
  "HomeDirectoryType": "LOGICAL",
  "HomeDirectory": "/marketing",
  "HomeDirectoryDetails": "[{\"Entry\":\"/\",\"Target\":\"/bucket/home\"},{\"Entry\":\"/marketing\",\"Target\":\"/marketing-bucket/campaigns\"}]"
}
```

## Active Directory group quotas

AWS Transfer Family has a default limit of 100 Active Directory groups per server. If your use
case requires more than 100 groups, consider using a custom identity provider solution
as described in [Simplify Active Directory authentication with a custom identity provider for
AWS Transfer Family](https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/ "https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/").

This limit applies to servers using the following identity providers:

- AWS Directory Service for Microsoft Active Directory
- AWS Directory Service for Entra ID Domain Services

If you need to request a service limit increase, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the
_AWS General Reference_. If your use case requires more
than 100 groups, consider using a custom identity provider solution as described in
[Simplify Active Directory authentication with a custom identity provider for
AWS Transfer Family](https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/ "https://aws.amazon.com/blogs/storage/simplify-active-directory-authentication-with-a-custom-identity-provider-for-aws-transfer-family/").

For troubleshooting information related to Active Directory group limits, see [Active Directory group limits exceeded](auth-issues.md#managed-ad-group-limits "auth-issues.md#managed-ad-group-limits").

###### Topics

- [Working with service-managed users](service-managed-users.md "service-managed-users.md")
- [Working with custom identity providers](custom-idp-intro.md "custom-idp-intro.md")
- [Using AWS Directory Service for Microsoft
  Active Directory](directory-services-users.md "directory-services-users.md")
- [Using AWS Directory Service for Entra ID Domain
  Services](azure-sftp.md "azure-sftp.md")
