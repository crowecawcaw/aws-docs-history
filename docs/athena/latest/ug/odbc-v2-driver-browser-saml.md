# Browser SAML

Browser SAML is a generic authentication plugin that can work with SAML based identity
providers and support multi-factor authentication. For detailed configuration
information, see [Configure single sign-on using ODBC, SAML 2.0, and the Okta Identity Provider](okta-saml-sso.md "okta-saml-sso.md").

## Authentication type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**     |
| -------------------------- | ------------------ | ----------------- | --------------------------------- |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=BrowserSAML;` |

## Preferred role

The Amazon Resource Name (ARN) of the role to assume. If your SAML assertion has
multiple roles, you can specify this parameter to choose the role to be assumed.
This role should be present in the SAML assertion. For more information about ARN
roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the
_AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                        |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------- |
| preferred_role             | Optional           | `none`            | `preferred_role=arn:aws:IAM::123456789012:id/user1;` |

## Session duration

The duration, in seconds, of the role session. For more information, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| duration                   | Optional           | `900`             | `duration=900;`               |

## Login URL

The single sign-on URL that is displayed for your application.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                                                                 |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------- |
| login_url                  | Required           | `none`            | `login_url=https://trial-1234567.okta.com/app/trial-1234567_oktabrowsersaml_1/zzz4izzzAzDFBzZz1234/sso/saml;` |

## Listen port

The port number that is used to listen for the SAML response. This value should
match the IAM Identity Center URL that you configured the IdP with (for example,
`http://localhost:7890/athena`).

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| listen_port                | Optional           | `7890`            | `listen_port=7890;`           |

## Timeout

The duration, in seconds, before the plugin stops waiting for the SAML response
from the identity provider.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| timeout                    | Optional           | `120`             | `timeout=90;`                 |
