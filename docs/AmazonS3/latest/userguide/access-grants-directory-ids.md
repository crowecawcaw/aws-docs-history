# S3 Access Grants and corporate directory identities

You can use Amazon S3 Access Grants to grant access to AWS Identity and Access Management (IAM) principals (users or
roles), both in the same AWS account and in others. However, in many cases, the entity
accessing the data is an end user from your corporate directory. Instead of granting access
to IAM principals, you can use S3 Access Grants to grant access directly to your corporate users and
groups. With S3 Access Grants, you no longer need to map your corporate identities to intermediate
IAM principals in order to access your S3 data through your corporate applications.

This new functionality—support for using end-user identities access to
data—is provided by associating your S3 Access Grants instance with an AWS IAM Identity Center instance.
IAM Identity Center supports standards-based identity providers and is the hub in AWS for any services
or features, including S3 Access Grants, that support end-user identities. IAM Identity Center provides
authentication support for corporate identities through its trusted identity propagation
feature. For more information, see [Trusted identity propagation across applications](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md").

To get started with workforce identity support in S3 Access Grants, as a prerequisite, you start in
IAM Identity Center by configuring identity provisioning between your corporate identity provider and
IAM Identity Center. IAM Identity Center supports corporate identity providers such as Okta,
Microsoft Entra ID (formerly Azure Active Directory), or
any other external identity provider (IdP) that supports the System for Cross-domain
Identity Management (SCIM) protocol. When you connect IAM Identity Center to your IdP and enable automatic
provisioning, the users and groups from your IdP are synchronized into the identity store in
IAM Identity Center. After this step, IAM Identity Center has its own view of your users and groups, so that you can
refer to them by using other AWS services and features, such as S3 Access Grants. For more
information about configuring IAM Identity Center automatic provisioning, see [Automatic
provisioning](../../../singlesignon/latest/userguide/provision-automatically.md "../../../singlesignon/latest/userguide/provision-automatically.md") in the _AWS IAM Identity Center User
Guide_.

IAM Identity Center is integrated with AWS Organizations so that you can centrally manage permissions across
multiple AWS accounts without configuring each of your accounts manually. In a typical
organization, your identity administrator configures one IAM Identity Center instance for the entire
organization, as a single point of identity synchronization. This IAM Identity Center instance typically
runs in a dedicated AWS account in your organization. In this common configuration, you
can refer to user and group identities in S3 Access Grants from any AWS account in the organization.

However, if your AWS Organizations administrator hasn't yet configured a central IAM Identity Center instance,
you can create a local one in the same account and AWS Region as your S3 Access Grants instance. If you have an IAM Identity Center instance configured in a different AWS Region, you can also [replicate](../../../singlesignon/latest/userguide/replicate-to-additional-region.md "../../../singlesignon/latest/userguide/replicate-to-additional-region.md") this instance to the same AWS Region as your S3 Access Grants instance. Such a configuration
is more common for proof-of-concept or local development use cases. In all cases, the IAM Identity Center
instance must be in the same AWS Region as the S3 Access Grants instance to which it will be
associated.

In the following diagram of an IAM Identity Center configuration with an external IdP, the IdP is
configured with SCIM to synchronize the identity store from the IdP to the identity store in
IAM Identity Center.

![IAM Identity Center integration with an external identity store through automatic provisioning.](images/s3ag-identity-store.png)
To use your corporate directory identities with S3 Access Grants, do the following:

- Set up [Automatic
  provisioning](../../../singlesignon/latest/userguide/provision-automatically.md "../../../singlesignon/latest/userguide/provision-automatically.md") in IAM Identity Center to synchronize user and group information from
  your IdP into IAM Identity Center.
- Configure your external identity source within IAM Identity Center as a trusted token issuer.
  For more information, see [Trusted
  identity propagation across applications](../../../singlesignon/latest/userguide/trustedidentitypropagation.md "../../../singlesignon/latest/userguide/trustedidentitypropagation.md") in the _AWS IAM Identity Center User Guide_.
- Associate your S3 Access Grants instance with your IAM Identity Center instance. You can do this when you
  [create your S3 Access Grants
  instance](access-grants-instance.md "access-grants-instance.md"). If you've already created your S3 Access Grants instance, see [Associate or disassociate your IAM Identity Center instance](access-grants-instance-idc.md "access-grants-instance-idc.md").

## How directory identities can access S3 data

Suppose that you have corporate directory users who need to access your S3 data
through a corporate application, for example, a document-viewer application, that is
integrated with your external IdP (for example, Okta) to authenticate
users. Authentication of the user in these applications is typically done through
redirects in the user's web browser. Because users in the directory are not IAM
principals, your application needs IAM credentials with which it can call the S3 Access Grants
`GetDataAccess` API operation to [get access
credentials to S3 data](access-grants-credentials.md "access-grants-credentials.md") on the users' behalf. Unlike IAM users and roles
who get credentials themselves, your application needs a way to represent a directory
user, who isn't mapped to an IAM role, so that the user can get data access through
S3 Access Grants.

This transition, from authenticated directory user to an IAM caller that can make
requests to S3 Access Grants on behalf of the directory user, is done by the application through
the trusted token issuer feature of IAM Identity Center. The application, after authenticating the
directory user, has an identity token from the IdP (for example, Okta)
that represents the directory user according to Okta. The trusted token
issuer configuration in IAM Identity Center enables the application to exchange this
Okta token (the Okta tenant is configured as the
"trusted issuer") for a different identity token from IAM Identity Center that will securely represent
the directory user within AWS services. The data application will then assume an IAM
role, providing the directory user's token from IAM Identity Center as additional context. The
application can use the resulting IAM session to call S3 Access Grants. The token represents
both the identity of the application (the IAM principal itself) as well as the
directory user's identity.

The main step of this transition is the token exchange. The application performs this
token exchange by calling the `CreateTokenWithIAM` API operation in IAM Identity Center. Of
course, that too is an AWS API call and requires an IAM principal to sign it. The
IAM principal that makes this request is typically an IAM role that's associated
with the application. For example, if the application runs on Amazon EC2, the
`CreateTokenWithIAM` request is typically performed by the IAM role
that's associated with the EC2 instance on which the application runs. The result of a
successful `CreateTokenWithIAM` call is a new identity token, which will be
recognized within AWS services.

The next step, before the application can call `GetDataAccess` on the
directory user's behalf, is for the application to obtain an IAM session that includes
the directory user's identity. The application does this with an AWS Security Token Service (AWS STS)
`AssumeRole` request that also includes the IAM Identity Center token for the directory
user as additional identity context. This additional context is what enables IAM Identity Center to
propagate the directory user's identity to the next step. The IAM role that the
application assumes is the role that will need IAM permissions to call the
`GetDataAccess` operation.

Having assumed the identity bearer IAM role with the IAM Identity Center token for the directory
user as additional context, the application now has everything it needs to make a signed
request to `GetDataAccess` on behalf of the authenticated directory
user.

Token propagation is based on the following steps:

**Create an IAM Identity Center application**

First, create a new application in IAM Identity Center. This application will use a template that
allows IAM Identity Center to identify which type of application settings that you can use. The
command to create the application requires you to provide the IAM Identity Center instance Amazon
Resource Name (ARN), an application name, and the application provider ARN. The
application provider is the SAML or OAuth application provider that the application will
use to make calls to IAM Identity Center.

To use the following example command, replace the `user input
 placeholders` with your own information:

```
aws sso-admin create-application \
 --instance-arn "arn:aws:sso:::instance/ssoins-ssoins-`1234567890abcdef`" \
 --application-provider-arn "arn:aws:sso::aws:applicationProvider/`custom`" \
 --name `MyDataApplication`
```

Response:

```
{
   "ApplicationArn": "arn:aws:sso::`123456789012`:application/ssoins-ssoins-`1234567890abcdef`/apl-`abcd1234a1b2c3d`"
}
```

**Create a trusted token issuer**

Now that you have your IAM Identity Center application, the next step is to configure a trusted
token issuer that will be used to exchange your `IdToken` values from your
IdP with IAM Identity Center tokens. In this step you need to provide the following items:

- The
  identity provider issuer URL
- The trusted token issuer name
- The claim attribute path
- The identity store attribute path
- The JSON Web Key Set (JWKS) retrieval option

The claim attribute path is the identity provider attribute that will be used to map
to the identity store attribute. Normally, the claim attribute path is the email address
of the user, but you can use other attributes to perform the mapping.

Create a file called `oidc-configuration.json` with the following
information. To use this file, replace the `user input
 placeholders` with your own information.

```
{
  "OidcJwtConfiguration":
     {
      "IssuerUrl": "`https://login.microsoftonline.com/a1b2c3d4-abcd-1234-b7d5-b154440ac123/v2.0`",
      "ClaimAttributePath": "`preferred_username`",
      "IdentityStoreAttributePath": "`userName`",
      "JwksRetrievalOption": "`OPEN_ID_DISCOVERY`"
     }
}
```

To create the trusted token issuer, run the following command. To use this example
command, replace the `user input placeholders`
with your own information.

```
aws sso-admin create-trusted-token-issuer \
  --instance-arn "arn:aws:sso:::instance/ssoins-`1234567890abcdef`" \
  --name `MyEntraIDTrustedIssuer` \
  --trusted-token-issuer-type `OIDC_JWT` \
  --trusted-token-issuer-configuration file://`./oidc-configuration`.json
