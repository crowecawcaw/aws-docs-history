# Browser trusted identity propagation credentials

This authentication type allows you to fetch a new JSON web token (JWT) from an external identity
provider and authenticate with Athena. You can use this plugin, to enable support for corporate
identities via trusted identity propagation. For more information on how to use trusted identity propagation with drivers, see [Use Trusted identity propagation with
Amazon Athena drivers](using-trusted-identity-propagation.md "using-trusted-identity-propagation.md").
You can also [configure and deploy
resources using CloudFormation](using-trusted-identity-propagation-cloudformation.md "using-trusted-identity-propagation-cloudformation.md").

With trusted identity propagation, identity context is added to an IAM role to identify the user requesting
access to AWS resources. For information on enabling and using trusted identity propagation, see [What is trusted identity propagation?](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md").

###### Note

The plugin is specifically designed for single-user desktop environments. In shared environments
like Windows Server, system administrators are responsible for establishing and maintaining security
boundaries between users.

## Authentication type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**        |
| -------------------------- | ------------------ | ----------------- | ------------------------------------ |
| AuthenticationType         | Required           | `none`            | `AuthenticationType=BrowserOidcTip;` |

## IDP well known configuration URL

The IDP Well Known Configuration URL is the endpoint that provides OpenID Connect configuration
details for your identity provider. This URL typically ends with `.well-known/openid-configuration`
and contains essential metadata about the authentication endpoints, supported features, and token
signing keys. For example, if you're using _Okta_, the URL might look like
`https://your-domain.okta.com/.well-known/openid-configuration`.

For troubleshooting: If you receive connection errors, verify that this URL is accessible
from your network and returns valid _OpenID Connect_ configuration JSON. The URL
must be reachable by the client where the driver is installed and should be provided by your
identity provider administrator.

| **Connection string name**   | **Parameter type** | **Default value** | **Connection string example**                                                          |
| ---------------------------- | ------------------ | ----------------- | -------------------------------------------------------------------------------------- |
| IdpWellKnownConfigurationUrl | Required           | `none`            | `IdpWellKnownConfigurationUrl=https://<your-domain>/.well-known/openid-configuration;` |

## Client Identifier

The client identifier issued to the application by the OpenID Connect provider.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                     |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------- |
| client_id                  | Required           | `none`            | `client_id=00001111-aaaa-2222-bbbb-3333cccc4444;` |

## Workgroup ARN

The Amazon Resource Name (ARN) of the Amazon Athena workgroup that contains the trusted
identity propagation configuration tags. For more information about workgroups, see
[WorkGroup](../APIReference/API_WorkGroup.md "../APIReference/API_WorkGroup.md").

###### Note

This parameter is different from the `Workgroup` parameter that specifies
where queries will run. You must set both parameters:

- `WorkgroupArn` - Points to the workgroup containing the trusted
  identity propagation configuration tags
- `Workgroup` - Specifies the workgroup where queries will execute
  While these typically reference the same workgroup, both parameters must be set
  explicitly for proper operation.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                          |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------------------------- |
| WorkGroupArn               | Required           | `none`            | `WorkgroupArn=arn:aws:athena:us-west-2:111122223333:workgroup/primary` |

## JWT application role ARN

The ARN of the role that will be assumed in the JWT exchange. This role is used for JWT exchange, getting IAM
Identity Center customer managed application ARN through workgroup tags, and getting
access role ARN. For more information about assuming roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md").

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                        |
| -------------------------- | ------------------ | ----------------- | -------------------------------------------------------------------- |
| ApplicationRoleArn         | Required           | `none`            | `ApplicationRoleArn=arn:aws:iam::111122223333:role/applicationRole;` |

## Role session name

A name for the IAM session. It can be anything you like, but typically you pass the name
or identifier that's associated with the user who is using your application. That way,
the temporary security credentials that your application will use are associated with
that user.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**     |
| -------------------------- | ------------------ | ----------------- | --------------------------------- |
| role_session_name          | Required           | `none`            | `role_session_name=familiarname;` |

## Client secret

The client secret is a confidential key issued by your identity provider that is used to
authenticate your application. While this parameter is optional and may not be required
for all authentication flows, it provides an additional layer of security when used. If your IDP
configuration requires a client secret, you must include this parameter with the value provided
by your identity provider administrator.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                        |
| -------------------------- | ------------------ | ----------------- | -------------------------------------------------------------------- |
| client_secret              | Optional           | `none`            | `client_secret=s0m3R@nd0mS3cr3tV@lu3Th@tS3cur3lyPr0t3ct5Th3Cl13nt;!` |

## Scope

The scope specifies what level of access your application is requesting from the identity provider.
You must include `openid` in the scope to receive an ID token containing
essential user identity claims. Your scope may need to include additional permissions like `email`
or `profile`, depending on which user claims your identity provider (such as _Microsoft Entra ID_)
is configured to include in the ID token. These claims are essential for proper _Trusted Identity
Propagation_ mapping. If user identity mapping fails, verify that your scope includes all necessary
permissions and your identity provider is configured to include the required claims in the ID token.
These claims must match your _Trusted Token Issuer_ mapping configuration in IAM Identity Center.

| **Connection string name** | **Parameter type** | **Default value**             | **Connection string example** |
| -------------------------- | ------------------ | ----------------------------- | ----------------------------- |
| Scope                      | Optional           | `openid email offline_access` | `Scope=openid email;`         |

## Session duration

The duration, in seconds, of the role session. For more information, see [AssumeRoleWithWebIdentity](../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md "../../../STS/latest/APIReference/API_AssumeRoleWithWebIdentity.md").

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| duration                   | Optional           | `3600`            | `duration=900;`               |

## JWT access role ARN

The ARN of the role that Athena assumes to make calls on the behalf of you.
For more information about assuming roles, see [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") in the _AWS Security Token Service API Reference_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                              |
| -------------------------- | ------------------ | ----------------- | ---------------------------------------------------------- |
| AccessRoleArn              | Optional           | `none`            | `AccessRoleArn=arn:aws:iam::111122223333:role/accessRole;` |

## IAM Identity Center customer managed application ARN

The ARN of IAM Identity Center customer managed IDC application. For more information about Customer
Managed Applications, see [customer managed
applications](../../../singlesignon/latest/userguide/customermanagedapps.md "../../../singlesignon/latest/userguide/customermanagedapps.md").

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                                                           |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------------------------------------------------------- |
| CustomerIdcApplicationArn  | Optional           | `none`            | `CustomerIdcApplicationArn=arn:aws:sso::111122223333:application/ssoins-111122223333/apl-111122223333;` |

## Identity provider port number

The local port number to use for the OAuth 2.0 callback server. This is used as redirect_uri
and you will need to allowlist this in your IDP application. The default generated redirect_uri is:
http://localhost:7890/athena

###### Warning

In shared environments like Windows Terminal Servers or Remote Desktop Services, the loopback
port (default: 7890) is shared among all users on the same machine. System administrators can
mitigate potential port hijacking risks by:

- Configuring different port numbers for different user groups
- Using Windows security policies to restrict port access
- Implementing network isolation between user sessions
  If these security controls cannot be implemented, we recommend using the
  [JWT trusted identity propagation](odbc-v2-driver-jwt-tip.md "odbc-v2-driver-jwt-tip.md")
  plugin instead, which doesn't require a loopback port.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| listen_port                | Optional           | `7890`            | `listen_port=8080;`           |

## Identity provider response timeout

The timeout in seconds to wait for the OAuth 2.0 callback response.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| IdpResponseTimeout         | Optional           | `120`             | `IdpResponseTimeout=140;`     |

## Enable file cache

The JwtTipFileCache parameter determines whether the driver caches the authentication token
between connections. Setting JwtTipFileCache to true reduces authentication prompts and improves
user experience, but should be used cautiously. This setting is best suited for single-user desktop
environments. In shared environments like Windows Server, it's recommended to keep this disabled
to prevent potential token sharing between users with similar connection strings.

For enterprise deployments using tools like PowerBI Server, we recommend using the
[JWT trusted identity propagation](odbc-v2-driver-jwt-tip.md "odbc-v2-driver-jwt-tip.md")
plugin instead of this authentication method.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| JwtTipFileCache            | Optional           | `0`               | `JwtTipFileCache=1;`          |
