# Editing Amazon Verified Permissions Amazon Cognito identity sources

You can edit some parameters of your identity source after you create it. You can't change
the type of identity source, you have to delete the identity source and create a new one to
switch from Amazon Cognito to OIDC or OIDC to Amazon Cognito. If your policy store schema matches your identity source
attributes, note that you must update your schema separately to reflect the changes that you
make to your identity source.

AWS Management Console

###### To update an Amazon Cognito identity source

1. Open the [Verified Permissions console](https://console.aws.amazon.com/verifiedpermissions/ "https://console.aws.amazon.com/verifiedpermissions/"). Choose your policy store.
2. In the navigation pane on the left, choose **Identity
   sources**.
3. Choose the ID of the identity source to edit.
4. Choose **Edit**.
5. In **Cognito user pool details**, select the
   AWS Region and type the **User pool ID** for your
   identity source.
6. In **Principal details**, you can update the
   **Principal type** for the identity source.
   Identities from the connected Amazon Cognito user pools will be mapped to the selected
   principal type.
7. In **Group configuration**, select **Use
   Cognito groups** if you want to map the user pool
   `cognito:groups` claim. Choose an entity type that is
   a parent of the principal type.
8. In **Client application validation**, choose
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

9. Choose **Save changes**.
10. If you changed the principal type for the identity source, you
    must update your schema to correctly reflect the updated principal
    type.

You can delete an identity source by choosing the radio button next to an
identity source and then choosing **Delete identity
source**. Type `delete` in the text box and then
choose **Delete identity source** to confirm deleting the
identity source.

AWS CLI

###### To update an Amazon Cognito identity source

You can update an identity source by using the [UpdateIdentitySource](../apireference/API_UpdateIdentitySource.md "../apireference/API_UpdateIdentitySource.md") operation. The following example
updates the specified identity source to use a different Amazon Cognito user
pool.

1. Create a `config.txt` file that contains the following details of the
   Amazon Cognito user pool for use by the `--configuration` parameter in the
   `update-identity-source` command.

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

2. Run the following command to update an Amazon Cognito identity source.

```
`$` `aws verifiedpermissions update-identity-source \
 --update-configuration file://config.txt \
 --policy-store-id 123456789012``{
 "createdDate": "2023-05-19T20:30:28.214829+00:00",
 "identitySourceId": "ISEXAMPLEabcdefg111111",
 "lastUpdatedDate": "2023-05-19T20:30:28.214829+00:00",
 "policyStoreId": "PSEXAMPLEabcdefg111111"
}`
```

###### Note

If you change the principal type for the identity source, you must update
your schema to correctly reflect the updated principal type.
