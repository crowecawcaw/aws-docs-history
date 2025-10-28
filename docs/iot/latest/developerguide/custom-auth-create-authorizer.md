# Creating an authorizer

You can create an authorizer by using the [CreateAuthorizer
API](../apireference/API_CreateAuthorizer.md "../apireference/API_CreateAuthorizer.md"). The following example describes the command.

```
aws iot create-authorizer
--authorizer-name MyAuthorizer
--authorizer-function-arn arn:aws:lambda:us-west-2:<account_id>:function:MyAuthorizerFunction  //The ARN of the Lambda function.
[--token-key-name MyAuthorizerToken //The key used to extract the token from headers.
[--token-signing-public-keys FirstKey=
 "-----BEGIN PUBLIC KEY-----
  [...insert your public key here...]
  -----END PUBLIC KEY-----"
[--status ACTIVE]
[--tags <value>]
[--signing-disabled | --no-signing-disabled]
```

You can use the `signing-disabled` parameter to opt out of
signature validation for each invocation of your authorizer. We strongly
recommend that you do not disable signing unless you have to. Signature
validation protects you against excessive invocations of your Lambda function
from unknown devices. You can't update the `signing-disabled` status
of an authorizer after you create it. To change this behavior, you must create
another custom authorizer with a different value for the
`signing-disabled` parameter.

Values for the `tokenKeyName` and
`tokenSigningPublicKeys` parameters are optional if you have
disabled signing. They are required values if signing is enabled.

After you create your Lambda function and the custom authorizer, you must
explicitly grant the AWS IoT Core service permission to invoke the function on your
behalf. You can do this with the following command.

###### Note

The default IoT endpoint might not support using custom authorizers
with Lambda functions. Instead, you can use domain configurations to define
a new endpoint and then specify that endpoint for the custom authorizer.

```
aws lambda add-permission --function-name <lambda_function_name>
--principal iot.amazonaws.com --source-arn <authorizer_arn>
--statement-id Id-123 --action "lambda:InvokeFunction"
```
