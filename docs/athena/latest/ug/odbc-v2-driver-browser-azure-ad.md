# Browser Azure AD

Browser Azure AD is a SAML based authentication plugin that works with Azure AD identity
provider and supports multi-factor authentication. Unlike the standard Azure AD plugin, this
plugin does not require a user name, password, or client secret in the connection
parameters.

## Authentication Type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**        |
| -------------------------- | ------------------ | ----------------- | ------------------------------------ |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=BrowserAzureAD;` |

## Preferred role

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has
multiple roles, you can specify this parameter to choose the role to be assumed. The
role specified should be present in the SAML assertion. For more information about ARN
roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

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

## Tenant ID

Specifies your application tenant ID.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                       |
| -------------------------- | ------------------ | ----------------- | --------------------------------------------------- |
| idp_tenant                 | Required           | `none`            | `idp_tenant=123zz112z-z12d-1z1f-11zz-f111aa111234;` |

## Client ID

Specifies your application client ID.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                     |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------- |
| client_id                  | Required           | `none`            | `client_id=9178ac27-a1bc-1a2b-1a2b-a123abcd1234;` |

## Timeout

The duration, in seconds, before the plugin stops waiting for the SAML response from
Azure AD.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| timeout                    | Optional           | `120`             | `timeout=90;`                 |

## Enable Azure file cache

Enables a temporary credentials cache. This connection parameter enables temporary
credentials to be cached and reused between multiple processes. Use this option to
reduce the number of opened browser windows when you use BI tools such as Microsoft
Power BI.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| browser_azure_cache        | Optional           | `1`               | `browser_azure_cache=0;`      |
