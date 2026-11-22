

# Create a JWT authorizer for a REST API

You can create a JWT authorizer by using the API Gateway console, the AWS CLI, an AWS SDK, AWS CloudFormation, or an OpenAPI definition. Before you create a JWT authorizer, you must create a REST API. For more information, see [Tutorial: Create a REST API with a Lambda proxy integration](api-gateway-create-api-as-simple-proxy-for-lambda.md).

Collect the following values from your identity provider before you begin:
+ The issuer URL, exactly as it appears in the token's `iss` claim. The issuer must be an absolute `https` URL with no query string or fragment.
+ One or more audience values that you accept from the issuer.
+ The signing algorithms that the issuer uses.

Your identity provider must publish an OIDC discovery document at the issuer URL followed by `/.well-known/openid-configuration`, for example, `https://identity.example.com/.well-known/openid-configuration`. API Gateway reads this document when you create the authorizer. The document must be reachable from the public internet. The discovery document and the key set must use a certificate issued by a certificate authority that API Gateway supports. For the list, see [API Gateway-supported certificate authorities for HTTP and HTTP proxy integrations in API Gateway](api-gateway-supported-certificate-authorities-for-http-endpoints.md).

**Important**  
The `issuer` that you configure must match the token's `iss` claim exactly, including any trailing slash. To find the value, decode a token from your identity provider and copy its `iss` claim.

## Additional claims
<a name="rest-api-jwt-authorizer-create.claims"></a>

You can require that a token carries other claims beyond the standard claims that API Gateway validates. You can configure up to 10 claim rules for each issuer. Each rule names a claim and sets whether the claim is required and which values API Gateway accepts. A claim name must be unique within the issuer, and it cannot be `iss`, `aud`, `exp`, `nbf`, `iat`, `scope`, or `scp`. A claim rule uses the `SINGLE_STRING` format and accepts at most one expected value, which you set as the only item in `expectedValues`. API Gateway matches the value exactly, and the match is case-sensitive. If `expectedValues` contains more than one value, API Gateway returns a `400` error. A claim rule matches only a claim whose value in the token is a single string. If the token's claim is an array, such as `"groups": ["admins", "users"]`, the token fails the rule and receives a `403` response.

The combination of the `required` setting and the expected value determines how API Gateway evaluates a claim:
+ **Required, no expected value** – The token must contain the claim. API Gateway does not check its value.
+ **Required, with an expected value** – The token must contain the claim, and the value must match the expected value exactly.
+ **Not required, with an expected value** – API Gateway checks the value only when the token contains the claim.
+ **Not required, no expected value** – API Gateway doesn't check the claim.

To reject tokens that don't carry a claim, select `required`. To also check the claim's value, set an expected value.

A token that fails a claim rule receives a `403 Forbidden` response.

## Create a JWT authorizer using the console
<a name="rest-api-jwt-authorizer-create.console"></a>

The following steps show how to create a JWT authorizer by using the console.

**To create a JWT authorizer using the console**

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. Choose a REST API.

1. In the main navigation pane, choose **Authorizers**.

1. Choose **Create authorizer**.

1. For **Authorizer name**, enter a name for the authorizer.

1. For **Authorizer type**, choose **JWT**.

1. For **Identity source**, enter the request header that carries the token, for example, `Authorization`. The header value can be the token alone or the token prefixed with `Bearer`. The prefix isn't case-sensitive.

1. For **Allowed signing algorithms**, select the algorithms that you accept. API Gateway rejects tokens that are signed with any other algorithm.

1. Under **Issuers**, configure each identity provider that issues tokens for this API:

   1. For **Issuer URL**, enter the issuer that matches the token's `iss` claim. Use an absolute HTTPS URL with no query string or fragment.

   1. For **Audiences**, enter the values that you accept from the issuer as a comma-separated list. You can enter up to 100 audiences.

   1. (Optional) Add claim rules for the issuer:

      1. Expand **Additional claims - optional**, and then choose **Add additional claims**.

      1. Choose **Add claim**, and then for **Claim name**, enter the name of the claim.

      1. (Optional) Select **Required** if the claim must be present.

      1. (Optional) For **Expected value**, enter the value that the claim must have.

      1. Repeat these steps for each claim, and then choose **Save**.  
![The Additional claims dialog box with one claim rule: the claim name department, Required selected, and the expected value engineering.](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/apigateway-rest-jwt-authorizer-additional-claims.png)

   To accept tokens from more than one issuer, choose **Add issuer** and repeat this step. You can add up to 10 issuers.  
