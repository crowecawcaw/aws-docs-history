# AD FS

AD FS is a SAML based authentication plugin that works with the Active Directory
Federation Service (AD FS) identity provider. The plugin supports [Integrated Windows authentication](https://learn.microsoft.com/en-us/aspnet/web-api/overview/security/integrated-windows-authentication "https://learn.microsoft.com/en-us/aspnet/web-api/overview/security/integrated-windows-authentication") and form-based authentication. If you use
Integrated Windows Authentication, you can omit the user name and password. For
information about configuring AD FS and Athena, see [Configure federated access to Amazon Athena for Microsoft AD FS
users using an ODBC client](odbc-adfs-saml.md "odbc-adfs-saml.md").

## Authentication

type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=ADFS;`    |

## User ID

Your user name for connecting to the AD FS server. For Integrated Windows
Authentication, you can omit the user name. If your AD FS setup requires a user
name, you must provide it in the connection parameter.

| **Connection string name** | **Parameter type**                             | **Default value** | **Connection string example** |
| -------------------------- | ---------------------------------------------- | ----------------- | ----------------------------- |
| UID                        | Optional for windows integrated authentication | `none`            | `UID=domain\username;`        |

## Password

Your password for connecting to the AD FS server. Like the user name field, you
can omit the user name if you use Integrated Windows Authentication. If your AD FS
setup requires a password, you must provide it in the connection parameter.

| **Connection string name** | **Parameter type**                             | **Default value** | **Connection string example** |
| -------------------------- | ---------------------------------------------- | ----------------- | ----------------------------- |
| PWD                        | Optional for windows integrated authentication | `none`            | `PWD=password_3EXAMPLE;`      |

## Preferred role

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has
multiple roles, you can specify this parameter to choose the role to be assumed.
This role should present in the SAML assertion. For more information about ARN
roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                        |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------- |
| preferred_role             | Optional           | `none`            | `preferred_role=arn:aws:IAM::123456789012:id/user1;` |

## Session duration

The duration, in seconds, of the role session. For more information about session
duration, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| duration                   | Optional           | `900`             | `duration=900;`               |

## IdP host

The name of the AD FS service host.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**           |
| -------------------------- | ------------------ | ----------------- | --------------------------------------- |
| idp_host                   | Require            | `none`            | `idp_host=<server-name>.<company.com>;` |

## IdP port

The port to use to connect to the AD FS host.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| idp_port                   | Required           | `none`            | `idp_port=443;`               |

## LoginToRP

The trusted relying party. Use this parameter to override the AD FS relying party
endpoint URL.

| **Connection string name** | **Parameter type** | **Default value**        | **Connection string example** |
| -------------------------- | ------------------ | ------------------------ | ----------------------------- |
| LoginToRP                  | Optional           | `urn:amazon:webservices` | `LoginToRP=trustedparty;`     |
