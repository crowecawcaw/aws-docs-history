# Adding and managing SAML

identity providers in a user pool

After you configure your identity provider to work with Amazon Cognito, you can add it to
your user pools and app clients. The following procedures demonstrate how to create,
modify, and delete SAML providers in an Amazon Cognito user pool.

AWS Management Console
You can use the AWS Management Console to create and delete SAML identity providers
(IdPs).

Before you create a SAML IdP, you must have the SAML metadata document
that you get from the third-party IdP. For instructions on how to get or
generate the required SAML metadata document, see [Configuring your third-party SAML identity provider](cognito-user-pools-integrating-3rd-party-saml-providers.md "cognito-user-pools-integrating-3rd-party-saml-providers.md").

###### To configure a SAML 2.0 IdP in your user pool

1. Go to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home"). If prompted, enter your AWS
   credentials.
2. Choose **User Pools**.
3. Choose an existing user pool from the list, or [create a user pool](cognito-user-pool-as-user-directory.md "cognito-user-pool-as-user-directory.md").
4. Choose the **Social and external providers**
   menu and then select **Add an identity
   provider**.
5. Choose a **SAML** IdP.
6. Enter a **Provider name**. You can pass this
   friendly name in an `identity_provider` request
   parameter to the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").
7. Enter **Identifiers** separated by commas. An
   identifier tells Amazon Cognito it should check the email address a user
   enters when they sign in, and then direct them to the provider
   that corresponds to their domain.
8. Choose **Add sign-out flow** if you want
   Amazon Cognito to send signed sign-out requests to your provider when a
   user logs out. You must configure your SAML 2.0 IdP to send
   sign-out responses to the
   `https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/logout`
   endpoint that is created when you configure managed login. The
   `saml2/logout` endpoint uses POST binding.

###### Note

If this option is selected and your SAML IdP expects a
signed logout request, you must also provide your SAML IdP
with the signing certificate from your user pool.

The SAML IdP will process the signed logout request and
sign out your user from the Amazon Cognito session. 9. Choose your **IdP-initiated SAML sign-in**
configuration. As a security best practice, choose
**Accept SP-initiated SAML assertions
only**. If you have prepared your environment to
securely accept unsolicited SAML sign-in sessions, choose
**Accept SP-initiated and IdP-initiated SAML
assertions**. For more information, see [SAML session initiation
in Amazon Cognito user pools](cognito-user-pools-SAML-session-initiation.md "cognito-user-pools-SAML-session-initiation.md"). 10. Choose a **Metadata document source**. If
your IdP offers SAML metadata at a public URL, you can choose
**Metadata document URL** and enter that
public URL. Otherwise, choose **Upload metadata
document** and select a metadata file you
downloaded from your provider earlier.

###### Note

We recommend that you enter a metadata document URL if
your provider has a public endpoint instead of uploading a
file. Amazon Cognito automatically refreshes metadata from the
metadata URL. Typically, metadata refresh happens every 6
hours or before the metadata expires, whichever is
earlier. 11. **Map attributes between your SAML provider and your
user pool** to map SAML provider attributes to the
user profile in your user pool. Include your user pool required
attributes in your attribute map.

For example, when you choose **User pool
attribute**
`email`, enter the SAML attribute name as it appears
in the SAML assertion from your IdP. If your IdP offers sample
SAML assertions, you can use these sample assertions to help you
to find the name. Some IdPs use simple names, such as
`email`, while others use names like the
following.

```
`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`
```

12. Choose **Create**.

API/CLI
Use the following commands to create and manage a SAML identity
provider (IdP).

###### To create an IdP and upload a metadata document

- AWS CLI: `aws cognito-idp
create-identity-provider`

Example with metadata file: `aws cognito-idp
 create-identity-provider --user-pool-id
 `us-east-1_EXAMPLE`
 --provider-name=`SAML_provider_1`  --provider-type SAML --provider-details file:///details.json
 --attribute-mapping
 `email`=`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress``

Where `details.json` contains:

```
"ProviderDetails": {
      "MetadataFile": "`<SAML metadata XML>`",
      "IDPSignout" : "`true`",
      "RequestSigningAlgorithm" : "rsa-sha256",
      "EncryptedResponses" : "`true`",
      "IDPInit" : "`true`"
}
```

###### Note

If the `<SAML metadata
 XML>` contains any instances of the
character `"`, you must add `\` as an
escape character: `\"`.

