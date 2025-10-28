# Creating and managing custom authorizers

(CLI)

AWS IoT Core implements custom authentication and authorization schemes by using
custom authorizers. A custom authorizer is an AWS IoT Core resource that gives you the
flexibility to define and implement the rules and policies based on your specific
requirements. To create a custom authorizer with step-by-step instructions, see
[Tutorial: Creating a custom authorizer for AWS IoT Core](custom-auth-tutorial.md "custom-auth-tutorial.md").

Each authorizer consists of the following components:

- _Name_: A unique user-defined string that identifies the
  authorizer.
- _Lambda function ARN_: The Amazon Resource Name (ARN) of
  the Lambda function that implements the authorization and authentication
  logic.
- _Token key name_: The key name used to extract the token
  from the HTTP headers, query parameters, or MQTT CONNECT user name in order
  to perform signature validation. This value is required if signing is
  enabled in your authorizer.
- _Signing disabled flag (optional)_: A Boolean value that
  specifies whether to disable the signing requirement on credentials. This is
  useful for scenarios where signing the credentials doesn't make sense, such
  as authentication schemes that use MQTT user name and password. The default
  value is `false`, so signing is enabled by default.
- _Token signing public key_: The public key that AWS IoT Core
  uses to validate the token signature. Its minimum length is 2,048 bits. This
  value is required if signing is enabled in your authorizer.
  Lambda charges you for the number of times your Lambda function runs and for the
  amount of time it takes for the code in your function to execute. For more
  information about Lambda pricing, see [Lambda Pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/"). For more
  information about creating Lambda functions, see the [Lambda
  Developer Guide](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md").

###### Note

If you leave signing enabled, you can prevent excessive triggering of your
Lambda by unrecognized clients. Consider this before you disable signing in your
authorizer.

###### Note

The Lambda function timeout limit for custom authorizer is 5 seconds.

###### In this chapter:

- [Defining your Lambda function](custom-auth-lambda.md "custom-auth-lambda.md")
- [Creating an authorizer](custom-auth-create-authorizer.md "custom-auth-create-authorizer.md")
- [Authorizing AWS IoT to invoke your Lambda
  function](custom-auth-authorize.md "custom-auth-authorize.md")
- [Testing your authorizers](custom-auth-testing.md "custom-auth-testing.md")
- [Managing custom authorizers](custom-auth-manage.md "custom-auth-manage.md")
