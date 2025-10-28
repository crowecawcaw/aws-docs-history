# Authorizing AWS IoT to invoke your Lambda

function

In this section, you'll grant the permission of the custom authorizer resource
that you just created to run the Lambda function. To grant the permission, you
can use the [add-permission](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md") CLI command.

###### Grant permission to your Lambda function using the AWS CLI

1. After inserting your values, enter the following command. Note that
   the `statement-id` value must be unique. Replace
   `Id-1234` with the exact
   value you have, otherwise, you might get a
   `ResourceConflictException` error.

```
aws lambda add-permission  \
--function-name "custom-auth-function" \
--principal "iot.amazonaws.com" \
--action "lambda:InvokeFunction" \
--statement-id "`Id-1234`" \
--source-arn `authorizerArn`
```

2. If the command succeeds, it returns a permission statement, such as this
   example. You can continue to the next section to test the custom
   authorizer.

```
{
    "Statement": "{\"Sid\":\"`Id-1234`\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"iot.amazonaws.com\"},\"Action\":\"lambda:InvokeFunction\",\"Resource\":\"arn:aws:lambda:`Region`:57EXAMPLE833:function:custom-auth-function\",\"Condition\":{\"ArnLike\":{\"AWS:SourceArn\":\"arn:aws:lambda:`Region`:57EXAMPLE833:function:custom-auth-function\"}}}"
}
```

If the command doesn't succeed, it returns an error, such as this example.
You'll need to review and correct the error before you continue.

```
An error occurred (AccessDeniedException) when calling the AddPermission operation: User: arn:aws:iam::57EXAMPLE833:user/EXAMPLE-1 is not authorized to perform: lambda:AddPer
mission on resource: arn:aws:lambda:`Region`:57EXAMPLE833:function:custom-auth-function
```
