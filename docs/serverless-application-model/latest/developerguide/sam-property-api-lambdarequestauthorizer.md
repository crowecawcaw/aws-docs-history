

# LambdaRequestAuthorizer
<a name="sam-property-api-lambdarequestauthorizer"></a>

Configure a Lambda Authorizer to control access to your API with a Lambda function.

For more information and examples, see [Control API access with your AWS SAM template](serverless-controlling-access-to-apis.md).

## Syntax
<a name="sam-property-api-lambdarequestauthorizer-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-api-lambdarequestauthorizer-syntax.yaml"></a>

```
DisableFunctionDefaultPermissions: {{Boolean}}
[FunctionArn](#sam-api-lambdarequestauthorizer-functionarn): {{String}}
[FunctionInvokeRole](#sam-api-lambdarequestauthorizer-functioninvokerole): {{String}}
[FunctionPayloadType](#sam-api-lambdarequestauthorizer-functionpayloadtype): {{String}}
[Identity](#sam-api-lambdarequestauthorizer-identity): {{LambdaRequestAuthorizationIdentity}}
```

## Properties
<a name="sam-property-api-lambdarequestauthorizer-properties"></a>

 `DisableFunctionDefaultPermissions`   <a name="sam-api-lambdarequestauthorizer-disablefunctiondefaultpermissions"></a>
Specify `true` to prevent AWS SAM from automatically creating an `AWS::Lambda::Permissions` resource to provision permissions between your `AWS::Serverless::Api` resource and authorizer Lambda function.  
*Default value*: `false`  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `FunctionArn`   <a name="sam-api-lambdarequestauthorizer-functionarn"></a>
Specify the function ARN of the Lambda function which provides authorization for the API.  
AWS SAM will automatically create an `AWS::Lambda::Permissions` resource when `FunctionArn` is specified for `AWS::Serverless::Api`. The `AWS::Lambda::Permissions` resource provisions permissions between your API and authorizer Lambda function.
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `FunctionInvokeRole`   <a name="sam-api-lambdarequestauthorizer-functioninvokerole"></a>
Adds authorizer credentials to the OpenApi definition of the Lambda authorizer.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `FunctionPayloadType`   <a name="sam-api-lambdarequestauthorizer-functionpayloadtype"></a>
This property can be used to define the type of Lambda Authorizer for an API.  
*Valid values*: `TOKEN` or `REQUEST`  
*Type*: String  
*Required*: No  
*Default*: `TOKEN`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Identity`   <a name="sam-api-lambdarequestauthorizer-identity"></a>
This property can be used to specify an `IdentitySource` in an incoming request for an authorizer. This property is only required if the `FunctionPayloadType` property is set to `REQUEST`.  
*Type*: [LambdaRequestAuthorizationIdentity](sam-property-api-lambdarequestauthorizationidentity.md)  
*Required*: Conditional  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples
<a name="sam-property-api-lambdarequestauthorizer--examples"></a>

### LambdaRequestAuth
<a name="sam-property-api-lambdarequestauthorizer--examples--lambdarequestauth"></a>

#### YAML
<a name="sam-property-api-lambdarequestauthorizer--examples--lambdarequestauth--yaml"></a>

```
Authorizers:
  MyLambdaRequestAuth:
    FunctionPayloadType: REQUEST
    FunctionArn:
      Fn::GetAtt:
        - MyAuthFunction
        - Arn
    FunctionInvokeRole:
      Fn::GetAtt:
        - LambdaAuthInvokeRole
        - Arn
    Identity:
      Headers:
        - Authorization1
```