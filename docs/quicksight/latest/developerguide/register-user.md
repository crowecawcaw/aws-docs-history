# RegisterUser

Use the `RegisterUser` operation to create an Quick Sight user whose identity is
associated with the IAM identity or role specified in the request. When you register a new
user from the Amazon Quick Sight API, Amazon Quick Sight generates a registration URL. The user accesses this
registration URL to create their account. Amazon Quick Sight does not send a registration email to users
who are registered from the Amazon Quick Sight API.

Following is an example AWS CLI command for this operation.

AWS CLI

```
aws quicksight register-user
    --identity-type `QUICKSIGHT`
    --email `EMAIL`
    --user-role `AUTHOR`
    --iam-arn `222233334444`
    --session-name `SESSION`
    --aws-account-id `AWSACCOUNTID`
    --namespace `default`
    --user-name `USERNAME`
    --external-login-federation-provider-type `CUSTOM_OIDC`
    --custom-federation-provider-url `www.example.com/`
    --external-login-id `EXTERNALLOGINID`
```

You can also make this command using a CLI skeleton file with the following command. For more information about CLI skeleton files, see [Use CLI skeleton files](cli-skeletons.md "cli-skeletons.md").

```
aws quicksight register-user
    --cli-input-json file://`registeruser`.json
```

After using this operation, you get a response that includes a link labeled
**Invitation URL**. Click the **Invitation URL**
to set up a password and activate the new account. The new user then appear in the
Quick Sight UI. You can use the `ListUsers` operation to list all users and
their corresponding user IDs.

For more information about `RegisterUser` operation, see [RegisterUser](../APIReference/API_RegisterUser.md "../APIReference/API_RegisterUser.md")in the _Quick Sight API Reference_.
