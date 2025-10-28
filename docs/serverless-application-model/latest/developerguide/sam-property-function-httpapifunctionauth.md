# HttpApiFunctionAuth

Configures authorization at the event level.

Configure Auth for a specific API + Path + Method

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  AuthorizationScopes: `List`
  Authorizer: `String`

```

## Properties

`AuthorizationScopes`

The authorization scopes to apply to this API, path, and method.

Scopes listed here will override any scopes applied by the `DefaultAuthorizer` if one exists.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`Authorizer`

The `Authorizer` for a specific Function. To use IAM authorization, specify `AWS_IAM` and specify `true` for `EnableIamAuthorizer` in the `Globals` section of your template.

If you have specified a Global Authorizer on the API and want to make a specific Function public, override by setting `Authorizer` to `NONE`.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

## Examples

### Function-Auth

Specifing Authorization at Function level

#### YAML

```
Auth:
  Authorizer: OpenIdAuth
  AuthorizationScopes:
    - scope1
    - scope2

```

### IAM authorization

Specifies IAM authorization at the event level. To use `AWS_IAM` authorization at the event level, you must also specify `true` for `EnableIamAuthorizer` in the `Globals` section of your template. For more information, see [Globals section of the AWS SAM
template](sam-specification-template-anatomy-globals.md "sam-specification-template-anatomy-globals.md").

#### YAML

```
Globals:
  HttpApi:
    Auth:
      EnableIamAuthorizer: true

Resources:
  HttpApiFunctionWithIamAuth:
    Type: AWS::Serverless::Function
    Properties:
      Events:
        ApiEvent:
          Type: HttpApi
          Properties:
            Path: /iam-auth
            Method: GET
            Auth:
              Authorizer: AWS_IAM
      Handler: index.handler
      InlineCode: |
        def handler(event, context):
          return {'body': 'HttpApiFunctionWithIamAuth', 'statusCode': 200}
      Runtime: python3.9

```