Example with metadata URL: `aws cognito-idp
 create-identity-provider --user-pool-id
 `us-east-1_EXAMPLE`
 --provider-name=`SAML_provider_1`
 --provider-type SAML --provider-details
 MetadataURL=`https://myidp.example.com/sso/saml/metadata`
--attribute-mapping
`email`=`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress``

- AWS API: [CreateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateIdentityProvider.md")

###### To upload a new metadata document for an IdP

- AWS CLI: `aws cognito-idp
update-identity-provider`

Example with metadata file: `aws cognito-idp
 update-identity-provider --user-pool-id
 `us-east-1_EXAMPLE`
 --provider-name=`SAML_provider_1`  --provider-details file:///details.json --attribute-mapping
 `email`=`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress``

Where `details.json` contains:

```
"ProviderDetails": {
      "MetadataFile": "`<SAML metadata XML>`",
      "IDPSignout" : "`true`",
      "RequestSigningAlgorithm" : "rsa-sha256",
      "EncryptedResponses" : "`true`",
      "IDPInit" : "`true`"
}
```

###### Note

If the `<SAML metadata
 XML>` contains any instances of the
character `"`, you must add `\` as an
escape character: `\"`.

Example with metadata URL: `aws cognito-idp
 update-identity-provider --user-pool-id
 `us-east-1_EXAMPLE`
 --provider-name=`SAML_provider_1`
 --provider-details
 MetadataURL=`https://myidp.example.com/sso/saml/metadata`
--attribute-mapping
`email`=`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress``

- AWS API: [UpdateIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateIdentityProvider.md")

###### To get information about a specific IdP

- AWS CLI: `aws cognito-idp
describe-identity-provider`

`aws cognito-idp describe-identity-provider
 --user-pool-id `us-east-1_EXAMPLE`
 --provider-name=`SAML_provider_1``

- AWS API: [DescribeIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_DescribeIdentityProvider.md")

###### To list information about all IdPs

- AWS CLI: `aws cognito-idp
list-identity-providers`

Example: `aws cognito-idp list-identity-providers
 --user-pool-id `us-east-1_EXAMPLE`
 --max-results 3`

- AWS API: [ListIdentityProviders](../../../cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListIdentityProviders.md")

###### To delete an IdP

- AWS CLI: `aws cognito-idp
delete-identity-provider`

`aws cognito-idp delete-identity-provider --user-pool-id
 `us-east-1_EXAMPLE`
 --provider-name=`SAML_provider_1``

- AWS API: [DeleteIdentityProvider](../../../cognito-user-identity-pools/latest/APIReference/API_DeleteIdentityProvider.md "../../../cognito-user-identity-pools/latest/APIReference/API_DeleteIdentityProvider.md")

###### To set up the SAML IdP to add a user pool as a relying party

- The user pools service provider URN is:
  `urn:amazon:cognito:sp:`us-east-1_EXAMPLE``.
  Amazon Cognito requires an audience restriction value that matches this URN in the
  SAML response. Configure your IdP to use the following POST binding endpoint
  for the IdP-to-SP response message.

```
https://`mydomain.auth.us-east-1.amazoncognito.com`/saml2/idpresponse
```

- Your SAML IdP must populate `NameID` and any required
  attributes for your user pool in the SAML assertion. `NameID` is
  used for uniquely identifying your SAML federated user in the user pool.
  Your IdP must pass each user’s SAML name ID in a consistent, case-sensitive
  format. Any variation in the value of a user's name ID creates a new user
  profile.

###### To provide a signing certificate to your SAML 2.0 IDP

- To download a copy of the the public key from Amazon Cognito that your IdP can use
  to validate SAML logout requests, choose the **Social and external
  providers** menu of your user pool, select your IdP, and under
  **View signing certificate**, select **Download
  as .crt**.
  You can delete any SAML provider you have set up in your user pool with the Amazon Cognito
  console.

###### To delete a SAML provider

1. Sign in to the [Amazon Cognito
   console](https://console.aws.amazon.com/cognito/home "https://console.aws.amazon.com/cognito/home").
2. In the navigation pane, choose **User Pools**, and choose
   the user pool you want to edit.
3. Choose the **Social and external providers** menu.
4. Select the radio button next to the SAML IdPs you wish to delete.
5. When you are prompted to **Delete identity provider**,
   enter the name of the SAML provider to confirm deletion, and then choose
   **Delete**.