![The Create authorizer page with JWT selected as the authorizer type, showing the identity source, allowed signing algorithms, issuer URL, audiences, and additional claims fields.](https://docs.aws.amazon.com/apigateway/latest/developerguide/images/apigateway-rest-jwt-authorizer-create.png)

1. Choose **Create authorizer**.

## Create a JWT authorizer using the AWS CLI
<a name="rest-api-jwt-authorizer-create.cli"></a>

First, describe the authorizer configuration in a file. The configuration lists the trusted issuers, the audiences that you accept from each issuer, and the signing algorithms that you allow. The following example defines one issuer.

```json
{
  "issuers": [
    {
      "issuer": "https://identity.example.com",
      "audiences": ["api://orders"]
    }
  ],
  "defaultAlgorithms": ["RS256"]
}
```

To require an additional claim, add an `additionalClaims` entry to the issuer. The following issuer accepts only tokens whose `department` claim equals `eng`.

```json
{
  "issuer": "https://identity.example.com",
  "audiences": ["api://orders"],
  "additionalClaims": [
    {
      "claimName": "department",
      "format": "SINGLE_STRING",
      "required": true,
      "expectedValues": ["eng"]
    }
  ]
}
```

Next, run the [create-authorizer](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-authorizer.html) command. For the identity source, specify the request header that carries the token.

```shell
aws apigateway create-authorizer \
    --rest-api-id {{api-id}} \
    --name {{authorizer-name}} \
    --type JWT \
    --identity-source method.request.header.Authorization \
    --jwt-configuration file://jwt-config.json
```

When you create the authorizer, API Gateway reads the issuer's discovery document and records the location of its key set. For more information, see [Signing keys and troubleshooting JWT authorizers](rest-api-jwt-authorizer-keys.md).

## Create a JWT authorizer using AWS CloudFormation
<a name="rest-api-jwt-authorizer-create.cfn"></a>

In CloudFormation, the `AWS::ApiGateway::Authorizer` resource includes a `JwtConfiguration` property that mirrors the API. A method references the authorizer with `AuthorizationType: JWT`.

```YAML
Parameters:
  IdpIssuer:
    Type: String
    Description: Issuer URL exactly as it appears in the token's iss claim
  IdpAudience:
    Type: String

Resources:
  OrdersAuthorizer:
    Type: AWS::ApiGateway::Authorizer
    Properties:
      RestApiId: !Ref OrdersApi
      Name: orders-jwt
      Type: JWT
      IdentitySource: method.request.header.Authorization
      JwtConfiguration:
        DefaultAlgorithms: [RS256]
        Issuers:
          - Issuer: !Ref IdpIssuer
            Audiences: [!Ref IdpAudience]

  GetOrders:
    Type: AWS::ApiGateway::Method
    Properties:
      RestApiId: !Ref OrdersApi
      ResourceId: !Ref OrdersResource
      HttpMethod: GET
      AuthorizationType: JWT
      AuthorizerId: !GetAtt OrdersAuthorizer.AuthorizerId
      AuthorizationScopes: [orders:read]
      Integration:
        Type: MOCK
        RequestTemplates:
          application/json: '{"statusCode": 200}'
```

## Create a JWT authorizer using OpenAPI
<a name="rest-api-jwt-authorizer-create.openapi"></a>

In an OpenAPI definition, a JWT authorizer uses the `x-amazon-apigateway-authorizer` extension with `type: jwt`. The scopes that you list in each operation's `security` entry become that method's authorization scopes. For more information about the extension, see [x-amazon-apigateway-authorizer object](api-gateway-swagger-extensions-authorizer.md).

```YAML
components:
  securitySchemes:
    orders-jwt:
      type: apiKey
      name: Authorization
      in: header
      x-amazon-apigateway-authtype: jwt
      x-amazon-apigateway-authorizer:
        type: jwt
        jwtConfiguration:
          issuers:
            - issuer: https://identity.example.com
              audiences: [ "api://orders" ]
          defaultAlgorithms: [ "RS256", "ES256" ]
paths:
  /orders:
    get:
      security:
        - orders-jwt: [ "orders:read" ]
```

When you import an OpenAPI definition, API Gateway ignores the `jwksUri` field. When you export an API, API Gateway omits the `jwksUri` field.