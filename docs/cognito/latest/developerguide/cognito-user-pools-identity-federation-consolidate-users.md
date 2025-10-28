# Linking

federated users to an existing user profile

Often, the same user has a profile with multiple identity providers (IdPs) that you
have connected to your user pool. Amazon Cognito can link each occurrence of a user to the same
user profile in your directory. This way, one person who has multiple IdP users can have
a consistent experience in your app. [AdminLinkProviderForUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.md") tells Amazon Cognito to recognize a user's unique ID in
your federated directory as a user in the user pool. A user in your user pool counts as
one monthly active user (MAU) for the purposes of [billing](https://aws.amazon.com/cognito/pricing/ "https://aws.amazon.com/cognito/pricing/") when you have zero or more federated
identities associated with the user profile.

When a federated user signs in to your user pool for the first time, Amazon Cognito looks for a
local profile that you have linked to their identity. If no linked profile exists, your
user pool creates a new profile. You can create a local profile and link it to your
federated user at any time before their first sign-in, in an
`AdminLinkProviderForUser` API request, either in a planned prestaging
task or in a [Pre sign-up Lambda trigger](user-pool-lambda-pre-sign-up.md "user-pool-lambda-pre-sign-up.md"). After your user signs in and Amazon Cognito detects
a linked local profile, your user pool reads your user's claims and compares them to
mapping rules for the IdP. Your user pool then updates the linked local profile with the
claims mapped from their sign-in. In this way, you can configure the local profile with
access claims and keep their identity claims up-to-date with your provider. After Amazon Cognito
matches your federated user to a linked profile, they always sign in to that profile.
You can then link more of your user's provider identities to the same profile, giving
one customer a consistent experience in your app. To link a federated user who has
previously signed in, you must first delete their existing profile. You can identify
existing profiles by their format: ``[Provider
 name]`\_identifier`. For example,
 `LoginWithAmazon_amzn1.account.AFAEXAMPLE`. A user that you created and
 then linked to a third-party user identity has the username that they were created with,
 and an `identities` attribute that contains the details of their linked
identities.

###### Important

Because `AdminLinkProviderForUser` allows a user with an external
federated identity to sign in as an existing user in the user pool, it is critical
that it only be used with external IdPs and provider attributes that have been
trusted by the application owner.

For example, if you're a managed service provider (MSP) with an app that you share
with multiple customers. Each of the customers signs in to your app through Active
Directory Federation Services (ADFS). Your IT administrator, Carlos, has an account in
each of your customers' domains. You want Carlos to be recognized as an app
administrator every time he signs in, regardless of the IdP.

Your ADFS IdPs present Carlos' email address `msp_carlos@example.com` in
the `email` claim of the Carlos' SAML assertions to Amazon Cognito. You create a user
in your user pool with the user name `Carlos`. The following AWS Command Line Interface
(AWS CLI) commands link Carlos' identities from IdPs ADFS1, ADFS2, and ADFS3.

###### Note

You can link a user based on specific attribute claims. This ability is unique to
OIDC and SAML IdPs. For other provider types, you must link based on a fixed source
attribute. For more information, see [AdminLinkProviderForUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.md"). You must set
`ProviderAttributeName` to `Cognito_Subject` when you link
a social IdP to a user profile. `ProviderAttributeValue` must be the
user's unique identifier with your IdP.

```
aws cognito-idp admin-link-provider-for-user \
--user-pool-id us-east-1_EXAMPLE \
--destination-user ProviderAttributeValue=Carlos,ProviderName=Cognito \
--source-user ProviderName=**ADFS1**,ProviderAttributeName=email,ProviderAttributeValue=msp_carlos@example.com

aws cognito-idp admin-link-provider-for-user \
--user-pool-id us-east-1_EXAMPLE \
--destination-user ProviderAttributeValue=Carlos,ProviderName=Cognito \
--source-user ProviderName=**ADFS2**,ProviderAttributeName=email,ProviderAttributeValue=msp_carlos@example.com

aws cognito-idp admin-link-provider-for-user \
--user-pool-id us-east-1_EXAMPLE \
--destination-user ProviderAttributeValue=Carlos,ProviderName=Cognito \
--source-user ProviderName=**ADFS3**,ProviderAttributeName=email,ProviderAttributeValue=msp_carlos@example.com
```

The user profile `Carlos` in your user pool now has the following
`identities` attribute.

```
[{
    "userId": "msp_carlos@example.com",
    "providerName": "ADFS1",
    "providerType": "SAML",
    "issuer": "http://auth.example.com",
    "primary": false,
    "dateCreated": 111111111111111
}, {
    "userId": "msp_carlos@example.com",
    "providerName": "ADFS2",
    "providerType": "SAML",
    "issuer": "http://auth2.example.com",
    "primary": false,
    "dateCreated": 111111111111111
}, {
    "userId": "msp_carlos@example.com",
    "providerName": "ADFS3",
    "providerType": "SAML",
    "issuer": "http://auth3.example.com",
    "primary": false,
    "dateCreated": 111111111111111
}]
```

###### Things to know about linking federated users

- You can link up to five federated users to each user profile.
- You can link users to each IdP from up to five IdP attribute claims, as
  defined by the `ProviderAttributeName` parameter of
  `SourceUser` in an `AdminLinkProviderForUser` API
  request. For example, if you have linked at least one user to the source
  attributes `email`, `phone`, `department`,
  `given_name`, and `location`, you can only link
  additional users on one of those five attributes.
- You can link federated users to either an existing federated user profile, or
  to a local user.
- You can't link providers to user profiles in the AWS Management Console.
- Your user's ID token contains all of their associated providers in the
  `identities` claim.
- You can set a password for the automatically-created federated user profile in
  an [AdminSetUserPassword](../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminSetUserPassword.md") API request. That user's status then changes
  from `EXTERNAL_PROVIDER` to `CONFIRMED`. A user in this
  state can sign in as a federated user, and initiate authentication flows in the
  API like a linked local user. They can also modify their password and attributes
  in token-authenticated API requests like [ChangePassword](../../../cognito-user-identity-pools/latest/APIReference/API_ChangePassword.md "../../../cognito-user-identity-pools/latest/APIReference/API_ChangePassword.md") and [UpdateUserAttributes](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserAttributes.md"). As a best security practice and to keep users
  in sync with your external IdP, don't set passwords on federated user profiles.
  Instead, link users to local profiles with
  `AdminLinkProviderForUser`.
- Amazon Cognito populates user attributes to a linked local user profile when the user
  signs in through their IdP. Amazon Cognito processes identity claims in the ID token from
  an OIDC IdP, and also checks the `userInfo` endpoint of both OAuth
  2.0 and OIDC providers. Amazon Cognito prioritizes information in an ID token over
  information from `userInfo`.
  When you learn that your user is no longer using an external user account that you've
  linked to their profile, you can disassociate that user account with your user pool
  user. When you linked your user, you supplied the user's attribute name, attribute value
  and provider name in the request. To remove a profile that your user no longer needs,
  make an [AdminDisableProviderForUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminDisableProviderForUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminDisableProviderForUser.md") API request with equivalent parameters.

See [AdminLinkProviderForUser](../../../cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminLinkProviderForUser.md") for additional command syntax and examples in the
AWS SDKs.
