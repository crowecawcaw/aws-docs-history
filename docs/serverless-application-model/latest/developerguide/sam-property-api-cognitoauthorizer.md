# CognitoAuthorizer

Define a Amazon Cognito User Pool authorizer.

For more information and examples, see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md "serverless-controlling-access-to-apis.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AuthorizationScopes: `List`
  Identity: `CognitoAuthorizationIdentity`
  UserPoolArn: `String`

```

## Properties

`AuthorizationScopes`

List of authorization scopes for this authorizer.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Identity`

This property can be used to specify an `IdentitySource` in an incoming request for an authorizer.

_Type_: [CognitoAuthorizationIdentity](sam-property-api-cognitoauthorizationidentity.md "sam-property-api-cognitoauthorizationidentity.md")

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`UserPoolArn`

Can refer to a user pool/specify a userpool arn to which you want to add this cognito authorizer

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### CognitoAuth

Cognito Auth Example

#### YAML

```
Auth:
  Authorizers:
    MyCognitoAuth:
      AuthorizationScopes:
        - scope1
        - scope2
      UserPoolArn:
        Fn::GetAtt:
          - MyCognitoUserPool
          - Arn
      Identity:
        Header: MyAuthorizationHeader
        ValidationExpression: myauthvalidationexpression

```
