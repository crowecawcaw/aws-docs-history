# ApiFunctionAuth

Configures authorization at the event level, for a specific API, path, and method.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
  ApiKeyRequired: `Boolean`
  AuthorizationScopes: `List`
  Authorizer: `String`
  InvokeRole: `String`
  OverrideApiAuth: `Boolean`
  ResourcePolicy: `ResourcePolicyStatement`

```

## Properties

`ApiKeyRequired`

Requires an API key for this API, path, and method.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM
and doesn't have an AWS CloudFormation equivalent.

`AuthorizationScopes`

The authorization scopes to apply to this API, path, and method.

The scopes that you specify will override any scopes applied by the
`DefaultAuthorizer` property if you have specified it.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM
and doesn't have an AWS CloudFormation equivalent.

`Authorizer`

The `Authorizer` for a specific function.

If you have a global authorizer specified for your `AWS::Serverless::Api` resource, you can override the authorizer by setting
`Authorizer` to `NONE`. For an example, see [Override a global authorizer for your Amazon API Gateway REST API](#sam-property-function-apifunctionauth--examples--override "#sam-property-function-apifunctionauth--examples--override").

###### Note

If you use the `DefinitionBody` property of an `AWS::Serverless::Api` resource to describe your API, you must use
`OverrideApiAuth` with `Authorizer` to override your global authorizer. See
`OverrideApiAuth` for more information.

_Valid values_: `AWS_IAM`, `NONE`, or the logical ID for any authorizer defined in your AWS SAM template.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM
and doesn't have an AWS CloudFormation equivalent.

`InvokeRole`

Specifies the `InvokeRole` to use for `AWS_IAM`
authorization.

_Type_: String

_Required_: No

_Default_: `CALLER_CREDENTIALS`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM
and doesn't have an AWS CloudFormation equivalent.

_Additional notes_: `CALLER_CREDENTIALS`
maps to `arn:aws:iam::`:<user>/``, which uses the caller
credentials to invoke the endpoint.

`OverrideApiAuth`

Specify as `true` to override the global authorizer configuration of your `AWS::Serverless::Api` resource. This property
is only required if you specify a global authorizer and use the `DefinitionBody` property of an `AWS::Serverless::Api` resource
to describe your API.

###### Note

When you specify `OverrideApiAuth` as `true`, AWS SAM will override your global authorizer with any values provided for
`ApiKeyRequired`, `Authorizer`, or `ResourcePolicy`. Therefore, at least one of these properties must also be specified
when using `OverrideApiAuth`. For an example, see [Override a global authorizer when DefinitionBody for AWS::Serverless::Api is specified](#sam-property-function-apifunctionauth--examples--override2 "#sam-property-function-apifunctionauth--examples--override2").

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`ResourcePolicy`

Configure Resource Policy for this path on an API.

_Type_: [ResourcePolicyStatement](sam-property-function-resourcepolicystatement.md "sam-property-function-resourcepolicystatement.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM
and doesn't have an AWS CloudFormation equivalent.

## Examples

### Function-Auth

The following example specifies authorization at the function level.

#### YAML

```
Auth:
  ApiKeyRequired: true
  Authorizer: NONE

```

### Override a global authorizer for your Amazon API Gateway REST API

You can specify a global authorizer for your `AWS::Serverless::Api` resource. The following is an example that configures a global
default authorizer:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyApiWithLambdaRequestAuth:
    Type: AWS::Serverless::Api
    Properties:
      ...
      Auth:
        Authorizers:
          MyLambdaRequestAuth:
            FunctionArn: !GetAtt MyAuthFn.Arn
        DefaultAuthorizer: MyLambdaRequestAuth
```

To override the default authorizer for your AWS Lambda function, you can specify `Authorizer` as `NONE`. The following is an example:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  ...
  MyFn:
    Type: AWS::Serverless::Function
    Properties:
      ...
      Events:
        LambdaRequest:
          Type: Api
          Properties:
            RestApiId: !Ref MyApiWithLambdaRequestAuth
            Method: GET
            Auth:
              Authorizer: NONE
```

###

Override a global authorizer when DefinitionBody for AWS::Serverless::Api is specified

When using the `DefinitionBody` property to describe your `AWS::Serverless::Api` resource, the previous override method does not work. The
following is an example of using the `DefinitionBody` property for an `AWS::Serverless::Api` resource:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyApiWithLambdaRequestAuth:
    Type: AWS::Serverless::Api
    Properties:
      ...
      DefinitionBody:
        swagger: 2.0
        ...
        paths:
          /lambda-request:
            ...
      Auth:
        Authorizers:
          MyLambdaRequestAuth:
            FunctionArn: !GetAtt MyAuthFn.Arn
        DefaultAuthorizer: MyLambdaRequestAuth
```

To override the global authorizer, use the `OverrideApiAuth` property. The following is an example that uses `OverrideApiAuth` to override the
global authorizer with the value provided for `Authorizer`:

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
...
Resources:
  MyApiWithLambdaRequestAuth:
    Type: AWS::Serverless::Api
    Properties:
      ...
      DefinitionBody:
        swagger: 2-0
        ...
        paths:
          /lambda-request:
            ...
      Auth:
        Authorizers:
          MyLambdaRequestAuth:
            FunctionArn: !GetAtt MyAuthFn.Arn
        DefaultAuthorizer: MyLambdaRequestAuth

    MyAuthFn:
      Type: AWS::Serverless::Function
      ...

    MyFn:
      Type: AWS::Serverless::Function
        Properties:
          ...
          Events:
            LambdaRequest:
              Type: Api
              Properties:
                RestApiId: !Ref MyApiWithLambdaRequestAuth
                Method: GET
                Auth:
                  Authorizer: NONE
                  OverrideApiAuth: true
                Path: /lambda-token
```
