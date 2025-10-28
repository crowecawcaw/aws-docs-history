# Setting up a SAML provider as an identity pool

IdP

With Amazon Cognito identity pools, you can authenticate users with identity providers (IdPs)
through SAML 2.0. You can use an IdP that supports SAML with Amazon Cognito to provide a simple
onboarding flow for your users. Your SAML-supporting IdP specifies the IAM roles that your
users can assume. This way, different users can receive different sets of permissions.

## Configuring your identity pool for a

SAML IdP

The following steps describe how to configure your identity pool to use a SAML-based
IdP.

###### Note

Before you configure your identity pool to support a SAML provider, first configure
the SAML IdP in the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam"). For more
information, see [Integrating third-party SAML solution providers with AWS](../../../IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.md "../../../IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.md") in the
_IAM User Guide_.

###### To add a SAML identity provider (IdP)

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). Select an identity
   pool.
2. Choose the **User access** tab.
3. Select **Add identity provider**.
4. Choose **SAML**.
5. Choose a **SAML identity provider** from the IAM IdPs in your
   AWS account. If you want to add a new SAML provider, choose **Create new
   provider** to navigate to the IAM console.
6. To set the role that Amazon Cognito requests when it issues credentials to users who have
   authenticated with this provider, configure **Role settings**.
   1. You can assign users from that IdP the **Default role** that
      you set up when you configured your **Authenticated role**, or you
      can **Choose role with rules**.
      1. If you chose **Choose role with rules**, enter the source
         **Claim** from your user's authentication, the
         **Operator** that you want to compare the claim by, the
         **Value** that will cause a match to this role choice, and
         the **Role** that you want to assign when the **Role
         assignment** matches. Select **Add another** to
         create an additional rule based on a different condition.
      2. Choose a **Role resolution**. When your user's claims don't
         match your rules, you can deny credentials or issue credentials for your
         **Authenticated role**.

7. To change the principal tags that Amazon Cognito assigns when it issues credentials to users
   who have authenticated with this provider, configure **Attributes for access
   control**.
   1. To apply no principal tags, choose **Inactive**.
   2. To apply principal tags based on `sub` and `aud` claims,
      choose **Use default mappings**.
   3. To create your own custom schema of attributes to principal tags, choose
      **Use custom mappings**. Then enter a **Tag
      key** that you want to source from each **Claim** that
      you want to represent in a tag.

8. Select **Save changes**.

## Configuring your SAML IdP

After you create the SAML provider, configure your SAML IdP to add relying party trust
between your IdP and AWS. With many IdPs, you can specify a URL that the IdP can use to
read relying party information and certificates from an XML document. For AWS, you can use
[https://signin.aws.amazon.com/static/saml-metadata.xml](https://signin.aws.amazon.com/static/saml-metadata.xml "https://signin.aws.amazon.com/static/saml-metadata.xml"). The next step is to
configure the SAML assertion response from your IdP to populate the claims that AWS needs.
For details on the claim configuration, see [Configuring SAML
assertions for authentication response](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md").

When your SAML IdP includes more than one signing certificate in SAML metadata, at
sign-in your identity pool determines that the SAML assertion is valid if it matches any
certificate in the SAML metadata.

## Customizing your user role with SAML

When you use SAML with Amazon Cognito Identity, you can customize the role for the end user. Amazon Cognito only
supports the [enhanced flow](authentication-flow.md "authentication-flow.md") with the SAML-based
IdP. You don't need to specify an authenticated or unauthenticated role for the identity
pool to use a SAML-based IdP. The `https://aws.amazon.com/SAML/Attributes/Role`
claim attribute specifies one or more pairs of comma -delimited role and provider ARN. These
are the roles that the user can assume. You can configure the SAML IdP to populate the role
attributes based on the user attribute information available from the IdP. If you receive
multiple roles in the SAML assertion, populate the optional `customRoleArn`
parameter when you call `getCredentialsForIdentity`. The user assumes this
`customRoleArn` if the role matches one in the claim in the SAML
assertion.

## Authenticating users with a SAML IdP

To federate with the SAML-based IdP, determine the URL where the user initiates the
login. AWS federation uses IdP-initiated login. In AD FS 2.0, the URL takes the form of
`https://`<fqdn>`/adfs/ls/IdpInitiatedSignOn.aspx?loginToRp=urn:amazon:webservices`.

To add support for your SAML IdP in Amazon Cognito, first authenticate users with your SAML
identity provider from your iOS or Android application. The code that you use to integrate
and authenticate with the SAML IdP is specific to SAML providers. After you authenticate
your user, you can use Amazon Cognito APIs to provide the resulting SAML assertion to Amazon Cognito Identity
.

You can't repeat, or _replay_, a SAML assertion in the
`Logins` map of your identity pool API request. A replayed SAML assertion has
an assertion ID that duplicates the ID of an earlier API request. API operations that can
accept a SAML assertion in the `Logins` map include [GetId](../../../cognitoidentity/latest/APIReference/API_GetId.md "../../../cognitoidentity/latest/APIReference/API_GetId.md"), [GetCredentialsForIdentity](../../../cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.md "../../../cognitoidentity/latest/APIReference/API_GetCredentialsForIdentity.md"), [GetOpenIdToken](../../../cognitoidentity/latest/APIReference/API_GetOpenIdToken.md "../../../cognitoidentity/latest/APIReference/API_GetOpenIdToken.md"),
and [GetOpenIDTokenForDeveloperIdentity](../../../cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.md "../../../cognitoidentity/latest/APIReference/API_GetOpenIdTokenForDeveloperIdentity.md"). You can replay a SAML assertion ID one time
per API request in an identity pool authentication flow. For example, you can supply the
same SAML assertion in a `GetId` request and a subsequent
`GetCredentialsForIdentity` request, but not in a second `GetId`
request.
