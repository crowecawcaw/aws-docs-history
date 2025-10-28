# Testing your authorizers

You can use the [TestInvokeAuthorizer](../apireference/API_TestInvokeAuthorizer.md "../apireference/API_TestInvokeAuthorizer.md") API to test the invocation and return values
of your authorizer. This API enables you to specify protocol metadata and test
the signature validation in your authorizer.

The following tabs show how to use the AWS CLI to test your authorizer.

Unix-like

```
`aws iot test-invoke-authorizer --authorizer-name `NAME_OF_AUTHORIZER` \
--token `TOKEN_VALUE` --token-signature `TOKEN_SIGNATURE``
```

Windows CMD

```
`aws iot test-invoke-authorizer --authorizer-name `NAME_OF_AUTHORIZER` ^
--token `TOKEN_VALUE` --token-signature `TOKEN_SIGNATURE``
```

Windows PowerShell

```
`aws iot test-invoke-authorizer --authorizer-name `NAME_OF_AUTHORIZER` `
--token `TOKEN_VALUE` --token-signature `TOKEN_SIGNATURE``
```

The value of the `token-signature` parameter is the signed token.
To learn how to obtain this value, see [Signing the token](custom-auth.md#custom-auth-token-signature "custom-auth.md#custom-auth-token-signature").

If your authorizer takes a user name and password, you can pass this
information by using the `--mqtt-context` parameter. The following
tabs show how to use the `TestInvokeAuthorizer` API to send a JSON
object that contains a user name, password, and client name to your custom
authorizer.

Unix-like

```
`aws iot test-invoke-authorizer --authorizer-name `NAME_OF_AUTHORIZER` \
--mqtt-context '{"username": "`USER_NAME`", "password": "dGVzdA==", "clientId":"`CLIENT_NAME`"}'`
```

Windows CMD

```
`aws iot test-invoke-authorizer --authorizer-name `NAME_OF_AUTHORIZER` ^
--mqtt-context '{"username": "`USER_NAME`", "password": "dGVzdA==", "clientId":"`CLIENT_NAME`"}'`

```

Windows PowerShell

```
`aws iot test-invoke-authorizer --authorizer-name `NAME_OF_AUTHORIZER` `
--mqtt-context '{"username": "`USER_NAME`", "password": "dGVzdA==", "clientId":"`CLIENT_NAME`"}'`
```

The password must be base64-encoded. The following example shows how to encode
a password in a Unix-like environment.

```
`echo -n `PASSWORD` | base64`
```
