

# Control and manage access to HTTP APIs in API Gateway
<a name="http-api-access-control"></a>

API Gateway supports multiple mechanisms for controlling and managing access to your HTTP API:
+ **Lambda authorizers** use Lambda functions to control access to APIs. For more information, see [Control access to HTTP APIs with AWS Lambda authorizers](http-api-lambda-authorizer.md).
+ **JWT authorizers** use JSON web tokens to control access to APIs. For more information, see [Control access to HTTP APIs with JWT authorizers in API Gateway](http-api-jwt-authorizer.md).
+ **Standard AWS IAM roles and policies** offer flexible and robust access controls. You can use IAM roles and policies to control who can create and manage your APIs, as well as who can invoke them. For more information, see [Control access to HTTP APIs with IAM authorization in API Gateway](http-api-access-control-iam.md).

To improve your security posture, we recommend that you configure an authorizer for all routes on your HTTP API. You might need to do this to comply with various compliance frameworks. For more information, see [Amazon API Gateway controls](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html) in the *AWS Security Hub User Guide*.