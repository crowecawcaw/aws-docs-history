# Okta

Okta is a SAML-based authentication plugin that works with the Okta identity provider. For
information about configuring federation for Okta and Amazon Athena, see [Configure SSO for ODBC using the Okta plugin and Okta Identity Provider](odbc-okta-plugin.md "odbc-okta-plugin.md").

## Authentication Type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| AuthenticationType         | Required           | `IAM Credentials` | `AuthenticationType=Okta;`    |

## User ID

Your Okta user name.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| UID                        | Required           | `none`            | `UID=jane.doe@org.com;`       |

## Password

Your Okta user password.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**  |
| -------------------------- | ------------------ | ----------------- | ------------------------------ |
| PWD                        | Required           | `none`            | `PWD=oktauserpasswordexample;` |

## Preferred role

The Amazon Resource Name (ARN) of the role to assume. For more information about ARN
roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                        |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------- |
| preferred_role             | Optional           | `none`            | `preferred_role=arn:aws:IAM::123456789012:id/user1;` |

## Session duration

The duration, in seconds, of the role session. For more information, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| duration                   | Optional           | `900`             | `duration=900;`               |

## IdP host

The URL for your Okta organization. You can extract the `idp_host`
parameter from the **Embed Link** URL in your Okta application. For
steps, see [Retrieve ODBC configuration information from Okta](odbc-okta-plugin.md#odbc-okta-plugin-retrieve-odbc-configuration-information-from-okta "odbc-okta-plugin.md#odbc-okta-plugin-retrieve-odbc-configuration-information-from-okta"). The first segment after `https://`, up to and including
`okta.com` is your IdP host (for example,
`http://trial-1234567.okta.com`).

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**     |
| -------------------------- | ------------------ | ----------------- | --------------------------------- |
| idp_host                   | Required           | `None`            | `idp_host=dev-99999999.okta.com;` |

## IdP port

The port number to use to connect to your IdP host.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| idp_port                   | Required           | `None`            | `idp_port=443;`               |

## Okta app ID

The two-part identifier for your application. You can extract the `app_id`
parameter from the **Embed Link** URL in your Okta application. For
steps, see [Retrieve ODBC configuration information from Okta](odbc-okta-plugin.md#odbc-okta-plugin-retrieve-odbc-configuration-information-from-okta "odbc-okta-plugin.md#odbc-okta-plugin-retrieve-odbc-configuration-information-from-okta"). The application ID is the last two segments of the URL, including the forward slash
in the middle. The segments are two 20-character strings with a mix of numbers and upper
and lowercase letters (for example,
`Abc1de2fghi3J45kL678/abc1defghij2klmNo3p4`).

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                       |
| -------------------------- | ------------------ | ----------------- | --------------------------------------------------- |
| app_id                     | Required           | `None`            | `app_id=0oa25kx8ze9A3example/alnexamplea0piaWa0g7;` |

## Okta app name

The name of the Okta application.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**   |
| -------------------------- | ------------------ | ----------------- | ------------------------------- |
| app_name                   | Required           | `None`            | `app_name=amazon_aws_redshift;` |

## Okta wait time

Specifies the duration in seconds to wait for the multifactor authentication (MFA)
code.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| okta_mfa_wait_time         | Optional           | `10`              | `okta_mfa_wait_time=20;`      |

## Okta MFA type

The MFA factor type. Supported types are Google Authenticator, SMS (Okta), Okta Verify
with Push, and Okta Verify with TOTP. Individual organization security policies
determine whether or not MFA is required for user login.

| **Connection string name** | **Parameter type** | **Default value** | **Possible values**                                                                 | **Connection string example**       |
| -------------------------- | ------------------ | ----------------- | ----------------------------------------------------------------------------------- | ----------------------------------- |
| okta_mfa_type              | `Optional`         | `None`            | `googleauthenticator, smsauthentication, oktaverifywithpush,<br>oktaverifywithtotp` | `okta_mfa_type=oktaverifywithpush;` |

## Okta phone number

The phone number to use with AWS SMS authentication. This parameter is required only for
multifactor enrollment. If your mobile number is already enrolled, or if AWS SMS
authentication is not used by the security policy, you can ignore this field.

| **Connection string name** | **Parameter type**                              | **Default value** | **Connection string example**        |
| -------------------------- | ----------------------------------------------- | ----------------- | ------------------------------------ |
| okta_mfa_phone_number      | Required for MFA enrollment, optional otherwise | `None`            | `okta_mfa_phone_number=19991234567;` |

## Enable Okta file cache

Enables a temporary credentials cache. This connection parameter enables temporary
credentials to be cached and reused between the multiple processes opened by BI
applications. Use this option to avoid the Okta API throttling limit.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| okta_cache                 | Optional           | `0`               | `okta_cache=1;`               |