```

Response

```
{
  "TrustedTokenIssuerArn": "arn:aws:sso::`123456789012`:trustedTokenIssuer/ssoins-`1234567890abcdef`/tti-`43b4a822-1234-1234-1234-a1b2c3d41234`"
}
```

**Connect the IAM Identity Center application with the trusted token
issuer**

The trusted token issuer requires a few more configuration settings to work. Set the
audience that the trusted token issuer will trust. The audience is the value inside the
`IdToken` that's identified by the key and can be found in the identity
provider settings. For example:

```
1234973b-abcd-1234-abcd-345c5a9c1234
```

Create a file named `grant.json` that contains the following
content. To use this file, change the audience to match your identity provider settings
and provide the trusted token issuer ARN that was returned by the previous
command.

```
{
   "JwtBearer":
     {
       "AuthorizedTokenIssuers":
         [
           {
             "TrustedTokenIssuerArn": "arn:aws:sso::`123456789012`:trustedTokenIssuer/ssoins-`1234567890abcdef`/tti-`43b4a822-1234-1234-1234-a1b2c3d41234`",
               "AuthorizedAudiences":
                 [
                   "`1234973b-abcd-1234-abcd-345c5a9c1234`"
                 ]
            }
         ]
     }
 }
```

Run the following example command. To use this command, replace the
`user input placeholders` with your own
information.

```
aws sso-admin put-application-grant \
  --application-arn "arn:aws:sso::`123456789012`:application/ssoins-ssoins-`1234567890abcdef`/apl-`abcd1234a1b2c3d`" \
  --grant-type "urn:ietf:params:oauth:grant-type:jwt-bearer" \
  --grant file://`./grant.json` \
