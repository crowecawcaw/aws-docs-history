

# Editing Amazon Verified Permissions OIDC identity sources
<a name="oidc-edit"></a>

You can edit some parameters of your identity source after you create it. You can't change the type of identity source, you have to delete the identity source and create a new one to switch from Amazon Cognito to OIDC or OIDC to Amazon Cognito. If your policy store schema matches your identity source attributes, note that you must update your schema separately to reflect the changes that you make to your identity source.

------
#### [ AWS Management Console ]

**To update an OIDC identity source**

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/). Choose your policy store.

1. In the navigation pane on the left, choose **Identity sources**.

1. Choose the ID of the identity source to edit.

1. Choose **Edit**.

1. In **OIDC provider details**, change the **Issuer URL** as needed.

1. In **Map token claims to schema attributes**, change the associations between user and group claims and policy store entity types, as needed. After you change entity types, you must update your policies and schema attributes to apply to the new entity types.

1. In **Audience validation**, add or remove audience values that you want to enforce.

1. Choose **Save changes**.

You can delete an identity source by choosing the radio button next to an identity source and then choosing **Delete identity source**. Type `delete` in the text box and then choose **Delete identity source** to confirm deleting the identity source.

------
#### [ AWS CLI ]

**To update an OIDC identity source**  
You can update an identity source by using the [UpdateIdentitySource](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateIdentitySource.html) operation. The following example updates the specified identity source to use a different OIDC provider.

1. Create a `config.txt` file that contains the following details of an OIDC IdP for use by the `--configuration` parameter of the `update-identity-source` command.

   ```
   {
       "openIdConnectConfiguration": {
           "issuer": "https://auth2.example.com",
           "tokenSelection": {
                   "identityTokenOnly": {
                           "clientIds":["2example10111213"],
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

1. Run the following command to update an OIDC identity source.

   ```
   $ aws verifiedpermissions update-identity-source \
       --update-configuration file://config.txt \
       --policy-store-id 123456789012
   {
       "createdDate": "2023-05-19T20:30:28.214829+00:00",
       "identitySourceId": "ISEXAMPLEabcdefg111111",
       "lastUpdatedDate": "2023-05-19T20:30:28.214829+00:00",
       "policyStoreId": "PSEXAMPLEabcdefg111111"
   }
   ```

**Note**  
If you change the principal type for the identity source, you must update your schema to correctly reflect the updated principal type.

------