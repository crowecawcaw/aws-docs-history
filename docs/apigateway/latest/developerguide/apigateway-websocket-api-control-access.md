# Control and manage access to

WebSocket APIs in API Gateway

API Gateway supports multiple mechanisms for controlling and managing access to your
WebSocket API.

You can use the following mechanisms for authentication and authorization:

- **Standard AWS IAM roles and policies** offer
  flexible and robust access controls. You can use IAM roles and policies for
  controlling who can create and manage your APIs, as well as who can invoke them. For
  more information, see [Control access to WebSocket APIs with IAM authorization](apigateway-websocket-control-access-iam.md "apigateway-websocket-control-access-iam.md").
- **IAM tags** can be used together with IAM
  policies to control access. For more information, see [Using tags to control access to API Gateway REST API resources](apigateway-tagging-iam-policy.md "apigateway-tagging-iam-policy.md").
- **Lambda authorizers** are Lambda functions that
  control access to APIs. For more information, see [Control access to WebSocket APIs with AWS Lambda REQUEST authorizers](apigateway-websocket-api-lambda-auth.md "apigateway-websocket-api-lambda-auth.md").
  To improve your security posture, we recommend that you configure an authorizer for the `$connect`
  route on all your WebSocket APIs. You might need to do this to comply with various compliance frameworks. For more
  information, see [Amazon API Gateway
  controls](../../../securityhub/latest/userguide/apigateway-controls.md "../../../securityhub/latest/userguide/apigateway-controls.md") in the _AWS Security Hub CSPM User Guide_.

###### Topics

- [Control access to WebSocket APIs with IAM authorization](apigateway-websocket-control-access-iam.md "apigateway-websocket-control-access-iam.md")
- [Control access to WebSocket APIs with AWS Lambda REQUEST authorizers](apigateway-websocket-api-lambda-auth.md "apigateway-websocket-api-lambda-auth.md")
