

# Accessing resources with API Gateway after sign-in
<a name="user-pool-accessing-resources-api-gateway-and-lambda"></a>

A common use of Amazon Cognito user pools tokens is to authorize requests to an [API Gateway REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html). The OAuth 2.0 scopes in access tokens can authorize a method and path, like `HTTP GET` for `/app_assets`. ID tokens can serve as generic authentication to an API and can pass user attributes to the backend service. API Gateway has additional custom authorization options like [JWT authorizers for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html) and [Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) that can apply more fine-grained logic.

The following diagram illustrates an application that is gaining access to a REST API with the OAuth 2.0 scopes in an access token.

![A flow diagram of an application that authenticates with an Amazon Cognito user pool and authorizes access to API resources with Amazon API Gateway.](http://docs.aws.amazon.com/cognito/latest/developerguide/images/access-services-api-gateway.png)


Your app must collect the tokens from authenticated sessions and add them as bearer tokens to an `Authorization` header in the request. Configure the authorizer that you configured for the API, path, and method to evaluate token contents. API Gateway returns data only if the request matches the conditions that you set up for your authorizer. 

Some potential ways that API Gateway API can approve access from an application are:
+ The access token is valid, isn't expired, and contains the correct OAuth 2.0 scope. The [Amazon Cognito user pools authorizer for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) is a common implementation with a low barrier to entry. You can also evaluate the body, query string parameters, and headers of a request to this type of authorizer.
+ The ID token is valid and isn't expired. When you pass an ID token to an Amazon Cognito authorizer, you can perform additional validation of the ID token contents on your application server.
+ A group, claim, attribute, or role in an access or ID token meets the requirements that you define in a Lambda function. A [Lambda authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) parses the token in the request header and evaluates it for an authorization decision. You can construct custom logic in your function or make an API request to [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html).

You can also authorize requests to an [AWS AppSync GraphQL API](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html#amazon-cognito-user-pools-authorization) with tokens from a user pool.