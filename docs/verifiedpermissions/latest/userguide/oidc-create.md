# Creating Amazon Verified Permissions OIDC identity sources

The following procedure adds an identity source to an existing policy store.

You can also create an identity source when you [create a new policy store](policy-stores-create.md "policy-stores-create.md") in the Verified Permissions console. In this process, you can automatically
import the claims in your identity source tokens into entity attributes. Choose the
**Guided setup** or **Set up with API Gateway and an identity
provider** option. These options also create initial policies.

###### Note

**Identity sources** is not available in the navigation pane on the
left until you have created a policy store. Identity sources that you create are associated with
the current policy store.

You can leave out the principal entity type when you create an identity source with [create-identity-source](../../../cli/latest/reference/verifiedpermissions/create-identity-source.md "../../../cli/latest/reference/verifiedpermissions/create-identity-source.md") in the AWS CLI or [CreateIdentitySource](../apireference/API_CreateIdentitySource.md "../apireference/API_CreateIdentitySource.md") in the Verified Permissions API. However, a blank entity type creates an
identity source with an entity type of `AWS::Cognito`. This entity name isn't
compatible with policy store schema. To integrate Amazon Cognito identities with your policy store
schema, you must set the principal entity type to a supported policy store entity.

AWS Management Console

###### To create an OpenID Connect (OIDC) identity source

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose **Identity
   sources**.
3. Choose **Create identity source**.
4. Choose **External OIDC provider**.
5. In **Issuer URL**, enter the URL of your OIDC
   issuer. This is the service endpoint that provides the authorization
   server, signing keys, and other information about your provider, for
   example `https://auth.example.com`. Your issuer URL must
   host an OIDC discovery document at
   `/.well-known/openid-configuration`.
6. In **Token type**, choose the type of OIDC JWT
   that you want your application to submit for authorization. For more
   information, see [Mapping OIDC tokens to
   schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").
7. In **Map token claims to schema entities**,
   choose a **User entity** and **User
   claim** for the identity source. The **User
   entity** is an entity in your policy store that you
   want to refer to users from your OIDC provider. The **User
   claim** is a claim, typically `sub`, from
   your ID or access token that holds the unique identifier for the
   entity to be evaluated. Identities from the connected OIDC IdP will
   be mapped to the selected principal type.
8. (Optional) In **Map token claims to schema
   entities**, choose a **Group entity**
   and **Group claim** for the identity source. The
   **Group entity** is a [parent](https://docs.cedarpolicy.com/overview/terminology.html#term-group "https://docs.cedarpolicy.com/overview/terminology.html#term-group") of the **User entity**. Group
   claims get mapped to this entity. The **Group
   claim** is a claim, typically `groups`, from
   your ID or access token that contains a string, JSON, or
   space-delimited string of user-group names for the entity to be
   evaluated. Identities from the connected OIDC IdP will be mapped to
   the selected principal type.
9. In **validation - optional**, enter the client
   IDs or audience URLs that you want your policy store to accept in
   authorization requests, if any.
10. Choose **Create identity source**.
11. (Optional) If your policy store has a schema, before you can reference attributes that you extract from identity or
    access tokens in your Cedar policies, you must update your schema to make
    Cedar aware of the type of principal that your identity source creates.
    That addition to the schema must include the attributes that you want to
    reference in your Cedar policies. For more
    information about mapping OIDC token attributes to Cedar principal
    attributes, see [Mapping OIDC tokens to
    schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").
12. Create policies that use information from the tokens to make authorization decisions. For more information, see
    [Creating Amazon Verified Permissions static policies](policies-create.md "policies-create.md").

Now that you've created an identity source, updated the schema, and created policies, use `IsAuthorizedWithToken` to
have Verified Permissions make authorization decisions. For more information, see [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md")
in the _Amazon Verified Permissions API reference guide_.

AWS CLI

###### To create an OIDC identity source

You can an create an identity source by using the [CreateIdentitySource](../apireference/API_CreateIdentitySource.md "../apireference/API_CreateIdentitySource.md") operation. The following example
creates an identity source that can access authenticated identities from
a an OIDC identity provider(IdP).

1. Create a `config.txt` file that contains the following details of an OIDC
   IdP for use by the `--configuration` parameter of the
   `create-identity-source` command.

```
{
    "openIdConnectConfiguration": {
        "issuer": "https://auth.example.com",
        "tokenSelection": {
                "identityTokenOnly": {
                        "clientIds":["1example23456789"],
                        "principalIdClaim": "sub"
                },
        },
        "entityIdPrefix": "MyOIDCProvider",
        "groupConfiguration": {
              "groupClaim": "groups",
              "groupEntityType": "MyCorp::UserGroup"
        }
    }
}
```

2. Run the following command to create an OIDC identity source.

```
`$` `aws verifiedpermissions create-identity-source \
 --configuration file://config.txt \
 --principal-entity-type "User" \
 --policy-store-id 123456789012``{
 "createdDate": "2023-05-19T20:30:28.214829+00:00",
 "identitySourceId": "ISEXAMPLEabcdefg111111",
 "lastUpdatedDate": "2023-05-19T20:30:28.214829+00:00",
 "policyStoreId": "PSEXAMPLEabcdefg111111"
}`
```

3. (Optional) If your policy store has a schema, before you can reference attributes that you extract from identity or
   access tokens in your Cedar policies, you must update your schema to make
   Cedar aware of the type of principal that your identity source creates.
   That addition to the schema must include the attributes that you want to
   reference in your Cedar policies. For more
   information about mapping OIDC token attributes to Cedar principal
   attributes, see [Mapping OIDC tokens to
   schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").
4. Create policies that use information from the tokens to make authorization decisions. For more information, see
   [Creating Amazon Verified Permissions static policies](policies-create.md "policies-create.md").

Now that you've created an identity source, updated the schema, and created policies, use `IsAuthorizedWithToken` to
have Verified Permissions make authorization decisions. For more information, see [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md")
in the _Amazon Verified Permissions API reference guide_.
