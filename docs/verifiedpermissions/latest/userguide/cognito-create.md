# Creating Amazon Verified Permissions Amazon Cognito identity sources

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

###### To create an Amazon Cognito user pools identity source

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose **Identity
   sources**.
3. Choose **Create identity source**.
4. In **Cognito user pool details**, select the
   AWS Region and enter the **User pool ID** for
   your identity source.
5. In **Principal configuration**, for
   **Principal type**, choose the entity type for
   principals from this source. Identities from the connected Amazon Cognito user pools
   will be mapped to the selected principal type.
6. In **Group configuration**, select **Use
   Cognito group** if you want to map the user pool
   `cognito:groups` claim. Choose an entity type that is
   a parent of the principal type.
7. In **Client application validation**, choose
   whether to validate client application IDs.
   - To validate client application IDs, choose **Only
     accept tokens with matching client application
     IDs**. Choose **Add new client
     application ID** for each client application ID
     to validate. To remove a client application ID that has been
     added, choose **Remove** next to the client
     application ID.
   - Choose **Do not validate client application
     IDs** if you do not want to validate client
     application IDs.

8. Choose **Create identity source**.
9. (Optional) If your policy store has a schema, before you can reference attributes you
   extract from identity or access tokens in your Cedar policies, you must
   update your schema to make Cedar aware of the type of principal that your
   identity source creates. That addition to the schema must include the
   attributes that you want to reference in your Cedar policies. For more
   information about mapping Amazon Cognito token attributes to Cedar principal
   attributes, see [Mapping Amazon Cognito tokens to
   schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md").

###### Note

When you create an [API-linked
policy store](policy-stores-api-userpool.md "policy-stores-api-userpool.md") or use **Set up with API Gateway and an identity
provider** when creating policy stores, Verified Permissions queries your user
pool for user attributes and creates a schema where your principal type is
populated with user pool attributes. 10. Create policies that use information from the tokens to make authorization decisions. For more information, see
[Creating Amazon Verified Permissions static policies](policies-create.md "policies-create.md").

Now that you've created an identity source, updated the schema, and created policies, use `IsAuthorizedWithToken` to
have Verified Permissions make authorization decisions. For more information, see [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md")
in the _Amazon Verified Permissions API reference guide_.

AWS CLI

###### To create an Amazon Cognito user pools identity source

You can an create an identity source by using the [CreateIdentitySource](../apireference/API_CreateIdentitySource.md "../apireference/API_CreateIdentitySource.md") operation. The following example
creates an identity source that can access authenticated identities from
a Amazon Cognito user pool.

1. Create a `config.txt` file that contains the following details of the
   Amazon Cognito user pool for use by the `--configuration` parameter in the
   `create-identity-source` command.

```
{
    "cognitoUserPoolConfiguration": {
        "userPoolArn": "arn:aws:cognito-idp:us-west-2:123456789012:userpool/us-west-2_1a2b3c4d5",
        "clientIds":["a1b2c3d4e5f6g7h8i9j0kalbmc"],
        "groupConfiguration": {
              "groupEntityType": "MyCorp::UserGroup"
        }
    }
}
```

2. Run the following command to create an Amazon Cognito identity source.

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

3. (Optional) If your policy store has a schema, before you can reference attributes you
   extract from identity or access tokens in your Cedar policies, you must
   update your schema to make Cedar aware of the type of principal that your
   identity source creates. That addition to the schema must include the
   attributes that you want to reference in your Cedar policies. For more
   information about mapping Amazon Cognito token attributes to Cedar principal
   attributes, see [Mapping Amazon Cognito tokens to
   schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md").

###### Note

When you create an [API-linked
policy store](policy-stores-api-userpool.md "policy-stores-api-userpool.md") or use **Set up with API Gateway and an identity
provider** when creating policy stores, Verified Permissions queries your user
pool for user attributes and creates a schema where your principal type is
populated with user pool attributes. 4. Create policies that use information from the tokens to make authorization decisions. For more information, see
[Creating Amazon Verified Permissions static policies](policies-create.md "policies-create.md").

Now that you've created an identity source, updated the schema, and created policies, use `IsAuthorizedWithToken` to
have Verified Permissions make authorization decisions. For more information, see [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md")
in the _Amazon Verified Permissions API reference guide_.

For more information about using Amazon Cognito access and identity tokens for
authenticated users in Verified Permissions, see [Authorization with
Amazon Verified Permissions](../../../cognito/latest/developerguide/amazon-cognito-authorization-with-avp.md "../../../cognito/latest/developerguide/amazon-cognito-authorization-with-avp.md") in the _Amazon Cognito Developer Guide_.