```

This command sets the trusted token issuer with configuration settings to trust the
audience in the `grant.json` file and link this audience with the
application created in the first step for exchanging tokens of the type
`jwt-bearer`. The string
`urn:ietf:params:oauth:grant-type:jwt-bearer` is not an arbitrary string.
It is a registered namespace in OAuth JSON Web Token (JWT) assertion profiles. You can
find more information about this namespace in [RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523 "https://datatracker.ietf.org/doc/html/rfc7523").

Next, use the following command to set up which scopes the trusted token issuer will
include when exchanging `IdToken` values from your identity provider. For
S3 Access Grants, the value for the `--scope` parameter is
`s3:access_grants:read_write`.

```
aws sso-admin put-application-access-scope \
  --application-arn "arn:aws:sso::`111122223333`:application/ssoins-ssoins-`111122223333abcdef/apl-abcd1234a1b2c3d`" \
  --scope "s3:access_grants:read_write"
```

The last step is to attach a resource policy to the IAM Identity Center application. This policy
will allow your application IAM role to make requests to the API operation
`sso-oauth:CreateTokenWithIAM` and receive the `IdToken`
values from IAM Identity Center.

Create a file named `authentication-method.json` that contains the
following content. Replace `123456789012` with
your account ID.

```
{
   "Iam":
       {
         "ActorPolicy":
             {
                "Version": "2012-10-17"		 	 	 ,		 	 	 TCX5-2025-waiver;,
                    "Statement":
                    [
                        {
                           "Effect": "Allow",
                            "Principal":
                            {
                              "AWS": "arn:aws:iam::`123456789012`:role/webapp"
                            },
                           "Action": "sso-oauth:CreateTokenWithIAM",
                            "Resource": "*"
                        }
                    ]
                }
            }
        }
