# Rotate an access token

An IAM Identity Center directory supports up to two access tokens at a time. To generate an
 additional access token prior to any rotation, delete any expired or unused access
 tokens.

If your SCIM access token is close to expiring, you can use the following procedure to
 rotate an existing access token in the IAM Identity Center console.

###### To rotate an access token

1. In the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon"), choose **Settings** in the left
 navigation pane.
2. On the **Settings** page, choose the **Identity
 source** tab, and then choose **Actions > Manage
 provisioning**.
3. On the **Automatic provisioning** page, under **Access
 tokens**, make a note of the token ID of the token you want to
 rotate.
4. Follow the steps in [Generate an access token](generate-token.md "generate-token.md") to create a new token. If you have already created the maximum number of SCIM
 access tokens, you will first need to delete one of the existing tokens.
5. Go to your identity provider's website and configure the new access token for SCIM
 provisioning, and then test connectivity to IAM Identity Center using the new SCIM access token.
 Once you've confirmed that provisioning is working successfully using the new token,
 continue to the next step in this procedure.
6. Follow the steps in [Delete an access token](delete-token.md "delete-token.md") to
 delete the old access token you noted earlier. You can also use the token’s creation
 date as a hint for which token to remove.
