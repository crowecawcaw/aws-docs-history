# x-amazon-apigateway-authorizer object

Defines a Lambda authorizer, Amazon Cognito user pool, or JWT authorizer to be applied for authorization of
method invocations in API Gateway. This extension applies to the security definition in [OpenAPI 2](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#security-definitions-object "https://github.com/OAI/OpenAPI-Specification/blob/main/versions/2.0.md#security-definitions-object") and
the security scheme in [OpenAPI 3](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#security-scheme-object "https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.1.md#security-scheme-object").

| Property name                    | Type                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`                           | `string`             | The type of the authorizer. This is a required property.<br>For REST APIs, specify `token` for an authorizer with the caller identity<br>embedded in an authorization token. Specify `request` for an authorizer with the caller<br>identity contained in request parameters. Specify `cognito_user_pools` for an authorizer that<br>uses an Amazon Cognito user pool to control access to your API.<br>For HTTP APIs, specify `request`<br>for a Lambda authorizer with the caller identity contained in request<br>parameters. Specify `jwt` for a JWT authorizer. |
| `authorizerUri`                  | `string`             | The Uniform Resource Identifier (URI) of the authorizer Lambda<br>function. The syntax is as follows:<br>``<br>"arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:`account-id`:function:`auth_function_name`/invocations"<br>``                                                                                                                                                                                                                                                                                                 |
| `authorizerCredentials`          | `string`             | The credentials required for invoking the authorizer, if any, in<br>the form of an ARN of an IAM execution role. For example,<br>"arn:aws:iam::`account-id`:`IAM_role`".                                                                                                                                                                                                                                                                                                                                                                                             |
| `authorizerPayloadFormatVersion` | `string`             | For HTTP APIs, specifies the format of the data that API Gateway sends to a Lambda authorizer, and how API Gateway interprets the response from Lambda. To learn more, see [Payload format<br>version](http-api-lambda-authorizer.md#http-api-lambda-authorizer.payload-format "http-api-lambda-authorizer.md#http-api-lambda-authorizer.payload-format").                                                                                                                                                                                                           |
| `enableSimpleResponses`          | `Boolean`            | For HTTP APIs, specifies whether a `request`<br>authorizer returns a Boolean value or an IAM policy. Supported<br>only for authorizers with an<br>`authorizerPayloadFormatVersion` of `2.0`.<br>If enabled, the Lambda authorizer function returns a Boolean value.<br>To learn more, see [Lambda function response<br>for format 2.0](http-api-lambda-authorizer.md#http-api-lambda-authorizer.v2 "http-api-lambda-authorizer.md#http-api-lambda-authorizer.v2").                                                                                                   |
| `identitySource`                 | `string`             | A comma-separated list of mapping expressions of the request<br>parameters as the identity source. Applicable for the authorizer of<br>the `request` and `jwt` type<br>only.                                                                                                                                                                                                                                                                                                                                                                                         |
| `jwtConfiguration`               | `Object`             | Specifies the issuer and audiences for a JWT authorizer. To learn<br>more, see [JWTConfiguration](../../../apigatewayv2/latest/api-reference/apis-apiid-authorizers-authorizerid.md#apis-apiid-authorizers-authorizerid-model-jwtconfiguration "../../../apigatewayv2/latest/api-reference/apis-apiid-authorizers-authorizerid.md#apis-apiid-authorizers-authorizerid-model-jwtconfiguration") in the API Gateway Version 2 API Reference. Supported only for<br>HTTP APIs.                                                                                          |
| `identityValidationExpression`   | `string`             | A regular expression for validating the token as the incoming<br>identity. For example, "^x-[a-z]+". Supported only for `TOKEN` authorizers for REST APIs.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `authorizerResultTtlInSeconds`   | `string`             | The number of seconds during which authorizer result is<br>cached.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `providerARNs`                   | An array of `string` | A list of the Amazon Cognito user pool ARNs for the `COGNITO_USER_POOLS`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## x-amazon-apigateway-authorizer examples for REST APIs

The following OpenAPI security definitions example specifies a Lambda authorizer of
the "token" type and named `test-authorizer`.

```

  "securityDefinitions" : {
    "test-authorizer" : {
      "type" : "apiKey",                         // Required and the value must be "apiKey" for an API Gateway API.
      "name" : "Authorization",                  // The name of the header containing the authorization token.
      "in" : "header",                           // Required and the value must be "header" for an API Gateway API.
      "x-amazon-apigateway-authtype" : "custom", // Specifies the authorization mechanism for the client.
      "x-amazon-apigateway-authorizer" : {       // An API Gateway Lambda authorizer definition
        "type" : "token",                        // Required property and the value must "token"
        "authorizerUri" : "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:`account-id`:function:`function-name`/invocations",
        "authorizerCredentials" : "arn:aws:iam::`account-id`:role",
        "identityValidationExpression" : "^x-[a-z]+",
        "authorizerResultTtlInSeconds" : 60
      }
    }
  }
```

The following OpenAPI operation object snippet sets the `GET /http` to
use the preceding Lambda authorizer.

```

   "/http" : {
      "get" : {
        "responses" : { },
        "security" : [ {
          "test-authorizer" : [ ]
        } ],
        "x-amazon-apigateway-integration" : {
          "type" : "http",
          "responses" : {
            "default" : {
              "statusCode" : "200"
            }
          },
          "httpMethod" : "GET",
          "uri" : "http://api.example.com"
        }
      }
    }
```

The following OpenAPI security definitions example specifies a Lambda authorizer of
the "request" type, with a single header parameter (`auth`) as the
identity source. The `securityDefinitions` is named
`request_authorizer_single_header`.

```
"securityDefinitions": {
    "request_authorizer_single_header" : {
      "type" : "apiKey",
      "name" : "auth",               // The name of a single header or query parameter as the identity source.
      "in" : "header",               // The location of the single identity source request parameter. The valid value is "header" or "query"
      "x-amazon-apigateway-authtype" : "custom",
      "x-amazon-apigateway-authorizer" : {
        "type" : "request",
        "identitySource" : "method.request.header.auth",   // Request parameter mapping expression of the identity source. In this example, it is the 'auth' header.
        "authorizerCredentials" : "arn:aws:iam::123456789012:role/AWSepIntegTest-CS-LambdaRole",
        "authorizerUri" : "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:APIGateway-Request-Authorizer:vtwo/invocations",
        "authorizerResultTtlInSeconds" : 300
      }
    }
}
```

The following OpenAPI security definitions example specifies a Lambda authorizer of
the "request" type, with one header (`HeaderAuth1`) and one query string
parameter `QueryString1` as the identity sources.

```
"securityDefinitions": {
    "request_authorizer_header_query" : {
      "type" : "apiKey",
      "name" : "Unused",             // Must be "Unused" for multiple identity sources or non header or query type of request parameters.
      "in" : "header",               // Must be "header" for multiple identity sources or non header or query type of request parameters.
      "x-amazon-apigateway-authtype" : "custom",
      "x-amazon-apigateway-authorizer" : {
        "type" : "request",
        "identitySource" : "method.request.header.HeaderAuth1, method.request.querystring.QueryString1",   // Request parameter mapping expressions of the identity sources.
        "authorizerCredentials" : "arn:aws:iam::123456789012:role/AWSepIntegTest-CS-LambdaRole",
        "authorizerUri" : "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:APIGateway-Request-Authorizer:vtwo/invocations",
        "authorizerResultTtlInSeconds" : 300
      }
    }
}
```

The following OpenAPI security definitions example specifies an API Gateway Lambda
authorizer of the "request" type, with a single stage variable (`stage`)
as the identity source.

```
"securityDefinitions": {
    "request_authorizer_single_stagevar" : {
      "type" : "apiKey",
      "name" : "Unused",             // Must be "Unused", for multiple identity sources or non header or query type of request parameters.
      "in" : "header",               // Must be "header", for multiple identity sources or non header or query type of request parameters.
      "x-amazon-apigateway-authtype" : "custom",
      "x-amazon-apigateway-authorizer" : {
        "type" : "request",
        "identitySource" : "stageVariables.stage",   // Request parameter mapping expression of the identity source. In this example, it is the `stage` variable.
        "authorizerCredentials" : "arn:aws:iam::123456789012:role/AWSepIntegTest-CS-LambdaRole",
        "authorizerUri" : "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:APIGateway-Request-Authorizer:vtwo/invocations",
        "authorizerResultTtlInSeconds" : 300
      }
    }
}
```

The following OpenAPI security definition example specifies an Amazon Cognito user pool as an authorizer.

```
 "securityDefinitions": {
    "cognito-pool": {
      "type": "apiKey",
      "name": "Authorization",
      "in": "header",
      "x-amazon-apigateway-authtype": "cognito_user_pools",
      "x-amazon-apigateway-authorizer": {
        "type": "cognito_user_pools",
        "providerARNs": [
          "arn:aws:cognito-idp:us-east-1:123456789012:userpool/us-east-1_ABC123"
        ]
      }
    }
```

The following OpenAPI operation object snippet sets the `GET /http` to
use the preceding Amazon Cognito user pool as an authorizer, with no custom scopes.

```

   "/http" : {
      "get" : {
        "responses" : { },
        "security" : [ {
          "cognito-pool" : [ ]
        } ],
        "x-amazon-apigateway-integration" : {
          "type" : "http",
          "responses" : {
            "default" : {
              "statusCode" : "200"
            }
          },
          "httpMethod" : "GET",
          "uri" : "http://api.example.com"
        }
      }
    }
```

## x-amazon-apigateway-authorizer examples for HTTP APIs

The following OpenAPI 3.0 example creates a JWT authorizer for an HTTP API
that uses Amazon Cognito as an identity provider, with the `Authorization` header as an identity source.

```
"securitySchemes": {
  "jwt-authorizer-oauth": {
    "type": "oauth2",
     "x-amazon-apigateway-authorizer": {
       "type": "jwt",
       "jwtConfiguration": {
          "issuer": "https://cognito-idp.region.amazonaws.com/userPoolId",
          "audience": [
            "audience1",
            "audience2"
          ]
        },
        "identitySource": "$request.header.Authorization"
    }
  }
}
```

The following OpenAPI 3.0 example produces the same JWT
authorizer as the previous example. However, this example uses the OpenAPI
`openIdConnectUrl` property to automatically detect the issuer. The
`openIdConnectUrl` must be fully formed.

```
"securitySchemes": {
  "jwt-authorizer-autofind": {
    "type": "openIdConnect",
    "openIdConnectUrl": "https://cognito-idp.region.amazonaws.com/userPoolId/.well-known/openid-configuration",
    "x-amazon-apigateway-authorizer": {
      "type": "jwt",
      "jwtConfiguration": {
        "audience": [
          "audience1",
          "audience2"
        ]
      },
      "identitySource": "$request.header.Authorization"
    }
  }
}

```

The following example creates a Lambda authorizer for an HTTP API. This
example authorizer uses the `Authorization` header as its identity
source. The authorizer uses the `2.0` payload format version, and returns
Boolean value, because `enableSimpleResponses` is set to `true`.

```
"securitySchemes" : {
  "lambda-authorizer" : {
    "type" : "apiKey",
    "name" : "Authorization",
    "in" : "header",
    "x-amazon-apigateway-authorizer" : {
      "type" : "request",
      "identitySource" : "$request.header.Authorization",
      "authorizerUri" : "arn:aws:apigateway:`us-west-2`:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:`function-name`/invocations",
      "authorizerPayloadFormatVersion" : "2.0",
      "authorizerResultTtlInSeconds" : 300,
      "enableSimpleResponses" : true
    }
  }
}

```