```

To attach the policy to the IAM Identity Center application, run the following command:

```
aws sso-admin put-application-authentication-method \
   --application-arn "arn:aws:sso::`123456789012`:application/ssoins-ssoins-`1234567890abcdef`/apl-`abcd1234a1b2c3d`" \
   --authentication-method-type `IAM` \
   --authentication-method file://./`authentication-method.json`
```

This completes the configuration settings for using S3 Access Grants with directory users
through a web application. You can test this setup directly in the application or you
can call the `CreateTokenWithIAM` API operation by using the following
command from an allowed IAM role in the IAM Identity Center application policy:

```
aws sso-oidc create-token-with-iam \
   --client-id "arn:aws:sso::`123456789012`:application/ssoins-ssoins-`1234567890abcdef`/apl-`abcd1234a1b2c3d`"  \
   --grant-type urn:ietf:params:oauth:grant-type:jwt-bearer \
   --assertion `IdToken`
```

The response will be similar to this:

```
{
    "accessToken": "<suppressed long string to reduce space>",
    "tokenType": "Bearer",
    "expiresIn": 3600,
    "refreshToken": "<suppressed long string to reduce space>",
    "idToken": "<suppressed long string to reduce space>",
    "issuedTokenType": "urn:ietf:params:oauth:token-type:refresh_token",
    "scope": [
      "sts:identity_context",
      "s3:access_grants:read_write",
      "openid",
      "aws"
    ]
}
```

If you decode the `IdToken` value that is encoded with base64, you can see
the key-value pairs in JSON format. The key `sts:identity_context` contains
the value that your application needs to send in the `sts:AssumeRole` request
to include the identity information of the directory user. Here is an example of the
`IdToken` decoded:

```
{
    "aws:identity_store_id": "d-996773e796",
    "sts:identity_context": "AQoJb3JpZ2luX2VjEOTtl;<SUPRESSED>",
    "sub": "83d43802-00b1-7054-db02-f1d683aacba5",
    "aws:instance_account": "123456789012",
    "iss": "https://identitycenter.amazonaws.com/ssoins-1234567890abcdef",
    "sts:audit_context": "AQoJb3JpZ2luX2VjEOT<SUPRESSED>==",
    "aws:identity_store_arn": "arn:aws:identitystore::232642235904:identitystore/d-996773e796",
    "aud": "abcd12344U0gi7n4Yyp0-WV1LWNlbnRyYWwtMQ",
    "aws:instance_arn": "arn:aws:sso:::instance/ssoins-6987d7fb04cf7a51",
    "aws:credential_id": "EXAMPLEHI5glPh40y9TpApJn8...",
    "act": {
       "sub": "arn:aws:sso::232642235904:trustedTokenIssuer/ssoins-6987d7fb04cf7a51/43b4a822-1020-7053-3631-cb2d3e28d10e"
    },
    "auth_time": "2023-11-01T20:24:28Z",
    "exp": 1698873868,
    "iat": 1698870268
}
```

You can get the value from `sts:identity_context` and pass this information
in an `sts:AssumeRole` call. The following is a CLI example of the syntax.
The role to be assumed is a temporary role with permissions to invoke
`s3:GetDataAccess`.

```
aws sts assume-role \
   --role-arn "arn:aws:iam::`123456789012`:role/`temp-role`" \
   --role-session-name "`TempDirectoryUserRole`" \
   --provided-contexts ProviderArn="arn:aws:iam::aws:contextProvider/IdentityCenter",ContextAssertion="`value from sts:identity_context`"
```

You can now use the credentials received from this call to invoke the
`s3:GetDataAccess` API operation and receive the final credentials with
access to your S3 resources.
